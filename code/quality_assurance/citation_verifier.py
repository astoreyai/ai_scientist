"""
Citation Verification System

Validates citations for accuracy, retraction status, and completeness.
"""

from pathlib import Path
from typing import List, Optional, Dict, Set, Tuple
import re
import requests
import time
import logging
from datetime import datetime, timedelta

from .base import BaseValidator, ValidationResult, ValidationStatus

logger = logging.getLogger(__name__)


class CitationVerifier(BaseValidator):
    """
    Verifies citations for validity, retractions, and completeness.

    Checks:
    - DOI validation
    - Retraction checking
    - BibTeX format validation
    - Citation completeness
    """

    def __init__(self, project_root: Path, config: Optional[Dict] = None):
        """
        Initialize citation verifier.

        Args:
            project_root: Project root directory
            config: Configuration dict with keys:
                - check_retractions: Check for retracted papers
                - validate_dois: Validate DOIs via Crossref
                - min_citation_count: Minimum expected citations
                - require_recent_papers: Require recent literature
                - recent_paper_threshold_years: Years threshold for "recent"
                - crossref_email: Email for Crossref API (polite pool)
        """
        super().__init__(project_root, config)

        cfg = config or {}
        self.check_retractions = cfg.get("check_retractions", True)
        self.validate_dois = cfg.get("validate_dois", True)
        self.min_citation_count = cfg.get("min_citation_count", 20)
        self.require_recent_papers = cfg.get("require_recent_papers", True)
        self.recent_threshold_years = cfg.get("recent_paper_threshold_years", 5)
        self.crossref_email = cfg.get("crossref_email", None)

        # Cache for API results (DOI -> result)
        self.doi_cache: Dict[str, Dict] = {}
        self.retraction_cache: Dict[str, bool] = {}

    def validate(self) -> List[ValidationResult]:
        """
        Run all citation validations.

        Returns:
            List of validation results
        """
        self.clear_results()

        # Find BibTeX files
        bib_files = self.find_files("**/*.bib")

        if not bib_files:
            self.warn_check(
                "BibTeX Files",
                "No BibTeX files found",
                category="citation"
            )
            return self.get_results()

        # Parse all BibTeX files
        all_entries = []
        for bib_file in bib_files:
            entries = self.parse_bibtex(bib_file)
            all_entries.extend(entries)

        if not all_entries:
            self.warn_check(
                "Citation Count",
                "No citations found in BibTeX files",
                category="citation"
            )
            return self.get_results()

        # Run validations
        self.validate_bibtex_format(all_entries)
        self.validate_citation_count(all_entries)

        if self.validate_dois:
            self.validate_dois_batch(all_entries)

        if self.check_retractions:
            self.check_retractions_batch(all_entries)

        if self.require_recent_papers:
            self.validate_recent_literature(all_entries)

        return self.get_results()

    # ============================================================================
    # BibTeX Parsing
    # ============================================================================

    def parse_bibtex(self, bib_file: Path) -> List[Dict]:
        """
        Parse BibTeX file into entries.

        Args:
            bib_file: Path to BibTeX file

        Returns:
            List of entry dictionaries
        """
        content = self.read_file(bib_file, relative=False)
        if not content:
            return []

        entries = []

        # Simple BibTeX parser
        # Pattern: @type{key, field = {value}, ...}
        entry_pattern = re.compile(
            r'@(\w+)\{([^,]+),\s*(.*?)\n\}',
            re.DOTALL | re.IGNORECASE
        )

        for match in entry_pattern.finditer(content):
            entry_type, key, fields_str = match.groups()

            entry = {
                "type": entry_type.lower(),
                "key": key.strip(),
                "file": str(bib_file.relative_to(self.project_root))
            }

            # Parse fields
            field_pattern = re.compile(r'(\w+)\s*=\s*\{([^}]*)\}')
            for field_match in field_pattern.finditer(fields_str):
                field_name, field_value = field_match.groups()
                entry[field_name.lower()] = field_value.strip()

            entries.append(entry)

        return entries

    # ============================================================================
    # BibTeX Format Validation
    # ============================================================================

    def validate_bibtex_format(self, entries: List[Dict]):
        """Validate BibTeX entries are complete."""
        check_name = "BibTeX Format Validation"
        category = "citation"

        if not entries:
            self.skip_check(
                check_name,
                "No BibTeX entries to validate",
                category=category
            )
            return

        # Required fields by entry type
        required_fields = {
            "article": ["author", "title", "journal", "year"],
            "inproceedings": ["author", "title", "booktitle", "year"],
            "book": ["author", "title", "publisher", "year"],
            "incollection": ["author", "title", "booktitle", "publisher", "year"],
            "phdthesis": ["author", "title", "school", "year"],
            "mastersthesis": ["author", "title", "school", "year"],
        }

        incomplete_entries = []

        for entry in entries:
            entry_type = entry.get("type", "").lower()
            required = required_fields.get(entry_type, ["author", "title", "year"])

            missing = [field for field in required if field not in entry or not entry[field]]

            if missing:
                incomplete_entries.append({
                    "key": entry["key"],
                    "type": entry_type,
                    "missing": missing
                })

        if not incomplete_entries:
            self.pass_check(
                check_name,
                f"All {len(entries)} BibTeX entries are complete",
                category=category,
                details={"total_entries": len(entries)}
            )
        else:
            self.warn_check(
                check_name,
                f"{len(incomplete_entries)} BibTeX entries are missing required fields",
                category=category,
                details={
                    "incomplete_count": len(incomplete_entries),
                    "examples": incomplete_entries[:5]
                }
            )

    def validate_citation_count(self, entries: List[Dict]):
        """Validate citation count is sufficient."""
        check_name = "Citation Count"
        category = "citation"

        count = len(entries)

        if count >= self.min_citation_count:
            self.pass_check(
                check_name,
                f"{count} citations found (minimum: {self.min_citation_count})",
                category=category,
                details={"count": count, "minimum": self.min_citation_count}
            )
        else:
            self.warn_check(
                check_name,
                f"Only {count} citations found (recommended minimum: {self.min_citation_count})",
                category=category,
                details={"count": count, "minimum": self.min_citation_count}
            )

    # ============================================================================
    # DOI Validation
    # ============================================================================

    def validate_dois_batch(self, entries: List[Dict]):
        """Validate DOIs using Crossref API."""
        check_name = "DOI Validation"
        category = "citation"

        # Extract DOIs
        dois = []
        for entry in entries:
            doi = entry.get("doi", "").strip()
            if doi:
                # Clean DOI (remove URL prefix if present)
                doi = doi.replace("https://doi.org/", "").replace("http://dx.doi.org/", "")
                dois.append((entry["key"], doi))

        if not dois:
            self.skip_check(
                check_name,
                "No DOIs found in citations",
                category=category
            )
            return

        # Validate DOIs
        valid_dois = []
        invalid_dois = []

        for key, doi in dois:
            # Check cache first
            if doi in self.doi_cache:
                if self.doi_cache[doi].get("valid", False):
                    valid_dois.append(doi)
                else:
                    invalid_dois.append((key, doi))
                continue

            # Query Crossref
            is_valid, metadata = self.check_doi_crossref(doi)

            # Cache result
            self.doi_cache[doi] = {"valid": is_valid, "metadata": metadata}

            if is_valid:
                valid_dois.append(doi)
            else:
                invalid_dois.append((key, doi))

            # Rate limiting
            time.sleep(0.05)  # 20 requests/second

        if not invalid_dois:
            self.pass_check(
                check_name,
                f"All {len(valid_dois)} DOIs are valid",
                category=category,
                details={"valid_count": len(valid_dois)}
            )
        else:
            self.warn_check(
                check_name,
                f"{len(invalid_dois)} invalid DOIs found",
                category=category,
                details={
                    "valid_count": len(valid_dois),
                    "invalid_count": len(invalid_dois),
                    "invalid_examples": [f"{k}: {d}" for k, d in invalid_dois[:5]]
                }
            )

    def check_doi_crossref(self, doi: str) -> Tuple[bool, Optional[Dict]]:
        """
        Check DOI validity using Crossref API.

        Args:
            doi: DOI to check

        Returns:
            (is_valid, metadata) tuple
        """
        try:
            url = f"https://api.crossref.org/works/{doi}"
            headers = {}

            if self.crossref_email:
                headers["User-Agent"] = f"ResearchAssistant/1.0 (mailto:{self.crossref_email})"

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                metadata = data.get("message", {})
                return True, metadata
            else:
                return False, None

        except Exception as e:
            logger.error(f"Error checking DOI {doi}: {e}")
            return False, None

    # ============================================================================
    # Retraction Checking
    # ============================================================================

    def check_retractions_batch(self, entries: List[Dict]):
        """Check for retracted papers using Crossref."""
        check_name = "Retraction Check"
        category = "citation"

        # Extract DOIs
        dois = []
        for entry in entries:
            doi = entry.get("doi", "").strip()
            if doi:
                doi = doi.replace("https://doi.org/", "").replace("http://dx.doi.org/", "")
                dois.append((entry["key"], doi))

        if not dois:
            self.skip_check(
                check_name,
                "No DOIs available for retraction checking",
                category=category
            )
            return

        retracted = []

        for key, doi in dois:
            # Check cache
            if doi in self.retraction_cache:
                if self.retraction_cache[doi]:
                    retracted.append((key, doi))
                continue

            # Check Crossref for retraction status
            is_retracted = self.check_retraction_crossref(doi)
            self.retraction_cache[doi] = is_retracted

            if is_retracted:
                retracted.append((key, doi))

            # Rate limiting
            time.sleep(0.05)

        if not retracted:
            self.pass_check(
                check_name,
                f"No retractions found in {len(dois)} citations with DOIs",
                category=category,
                details={"checked_count": len(dois)}
            )
        else:
            self.error_check(
                check_name,
                f"{len(retracted)} retracted paper(s) found",
                category=category,
                details={
                    "retracted_count": len(retracted),
                    "retracted": [f"{k}: {d}" for k, d in retracted]
                }
            )

    def check_retraction_crossref(self, doi: str) -> bool:
        """
        Check if paper is retracted using Crossref.

        Args:
            doi: DOI to check

        Returns:
            True if retracted
        """
        try:
            # First check if we have metadata cached
            if doi in self.doi_cache:
                metadata = self.doi_cache[doi].get("metadata", {})
            else:
                # Fetch metadata
                is_valid, metadata = self.check_doi_crossref(doi)
                if not is_valid or not metadata:
                    return False

            # Check for update-to field (retractions are updates)
            update_to = metadata.get("update-to", [])
            for update in update_to:
                if update.get("type") == "retraction":
                    return True

            # Check content-type
            content_type = metadata.get("type", "")
            if "retraction" in content_type.lower():
                return True

            return False

        except Exception as e:
            logger.error(f"Error checking retraction for {doi}: {e}")
            return False

    # ============================================================================
    # Recent Literature Validation
    # ============================================================================

    def validate_recent_literature(self, entries: List[Dict]):
        """Check that recent literature is cited."""
        check_name = "Recent Literature"
        category = "citation"

        current_year = datetime.now().year
        threshold_year = current_year - self.recent_threshold_years

        recent_papers = []
        old_papers = []
        no_year = []

        for entry in entries:
            year_str = entry.get("year", "").strip()

            if not year_str:
                no_year.append(entry["key"])
                continue

            try:
                year = int(year_str)
                if year >= threshold_year:
                    recent_papers.append((entry["key"], year))
                else:
                    old_papers.append((entry["key"], year))
            except ValueError:
                no_year.append(entry["key"])

        total = len(recent_papers) + len(old_papers)
        if total == 0:
            self.skip_check(
                check_name,
                "No papers with valid years found",
                category=category
            )
            return

        recent_percentage = (len(recent_papers) / total) * 100

        if recent_percentage >= 30:  # At least 30% recent
            self.pass_check(
                check_name,
                f"{len(recent_papers)} recent papers ({recent_percentage:.1f}%) from last {self.recent_threshold_years} years",
                category=category,
                details={
                    "recent_count": len(recent_papers),
                    "total_count": total,
                    "percentage": f"{recent_percentage:.1f}%",
                    "threshold_year": threshold_year
                }
            )
        else:
            self.warn_check(
                check_name,
                f"Only {len(recent_papers)} recent papers ({recent_percentage:.1f}%) from last {self.recent_threshold_years} years",
                category=category,
                details={
                    "recent_count": len(recent_papers),
                    "total_count": total,
                    "percentage": f"{recent_percentage:.1f}%",
                    "threshold_year": threshold_year,
                    "recommendation": "Include more papers from the last 5 years"
                }
            )
