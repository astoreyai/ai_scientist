"""
PRISMA 2020 Validator

Validates literature review completeness using PRISMA 2020 checklist.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_context import WorkflowContext, ValidationResult, ResearchPhase
from validators.base import BaseValidator


class PRISMAValidator(BaseValidator):
    """
    Validator for Literature Review phase using PRISMA 2020.

    Checks that systematic review meets PRISMA standards.
    """

    def __init__(self, context: WorkflowContext):
        super().__init__(context)
        self.required_files = [
            "data/literature/search_results.csv",
            "data/literature/screened_abstracts.csv",
            "data/literature/included_studies.csv",
            "results/prisma_flow_diagram.md"
        ]

    def can_enter(self) -> ValidationResult:
        """
        Check if literature review can be started.

        Requirements:
        - Problem formulation complete
        """
        if not self.context.has_completed_phase(ResearchPhase.PROBLEM_FORMULATION):
            return ValidationResult(
                passed=False,
                score=0.0,
                blocking_issues=["Problem formulation must be complete first"]
            )

        return ValidationResult(passed=True, score=1.0)

    def can_exit(self) -> ValidationResult:
        """
        Check if literature review is complete per PRISMA 2020.

        Requirements:
        - All required files present
        - ≥10 included studies (or justification)
        - PRISMA flow diagram with counts
        """
        missing_items = []
        warnings = []
        blocking_issues = []
        checks = {}

        # Check required files
        for filepath in self.required_files:
            if not self._file_exists(filepath):
                missing_items.append(filepath)
                checks[f"file_{filepath}"] = False
            else:
                checks[f"file_{filepath}"] = True

        # Check for minimum included studies
        included_file = "data/literature/included_studies.csv"
        if self._file_exists(included_file):
            study_count = self._count_studies(included_file)
            checks["minimum_studies"] = study_count >= 10

            if study_count < 10:
                warnings.append(
                    f"Only {study_count} included studies (recommend ≥10)"
                )
        else:
            checks["minimum_studies"] = False

        # Check for risk of bias assessment
        rob_file = "results/risk_of_bias_assessment.csv"
        if self._file_exists(rob_file):
            checks["risk_of_bias"] = True
        else:
            warnings.append("Risk of bias assessment not found (recommended)")
            checks["risk_of_bias"] = False

        # Calculate score
        score = sum(1 for v in checks.values() if v) / len(checks)

        # Must have all required files to pass
        passed = all(checks[f"file_{f}"] for f in self.required_files)

        if missing_items:
            blocking_issues.append(
                f"{len(missing_items)} required files missing"
            )

        return ValidationResult(
            passed=passed,
            score=score,
            missing_items=missing_items,
            warnings=warnings,
            blocking_issues=blocking_issues,
            details={"checks": checks}
        )

    def _count_studies(self, filepath: str) -> int:
        """Count number of studies in CSV file (excluding header)"""
        path = self.project_root / filepath
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                # Subtract 1 for header
                return max(0, len(lines) - 1)
        except Exception:
            return 0
