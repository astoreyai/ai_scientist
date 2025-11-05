"""
NIH Rigor & Reproducibility Validator

Validates experimental design meets NIH rigor standards.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_context import WorkflowContext, ValidationResult, ResearchPhase
from validators.base import BaseValidator


class NIHRigorValidator(BaseValidator):
    """
    Validator for Experimental Design phase using NIH rigor standards.

    Four pillars:
    1. Scientific rigor (controls, randomization, blinding)
    2. Sex as biological variable (SABV)
    3. Reproducibility (pre-registration, seeds, code)
    4. Authentication (cell lines, reagents)
    """

    def __init__(self, context: WorkflowContext):
        super().__init__(context)
        self.required_files = [
            "docs/experimental_protocol.md",
            "docs/power_analysis.md",
            "code/randomization.py"
        ]

    def can_enter(self) -> ValidationResult:
        """
        Check if experimental design can be started.

        Requirements:
        - Hypotheses formulated
        """
        if not self.context.has_completed_phase(ResearchPhase.HYPOTHESIS_FORMATION):
            return ValidationResult(
                passed=False,
                score=0.0,
                blocking_issues=["Hypothesis formation must be complete first"]
            )

        return ValidationResult(passed=True, score=1.0)

    def can_exit(self) -> ValidationResult:
        """
        Check if experimental design meets NIH rigor standards.

        Requirements:
        - Protocol document complete
        - Power analysis ≥80%
        - Randomization protocol with seed
        - Pre-registration document
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

        # Check power analysis
        if self._file_exists("docs/power_analysis.md"):
            checks["power_analysis"] = self._check_power_analysis()
        else:
            checks["power_analysis"] = False

        # Check randomization has seed
        if self._file_exists("code/randomization.py"):
            checks["random_seed"] = self._check_random_seed()
        else:
            checks["random_seed"] = False

        # Check pre-registration
        prereg_file = "data/preregistration.md"
        if self._file_exists(prereg_file):
            checks["preregistration"] = True
        else:
            warnings.append("Pre-registration document recommended")
            checks["preregistration"] = False

        # Check SABV consideration
        if self._file_exists("docs/experimental_protocol.md"):
            checks["sabv"] = self._check_sabv()
        else:
            checks["sabv"] = False

        # Calculate score
        core_checks = ["power_analysis", "random_seed"]
        core_passed = all(checks.get(c, False) for c in core_checks)

        score = sum(1 for v in checks.values() if v) / len(checks)

        # Must pass core requirements
        passed = (
            core_passed and
            all(checks.get(f"file_{f}", False) for f in self.required_files)
        )

        if not passed:
            if not core_passed:
                blocking_issues.append(
                    "Core NIH requirements not met (power analysis, randomization)"
                )
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

    def _check_power_analysis(self) -> bool:
        """Check if power analysis mentions ≥80% power"""
        path = self.project_root / "docs/power_analysis.md"
        try:
            with open(path, 'r') as f:
                content = f.read().lower()
                # Look for power >= 0.8 or 80%
                return ('0.8' in content or '80%' in content) and 'power' in content
        except Exception:
            return False

    def _check_random_seed(self) -> bool:
        """Check if randomization code specifies a seed"""
        path = self.project_root / "code/randomization.py"
        try:
            with open(path, 'r') as f:
                content = f.read().lower()
                return 'seed' in content
        except Exception:
            return False

    def _check_sabv(self) -> bool:
        """Check if SABV (sex as biological variable) is mentioned"""
        path = self.project_root / "docs/experimental_protocol.md"
        try:
            with open(path, 'r') as f:
                content = f.read().lower()
                return 'sex' in content or 'sabv' in content
        except Exception:
            return False
