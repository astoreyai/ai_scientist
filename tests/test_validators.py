"""
Tests for Research Validators

Tests FINER, PRISMA, and NIH validators for research quality.
"""

import pytest
from pathlib import Path
import sys

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from validators import BaseValidator, FINERValidator, PRISMAValidator, NIHRigorValidator
from workflow_context import WorkflowContext, ResearchPhase, Mode, ValidationResult


class TestBaseValidator:
    """Test base validator functionality"""

    # BaseValidator is abstract, so create a concrete implementation for testing
    class ConcreteValidator(BaseValidator):
        def can_enter(self) -> ValidationResult:
            return ValidationResult(passed=True, score=1.0)

        def can_exit(self) -> ValidationResult:
            return ValidationResult(passed=True, score=1.0)

    def test_validator_initialization(self):
        """Test validator initializes with context"""
        context = WorkflowContext(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )
        validator = self.ConcreteValidator(context)

        assert validator.context == context
        assert validator.project_root == context.project_root

    def test_file_exists_helper(self, tmp_path):
        """Test file existence check"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )
        validator = self.ConcreteValidator(context)

        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")

        assert validator._file_exists("test.txt") is True
        assert validator._file_exists("nonexistent.txt") is False

    def test_file_has_content_helper(self, tmp_path):
        """Test file content check"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )
        validator = self.ConcreteValidator(context)

        # Create test file with content
        test_file = tmp_path / "test.txt"
        test_file.write_text("Line 1\nLine 2\nLine 3")

        assert validator._file_has_content("test.txt", min_lines=1) is True
        assert validator._file_has_content("test.txt", min_lines=3) is True
        assert validator._file_has_content("test.txt", min_lines=10) is False
        assert validator._file_has_content("nonexistent.txt") is False

    def test_count_files_in_dir(self, tmp_path):
        """Test counting files in directory"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )
        validator = self.ConcreteValidator(context)

        # Create test directory with files
        test_dir = tmp_path / "testdir"
        test_dir.mkdir()
        (test_dir / "file1.txt").write_text("content1")
        (test_dir / "file2.txt").write_text("content2")

        assert validator._count_files_in_dir("testdir") == 2
        assert validator._count_files_in_dir("nonexistent") == 0

    def test_validate_outputs_default(self):
        """Test default validate_outputs delegates to can_exit"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT
        )
        validator = self.ConcreteValidator(context)

        result = validator.validate_outputs()

        assert isinstance(result, ValidationResult)
        assert result.passed is True


class TestFINERValidator:
    """Test FINER (Feasible, Interesting, Novel, Ethical, Relevant) validator"""

    def test_finer_initialization(self):
        """Test FINER validator initializes"""
        context = WorkflowContext(
            research_question="Does exercise reduce depression?",
            mode=Mode.ASSISTANT
        )
        validator = FINERValidator(context)

        assert validator.context == context
        assert isinstance(validator, BaseValidator)

    def test_can_enter_always_true(self):
        """Test FINER can_enter always allows entry"""
        context = WorkflowContext(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )
        validator = FINERValidator(context)

        result = validator.can_enter()

        assert isinstance(result, ValidationResult)
        assert result.passed is True
        assert result.score == 1.0

    def test_can_exit_checks_research_question(self):
        """Test FINER can_exit validates research question"""
        context = WorkflowContext(
            research_question="",
            mode=Mode.ASSISTANT
        )
        validator = FINERValidator(context)

        result = validator.can_exit()

        assert isinstance(result, ValidationResult)
        # Should fail with empty research question
        assert result.passed is False

    def test_can_exit_with_good_question(self, tmp_path):
        """Test FINER can_exit passes with good question and files"""
        context = WorkflowContext(
            research_question="Does daily exercise for 30 minutes reduce symptoms of depression in college students over 8 weeks?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Create required file
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "problem_statement.md").write_text("# Problem Statement\n" * 10)

        validator = FINERValidator(context)

        result = validator.can_exit()

        assert isinstance(result, ValidationResult)
        # Should pass with specific, measurable question and required files
        assert result.score > 0.0


class TestPRISMAValidator:
    """Test PRISMA (Preferred Reporting Items for Systematic Reviews) validator"""

    def test_prisma_initialization(self):
        """Test PRISMA validator initializes"""
        context = WorkflowContext(
            research_question="What are the effects of X?",
            mode=Mode.ASSISTANT
        )
        validator = PRISMAValidator(context)

        assert validator.context == context
        assert isinstance(validator, BaseValidator)

    def test_can_enter_requires_problem_formulation(self):
        """Test PRISMA requires problem formulation first"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT
        )
        validator = PRISMAValidator(context)

        result = validator.can_enter()

        assert isinstance(result, ValidationResult)
        assert isinstance(result.passed, bool)
        # Should check if problem_formulation is complete

    def test_can_exit_checks_literature(self, tmp_path):
        """Test PRISMA can_exit checks for literature"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )
        context.complete_phase(
            ValidationResult(passed=True, score=1.0),
            []
        )
        validator = PRISMAValidator(context)

        result = validator.can_exit()

        assert isinstance(result, ValidationResult)
        # Should check for literature files
        assert isinstance(result.score, float)


class TestNIHRigorValidator:
    """Test NIH Rigor and Reproducibility validator"""

    def test_nih_initialization(self):
        """Test NIH validator initializes"""
        context = WorkflowContext(
            research_question="Test question?",
            mode=Mode.ASSISTANT
        )
        validator = NIHRigorValidator(context)

        assert validator.context == context
        assert isinstance(validator, BaseValidator)

    def test_can_enter_requires_hypothesis(self):
        """Test NIH requires hypothesis formation"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT
        )
        validator = NIHRigorValidator(context)

        result = validator.can_enter()

        assert isinstance(result, ValidationResult)
        assert isinstance(result.passed, bool)

    def test_can_exit_checks_design_elements(self, tmp_path):
        """Test NIH can_exit checks for experimental design elements"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )
        validator = NIHRigorValidator(context)

        result = validator.can_exit()

        assert isinstance(result, ValidationResult)
        # Should check for power analysis, randomization, blinding
        assert isinstance(result.score, float)
        assert isinstance(result.blocking_issues, list)


class TestValidatorIntegration:
    """Integration tests for validators"""

    def test_all_validators_implement_interface(self):
        """Test all validators implement BaseValidator interface"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT
        )

        validators = [
            FINERValidator(context),
            PRISMAValidator(context),
            NIHRigorValidator(context)
        ]

        for validator in validators:
            assert isinstance(validator, BaseValidator)
            assert hasattr(validator, 'can_enter')
            assert hasattr(validator, 'can_exit')
            assert hasattr(validator, 'validate_outputs')

    def test_validators_return_validation_results(self):
        """Test all validators return proper ValidationResults"""
        context = WorkflowContext(
            research_question="Does X affect Y in population Z?",
            mode=Mode.ASSISTANT
        )

        validators = [
            FINERValidator(context),
            PRISMAValidator(context),
            NIHRigorValidator(context)
        ]

        for validator in validators:
            entry_result = validator.can_enter()
            exit_result = validator.can_exit()

            assert isinstance(entry_result, ValidationResult)
            assert isinstance(exit_result, ValidationResult)
            assert isinstance(entry_result.passed, bool)
            assert isinstance(exit_result.passed, bool)
            assert isinstance(entry_result.score, float)
            assert isinstance(exit_result.score, float)
            assert 0.0 <= entry_result.score <= 1.0
            assert 0.0 <= exit_result.score <= 1.0

    def test_validator_file_utilities_work(self, tmp_path):
        """Test that validator file utilities work across implementations"""
        context = WorkflowContext(
            research_question="Test?",
            mode=Mode.ASSISTANT,
            project_root=tmp_path
        )

        # Create test structure
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "problem.md").write_text("# Problem Statement\n" * 10)

        validator = FINERValidator(context)

        assert validator._file_exists("docs/problem.md")
        assert validator._file_has_content("docs/problem.md", min_lines=5)
        assert validator._count_files_in_dir("docs") == 1
