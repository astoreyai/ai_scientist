"""
Auto Tracking

Automatic tracking of data files and experiments.
"""

from pathlib import Path
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)


class AutoTracker:
    """
    Automatic tracker for data files and experiments.

    Integrates DVC, MLflow, and git to provide seamless tracking.
    """

    def __init__(
        self,
        project_root: Path,
        dvc_manager=None,
        mlflow_manager=None,
        git_manager=None
    ):
        """
        Initialize auto tracker.

        Args:
            project_root: Project root directory
            dvc_manager: DVCManager instance
            mlflow_manager: MLflowManager instance
            git_manager: GitWorkflowManager instance
        """
        self.project_root = Path(project_root)
        self.dvc = dvc_manager
        self.mlflow = mlflow_manager
        self.git = git_manager

    def track_data_file(
        self,
        filepath: Path,
        commit: bool = True,
        commit_message: Optional[str] = None
    ) -> bool:
        """
        Automatically track data file with appropriate system.

        - Large files (>10MB): DVC
        - Small files: git
        - Always commit changes

        Args:
            filepath: Path to file
            commit: Create git commit
            commit_message: Custom commit message

        Returns:
            True if successful
        """
        file_path = self.project_root / filepath

        if not file_path.exists():
            logger.error(f"File not found: {filepath}")
            return False

        # Check file size
        size_mb = file_path.stat().st_size / (1024 * 1024)

        try:
            if size_mb >= 10.0 and self.dvc:
                # Track with DVC
                logger.info(f"Tracking {filepath} with DVC ({size_mb:.1f} MB)")
                success = self.dvc.track_file(filepath)

                if success and commit and self.git:
                    message = commit_message or f"data(collection): Add {filepath.name}"
                    self.git.commit_with_convention(
                        "data",
                        "collection",
                        f"Add {filepath.name}",
                        body=f"File size: {size_mb:.1f} MB\nTracked with DVC"
                    )

                return success

            else:
                # Track with git
                logger.info(f"Tracking {filepath} with git ({size_mb:.1f} MB)")

                if commit and self.git:
                    message = commit_message or f"data(collection): Add {filepath.name}"
                    self.git.commit_with_convention(
                        "data",
                        "collection",
                        f"Add {filepath.name}",
                        body=f"File size: {size_mb:.1f} MB",
                        files=[str(filepath)]
                    )

                return True

        except Exception as e:
            logger.error(f"Error tracking file: {e}")
            return False

    def track_experiment_results(
        self,
        experiment_name: str,
        params: dict,
        metrics: dict,
        artifacts: Optional[List[Path]] = None
    ) -> Optional[str]:
        """
        Automatically track experiment results.

        Args:
            experiment_name: Experiment name
            params: Parameters dictionary
            metrics: Metrics dictionary
            artifacts: List of artifact files

        Returns:
            MLflow run ID or None
        """
        if not self.mlflow:
            logger.warning("MLflow manager not available")
            return None

        try:
            run_id = self.mlflow.create_experiment_run(
                run_name=experiment_name,
                params=params,
                metrics=metrics,
                artifacts=artifacts
            )

            logger.info(f"Tracked experiment: {experiment_name} (run_id: {run_id})")
            return run_id

        except Exception as e:
            logger.error(f"Error tracking experiment: {e}")
            return None

    def track_phase_completion(
        self,
        phase_name: str,
        outputs: List[str],
        validation_score: float,
        tag_version: Optional[str] = None
    ) -> bool:
        """
        Track completion of research phase.

        Args:
            phase_name: Phase name
            outputs: Output files
            validation_score: Validation score
            tag_version: Version for git tag

        Returns:
            True if successful
        """
        success = True

        # Log to MLflow
        if self.mlflow:
            try:
                self.mlflow.log_research_phase(
                    phase=phase_name,
                    outputs=outputs,
                    validation_score=validation_score
                )
                logger.info(f"Logged phase to MLflow: {phase_name}")
            except Exception as e:
                logger.error(f"Failed to log to MLflow: {e}")
                success = False

        # Create git tag
        if self.git and tag_version:
            try:
                self.git.tag_phase_completion(
                    phase_name=phase_name,
                    version=tag_version,
                    message=f"Phase complete: {phase_name} (score: {validation_score})"
                )
                logger.info(f"Created git tag for phase: {phase_name}")
            except Exception as e:
                logger.error(f"Failed to create tag: {e}")
                success = False

        return success

    def scan_and_track_large_files(
        self,
        directory: Path,
        size_threshold_mb: float = 10.0
    ) -> List[Path]:
        """
        Scan directory and automatically track large files.

        Args:
            directory: Directory to scan
            size_threshold_mb: Size threshold for DVC tracking

        Returns:
            List of tracked files
        """
        if not self.dvc:
            logger.warning("DVC manager not available")
            return []

        return self.dvc.auto_track_large_files(directory, size_threshold_mb)


def create_auto_tracker(
    project_root: Path,
    enable_dvc: bool = True,
    enable_mlflow: bool = True,
    enable_git: bool = True
):
    """
    Create auto tracker with all managers.

    Args:
        project_root: Project root directory
        enable_dvc: Enable DVC tracking
        enable_mlflow: Enable MLflow tracking
        enable_git: Enable git integration

    Returns:
        AutoTracker instance
    """
    from .dvc_manager import DVCManager
    from .mlflow_manager import MLflowManager
    from .git_workflows import GitWorkflowManager

    dvc = DVCManager(project_root) if enable_dvc else None
    mlflow = MLflowManager() if enable_mlflow else None
    git = GitWorkflowManager(project_root) if enable_git else None

    return AutoTracker(project_root, dvc, mlflow, git)
