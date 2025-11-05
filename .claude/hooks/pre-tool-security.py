#!/usr/bin/env python3
"""
Pre-Tool Security Hook for Claude Code Research Assistant

Triggered: Before bash commands and file operations
Purpose: Validate commands and file paths for security vulnerabilities

Input: JSON from stdin with tool use information
Output: JSON to stdout with validation decision
Exit codes:
    0 = Approve (safe to execute)
    1 = Warning (log but allow)
    2 = Block (prevent execution)

Security Checks:
    - Dangerous bash commands (rm -rf /, dd, mkfs, etc.)
    - Path traversal attempts (../, /etc/, /sys/, etc.)
    - Privilege escalation (sudo, su, etc.)
    - Network access validation
    - File system boundary enforcement

Integration with .claude/settings.json:
    {
      "PreToolUse": [{
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/pre-tool-security.py", "timeout": 5}]
      }]
    }
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
import logging
from datetime import datetime

# ============================================
# CONFIGURATION
# ============================================

PROJECT_DIR = Path(os.getenv("CLAUDE_PROJECT_DIR", os.getcwd()))
CLAUDE_DIR = PROJECT_DIR / ".claude"
LOG_FILE = CLAUDE_DIR / "security.log"

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
# SECURITY RULES
# ============================================

# Commands that are ALWAYS blocked
BLOCKED_COMMANDS = {
    # Destructive operations
    "rm -rf /",
    "rm -fr /",
    "rm -rf /*",
    "rm -fr /*",
    "> /dev/sda",
    "dd if=/dev/zero",
    "dd if=/dev/random",
    "mkfs",
    "mkfs.ext4",
    "mkfs.xfs",
    "fdisk",
    "parted",

    # Fork bombs
    ":(){ :|:& };:",

    # Kernel/system manipulation
    "echo 1 > /proc/sys/kernel/panic",

    # Mass file operations
    "find / -delete",
    "find / -exec rm",
}

# Command patterns that are blocked (regex)
BLOCKED_PATTERNS = [
    r"rm\s+-rf\s+/\s*$",                    # rm -rf / variants
    r"chmod\s+-R\s+777\s+/",                # Recursive 777 on root
    r"chown\s+-R\s+.*\s+/\s*$",             # Recursive chown on root
    r"dd\s+if=/dev/(zero|random|urandom)",  # DD to devices
    r":\(\)\{.*:\|:&\s*\};:",               # Fork bomb variants
    r"curl.*\|\s*bash",                     # Pipe curl to bash (potential malware)
    r"wget.*\|\s*bash",                     # Pipe wget to bash
    r"bash\s+-i\s*>&\s*/dev/tcp",           # Reverse shell
    r"/dev/tcp/.*bash",                     # TCP reverse shell
]

# Dangerous command keywords (require review)
DANGEROUS_KEYWORDS = [
    "sudo", "su", "doas",                   # Privilege escalation
    "passwd", "usermod", "useradd",         # User management
    "iptables", "ufw", "firewall-cmd",      # Firewall
    "systemctl", "service",                 # Service management
    "shutdown", "reboot", "halt", "poweroff",  # System control
    "kill -9", "killall",                   # Process killing
]

# Protected paths (cannot be modified/deleted)
PROTECTED_PATHS = [
    "/bin", "/sbin", "/usr/bin", "/usr/sbin",
    "/etc", "/boot", "/sys", "/proc", "/dev",
    "/lib", "/lib64", "/usr/lib", "/usr/lib64",
    "/root", "/var/log",
]

# Allowed base directories for file operations
ALLOWED_BASES = [
    PROJECT_DIR,
    Path.home() / ".cache",
    Path.home() / ".config",
    Path("/tmp"),
    Path("/var/tmp"),
]

# ============================================
# VALIDATION FUNCTIONS
# ============================================

def check_command_safety(command: str) -> Tuple[str, str, int]:
    """
    Check if a bash command is safe to execute

    Args:
        command: Bash command string

    Returns:
        (decision, reason, exit_code) tuple
        - decision: "approve", "warn", or "block"
        - reason: Human-readable explanation
        - exit_code: 0=approve, 1=warn, 2=block
    """

    # Check for exact blocked commands
    command_clean = command.strip()
    if command_clean in BLOCKED_COMMANDS:
        return ("block", f"Blocked command detected: {command_clean}", 2)

    # Check for blocked patterns
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return ("block", f"Blocked pattern matched: {pattern}", 2)

    # Check for dangerous keywords (warn but allow)
    for keyword in DANGEROUS_KEYWORDS:
        if keyword in command:
            return ("warn", f"Dangerous keyword detected: {keyword}", 1)

    # Check for protected path access
    for protected in PROTECTED_PATHS:
        if protected in command and any(op in command for op in ["rm", "rmdir", "mv", "chmod", "chown"]):
            return ("block", f"Attempt to modify protected path: {protected}", 2)

    # Default: approve
    return ("approve", "Command passed security checks", 0)


def check_path_safety(file_path: str) -> Tuple[str, str, int]:
    """
    Check if a file path is safe to access

    Args:
        file_path: File path string

    Returns:
        (decision, reason, exit_code) tuple
    """

    try:
        path = Path(file_path).resolve()
    except (ValueError, OSError) as e:
        return ("block", f"Invalid path: {e}", 2)

    # Check for path traversal to protected areas
    for protected in PROTECTED_PATHS:
        protected_path = Path(protected).resolve()
        try:
            path.relative_to(protected_path)
            return ("block", f"Access to protected system path: {protected}", 2)
        except ValueError:
            # Not a subpath, continue checking
            pass

    # Check if path is within allowed bases
    is_allowed = False
    for allowed_base in ALLOWED_BASES:
        try:
            allowed_base_resolved = allowed_base.resolve()
            path.relative_to(allowed_base_resolved)
            is_allowed = True
            break
        except ValueError:
            continue

    if not is_allowed:
        return ("warn", f"Path outside typical project boundaries: {path}", 1)

    return ("approve", "Path passed security checks", 0)


def validate_tool_use(tool_data: Dict) -> Tuple[str, str, int]:
    """
    Validate tool use for security

    Args:
        tool_data: Tool use information from Claude Code hook

    Returns:
        (decision, reason, exit_code) tuple
    """

    tool_name = tool_data.get("name", "unknown")

    if tool_name == "Bash":
        # Validate bash command
        command = tool_data.get("input", {}).get("command", "")
        return check_command_safety(command)

    elif tool_name in ["Write", "Edit"]:
        # Validate file path
        file_path = tool_data.get("input", {}).get("file_path", "")
        return check_path_safety(file_path)

    elif tool_name == "Read":
        # Read is generally safe, but check for sensitive paths
        file_path = tool_data.get("input", {}).get("file_path", "")

        # Block reading of sensitive files
        sensitive_files = ["/etc/shadow", "/etc/passwd", "/root/.ssh/id_rsa"]
        if any(sensitive in file_path for sensitive in sensitive_files):
            return ("block", f"Attempt to read sensitive file: {file_path}", 2)

        return ("approve", "Read operation approved", 0)

    else:
        # Other tools are generally safe
        return ("approve", f"Tool {tool_name} approved", 0)


# ============================================
# MAIN HOOK LOGIC
# ============================================

def main():
    """Main hook execution"""

    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())

        logger.info(f"Security validation triggered for tool: {input_data.get('name', 'unknown')}")

        # Validate the tool use
        decision, reason, exit_code = validate_tool_use(input_data)

        # Log the decision
        log_level = {
            "approve": logging.INFO,
            "warn": logging.WARNING,
            "block": logging.ERROR
        }.get(decision, logging.INFO)

        logger.log(log_level, f"Decision: {decision.upper()} - {reason}")

        # Output response
        response = {
            "decision": decision,
            "reason": reason,
            "timestamp": datetime.now().isoformat(),
            "tool": input_data.get("name", "unknown")
        }

        # For blocked commands, add helpful message
        if decision == "block":
            response["user_message"] = (
                f"🛑 Security Policy Violation\n\n"
                f"Reason: {reason}\n\n"
                f"This operation was blocked to protect system integrity. "
                f"If this is a legitimate operation, please review the security policy "
                f"in .claude/hooks/pre-tool-security.py or contact your administrator."
            )

        # Output JSON response
        print(json.dumps(response, indent=2))

        # Exit with appropriate code
        sys.exit(exit_code)

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse input JSON: {e}")
        print(json.dumps({
            "decision": "block",
            "reason": "Invalid input format",
            "error": str(e)
        }), file=sys.stdout)
        sys.exit(2)

    except Exception as e:
        logger.error(f"Security hook failed: {e}", exc_info=True)
        print(json.dumps({
            "decision": "approve",  # Fail open to avoid blocking legitimate work
            "reason": "Security hook error (failing open)",
            "error": str(e)
        }), file=sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()
