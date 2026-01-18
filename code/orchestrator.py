"""
Workflow Orchestrator

Orchestrates agent execution for each research phase.
Manages transitions between phases and validates outputs.
"""

from typing import Optional, Dict, Any
from pathlib import Path
import logging
import sys
import json

sys.path.insert(0, str(Path(__file__).parent))

from workflow_context import WorkflowContext, ResearchPhase, Mode, ValidationResult
from research_workflow import ResearchWorkflow
from validators import FINERValidator, PRISMAValidator, NIHRigorValidator

logger = logging.getLogger(__name__)


# Agent specifications from settings.json
AGENT_SPECS = {
    "literature-reviewer": {
        "path": ".claude/agents/literature-reviewer.md",
        "description": "PRISMA 2020 systematic literature reviews",
        "subagent_type": "literature-reviewer"  # Registered agent type
    },
    "gap-analyst": {
        "path": ".claude/agents/gap-analyst.md",
        "description": "Research gap identification and prioritization",
        "subagent_type": "gap-analyst"
    },
    "hypothesis-generator": {
        "path": ".claude/agents/hypothesis-generator.md",
        "description": "Generate testable hypotheses using Tree-of-Thought",
        "subagent_type": "hypothesis-generator"
    },
    "experiment-designer": {
        "path": ".claude/agents/experiment-designer.md",
        "description": "NIH-rigorous experimental design",
        "subagent_type": "experiment-designer"
    },
    "data-analyst": {
        "path": ".claude/agents/data-analyst.md",
        "description": "Reproducible statistical analysis",
        "subagent_type": "data-analyst"
    },
    "manuscript-writer": {
        "path": ".claude/agents/manuscript-writer.md",
        "description": "CONSORT/PRISMA-compliant manuscript writing",
        "subagent_type": "manuscript-writer"
    },
    "citation-manager": {
        "path": ".claude/agents/citation-manager.md",
        "description": "Citation management and verification",
        "subagent_type": "citation-manager"
    },
    "quality-assurance": {
        "path": ".claude/agents/quality-assurance.md",
        "description": "Research quality validation and audits",
        "subagent_type": "quality-assurance"
    },
    "meta-reviewer": {
        "path": ".claude/agents/meta-reviewer.md",
        "description": "AMSTAR 2 quality assessment for systematic reviews",
        "subagent_type": "meta-reviewer"
    },
    "code-reviewer": {
        "path": ".claude/agents/code-reviewer.md",
        "description": "Statistical code verification for reproducibility",
        "subagent_type": "code-reviewer"
    }
}


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

    def load_agent_spec(self, agent_name: str) -> Optional[Dict[str, Any]]:
        """
        Load agent specification from file.

        Args:
            agent_name: Name of the agent

        Returns:
            Agent specification dictionary or None if not found
        """
        if agent_name not in AGENT_SPECS:
            logger.warning(f"Unknown agent: {agent_name}")
            return None

        spec = AGENT_SPECS[agent_name].copy()
        agent_path = self.context.project_root / spec["path"]

        if agent_path.exists():
            try:
                with open(agent_path, 'r') as f:
                    spec["prompt_content"] = f.read()
                spec["loaded"] = True
                logger.info(f"Loaded agent spec: {agent_name} from {agent_path}")
            except Exception as e:
                logger.error(f"Failed to load agent spec {agent_name}: {e}")
                spec["loaded"] = False
                spec["error"] = str(e)
        else:
            logger.warning(f"Agent spec file not found: {agent_path}")
            spec["loaded"] = False
            spec["error"] = f"File not found: {agent_path}"

        return spec

    def generate_task_invocation(
        self,
        agent_name: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate Task tool invocation parameters for an agent.

        This creates the structured parameters needed to invoke the Task tool
        with the specified agent.

        Args:
            agent_name: Name of the agent to invoke
            params: Optional parameters to pass to the agent

        Returns:
            Dictionary with Task tool parameters:
            {
                "subagent_type": str,
                "description": str,
                "prompt": str,
                "ready": bool,
                "error": str (if not ready)
            }
        """
        spec = self.load_agent_spec(agent_name)

        if spec is None:
            return {
                "ready": False,
                "error": f"Unknown agent: {agent_name}"
            }

        if not spec.get("loaded", False):
            return {
                "ready": False,
                "error": spec.get("error", "Failed to load agent specification")
            }

        # Build the prompt with context
        context_section = f"""
## Research Context

**Research Question:** {self.context.research_question}
**Domain:** {self.context.domain}
**Mode:** {self.context.mode.value}
**Current Phase:** {self.workflow.current_state.value}
**Project Root:** {self.context.project_root}
"""

        # Add parameters if provided
        params_section = ""
        if params:
            params_section = f"""
## Task Parameters

```json
{json.dumps(params, indent=2)}
```
"""

        # Combine prompt components
        full_prompt = f"""{spec.get('prompt_content', '')}

{context_section}
{params_section}

Execute this task according to the agent specification above.
"""

        return {
            "subagent_type": spec.get("subagent_type", "general-purpose"),
            "description": f"{agent_name}: {spec.get('description', 'Research agent')}",
            "prompt": full_prompt,
            "ready": True
        }

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

        # Generate Task tool invocation parameters
        logger.info(f"Phase {phase.value} uses agent: {agent}")

        task_params = self.generate_task_invocation(
            agent_name=agent,
            params={
                "phase": phase.value,
                "mode": self.context.mode.value,
                "research_question": self.context.research_question,
                "domain": self.context.domain
            }
        )

        if not task_params.get("ready", False):
            logger.error(f"Failed to prepare agent {agent}: {task_params.get('error')}")
            return {
                "success": False,
                "phase": phase.value,
                "agent": agent,
                "error": task_params.get("error"),
                "mode": self.context.mode.value
            }

        return {
            "success": True,
            "phase": phase.value,
            "agent": agent,
            "task_invocation": task_params,
            "message": f"Agent {agent} ready for execution via Task tool",
            "mode": self.context.mode.value,
            "usage": (
                "Invoke with Task tool using:\n"
                f"  subagent_type: {task_params['subagent_type']}\n"
                f"  description: {task_params['description']}\n"
                f"  prompt: <see task_invocation.prompt>"
            )
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
