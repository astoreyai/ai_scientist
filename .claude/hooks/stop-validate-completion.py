#!/usr/bin/env python3
"""
Stop Validation Hook for Claude Code Research Assistant

Triggered: When Claude Code session stops
Purpose: Validate deliverables, quality gates, and completion criteria

Input: JSON from stdin with session stop information
Output: JSON to stdout with validation results
Exit codes: 0 = all validations passed, 1 = warnings, 2 = critical failures

Validates:
    - Phase-specific deliverables completed
    - Quality gates passed (PRISMA, NIH rigor)
    - Required files generated
    - Git commit status
    - DVC data tracking
    - Documentation completeness

Integration with .claude/settings.json:
    {
      "Stop": [{
        "matcher": "",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/stop-validate-completion.py"}]
      }]
    }
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging
from datetime import datetime
import subprocess
import sqlite3

# ============================================
# CONFIGURATION
# ============================================

PROJECT_DIR = Path(os.getenv("CLAUDE_PROJECT_DIR", os.getcwd()))
CLAUDE_DIR = PROJECT_DIR / ".claude"
LOG_FILE = CLAUDE_DIR / "stop-validation.log"

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
# PHASE VALIDATION RULES
# ============================================

# Required deliverables for each phase
PHASE_DELIVERABLES = {
    "problem_formulation": [
        "docs/problem_statement.md",
    ],
    "literature_review": [
        "docs/search_strategy.md",
        "data/literature/search_results.csv",
    ],
    "gap_analysis": [
        "docs/gap_analysis.md",
    ],
    "hypothesis_formation": [
        "docs/hypotheses.md",
    ],
    "experimental_design": [
        "docs/experimental_protocol.md",
    ],
    "data_collection": [
        "data/raw/",
    ],
    "analysis": [
        "code/analysis/primary_analysis.py",
        "results/primary_results.json",
    ],
    "interpretation": [
        "results/",
    ],
    "writing": [
        "docs/manuscript/",
    ],
    "publication": [
        "docs/manuscript/final_manuscript.md",
    ],
}

# Quality gates for each phase
PHASE_QUALITY_GATES = {
    "problem_formulation": {
        "finer_criteria": "FINER criteria validated",
    },
    "literature_review": {
        "prisma_checklist": "PRISMA 2020 checklist ≥24/27",
        "inter_rater_reliability": "Cohen's κ > 0.6",
    },
    "experimental_design": {
        "power_analysis": "Power ≥80%",
        "nih_rigor": "NIH rigor checklist ≥90%",
    },
    "analysis": {
        "reproducibility": "Analysis executable in clean environment",
        "effect_sizes": "All effects reported with 95% CI",
    },
}

# ============================================
# VALIDATION FUNCTIONS
# ============================================

def load_session_state() -> Dict:
    """Load current session state"""

    state_file = CLAUDE_DIR / "session_state.json"

    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load session state: {e}")
            return {}

    return {}


def validate_phase_deliverables(phase: str) -> Tuple[List[str], List[str]]:
    """
    Validate required deliverables for a phase

    Args:
        phase: Current research phase

    Returns:
        (present_deliverables, missing_deliverables) tuple
    """

    required = PHASE_DELIVERABLES.get(phase, [])
    present = []
    missing = []

    for deliverable in required:
        path = PROJECT_DIR / deliverable

        # Check if it's a directory or file
        if deliverable.endswith("/"):
            # Directory check
            if path.exists() and path.is_dir():
                # Check if directory has content
                if any(path.iterdir()):
                    present.append(deliverable)
                else:
                    missing.append(deliverable + " (empty)")
            else:
                missing.append(deliverable)
        else:
            # File check
            if path.exists() and path.is_file():
                present.append(deliverable)
            else:
                missing.append(deliverable)

    return present, missing


def check_git_status() -> Dict:
    """
    Check git repository status

    Returns:
        Dictionary with git status information
    """

    try:
        # Check if git repo
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=PROJECT_DIR,
            capture_output=True,
            timeout=5
        )

        if result.returncode != 0:
            return {"status": "not_a_repo"}

        # Get uncommitted changes
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=PROJECT_DIR,
            capture_output=True,
            timeout=5
        )

        uncommitted = result.stdout.decode().strip().split("\n") if result.stdout else []
        uncommitted = [line for line in uncommitted if line]

        # Get current branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=PROJECT_DIR,
            capture_output=True,
            timeout=5
        )
        branch = result.stdout.decode().strip()

        # Get last commit
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H %s"],
            cwd=PROJECT_DIR,
            capture_output=True,
            timeout=5
        )
        last_commit = result.stdout.decode().strip()

        return {
            "status": "clean" if not uncommitted else "uncommitted_changes",
            "branch": branch,
            "uncommitted_count": len(uncommitted),
            "uncommitted_files": uncommitted[:10],  # Limit to 10
            "last_commit": last_commit
        }

    except Exception as e:
        logger.error(f"Failed to check git status: {e}")
        return {"status": "error", "error": str(e)}


def check_dvc_status() -> Dict:
    """
    Check DVC tracking status

    Returns:
        Dictionary with DVC status information
    """

    try:
        # Check if DVC is available
        result = subprocess.run(
            ["dvc", "status"],
            cwd=PROJECT_DIR,
            capture_output=True,
            timeout=10
        )

        if result.returncode != 0:
            return {"status": "not_initialized"}

        status_output = result.stdout.decode().strip()

        if not status_output:
            return {"status": "clean"}

        return {
            "status": "uncommitted_changes",
            "output": status_output[:500]  # Truncate
        }

    except FileNotFoundError:
        return {"status": "not_installed"}
    except Exception as e:
        logger.error(f"Failed to check DVC status: {e}")
        return {"status": "error", "error": str(e)}


def get_tool_usage_stats() -> Dict:
    """
    Get tool usage statistics from database

    Returns:
        Dictionary with tool usage stats
    """

    db_file = CLAUDE_DIR / "tool_log.db"

    if not db_file.exists():
        return {"status": "no_database"}

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Get total tool invocations
        cursor.execute("SELECT COUNT(*) FROM tool_log")
        total = cursor.fetchone()[0]

        # Get tool breakdown
        cursor.execute("""
            SELECT tool_name, COUNT(*) as count
            FROM tool_log
            GROUP BY tool_name
            ORDER BY count DESC
            LIMIT 10
        """)
        tool_counts = dict(cursor.fetchall())

        # Get success rate
        cursor.execute("""
            SELECT status, COUNT(*) as count
            FROM tool_log
            GROUP BY status
        """)
        status_counts = dict(cursor.fetchall())

        conn.close()

        return {
            "status": "available",
            "total_invocations": total,
            "tool_breakdown": tool_counts,
            "status_breakdown": status_counts
        }

    except Exception as e:
        logger.error(f"Failed to get tool usage stats: {e}")
        return {"status": "error", "error": str(e)}


def validate_quality_gates(phase: str) -> Dict:
    """
    Validate quality gates for a phase

    Args:
        phase: Current research phase

    Returns:
        Dictionary with quality gate validation results
    """

    gates = PHASE_QUALITY_GATES.get(phase, {})
    results = {}

    for gate_name, gate_description in gates.items():
        # For now, mark as "not_checked" since we need specific checkers
        # In production, these would check actual compliance
        results[gate_name] = {
            "description": gate_description,
            "status": "not_checked",
            "note": "Manual verification required"
        }

    return results


def generate_session_summary(state: Dict, validations: Dict) -> str:
    """
    Generate human-readable session summary

    Args:
        state: Session state
        validations: Validation results

    Returns:
        Formatted summary string
    """

    phase = state.get("current_phase", "unknown")
    mode = state.get("mode", "unknown")

    summary_parts = [
        "📋 Session Completion Summary",
        "",
        f"Mode: {mode}",
        f"Phase: {phase}",
        f"Started: {state.get('started_at', 'unknown')}",
        f"Duration: {state.get('duration', 'unknown')}",
        "",
        "Deliverables:",
    ]

    present = validations.get("deliverables", {}).get("present", [])
    missing = validations.get("deliverables", {}).get("missing", [])

    if present:
        summary_parts.append(f"  ✅ {len(present)} present: {', '.join(present[:3])}")
    if missing:
        summary_parts.append(f"  ⚠️  {len(missing)} missing: {', '.join(missing[:3])}")

    summary_parts.append("")
    summary_parts.append("Tool Usage:")
    tool_stats = validations.get("tool_usage", {})
    if tool_stats.get("total_invocations"):
        summary_parts.append(f"  Total invocations: {tool_stats['total_invocations']}")

    summary_parts.append("")
    summary_parts.append("Version Control:")
    git_status = validations.get("git_status", {})
    if git_status.get("status") == "clean":
        summary_parts.append("  ✅ All changes committed")
    elif git_status.get("uncommitted_count", 0) > 0:
        summary_parts.append(f"  ⚠️  {git_status['uncommitted_count']} uncommitted changes")

    return "\n".join(summary_parts)


# ============================================
# MAIN HOOK LOGIC
# ============================================

def main():
    """Main hook execution"""

    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())

        logger.info("=== STOP VALIDATION INITIATED ===")

        # Load session state
        state = load_session_state()
        phase = state.get("current_phase", "unknown")
        mode = state.get("mode", "ASSISTANT")

        logger.info(f"Phase: {phase}, Mode: {mode}")

        # Run validations
        validations = {}

        # 1. Validate deliverables
        present, missing = validate_phase_deliverables(phase)
        validations["deliverables"] = {
            "present": present,
            "missing": missing,
            "present_count": len(present),
            "missing_count": len(missing)
        }

        # 2. Check quality gates
        validations["quality_gates"] = validate_quality_gates(phase)

        # 3. Check git status
        validations["git_status"] = check_git_status()

        # 4. Check DVC status
        validations["dvc_status"] = check_dvc_status()

        # 5. Get tool usage stats
        validations["tool_usage"] = get_tool_usage_stats()

        # Determine overall status
        critical_failures = []
        warnings = []

        if missing:
            warnings.append(f"{len(missing)} deliverable(s) missing")

        if validations["git_status"].get("uncommitted_count", 0) > 0:
            warnings.append("Uncommitted changes in git")

        if validations["dvc_status"].get("status") == "uncommitted_changes":
            warnings.append("Uncommitted DVC changes")

        # Determine exit code
        if critical_failures:
            status = "failure"
            exit_code = 2
        elif warnings:
            status = "warnings"
            exit_code = 1
        else:
            status = "success"
            exit_code = 0

        # Generate response
        response = {
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "phase": phase,
            "mode": mode,
            "validations": validations,
            "critical_failures": critical_failures,
            "warnings": warnings,
        }

        # Add user message
        response["user_message"] = generate_session_summary(state, validations)

        # Output JSON response
        print(json.dumps(response, indent=2))

        logger.info(f"=== VALIDATION COMPLETE: {status.upper()} ===")
        logger.info(f"Warnings: {len(warnings)}, Failures: {len(critical_failures)}")

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
        logger.error(f"Stop validation hook failed: {e}", exc_info=True)
        print(json.dumps({
            "status": "error",
            "error": str(e)
        }), file=sys.stdout)
        sys.exit(2)


if __name__ == "__main__":
    main()
