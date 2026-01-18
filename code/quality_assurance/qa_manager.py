"""
QA Manager

Orchestrates all quality assurance components and generates comprehensive reports.
"""

from pathlib import Path
from typing import List, Optional, Dict
from datetime import datetime
import yaml
import logging

from .base import QAReport, ValidationResult, ValidationStatus, CriticalQAError
from .reproducibility_validator import ReproducibilityValidator
from .citation_verifier import CitationVerifier
from .statistical_validator import StatisticalValidator

logger = logging.getLogger(__name__)


class QAManager:
    """
    Central manager for all quality assurance components.

    Orchestrates validation across:
    - Reproducibility
    - Citations
    - Statistics
    """

    def __init__(self, project_root: Path, config_file: Optional[Path] = None):
        """
        Initialize QA manager.

        Args:
            project_root: Project root directory
            config_file: Path to .qa_config.yaml (optional)
        """
        self.project_root = Path(project_root)
        self.config = self._load_config(config_file)

        # Initialize validators
        self.reproducibility = ReproducibilityValidator(
            project_root,
            self.config.get("reproducibility", {})
        )

        self.citations = CitationVerifier(
            project_root,
            self.config.get("citations", {})
        )

        self.statistics = StatisticalValidator(
            project_root,
            self.config.get("statistics", {})
        )

    def _load_config(self, config_file: Optional[Path]) -> Dict:
        """Load configuration from YAML file or use defaults."""
        if config_file and config_file.exists():
            try:
                with open(config_file) as f:
                    config = yaml.safe_load(f)
                logger.info(f"Loaded QA config from {config_file}")
                return config
            except Exception as e:
                logger.error(f"Error loading config: {e}, using defaults")

        # Default configuration
        return {
            "reproducibility": {
                "require_pinned_deps": True,
                "require_seed_docs": True,
                "require_docker": False,
                "check_data_provenance": True,
            },
            "citations": {
                "check_retractions": True,
                "validate_dois": True,
                "min_citation_count": 20,
                "require_recent_papers": True,
                "recent_paper_threshold_years": 5,
            },
            "statistics": {
                "require_power_analysis": True,
                "min_power": 0.80,
                "require_effect_sizes": True,
                "require_confidence_intervals": True,
                "check_multiple_comparisons": True,
                "require_assumption_checks": True,
            },
            "qa_manager": {
                "block_on_critical": True,
                "report_format": "markdown",
                "report_dir": "qa_reports",
            }
        }

    def run_full_qa(self, phase: Optional[str] = None) -> QAReport:
        """
        Run all QA checks.

        Args:
            phase: Research phase (optional)

        Returns:
            Comprehensive QA report
        """
        logger.info(f"Running full QA suite{f' for phase: {phase}' if phase else ''}")

        all_results = []

        # Run reproducibility checks
        logger.info("Running reproducibility validation...")
        try:
            repro_results = self.reproducibility.validate()
            all_results.extend(repro_results)
            logger.info(f"Reproducibility: {len(repro_results)} checks completed")
        except Exception as e:
            logger.error(f"Reproducibility validation error: {e}")
            all_results.append(
                ValidationResult(
                    check_name="Reproducibility Validator",
                    status=ValidationStatus.ERROR,
                    message=f"Validator crashed: {str(e)}",
                    category="reproducibility"
                )
            )

        # Run citation checks
        logger.info("Running citation verification...")
        try:
            citation_results = self.citations.validate()
            all_results.extend(citation_results)
            logger.info(f"Citations: {len(citation_results)} checks completed")
        except Exception as e:
            logger.error(f"Citation verification error: {e}")
            all_results.append(
                ValidationResult(
                    check_name="Citation Verifier",
                    status=ValidationStatus.ERROR,
                    message=f"Verifier crashed: {str(e)}",
                    category="citation"
                )
            )

        # Run statistical checks
        logger.info("Running statistical validation...")
        try:
            stat_results = self.statistics.validate()
            all_results.extend(stat_results)
            logger.info(f"Statistics: {len(stat_results)} checks completed")
        except Exception as e:
            logger.error(f"Statistical validation error: {e}")
            all_results.append(
                ValidationResult(
                    check_name="Statistical Validator",
                    status=ValidationStatus.ERROR,
                    message=f"Validator crashed: {str(e)}",
                    category="statistical"
                )
            )

        # Create report
        report = QAReport(
            timestamp=datetime.now(),
            project=str(self.project_root.name),
            phase=phase,
            results=all_results
        )

        logger.info(f"QA complete: {report.total_checks} checks, {report.passed} passed, "
                   f"{report.warnings} warnings, {report.errors} errors")

        return report

    def run_phase_qa(self, phase: str) -> QAReport:
        """
        Run phase-specific QA checks.

        Args:
            phase: Research phase name

        Returns:
            QA report for phase
        """
        # Phase-specific QA requirements
        phase_requirements = {
            "problem_formulation": ["statistics"],  # Power analysis
            "literature_review": ["citations"],  # Citation completeness
            "gap_analysis": [],
            "hypothesis_formation": [],
            "experimental_design": ["statistics", "reproducibility"],  # Power, seeds
            "data_collection": ["reproducibility"],  # Seeds, provenance
            "analysis": ["statistics", "reproducibility"],  # All statistical checks
            "interpretation": ["statistics"],
            "writing": ["citations", "statistics", "reproducibility"],  # Everything
            "publication": ["citations", "statistics", "reproducibility"],  # Full QA
        }

        required = phase_requirements.get(phase.lower(), [])

        if not required:
            logger.info(f"No specific QA requirements for phase: {phase}")
            return QAReport(
                timestamp=datetime.now(),
                project=str(self.project_root.name),
                phase=phase,
                results=[]
            )

        logger.info(f"Running QA for phase '{phase}': {', '.join(required)}")

        all_results = []

        # Run only required validators
        if "reproducibility" in required:
            try:
                results = self.reproducibility.validate()
                all_results.extend(results)
            except Exception as e:
                logger.error(f"Reproducibility validation error: {e}")

        if "citations" in required:
            try:
                results = self.citations.validate()
                all_results.extend(results)
            except Exception as e:
                logger.error(f"Citation verification error: {e}")

        if "statistics" in required:
            try:
                results = self.statistics.validate()
                all_results.extend(results)
            except Exception as e:
                logger.error(f"Statistical validation error: {e}")

        report = QAReport(
            timestamp=datetime.now(),
            project=str(self.project_root.name),
            phase=phase,
            results=all_results
        )

        return report

    def generate_and_save_report(
        self,
        report: QAReport,
        output_dir: Optional[Path] = None
    ) -> Path:
        """
        Generate and save QA report.

        Args:
            report: QA report to save
            output_dir: Output directory (defaults to config)

        Returns:
            Path to saved report
        """
        if output_dir is None:
            report_dir_name = self.config.get("qa_manager", {}).get("report_dir", "qa_reports")
            output_dir = self.project_root / report_dir_name

        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate filename
        timestamp = report.timestamp.strftime("%Y%m%d_%H%M%S")
        phase_suffix = f"_{report.phase}" if report.phase else ""
        filename = f"qa_report{phase_suffix}_{timestamp}.md"

        output_path = output_dir / filename

        # Save report
        report_format = self.config.get("qa_manager", {}).get("report_format", "markdown")

        if report_format == "json":
            output_path = output_path.with_suffix(".json")
            report.save_json(output_path)
        else:
            report.save_markdown(output_path)

        logger.info(f"QA report saved to: {output_path}")

        return output_path

    def check_critical_errors(self, report: QAReport) -> bool:
        """
        Check if report contains critical errors.

        Args:
            report: QA report

        Returns:
            True if critical errors present
        """
        block_on_critical = self.config.get("qa_manager", {}).get("block_on_critical", True)

        if not block_on_critical:
            return False

        # Critical error categories
        critical_checks = [
            "Retraction Check",  # Retracted papers are critical
            "DOI Validation",  # Invalid DOIs are important but not always critical
        ]

        for result in report.results:
            if result.is_error() and result.check_name in critical_checks:
                logger.error(f"Critical QA error: {result.check_name} - {result.message}")
                return True

        return False

    def validate_and_block(self, phase: Optional[str] = None) -> QAReport:
        """
        Run QA and raise exception if critical errors found.

        Args:
            phase: Research phase (optional)

        Returns:
            QA report

        Raises:
            CriticalQAError: If critical errors found and blocking enabled
        """
        if phase:
            report = self.run_phase_qa(phase)
        else:
            report = self.run_full_qa()

        # Save report
        self.generate_and_save_report(report)

        # Check for critical errors
        if self.check_critical_errors(report):
            raise CriticalQAError(
                f"Critical QA errors found. Report saved. "
                f"Errors: {report.errors}, Warnings: {report.warnings}"
            )

        return report

    def get_summary(self, report: QAReport) -> Dict:
        """
        Get summary statistics from report.

        Args:
            report: QA report

        Returns:
            Summary dictionary
        """
        return {
            "timestamp": report.timestamp.isoformat(),
            "project": report.project,
            "phase": report.phase,
            "total_checks": report.total_checks,
            "passed": report.passed,
            "warnings": report.warnings,
            "errors": report.errors,
            "skipped": report.skipped,
            "status": report.status.value,
            "pass_rate": f"{(report.passed / report.total_checks * 100):.1f}%" if report.total_checks > 0 else "N/A",
        }


def create_default_config(output_path: Path):
    """
    Create default QA configuration file.

    Args:
        output_path: Path to write config
    """
    default_config = {
        "reproducibility": {
            "require_pinned_deps": True,
            "require_seed_docs": True,
            "require_docker": False,
            "check_data_provenance": True,
        },
        "citations": {
            "check_retractions": True,
            "validate_dois": True,
            "min_citation_count": 20,
            "require_recent_papers": True,
            "recent_paper_threshold_years": 5,
            "crossref_email": None,  # Set your email for Crossref API
        },
        "statistics": {
            "require_power_analysis": True,
            "min_power": 0.80,
            "require_effect_sizes": True,
            "require_confidence_intervals": True,
            "check_multiple_comparisons": True,
            "require_assumption_checks": True,
        },
        "qa_manager": {
            "block_on_critical": True,
            "report_format": "markdown",  # markdown or json
            "report_dir": "qa_reports",
        }
    }

    with open(output_path, "w") as f:
        yaml.dump(default_config, f, default_flow_style=False, sort_keys=False)

    logger.info(f"Created default QA config at {output_path}")
