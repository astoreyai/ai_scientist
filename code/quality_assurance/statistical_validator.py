"""
Statistical Validation System

Validates statistical analyses for rigor, completeness, and proper reporting.
"""

from pathlib import Path
from typing import List, Optional, Dict, Set
import re
import ast
import logging

from .base import BaseValidator, ValidationResult, ValidationStatus

logger = logging.getLogger(__name__)


class StatisticalValidator(BaseValidator):
    """
    Validates statistical analyses for rigor and completeness.

    Checks:
    - Power analysis presence and appropriateness
    - Effect size reporting
    - P-value interpretation
    - Multiple comparison corrections
    - Confidence interval reporting
    - Assumption checking
    """

    def __init__(self, project_root: Path, config: Optional[Dict] = None):
        """
        Initialize statistical validator.

        Args:
            project_root: Project root directory
            config: Configuration dict with keys:
                - require_power_analysis: Require power analysis
                - min_power: Minimum required power (default: 0.80)
                - require_effect_sizes: Require effect size reporting
                - require_confidence_intervals: Require CIs
                - check_multiple_comparisons: Check for corrections
                - require_assumption_checks: Require assumption testing
        """
        super().__init__(project_root, config)

        cfg = config or {}
        self.require_power_analysis = cfg.get("require_power_analysis", True)
        self.min_power = cfg.get("min_power", 0.80)
        self.require_effect_sizes = cfg.get("require_effect_sizes", True)
        self.require_cis = cfg.get("require_confidence_intervals", True)
        self.check_multiple_comparisons = cfg.get("check_multiple_comparisons", True)
        self.require_assumption_checks = cfg.get("require_assumption_checks", True)

    def validate(self) -> List[ValidationResult]:
        """
        Run all statistical validations.

        Returns:
            List of validation results
        """
        self.clear_results()

        # Find Python and notebook files
        py_files = self.find_files("**/*.py")
        nb_files = self.find_files("**/*.ipynb")

        # Collect all code
        code_contents = []
        for py_file in py_files:
            content = self.read_file(py_file, relative=False)
            if content:
                code_contents.append((str(py_file.relative_to(self.project_root)), content))

        # Read notebooks (simplified - just extract code cells)
        for nb_file in nb_files:
            code = self.extract_notebook_code(nb_file)
            if code:
                code_contents.append((str(nb_file.relative_to(self.project_root)), code))

        if not code_contents:
            self.skip_check(
                "Statistical Analysis",
                "No Python files or notebooks found",
                category="statistical"
            )
            return self.get_results()

        # Run validations
        if self.require_power_analysis:
            self.validate_power_analysis(code_contents)

        if self.require_effect_sizes:
            self.validate_effect_sizes(code_contents)

        self.validate_p_values(code_contents)

        if self.require_cis:
            self.validate_confidence_intervals(code_contents)

        if self.check_multiple_comparisons:
            self.validate_multiple_comparisons(code_contents)

        if self.require_assumption_checks:
            self.validate_assumptions(code_contents)

        return self.get_results()

    # ============================================================================
    # Helper Methods
    # ============================================================================

    def extract_notebook_code(self, nb_file: Path) -> Optional[str]:
        """Extract code from Jupyter notebook."""
        import json

        try:
            content = self.read_file(nb_file, relative=False)
            if not content:
                return None

            notebook = json.loads(content)
            cells = notebook.get("cells", [])

            code_cells = []
            for cell in cells:
                if cell.get("cell_type") == "code":
                    source = cell.get("source", [])
                    if isinstance(source, list):
                        code_cells.append("".join(source))
                    else:
                        code_cells.append(source)

            return "\n\n".join(code_cells)

        except Exception as e:
            logger.error(f"Error extracting code from {nb_file}: {e}")
            return None

    # ============================================================================
    # Power Analysis Validation
    # ============================================================================

    def validate_power_analysis(self, code_contents: List[tuple]):
        """Validate power analysis presence."""
        check_name = "Power Analysis"
        category = "statistical"

        # Patterns for power analysis
        power_patterns = [
            re.compile(r"power[_\s]*analysis", re.IGNORECASE),
            re.compile(r"statsmodels\.stats\.power", re.IGNORECASE),
            re.compile(r"from.*power.*import", re.IGNORECASE),
            re.compile(r"pwr\.", re.IGNORECASE),  # R pwr package
            re.compile(r"TTestPower|FTestAnovaPower|NormalIndPower", re.IGNORECASE),
            re.compile(r"sample[_\s]*size[_\s]*calculation", re.IGNORECASE),
        ]

        files_with_power = []
        for filename, content in code_contents:
            if any(pattern.search(content) for pattern in power_patterns):
                files_with_power.append(filename)

        # Also check documentation
        docs_files = self.find_files("docs/**/*.md")
        readme = self.read_file("README.md")

        doc_has_power = False
        if readme and any(pattern.search(readme) for pattern in power_patterns):
            doc_has_power = True

        for doc_file in docs_files:
            content = self.read_file(doc_file, relative=False)
            if content and any(pattern.search(content) for pattern in power_patterns):
                doc_has_power = True
                break

        if files_with_power or doc_has_power:
            self.pass_check(
                check_name,
                f"Power analysis found in {len(files_with_power)} file(s)" +
                (" and documentation" if doc_has_power else ""),
                category=category,
                details={"files": files_with_power}
            )
        else:
            self.warn_check(
                check_name,
                "No power analysis found in code or documentation",
                category=category,
                details={
                    "recommendation": "Conduct a priori power analysis for sample size justification",
                    "target_power": self.min_power
                }
            )

    # ============================================================================
    # Effect Size Validation
    # ============================================================================

    def validate_effect_sizes(self, code_contents: List[tuple]):
        """Validate effect size reporting."""
        check_name = "Effect Size Reporting"
        category = "statistical"

        # Patterns for effect size calculations
        effect_size_patterns = [
            re.compile(r"cohen[_\s]*d", re.IGNORECASE),
            re.compile(r"effect[_\s]*size", re.IGNORECASE),
            re.compile(r"eta[_\s]*squared", re.IGNORECASE),
            re.compile(r"omega[_\s]*squared", re.IGNORECASE),
            re.compile(r"partial[_\s]*eta", re.IGNORECASE),
            re.compile(r"hedges[_\s]*g", re.IGNORECASE),
            re.compile(r"glass[_\s]*delta", re.IGNORECASE),
            re.compile(r"cramer[_\s]*v", re.IGNORECASE),
            re.compile(r"odds[_\s]*ratio", re.IGNORECASE),
            re.compile(r"risk[_\s]*ratio", re.IGNORECASE),
            re.compile(r"correlation[_\s]*coefficient", re.IGNORECASE),
        ]

        files_with_effect_sizes = []
        for filename, content in code_contents:
            if any(pattern.search(content) for pattern in effect_size_patterns):
                files_with_effect_sizes.append(filename)

        if files_with_effect_sizes:
            self.pass_check(
                check_name,
                f"Effect size calculations found in {len(files_with_effect_sizes)} file(s)",
                category=category,
                details={"files": files_with_effect_sizes}
            )
        else:
            self.warn_check(
                check_name,
                "No effect size calculations found in code",
                category=category,
                details={
                    "recommendation": "Report effect sizes (Cohen's d, η², odds ratio, etc.) for all analyses"
                }
            )

    # ============================================================================
    # P-Value Validation
    # ============================================================================

    def validate_p_values(self, code_contents: List[tuple]):
        """Validate p-value usage and reporting."""
        check_name = "P-Value Usage"
        category = "statistical"

        # Check for p-value calculations
        pvalue_patterns = [
            re.compile(r"p[_\s]*value", re.IGNORECASE),
            re.compile(r"pval", re.IGNORECASE),
            re.compile(r"\.pvalue", re.IGNORECASE),
            re.compile(r"ttest|chi2|anova|mannwhitneyu|wilcoxon|kruskal", re.IGNORECASE),
        ]

        # Problematic interpretation patterns
        problematic_patterns = [
            re.compile(r"marginally\s+significant", re.IGNORECASE),
            re.compile(r"trending\s+toward", re.IGNORECASE),
            re.compile(r"approached\s+significance", re.IGNORECASE),
            re.compile(r"almost\s+significant", re.IGNORECASE),
        ]

        files_with_pvalues = []
        files_with_problems = []

        for filename, content in code_contents:
            # Skip validator files themselves (they contain detection patterns as strings)
            is_validator = "quality_assurance" in filename and filename.endswith("_validator.py")

            has_pvalue = any(pattern.search(content) for pattern in pvalue_patterns)
            has_problem = any(pattern.search(content) for pattern in problematic_patterns)

            if has_pvalue:
                files_with_pvalues.append(filename)

            if has_problem and not is_validator:
                files_with_problems.append(filename)

        if files_with_problems:
            self.warn_check(
                check_name,
                f"Problematic p-value interpretation found in {len(files_with_problems)} file(s)",
                category=category,
                details={
                    "files": files_with_problems,
                    "issue": "Avoid 'marginally significant', 'trending', or similar language",
                    "recommendation": "Report exact p-values and interpret binary (significant/not significant)"
                }
            )
        elif files_with_pvalues:
            self.pass_check(
                check_name,
                f"P-value calculations found in {len(files_with_pvalues)} file(s), no problematic interpretations detected",
                category=category,
                details={"files": files_with_pvalues}
            )
        else:
            self.skip_check(
                check_name,
                "No statistical tests found in code",
                category=category
            )

    # ============================================================================
    # Confidence Interval Validation
    # ============================================================================

    def validate_confidence_intervals(self, code_contents: List[tuple]):
        """Validate confidence interval reporting."""
        check_name = "Confidence Intervals"
        category = "statistical"

        ci_patterns = [
            re.compile(r"confidence[_\s]*interval", re.IGNORECASE),
            re.compile(r"\bci\b", re.IGNORECASE),
            re.compile(r"confint", re.IGNORECASE),
            re.compile(r"conf_int", re.IGNORECASE),
            re.compile(r"\.conf_int\(", re.IGNORECASE),
        ]

        files_with_cis = []
        for filename, content in code_contents:
            if any(pattern.search(content) for pattern in ci_patterns):
                files_with_cis.append(filename)

        if files_with_cis:
            self.pass_check(
                check_name,
                f"Confidence interval calculations found in {len(files_with_cis)} file(s)",
                category=category,
                details={"files": files_with_cis}
            )
        else:
            self.warn_check(
                check_name,
                "No confidence interval calculations found in code",
                category=category,
                details={
                    "recommendation": "Report 95% confidence intervals for all estimates"
                }
            )

    # ============================================================================
    # Multiple Comparisons Validation
    # ============================================================================

    def validate_multiple_comparisons(self, code_contents: List[tuple]):
        """Validate corrections for multiple comparisons."""
        check_name = "Multiple Comparison Corrections"
        category = "statistical"

        # Detect multiple comparisons
        multiple_test_indicators = [
            re.compile(r"for\s+\w+\s+in.*:\s*ttest", re.IGNORECASE),
            re.compile(r"for\s+\w+\s+in.*:\s*chi2", re.IGNORECASE),
            re.compile(r"for\s+\w+\s+in.*:\s*mannwhitneyu", re.IGNORECASE),
            re.compile(r"multiple.*test", re.IGNORECASE),
            re.compile(r"pairwise.*comparison", re.IGNORECASE),
        ]

        # Correction methods
        correction_patterns = [
            re.compile(r"bonferroni", re.IGNORECASE),
            re.compile(r"holm", re.IGNORECASE),
            re.compile(r"benjamini", re.IGNORECASE),
            re.compile(r"hochberg", re.IGNORECASE),
            re.compile(r"fdr", re.IGNORECASE),
            re.compile(r"multipletests", re.IGNORECASE),
            re.compile(r"p\.adjust", re.IGNORECASE),
        ]

        files_with_multiple = []
        files_with_correction = []

        for filename, content in code_contents:
            has_multiple = any(pattern.search(content) for pattern in multiple_test_indicators)
            has_correction = any(pattern.search(content) for pattern in correction_patterns)

            if has_multiple:
                files_with_multiple.append(filename)
            if has_correction:
                files_with_correction.append(filename)

        if not files_with_multiple:
            self.skip_check(
                check_name,
                "No multiple comparisons detected",
                category=category
            )
        elif files_with_correction:
            self.pass_check(
                check_name,
                f"Multiple comparison corrections found in {len(files_with_correction)} file(s)",
                category=category,
                details={
                    "multiple_tests_in": files_with_multiple,
                    "corrections_in": files_with_correction
                }
            )
        else:
            self.warn_check(
                check_name,
                f"Multiple comparisons detected in {len(files_with_multiple)} file(s) but no corrections found",
                category=category,
                details={
                    "files": files_with_multiple,
                    "recommendation": "Apply Bonferroni, Holm, or FDR correction for multiple comparisons"
                }
            )

    # ============================================================================
    # Assumption Checking Validation
    # ============================================================================

    def validate_assumptions(self, code_contents: List[tuple]):
        """Validate statistical assumption checking."""
        check_name = "Statistical Assumptions"
        category = "statistical"

        # Assumption test patterns
        assumption_patterns = [
            # Normality tests
            re.compile(r"shapiro|normaltest|kstest|anderson", re.IGNORECASE),
            re.compile(r"qqplot|probplot", re.IGNORECASE),

            # Homogeneity of variance
            re.compile(r"levene|bartlett|fligner", re.IGNORECASE),

            # Sphericity
            re.compile(r"mauchly", re.IGNORECASE),

            # Independence
            re.compile(r"durbin.watson", re.IGNORECASE),

            # General diagnostics
            re.compile(r"diagnostic|residual.*plot", re.IGNORECASE),
        ]

        # Parametric tests that require assumptions
        parametric_tests = [
            re.compile(r"ttest_ind|ttest_rel", re.IGNORECASE),
            re.compile(r"anova|f_oneway", re.IGNORECASE),
            re.compile(r"pearsonr", re.IGNORECASE),
            re.compile(r"linregress|OLS|regression", re.IGNORECASE),
        ]

        files_with_parametric = []
        files_with_assumptions = []

        for filename, content in code_contents:
            has_parametric = any(pattern.search(content) for pattern in parametric_tests)
            has_assumptions = any(pattern.search(content) for pattern in assumption_patterns)

            if has_parametric:
                files_with_parametric.append(filename)
            if has_assumptions:
                files_with_assumptions.append(filename)

        if not files_with_parametric:
            self.skip_check(
                check_name,
                "No parametric tests detected",
                category=category
            )
        elif files_with_assumptions:
            self.pass_check(
                check_name,
                f"Assumption checks found in {len(files_with_assumptions)} file(s)",
                category=category,
                details={
                    "parametric_tests_in": files_with_parametric,
                    "assumption_checks_in": files_with_assumptions
                }
            )
        else:
            self.warn_check(
                check_name,
                f"Parametric tests found in {len(files_with_parametric)} file(s) but no assumption checks detected",
                category=category,
                details={
                    "files": files_with_parametric,
                    "recommendation": "Check normality, homogeneity of variance, and other assumptions"
                }
            )
