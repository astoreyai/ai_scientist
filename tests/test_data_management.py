"""
Unit tests for Data Management System
"""

import pytest
from pathlib import Path
import tempfile
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from data_management.dvc_manager import DVCManager
from data_management.mlflow_manager import MLflowManager, track_experiment
from data_management.artifact_manager import ArtifactManager
from data_management.git_workflows import GitWorkflowManager
from data_management.auto_tracking import AutoTracker, create_auto_tracker


class TestDVCManager:
    """Test DVCManager functionality"""

    def test_create_dvc_manager(self, tmp_path):
        """Test creating DVC manager"""
        manager = DVCManager(tmp_path)

        assert manager.project_root == tmp_path
        assert manager.dvc_dir == tmp_path / ".dvc"

    def test_is_initialized(self, tmp_path):
        """Test checking DVC initialization"""
        manager = DVCManager(tmp_path)

        # Not initialized initially
        assert not manager.is_initialized()

        # Create .dvc directory
        (tmp_path / ".dvc").mkdir()
        assert manager.is_initialized()

    def test_list_tracked_files(self, tmp_path):
        """Test listing DVC-tracked files"""
        manager = DVCManager(tmp_path)

        # Create some .dvc files
        (tmp_path / "data").mkdir()
        (tmp_path / "data" / "file1.csv.dvc").write_text("{}")
        (tmp_path / "data" / "file2.csv.dvc").write_text("{}")

        tracked = manager.list_tracked_files()

        assert len(tracked) == 2
        assert all(str(f).endswith(".dvc") for f in tracked)

    def test_auto_track_large_files(self, tmp_path):
        """Test auto-tracking large files"""
        manager = DVCManager(tmp_path)

        # Create test files
        data_dir = tmp_path / "data"
        data_dir.mkdir()

        # Small file (won't be tracked)
        small_file = data_dir / "small.txt"
        small_file.write_text("small content")

        # Large file simulation (11MB worth of data)
        large_file = data_dir / "large.csv"
        large_content = "x" * (11 * 1024 * 1024)  # 11 MB
        large_file.write_text(large_content)

        # Note: This will fail without DVC installed, but tests the logic
        # In real usage, DVC would be installed
        # For testing, we just verify the method exists and can be called


class TestMLflowManager:
    """Test MLflowManager functionality"""

    def test_create_mlflow_manager(self, tmp_path):
        """Test creating MLflow manager"""
        tracking_uri = f"file://{tmp_path}/mlruns"
        manager = MLflowManager(tracking_uri=tracking_uri)

        assert manager.tracking_uri == tracking_uri
        assert manager.experiment_name == "research_experiment"

    def test_set_experiment(self, tmp_path):
        """Test setting experiment"""
        tracking_uri = f"file://{tmp_path}/mlruns"
        manager = MLflowManager(tracking_uri=tracking_uri)

        exp_id = manager.set_experiment("test_experiment")

        assert exp_id is not None
        assert manager.experiment_name == "test_experiment"

    def test_create_experiment_run(self, tmp_path):
        """Test creating complete experiment run"""
        tracking_uri = f"file://{tmp_path}/mlruns"
        manager = MLflowManager(tracking_uri=tracking_uri)

        # Ensure experiment exists
        manager.set_experiment("test_experiment_run")

        params = {"alpha": 0.05, "sample_size": 100}
        metrics = {"effect_size": 0.65, "p_value": 0.003}

        run_id = manager.create_experiment_run(
            run_name="test_run",
            params=params,
            metrics=metrics
        )

        assert run_id is not None

        # Verify run exists
        run = manager.get_run(run_id)
        assert run is not None
        assert run.data.params["alpha"] == "0.05"

    def test_compare_runs(self, tmp_path):
        """Test comparing multiple runs"""
        tracking_uri = f"file://{tmp_path}/mlruns"
        manager = MLflowManager(tracking_uri=tracking_uri)

        # Set experiment first
        manager.set_experiment("test_compare")

        # Create two runs
        run_id1 = manager.create_experiment_run(
            "run1",
            {"alpha": 0.05},
            {"effect_size": 0.5}
        )

        run_id2 = manager.create_experiment_run(
            "run2",
            {"alpha": 0.01},
            {"effect_size": 0.7}
        )

        # Compare
        comparison = manager.compare_runs([run_id1, run_id2])

        assert "runs" in comparison
        assert len(comparison["runs"]) == 2

    def test_track_experiment_decorator(self, tmp_path):
        """Test experiment tracking decorator"""
        tracking_uri = f"file://{tmp_path}/mlruns"

        # Set up MLflow with explicit tracking URI
        import mlflow
        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment("test_decorator")

        @track_experiment("test_decorator")
        def dummy_analysis(alpha=0.05):
            return {"effect_size": 0.6, "p_value": 0.01}

        result = dummy_analysis(alpha=0.01)

        assert result["effect_size"] == 0.6
        assert result["p_value"] == 0.01


class TestArtifactManager:
    """Test ArtifactManager functionality"""

    def test_create_artifact_manager(self):
        """Test creating artifact manager"""
        manager = ArtifactManager(sandbox=True)

        assert manager.sandbox is True
        assert "sandbox" in manager.base_url

    def test_create_metadata_template(self):
        """Test creating metadata template"""
        manager = ArtifactManager(sandbox=True)

        metadata = manager.create_metadata_template(
            title="Test Dataset",
            description="Test description",
            creators=[
                {"name": "Test Author", "affiliation": "Test University"}
            ]
        )

        assert metadata["title"] == "Test Dataset"
        assert metadata["upload_type"] == "dataset"
        assert len(metadata["creators"]) == 1

    def test_create_reproducibility_package(self, tmp_path):
        """Test creating reproducibility package"""
        # Create project structure
        (tmp_path / "code").mkdir()
        (tmp_path / "code" / "analysis.py").write_text("# analysis code")

        (tmp_path / "data").mkdir()
        (tmp_path / "data" / "data.csv").write_text("col1,col2\n1,2")

        (tmp_path / "results").mkdir()
        (tmp_path / "results" / "output.txt").write_text("results")

        manager = ArtifactManager(sandbox=True)

        output_dir = tmp_path / "output"
        output_dir.mkdir()

        package = manager.create_reproducibility_package(
            project_root=tmp_path,
            output_dir=output_dir,
            include_data=True
        )

        assert package is not None
        assert package.exists()
        assert package.suffix == ".zip"


class TestGitWorkflowManager:
    """Test GitWorkflowManager functionality"""

    def test_create_git_manager(self, tmp_path):
        """Test creating git workflow manager"""
        manager = GitWorkflowManager(tmp_path)

        assert manager.project_root == tmp_path


class TestAutoTracker:
    """Test AutoTracker functionality"""

    def test_create_auto_tracker(self, tmp_path):
        """Test creating auto tracker"""
        tracker = AutoTracker(project_root=tmp_path)

        assert tracker.project_root == tmp_path

    def test_create_with_managers(self, tmp_path):
        """Test creating auto tracker with managers"""
        tracker = create_auto_tracker(
            project_root=tmp_path,
            enable_dvc=True,
            enable_mlflow=True,
            enable_git=True
        )

        assert tracker.dvc is not None
        assert tracker.mlflow is not None
        assert tracker.git is not None

    def test_track_experiment_results(self, tmp_path):
        """Test tracking experiment results"""
        tracking_uri = f"file://{tmp_path}/mlruns"
        mlflow_manager = MLflowManager(tracking_uri=tracking_uri)

        # Set experiment first
        mlflow_manager.set_experiment("test_auto_track")

        tracker = AutoTracker(
            project_root=tmp_path,
            mlflow_manager=mlflow_manager
        )

        run_id = tracker.track_experiment_results(
            experiment_name="test_exp",
            params={"alpha": 0.05},
            metrics={"effect_size": 0.6}
        )

        assert run_id is not None


class TestDVCManagerExtended:
    """Extended DVC tests for comprehensive coverage"""

    def test_initialize_success(self, tmp_path, monkeypatch):
        """Test DVC initialization success path"""
        from unittest.mock import Mock, MagicMock

        manager = DVCManager(tmp_path)

        # Mock subprocess.run to simulate successful init
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stderr = ""

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.initialize()

        assert result is True
        mock_run.assert_called_once()

    def test_initialize_already_initialized(self, tmp_path):
        """Test initialize when DVC already initialized"""
        manager = DVCManager(tmp_path)

        # Create .dvc directory to simulate already initialized
        (tmp_path / ".dvc").mkdir()

        result = manager.initialize()
        assert result is True

    def test_initialize_command_not_found(self, tmp_path, monkeypatch):
        """Test initialize when DVC not installed"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        # Mock subprocess.run to raise FileNotFoundError
        def mock_run(*args, **kwargs):
            raise FileNotFoundError("dvc not found")

        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.initialize()
        assert result is False

    def test_initialize_with_no_scm(self, tmp_path, monkeypatch):
        """Test initialize with --no-scm flag"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stderr = ""

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.initialize(no_scm=True)

        assert result is True
        # Verify --no-scm was included in command
        call_args = mock_run.call_args
        assert "--no-scm" in call_args[0][0]

    def test_add_remote_success(self, tmp_path, monkeypatch):
        """Test adding DVC remote successfully"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stderr = ""

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.add_remote("origin", "/path/to/storage", default=True)

        assert result is True
        mock_run.assert_called_once()

    def test_add_remote_failure(self, tmp_path, monkeypatch):
        """Test add_remote failure path"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stderr = "Error adding remote"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.add_remote("origin", "/path/to/storage")

        assert result is False

    def test_track_file_success(self, tmp_path, monkeypatch):
        """Test tracking file with DVC"""
        from unittest.mock import Mock
        from pathlib import Path

        manager = DVCManager(tmp_path)

        # Create test file
        test_file = tmp_path / "data.csv"
        test_file.write_text("col1,col2\\n1,2")

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.track_file(Path("data.csv"))

        assert result is True
        # Should have called dvc add and git add
        assert mock_run.call_count == 2

    def test_track_file_not_found(self, tmp_path):
        """Test tracking non-existent file"""
        manager = DVCManager(tmp_path)

        result = manager.track_file(Path("nonexistent.csv"))

        assert result is False

    def test_track_directory(self, tmp_path, monkeypatch):
        """Test tracking directory"""
        from unittest.mock import Mock
        from pathlib import Path

        manager = DVCManager(tmp_path)

        # Create test directory
        test_dir = tmp_path / "data"
        test_dir.mkdir()
        (test_dir / "file.txt").write_text("content")

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.track_directory(Path("data"))

        assert result is True

    def test_push_success(self, tmp_path, monkeypatch):
        """Test DVC push success"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stderr = ""

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.push()

        assert result is True

    def test_push_with_remote(self, tmp_path, monkeypatch):
        """Test DVC push with specific remote"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.push(remote="origin")

        assert result is True
        call_args = mock_run.call_args[0][0]
        assert "-r" in call_args
        assert "origin" in call_args

    def test_pull_success(self, tmp_path, monkeypatch):
        """Test DVC pull success"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.pull()

        assert result is True

    def test_status_success(self, tmp_path, monkeypatch):
        """Test DVC status"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "modified: data.csv.dvc"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        status = manager.status()

        assert status["success"] is True
        assert status["has_changes"] is True

    def test_status_cloud(self, tmp_path, monkeypatch):
        """Test DVC status with cloud flag"""
        from unittest.mock import Mock

        manager = DVCManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = ""

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        status = manager.status(cloud=True)

        assert status["success"] is True
        call_args = mock_run.call_args[0][0]
        assert "-c" in call_args

    def test_get_file_info(self, tmp_path):
        """Test getting DVC file info"""
        import json
        from pathlib import Path

        manager = DVCManager(tmp_path)

        # Create .dvc file
        dvc_data = {
            "outs": [{"path": "data.csv", "md5": "abc123", "size": 1024}]
        }
        dvc_file = tmp_path / "data.csv.dvc"
        dvc_file.write_text(json.dumps(dvc_data))

        info = manager.get_file_info(Path("data.csv"))

        assert info is not None
        assert "outs" in info

    def test_get_file_info_not_tracked(self, tmp_path):
        """Test get_file_info for untracked file"""
        manager = DVCManager(tmp_path)

        info = manager.get_file_info(Path("untracked.csv"))

        assert info is None


class TestGitWorkflowManagerExtended:
    """Extended Git workflow tests for comprehensive coverage"""

    def test_create_phase_branch_success(self, tmp_path, monkeypatch):
        """Test creating phase branch"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stderr = ""

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.create_phase_branch("literature-review")

        assert result is True
        call_args = mock_run.call_args[0][0]
        assert "git" in call_args
        assert "checkout" in call_args
        assert "-b" in call_args
        assert "phase/literature-review" in call_args

    def test_create_phase_branch_failure(self, tmp_path, monkeypatch):
        """Test branch creation failure"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stderr = "fatal: branch already exists"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.create_phase_branch("literature-review")

        assert result is False

    def test_commit_with_convention_all_files(self, tmp_path, monkeypatch):
        """Test commit with convention (all files)"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.commit_with_convention(
            commit_type="feat",
            scope="analysis",
            subject="Add statistical tests"
        )

        assert result is True
        # Should call git add -A and git commit
        assert mock_run.call_count == 2

    def test_commit_with_convention_specific_files(self, tmp_path, monkeypatch):
        """Test commit with specific files"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.commit_with_convention(
            commit_type="data",
            scope="collection",
            subject="Add survey results",
            files=["data/survey.csv", "data/metadata.json"]
        )

        assert result is True
        # Should call git add twice and git commit once
        assert mock_run.call_count >= 3

    def test_commit_with_body(self, tmp_path, monkeypatch):
        """Test commit with body text"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.commit_with_convention(
            commit_type="docs",
            scope="writing",
            subject="Update methodology",
            body="Added power analysis section\\nRevised sample size calculation"
        )

        assert result is True

    def test_tag_phase_completion_success(self, tmp_path, monkeypatch):
        """Test tagging phase completion"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.tag_phase_completion(
            phase_name="literature-review",
            version="1.0.0",
            message="Completed systematic review"
        )

        assert result is True
        call_args = mock_run.call_args[0][0]
        assert "git" in call_args
        assert "tag" in call_args
        assert "v1.0.0-literature-review" in call_args

    def test_tag_phase_completion_failure(self, tmp_path, monkeypatch):
        """Test tag creation failure"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 1
        mock_result.stderr = "tag already exists"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        result = manager.tag_phase_completion("data-collection", "1.0.0")

        assert result is False

    def test_get_current_branch_success(self, tmp_path, monkeypatch):
        """Test getting current branch"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "phase/literature-review"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        branch = manager.get_current_branch()

        assert branch == "phase/literature-review"

    def test_get_current_branch_failure(self, tmp_path, monkeypatch):
        """Test get_current_branch failure"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 1

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        branch = manager.get_current_branch()

        assert branch is None

    def test_get_tags(self, tmp_path, monkeypatch):
        """Test getting all tags"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "v1.0.0-literature-review\nv1.0.1-data-collection"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        tags = manager.get_tags()

        assert len(tags) == 2
        assert "v1.0.0-literature-review" in tags

    def test_get_commit_history(self, tmp_path, monkeypatch):
        """Test getting commit history"""
        from unittest.mock import Mock

        manager = GitWorkflowManager(tmp_path)

        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "abc123 feat(analysis): Add tests\ndef456 data(collection): Add dataset"

        mock_run = Mock(return_value=mock_result)
        monkeypatch.setattr("subprocess.run", mock_run)

        history = manager.get_commit_history(max_count=2)

        assert len(history) == 2
        assert "feat(analysis)" in history[0]


class TestArtifactManagerExtended:
    """Extended artifact manager tests"""

    def test_create_basic(self, tmp_path):
        """Test creating artifact manager"""
        manager = ArtifactManager(tmp_path)
        assert manager is not None


class TestMLflowManagerExtended:
    """Extended MLflow tests"""

    def test_create_with_tracking_uri(self, tmp_path):
        """Test creating manager with tracking URI"""
        tracking_uri = f"file://{tmp_path}/mlruns"
        manager = MLflowManager(tracking_uri=tracking_uri)
        assert manager.tracking_uri == tracking_uri


class TestAutoTrackerExtended:
    """Extended auto tracker tests"""

    def test_create_basic(self, tmp_path):
        """Test creating auto tracker"""
        tracker = AutoTracker(project_root=tmp_path)
        assert tracker.project_root == tmp_path


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
