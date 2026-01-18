"""
DVC Manager

Manages Data Version Control (DVC) operations for large files and datasets.
"""

from pathlib import Path
from typing import Optional, List, Dict
import subprocess
import json
import logging

logger = logging.getLogger(__name__)


class DVCManager:
    """
    Manager for DVC (Data Version Control) operations.

    Handles:
    - DVC initialization
    - File tracking
    - Remote storage configuration
    - Push/pull operations
    - Pipeline management
    """

    def __init__(self, project_root: Path):
        """
        Initialize DVC manager.

        Args:
            project_root: Project root directory
        """
        self.project_root = Path(project_root)
        self.dvc_dir = self.project_root / ".dvc"

    def is_initialized(self) -> bool:
        """Check if DVC is initialized in project"""
        return self.dvc_dir.exists() and self.dvc_dir.is_dir()

    def initialize(self, no_scm: bool = False) -> bool:
        """
        Initialize DVC in project.

        Args:
            no_scm: Initialize without git (standalone DVC)

        Returns:
            True if successful
        """
        if self.is_initialized():
            logger.info("DVC already initialized")
            return True

        try:
            cmd = ["dvc", "init"]
            if no_scm:
                cmd.append("--no-scm")

            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info("DVC initialized successfully")
                return True
            else:
                logger.error(f"DVC init failed: {result.stderr}")
                return False

        except FileNotFoundError:
            logger.error("DVC not installed. Install with: pip install dvc")
            return False

    def add_remote(
        self,
        name: str,
        url: str,
        default: bool = True
    ) -> bool:
        """
        Add remote storage for DVC.

        Args:
            name: Remote name
            url: Remote URL (s3://bucket, gs://bucket, /path/to/storage)
            default: Set as default remote

        Returns:
            True if successful
        """
        try:
            cmd = ["dvc", "remote", "add"]
            if default:
                cmd.append("-d")
            cmd.extend([name, url])

            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info(f"Added DVC remote '{name}': {url}")
                return True
            else:
                logger.error(f"Failed to add remote: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error adding remote: {e}")
            return False

    def track_file(self, filepath: Path) -> bool:
        """
        Track a file with DVC.

        Args:
            filepath: Path to file (relative to project root)

        Returns:
            True if successful
        """
        file_path = self.project_root / filepath

        if not file_path.exists():
            logger.error(f"File not found: {filepath}")
            return False

        try:
            result = subprocess.run(
                ["dvc", "add", str(filepath)],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info(f"Tracking {filepath} with DVC")
                # Also stage the .dvc file and .gitignore
                subprocess.run(
                    ["git", "add", f"{filepath}.dvc", ".gitignore"],
                    cwd=self.project_root
                )
                return True
            else:
                logger.error(f"DVC add failed: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error tracking file: {e}")
            return False

    def track_directory(self, dirpath: Path) -> bool:
        """
        Track entire directory with DVC.

        Args:
            dirpath: Path to directory

        Returns:
            True if successful
        """
        return self.track_file(dirpath)

    def push(self, remote: Optional[str] = None) -> bool:
        """
        Push DVC-tracked files to remote storage.

        Args:
            remote: Remote name (uses default if None)

        Returns:
            True if successful
        """
        try:
            cmd = ["dvc", "push"]
            if remote:
                cmd.extend(["-r", remote])

            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info("DVC push successful")
                return True
            else:
                logger.error(f"DVC push failed: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error pushing to remote: {e}")
            return False

    def pull(self, remote: Optional[str] = None) -> bool:
        """
        Pull DVC-tracked files from remote storage.

        Args:
            remote: Remote name (uses default if None)

        Returns:
            True if successful
        """
        try:
            cmd = ["dvc", "pull"]
            if remote:
                cmd.extend(["-r", remote])

            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info("DVC pull successful")
                return True
            else:
                logger.error(f"DVC pull failed: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error pulling from remote: {e}")
            return False

    def status(self, cloud: bool = False) -> Dict:
        """
        Get DVC status.

        Args:
            cloud: Check cloud status (requires remote)

        Returns:
            Dictionary with status information
        """
        try:
            cmd = ["dvc", "status"]
            if cloud:
                cmd.append("-c")

            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "has_changes": bool(result.stdout.strip())
            }

        except Exception as e:
            logger.error(f"Error getting status: {e}")
            return {"success": False, "error": str(e)}

    def list_tracked_files(self) -> List[Path]:
        """
        List all DVC-tracked files.

        Returns:
            List of paths to .dvc files
        """
        return list(self.project_root.rglob("*.dvc"))

    def get_file_info(self, filepath: Path) -> Optional[Dict]:
        """
        Get information about a DVC-tracked file.

        Args:
            filepath: Path to file

        Returns:
            Dictionary with file info or None
        """
        dvc_file = self.project_root / f"{filepath}.dvc"

        if not dvc_file.exists():
            return None

        try:
            with open(dvc_file, 'r') as f:
                info = json.load(f)
            return info
        except Exception as e:
            logger.error(f"Error reading .dvc file: {e}")
            return None

    def auto_track_large_files(
        self,
        directory: Path,
        size_threshold_mb: float = 10.0
    ) -> List[Path]:
        """
        Automatically track files above size threshold.

        Args:
            directory: Directory to scan
            size_threshold_mb: Size threshold in MB

        Returns:
            List of tracked files
        """
        threshold_bytes = int(size_threshold_mb * 1024 * 1024)
        tracked = []

        dir_path = self.project_root / directory

        if not dir_path.exists():
            logger.warning(f"Directory not found: {directory}")
            return tracked

        for file in dir_path.rglob("*"):
            if not file.is_file():
                continue

            # Skip already tracked files
            dvc_file = file.parent / f"{file.name}.dvc"
            if dvc_file.exists():
                continue

            # Check size
            if file.stat().st_size >= threshold_bytes:
                size_mb = file.stat().st_size / (1024 * 1024)
                logger.info(
                    f"Auto-tracking {file.relative_to(self.project_root)} "
                    f"({size_mb:.1f} MB)"
                )

                relative_path = file.relative_to(self.project_root)
                if self.track_file(relative_path):
                    tracked.append(relative_path)

        return tracked
