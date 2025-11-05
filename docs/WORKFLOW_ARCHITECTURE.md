# Research Workflow State Machine Architecture

**Version:** 1.0
**Date:** November 5, 2025
**Status:** Design Document

---

## Overview

The Research Workflow State Machine manages progression through the 11 phases of scientific research, from problem formulation to publication. It orchestrates specialized agents, validates completion criteria, and respects mode-specific behaviors.

---

## Architecture Principles

### 1. State Safety (R3)
- Every transition validated before execution
- State persisted to disk after each phase
- Rollback capability for failed transitions
- Complete audit trail of all decisions

### 2. Mode Awareness
- **ASSISTANT Mode:** Human approval required at decision gates
- **AUTONOMOUS Mode:** Auto-proceed if validation passes
- Mode can change mid-workflow

### 3. Agent Orchestration
- Each phase invokes appropriate specialized agent(s)
- Agents receive context from previous phases
- Outputs validated before phase completion

### 4. Validation Gates
- Entry requirements: Can we start this phase?
- Exit criteria: Can we proceed to next phase?
- Quality standards: Does output meet standards?

---

## State Machine Design

### 11 Research Phases (States)

```python
class ResearchPhase(str, Enum):
    """11 phases of research workflow"""
    PROBLEM_FORMULATION = "problem_formulation"
    LITERATURE_REVIEW = "literature_review"
    GAP_ANALYSIS = "gap_analysis"
    HYPOTHESIS_FORMATION = "hypothesis_formation"
    EXPERIMENTAL_DESIGN = "experimental_design"
    IRB_APPROVAL = "irb_approval"
    DATA_COLLECTION = "data_collection"
    ANALYSIS = "analysis"
    INTERPRETATION = "interpretation"
    WRITING = "writing"
    PUBLICATION = "publication"
```

### Transition Rules

**Linear Progression (Default):**
```
Problem → Literature → Gap → Hypothesis → Design → IRB →
Data → Analysis → Interpretation → Writing → Publication
```

**Allowed Backward Transitions:**
- Any phase can return to PROBLEM_FORMULATION (major pivot)
- HYPOTHESIS can return to LITERATURE_REVIEW (insufficient evidence)
- DESIGN can return to HYPOTHESIS (infeasible design)
- ANALYSIS can return to DATA_COLLECTION (insufficient data)

**Blocked Transitions:**
- Cannot skip phases (must progress sequentially)
- Cannot skip IRB_APPROVAL if human subjects involved
- Cannot skip DATA_COLLECTION for empirical studies

---

## Phase Specifications

### Phase 1: Problem Formulation

**Agent:** None (direct Claude Code interaction)

**Entry Requirements:**
- None (starting phase)

**Activities:**
- Define research question using FINER criteria
  - **F**easible
  - **I**nteresting
  - **N**ovel
  - **E**thical
  - **R**elevant
- Create `docs/problem_statement.md`

**Exit Criteria:**
- ✅ Problem statement exists
- ✅ Research question operationalized
- ✅ FINER criteria satisfied (≥4/5)
- ✅ Feasibility assessment documented

**Outputs:**
- `docs/problem_statement.md`

**Mode Behavior:**
- ASSISTANT: Collaborate on FINER criteria evaluation
- AUTONOMOUS: Auto-validate if all criteria met

---

### Phase 2: Literature Review

**Agent:** `literature-reviewer`

**Entry Requirements:**
- ✅ Problem statement complete (Phase 1 exit criteria)

**Activities:**
- Execute PRISMA 2020 systematic review
- Search multiple databases (OpenAlex, PubMed, arXiv)
- Screen abstracts and full texts
- Extract data from included studies
- Assess risk of bias

**Exit Criteria:**
- ✅ PRISMA 2020 checklist ≥24/27 items
- ✅ Inter-rater reliability κ ≥ 0.6
- ✅ ≥10 included studies (or justification if fewer)
- ✅ Risk of bias assessment complete
- ✅ PRISMA flow diagram with counts

**Outputs:**
- `data/literature/search_results.csv`
- `data/literature/screened_abstracts.csv`
- `data/literature/included_studies.csv`
- `data/literature/extracted_data.csv`
- `results/prisma_flow_diagram.md`
- `results/risk_of_bias_assessment.csv`

**Mode Behavior:**
- ASSISTANT: Present screening decisions for review
- AUTONOMOUS: Simulate inter-rater reliability with two passes

---

### Phase 3: Gap Analysis

**Agent:** `gap-analyst`

**Entry Requirements:**
- ✅ Literature review complete (Phase 2 exit criteria)

**Activities:**
- Identify patterns across studies
- Analyze methodological gaps
- Prioritize gaps by impact and feasibility
- Generate gap matrix

**Exit Criteria:**
- ✅ ≥3 research gaps identified
- ✅ Gaps prioritized with scoring matrix
- ✅ Top gap selected with justification
- ✅ PICO framework applied to selected gap

**Outputs:**
- `docs/gap_analysis.md`
- `data/gap_matrix.csv`

**Mode Behavior:**
- ASSISTANT: Present gap options for human selection
- AUTONOMOUS: Auto-select top-ranked gap

---

### Phase 4: Hypothesis Formation

**Agent:** `hypothesis-generator`

**Entry Requirements:**
- ✅ Gap analysis complete (Phase 3 exit criteria)

**Activities:**
- Generate 5 candidate hypotheses (Tree-of-Thought)
- Evaluate testability, falsifiability, novelty
- Rank by composite score
- Refine top hypotheses

**Exit Criteria:**
- ✅ ≥3 hypotheses generated
- ✅ All hypotheses falsifiable (H₀ specified)
- ✅ Variables operationally defined
- ✅ Directional predictions specified
- ✅ Testability score ≥0.7

**Outputs:**
- `docs/hypotheses.md`
- `docs/hypothesis_generation_log.md`
- `docs/falsifiability_statements.md`

**Mode Behavior:**
- ASSISTANT: Present candidates, collaborative selection
- AUTONOMOUS: Auto-select top 3 by composite score

---

### Phase 5: Experimental Design

**Agent:** `experiment-designer`

**Entry Requirements:**
- ✅ Hypotheses formulated (Phase 4 exit criteria)

**Activities:**
- Select optimal study design (RCT, quasi-experimental, observational)
- Conduct power analysis (≥80% power)
- Generate randomization protocol
- Create pre-registration document
- Develop FAIR data management plan

**Exit Criteria:**
- ✅ Study design justified
- ✅ Power ≥80%
- ✅ Randomization protocol with seed
- ✅ Pre-registration document complete
- ✅ NIH rigor checklist ≥90%

**Outputs:**
- `docs/experimental_design_rationale.md`
- `docs/power_analysis.md`
- `docs/experimental_protocol.md`
- `code/randomization.py`
- `docs/data_management_plan.md`
- `data/preregistration.md`

**Mode Behavior:**
- ASSISTANT: Explain design options, get approval for sample size
- AUTONOMOUS: Select most rigorous feasible design

---

### Phase 6: IRB Approval

**Agent:** None (human-only phase)

**Entry Requirements:**
- ✅ Experimental design complete (Phase 5 exit criteria)
- ✅ Human subjects involved (if false, skip this phase)

**Activities:**
- Submit IRB application
- Respond to IRB queries
- Obtain approval or exemption

**Exit Criteria:**
- ✅ IRB approval obtained (or exemption documented)
- ✅ Consent forms approved
- ✅ Protocol modifications documented

**Outputs:**
- `docs/irb_approval.pdf`
- `docs/consent_forms.pdf`

**Mode Behavior:**
- ASSISTANT: Remind user to submit IRB, wait for human confirmation
- AUTONOMOUS: Automatically wait (cannot proceed without human IRB submission)

---

### Phase 7: Data Collection

**Agent:** None (real-world activity, monitored by system)

**Entry Requirements:**
- ✅ IRB approval (Phase 6) OR no human subjects
- ✅ Pre-registration complete

**Activities:**
- Execute data collection protocol
- Monitor data quality in real-time
- Track recruitment progress

**Exit Criteria:**
- ✅ Target sample size achieved (or stopping rule met)
- ✅ Data quality checks passed
- ✅ Protocol violations documented
- ✅ Data stored securely per DMP

**Outputs:**
- `data/raw/` (DVC tracked)
- `data/data_quality_log.csv`

**Mode Behavior:**
- ASSISTANT: Regular check-ins, human confirms completion
- AUTONOMOUS: Monitor data file creation, auto-proceed when N achieved

---

### Phase 8: Analysis

**Agent:** `data-analyst`

**Entry Requirements:**
- ✅ Data collection complete (Phase 7 exit criteria)

**Activities:**
- Execute pre-registered analysis plan
- Test statistical assumptions
- Calculate effect sizes with confidence intervals
- Run sensitivity analyses

**Exit Criteria:**
- ✅ Primary analysis complete
- ✅ Assumptions tested and documented
- ✅ Effect sizes with 95% CI calculated
- ✅ Sensitivity analyses conducted
- ✅ Code executable in clean environment

**Outputs:**
- `code/analysis/primary_analysis.py`
- `results/primary_results.json`
- `results/assumption_tests.csv`
- `results/effect_sizes.csv`

**Mode Behavior:**
- ASSISTANT: Explain results, discuss violations if any
- AUTONOMOUS: Execute analysis, flag anomalies for review

---

### Phase 9: Interpretation

**Agent:** `quality-assurance`

**Entry Requirements:**
- ✅ Analysis complete (Phase 8 exit criteria)

**Activities:**
- Interpret statistical results
- Relate findings to hypotheses
- Assess clinical/practical significance
- Identify limitations
- Suggest future directions

**Exit Criteria:**
- ✅ All hypotheses addressed
- ✅ Effect sizes interpreted (not just p-values)
- ✅ Limitations documented
- ✅ Clinical significance assessed
- ✅ Alternative explanations considered

**Outputs:**
- `docs/interpretation.md`
- `docs/limitations.md`

**Mode Behavior:**
- ASSISTANT: Collaborative interpretation
- AUTONOMOUS: Generate interpretation, flag for human review

---

### Phase 10: Writing

**Agent:** `manuscript-writer`

**Entry Requirements:**
- ✅ Interpretation complete (Phase 9 exit criteria)

**Activities:**
- Write manuscript following IMRaD structure
- Apply reporting guidelines (CONSORT/PRISMA/STROBE)
- Create tables and figures
- Format references

**Exit Criteria:**
- ✅ Complete manuscript (6000-8000 words)
- ✅ Reporting guideline checklist ≥90%
- ✅ All figures/tables referenced
- ✅ References formatted consistently
- ✅ Abstract ≤250 words

**Outputs:**
- `docs/manuscript/manuscript.md`
- `docs/manuscript/abstract.md`
- `results/figures/` (publication-ready)
- `results/tables/` (formatted)

**Mode Behavior:**
- ASSISTANT: Draft sections iteratively, request feedback
- AUTONOMOUS: Generate complete draft for human review

---

### Phase 11: Publication

**Agent:** `quality-assurance`

**Entry Requirements:**
- ✅ Manuscript complete (Phase 10 exit criteria)

**Activities:**
- Final quality checks
- Generate DOI for data/code
- Deposit data in repository
- Submit to journal (human action)

**Exit Criteria:**
- ✅ Data deposited with DOI
- ✅ Code repository public
- ✅ Pre-registration linked
- ✅ Manuscript submitted (human confirms)

**Outputs:**
- DOI for data (Zenodo/OSF)
- DOI for code (GitHub/GitLab)
- Submission confirmation

**Mode Behavior:**
- ASSISTANT: Guide through publication checklist
- AUTONOMOUS: Prepare all materials, remind user to submit

---

## Validation Framework

### Validation Gate Structure

```python
class ValidationGate:
    """Base class for phase validation"""

    def can_enter(self, context: WorkflowContext) -> ValidationResult:
        """Check if phase can be entered"""
        pass

    def can_exit(self, context: WorkflowContext) -> ValidationResult:
        """Check if phase can be exited"""
        pass

    def validate_outputs(self, context: WorkflowContext) -> ValidationResult:
        """Validate phase outputs meet quality standards"""
        pass

class ValidationResult:
    passed: bool
    score: float  # 0.0 - 1.0
    missing_items: List[str]
    warnings: List[str]
    blocking_issues: List[str]
```

### Validation Examples

**FINER Criteria Validator:**
```python
def validate_finer_criteria(problem_statement: str) -> ValidationResult:
    checks = {
        "feasible": check_feasibility(problem_statement),
        "interesting": check_novelty(problem_statement),
        "novel": check_gap_mentioned(problem_statement),
        "ethical": check_no_ethical_concerns(problem_statement),
        "relevant": check_significance(problem_statement)
    }

    score = sum(checks.values()) / len(checks)
    passed = score >= 0.8  # 4/5 criteria

    return ValidationResult(
        passed=passed,
        score=score,
        missing_items=[k for k, v in checks.items() if not v]
    )
```

**PRISMA Validator:**
```python
def validate_prisma_completion(literature_review_path: str) -> ValidationResult:
    checklist = load_prisma_checklist()
    completed_items = check_prisma_items(literature_review_path)

    score = len(completed_items) / 27
    passed = score >= 0.89  # 24/27 items

    return ValidationResult(
        passed=passed,
        score=score,
        missing_items=list(set(checklist) - set(completed_items))
    )
```

---

## Agent Orchestration

### Orchestrator Design

```python
class WorkflowOrchestrator:
    """Orchestrates agent execution for each phase"""

    def __init__(self, mode: Mode):
        self.mode = mode
        self.agents = self._load_agents()

    def execute_phase(self, phase: ResearchPhase, context: WorkflowContext):
        """Execute a research phase using appropriate agent(s)"""

        # Get agent for this phase
        agent = self.agents.get(phase)

        if agent is None:
            # Human-only phase (IRB, Data Collection)
            return self._wait_for_human_completion(phase, context)

        # Prepare agent prompt
        prompt = self._build_agent_prompt(phase, context)

        # Execute agent
        if self.mode == Mode.ASSISTANT:
            result = self._execute_collaborative(agent, prompt, context)
        else:  # AUTONOMOUS
            result = self._execute_autonomous(agent, prompt, context)

        # Validate outputs
        validation = self._validate_phase_outputs(phase, result)

        return result, validation
```

### Phase-to-Agent Mapping

```python
PHASE_AGENTS = {
    ResearchPhase.PROBLEM_FORMULATION: None,  # Direct interaction
    ResearchPhase.LITERATURE_REVIEW: "literature-reviewer",
    ResearchPhase.GAP_ANALYSIS: "gap-analyst",
    ResearchPhase.HYPOTHESIS_FORMATION: "hypothesis-generator",
    ResearchPhase.EXPERIMENTAL_DESIGN: "experiment-designer",
    ResearchPhase.IRB_APPROVAL: None,  # Human-only
    ResearchPhase.DATA_COLLECTION: None,  # Real-world activity
    ResearchPhase.ANALYSIS: "data-analyst",
    ResearchPhase.INTERPRETATION: "quality-assurance",
    ResearchPhase.WRITING: "manuscript-writer",
    ResearchPhase.PUBLICATION: "quality-assurance"
}
```

---

## State Persistence

### Workflow State Structure

```json
{
  "workflow_id": "uuid",
  "created_at": "2025-11-05T12:00:00Z",
  "updated_at": "2025-11-05T14:30:00Z",
  "mode": "ASSISTANT",
  "current_phase": "literature_review",
  "phase_history": [
    {
      "phase": "problem_formulation",
      "entered_at": "2025-11-05T12:00:00Z",
      "exited_at": "2025-11-05T12:45:00Z",
      "validation_score": 0.85,
      "outputs": ["docs/problem_statement.md"]
    }
  ],
  "context": {
    "research_question": "Does exercise reduce depression?",
    "domain": "clinical psychology",
    "resources": {
      "budget": 50000,
      "timeline_months": 18
    }
  },
  "validation_results": {},
  "audit_trail": []
}
```

### Persistence Locations

- `~/.claude/workflow_state.json` - Current state
- `~/.claude/backups/workflow_state_<timestamp>.json` - Backups
- `project/.research_workflow/state.json` - Project-specific state

---

## CLI Interface

### Workflow Commands

```bash
# Initialize new research workflow
claude-research init --mode assistant --question "Your research question"

# Show current phase and status
claude-research status

# Execute current phase
claude-research run

# Move to next phase (if validation passes)
claude-research next

# Go back to previous phase
claude-research back --to hypothesis_formation

# Show validation results
claude-research validate

# Switch mode
claude-research mode --set autonomous

# Show complete workflow history
claude-research history
```

---

## Error Handling

### Common Failure Scenarios

1. **Validation Gate Fails:**
   - ASSISTANT: Show missing items, request human decision (override or fix)
   - AUTONOMOUS: Log failure, retry with adjustments, escalate if persistent

2. **Agent Execution Error:**
   - Save state before agent execution
   - Rollback to pre-execution state
   - Log error details
   - Request human intervention

3. **Missing Dependencies:**
   - Check for required files before phase execution
   - Provide clear error messages
   - Suggest remediation steps

4. **State Corruption:**
   - Maintain backup states (last 10 transitions)
   - Provide rollback command
   - Validate state integrity on load

---

## Testing Strategy

### Unit Tests

- State machine transitions
- Validation gate logic
- Agent orchestration
- State persistence

### Integration Tests

- End-to-end workflow (mocked agents)
- Phase transitions with real validation
- Mode switching mid-workflow
- State persistence and recovery

### End-to-End Tests

- Complete research workflow simulation
- Real agent execution (on test data)
- Quality gate validation
- Publication readiness check

---

## Implementation Plan

### Phase 5.1: Core State Machine
- Implement `ResearchWorkflow` class
- Add transition logic
- Add state persistence
- Unit tests

### Phase 5.2: Validation Gates
- Implement validators for all 11 phases
- Add quality scoring
- Integration tests

### Phase 5.3: Agent Orchestration
- Build `WorkflowOrchestrator`
- Implement phase-to-agent mapping
- Add context passing
- Integration tests

### Phase 5.4: CLI Interface
- Add workflow commands to Claude Code
- Progress tracking
- Status reporting

### Phase 5.5: Testing & Documentation
- Comprehensive test suite
- User guide
- API documentation
- Examples

---

## Success Criteria

Phase 5 complete when:
- ✅ State machine handles all 11 phases
- ✅ All validation gates implemented and tested
- ✅ Agent orchestration functional
- ✅ State persistence working
- ✅ Both ASSISTANT and AUTONOMOUS modes tested
- ✅ End-to-end test passes (simulated research workflow)
- ✅ Documentation complete
- ✅ Zero placeholders (R2)

---

**Architecture Status:** ✅ Design Complete
**Next Step:** Implementation (Phase 5.1)
