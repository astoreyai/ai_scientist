# AI Scientist Harness Integration Plan

**Version**: 1.0.0
**Date**: 2025-12-28
**Status**: DRAFT - Awaiting Review

---

## Executive Summary

Integrate the proven Kymera harness pattern into AI Scientist to enable:
- **Continuous research cycles** with automated revision logic
- **ReAct-style reflection loops** for failed validations
- **Experiment harness** for hypothesis testing iterations
- **Convergence criteria** to prevent infinite loops
- **Session-based progress tracking** with audit trails

---

## Current State Analysis

### AI Scientist Strengths (Keep)
- 11-phase state machine with forward/backward transitions
- Phase validators with entry/exit criteria (FINER, PRISMA, NIH Rigor)
- 10 specialized agents + 22 reusable skills
- Dual-mode operation (ASSISTANT/AUTONOMOUS)
- Complete audit trail & state persistence
- MCP servers for literature search, citations, database

### AI Scientist Gaps (Address)
| Gap | Impact | Harness Solution |
|-----|--------|------------------|
| No automated revision decisions | Manual intervention required | `research-harness-coordinator` agent |
| No ReAct reflection loops | Failed validations dead-end | `reflection` phase in cycle |
| No iteration limits | Potential infinite loops | `max_iterations` per phase |
| No remediation logic | User must fix all issues | Auto-remediation suggestions |
| No convergence criteria | Can't assess "good enough" | Score thresholds + stability check |
| No experiment harness | Single-shot hypothesis testing | `experiment-harness` for multiple runs |

---

## Architecture Design

### Component Integration

```
                    ┌─────────────────────────────────────────┐
                    │         research-harness-coordinator     │
                    │  (Orchestrates cycles, manages state)    │
                    └────────────────┬────────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
         ▼                           ▼                           ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ /research-start │       │ /research-cycle │       │ /research-stop  │
│ (Init session)  │       │ (Execute phase) │       │ (Wrap up)       │
└─────────────────┘       └────────┬────────┘       └─────────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
           ┌────────────┐  ┌────────────┐  ┌────────────┐
           │  Validate  │  │  Execute   │  │  Reflect   │
           │   Entry    │  │   Phase    │  │  & Revise  │
           └────────────┘  └────────────┘  └────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
           ┌────────────────┐           ┌────────────────┐
           │ Validate Exit  │           │  Remediate     │
           │ (Pass? Next)   │           │  (Fail? Fix)   │
           └────────────────┘           └────────────────┘
```

### Data Flow

```
.research-harness/
├── config.json          # Project settings, thresholds
├── state.json           # Current workflow state (existing)
├── cycles.json          # Cycle history with iterations
├── experiments.json     # Hypothesis experiment tracking
├── progress.md          # Session log (human-readable)
├── verify/              # Phase verification scripts
│   ├── verify_problem.sh
│   ├── verify_literature.sh
│   ├── verify_hypothesis.sh
│   └── ...
└── remediation/         # Auto-fix suggestions
    ├── finer.json
    ├── prisma.json
    └── nih_rigor.json
```

---

## New Components

### 1. Research Harness Skills (4 skills)

#### `/research-start` - Session Initialization
```yaml
---
name: research-start
description: Initialize research harness session, load state, verify environment
allowed-tools: Read, Write, Bash, Glob
version: 1.0.0
---

## Behavior
1. Check for `.research-harness/` directory
2. Read `config.json` for project settings
3. Load existing `state.json` (WorkflowContext)
4. Calculate statistics from `cycles.json`
5. Identify current phase and pending validations
6. Display session startup report

## Output
- Current phase + validation status
- Cycle count and iteration statistics
- Next action recommendation
- Environment health check
```

#### `/research-cycle` - Execute Single Cycle
```yaml
---
name: research-cycle
description: Execute one cycle of current phase with validation and reflection
allowed-tools: Read, Write, Bash, Glob, Grep, Task
version: 1.0.0
arguments: "[--phase=X] [--max-iterations=N] [--auto-remediate]"
---

## Behavior
1. Load current state from `.research-harness/state.json`
2. Validate entry requirements for current phase
3. Execute phase with appropriate agent (from orchestrator.PHASE_AGENTS)
4. Validate exit criteria
5. If PASS: Record success, advance to next phase
6. If FAIL: Enter reflection loop
   a. Analyze validation failures
   b. Generate remediation suggestions
   c. If auto-remediate: Apply fixes
   d. Increment iteration counter
   e. Check convergence (max iterations, score stability)
   f. If converged: Escalate or accept partial
7. Update cycles.json with iteration record
8. Log to progress.md

## Cycle States
- EXECUTING: Phase work in progress
- VALIDATING: Running exit validators
- REFLECTING: Analyzing failures
- REMEDIATING: Applying fixes
- CONVERGED: Met criteria or hit limits
```

#### `/research-status` - Display Progress
```yaml
---
name: research-status
description: Display research workflow progress and cycle statistics
allowed-tools: Read, Glob
version: 1.0.0
arguments: "[--phase=X] [--verbose]"
---

## Output
- Overall workflow progress (phase X of 11)
- Current phase details
- Validation scores per phase
- Total cycles and iterations
- Time spent per phase
- Blockers and warnings
```

#### `/research-experiment` - Hypothesis Experimentation
```yaml
---
name: research-experiment
description: Run hypothesis experimentation cycle with multiple trials
allowed-tools: Read, Write, Bash, Task
version: 1.0.0
arguments: "[hypothesis-id] [--trials=N] [--parameters={}]"
---

## Behavior
1. Load hypothesis from docs/hypotheses.md
2. Load experiment design from docs/experimental_protocol.md
3. For each trial:
   a. Generate parameter variations (if applicable)
   b. Execute experiment-designer agent
   c. Run data-analyst agent on results
   d. Record trial outcome
4. Aggregate results across trials
5. Update experiments.json with findings
6. Generate summary report

## Experiment States
- DESIGNED: Protocol ready
- RUNNING: Trials in progress
- ANALYZING: Processing results
- CONCLUDED: Final assessment made
```

### 2. Research Harness Agents (2 agents)

#### `research-harness-coordinator.md` - Main Orchestrator
```markdown
# Research Harness Coordinator

## Purpose
Orchestrate continuous research workflow cycles with automated revision logic.

## Tools
- Task (spawn phase agents)
- Read/Write (state files)
- Bash (verification scripts)
- TodoWrite (progress tracking)
- Glob/Grep (codebase scanning)

## Commands
- `/research-start` - Initialize harness session
- `/research-cycle` - Execute one workflow cycle
- `/research-auto [--max-cycles=N] [--until-phase=X]` - Continuous execution
- `/research-reflect [phase]` - Deep reflection on phase failures

## Cycle Logic

### Entry Validation
```python
def validate_entry(phase):
    validator = get_validator(phase)
    result = validator.can_enter(context)
    if not result.passed:
        return BLOCK, result.missing_items
    return PROCEED, None
```

### Phase Execution
```python
def execute_phase(phase):
    agent = get_agent(phase)  # From PHASE_AGENTS map
    spawn_agent(agent, context)
    return agent.outputs
```

### Exit Validation with Reflection
```python
def validate_exit_with_reflection(phase, iteration):
    validator = get_validator(phase)
    result = validator.can_exit(context)

    if result.passed and result.score >= 0.8:
        return ADVANCE, result

    if iteration >= config.max_iterations:
        return CONVERGED_LIMIT, result

    if is_score_stable(phase, window=3):
        return CONVERGED_STABLE, result

    remediation = generate_remediation(phase, result)
    return REFLECT, remediation
```

### Convergence Criteria
1. **Score threshold**: validation.score >= config.phase_thresholds[phase]
2. **Max iterations**: iteration >= config.max_iterations (default: 5)
3. **Score stability**: |score[n] - score[n-3]| < 0.05 for 3 consecutive
4. **Blocking issues**: result.blocking_issues is empty

## State Management
- Save state before each transition (atomic)
- Track iteration count per phase
- Record all validation scores in history
- Maintain reflection log for debugging

## Error Handling
- Network failures: Retry with exponential backoff
- Agent failures: Log, increment failure count, escalate at threshold
- Validation errors: Enter reflection loop
- State corruption: Restore from last backup
```

#### `research-harness-experimenter.md` - Experiment Runner
```markdown
# Research Harness Experimenter

## Purpose
Execute hypothesis experiments with parameter variations and result aggregation.

## Tools
- Task (spawn experiment-designer, data-analyst)
- Read/Write (experiment files)
- Bash (statistical scripts)

## Experiment Protocol

### Trial Execution
```python
def run_trial(hypothesis, parameters, trial_id):
    # 1. Configure experiment
    config = apply_parameters(hypothesis.base_config, parameters)

    # 2. Execute experiment
    spawn_agent("experiment-designer", config)

    # 3. Collect data
    data = collect_experiment_data()

    # 4. Analyze
    spawn_agent("data-analyst", data)

    # 5. Record
    record_trial(trial_id, parameters, results)

    return results
```

### Aggregation
```python
def aggregate_trials(trials):
    # Effect size meta-analysis
    effect_sizes = [t.effect_size for t in trials]
    pooled_effect = random_effects_meta(effect_sizes)

    # Heterogeneity
    I2 = calculate_heterogeneity(trials)

    # Conclusion
    if pooled_effect.p < 0.05 and I2 < 0.5:
        return SUPPORTED, pooled_effect
    elif pooled_effect.p >= 0.05:
        return NOT_SUPPORTED, pooled_effect
    else:
        return INCONCLUSIVE, {"I2": I2, "effect": pooled_effect}
```

## Output
- experiments.json updated with trial results
- Summary report in results/experiment_summary.md
- Effect size forest plot
```

### 3. Configuration Schema

#### `.research-harness/config.json`
```json
{
  "project": "research-project-name",
  "harness": {
    "type": "research-workflow",
    "pattern": "continuous-revision"
  },
  "mode": "AUTONOMOUS",
  "thresholds": {
    "phase_scores": {
      "PROBLEM_FORMULATION": 0.8,
      "LITERATURE_REVIEW": 0.8,
      "GAP_ANALYSIS": 0.7,
      "HYPOTHESIS_FORMATION": 0.8,
      "EXPERIMENTAL_DESIGN": 0.9,
      "IRB_APPROVAL": 1.0,
      "DATA_COLLECTION": 0.8,
      "ANALYSIS": 0.9,
      "INTERPRETATION": 0.8,
      "WRITING": 0.8,
      "PUBLICATION": 0.9
    },
    "max_iterations_per_phase": 5,
    "score_stability_window": 3,
    "score_stability_delta": 0.05
  },
  "convergence": {
    "accept_partial_at_iteration": 4,
    "escalate_to_human_at_iteration": 5,
    "minimum_acceptable_score": 0.6
  },
  "experiment": {
    "default_trials": 3,
    "max_trials": 10,
    "parameter_variation_strategy": "grid"
  },
  "logging": {
    "verbose": true,
    "log_reflections": true,
    "session_log": "progress.md"
  }
}
```

#### `.research-harness/cycles.json`
```json
{
  "workflow_id": "uuid",
  "started_at": "2025-12-28T00:00:00Z",
  "current_phase": "LITERATURE_REVIEW",
  "total_cycles": 7,
  "phases": {
    "PROBLEM_FORMULATION": {
      "iterations": 2,
      "scores": [0.65, 0.85],
      "status": "COMPLETED",
      "completed_at": "2025-12-28T01:00:00Z",
      "reflections": [
        {
          "iteration": 1,
          "issues": ["Missing 'Novel' criterion evidence"],
          "remediation": "Added literature gap analysis",
          "score_delta": 0.20
        }
      ]
    },
    "LITERATURE_REVIEW": {
      "iterations": 3,
      "scores": [0.55, 0.68, 0.72],
      "status": "IN_PROGRESS",
      "reflections": [
        {
          "iteration": 1,
          "issues": ["κ < 0.6 for screening", "Missing 8 PRISMA items"],
          "remediation": "Re-screened with refined criteria",
          "score_delta": 0.13
        },
        {
          "iteration": 2,
          "issues": ["κ = 0.58 (still below threshold)"],
          "remediation": "Added third reviewer simulation",
          "score_delta": 0.04
        }
      ]
    }
  }
}
```

### 4. Remediation Logic

#### `code/remediation/base.py`
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class RemediationAction:
    issue: str
    action_type: str  # "modify", "add", "remove", "regenerate"
    target: str       # File or artifact
    suggestion: str
    auto_applicable: bool
    priority: int

class BaseRemediator(ABC):
    @abstractmethod
    def analyze_failures(self, validation_result) -> List[str]:
        """Identify specific failure reasons"""
        pass

    @abstractmethod
    def generate_actions(self, failures: List[str]) -> List[RemediationAction]:
        """Generate remediation actions for failures"""
        pass

    @abstractmethod
    def apply_action(self, action: RemediationAction) -> bool:
        """Apply a single remediation action"""
        pass

    def remediate(self, validation_result, auto_apply: bool = False):
        failures = self.analyze_failures(validation_result)
        actions = self.generate_actions(failures)

        if auto_apply:
            for action in actions:
                if action.auto_applicable:
                    self.apply_action(action)

        return actions
```

#### `code/remediation/finer_remediation.py`
```python
class FINERRemediator(BaseRemediator):
    REMEDIATION_MAP = {
        "feasibility_missing": {
            "action_type": "add",
            "target": "docs/problem_statement.md",
            "suggestion": "Add feasibility analysis section with:\n"
                         "- Timeline estimate\n"
                         "- Resource requirements\n"
                         "- Technical constraints\n"
                         "- Pilot study plan",
            "auto_applicable": False
        },
        "novelty_weak": {
            "action_type": "modify",
            "target": "docs/problem_statement.md",
            "suggestion": "Strengthen novelty claim by:\n"
                         "- Citing specific gaps in existing literature\n"
                         "- Explaining how this differs from prior work\n"
                         "- Quantifying expected improvement",
            "auto_applicable": False
        },
        "ethical_missing": {
            "action_type": "add",
            "target": "docs/problem_statement.md",
            "suggestion": "Add ethics section addressing:\n"
                         "- Human subjects considerations\n"
                         "- Data privacy/security\n"
                         "- Potential societal impact\n"
                         "- Mitigation strategies",
            "auto_applicable": False
        }
    }

    def analyze_failures(self, result):
        failures = []
        for item in result.missing_items:
            if "feasib" in item.lower():
                failures.append("feasibility_missing")
            elif "novel" in item.lower():
                failures.append("novelty_weak")
            elif "ethic" in item.lower():
                failures.append("ethical_missing")
        return failures
```

#### `code/remediation/prisma_remediation.py`
```python
class PRISMARemediator(BaseRemediator):
    REMEDIATION_MAP = {
        "kappa_low": {
            "action_type": "regenerate",
            "target": "data/literature/screened_abstracts.csv",
            "suggestion": "Re-screen abstracts with:\n"
                         "- More specific inclusion criteria\n"
                         "- Additional reviewer (simulated)\n"
                         "- Consensus meeting for disagreements",
            "auto_applicable": True  # Can re-run screening
        },
        "insufficient_studies": {
            "action_type": "modify",
            "target": "docs/search_strategy.md",
            "suggestion": "Expand search by:\n"
                         "- Adding databases (OpenAlex, bioRxiv)\n"
                         "- Relaxing date restrictions\n"
                         "- Adding synonym search terms\n"
                         "- Including grey literature",
            "auto_applicable": True  # Can re-run search
        },
        "prisma_items_missing": {
            "action_type": "add",
            "target": "docs/prisma_checklist.md",
            "suggestion": "Add missing PRISMA items:\n"
                         "{missing_items}",  # Dynamic
            "auto_applicable": False
        }
    }
```

### 5. Verification Scripts

#### `.research-harness/verify/verify_literature.sh`
```bash
#!/bin/bash
# Verify LITERATURE_REVIEW phase completion

PROJECT_ROOT="${1:-.}"
THRESHOLD_KAPPA=0.6
THRESHOLD_STUDIES=10
THRESHOLD_PRISMA=24

# Check required files exist
required_files=(
    "data/literature/search_results.csv"
    "data/literature/screened_abstracts.csv"
    "data/literature/included_studies.csv"
    "data/literature/extracted_data.csv"
    "docs/search_strategy.md"
)

for file in "${required_files[@]}"; do
    if [[ ! -f "$PROJECT_ROOT/$file" ]]; then
        echo "FAIL: Missing $file"
        exit 1
    fi
done

# Check study count
study_count=$(wc -l < "$PROJECT_ROOT/data/literature/included_studies.csv")
study_count=$((study_count - 1))  # Subtract header
if [[ $study_count -lt $THRESHOLD_STUDIES ]]; then
    echo "PARTIAL: Only $study_count studies (need $THRESHOLD_STUDIES)"
    exit 2
fi

# Check inter-rater reliability (if file exists)
if [[ -f "$PROJECT_ROOT/data/literature/inter_rater_reliability.md" ]]; then
    kappa=$(grep -oP 'κ\s*=\s*\K[\d.]+' "$PROJECT_ROOT/data/literature/inter_rater_reliability.md")
    if (( $(echo "$kappa < $THRESHOLD_KAPPA" | bc -l) )); then
        echo "PARTIAL: κ = $kappa (need $THRESHOLD_KAPPA)"
        exit 2
    fi
fi

echo "PASS: Literature review complete"
exit 0
```

---

## Implementation Sequence

### Phase 1: Foundation (Day 1-2)
1. Create `.research-harness/` directory structure
2. Implement `config.json` schema
3. Implement `cycles.json` tracking
4. Create base remediation framework
5. Write verification scripts for all 11 phases

### Phase 2: Skills (Day 2-3)
1. Implement `/research-start` skill
2. Implement `/research-status` skill
3. Implement `/research-cycle` skill
4. Implement `/research-experiment` skill
5. Add skills to `~/.claude/skills/` and claude-skills repo

### Phase 3: Agents (Day 3-4)
1. Implement `research-harness-coordinator.md`
2. Implement `research-harness-experimenter.md`
3. Add agents to `~/.claude/agents/` and claude-skills repo
4. Integrate with existing orchestrator.py

### Phase 4: Remediation (Day 4-5)
1. Implement FINERRemediator
2. Implement PRISMARemediator
3. Implement NIHRigorRemediator
4. Add remediation to reflection loop

### Phase 5: Integration Testing (Day 5-6)
1. Test single-phase cycles
2. Test multi-phase workflows
3. Test convergence logic
4. Test experiment harness
5. Test ASSISTANT vs AUTONOMOUS modes

### Phase 6: Documentation (Day 6)
1. Update AI Scientist README
2. Update CLAUDE.md with harness instructions
3. Add examples and tutorials
4. Update agent/skill documentation

---

## Testing Strategy

### Unit Tests
- Remediation action generation
- Convergence criteria logic
- Verification script parsing

### Integration Tests
- Full cycle execution (mock agents)
- State persistence across sessions
- Reflection loop with remediation

### End-to-End Tests
- Complete PROBLEM_FORMULATION → LITERATURE_REVIEW cycle
- Experiment harness with 3 trials
- AUTONOMOUS mode full workflow

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Infinite loops | Max iteration limits + score stability |
| State corruption | Atomic saves + backup before transitions |
| Agent failures | Retry logic + escalation thresholds |
| Over-remediation | Conservative auto-apply flags |
| Resource exhaustion | Session time limits |

---

## Success Criteria

1. **Continuous Cycles**: Can execute 5+ cycles without human intervention
2. **Revision Logic**: Automatically detects and attempts to fix validation failures
3. **Convergence**: Reliably stops at threshold or max iterations
4. **Experiment Harness**: Can run multi-trial experiments with aggregation
5. **Progress Tracking**: Complete audit trail in cycles.json and progress.md
6. **Mode Support**: Works in both ASSISTANT and AUTONOMOUS modes

---

## Open Questions for Review

1. **Remediation Aggressiveness**: How much should auto-remediate vs. escalate?
2. **Experiment Trials**: Default to 3 trials or make configurable per hypothesis?
3. **Cross-Phase Dependencies**: When a revision invalidates later phases, auto-rollback?
4. **Session Limits**: Max cycles per session (resource protection)?
5. **Human Checkpoints**: Even in AUTONOMOUS, require human approval at key gates?

---

## Appendix: File Locations

### New Files to Create
```
~/github/astoreyai/ai_scientist/
├── .research-harness/
│   ├── config.json
│   ├── cycles.json
│   ├── experiments.json
│   ├── progress.md
│   └── verify/
│       ├── verify_problem.sh
│       ├── verify_literature.sh
│       ├── verify_gap.sh
│       ├── verify_hypothesis.sh
│       ├── verify_design.sh
│       ├── verify_irb.sh
│       ├── verify_data.sh
│       ├── verify_analysis.sh
│       ├── verify_interpretation.sh
│       ├── verify_writing.sh
│       └── verify_publication.sh
├── code/
│   ├── harness/
│   │   ├── __init__.py
│   │   ├── coordinator.py
│   │   ├── experimenter.py
│   │   └── cycle_tracker.py
│   └── remediation/
│       ├── __init__.py
│       ├── base.py
│       ├── finer_remediation.py
│       ├── prisma_remediation.py
│       └── nih_rigor_remediation.py

~/.claude/skills/
├── research-start/SKILL.md
├── research-cycle/SKILL.md
├── research-status/SKILL.md
└── research-experiment/SKILL.md

~/.claude/agents/
├── research-harness-coordinator.md
└── research-harness-experimenter.md

~/github/astoreyai/claude-skills/  (for plugin distribution)
├── skills/research-harness/
└── agents/research-harness/
```
