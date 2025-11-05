"""
CLI Interface for QA System

Command-line interface for running QA checks.
"""

import argparse
import sys
from pathlib import Path
import logging

from .qa_manager import QAManager, create_default_config
from .base import ValidationStatus

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Research Quality Assurance System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full QA suite
  python -m code.quality_assurance.cli full

  # Run specific validator
  python -m code.quality_assurance.cli reproducibility
  python -m code.quality_assurance.cli citations
  python -m code.quality_assurance.cli statistics

  # Run for specific phase
  python -m code.quality_assurance.cli full --phase analysis

  # Generate default config
  python -m code.quality_assurance.cli init

  # Use custom config
  python -m code.quality_assurance.cli full --config .qa_config.yaml
        """
    )

    parser.add_argument(
        "command",
        choices=["full", "reproducibility", "citations", "statistics", "init"],
        help="QA command to run"
    )

    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Project root directory (default: current directory)"
    )

    parser.add_argument(
        "--config",
        type=Path,
        help="Path to .qa_config.yaml (default: .qa_config.yaml in project root)"
    )

    parser.add_argument(
        "--phase",
        type=str,
        help="Research phase name (for phase-specific QA)"
    )

    parser.add_argument(
        "--output",
        type=Path,
        help="Output path for report (default: qa_reports/ in project root)"
    )

    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Report format (default: markdown)"
    )

    parser.add_argument(
        "--no-block",
        action="store_true",
        help="Don't block/exit with error on critical issues"
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress output except errors"
    )

    args = parser.parse_args()

    # Set logging level
    if args.quiet:
        logging.getLogger().setLevel(logging.ERROR)

    # Handle init command
    if args.command == "init":
        config_path = args.project_root / ".qa_config.yaml"
        if config_path.exists():
            print(f"Config already exists at {config_path}")
            response = input("Overwrite? (y/N): ")
            if response.lower() != "y":
                print("Aborted")
                return 0

        create_default_config(config_path)
        print(f"Created default QA config at {config_path}")
        return 0

    # Determine config file
    config_file = args.config
    if config_file is None:
        default_config = args.project_root / ".qa_config.yaml"
        if default_config.exists():
            config_file = default_config

    # Initialize QA manager
    try:
        manager = QAManager(args.project_root, config_file)
    except Exception as e:
        logger.error(f"Failed to initialize QA manager: {e}")
        return 1

    # Override block_on_critical if requested
    if args.no_block:
        manager.config["qa_manager"]["block_on_critical"] = False

    # Override report format if specified
    if args.format:
        manager.config["qa_manager"]["report_format"] = args.format

    # Run appropriate command
    try:
        if args.command == "full":
            report = manager.run_full_qa(phase=args.phase)

        elif args.command == "reproducibility":
            logger.info("Running reproducibility validation...")
            results = manager.reproducibility.validate()
            from .base import QAReport
            from datetime import datetime
            report = QAReport(
                timestamp=datetime.now(),
                project=str(args.project_root.name),
                phase=args.phase,
                results=results
            )

        elif args.command == "citations":
            logger.info("Running citation verification...")
            results = manager.citations.validate()
            from .base import QAReport
            from datetime import datetime
            report = QAReport(
                timestamp=datetime.now(),
                project=str(args.project_root.name),
                phase=args.phase,
                results=results
            )

        elif args.command == "statistics":
            logger.info("Running statistical validation...")
            results = manager.statistics.validate()
            from .base import QAReport
            from datetime import datetime
            report = QAReport(
                timestamp=datetime.now(),
                project=str(args.project_root.name),
                phase=args.phase,
                results=results
            )

        else:
            logger.error(f"Unknown command: {args.command}")
            return 1

    except Exception as e:
        logger.error(f"QA check failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # Save report
    try:
        output_path = manager.generate_and_save_report(report, args.output)
        print(f"\nQA Report saved to: {output_path}")
    except Exception as e:
        logger.error(f"Failed to save report: {e}")

    # Print summary
    if not args.quiet:
        print("\n" + "=" * 70)
        print("QA SUMMARY")
        print("=" * 70)
        summary = manager.get_summary(report)
        for key, value in summary.items():
            if key != "timestamp":
                print(f"{key.replace('_', ' ').title()}: {value}")
        print("=" * 70)

        # Print errors and warnings
        if report.errors > 0:
            print(f"\n❌ {report.errors} ERROR(S):")
            for result in report.results:
                if result.is_error():
                    print(f"  - {result.check_name}: {result.message}")

        if report.warnings > 0:
            print(f"\n⚠️  {report.warnings} WARNING(S):")
            for result in report.results:
                if result.is_warning():
                    print(f"  - {result.check_name}: {result.message}")

    # Check for critical errors
    has_critical = manager.check_critical_errors(report)

    # Exit with appropriate code
    if has_critical:
        logger.error("Critical QA errors found. See report for details.")
        return 1
    elif report.errors > 0:
        if manager.config.get("qa_manager", {}).get("block_on_critical", True):
            logger.warning("QA errors found but not critical. Proceeding.")
            return 1
        else:
            return 0
    else:
        if not args.quiet:
            print("\n✅ QA checks passed!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
