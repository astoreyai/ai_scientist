"""
Git Workflow Manager

Research-specific git workflow patterns and utilities.
"""

from pathlib import Path
from typing import Optional, List
import subprocess
import logging

logger = logging.getLogger(__name__)


class GitWorkflowManager:
    """
    Manager for git workflows in research projects.

    Handles:
    - Branch management
    - Commit conventions
    - Version tagging
    - Research phase integration
    """

    def __init__(self, project_root: Path):
        """
        Initialize git workflow manager.

        Args:
            project_root: Project root directory
        """
        self.project_root = Path(project_root)

    def create_phase_branch(self, phase_name: str) -> bool:
        """
        Create branch for research phase.

        Args:
            phase_name: Phase name (e.g., "literature-review")

        Returns:
            True if successful
        """
        branch_name = f"phase/{phase_name}"

        try:
            result = subprocess.run(
                ["git", "checkout", "-b", branch_name],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info(f"Created branch: {branch_name}")
                return True
            else:
                logger.error(f"Failed to create branch: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error creating branch: {e}")
            return False

    def commit_with_convention(
        self,
        commit_type: str,
        scope: str,
        subject: str,
        body: Optional[str] = None,
        files: Optional[List[str]] = None
    ) -> bool:
        """
        Create commit following research convention.

        Args:
            commit_type: Type (feat, fix, data, docs, test, refactor)
            scope: Scope (analysis, collection, writing, etc.)
            subject: Short description
            body: Detailed description
            files: Files to stage (stages all if None)

        Returns:
            True if successful
        """
        try:
            # Stage files
            if files:
                for file in files:
                    subprocess.run(
                        ["git", "add", file],
                        cwd=self.project_root
                    )
            else:
                subprocess.run(
                    ["git", "add", "-A"],
                    cwd=self.project_root
                )

            # Build commit message
            message = f"{commit_type}({scope}): {subject}"
            if body:
                message += f"\n\n{body}"

            # Commit
            result = subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info(f"Created commit: {commit_type}({scope})")
                return True
            else:
                logger.error(f"Commit failed: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error committing: {e}")
            return False

    def tag_phase_completion(
        self,
        phase_name: str,
        version: str,
        message: Optional[str] = None
    ) -> bool:
        """
        Tag phase completion.

        Args:
            phase_name: Phase name
            version: Version (e.g., "1.0.0")
            message: Tag message

        Returns:
            True if successful
        """
        tag_name = f"v{version}-{phase_name}"
        tag_message = message or f"Phase complete: {phase_name}"

        try:
            result = subprocess.run(
                ["git", "tag", "-a", tag_name, "-m", tag_message],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info(f"Created tag: {tag_name}")
                return True
            else:
                logger.error(f"Tag failed: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Error tagging: {e}")
            return False

    def get_current_branch(self) -> Optional[str]:
        """Get current git branch"""
        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return result.stdout.strip()
            return None

        except Exception as e:
            logger.error(f"Error getting branch: {e}")
            return None

    def get_tags(self) -> List[str]:
        """Get all git tags"""
        try:
            result = subprocess.run(
                ["git", "tag", "-l"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return result.stdout.strip().split("\n")
            return []

        except Exception as e:
            logger.error(f"Error getting tags: {e}")
            return []

    def get_commit_history(self, max_count: int = 10) -> List[str]:
        """Get recent commit history"""
        try:
            result = subprocess.run(
                ["git", "log", f"--max-count={max_count}", "--oneline"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return result.stdout.strip().split("\n")
            return []

        except Exception as e:
            logger.error(f"Error getting history: {e}")
            return []
