"""
Research Workflow State Machine

Manages progression through 11 phases of scientific research workflow.
Enforces validation gates and orchestrates specialized agents.
"""

from typing import Optional, List
from pathlib import Path
import logging

from statemachine import StateMachine, State
from statemachine.exceptions import TransitionNotAllowed

from workflow_context import (
    WorkflowContext,
    ResearchPhase,
    Mode,
    ValidationResult,
    create_backup
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ResearchWorkflow(StateMachine):
    """
    State machine for research workflow progression.

    11 phases from problem formulation to publication.
    Validates transitions and maintains workflow state.
    """

    # Define 11 states
    problem_formulation = State(ResearchPhase.PROBLEM_FORMULATION, initial=True)
    literature_review = State(ResearchPhase.LITERATURE_REVIEW)
    gap_analysis = State(ResearchPhase.GAP_ANALYSIS)
    hypothesis_formation = State(ResearchPhase.HYPOTHESIS_FORMATION)
    experimental_design = State(ResearchPhase.EXPERIMENTAL_DESIGN)
    irb_approval = State(ResearchPhase.IRB_APPROVAL)
    data_collection = State(ResearchPhase.DATA_COLLECTION)
    analysis = State(ResearchPhase.ANALYSIS)
    interpretation = State(ResearchPhase.INTERPRETATION)
    writing = State(ResearchPhase.WRITING)
    publication = State(ResearchPhase.PUBLICATION)

    # Define transitions (forward progression)
    start_literature_review = problem_formulation.to(literature_review)
    start_gap_analysis = literature_review.to(gap_analysis)
    start_hypothesis_formation = gap_analysis.to(hypothesis_formation)
    start_experimental_design = hypothesis_formation.to(experimental_design)
    start_irb_approval = experimental_design.to(irb_approval)
    start_data_collection = (
        irb_approval.to(data_collection) |
        experimental_design.to(data_collection)  # Skip IRB if no human subjects
    )
    start_analysis = data_collection.to(analysis)
    start_interpretation = analysis.to(interpretation)
    start_writing = interpretation.to(writing)
    start_publication = writing.to(publication)

    # Define backward transitions (revisions)
    revise_literature = (
        gap_analysis.to(literature_review) |
        hypothesis_formation.to(literature_review)
    )
    revise_hypothesis = experimental_design.to(hypothesis_formation)
    revise_data_collection = analysis.to(data_collection)
    restart_from_problem = (
        literature_review.to(problem_formulation) |
        gap_analysis.to(problem_formulation) |
        hypothesis_formation.to(problem_formulation) |
        experimental_design.to(problem_formulation)
    )

    def __init__(self, context: Optional[WorkflowContext] = None):
        """
        Initialize workflow state machine.

        Args:
            context: Workflow context (creates new if None)
        """
        self.context = context or WorkflowContext()
        super().__init__()

        # Set initial state from context
        if context:
            self._set_state_from_context()

        logger.info(f"Initialized workflow {self.context.workflow_id}")

    def _set_state_from_context(self):
        """Set state machine to match context's current phase"""
        phase_to_state = {
            ResearchPhase.PROBLEM_FORMULATION: self.problem_formulation,
            ResearchPhase.LITERATURE_REVIEW: self.literature_review,
            ResearchPhase.GAP_ANALYSIS: self.gap_analysis,
            ResearchPhase.HYPOTHESIS_FORMATION: self.hypothesis_formation,
            ResearchPhase.EXPERIMENTAL_DESIGN: self.experimental_design,
            ResearchPhase.IRB_APPROVAL: self.irb_approval,
            ResearchPhase.DATA_COLLECTION: self.data_collection,
            ResearchPhase.ANALYSIS: self.analysis,
            ResearchPhase.INTERPRETATION: self.interpretation,
            ResearchPhase.WRITING: self.writing,
            ResearchPhase.PUBLICATION: self.publication,
        }
        target_state = phase_to_state[self.context.current_phase]
        self.current_state = target_state

    def get_phase_name(self) -> str:
        """Get human-readable name of current phase"""
        return self.current_state.value.replace("_", " ").title()

    def can_progress(self) -> bool:
        """Check if workflow can progress to next phase"""
        if self.current_state == self.publication:
            return False  # Final state

        # Check if current phase is complete
        current_phase = ResearchPhase(self.current_state.value)
        return self.context.has_completed_phase(current_phase)

    def get_next_phase(self) -> Optional[ResearchPhase]:
        """Get the next phase in linear progression"""
        phases = list(ResearchPhase)
        current_index = self.context.get_current_phase_index()

        if current_index < len(phases) - 1:
            return phases[current_index + 1]
        return None

    def progress_to_next(self, skip_irb: bool = False) -> bool:
        """
        Progress to next phase if validation passes.

        Args:
            skip_irb: Skip IRB approval phase (no human subjects)

        Returns:
            True if progression succeeded, False otherwise
        """
        # Create backup before transition
        create_backup(self.context)

        # Determine next transition
        current = self.current_state

        try:
            if current == self.problem_formulation:
                self.start_literature_review()
                return True

            elif current == self.literature_review:
                self.start_gap_analysis()
                return True

            elif current == self.gap_analysis:
                self.start_hypothesis_formation()
                return True

            elif current == self.hypothesis_formation:
                self.start_experimental_design()
                return True

            elif current == self.experimental_design:
                if skip_irb:
                    self.start_data_collection()
                else:
                    self.start_irb_approval()
                return True

            elif current == self.irb_approval:
                self.start_data_collection()
                return True

            elif current == self.data_collection:
                self.start_analysis()
                return True

            elif current == self.analysis:
                self.start_interpretation()
                return True

            elif current == self.interpretation:
                self.start_writing()
                return True

            elif current == self.writing:
                self.start_publication()
                return True

            elif current == self.publication:
                logger.info("Already at final phase (Publication)")
                return False

            return False

        except TransitionNotAllowed as e:
            logger.error(f"Transition not allowed: {e}")
            return False

    def go_back_to(self, phase: ResearchPhase) -> bool:
        """
        Go back to a previous phase for revision.

        Args:
            phase: Target phase to return to

        Returns:
            True if successful, False otherwise
        """
        current = self.current_state
        target_phase = phase

        try:
            # Check if backward transition is allowed
            if target_phase == ResearchPhase.LITERATURE_REVIEW:
                if current in [self.gap_analysis, self.hypothesis_formation]:
                    self.revise_literature()
                    return True

            elif target_phase == ResearchPhase.HYPOTHESIS_FORMATION:
                if current == self.experimental_design:
                    self.revise_hypothesis()
                    return True

            elif target_phase == ResearchPhase.DATA_COLLECTION:
                if current == self.analysis:
                    self.revise_data_collection()
                    return True

            elif target_phase == ResearchPhase.PROBLEM_FORMULATION:
                if current in [
                    self.literature_review,
                    self.gap_analysis,
                    self.hypothesis_formation,
                    self.experimental_design
                ]:
                    self.restart_from_problem()
                    return True

            logger.warning(
                f"Backward transition from {current.value} to {target_phase.value} "
                f"not allowed"
            )
            return False

        except TransitionNotAllowed as e:
            logger.error(f"Transition not allowed: {e}")
            return False

    def get_allowed_transitions(self) -> List[str]:
        """Get list of allowed transitions from current state"""
        transitions = []
        for transition in self.current_state.transitions:
            # Get transition name (different versions of python-statemachine use different attrs)
            name = getattr(transition, 'identifier', None) or getattr(transition, 'name', str(transition))
            transitions.append(name)
        return transitions

    def get_progress_percentage(self) -> float:
        """Calculate workflow completion percentage"""
        total_phases = len(list(ResearchPhase))
        completed = sum(
            1 for phase in ResearchPhase
            if self.context.has_completed_phase(phase)
        )
        return (completed / total_phases) * 100

    def save_state(self, filepath: Optional[Path] = None):
        """Save current workflow state"""
        self.context.current_phase = ResearchPhase(self.current_state.value)
        self.context.save(filepath)

    @classmethod
    def load_state(cls, filepath: Path) -> "ResearchWorkflow":
        """Load workflow from saved state"""
        context = WorkflowContext.load(filepath)
        return cls(context=context)

    def summary(self) -> dict:
        """Get workflow summary"""
        return {
            "workflow_id": self.context.workflow_id,
            "mode": self.context.mode.value,
            "current_phase": self.get_phase_name(),
            "progress": f"{self.get_progress_percentage():.1f}%",
            "completed_phases": sum(
                1 for phase in ResearchPhase
                if self.context.has_completed_phase(phase)
            ),
            "total_phases": len(list(ResearchPhase)),
            "can_progress": self.can_progress(),
            "allowed_transitions": self.get_allowed_transitions()
        }

    # Transition hooks (called on state changes)
    def on_enter_state(self, state, event):
        """Called when entering any state"""
        phase = ResearchPhase(state.value)
        logger.info(f"Entering phase: {phase.value}")
        self.context.add_audit_entry(
            "state_entered",
            {"phase": phase.value, "event": event}
        )

    def on_exit_state(self, state, event):
        """Called when exiting any state"""
        phase = ResearchPhase(state.value)
        logger.info(f"Exiting phase: {phase.value}")
        self.context.add_audit_entry(
            "state_exited",
            {"phase": phase.value, "event": event}
        )


def create_workflow(
    research_question: str,
    domain: str = "",
    mode: Mode = Mode.ASSISTANT,
    project_root: Optional[Path] = None
) -> ResearchWorkflow:
    """
    Create a new research workflow.

    Args:
        research_question: The research question to investigate
        domain: Research domain (e.g., "clinical psychology")
        mode: Operation mode (ASSISTANT or AUTONOMOUS)
        project_root: Project root directory

    Returns:
        Initialized ResearchWorkflow
    """
    context = WorkflowContext(
        research_question=research_question,
        domain=domain,
        mode=mode,
        project_root=project_root or Path.cwd()
    )

    workflow = ResearchWorkflow(context=context)

    # Start first phase
    context.start_phase(ResearchPhase.PROBLEM_FORMULATION)

    logger.info(f"Created new workflow: {context.workflow_id}")
    logger.info(f"Research question: {research_question}")
    logger.info(f"Mode: {mode.value}")

    return workflow


if __name__ == "__main__":
    # Example usage
    print("Research Workflow State Machine")
    print("=" * 80)

    # Create new workflow
    workflow = create_workflow(
        research_question="Does exercise reduce depression in college students?",
        domain="clinical psychology",
        mode=Mode.ASSISTANT
    )

    # Show summary
    print("\nWorkflow Summary:")
    for key, value in workflow.summary().items():
        print(f"  {key}: {value}")

    # Show allowed transitions
    print(f"\nCurrent phase: {workflow.get_phase_name()}")
    print(f"Allowed transitions: {workflow.get_allowed_transitions()}")

    # Simulate progression
    print("\nSimulating phase progression...")
    phases_completed = 0

    while phases_completed < 5:  # Simulate first 5 phases
        current_phase = ResearchPhase(workflow.current_state.value)

        # Mark phase as complete (simulation)
        validation = ValidationResult(passed=True, score=0.95)
        workflow.context.complete_phase(validation, outputs=[f"output_{current_phase.value}.md"])

        # Progress to next
        if workflow.progress_to_next():
            phases_completed += 1
            print(f"  → Advanced to: {workflow.get_phase_name()}")
        else:
            print(f"  ! Cannot progress from {workflow.get_phase_name()}")
            break

    # Final summary
    print("\nFinal Summary:")
    for key, value in workflow.summary().items():
        print(f"  {key}: {value}")

    # Save state
    save_path = Path("/tmp/workflow_state.json")
    workflow.save_state(save_path)
    print(f"\nWorkflow state saved to: {save_path}")
