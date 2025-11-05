#!/usr/bin/env python3
"""
User Prompt Validation Hook for Claude Code Research Assistant

Triggered: When user submits a prompt
Purpose: Validate research scope, mode compatibility, and suggest improvements

Input: JSON from stdin with user prompt information
Output: JSON to stdout with validation and suggestions
Exit codes: 0 = approve, 1 = approve with suggestions, 2 = block

Validates:
    - Prompt appropriateness for current research phase
    - Mode compatibility (ASSISTANT vs AUTONOMOUS)
    - Research standards compliance requests
    - Dangerous operations warnings
    - Scope creep detection

Integration with .claude/settings.json:
    {
      "UserPromptSubmit": [{
        "matcher": "",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/prompt-validate.py"}]
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
import re

# ============================================
# CONFIGURATION
# ============================================

PROJECT_DIR = Path(os.getenv("CLAUDE_PROJECT_DIR", os.getcwd()))
CLAUDE_DIR = PROJECT_DIR / ".claude"
LOG_FILE = CLAUDE_DIR / "prompt-validation.log"

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
# VALIDATION PATTERNS
# ============================================

# Patterns that require AUTONOMOUS mode
AUTONOMOUS_PATTERNS = [
    r"automatically generate",
    r"auto.*(generate|create|proceed)",
    r"continue (without|autonomously)",
    r"generate .* hypotheses? without",
    r"full autonomous",
]

# Patterns that suggest research standards
STANDARDS_KEYWORDS = {
    "systematic review": "Remember to follow PRISMA 2020 guidelines (use literature-reviewer agent)",
    "literature review": "Consider using PRISMA 2020 protocol (use literature-reviewer agent)",
    "rct": "Use CONSORT reporting guidelines for RCT design",
    "randomized": "Ensure NIH rigor standards: power ≥80%, pre-registration, SABV",
    "experiment": "Use experiment-designer agent for NIH-compliant design",
    "statistical analysis": "Use data-analyst agent for reproducible analysis with effect sizes",
    "power analysis": "Ensure ≥80% power with justified effect size from literature",
}

# Dangerous operation patterns
DANGEROUS_PATTERNS = [
    (r"delete.*all", "Consider backing up before bulk deletion"),
    (r"remove.*everything", "Destructive operation - ensure you have backups"),
    (r"overwrite.*data", "Ensure data is versioned with DVC before overwriting"),
    (r"change.*protocol", "Protocol changes after data collection violate pre-registration"),
    (r"modify.*results", "Results modification compromises research integrity"),
]

# Phase transition keywords
PHASE_KEYWORDS = {
    "problem_formulation": ["problem", "research question", "finer criteria"],
    "literature_review": ["literature", "systematic review", "search strategy", "prisma"],
    "gap_analysis": ["gap", "missing", "unexplored"],
    "hypothesis_formation": ["hypothesis", "hypotheses", "testable"],
    "experimental_design": ["experiment", "design", "protocol", "power analysis"],
    "data_collection": ["collect data", "gather data", "recruitment"],
    "analysis": ["analyze", "statistical", "results"],
    "interpretation": ["interpret", "discuss", "meaning"],
    "writing": ["write", "manuscript", "paper", "draft"],
    "publication": ["publish", "submit", "journal"],
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


def get_current_mode() -> str:
    """Get current operating mode from CLAUDE.md"""

    claude_md = CLAUDE_DIR / "CLAUDE.md"

    if claude_md.exists():
        try:
            with open(claude_md, 'r') as f:
                content = f.read()
                if "# Current Mode: ASSISTANT" in content:
                    return "ASSISTANT"
                elif "# Current Mode: AUTONOMOUS" in content:
                    return "AUTONOMOUS"
        except Exception as e:
            logger.error(f"Failed to read CLAUDE.md: {e}")

    return "ASSISTANT"  # Default


def check_autonomous_requirement(prompt: str) -> Tuple[bool, Optional[str]]:
    """
    Check if prompt requires AUTONOMOUS mode

    Args:
        prompt: User prompt text

    Returns:
        (requires_autonomous, reason) tuple
    """

    prompt_lower = prompt.lower()

    for pattern in AUTONOMOUS_PATTERNS:
        if re.search(pattern, prompt_lower):
            return (True, f"Prompt contains autonomous request: '{pattern}'")

    return (False, None)


def detect_phase_intent(prompt: str) -> Optional[str]:
    """
    Detect which research phase the prompt relates to

    Args:
        prompt: User prompt text

    Returns:
        Detected phase name or None
    """

    prompt_lower = prompt.lower()

    # Count keyword matches for each phase
    phase_scores = {}
    for phase, keywords in PHASE_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in prompt_lower)
        if score > 0:
            phase_scores[phase] = score

    if not phase_scores:
        return None

    # Return phase with highest score
    return max(phase_scores, key=phase_scores.get)


def check_standards_compliance(prompt: str) -> List[str]:
    """
    Check if prompt should reference research standards

    Args:
        prompt: User prompt text

    Returns:
        List of suggestions
    """

    suggestions = []
    prompt_lower = prompt.lower()

    for keyword, suggestion in STANDARDS_KEYWORDS.items():
        if keyword in prompt_lower:
            suggestions.append(suggestion)

    return suggestions


def check_dangerous_operations(prompt: str) -> List[str]:
    """
    Check for potentially dangerous operations

    Args:
        prompt: User prompt text

    Returns:
        List of warnings
    """

    warnings = []
    prompt_lower = prompt.lower()

    for pattern, warning in DANGEROUS_PATTERNS:
        if re.search(pattern, prompt_lower):
            warnings.append(warning)

    return warnings


def validate_phase_compatibility(prompt: str, current_phase: str) -> Tuple[bool, Optional[str]]:
    """
    Validate if prompt is appropriate for current phase

    Args:
        prompt: User prompt text
        current_phase: Current research phase

    Returns:
        (is_compatible, message) tuple
    """

    detected_phase = detect_phase_intent(prompt)

    if not detected_phase:
        # No specific phase detected, assume compatible
        return (True, None)

    # Check if detected phase is far ahead of current phase
    phase_order = list(PHASE_KEYWORDS.keys())

    try:
        current_idx = phase_order.index(current_phase)
        detected_idx = phase_order.index(detected_phase)

        if detected_idx > current_idx + 2:
            return (False,
                   f"Prompt appears to request '{detected_phase}' but current phase is '{current_phase}'. "
                   f"Consider completing intermediate phases first.")

        if detected_idx < current_idx - 1:
            return (True,
                   f"Note: This prompt references earlier phase '{detected_phase}' "
                   f"while current phase is '{current_phase}'. Revisions are acceptable.")

    except ValueError:
        # Phase not in order list, assume compatible
        pass

    return (True, None)


def generate_feedback_message(
    mode: str,
    current_phase: str,
    autonomous_required: bool,
    suggestions: List[str],
    warnings: List[str],
    phase_message: Optional[str]
) -> str:
    """Generate human-readable feedback message"""

    parts = []

    # Mode mismatch warning
    if autonomous_required and mode == "ASSISTANT":
        parts.append(
            "⚠️  Your prompt requests autonomous operation, but system is in ASSISTANT mode.\n"
            "To enable autonomous operation:\n"
            "1. Edit .claude/CLAUDE.md\n"
            "2. Change '# Current Mode: ASSISTANT' to '# Current Mode: AUTONOMOUS'\n"
            "3. Restart session\n"
        )

    # Phase compatibility message
    if phase_message:
        parts.append(f"📍 Phase Check: {phase_message}\n")

    # Research standards suggestions
    if suggestions:
        parts.append("💡 Research Standards Suggestions:")
        for suggestion in suggestions:
            parts.append(f"  • {suggestion}")
        parts.append("")

    # Dangerous operation warnings
    if warnings:
        parts.append("⚠️  Safety Warnings:")
        for warning in warnings:
            parts.append(f"  • {warning}")
        parts.append("")

    # Current context
    parts.append(f"Current Mode: {mode}")
    parts.append(f"Current Phase: {current_phase}")

    return "\n".join(parts)


# ============================================
# MAIN HOOK LOGIC
# ============================================

def main():
    """Main hook execution"""

    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())

        prompt = input_data.get("prompt", "")
        logger.info(f"Validating prompt (length: {len(prompt)} chars)")

        # Load context
        state = load_session_state()
        current_phase = state.get("current_phase", "initialization")
        mode = get_current_mode()

        # Run validations
        autonomous_required, auto_reason = check_autonomous_requirement(prompt)
        suggestions = check_standards_compliance(prompt)
        warnings = check_dangerous_operations(prompt)
        phase_compatible, phase_message = validate_phase_compatibility(prompt, current_phase)

        # Determine if we should block
        should_block = False
        block_reason = None

        # Block if autonomous required but in assistant mode
        if autonomous_required and mode == "ASSISTANT":
            # Don't block, just warn
            pass

        # Block if phase incompatible
        if not phase_compatible:
            should_block = True
            block_reason = phase_message

        # Determine exit code
        if should_block:
            decision = "block"
            exit_code = 2
        elif suggestions or warnings or autonomous_required:
            decision = "approve_with_suggestions"
            exit_code = 1
        else:
            decision = "approve"
            exit_code = 0

        # Generate response
        response = {
            "decision": decision,
            "timestamp": datetime.now().isoformat(),
            "mode": mode,
            "current_phase": current_phase,
            "autonomous_required": autonomous_required,
            "suggestions": suggestions,
            "warnings": warnings,
            "phase_compatible": phase_compatible,
        }

        # Add user message if there's feedback
        if decision != "approve" or suggestions or warnings:
            response["user_message"] = generate_feedback_message(
                mode, current_phase, autonomous_required,
                suggestions, warnings, phase_message
            )

        # Add block reason
        if should_block:
            response["block_reason"] = block_reason

        # Output JSON response
        print(json.dumps(response, indent=2))

        logger.info(f"Validation result: {decision}")

        # Exit with appropriate code
        sys.exit(exit_code)

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse input JSON: {e}")
        print(json.dumps({
            "decision": "approve",  # Fail open
            "error": "Invalid input format"
        }), file=sys.stdout)
        sys.exit(0)

    except Exception as e:
        logger.error(f"Prompt validation hook failed: {e}", exc_info=True)
        print(json.dumps({
            "decision": "approve",  # Fail open to avoid blocking legitimate work
            "error": str(e)
        }), file=sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()
