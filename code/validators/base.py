"""
Base Validator

Abstract base class for all phase validators.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_context import WorkflowContext, ValidationResult


class BaseValidator(ABC):
    """
    Base class for phase validators.

    Each validator checks if a phase can be entered and exited,
    and validates the quality of phase outputs.
    """

    def __init__(self, context: WorkflowContext):
        """
        Initialize validator with workflow context.

        Args:
            context: Workflow context containing project state
        """
        self.context = context
        self.project_root = context.project_root

    @abstractmethod
    def can_enter(self) -> ValidationResult:
        """
        Check if phase can be entered.

        Returns:
            ValidationResult with entry requirements check
        """
        pass

    @abstractmethod
    def can_exit(self) -> ValidationResult:
        """
        Check if phase can be exited (completion criteria).

        Returns:
            ValidationResult with exit criteria check
        """
        pass

    def validate_outputs(self) -> ValidationResult:
        """
        Validate quality of phase outputs.

        Default implementation delegates to can_exit().
        Override for custom output validation.

        Returns:
            ValidationResult with output quality check
        """
        return self.can_exit()

    def _file_exists(self, filepath: str) -> bool:
        """Check if a file exists relative to project root"""
        path = self.project_root / filepath
        return path.exists() and path.is_file()

    def _file_has_content(self, filepath: str, min_lines: int = 1) -> bool:
        """Check if file exists and has minimum content"""
        if not self._file_exists(filepath):
            return False

        path = self.project_root / filepath
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                return len(lines) >= min_lines
        except Exception:
            return False

    def _count_files_in_dir(self, dirpath: str) -> int:
        """Count files in a directory"""
        dir_path = self.project_root / dirpath
        if not dir_path.exists() or not dir_path.is_dir():
            return 0

        return len(list(dir_path.glob("*")))
