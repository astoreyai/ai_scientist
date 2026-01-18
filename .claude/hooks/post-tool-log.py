#!/usr/bin/env python3
"""
Post-Tool Logging Hook for Claude Code Research Assistant

Triggered: After every tool execution
Purpose: Log tool usage, auto-track large files with DVC, maintain audit trail

Input: JSON from stdin with tool execution results
Output: JSON to stdout with logging confirmation
Exit codes: 0 = success, 1 = warning (logged but with issues)

Features:
    - SQLite database logging of all tool invocations
    - Automatic DVC tracking for large files (>10MB)
    - Tool input/output recording
    - Success/failure status tracking
    - Timestamp and session tracking
    - Research phase association

Integration with .claude/settings.json:
    {
      "PostToolUse": [{
        "matcher": "",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/post-tool-log.py"}]
      }]
    }
"""

import os
import sys
import json
import sqlite3
from pathlib import Path
from typing import Dict, Optional, List
import logging
from datetime import datetime
import hashlib
import subprocess

# ============================================
# CONFIGURATION
# ============================================

PROJECT_DIR = Path(os.getenv("CLAUDE_PROJECT_DIR", os.getcwd()))
CLAUDE_DIR = PROJECT_DIR / ".claude"
LOG_FILE = CLAUDE_DIR / "post-tool.log"
DB_FILE = CLAUDE_DIR / "tool_log.db"

# DVC auto-tracking threshold (10MB)
DVC_THRESHOLD_BYTES = 10 * 1024 * 1024

# Ensure log directory exists
CLAUDE_DIR.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr)
    ]
)
logger = logging.getLogger(__name__)

# ============================================
# DATABASE INITIALIZATION
# ============================================

def initialize_database():
    """Create tool log database schema if not exists"""

    schema_sql = """
    CREATE TABLE IF NOT EXISTS tool_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        session_id TEXT,
        tool_name TEXT NOT NULL,
        status TEXT NOT NULL,
        input_data TEXT,
        output_data TEXT,
        output_hash TEXT,
        error TEXT,
        duration_ms INTEGER,
        phase TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );

    CREATE INDEX IF NOT EXISTS idx_tool_log_timestamp ON tool_log(timestamp);
    CREATE INDEX IF NOT EXISTS idx_tool_log_tool_name ON tool_log(tool_name);
    CREATE INDEX IF NOT EXISTS idx_tool_log_status ON tool_log(status);
    CREATE INDEX IF NOT EXISTS idx_tool_log_session ON tool_log(session_id);

    CREATE TABLE IF NOT EXISTS file_tracking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT UNIQUE NOT NULL,
        size_bytes INTEGER,
        dvc_tracked BOOLEAN DEFAULT 0,
        first_seen TEXT NOT NULL,
        last_modified TEXT NOT NULL,
        checksum TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_file_tracking_path ON file_tracking(file_path);
    CREATE INDEX IF NOT EXISTS idx_file_tracking_dvc ON file_tracking(dvc_tracked);
    """

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.executescript(schema_sql)
        conn.commit()
        conn.close()
        logger.info("Tool log database initialized")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


# ============================================
# LOGGING FUNCTIONS
# ============================================

def get_session_id() -> str:
    """Get current session ID from state file"""

    state_file = CLAUDE_DIR / "session_state.json"

    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                state = json.load(f)
                return state.get("session_id", "unknown")
        except Exception:
            pass

    return "unknown"


def get_current_phase() -> str:
    """Get current research phase from state file"""

    state_file = CLAUDE_DIR / "session_state.json"

    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                state = json.load(f)
                return state.get("current_phase", "unknown")
        except Exception:
            pass

    return "unknown"


def compute_output_hash(output_data: Dict) -> str:
    """Compute hash of output data for deduplication"""

    try:
        output_str = json.dumps(output_data, sort_keys=True)
        return hashlib.sha256(output_str.encode()).hexdigest()[:16]
    except Exception:
        return "error"


def log_tool_use(tool_data: Dict) -> bool:
    """
    Log tool usage to SQLite database

    Args:
        tool_data: Tool execution data from hook

    Returns:
        True if logged successfully, False otherwise
    """

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Extract tool information
        tool_name = tool_data.get("name", "unknown")
        status = tool_data.get("status", "unknown")
        input_data = json.dumps(tool_data.get("input", {}))
        output_data = tool_data.get("output", {})
        error = tool_data.get("error")
        duration_ms = tool_data.get("duration_ms")

        # Compute output hash
        output_hash = compute_output_hash(output_data)

        # Get session and phase
        session_id = get_session_id()
        phase = get_current_phase()

        # Truncate large outputs for storage
        output_str = json.dumps(output_data)
        if len(output_str) > 10000:
            output_str = output_str[:10000] + "... [truncated]"

        # Insert log entry
        cursor.execute("""
            INSERT INTO tool_log (
                timestamp, session_id, tool_name, status,
                input_data, output_data, output_hash, error,
                duration_ms, phase
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            session_id,
            tool_name,
            status,
            input_data,
            output_str,
            output_hash,
            error,
            duration_ms,
            phase
        ))

        conn.commit()
        conn.close()

        logger.info(f"Logged {tool_name} execution: {status}")
        return True

    except Exception as e:
        logger.error(f"Failed to log tool use: {e}")
        return False


# ============================================
# DVC AUTO-TRACKING
# ============================================

def is_dvc_available() -> bool:
    """Check if DVC is installed and available"""

    try:
        result = subprocess.run(
            ["dvc", "version"],
            capture_output=True,
            timeout=2
        )
        return result.returncode == 0
    except Exception:
        return False


def check_and_track_files(tool_data: Dict) -> List[str]:
    """
    Check if tool created/modified large files and auto-track with DVC

    Args:
        tool_data: Tool execution data

    Returns:
        List of files that were tracked with DVC
    """

    tracked_files = []
    tool_name = tool_data.get("name", "")

    # Only track for Write and Edit tools
    if tool_name not in ["Write", "Edit"]:
        return tracked_files

    # Get file path from input
    file_path_str = tool_data.get("input", {}).get("file_path")
    if not file_path_str:
        return tracked_files

    try:
        file_path = Path(file_path_str)

        # Check if file exists and is large enough
        if not file_path.exists() or not file_path.is_file():
            return tracked_files

        file_size = file_path.stat().st_size

        if file_size < DVC_THRESHOLD_BYTES:
            return tracked_files

        # Check if DVC is available
        if not is_dvc_available():
            logger.warning(f"Large file created ({file_size / 1024 / 1024:.1f}MB) but DVC not available: {file_path}")
            return tracked_files

        # Check if already tracked
        dvc_file = Path(str(file_path) + ".dvc")
        if dvc_file.exists():
            logger.info(f"File already DVC tracked: {file_path}")
            return tracked_files

        # Track with DVC
        logger.info(f"Auto-tracking large file ({file_size / 1024 / 1024:.1f}MB) with DVC: {file_path}")

        result = subprocess.run(
            ["dvc", "add", str(file_path)],
            cwd=PROJECT_DIR,
            capture_output=True,
            timeout=30
        )

        if result.returncode == 0:
            tracked_files.append(str(file_path))
            logger.info(f"Successfully tracked with DVC: {file_path}")

            # Update database
            update_file_tracking(file_path, file_size, dvc_tracked=True)

            # Stage DVC file in git
            try:
                subprocess.run(
                    ["git", "add", str(dvc_file), ".gitignore"],
                    cwd=PROJECT_DIR,
                    capture_output=True,
                    timeout=5
                )
                logger.info(f"Staged DVC file in git: {dvc_file}")
            except Exception as e:
                logger.warning(f"Failed to stage DVC file: {e}")
        else:
            logger.error(f"DVC tracking failed: {result.stderr.decode()}")

    except Exception as e:
        logger.error(f"Error in DVC auto-tracking: {e}")

    return tracked_files


def update_file_tracking(file_path: Path, size_bytes: int, dvc_tracked: bool = False):
    """Update file tracking database"""

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Compute checksum for small files
        checksum = None
        if size_bytes < 1024 * 1024:  # Only for files < 1MB
            try:
                with open(file_path, 'rb') as f:
                    checksum = hashlib.md5(f.read()).hexdigest()
            except Exception:
                pass

        # Insert or update
        cursor.execute("""
            INSERT INTO file_tracking (
                file_path, size_bytes, dvc_tracked, first_seen, last_modified, checksum
            )
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(file_path) DO UPDATE SET
                size_bytes = excluded.size_bytes,
                dvc_tracked = excluded.dvc_tracked,
                last_modified = excluded.last_modified,
                checksum = excluded.checksum
        """, (
            str(file_path),
            size_bytes,
            1 if dvc_tracked else 0,
            datetime.now().isoformat(),
            datetime.now().isoformat(),
            checksum
        ))

        conn.commit()
        conn.close()

    except Exception as e:
        logger.error(f"Failed to update file tracking: {e}")


# ============================================
# MAIN HOOK LOGIC
# ============================================

def main():
    """Main hook execution"""

    try:
        # Initialize database
        initialize_database()

        # Read input from stdin
        input_data = json.loads(sys.stdin.read())

        logger.info(f"Logging tool execution: {input_data.get('name', 'unknown')}")

        # Log the tool use
        log_success = log_tool_use(input_data)

        # Check and track large files with DVC
        tracked_files = check_and_track_files(input_data)

        # Prepare response
        response = {
            "status": "success" if log_success else "warning",
            "logged": log_success,
            "timestamp": datetime.now().isoformat(),
            "tool": input_data.get("name", "unknown"),
            "dvc_tracked_files": tracked_files
        }

        if tracked_files:
            response["message"] = f"Auto-tracked {len(tracked_files)} large file(s) with DVC"

        # Output JSON response
        print(json.dumps(response, indent=2))

        # Exit with appropriate code
        sys.exit(0 if log_success else 1)

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse input JSON: {e}")
        print(json.dumps({
            "status": "error",
            "logged": False,
            "error": "Invalid input format"
        }), file=sys.stdout)
        sys.exit(1)

    except Exception as e:
        logger.error(f"Post-tool hook failed: {e}", exc_info=True)
        print(json.dumps({
            "status": "error",
            "logged": False,
            "error": str(e)
        }), file=sys.stdout)
        sys.exit(1)


if __name__ == "__main__":
    main()
