#!/bin/bash
# Session Start Hook for Claude Code Research Assistant
#
# Triggered: When a new Claude Code session starts
# Purpose: Load research protocols, mode configuration, and session state
#
# Input: JSON from stdin with session metadata
# Output: JSON to stdout with loaded context (optional)
# Exit codes: 0 = success, 1 = warning, 2 = block session start

set -euo pipefail

# Configuration
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
CLAUDE_DIR="$PROJECT_DIR/.claude"
PROTOCOLS_DIR="$CLAUDE_DIR/protocols"
LOG_FILE="$CLAUDE_DIR/session.log"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

# Read input from stdin (Claude Code hook protocol)
INPUT=$(cat)

# Log session start
log "=== SESSION START ==="
log "Input: $INPUT"

# Ensure required directories exist
mkdir -p "$PROTOCOLS_DIR"

# Load research protocols
load_protocols() {
    local protocols_loaded=0

    # Check for PRISMA 2020 checklist
    if [[ -f "$PROTOCOLS_DIR/prisma_2020_checklist.md" ]]; then
        log "Loaded: PRISMA 2020 checklist"
        ((protocols_loaded++))
    else
        # Create default PRISMA checklist
        cat > "$PROTOCOLS_DIR/prisma_2020_checklist.md" << 'EOF'
# PRISMA 2020 Checklist

## Title (1)
- [ ] Identify report as systematic review

## Abstract (2)
- [ ] Structured summary

## Introduction (3-5)
- [ ] Rationale
- [ ] Objectives

## Methods (6-16)
- [ ] Eligibility criteria
- [ ] Information sources
- [ ] Search strategy
- [ ] Selection process
- [ ] Data collection
- [ ] Data items
- [ ] Risk of bias assessment
- [ ] Effect measures
- [ ] Synthesis methods
- [ ] Reporting bias assessment
- [ ] Certainty assessment

## Results (17-22)
- [ ] Study selection
- [ ] Study characteristics
- [ ] Risk of bias
- [ ] Results synthesis
- [ ] Reporting biases
- [ ] Certainty of evidence

## Discussion (23-26)
- [ ] Discussion of results
- [ ] Limitations
- [ ] Interpretation
- [ ] Implications

## Other (27)
- [ ] Funding and registration

Target: ≥24/27 items for compliance
EOF
        log "Created: Default PRISMA 2020 checklist"
        ((protocols_loaded++))
    fi

    # Check for NIH rigor checklist
    if [[ -f "$PROTOCOLS_DIR/nih_rigor_checklist.md" ]]; then
        log "Loaded: NIH rigor checklist"
        ((protocols_loaded++))
    else
        # Create default NIH rigor checklist
        cat > "$PROTOCOLS_DIR/nih_rigor_checklist.md" << 'EOF'
# NIH Rigor and Reproducibility Checklist

## Scientific Rigor
- [ ] Robust experimental design (controls, randomization, blinding)
- [ ] Power analysis ≥80%
- [ ] Effect size justified from literature or pilot data

## Sex as Biological Variable (SABV)
- [ ] Sex considered in study design and analysis
- [ ] Justification if single-sex study

## Reproducibility
- [ ] Pre-registered before data collection (OSF/ClinicalTrials.gov)
- [ ] Random seeds documented in code
- [ ] Analysis code publicly available
- [ ] Data shared per FAIR principles

## Statistical Analysis
- [ ] Primary analysis pre-specified
- [ ] Multiple comparisons correction specified
- [ ] Missing data handling pre-specified
- [ ] All outcomes reported (including null results)

## Data Management
- [ ] FAIR-compliant data management plan
- [ ] Data dictionary provided
- [ ] Version control (Git for code, DVC for data)

Target: ≥90% compliance required
EOF
        log "Created: Default NIH rigor checklist"
        ((protocols_loaded++))
    fi

    log "Protocols loaded: $protocols_loaded"
}

# Load mode configuration
load_mode() {
    if [[ -f "$CLAUDE_DIR/CLAUDE.md" ]]; then
        # Extract current mode from CLAUDE.md
        if grep -q "# Current Mode: ASSISTANT" "$CLAUDE_DIR/CLAUDE.md"; then
            MODE="ASSISTANT"
        elif grep -q "# Current Mode: AUTONOMOUS" "$CLAUDE_DIR/CLAUDE.md"; then
            MODE="AUTONOMOUS"
        else
            MODE="ASSISTANT"  # Default to ASSISTANT mode
            log "WARNING: Mode not specified in CLAUDE.md, defaulting to ASSISTANT"
        fi

        log "Mode: $MODE"
        echo "Current research mode: $MODE" >&2
    else
        log "ERROR: CLAUDE.md not found"
        echo "ERROR: Project configuration missing (.claude/CLAUDE.md)" >&2
        exit 1
    fi
}

# Load previous session state (if exists)
load_session_state() {
    local state_file="$CLAUDE_DIR/session_state.json"

    if [[ -f "$state_file" ]]; then
        local last_phase
        last_phase=$(jq -r '.current_phase // "none"' "$state_file" 2>/dev/null || echo "none")

        if [[ "$last_phase" != "none" ]]; then
            log "Resuming from phase: $last_phase"
            echo "Resuming research workflow from: $last_phase" >&2
        fi
    else
        # Create initial state file
        cat > "$state_file" << EOF
{
  "current_phase": "initialization",
  "mode": "$MODE",
  "started_at": "$(date -Iseconds)",
  "last_updated": "$(date -Iseconds)"
}
EOF
        log "Created: Initial session state"
    fi
}

# Check for required tools
check_dependencies() {
    local missing_deps=()

    # Check Python
    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
    fi

    # Check Git
    if ! command -v git &> /dev/null; then
        missing_deps+=("git")
    fi

    # Check jq (for JSON processing)
    if ! command -v jq &> /dev/null; then
        missing_deps+=("jq")
    fi

    if [[ ${#missing_deps[@]} -gt 0 ]]; then
        log "WARNING: Missing dependencies: ${missing_deps[*]}"
        echo "WARNING: Missing tools: ${missing_deps[*]}" >&2
        echo "Install with: sudo apt-get install ${missing_deps[*]}" >&2
    fi
}

# Main execution
main() {
    log "Project directory: $PROJECT_DIR"

    # Load protocols and configuration
    load_protocols
    load_mode
    load_session_state
    check_dependencies

    # Output context for Claude Code (optional)
    # This gets displayed to the user
    cat << EOF
Research Assistant System ready.

Mode: $MODE
Protocols: PRISMA 2020, NIH Rigor
Session log: .claude/session.log

Type '/help research' for research workflow commands.
EOF

    log "=== SESSION START COMPLETE ==="

    # Exit 0 = success, session can proceed
    exit 0
}

# Handle errors
trap 'log "ERROR: Session start failed at line $LINENO"; exit 1' ERR

# Run main function
main
