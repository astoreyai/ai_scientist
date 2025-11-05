"""
Unit tests for Research Workflow State Machine
"""

import pytest
import json
from pathlib import Path
import sys

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from workflow_context import (
    WorkflowContext,
    ResearchPhase,
    Mode,
    ValidationResult,
    PhaseRecord
)
from research_workflow import ResearchWorkflow, create_workflow


class TestWorkflowContext:
    """Test WorkflowContext functionality"""

    def test_create_context(self):
        """Test context creation"""
        context = WorkflowContext(
            research_question="Test question",
            domain="test domain",
            mode=Mode.ASSISTANT
        )

        assert context.research_question == "Test question"
        assert context.domain == "test domain"
        assert context.mode == Mode.ASSISTANT
        assert context.current_phase == ResearchPhase.PROBLEM_FORMULATION

    def test_phase_tracking(self):
        """Test phase start/complete tracking"""
        context = WorkflowContext()

        # Start a phase
        context.start_phase(ResearchPhase.LITERATURE_REVIEW, agent="literature-reviewer")
        assert context.current_phase == ResearchPhase.LITERATURE_REVIEW
        assert len(context.phase_history) == 1

        # Complete the phase
        validation = ValidationResult(passed=True, score=0.95)
        context.complete_phase(validation, outputs=["output1.md", "output2.csv"])

        assert context.phase_history[0].validation_score == 0.95
        assert len(context.phase_history[0].outputs) == 2
        assert context.has_completed_phase(ResearchPhase.LITERATURE_REVIEW)

    def test_audit_trail(self):
        """Test audit trail logging"""
        context = WorkflowContext()

        context.add_audit_entry("test_action", {"detail": "value"})

        assert len(context.audit_trail) == 1
        assert context.audit_trail[0]["action"] == "test_action"
        assert context.audit_trail[0]["details"]["detail"] == "value"

    def test_serialization(self):
        """Test context serialization/deserialization"""
        context = WorkflowContext(
            research_question="Test",
            mode=Mode.AUTONOMOUS
        )

        # Add some data
        context.start_phase(ResearchPhase.LITERATURE_REVIEW)
        validation = ValidationResult(passed=True, score=0.9)
        context.complete_phase(validation, outputs=["test.md"])

        # Serialize
        data = context.to_dict()
        assert isinstance(data, dict)
        assert data["research_question"] == "Test"
        assert data["mode"] == "autonomous"

        # Deserialize
        restored = WorkflowContext.from_dict(data)
        assert restored.research_question == context.research_question
        assert restored.mode == context.mode
        assert restored.current_phase == context.current_phase
        assert len(restored.phase_history) == len(context.phase_history)


class TestResearchWorkflow:
    """Test ResearchWorkflow state machine"""

    def test_create_workflow(self):
        """Test workflow creation"""
        workflow = create_workflow(
            research_question="Does X affect Y?",
            domain="test",
            mode=Mode.ASSISTANT
        )

        assert workflow.context.research_question == "Does X affect Y?"
        assert workflow.context.mode == Mode.ASSISTANT
        assert workflow.current_state == workflow.problem_formulation

    def test_linear_progression(self):
        """Test linear progression through phases"""
        workflow = create_workflow(
            research_question="Test question",
            mode=Mode.AUTONOMOUS
        )

        # Start at problem formulation
        assert workflow.current_state == workflow.problem_formulation

        # Mark phase complete and progress
        validation = ValidationResult(passed=True, score=0.9)
        workflow.context.complete_phase(validation, outputs=["problem.md"])

        success = workflow.progress_to_next()
        assert success
        assert workflow.current_state == workflow.literature_review

        # Progress through next few phases
        for expected_state in [
            workflow.gap_analysis,
            workflow.hypothesis_formation,
            workflow.experimental_design
        ]:
            validation = ValidationResult(passed=True, score=0.9)
            workflow.context.complete_phase(validation, outputs=["output.md"])

            success = workflow.progress_to_next()
            assert success
            assert workflow.current_state == expected_state

    def test_skip_irb(self):
        """Test skipping IRB phase when no human subjects"""
        workflow = create_workflow(
            research_question="Computational study",
            mode=Mode.AUTONOMOUS
        )

        # Progress to experimental design
        for _ in range(4):
            validation = ValidationResult(passed=True, score=0.9)
            workflow.context.complete_phase(validation, outputs=["output.md"])
            workflow.progress_to_next()

        assert workflow.current_state == workflow.experimental_design

        # Skip IRB
        validation = ValidationResult(passed=True, score=0.9)
        workflow.context.complete_phase(validation, outputs=["design.md"])

        success = workflow.progress_to_next(skip_irb=True)
        assert success
        assert workflow.current_state == workflow.data_collection

    def test_backward_transition(self):
        """Test going back to previous phase"""
        workflow = create_workflow(
            research_question="Test",
            mode=Mode.ASSISTANT
        )

        # Progress to hypothesis formation
        for _ in range(3):
            validation = ValidationResult(passed=True, score=0.9)
            workflow.context.complete_phase(validation, outputs=["output.md"])
            workflow.progress_to_next()

        assert workflow.current_state == workflow.hypothesis_formation

        # Go back to literature review
        success = workflow.go_back_to(ResearchPhase.LITERATURE_REVIEW)
        assert success
        assert workflow.current_state == workflow.literature_review

    def test_progress_calculation(self):
        """Test progress percentage calculation"""
        workflow = create_workflow(
            research_question="Test",
            mode=Mode.AUTONOMOUS
        )

        # Initially 0%
        assert workflow.get_progress_percentage() == 0.0

        # Complete first phase
        validation = ValidationResult(passed=True, score=0.9)
        workflow.context.complete_phase(validation, outputs=["output.md"])

        # Should be ~9% (1/11)
        assert 9.0 <= workflow.get_progress_percentage() <= 9.2

    def test_state_persistence(self, tmp_path):
        """Test saving and loading workflow state"""
        workflow = create_workflow(
            research_question="Test persistence",
            mode=Mode.ASSISTANT
        )

        # Progress a few phases
        for _ in range(3):
            validation = ValidationResult(passed=True, score=0.9)
            workflow.context.complete_phase(validation, outputs=["output.md"])
            workflow.progress_to_next()

        # Save state
        save_path = tmp_path / "workflow_state.json"
        workflow.save_state(save_path)

        assert save_path.exists()

        # Load state
        loaded_workflow = ResearchWorkflow.load_state(save_path)

        assert loaded_workflow.context.research_question == workflow.context.research_question
        assert loaded_workflow.current_state.value == workflow.current_state.value
        assert len(loaded_workflow.context.phase_history) == len(workflow.context.phase_history)

    def test_workflow_summary(self):
        """Test workflow summary generation"""
        workflow = create_workflow(
            research_question="Test",
            mode=Mode.ASSISTANT
        )

        summary = workflow.summary()

        assert "workflow_id" in summary
        assert "mode" in summary
        assert "current_phase" in summary
        assert "progress" in summary
        assert summary["mode"] == "assistant"
        assert summary["total_phases"] == 11


class TestValidationResult:
    """Test ValidationResult"""

    def test_create_validation_result(self):
        """Test creating validation result"""
        result = ValidationResult(
            passed=True,
            score=0.85,
            missing_items=["item1"],
            warnings=["warning1"]
        )

        assert result.passed
        assert result.score == 0.85
        assert len(result.missing_items) == 1
        assert len(result.warnings) == 1

    def test_validation_result_serialization(self):
        """Test validation result to dict"""
        result = ValidationResult(
            passed=False,
            score=0.6,
            missing_items=["item1", "item2"],
            blocking_issues=["critical issue"]
        )

        data = result.to_dict()

        assert isinstance(data, dict)
        assert data["passed"] is False
        assert data["score"] == 0.6
        assert len(data["missing_items"]) == 2
        assert len(data["blocking_issues"]) == 1


class TestPhaseEnum:
    """Test ResearchPhase enum"""

    def test_all_phases_defined(self):
        """Test that all 11 phases are defined"""
        phases = list(ResearchPhase)
        assert len(phases) == 11

    def test_phase_values(self):
        """Test phase string values"""
        assert ResearchPhase.PROBLEM_FORMULATION.value == "problem_formulation"
        assert ResearchPhase.PUBLICATION.value == "publication"


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
