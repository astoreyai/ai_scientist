"""
Artifact Manager

Manages research artifact archival and DOI generation via Zenodo.
"""

from pathlib import Path
from typing import Optional, Dict, List
import requests
import json
import logging
import shutil
import subprocess

logger = logging.getLogger(__name__)


class ArtifactManager:
    """
    Manager for research artifact archival and DOI generation.

    Handles:
    - Zenodo deposition
    - DOI generation
    - Reproducibility packages
    - Metadata management
    """

    def __init__(
        self,
        zenodo_token: Optional[str] = None,
        sandbox: bool = True
    ):
        """
        Initialize artifact manager.

        Args:
            zenodo_token: Zenodo API token
            sandbox: Use sandbox environment (for testing)
        """
        self.zenodo_token = zenodo_token
        self.sandbox = sandbox
        self.base_url = (
            "https://sandbox.zenodo.org/api" if sandbox
            else "https://zenodo.org/api"
        )

    def create_deposition(self) -> Optional[Dict]:
        """
        Create new Zenodo deposition.

        Returns:
            Deposition data or None if failed
        """
        if not self.zenodo_token:
            logger.error("Zenodo token not provided")
            return None

        try:
            response = requests.post(
                f"{self.base_url}/deposit/depositions",
                params={"access_token": self.zenodo_token},
                json={},
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()

            data = response.json()
            logger.info(f"Created deposition: {data['id']}")
            return data

        except Exception as e:
            logger.error(f"Failed to create deposition: {e}")
            return None

    def upload_file(
        self,
        deposition_id: int,
        filepath: Path
    ) -> bool:
        """
        Upload file to deposition.

        Args:
            deposition_id: Deposition ID
            filepath: Path to file

        Returns:
            True if successful
        """
        if not self.zenodo_token:
            logger.error("Zenodo token not provided")
            return False

        if not filepath.exists():
            logger.error(f"File not found: {filepath}")
            return False

        try:
            with open(filepath, 'rb') as f:
                response = requests.put(
                    f"{self.base_url}/deposit/depositions/{deposition_id}/files",
                    params={"access_token": self.zenodo_token},
                    data={"name": filepath.name},
                    files={"file": f}
                )
            response.raise_for_status()

            logger.info(f"Uploaded {filepath.name} to deposition {deposition_id}")
            return True

        except Exception as e:
            logger.error(f"Failed to upload file: {e}")
            return False

    def add_metadata(
        self,
        deposition_id: int,
        metadata: Dict
    ) -> bool:
        """
        Add metadata to deposition.

        Args:
            deposition_id: Deposition ID
            metadata: Metadata dictionary

        Returns:
            True if successful
        """
        if not self.zenodo_token:
            logger.error("Zenodo token not provided")
            return False

        try:
            response = requests.put(
                f"{self.base_url}/deposit/depositions/{deposition_id}",
                params={"access_token": self.zenodo_token},
                json={"metadata": metadata},
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()

            logger.info(f"Added metadata to deposition {deposition_id}")
            return True

        except Exception as e:
            logger.error(f"Failed to add metadata: {e}")
            return False

    def publish(self, deposition_id: int) -> Optional[Dict]:
        """
        Publish deposition (generates DOI).

        Args:
            deposition_id: Deposition ID

        Returns:
            Publication data with DOI or None if failed
        """
        if not self.zenodo_token:
            logger.error("Zenodo token not provided")
            return None

        try:
            response = requests.post(
                f"{self.base_url}/deposit/depositions/{deposition_id}/actions/publish",
                params={"access_token": self.zenodo_token}
            )
            response.raise_for_status()

            data = response.json()
            doi = data.get("doi")
            logger.info(f"Published deposition {deposition_id}, DOI: {doi}")
            return data

        except Exception as e:
            logger.error(f"Failed to publish deposition: {e}")
            return None

    def create_reproducibility_package(
        self,
        project_root: Path,
        output_dir: Path,
        include_data: bool = True
    ) -> Optional[Path]:
        """
        Create reproducibility package for archival.

        Args:
            project_root: Project root directory
            output_dir: Output directory for package
            include_data: Include data files (may be large)

        Returns:
            Path to created package or None if failed
        """
        try:
            # Create package directory
            pkg_dir = output_dir / "reproducibility_package"
            pkg_dir.mkdir(parents=True, exist_ok=True)

            # Copy code
            code_dir = project_root / "code"
            if code_dir.exists():
                shutil.copytree(code_dir, pkg_dir / "code", dirs_exist_ok=True)

            # Copy data (DVC files only if large)
            if include_data:
                data_dir = project_root / "data"
                if data_dir.exists():
                    shutil.copytree(
                        data_dir,
                        pkg_dir / "data",
                        dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("*.csv", "*.pkl") if not include_data else None
                    )

            # Copy results
            results_dir = project_root / "results"
            if results_dir.exists():
                shutil.copytree(results_dir, pkg_dir / "results", dirs_exist_ok=True)

            # Export environment
            try:
                with open(pkg_dir / "requirements.txt", 'w') as f:
                    subprocess.run(
                        ["pip", "freeze"],
                        stdout=f,
                        cwd=project_root
                    )
            except Exception as e:
                logger.warning(f"Could not export requirements: {e}")

            # Create README
            readme = self._generate_readme(project_root)
            (pkg_dir / "README.md").write_text(readme)

            # Create manifest
            manifest = self._generate_manifest(project_root)
            with open(pkg_dir / "MANIFEST.json", 'w') as f:
                json.dump(manifest, f, indent=2)

            # Create archive
            archive_path = shutil.make_archive(
                str(output_dir / "reproducibility_package"),
                'zip',
                pkg_dir
            )

            logger.info(f"Created reproducibility package: {archive_path}")
            return Path(archive_path)

        except Exception as e:
            logger.error(f"Failed to create reproducibility package: {e}")
            return None

    def _generate_readme(self, project_root: Path) -> str:
        """Generate README for reproducibility package"""
        return """# Reproducibility Package

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. If using DVC (large data files):
   ```bash
   dvc pull
   ```

3. Run analysis:
   ```bash
   python code/analysis/primary_analysis.py
   ```

## Contents

- `code/` - All analysis code
- `data/` - Data files (may be DVC tracked)
- `results/` - Pre-computed results
- `requirements.txt` - Exact package versions
- `MANIFEST.json` - Package metadata

## Citation

[Include paper citation and DOI once published]

## License

[Specify license]
"""

    def _generate_manifest(self, project_root: Path) -> Dict:
        """Generate manifest for reproducibility package"""
        return {
            "created": "2025-11-05",
            "package_version": "1.0.0",
            "study": "Research Study",
            "contents": {
                "code": True,
                "data": True,
                "results": True,
                "requirements": True
            },
            "reproducibility": {
                "environment": "Python 3.11+",
                "operating_system": "Linux/macOS/Windows",
                "estimated_runtime": "< 1 hour"
            }
        }

    def create_metadata_template(
        self,
        title: str,
        description: str,
        creators: List[Dict],
        upload_type: str = "dataset"
    ) -> Dict:
        """
        Create Zenodo metadata template.

        Args:
            title: Dataset/publication title
            description: Description
            creators: List of creator dicts with name, affiliation, orcid
            upload_type: Type (dataset, publication, software, etc.)

        Returns:
            Metadata dictionary
        """
        return {
            "title": title,
            "upload_type": upload_type,
            "description": description,
            "creators": creators,
            "access_right": "open",
            "license": "cc-by-4.0",
            "keywords": [],
            "related_identifiers": [],
            "version": "1.0.0",
            "language": "eng"
        }
