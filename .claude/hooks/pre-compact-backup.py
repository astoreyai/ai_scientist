#!/usr/bin/env python3
"""
Pre-Compact Backup Hook for Claude Code Research Assistant

Triggered: Before context compaction/summarization
Purpose: Backup critical research state before losing conversation history

Input: JSON from stdin with compaction event information
Output: JSON to stdout with backup confirmation
Exit codes: 0 = success, 1 = warning (partial backup), 2 = failure

Backs up:
    - Research state (hypotheses, decisions, current phase)
    - Tool log database
    - Session state
    - Important conversation context
    - Timestamp-stamped versioned backups

Integration with .claude/settings.json:
    {
      "PreCompact": [{
        "matcher": "",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/pre-compact-backup.py"}]
      }]
    }
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import logging
from datetime import datetime
import sqlite3

# ============================================
# CONFIGURATION
# ============================================

PROJECT_DIR = Path(os.getenv("CLAUDE_PROJECT_DIR", os.getcwd()))
CLAUDE_DIR = PROJECT_DIR / ".claude"
BACKUP_DIR = CLAUDE_DIR / "backups"
LOG_FILE = CLAUDE_DIR / "pre-compact.log"

# Files to backup
BACKUP_FILES = [
    "session_state.json",
    "tool_log.db",
    "session.log",
    "security.log",
    "post-tool.log",
]

# Research artifact paths to check
RESEARCH_PATHS = [
    "docs/problem_statement.md",
    "docs/search_strategy.md",
    "docs/gap_analysis.md",
    "docs/hypotheses.md",
    "docs/experimental_protocol.md",
]

# Ensure directories exist
CLAUDE_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

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
# BACKUP FUNCTIONS
# ============================================

def get_timestamp() -> str:
    """Get formatted timestamp for backup filenames"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def backup_file(source: Path, backup_dir: Path, timestamp: str) -> bool:
    """
    Backup a single file with timestamp

    Args:
        source: Source file path
        backup_dir: Backup directory
        timestamp: Timestamp string for filename

    Returns:
        True if backed up successfully
    """

    try:
        if not source.exists():
            logger.warning(f"File not found, skipping: {source}")
            return False

        # Create backup filename
        backup_name = f"{source.name}.{timestamp}"
        backup_path = backup_dir / backup_name

        # Copy file
        shutil.copy2(source, backup_path)
        logger.info(f"Backed up: {source.name} -> {backup_name}")

        return True

    except Exception as e:
        logger.error(f"Failed to backup {source}: {e}")
        return False


def extract_tool_log_summary() -> Dict:
    """
    Extract summary statistics from tool log database

    Returns:
        Dictionary with tool usage summary
    """

    db_file = CLAUDE_DIR / "tool_log.db"

    if not db_file.exists():
        return {"error": "Tool log database not found"}

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Get tool usage counts
        cursor.execute("""
            SELECT tool_name, COUNT(*) as count
            FROM tool_log
            GROUP BY tool_name
            ORDER BY count DESC
        """)
        tool_counts = dict(cursor.fetchall())

        # Get recent tools
        cursor.execute("""
            SELECT tool_name, timestamp, status
            FROM tool_log
            ORDER BY timestamp DESC
            LIMIT 20
        """)
        recent_tools = [
            {"tool": row[0], "timestamp": row[1], "status": row[2]}
            for row in cursor.fetchall()
        ]

        # Get status breakdown
        cursor.execute("""
            SELECT status, COUNT(*) as count
            FROM tool_log
            GROUP BY status
        """)
        status_counts = dict(cursor.fetchall())

        conn.close()

        return {
            "tool_counts": tool_counts,
            "recent_tools": recent_tools,
            "status_counts": status_counts,
            "total_invocations": sum(tool_counts.values())
        }

    except Exception as e:
        logger.error(f"Failed to extract tool log summary: {e}")
        return {"error": str(e)}


def load_session_state() -> Dict:
    """Load current session state"""

    state_file = CLAUDE_DIR / "session_state.json"

    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load session state: {e}")
            return {"error": str(e)}

    return {"status": "no_state_file"}


def check_research_artifacts() -> Dict:
    """
    Check which research artifacts exist

    Returns:
        Dictionary with artifact status
    """

    artifacts = {}

    for path_str in RESEARCH_PATHS:
        path = PROJECT_DIR / path_str
        artifacts[path_str] = {
            "exists": path.exists(),
            "size": path.stat().st_size if path.exists() else 0,
            "modified": path.stat().st_mtime if path.exists() else None
        }

    return artifacts


def create_state_snapshot(timestamp: str) -> Dict:
    """
    Create comprehensive state snapshot

    Args:
        timestamp: Timestamp string

    Returns:
        Dictionary with complete state information
    """

    snapshot = {
        "timestamp": timestamp,
        "datetime": datetime.now().isoformat(),
        "session_state": load_session_state(),
        "tool_log_summary": extract_tool_log_summary(),
        "research_artifacts": check_research_artifacts(),
        "project_dir": str(PROJECT_DIR),
    }

    return snapshot


def save_state_snapshot(snapshot: Dict, timestamp: str) -> bool:
    """
    Save state snapshot to JSON file

    Args:
        snapshot: State snapshot dictionary
        timestamp: Timestamp string

    Returns:
        True if saved successfully
    """

    try:
        snapshot_file = BACKUP_DIR / f"state_snapshot_{timestamp}.json"

        with open(snapshot_file, 'w') as f:
            json.dump(snapshot, f, indent=2)

        logger.info(f"Saved state snapshot: {snapshot_file.name}")
        return True

    except Exception as e:
        logger.error(f"Failed to save state snapshot: {e}")
        return False


def cleanup_old_backups(keep_count: int = 10):
    """
    Clean up old backups, keeping only most recent N

    Args:
        keep_count: Number of recent backups to keep
    """

    try:
        # Get all backup files
        backup_files = sorted(
            BACKUP_DIR.glob("state_snapshot_*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )

        # Delete old backups
        deleted = 0
        for backup_file in backup_files[keep_count:]:
            try:
                backup_file.unlink()
                deleted += 1
            except Exception as e:
                logger.warning(f"Failed to delete old backup {backup_file}: {e}")

        if deleted > 0:
            logger.info(f"Cleaned up {deleted} old backup(s)")

    except Exception as e:
        logger.error(f"Failed to cleanup old backups: {e}")


# ============================================
# MAIN HOOK LOGIC
# ============================================

def main():
    """Main hook execution"""

    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())

        logger.info("=== PRE-COMPACT BACKUP INITIATED ===")
        logger.info(f"Compaction event: {input_data.get('event', 'unknown')}")

        timestamp = get_timestamp()
        backed_up = []
        failed = []

        # Backup individual files
        for filename in BACKUP_FILES:
            source = CLAUDE_DIR / filename
            if backup_file(source, BACKUP_DIR, timestamp):
                backed_up.append(filename)
            else:
                failed.append(filename)

        # Create and save state snapshot
        snapshot = create_state_snapshot(timestamp)
        snapshot_saved = save_state_snapshot(snapshot, timestamp)

        if snapshot_saved:
            backed_up.append("state_snapshot.json")

        # Cleanup old backups
        cleanup_old_backups(keep_count=10)

        # Determine exit code
        if not backed_up:
            status = "failure"
            exit_code = 2
        elif failed:
            status = "partial"
            exit_code = 1
        else:
            status = "success"
            exit_code = 0

        # Prepare response
        response = {
            "status": status,
            "timestamp": timestamp,
            "backed_up": backed_up,
            "failed": failed,
            "backup_dir": str(BACKUP_DIR),
            "snapshot": {
                "session_state": snapshot.get("session_state", {}),
                "tool_invocations": snapshot.get("tool_log_summary", {}).get("total_invocations", 0),
                "research_artifacts_found": sum(
                    1 for a in snapshot.get("research_artifacts", {}).values() if a.get("exists")
                )
            }
        }

        # Add user message for important backups
        if snapshot.get("session_state", {}).get("current_phase") != "initialization":
            response["user_message"] = (
                f"📦 Pre-Compaction Backup Complete\n\n"
                f"Backed up {len(backed_up)} file(s) to .claude/backups/\n"
                f"Timestamp: {timestamp}\n\n"
                f"Current phase: {snapshot.get('session_state', {}).get('current_phase', 'unknown')}\n"
                f"Tool invocations: {snapshot.get('tool_log_summary', {}).get('total_invocations', 0)}\n"
                f"Research artifacts: {response['snapshot']['research_artifacts_found']}\n\n"
                f"Context compaction will now proceed."
            )

        # Output JSON response
        print(json.dumps(response, indent=2))

        logger.info(f"=== BACKUP COMPLETE: {status.upper()} ===")
        logger.info(f"Files backed up: {len(backed_up)}, Failed: {len(failed)}")

        # Exit with appropriate code
        sys.exit(exit_code)

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse input JSON: {e}")
        print(json.dumps({
            "status": "error",
            "error": "Invalid input format"
        }), file=sys.stdout)
        sys.exit(2)

    except Exception as e:
        logger.error(f"Pre-compact hook failed: {e}", exc_info=True)
        print(json.dumps({
            "status": "error",
            "error": str(e)
        }), file=sys.stdout)
        sys.exit(2)


if __name__ == "__main__":
    main()
