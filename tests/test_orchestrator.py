"""
Tests for Workflow Orchestrator

Tests orchestration of research workflow phases, validation, and agent mapping.
"""

import pytest
from pathlib import Path
import sys

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from orchestrator import WorkflowOrchestrator, create_orchestrator
from research_workflow import ResearchWorkflow, create_workflow
from workflow_context import WorkflowContext, ResearchPhase, Mode, ValidationResult
from validators import FINERValidator, PRISMAValidator, NIHRigorValidator


class TestOrchestratorInitialization:
    """Test orchestrator creation and initialization"""

    def test_create_with_workflow(self):
        """Test creating orchestrator with workflow"""
        workflow = create_workflow(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )
        orchestrator = WorkflowOrchestrator(workflow)

        assert orchestrator.workflow == workflow
        assert orchestrator.context == workflow.context
        assert isinstance(orchestrator.context, WorkflowContext)

    def test_create_via_factory(self):
        """Test creating orchestrator via factory function"""
        orchestrator = create_orchestrator(
            research_question="Does X affect Y?",
            domain="test domain",
            mode=Mode.AUTONOMOUS
        )

        assert isinstance(orchestrator, WorkflowOrchestrator)
        assert isinstance(orchestrator.workflow, ResearchWorkflow)
        assert orchestrator.context.research_question == "Does X affect Y?"
        assert orchestrator.context.domain == "test domain"
        assert orchestrator.context.mode == Mode.AUTONOMOUS

    def test_phase_validators_mapping(self):
        """Test that phase validators are properly mapped"""
        assert WorkflowOrchestrator.PHASE_VALIDATORS[ResearchPhase.PROBLEM_FORMULATION] == FINERValidator
        assert WorkflowOrchestrator.PHASE_VALIDATORS[ResearchPhase.LITERATURE_REVIEW] == PRISMAValidator
        assert WorkflowOrchestrator.PHASE_VALIDATORS[ResearchPhase.EXPERIMENTAL_DESIGN] == NIHRigorValidator

    def test_phase_agents_mapping(self):
        """Test that phase agents are properly mapped"""
        agents = WorkflowOrchestrator.PHASE_AGENTS

        assert agents[ResearchPhase.PROBLEM_FORMULATION] is None  # Direct interaction
        assert agents[ResearchPhase.LITERATURE_REVIEW] == "literature-reviewer"
        assert agents[ResearchPhase.GAP_ANALYSIS] == "gap-analyst"
        assert agents[ResearchPhase.HYPOTHESIS_FORMATION] == "hypothesis-generator"
        assert agents[ResearchPhase.EXPERIMENTAL_DESIGN] == "experiment-designer"
        assert agents[ResearchPhase.IRB_APPROVAL] is None  # Human-only
        assert agents[ResearchPhase.DATA_COLLECTION] is None  # Real-world
        assert agents[ResearchPhase.ANALYSIS] == "data-analyst"
        assert agents[ResearchPhase.INTERPRETATION] == "quality-assurance"
        assert agents[ResearchPhase.WRITING] == "manuscript-writer"
        assert agents[ResearchPhase.PUBLICATION] == "quality-assurance"


class TestValidatorAccess:
    """Test validator access methods"""

    def test_get_validator_for_phase_with_validator(self):
        """Test getting validator for phase that has one"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        validator = orchestrator.get_validator(ResearchPhase.PROBLEM_FORMULATION)

        assert validator is not None
        assert isinstance(validator, FINERValidator)

    def test_get_validator_for_phase_without_validator(self):
        """Test getting validator for phase that doesn't have one"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        validator = orchestrator.get_validator(ResearchPhase.DATA_COLLECTION)

        assert validator is None

    def test_validator_receives_context(self):
        """Test that validators are initialized with context"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        validator = orchestrator.get_validator(ResearchPhase.PROBLEM_FORMULATION)

        assert validator is not None
        assert hasattr(validator, 'context')
        assert validator.context == orchestrator.context


class TestAgentAccess:
    """Test agent access methods"""

    def test_get_agent_for_phase_with_agent(self):
        """Test getting agent for phase that has one"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        agent = orchestrator.get_agent(ResearchPhase.LITERATURE_REVIEW)

        assert agent == "literature-reviewer"

    def test_get_agent_for_human_only_phase(self):
        """Test getting agent for human-only phase"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        agent = orchestrator.get_agent(ResearchPhase.IRB_APPROVAL)

        assert agent is None

    def test_get_agent_for_all_phases(self):
        """Test that all phases have agent mapping"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        for phase in ResearchPhase:
            agent = orchestrator.get_agent(phase)
            # agent can be None or str, but key must exist
            assert agent is None or isinstance(agent, str)


class TestValidation:
    """Test validation methods"""

    def test_validate_entry_with_validator(self):
        """Test validating entry to phase with validator"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        result = orchestrator.validate_entry(ResearchPhase.PROBLEM_FORMULATION)

        assert isinstance(result, ValidationResult)
        assert isinstance(result.passed, bool)
        assert isinstance(result.score, float)

    def test_validate_entry_without_validator(self):
        """Test validating entry to phase without validator"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        result = orchestrator.validate_entry(ResearchPhase.DATA_COLLECTION)

        assert isinstance(result, ValidationResult)
        assert result.passed is True  # No validator = always allow
        assert result.score == 1.0

    def test_validate_exit_with_validator(self):
        """Test validating exit from phase with validator"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        result = orchestrator.validate_exit(ResearchPhase.PROBLEM_FORMULATION)

        assert isinstance(result, ValidationResult)
        assert isinstance(result.passed, bool)
        assert isinstance(result.score, float)

    def test_validate_exit_without_validator(self):
        """Test validating exit from phase without validator"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        result = orchestrator.validate_exit(ResearchPhase.DATA_COLLECTION)

        assert isinstance(result, ValidationResult)
        # Without validator, checks if phase completed
        assert isinstance(result.passed, bool)
        assert len(result.warnings) > 0  # Should warn about missing validator

    def test_can_progress(self):
        """Test checking if workflow can progress"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        can_progress = orchestrator.can_progress()

        assert isinstance(can_progress, bool)


class TestPhaseExecution:
    """Test phase execution"""

    def test_execute_current_phase(self):
        """Test executing current phase"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        result = orchestrator.execute_phase()

        assert isinstance(result, dict)
        assert "success" in result
        assert "phase" in result
        assert result["phase"] == ResearchPhase.PROBLEM_FORMULATION.value

    def test_execute_specific_phase_with_agent(self):
        """Test executing specific phase that has agent"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        # Cannot execute literature_review without completing problem_formulation first
        result = orchestrator.execute_phase(ResearchPhase.LITERATURE_REVIEW)

        assert result["success"] is False  # Entry validation fails
        assert result["phase"] == ResearchPhase.LITERATURE_REVIEW.value
        assert "error" in result
        assert "Entry requirements not met" in result["error"]

    def test_execute_human_only_phase(self):
        """Test executing human-only phase"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        result = orchestrator.execute_phase(ResearchPhase.IRB_APPROVAL)

        assert result["success"] is True
        assert result["phase"] == ResearchPhase.IRB_APPROVAL.value
        assert result["agent"] is None
        assert "Human interaction" in result["message"]

    def test_execute_phase_includes_mode(self):
        """Test that phase execution includes mode"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.AUTONOMOUS
        )

        result = orchestrator.execute_phase()

        assert "mode" in result
        assert result["mode"] == Mode.AUTONOMOUS.value


class TestWorkflowAdvancement:
    """Test workflow advancement"""

    def test_get_phase_outputs(self):
        """Test getting phase outputs"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        outputs = orchestrator._get_phase_outputs(ResearchPhase.PROBLEM_FORMULATION)

        assert isinstance(outputs, list)
        assert len(outputs) > 0
        assert all(isinstance(o, str) for o in outputs)

    def test_get_phase_outputs_literature_review(self):
        """Test getting outputs for literature review phase"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        outputs = orchestrator._get_phase_outputs(ResearchPhase.LITERATURE_REVIEW)

        assert len(outputs) >= 2
        assert any("search_results" in o for o in outputs)
        assert any("included_studies" in o for o in outputs)

    def test_get_phase_outputs_unknown_phase(self):
        """Test getting outputs for phase without defined outputs"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        outputs = orchestrator._get_phase_outputs(ResearchPhase.IRB_APPROVAL)

        assert isinstance(outputs, list)
        assert len(outputs) > 0  # Should have default output


class TestWorkflowStatus:
    """Test workflow status reporting"""

    def test_get_workflow_status(self):
        """Test getting complete workflow status"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            domain="test",
            mode=Mode.ASSISTANT
        )

        status = orchestrator.get_workflow_status()

        assert isinstance(status, dict)
        assert "workflow_id" in status
        assert "mode" in status
        assert "current_phase" in status
        assert "current_agent" in status
        assert "can_advance" in status
        assert "progress_percentage" in status
        assert "completed_phases" in status
        assert "total_phases" in status

    def test_workflow_status_initial_state(self):
        """Test workflow status at initial state"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        status = orchestrator.get_workflow_status()

        assert status["current_phase"] == ResearchPhase.PROBLEM_FORMULATION.value
        assert status["completed_phases"] == 0
        assert status["total_phases"] == len(list(ResearchPhase))
        assert status["progress_percentage"] == 0.0

    def test_workflow_status_mode(self):
        """Test workflow status includes correct mode"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.AUTONOMOUS
        )

        status = orchestrator.get_workflow_status()

        assert status["mode"] == Mode.AUTONOMOUS.value

    def test_workflow_status_agent(self):
        """Test workflow status shows current agent"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )

        status = orchestrator.get_workflow_status()

        # Problem formulation has no agent
        assert status["current_agent"] is None


class TestIntegration:
    """Integration tests for orchestrator"""

    def test_orchestrator_workflow_integration(self):
        """Test that orchestrator properly integrates with workflow"""
        orchestrator = create_orchestrator(
            research_question="Integration test question?",
            domain="test domain",
            mode=Mode.ASSISTANT
        )

        # Verify workflow is properly initialized
        assert orchestrator.workflow is not None
        assert orchestrator.context is not None

        # Verify workflow state matches orchestrator
        workflow_phase = ResearchPhase(orchestrator.workflow.current_state.value)
        status = orchestrator.get_workflow_status()
        assert status["current_phase"] == workflow_phase.value

    def test_full_orchestrator_lifecycle(self):
        """Test complete orchestrator lifecycle"""
        orchestrator = create_orchestrator(
            research_question="Lifecycle test?",
            mode=Mode.ASSISTANT
        )

        # 1. Check initial status
        status = orchestrator.get_workflow_status()
        assert status["completed_phases"] == 0

        # 2. Execute current phase
        result = orchestrator.execute_phase()
        assert result["success"] is True

        # 3. Check if can progress
        can_progress = orchestrator.can_progress()
        assert isinstance(can_progress, bool)

        # 4. Get workflow status again
        status = orchestrator.get_workflow_status()
        assert "current_phase" in status
        assert "progress_percentage" in status
