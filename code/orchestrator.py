"""
Workflow Orchestrator

Orchestrates agent execution for each research phase.
Manages transitions between phases and validates outputs.
"""

from typing import Optional, Dict
from pathlib import Path
import logging
import sys

sys.path.insert(0, str(Path(__file__).parent))

from workflow_context import WorkflowContext, ResearchPhase, Mode, ValidationResult
from research_workflow import ResearchWorkflow
from validators import FINERValidator, PRISMAValidator, NIHRigorValidator

logger = logging.getLogger(__name__)


class WorkflowOrchestrator:
    """
    Orchestrates the research workflow.

    Manages:
    - Agent invocation for each phase
    - Validation gates
    - Phase transitions
    - Mode-aware behavior
    """

    # Map phases to their validators
    PHASE_VALIDATORS = {
        ResearchPhase.PROBLEM_FORMULATION: FINERValidator,
        ResearchPhase.LITERATURE_REVIEW: PRISMAValidator,
        ResearchPhase.EXPERIMENTAL_DESIGN: NIHRigorValidator,
        # Add more validators here as they're implemented
    }

    # Map phases to their agents
    PHASE_AGENTS = {
        ResearchPhase.PROBLEM_FORMULATION: None,  # Direct interaction
        ResearchPhase.LITERATURE_REVIEW: "literature-reviewer",
        ResearchPhase.GAP_ANALYSIS: "gap-analyst",
        ResearchPhase.HYPOTHESIS_FORMATION: "hypothesis-generator",
        ResearchPhase.EXPERIMENTAL_DESIGN: "experiment-designer",
        ResearchPhase.IRB_APPROVAL: None,  # Human-only phase
        ResearchPhase.DATA_COLLECTION: None,  # Real-world activity
        ResearchPhase.ANALYSIS: "data-analyst",
        ResearchPhase.INTERPRETATION: "quality-assurance",
        ResearchPhase.WRITING: "manuscript-writer",
        ResearchPhase.PUBLICATION: "quality-assurance"
    }

    def __init__(self, workflow: ResearchWorkflow):
        """
        Initialize orchestrator with workflow.

        Args:
            workflow: ResearchWorkflow state machine
        """
        self.workflow = workflow
        self.context = workflow.context

    def get_validator(self, phase: ResearchPhase) -> Optional[object]:
        """Get validator for a specific phase"""
        validator_class = self.PHASE_VALIDATORS.get(phase)
        if validator_class:
            return validator_class(self.context)
        return None

    def get_agent(self, phase: ResearchPhase) -> Optional[str]:
        """Get agent name for a specific phase"""
        return self.PHASE_AGENTS.get(phase)

    def validate_entry(self, phase: ResearchPhase) -> ValidationResult:
        """
        Validate entry requirements for a phase.

        Args:
            phase: Phase to validate entry for

        Returns:
            ValidationResult indicating if phase can be entered
        """
        validator = self.get_validator(phase)
        if validator:
            return validator.can_enter()

        # No validator = always allow entry
        return ValidationResult(passed=True, score=1.0)

    def validate_exit(self, phase: ResearchPhase) -> ValidationResult:
        """
        Validate exit criteria for a phase.

        Args:
            phase: Phase to validate exit from

        Returns:
            ValidationResult indicating if phase is complete
        """
        validator = self.get_validator(phase)
        if validator:
            return validator.can_exit()

        # No validator = assume complete if in phase history
        is_complete = self.context.has_completed_phase(phase)
        return ValidationResult(
            passed=is_complete,
            score=1.0 if is_complete else 0.0,
            warnings=["No validator for this phase"]
        )

    def can_progress(self) -> bool:
        """
        Check if workflow can progress to next phase.

        Returns:
            True if current phase is complete and can advance
        """
        current_phase = ResearchPhase(self.workflow.current_state.value)

        # Validate exit from current phase
        validation = self.validate_exit(current_phase)

        return validation.passed

    def execute_phase(self, phase: Optional[ResearchPhase] = None) -> Dict:
        """
        Execute a research phase.

        Args:
            phase: Phase to execute (uses current if None)

        Returns:
            Dictionary with execution results
        """
        if phase is None:
            phase = ResearchPhase(self.workflow.current_state.value)

        logger.info(f"Executing phase: {phase.value}")

        # Check entry requirements
        entry_validation = self.validate_entry(phase)
        if not entry_validation.passed:
            logger.error(f"Cannot enter phase {phase.value}: {entry_validation.blocking_issues}")
            return {
                "success": False,
                "phase": phase.value,
                "error": "Entry requirements not met",
                "validation": entry_validation
            }

        # Get agent for this phase
        agent = self.get_agent(phase)

        if agent is None:
            # Human-only or direct interaction phase
            logger.info(f"Phase {phase.value} requires human interaction")
            return {
                "success": True,
                "phase": phase.value,
                "agent": None,
                "message": "Human interaction required",
                "mode": self.context.mode.value
            }

        # In actual implementation, would invoke agent here via Claude Code
        # For now, return agent invocation info
        logger.info(f"Phase {phase.value} uses agent: {agent}")

        return {
            "success": True,
            "phase": phase.value,
            "agent": agent,
            "message": f"Agent {agent} ready for execution",
            "mode": self.context.mode.value
        }

    def advance_workflow(self, skip_irb: bool = False) -> Dict:
        """
        Advance workflow to next phase if validation passes.

        Args:
            skip_irb: Skip IRB approval phase (no human subjects)

        Returns:
            Dictionary with advancement results
        """
        current_phase = ResearchPhase(self.workflow.current_state.value)

        # Validate current phase completion
        validation = self.validate_exit(current_phase)

        if not validation.passed:
            logger.warning(f"Cannot advance: {current_phase.value} validation failed")
            return {
                "success": False,
                "current_phase": current_phase.value,
                "error": "Current phase validation failed",
                "validation": validation
            }

        # Mark current phase as complete
        # Get outputs (simplified - would scan output directories in real implementation)
        outputs = self._get_phase_outputs(current_phase)
        self.context.complete_phase(validation, outputs)

        # Attempt to progress
        success = self.workflow.progress_to_next(skip_irb=skip_irb)

        if success:
            new_phase = ResearchPhase(self.workflow.current_state.value)
            logger.info(f"Advanced from {current_phase.value} to {new_phase.value}")

            return {
                "success": True,
                "from_phase": current_phase.value,
                "to_phase": new_phase.value,
                "progress": self.workflow.get_progress_percentage()
            }
        else:
            logger.error(f"Failed to advance from {current_phase.value}")
            return {
                "success": False,
                "current_phase": current_phase.value,
                "error": "State transition failed"
            }

    def _get_phase_outputs(self, phase: ResearchPhase) -> list:
        """
        Get list of outputs for a phase.

        In real implementation, would scan project directories.
        For now, returns placeholder based on phase.
        """
        output_map = {
            ResearchPhase.PROBLEM_FORMULATION: ["docs/problem_statement.md"],
            ResearchPhase.LITERATURE_REVIEW: [
                "data/literature/search_results.csv",
                "data/literature/included_studies.csv"
            ],
            ResearchPhase.GAP_ANALYSIS: ["docs/gap_analysis.md"],
            ResearchPhase.HYPOTHESIS_FORMATION: ["docs/hypotheses.md"],
            ResearchPhase.EXPERIMENTAL_DESIGN: [
                "docs/experimental_protocol.md",
                "docs/power_analysis.md",
                "code/randomization.py"
            ],
        }

        return output_map.get(phase, [f"output_{phase.value}.md"])

    def get_workflow_status(self) -> Dict:
        """Get current workflow status"""
        current_phase = ResearchPhase(self.workflow.current_state.value)
        agent = self.get_agent(current_phase)
        can_advance = self.can_progress()

        return {
            "workflow_id": self.context.workflow_id,
            "mode": self.context.mode.value,
            "current_phase": current_phase.value,
            "current_agent": agent,
            "can_advance": can_advance,
            "progress_percentage": self.workflow.get_progress_percentage(),
            "completed_phases": sum(
                1 for phase in ResearchPhase
                if self.context.has_completed_phase(phase)
            ),
            "total_phases": len(list(ResearchPhase))
        }


def create_orchestrator(
    research_question: str,
    domain: str = "",
    mode: Mode = Mode.ASSISTANT,
    project_root: Optional[Path] = None
) -> WorkflowOrchestrator:
    """
    Create a new workflow orchestrator.

    Args:
        research_question: Research question to investigate
        domain: Research domain
        mode: Operation mode (ASSISTANT or AUTONOMOUS)
        project_root: Project root directory

    Returns:
        Initialized WorkflowOrchestrator
    """
    from research_workflow import create_workflow

    workflow = create_workflow(
        research_question=research_question,
        domain=domain,
        mode=mode,
        project_root=project_root
    )

    return WorkflowOrchestrator(workflow)


if __name__ == "__main__":
    # Example usage
    print("Research Workflow Orchestrator")
    print("=" * 80)

    # Create orchestrator
    orchestrator = create_orchestrator(
        research_question="Does exercise reduce depression in college students?",
        domain="clinical psychology",
        mode=Mode.ASSISTANT
    )

    # Show status
    status = orchestrator.get_workflow_status()
    print("\nWorkflow Status:")
    for key, value in status.items():
        print(f"  {key}: {value}")

    # Show current phase agent
    current_phase = ResearchPhase(orchestrator.workflow.current_state.value)
    print(f"\nCurrent phase: {current_phase.value}")
    print(f"Agent: {orchestrator.get_agent(current_phase) or 'Human interaction'}")

    # Test validation
    print("\nValidating entry to current phase...")
    entry_validation = orchestrator.validate_entry(current_phase)
    print(f"  Can enter: {entry_validation.passed}")
    print(f"  Score: {entry_validation.score}")
