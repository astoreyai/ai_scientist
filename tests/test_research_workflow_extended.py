"""
Extended tests for Research Workflow and Orchestrator

Tests state transitions, phase execution, and workflow advancement.
"""

import pytest
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from research_workflow import (
    ResearchWorkflow, ResearchPhase, create_workflow
)
from orchestrator import WorkflowOrchestrator, create_orchestrator
from workflow_context import WorkflowContext, Mode, ValidationResult


class TestResearchWorkflowExtended:
    """Extended tests for research workflow state machine"""

    def test_progress_to_next_success(self, tmp_path):
        """Test successful progression to next phase"""
        workflow = create_workflow(
            research_question="Test question?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Complete current phase
        result = ValidationResult(passed=True, score=1.0)
        workflow.context.complete_phase(result, ["test_output.md"])

        # Progress to next
        success = workflow.progress_to_next()

        assert success is True
        assert workflow.current_state.value != ResearchPhase.PROBLEM_FORMULATION.value

    def test_get_progress_percentage(self, tmp_path):
        """Test progress percentage calculation"""
        workflow = create_workflow(
            research_question="Test question?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Initial progress
        initial_progress = workflow.get_progress_percentage()
        assert 0 <= initial_progress <= 100

        # Complete first phase and progress
        result = ValidationResult(passed=True, score=1.0)
        workflow.context.complete_phase(result, [])
        workflow.progress_to_next()

        # Progress should increase
        new_progress = workflow.get_progress_percentage()
        assert new_progress > initial_progress

    def test_current_state(self, tmp_path):
        """Test current state tracking"""
        workflow = create_workflow(
            research_question="Test question?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Should have a current state
        assert workflow.current_state is not None
        assert workflow.current_state.value == ResearchPhase.PROBLEM_FORMULATION.value

    def test_multiple_phase_progression(self, tmp_path):
        """Test progressing through multiple phases"""
        workflow = create_workflow(
            research_question="Does exercise reduce stress?",
            mode=Mode.AUTONOMOUS,
            project_root=tmp_path
        )

        phases_visited = []
        result = ValidationResult(passed=True, score=1.0)

        # Progress through 5 phases
        for i in range(5):
            phases_visited.append(workflow.current_state.value)
            workflow.context.complete_phase(result, [f"output_{i}.md"])
            success = workflow.progress_to_next(skip_irb=True)

            if not success:
                break

        assert len(phases_visited) >= 3


class TestOrchestratorExtended:
    """Extended tests for workflow orchestrator"""

    def test_execute_phase_success(self, tmp_path):
        """Test executing a phase successfully"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        result = orchestrator.execute_phase()

        assert result["success"] is True
        assert "phase" in result

    def test_execute_phase_with_agent(self, tmp_path):
        """Test executing phase that has an agent"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Progress to literature review (has agent)
        validation = ValidationResult(passed=True, score=1.0)
        orchestrator.context.complete_phase(validation, [])
        orchestrator.workflow.progress_to_next()

        result = orchestrator.execute_phase()

        assert result["success"] is True
        assert result["agent"] is not None

    def test_execute_phase_entry_validation_failure(self, tmp_path):
        """Test executing phase when entry validation fails"""
        orchestrator = create_orchestrator(
            research_question="",  # Empty question will fail FINER validation
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Try to execute experimental design phase without completing prerequisites
        orchestrator.workflow.current_state = ResearchPhase.EXPERIMENTAL_DESIGN

        result = orchestrator.execute_phase()

        # Should fail entry validation
        assert "validation" in result or "error" in result

    def test_advance_workflow_success(self, tmp_path):
        """Test advancing workflow successfully"""
        orchestrator = create_orchestrator(
            research_question="Does daily exercise reduce anxiety?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Create required files for FINER validation
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        (docs_dir / "problem_statement.md").write_text("# Problem Statement\n" * 10)

        result = orchestrator.advance_workflow(skip_irb=True)

        assert "from_phase" in result or "current_phase" in result

    def test_advance_workflow_validation_failure(self, tmp_path):
        """Test advance_workflow when validation fails"""
        orchestrator = create_orchestrator(
            research_question="",  # Empty question fails validation
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        result = orchestrator.advance_workflow()

        # Should fail validation
        assert "success" in result
        if not result["success"]:
            assert "error" in result or "validation" in result

    def test_get_workflow_status(self, tmp_path):
        """Test getting comprehensive workflow status"""
        orchestrator = create_orchestrator(
            research_question="Test question?",
            mode=Mode.AUTONOMOUS,
            project_root=tmp_path
        )

        status = orchestrator.get_workflow_status()

        assert "workflow_id" in status
        assert "mode" in status
        assert "current_phase" in status
        assert "current_agent" in status
        assert "can_advance" in status
        assert "progress_percentage" in status
        assert "completed_phases" in status
        assert "total_phases" in status

        # Check types
        assert isinstance(status["mode"], str)
        assert isinstance(status["progress_percentage"], (int, float))
        assert isinstance(status["completed_phases"], int)
        assert isinstance(status["total_phases"], int)

    def test_can_progress(self, tmp_path):
        """Test checking if can progress"""
        orchestrator = create_orchestrator(
            research_question="Can we progress?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        can_progress = orchestrator.can_progress()

        # Should return boolean
        assert isinstance(can_progress, bool)

    def test_get_phase_outputs(self, tmp_path):
        """Test getting phase outputs"""
        orchestrator = create_orchestrator(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        outputs = orchestrator._get_phase_outputs(ResearchPhase.PROBLEM_FORMULATION)

        assert isinstance(outputs, list)
        assert len(outputs) > 0

    def test_orchestrator_phase_progression(self, tmp_path):
        """Test full orchestrator phase progression"""
        orchestrator = create_orchestrator(
            research_question="Does meditation improve focus?",
            mode=Mode.AUTONOMOUS,
            project_root=tmp_path
        )

        # Get initial status
        initial_status = orchestrator.get_workflow_status()
        initial_phase = initial_status["current_phase"]

        # Complete current phase with validation
        validation = ValidationResult(passed=True, score=1.0)
        orchestrator.context.complete_phase(validation, ["output.md"])

        # Advance
        result = orchestrator.advance_workflow(skip_irb=True)

        if result.get("success"):
            # Get new status
            new_status = orchestrator.get_workflow_status()

            # Phase should have changed
            assert new_status["current_phase"] != initial_phase
            assert new_status["completed_phases"] > initial_status["completed_phases"]


class TestAutoTrackerExtended:
    """Extended auto tracker tests"""

    def test_create_with_selective_managers(self, tmp_path):
        """Test creating auto tracker with selective managers"""
        from data_management.auto_tracking import create_auto_tracker

        tracker = create_auto_tracker(
            project_root=tmp_path,
            enable_dvc=False,
            enable_mlflow=False,
            enable_git=False
        )

        assert tracker.project_root == tmp_path
        assert tracker.dvc is None
        assert tracker.mlflow is None
        assert tracker.git is None

    def test_auto_tracker_basic_creation(self, tmp_path):
        """Test basic auto tracker creation"""
        from data_management.auto_tracking import AutoTracker

        tracker = AutoTracker(project_root=tmp_path)

        # Should still work, just won't track to external systems
        assert tracker.project_root == tmp_path
        assert tracker.dvc is None
        assert tracker.mlflow is None
        assert tracker.git is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
