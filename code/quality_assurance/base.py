"""
Base Validation Framework

Core classes and utilities for quality assurance validation.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any
from pathlib import Path
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class ValidationStatus(Enum):
    """Validation check status."""
    PASS = "pass"
    WARNING = "warning"
    ERROR = "error"
    SKIPPED = "skipped"


@dataclass
class ValidationResult:
    """
    Result from a single validation check.

    Attributes:
        check_name: Name of the validation check
        status: Status (pass, warning, error, skipped)
        message: Human-readable message
        details: Additional details (dict)
        timestamp: When check was performed
        category: Validation category (reproducibility, citation, statistical)
    """
    check_name: str
    status: ValidationStatus
    message: str
    details: Optional[Dict[str, Any]] = None
    timestamp: datetime = field(default_factory=datetime.now)
    category: str = "general"

    def is_passing(self) -> bool:
        """Check if validation passed."""
        return self.status == ValidationStatus.PASS

    def is_error(self) -> bool:
        """Check if validation errored."""
        return self.status == ValidationStatus.ERROR

    def is_warning(self) -> bool:
        """Check if validation warned."""
        return self.status == ValidationStatus.WARNING

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "check_name": self.check_name,
            "status": self.status.value,
            "message": self.message,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
            "category": self.category
        }


@dataclass
class QAReport:
    """
    Comprehensive QA report aggregating all validation results.

    Attributes:
        timestamp: When report was generated
        project: Project name/path
        phase: Research phase (optional)
        results: All validation results
    """
    timestamp: datetime
    project: str
    phase: Optional[str] = None
    results: List[ValidationResult] = field(default_factory=list)

    @property
    def total_checks(self) -> int:
        """Total number of checks performed."""
        return len(self.results)

    @property
    def passed(self) -> int:
        """Number of checks that passed."""
        return sum(1 for r in self.results if r.is_passing())

    @property
    def warnings(self) -> int:
        """Number of warnings."""
        return sum(1 for r in self.results if r.is_warning())

    @property
    def errors(self) -> int:
        """Number of errors."""
        return sum(1 for r in self.results if r.is_error())

    @property
    def skipped(self) -> int:
        """Number of skipped checks."""
        return sum(1 for r in self.results if r.status == ValidationStatus.SKIPPED)

    @property
    def status(self) -> ValidationStatus:
        """Overall report status."""
        if self.errors > 0:
            return ValidationStatus.ERROR
        if self.warnings > 0:
            return ValidationStatus.WARNING
        return ValidationStatus.PASS

    def get_by_category(self, category: str) -> List[ValidationResult]:
        """Get results filtered by category."""
        return [r for r in self.results if r.category == category]

    def to_markdown(self) -> str:
        """Export report as markdown."""
        lines = [
            f"# QA Report: {self.project}",
            f"",
            f"**Generated:** {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if self.phase:
            lines.append(f"**Phase:** {self.phase}")

        lines.extend([
            f"**Status:** {self.status.value.upper()}",
            f"",
            f"## Summary",
            f"",
            f"- Total Checks: {self.total_checks}",
            f"- Passed: {self.passed} ✅",
            f"- Warnings: {self.warnings} ⚠️",
            f"- Errors: {self.errors} ❌",
            f"- Skipped: {self.skipped}",
            f"",
        ])

        # Group by category
        categories = set(r.category for r in self.results)

        for category in sorted(categories):
            results = self.get_by_category(category)

            lines.extend([
                f"## {category.title()} ({len(results)} checks)",
                f"",
            ])

            for result in results:
                status_emoji = {
                    ValidationStatus.PASS: "✅",
                    ValidationStatus.WARNING: "⚠️",
                    ValidationStatus.ERROR: "❌",
                    ValidationStatus.SKIPPED: "⏭️",
                }[result.status]

                lines.append(f"### {status_emoji} {result.check_name}")
                lines.append(f"")
                lines.append(f"**Status:** {result.status.value}")
                lines.append(f"**Message:** {result.message}")

                if result.details:
                    lines.append(f"")
                    lines.append(f"**Details:**")
                    for key, value in result.details.items():
                        lines.append(f"- {key}: {value}")

                lines.append(f"")

        return "\n".join(lines)

    def to_dict(self) -> Dict[str, Any]:
        """Export report as dictionary."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "project": self.project,
            "phase": self.phase,
            "summary": {
                "total_checks": self.total_checks,
                "passed": self.passed,
                "warnings": self.warnings,
                "errors": self.errors,
                "skipped": self.skipped,
                "status": self.status.value,
            },
            "results": [r.to_dict() for r in self.results],
        }

    def save_markdown(self, output_path: Path):
        """Save report as markdown file."""
        output_path.write_text(self.to_markdown())
        logger.info(f"QA report saved to {output_path}")

    def save_json(self, output_path: Path):
        """Save report as JSON file."""
        import json
        output_path.write_text(json.dumps(self.to_dict(), indent=2))
        logger.info(f"QA report saved to {output_path}")


class BaseValidator:
    """
    Base class for all validators.

    Provides common validation patterns and utilities.
    """

    def __init__(self, project_root: Path, config: Optional[Dict] = None):
        """
        Initialize validator.

        Args:
            project_root: Project root directory
            config: Configuration dictionary
        """
        self.project_root = Path(project_root)
        self.config = config or {}
        self.results: List[ValidationResult] = []

    def add_result(
        self,
        check_name: str,
        status: ValidationStatus,
        message: str,
        details: Optional[Dict] = None,
        category: str = "general"
    ):
        """
        Add validation result.

        Args:
            check_name: Name of check
            status: ValidationStatus
            message: Message
            details: Additional details
            category: Validation category
        """
        result = ValidationResult(
            check_name=check_name,
            status=status,
            message=message,
            details=details,
            category=category
        )
        self.results.append(result)
        logger.info(f"{check_name}: {status.value} - {message}")

    def pass_check(self, check_name: str, message: str, **kwargs):
        """Add passing check result."""
        self.add_result(check_name, ValidationStatus.PASS, message, **kwargs)

    def warn_check(self, check_name: str, message: str, **kwargs):
        """Add warning check result."""
        self.add_result(check_name, ValidationStatus.WARNING, message, **kwargs)

    def error_check(self, check_name: str, message: str, **kwargs):
        """Add error check result."""
        self.add_result(check_name, ValidationStatus.ERROR, message, **kwargs)

    def skip_check(self, check_name: str, message: str, **kwargs):
        """Add skipped check result."""
        self.add_result(check_name, ValidationStatus.SKIPPED, message, **kwargs)

    def clear_results(self):
        """Clear all validation results."""
        self.results = []

    def get_results(self) -> List[ValidationResult]:
        """Get all validation results."""
        return self.results

    def validate(self) -> List[ValidationResult]:
        """
        Run all validations.

        Must be implemented by subclasses.

        Returns:
            List of validation results
        """
        raise NotImplementedError("Subclasses must implement validate()")

    def file_exists(self, filepath: Path, relative: bool = True) -> bool:
        """
        Check if file exists.

        Args:
            filepath: File path
            relative: If True, resolve relative to project_root

        Returns:
            True if file exists
        """
        if relative:
            filepath = self.project_root / filepath
        return filepath.exists()

    def read_file(self, filepath: Path, relative: bool = True) -> Optional[str]:
        """
        Read file contents.

        Args:
            filepath: File path
            relative: If True, resolve relative to project_root

        Returns:
            File contents or None if file doesn't exist
        """
        if relative:
            filepath = self.project_root / filepath

        if not filepath.exists():
            return None

        try:
            return filepath.read_text()
        except Exception as e:
            logger.error(f"Error reading {filepath}: {e}")
            return None

    def find_files(self, pattern: str) -> List[Path]:
        """
        Find files matching glob pattern.

        Args:
            pattern: Glob pattern (e.g., "**/*.py")

        Returns:
            List of matching file paths
        """
        return list(self.project_root.glob(pattern))


class QAException(Exception):
    """Base exception for QA system."""
    pass


class CriticalQAError(QAException):
    """Critical QA error that blocks progress."""
    pass


class QAWarning(QAException):
    """Non-blocking QA warning."""
    pass


class ValidationTimeoutError(QAException):
    """Validation took too long."""
    pass
