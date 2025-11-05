"""
Reproducibility Validator

Validates research reproducibility through environment, seed, and provenance checks.
"""

from pathlib import Path
from typing import List, Optional, Dict, Set
import re
import sys
import logging

from .base import BaseValidator, ValidationResult, ValidationStatus

logger = logging.getLogger(__name__)


class ReproducibilityValidator(BaseValidator):
    """
    Validates reproducibility of research project.

    Checks:
    - Environment configuration
    - Random seed usage
    - Data provenance
    - Container specifications
    """

    def __init__(self, project_root: Path, config: Optional[Dict] = None):
        """
        Initialize reproducibility validator.

        Args:
            project_root: Project root directory
            config: Configuration dict with keys:
                - require_pinned_deps: Require pinned dependency versions
                - require_seed_docs: Require seed documentation
                - require_docker: Require Dockerfile
                - check_data_provenance: Check data source documentation
        """
        super().__init__(project_root, config)

        cfg = config or {}
        self.require_pinned_deps = cfg.get("require_pinned_deps", True)
        self.require_seed_docs = cfg.get("require_seed_docs", True)
        self.require_docker = cfg.get("require_docker", False)
        self.check_data_provenance = cfg.get("check_data_provenance", True)

    def validate(self) -> List[ValidationResult]:
        """
        Run all reproducibility validations.

        Returns:
            List of validation results
        """
        self.clear_results()

        # Environment validation
        self.validate_python_version()
        self.validate_dependencies()
        self.validate_system_info()

        # Random seed validation
        self.validate_seed_usage()
        self.validate_seed_documentation()

        # Data provenance
        if self.check_data_provenance:
            self.validate_data_sources()
            self.validate_data_versions()

        # Container validation
        if self.require_docker:
            self.validate_container_setup()

        return self.get_results()

    # ============================================================================
    # Environment Validation
    # ============================================================================

    def validate_python_version(self):
        """Check Python version is documented."""
        check_name = "Python Version Documentation"
        category = "reproducibility"

        # Check requirements.txt
        requirements = self.read_file("requirements.txt")
        pyproject = self.read_file("pyproject.toml")
        readme = self.read_file("README.md")

        python_version_pattern = re.compile(r"python[>=<~!]*\s*[0-9.]+", re.IGNORECASE)

        documented = False
        location = None

        if requirements and python_version_pattern.search(requirements):
            documented = True
            location = "requirements.txt"
        elif pyproject and python_version_pattern.search(pyproject):
            documented = True
            location = "pyproject.toml"
        elif readme and python_version_pattern.search(readme):
            documented = True
            location = "README.md"

        if documented:
            self.pass_check(
                check_name,
                f"Python version documented in {location}",
                category=category,
                details={"location": location, "current_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"}
            )
        else:
            self.warn_check(
                check_name,
                "Python version not documented in requirements.txt, pyproject.toml, or README.md",
                category=category,
                details={"current_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"}
            )

    def validate_dependencies(self):
        """Check all dependencies are pinned with versions."""
        check_name = "Dependency Pinning"
        category = "reproducibility"

        requirements_file = self.project_root / "requirements.txt"

        if not requirements_file.exists():
            self.warn_check(
                check_name,
                "requirements.txt not found",
                category=category
            )
            return

        requirements = requirements_file.read_text()
        lines = [line.strip() for line in requirements.split("\n") if line.strip() and not line.startswith("#")]

        unpinned = []
        pinned = []

        # Check for version specifiers
        for line in lines:
            # Skip git/url dependencies
            if line.startswith("git+") or line.startswith("http"):
                continue

            # Check for exact version pinning (==)
            if "==" in line:
                pinned.append(line)
            # Check for any version specifier
            elif any(op in line for op in [">=", "<=", ">", "<", "~=", "!="]):
                if self.require_pinned_deps:
                    unpinned.append(line)
                else:
                    pinned.append(line)
            else:
                unpinned.append(line)

        if not unpinned:
            self.pass_check(
                check_name,
                f"All {len(pinned)} dependencies have pinned versions",
                category=category,
                details={"pinned_count": len(pinned)}
            )
        elif self.require_pinned_deps:
            self.warn_check(
                check_name,
                f"{len(unpinned)} dependencies are not pinned with exact versions (==)",
                category=category,
                details={"unpinned": unpinned[:10], "total_unpinned": len(unpinned)}
            )
        else:
            self.pass_check(
                check_name,
                f"{len(pinned)} dependencies have version specifiers",
                category=category,
                details={"pinned_count": len(pinned), "unpinned_count": len(unpinned)}
            )

    def validate_system_info(self):
        """Check system info is documented."""
        check_name = "System Information Documentation"
        category = "reproducibility"

        readme = self.read_file("README.md")

        if not readme:
            self.skip_check(
                check_name,
                "README.md not found",
                category=category
            )
            return

        # Check for system-related keywords
        system_keywords = ["os", "operating system", "ubuntu", "linux", "macos", "windows", "cpu", "gpu", "hardware"]
        found_keywords = [kw for kw in system_keywords if kw.lower() in readme.lower()]

        if found_keywords:
            self.pass_check(
                check_name,
                f"System information documented in README.md",
                category=category,
                details={"keywords_found": found_keywords}
            )
        else:
            self.warn_check(
                check_name,
                "System information not documented in README.md",
                category=category,
                details={"suggestion": "Document OS, hardware specs for reproducibility"}
            )

    # ============================================================================
    # Random Seed Validation
    # ============================================================================

    def validate_seed_usage(self):
        """Check that random seeds are set in code."""
        check_name = "Random Seed Usage"
        category = "reproducibility"

        # Find Python files
        python_files = self.find_files("**/*.py")

        if not python_files:
            self.skip_check(
                check_name,
                "No Python files found",
                category=category
            )
            return

        # Patterns to detect seed setting
        seed_patterns = [
            re.compile(r"random\.seed\(", re.IGNORECASE),
            re.compile(r"np\.random\.seed\(", re.IGNORECASE),
            re.compile(r"numpy\.random\.seed\(", re.IGNORECASE),
            re.compile(r"torch\.manual_seed\(", re.IGNORECASE),
            re.compile(r"tf\.random\.set_seed\(", re.IGNORECASE),
            re.compile(r"tensorflow\.random\.set_seed\(", re.IGNORECASE),
        ]

        files_with_seeds: Set[Path] = set()

        for py_file in python_files:
            content = self.read_file(py_file, relative=False)
            if not content:
                continue

            for pattern in seed_patterns:
                if pattern.search(content):
                    files_with_seeds.add(py_file.relative_to(self.project_root))
                    break

        if files_with_seeds:
            self.pass_check(
                check_name,
                f"Random seeds set in {len(files_with_seeds)} file(s)",
                category=category,
                details={"files": [str(f) for f in sorted(files_with_seeds)]}
            )
        else:
            self.warn_check(
                check_name,
                "No random seed setting detected in Python files",
                category=category,
                details={"suggestion": "Set seeds for numpy, random, torch, tensorflow"}
            )

    def validate_seed_documentation(self):
        """Check that seed values are documented."""
        check_name = "Random Seed Documentation"
        category = "reproducibility"

        if not self.require_seed_docs:
            self.skip_check(
                check_name,
                "Seed documentation not required",
                category=category
            )
            return

        # Check README, docs, or comments for seed documentation
        readme = self.read_file("README.md")
        docs_files = self.find_files("docs/**/*.md")

        seed_pattern = re.compile(r"seed[s]?\s*[:=]\s*\d+", re.IGNORECASE)

        documented = False
        location = None

        if readme and seed_pattern.search(readme):
            documented = True
            location = "README.md"
        else:
            for doc_file in docs_files:
                content = self.read_file(doc_file, relative=False)
                if content and seed_pattern.search(content):
                    documented = True
                    location = str(doc_file.relative_to(self.project_root))
                    break

        if documented:
            self.pass_check(
                check_name,
                f"Random seed values documented in {location}",
                category=category,
                details={"location": location}
            )
        else:
            self.warn_check(
                check_name,
                "Random seed values not documented",
                category=category,
                details={"suggestion": "Document seed values used for experiments"}
            )

    # ============================================================================
    # Data Provenance Validation
    # ============================================================================

    def validate_data_sources(self):
        """Check all data sources are documented with URLs/DOIs."""
        check_name = "Data Source Documentation"
        category = "reproducibility"

        # Check for data documentation
        readme = self.read_file("README.md")
        data_readme = self.read_file("data/README.md")
        docs_files = self.find_files("docs/**/*.md")

        # Patterns for data source indicators
        url_pattern = re.compile(r"https?://[^\s]+")
        doi_pattern = re.compile(r"10\.\d{4,}/[^\s]+")
        data_keywords = ["dataset", "data source", "downloaded from", "obtained from"]

        documented = False
        locations = []

        for content, name in [
            (readme, "README.md"),
            (data_readme, "data/README.md"),
        ]:
            if not content:
                continue

            has_url = url_pattern.search(content)
            has_doi = doi_pattern.search(content)
            has_keywords = any(kw in content.lower() for kw in data_keywords)

            if (has_url or has_doi) and has_keywords:
                documented = True
                locations.append(name)

        # Check docs
        for doc_file in docs_files:
            content = self.read_file(doc_file, relative=False)
            if not content:
                continue

            has_url = url_pattern.search(content)
            has_doi = doi_pattern.search(content)
            has_keywords = any(kw in content.lower() for kw in data_keywords)

            if (has_url or has_doi) and has_keywords:
                documented = True
                locations.append(str(doc_file.relative_to(self.project_root)))

        if documented:
            self.pass_check(
                check_name,
                f"Data sources documented in {len(locations)} file(s)",
                category=category,
                details={"locations": locations}
            )
        else:
            self.warn_check(
                check_name,
                "Data sources not documented with URLs/DOIs",
                category=category,
                details={"suggestion": "Document data sources with URLs, DOIs, or access information"}
            )

    def validate_data_versions(self):
        """Check data versions/checksums are recorded."""
        check_name = "Data Version/Checksum Documentation"
        category = "reproducibility"

        # Check for DVC files (.dvc)
        dvc_files = self.find_files("**/*.dvc")

        # Check for checksum documentation
        readme = self.read_file("README.md")
        data_readme = self.read_file("data/README.md")

        # Patterns for checksums
        checksum_patterns = [
            re.compile(r"md5[:=]\s*[a-f0-9]{32}", re.IGNORECASE),
            re.compile(r"sha256[:=]\s*[a-f0-9]{64}", re.IGNORECASE),
        ]

        has_dvc = len(dvc_files) > 0
        has_checksum_docs = False

        for content in [readme, data_readme]:
            if not content:
                continue
            if any(pattern.search(content) for pattern in checksum_patterns):
                has_checksum_docs = True
                break

        if has_dvc:
            self.pass_check(
                check_name,
                f"Data versioning with DVC ({len(dvc_files)} tracked files)",
                category=category,
                details={"dvc_files": len(dvc_files)}
            )
        elif has_checksum_docs:
            self.pass_check(
                check_name,
                "Data checksums documented",
                category=category
            )
        else:
            self.warn_check(
                check_name,
                "Data versions/checksums not documented",
                category=category,
                details={"suggestion": "Use DVC or document data checksums (MD5, SHA256)"}
            )

    # ============================================================================
    # Container Validation
    # ============================================================================

    def validate_container_setup(self):
        """Check container setup for reproducibility."""
        check_name = "Container Configuration"
        category = "reproducibility"

        # Check for Dockerfile or Singularity recipe
        has_dockerfile = self.file_exists("Dockerfile")
        has_singularity = self.file_exists("Singularity") or self.file_exists("Singularity.def")
        has_docker_compose = self.file_exists("docker-compose.yml")

        if has_dockerfile or has_singularity:
            container_type = "Docker" if has_dockerfile else "Singularity"
            self.pass_check(
                check_name,
                f"{container_type} configuration found",
                category=category,
                details={
                    "dockerfile": has_dockerfile,
                    "singularity": has_singularity,
                    "docker_compose": has_docker_compose
                }
            )
        elif self.require_docker:
            self.warn_check(
                check_name,
                "No container configuration found (Dockerfile or Singularity)",
                category=category,
                details={"suggestion": "Create Dockerfile for reproducible environments"}
            )
        else:
            self.skip_check(
                check_name,
                "Container configuration not required",
                category=category
            )
