"""
MLflow Manager

Manages MLflow experiment tracking, logging, and artifact management.
"""

from pathlib import Path
from typing import Optional, Dict, List, Any
import mlflow
from mlflow.tracking import MlflowClient
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class MLflowManager:
    """
    Manager for MLflow experiment tracking.

    Handles:
    - Experiment setup
    - Run logging
    - Metric tracking
    - Artifact management
    - Model registry
    """

    def __init__(
        self,
        tracking_uri: Optional[str] = None,
        experiment_name: str = "research_experiment"
    ):
        """
        Initialize MLflow manager.

        Args:
            tracking_uri: MLflow tracking URI (defaults to ./mlruns)
            experiment_name: Default experiment name
        """
        self.tracking_uri = tracking_uri or "file:./mlruns"
        self.experiment_name = experiment_name
        self.client = None

        self._setup()

    def _setup(self):
        """Configure MLflow"""
        mlflow.set_tracking_uri(self.tracking_uri)
        self.client = MlflowClient(tracking_uri=self.tracking_uri)
        logger.info(f"MLflow tracking URI: {self.tracking_uri}")

    def set_experiment(self, experiment_name: str) -> str:
        """
        Set active experiment.

        Args:
            experiment_name: Experiment name

        Returns:
            Experiment ID
        """
        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)

        experiment = self.client.get_experiment_by_name(experiment_name)
        return experiment.experiment_id

    def start_run(
        self,
        run_name: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None
    ):
        """
        Start MLflow run (context manager).

        Args:
            run_name: Name for this run
            tags: Tags to attach to run

        Returns:
            MLflow run context
        """
        return mlflow.start_run(run_name=run_name, tags=tags)

    def log_params(self, params: Dict[str, Any]):
        """Log multiple parameters"""
        for key, value in params.items():
            mlflow.log_param(key, value)

    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None):
        """Log multiple metrics"""
        for key, value in metrics.items():
            mlflow.log_metric(key, value, step=step)

    def log_artifact(self, filepath: Path, artifact_path: Optional[str] = None):
        """
        Log artifact file.

        Args:
            filepath: Path to file
            artifact_path: Subdirectory in artifact store
        """
        mlflow.log_artifact(str(filepath), artifact_path)

    def log_dict(self, dictionary: Dict, filename: str):
        """Log dictionary as JSON artifact"""
        mlflow.log_dict(dictionary, filename)

    def log_figure(self, figure, filename: str):
        """
        Log matplotlib figure.

        Args:
            figure: Matplotlib figure object
            filename: Filename for saved figure
        """
        mlflow.log_figure(figure, filename)

    def create_experiment_run(
        self,
        run_name: str,
        params: Dict[str, Any],
        metrics: Dict[str, float],
        artifacts: Optional[List[Path]] = None,
        tags: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Create complete experiment run.

        Args:
            run_name: Run name
            params: Parameters to log
            metrics: Metrics to log
            artifacts: Artifacts to upload
            tags: Tags for run

        Returns:
            Run ID
        """
        with self.start_run(run_name=run_name, tags=tags) as run:
            # Log parameters
            self.log_params(params)

            # Log metrics
            self.log_metrics(metrics)

            # Log artifacts
            if artifacts:
                for artifact in artifacts:
                    self.log_artifact(artifact)

            return run.info.run_id

    def get_experiment(self, experiment_name: Optional[str] = None):
        """Get experiment by name"""
        name = experiment_name or self.experiment_name
        return self.client.get_experiment_by_name(name)

    def search_runs(
        self,
        filter_string: Optional[str] = None,
        max_results: int = 100,
        order_by: Optional[List[str]] = None
    ):
        """
        Search runs in current experiment.

        Args:
            filter_string: Filter (e.g., "metrics.rmse < 1")
            max_results: Maximum results to return
            order_by: List of order by clauses

        Returns:
            List of runs
        """
        experiment = self.get_experiment()

        return self.client.search_runs(
            experiment_ids=[experiment.experiment_id],
            filter_string=filter_string,
            max_results=max_results,
            order_by=order_by
        )

    def get_run(self, run_id: str):
        """Get run by ID"""
        return self.client.get_run(run_id)

    def compare_runs(self, run_ids: List[str]) -> Dict:
        """
        Compare multiple runs.

        Args:
            run_ids: List of run IDs

        Returns:
            Dictionary with comparison data
        """
        runs_data = []

        for run_id in run_ids:
            run = self.get_run(run_id)
            runs_data.append({
                "run_id": run_id,
                "run_name": run.data.tags.get("mlflow.runName", ""),
                "params": run.data.params,
                "metrics": run.data.metrics,
                "start_time": run.info.start_time
            })

        return {
            "runs": runs_data,
            "compared_at": datetime.now().isoformat()
        }

    def get_best_run(
        self,
        metric: str,
        ascending: bool = False
    ):
        """
        Get best run by metric.

        Args:
            metric: Metric name
            ascending: True for minimization, False for maximization

        Returns:
            Best run
        """
        order = "ASC" if ascending else "DESC"
        runs = self.search_runs(
            max_results=1,
            order_by=[f"metrics.{metric} {order}"]
        )

        if runs:
            return runs[0]
        return None

    def log_research_phase(
        self,
        phase: str,
        outputs: List[str],
        validation_score: float,
        notes: str = ""
    ):
        """
        Log completion of research phase.

        Args:
            phase: Phase name
            outputs: List of output files
            validation_score: Validation score (0-1)
            notes: Additional notes
        """
        with self.start_run(run_name=f"phase_{phase}") as run:
            # Log phase info
            mlflow.log_param("phase", phase)
            mlflow.log_param("outputs_count", len(outputs))

            # Log metrics
            mlflow.log_metric("validation_score", validation_score)

            # Log outputs as text artifact
            outputs_text = "\n".join(outputs)
            mlflow.log_text(outputs_text, "outputs.txt")

            # Log notes
            if notes:
                mlflow.log_text(notes, "notes.txt")

            return run.info.run_id

    def export_experiments(self, output_path: Path):
        """
        Export all experiments to CSV.

        Args:
            output_path: Path for output CSV
        """
        import pandas as pd

        experiment = self.get_experiment()
        runs = self.search_runs(max_results=10000)

        data = []
        for run in runs:
            row = {
                "run_id": run.info.run_id,
                "run_name": run.data.tags.get("mlflow.runName", ""),
                "start_time": run.info.start_time,
                "status": run.info.status,
                **{f"param.{k}": v for k, v in run.data.params.items()},
                **{f"metric.{k}": v for k, v in run.data.metrics.items()}
            }
            data.append(row)

        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
        logger.info(f"Exported {len(runs)} runs to {output_path}")

    def cleanup_old_runs(self, days: int = 30):
        """
        Delete runs older than specified days.

        Args:
            days: Age threshold in days
        """
        from datetime import timedelta

        cutoff_time = datetime.now() - timedelta(days=days)
        cutoff_ms = int(cutoff_time.timestamp() * 1000)

        experiment = self.get_experiment()
        runs = self.client.search_runs(
            experiment_ids=[experiment.experiment_id],
            filter_string=f"attributes.start_time < {cutoff_ms}"
        )

        deleted_count = 0
        for run in runs:
            self.client.delete_run(run.info.run_id)
            deleted_count += 1

        logger.info(f"Deleted {deleted_count} runs older than {days} days")
        return deleted_count


def track_experiment(experiment_name: Optional[str] = None):
    """
    Decorator to automatically track function as MLflow experiment.

    Usage:
        @track_experiment("my_analysis")
        def run_analysis(data, alpha=0.05):
            # Analysis code
            return {"effect_size": 0.5, "p_value": 0.01}
    """
    def decorator(func):
        from functools import wraps

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use current MLflow tracking URI (respects already-set URI)
            current_uri = mlflow.get_tracking_uri()

            # Set experiment (will use current tracking URI)
            if experiment_name:
                mlflow.set_experiment(experiment_name)
            else:
                mlflow.set_experiment(func.__name__)

            with mlflow.start_run(run_name=func.__name__):
                # Log parameters
                for key, value in kwargs.items():
                    mlflow.log_param(key, value)

                # Execute function
                result = func(*args, **kwargs)

                # Log result metrics if dict
                if isinstance(result, dict):
                    metrics = {
                        k: v for k, v in result.items()
                        if isinstance(v, (int, float))
                    }
                    if metrics:
                        for k, v in metrics.items():
                            mlflow.log_metric(k, v)

                return result

        return wrapper
    return decorator
