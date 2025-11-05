"""
Unit Tests for Quality Assurance System
"""

import pytest
from pathlib import Path
import tempfile
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from quality_assurance.base import (
    ValidationResult, ValidationStatus, QAReport, BaseValidator
)
from quality_assurance.reproducibility_validator import ReproducibilityValidator
from quality_assurance.citation_verifier import CitationVerifier
from quality_assurance.statistical_validator import StatisticalValidator
from quality_assurance.qa_manager import QAManager, create_default_config
from workflow_context import WorkflowContext


class TestBase:
    """Test base validation framework."""

    def test_validation_result_creation(self):
        """Test creating validation result."""
        result = ValidationResult(
            check_name="Test Check",
            status=ValidationStatus.PASS,
            message="Test passed",
            category="test"
        )

        assert result.check_name == "Test Check"
        assert result.status == ValidationStatus.PASS
        assert result.is_passing()
        assert not result.is_error()

    def test_validation_result_to_dict(self):
        """Test converting result to dict."""
        result = ValidationResult(
            check_name="Test",
            status=ValidationStatus.WARNING,
            message="Warning message",
            details={"key": "value"}
        )

        d = result.to_dict()
        assert d["check_name"] == "Test"
        assert d["status"] == "warning"
        assert d["details"]["key"] == "value"

    def test_qa_report_creation(self):
        """Test creating QA report."""
        from datetime import datetime

        results = [
            ValidationResult("Check1", ValidationStatus.PASS, "Passed"),
            ValidationResult("Check2", ValidationStatus.WARNING, "Warning"),
            ValidationResult("Check3", ValidationStatus.ERROR, "Error"),
        ]

        report = QAReport(
            timestamp=datetime.now(),
            project="test_project",
            results=results
        )

        assert report.total_checks == 3
        assert report.passed == 1
        assert report.warnings == 1
        assert report.errors == 1
        assert report.status == ValidationStatus.ERROR  # Overall status

    def test_qa_report_markdown(self):
        """Test generating markdown report."""
        from datetime import datetime

        results = [
            ValidationResult("Check1", ValidationStatus.PASS, "Passed", category="test"),
        ]

        report = QAReport(
            timestamp=datetime.now(),
            project="test_project",
            results=results
        )

        markdown = report.to_markdown()
        assert "# QA Report: test_project" in markdown
        assert "Check1" in markdown
        assert "✅" in markdown

    def test_base_validator(self, tmp_path):
        """Test base validator functionality."""
        validator = BaseValidator(tmp_path)

        # Test file checking
        test_file = tmp_path / "test.txt"
        assert not validator.file_exists("test.txt")

        test_file.write_text("content")
        assert validator.file_exists("test.txt")

        # Test reading
        content = validator.read_file("test.txt")
        assert content == "content"

        # Test adding results
        validator.pass_check("Test", "Success", category="test")
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()


class TestReproducibilityValidator:
    """Test reproducibility validator."""

    def test_create_validator(self, tmp_path):
        """Test creating reproducibility validator."""
        validator = ReproducibilityValidator(tmp_path)
        assert validator.project_root == tmp_path

    def test_python_version_documentation(self, tmp_path):
        """Test Python version documentation check."""
        validator = ReproducibilityValidator(tmp_path)

        # No requirements file
        validator.validate_python_version()
        assert len(validator.results) == 1
        assert validator.results[0].is_warning()

        # With requirements
        validator.clear_results()
        (tmp_path / "requirements.txt").write_text("python>=3.11\nnumpy==1.24.0")
        validator.validate_python_version()
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()

    def test_dependency_pinning(self, tmp_path):
        """Test dependency pinning check."""
        validator = ReproducibilityValidator(tmp_path)

        # No requirements file
        validator.validate_dependencies()
        assert len(validator.results) == 1
        assert validator.results[0].is_warning()

        # With pinned dependencies
        validator.clear_results()
        (tmp_path / "requirements.txt").write_text("numpy==1.24.0\npandas==2.0.0")
        validator.validate_dependencies()
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()

        # With unpinned dependencies
        validator.clear_results()
        (tmp_path / "requirements.txt").write_text("numpy>=1.24.0\npandas")
        validator.validate_dependencies()
        assert len(validator.results) == 1
        assert validator.results[0].is_warning()

    def test_seed_usage(self, tmp_path):
        """Test random seed usage check."""
        validator = ReproducibilityValidator(tmp_path)

        # Create Python file with seed
        code_dir = tmp_path / "code"
        code_dir.mkdir()
        (code_dir / "analysis.py").write_text("""
import numpy as np
import random

random.seed(42)
np.random.seed(42)
""")

        validator.validate_seed_usage()
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()

    def test_data_provenance(self, tmp_path):
        """Test data source documentation check."""
        validator = ReproducibilityValidator(tmp_path)

        # No documentation
        validator.validate_data_sources()
        assert len(validator.results) == 1
        assert validator.results[0].is_warning()

        # With data documentation
        validator.clear_results()
        (tmp_path / "README.md").write_text("""
# Data

Dataset obtained from https://example.com/dataset
DOI: 10.1234/example
""")
        validator.validate_data_sources()
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()


class TestCitationVerifier:
    """Test citation verifier."""

    def test_create_verifier(self, tmp_path):
        """Test creating citation verifier."""
        verifier = CitationVerifier(tmp_path)
        assert verifier.project_root == tmp_path

    def test_bibtex_parsing(self, tmp_path):
        """Test BibTeX file parsing."""
        verifier = CitationVerifier(tmp_path)

        bib_file = tmp_path / "references.bib"
        bib_file.write_text("""
@article{smith2020,
  author = {Smith, John},
  title = {Test Article},
  journal = {Test Journal},
  year = {2020}
}

@inproceedings{jones2021,
  author = {Jones, Jane},
  title = {Conference Paper},
  booktitle = {Test Conference},
  year = {2021}
}
""")

        entries = verifier.parse_bibtex(bib_file)
        assert len(entries) == 2
        assert entries[0]["type"] == "article"
        assert entries[0]["author"] == "Smith, John"
        assert entries[1]["type"] == "inproceedings"

    def test_bibtex_format_validation(self, tmp_path):
        """Test BibTeX format validation."""
        verifier = CitationVerifier(tmp_path)

        # Complete entry
        entries = [
            {
                "type": "article",
                "key": "smith2020",
                "author": "Smith, John",
                "title": "Test",
                "journal": "Journal",
                "year": "2020"
            }
        ]

        verifier.validate_bibtex_format(entries)
        assert len(verifier.results) == 1
        assert verifier.results[0].is_passing()

        # Incomplete entry
        verifier.clear_results()
        incomplete_entries = [
            {
                "type": "article",
                "key": "incomplete",
                "author": "Author",
                "title": "Title"
                # Missing journal and year
            }
        ]

        verifier.validate_bibtex_format(incomplete_entries)
        assert len(verifier.results) == 1
        assert verifier.results[0].is_warning()

    def test_citation_count(self, tmp_path):
        """Test citation count validation."""
        verifier = CitationVerifier(tmp_path, config={"min_citation_count": 5})

        # Sufficient citations
        entries = [{"key": f"ref{i}"} for i in range(10)]
        verifier.validate_citation_count(entries)
        assert len(verifier.results) == 1
        assert verifier.results[0].is_passing()

        # Insufficient citations
        verifier.clear_results()
        entries = [{"key": f"ref{i}"} for i in range(3)]
        verifier.validate_citation_count(entries)
        assert len(verifier.results) == 1
        assert verifier.results[0].is_warning()

    def test_recent_literature(self, tmp_path):
        """Test recent literature validation."""
        from datetime import datetime

        current_year = datetime.now().year
        verifier = CitationVerifier(tmp_path)

        # Mix of recent and old papers
        entries = [
            {"key": "recent1", "year": str(current_year)},
            {"key": "recent2", "year": str(current_year - 1)},
            {"key": "old1", "year": "2000"},
            {"key": "old2", "year": "1990"},
        ]

        verifier.validate_recent_literature(entries)
        assert len(verifier.results) == 1
        # 2/4 = 50% recent, should pass (>= 30% threshold)
        assert verifier.results[0].is_passing()


class TestStatisticalValidator:
    """Test statistical validator."""

    def test_create_validator(self, tmp_path):
        """Test creating statistical validator."""
        validator = StatisticalValidator(tmp_path)
        assert validator.project_root == tmp_path

    def test_power_analysis_detection(self, tmp_path):
        """Test power analysis detection."""
        validator = StatisticalValidator(tmp_path)

        # Create file with power analysis
        code_dir = tmp_path / "code"
        code_dir.mkdir()
        (code_dir / "analysis.py").write_text("""
from statsmodels.stats.power import TTestPower

power_analysis = TTestPower()
sample_size = power_analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.80)
""")

        validator.validate_power_analysis([
            ("code/analysis.py", (code_dir / "analysis.py").read_text())
        ])

        assert len(validator.results) == 1
        assert validator.results[0].is_passing()

    def test_effect_size_detection(self, tmp_path):
        """Test effect size detection."""
        validator = StatisticalValidator(tmp_path)

        code = """
import numpy as np

# Calculate Cohen's d effect size
mean1, mean2 = 10.5, 12.3
sd_pooled = 2.1
effect_size = (mean2 - mean1) / sd_pooled  # Cohen's d
"""

        validator.validate_effect_sizes([("code/stats.py", code)])
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()

    def test_multiple_comparisons(self, tmp_path):
        """Test multiple comparisons detection."""
        validator = StatisticalValidator(tmp_path)

        # Code with multiple tests but no correction
        code_no_correction = """
from scipy.stats import ttest_ind

# Performing multiple tests across groups
pvalues = []
for group in groups:  # multiple test loop
    stat, pval = ttest_ind(group1, group2)
    pvalues.append(pval)
"""

        validator.validate_multiple_comparisons([("code/test.py", code_no_correction)])
        assert len(validator.results) == 1
        assert validator.results[0].is_warning()

        # Code with correction
        validator.clear_results()
        code_with_correction = """
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

pvalues = []
for group in groups:
    stat, pval = ttest_ind(group1, group2)
    pvalues.append(pval)

reject, pvals_corrected, _, _ = multipletests(pvalues, method='bonferroni')
"""

        validator.validate_multiple_comparisons([("code/test.py", code_with_correction)])
        assert len(validator.results) == 1
        assert validator.results[0].is_passing()


class TestQAManager:
    """Test QA manager."""

    def test_create_manager(self, tmp_path):
        """Test creating QA manager."""
        manager = QAManager(tmp_path)
        assert manager.project_root == tmp_path
        assert manager.reproducibility is not None
        assert manager.citations is not None
        assert manager.statistics is not None

    def test_config_loading(self, tmp_path):
        """Test loading configuration."""
        config_file = tmp_path / ".qa_config.yaml"
        create_default_config(config_file)
        assert config_file.exists()

        manager = QAManager(tmp_path, config_file)
        assert "reproducibility" in manager.config
        assert "citations" in manager.config
        assert "statistics" in manager.config

    def test_run_full_qa(self, tmp_path):
        """Test running full QA suite."""
        # Create minimal project structure
        (tmp_path / "requirements.txt").write_text("numpy==1.24.0")
        (tmp_path / "README.md").write_text("# Test Project")

        manager = QAManager(tmp_path)
        report = manager.run_full_qa()

        assert report.total_checks > 0
        assert report.project == tmp_path.name

    def test_phase_qa(self, tmp_path):
        """Test phase-specific QA."""
        (tmp_path / "requirements.txt").write_text("numpy==1.24.0")

        manager = QAManager(tmp_path)

        # Test data collection phase (reproducibility only)
        report = manager.run_phase_qa("data_collection")
        assert report.phase == "data_collection"

        # Check only reproducibility checks ran
        categories = set(r.category for r in report.results)
        assert "reproducibility" in categories

    def test_generate_report(self, tmp_path):
        """Test report generation and saving."""
        from datetime import datetime

        manager = QAManager(tmp_path)

        # Create simple report
        report = QAReport(
            timestamp=datetime.now(),
            project="test",
            results=[
                ValidationResult("Test", ValidationStatus.PASS, "OK", category="test")
            ]
        )

        # Save report
        output_path = manager.generate_and_save_report(report)
        assert output_path.exists()
        assert output_path.suffix == ".md"

        # Check content
        content = output_path.read_text()
        assert "# QA Report" in content
        assert "Test" in content

    def test_get_summary(self, tmp_path):
        """Test getting report summary."""
        from datetime import datetime

        manager = QAManager(tmp_path)

        report = QAReport(
            timestamp=datetime.now(),
            project="test",
            results=[
                ValidationResult("Check1", ValidationStatus.PASS, "OK"),
                ValidationResult("Check2", ValidationStatus.WARNING, "Warning"),
            ]
        )

        summary = manager.get_summary(report)
        assert summary["total_checks"] == 2
        assert summary["passed"] == 1
        assert summary["warnings"] == 1
        assert summary["errors"] == 0


class TestCitationVerifierExtended:
    """Extended citation verifier tests for comprehensive coverage"""

    def test_validate_dois_batch_success(self, tmp_path, monkeypatch):
        """Test DOI validation with mocked Crossref API"""
        from unittest.mock import Mock

        verifier = CitationVerifier(tmp_path, {"validate_dois": True})

        # Create test BibTeX file with DOIs
        (tmp_path / "bibliography").mkdir()
        bib_file = tmp_path / "bibliography" / "refs.bib"
        bib_file.write_text("""
@article{smith2020,
  author = {Smith, John},
  title = {Test Article},
  journal = {Nature},
  year = {2020},
  doi = {10.1234/test123}
}

@article{jones2021,
  author = {Jones, Jane},
  title = {Another Article},
  journal = {Science},
  year = {2021},
  doi = {10.5678/test456}
}
""")

        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": {
                "DOI": "10.1234/test123",
                "title": ["Test Article"],
                "author": [{"given": "John", "family": "Smith"}]
            }
        }

        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)

        # Run validation
        results = verifier.validate()

        # Should have validation results
        assert len(results) > 0

        # Check that API was called
        assert mock_get.called

    def test_check_doi_crossref_valid(self, tmp_path, monkeypatch):
        """Test checking valid DOI via Crossref"""
        from unittest.mock import Mock

        verifier = CitationVerifier(tmp_path)

        # Mock successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": {"DOI": "10.1234/test", "title": ["Test"]}
        }

        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)

        is_valid, metadata = verifier.check_doi_crossref("10.1234/test")

        assert is_valid is True
        assert metadata is not None
        assert "DOI" in metadata

    def test_check_doi_crossref_invalid(self, tmp_path, monkeypatch):
        """Test checking invalid DOI"""
        from unittest.mock import Mock

        verifier = CitationVerifier(tmp_path)

        # Mock 404 response
        mock_response = Mock()
        mock_response.status_code = 404

        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)

        is_valid, metadata = verifier.check_doi_crossref("10.invalid/doi")

        assert is_valid is False
        assert metadata is None

    def test_check_doi_crossref_with_email(self, tmp_path, monkeypatch):
        """Test DOI check with polite pool email"""
        from unittest.mock import Mock

        verifier = CitationVerifier(
            tmp_path,
            {"crossref_email": "researcher@university.edu"}
        )

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": {}}

        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)

        verifier.check_doi_crossref("10.1234/test")

        # Verify email was included in headers
        call_kwargs = mock_get.call_args[1]
        assert "headers" in call_kwargs
        assert "User-Agent" in call_kwargs["headers"]

    def test_check_retractions_batch_no_retractions(self, tmp_path, monkeypatch):
        """Test retraction checking with no retractions found"""
        from unittest.mock import Mock

        verifier = CitationVerifier(tmp_path, {"check_retractions": True})

        # Create BibTeX with DOIs
        (tmp_path / "refs.bib").write_text("""
@article{test2020,
  author = {Test},
  title = {Valid Article},
  journal = {Journal},
  year = {2020},
  doi = {10.1234/valid}
}
""")

        # Mock API response (no retraction)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": {"update-to": [], "type": "journal-article"}
        }

        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)

        results = verifier.validate()

        # Should pass retraction check
        retraction_results = [r for r in results if "Retraction" in r.check_name]
        assert len(retraction_results) > 0
        assert retraction_results[0].is_passing()

    def test_check_retractions_batch_retracted_found(self, tmp_path, monkeypatch):
        """Test retraction checking with retracted paper"""
        from unittest.mock import Mock

        verifier = CitationVerifier(tmp_path, {"check_retractions": True})

        # Create BibTeX with DOI
        (tmp_path / "refs.bib").write_text("""
@article{retracted2020,
  author = {Retracted},
  title = {Bad Article},
  journal = {Journal},
  year = {2020},
  doi = {10.1234/retracted}
}
""")

        # Mock API response indicating retraction
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": {
                "update-to": [{"type": "retraction", "DOI": "10.1234/retraction-notice"}],
                "type": "journal-article"
            }
        }

        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)

        results = verifier.validate()

        # Should fail retraction check
        retraction_results = [r for r in results if "Retraction" in r.check_name]
        assert len(retraction_results) > 0
        assert retraction_results[0].is_error()

    def test_check_retraction_crossref_cache(self, tmp_path):
        """Test retraction checking with cached metadata"""
        verifier = CitationVerifier(tmp_path)

        # Pre-populate cache with non-retracted paper
        verifier.doi_cache["10.1234/cached"] = {
            "valid": True,
            "metadata": {"update-to": [], "type": "journal-article"}
        }

        is_retracted = verifier.check_retraction_crossref("10.1234/cached")

        assert is_retracted is False

    def test_validate_recent_literature_passing(self, tmp_path):
        """Test recent literature validation passing"""
        from datetime import datetime

        current_year = datetime.now().year

        verifier = CitationVerifier(tmp_path, {"require_recent_papers": True})

        # Create BibTeX with recent papers
        (tmp_path / "refs.bib").write_text(f"""
@article{{recent1,
  author = {{Author1}},
  title = {{Recent Paper 1}},
  journal = {{Journal}},
  year = {{{current_year}}}
}}

@article{{recent2,
  author = {{Author2}},
  title = {{Recent Paper 2}},
  journal = {{Journal}},
  year = {{{current_year - 1}}}
}}

@article{{old1,
  author = {{Author3}},
  title = {{Old Paper}},
  journal = {{Journal}},
  year = {{2000}}
}}
""")

        results = verifier.validate()

        # Should pass with 66% recent papers (2/3)
        recent_results = [r for r in results if "Recent Literature" in r.check_name]
        assert len(recent_results) > 0
        assert recent_results[0].is_passing()

    def test_doi_cache_usage(self, tmp_path, monkeypatch):
        """Test that DOI cache is used to avoid redundant API calls"""
        from unittest.mock import Mock

        verifier = CitationVerifier(tmp_path)

        # Pre-populate cache
        verifier.doi_cache["10.1234/cached"] = {
            "valid": True,
            "metadata": {"title": "Cached Article"}
        }

        # Create entries with same DOI twice
        entries = [
            {"key": "ref1", "doi": "10.1234/cached"},
            {"key": "ref2", "doi": "10.1234/cached"}
        ]

        # Mock API (should not be called due to cache)
        mock_get = Mock()
        monkeypatch.setattr("requests.get", mock_get)

        verifier.validate_dois_batch(entries)

        # API should not have been called
        assert not mock_get.called


class TestStatisticalValidatorExtended:
    """Extended statistical validator tests for comprehensive coverage"""

    def test_extract_notebook_code(self, tmp_path):
        """Test extracting code from Jupyter notebook"""
        import json

        validator = StatisticalValidator(tmp_path)

        # Create a test notebook
        notebook = {
            "cells": [
                {
                    "cell_type": "code",
                    "source": ["import numpy as np\n", "import pandas as pd"]
                },
                {
                    "cell_type": "markdown",
                    "source": ["# This is markdown"]
                },
                {
                    "cell_type": "code",
                    "source": ["data = pd.read_csv('data.csv')"]
                }
            ]
        }

        nb_file = tmp_path / "analysis.ipynb"
        nb_file.write_text(json.dumps(notebook))

        code = validator.extract_notebook_code(nb_file)

        assert code is not None
        assert "import numpy" in code
        assert "import pandas" in code
        assert "read_csv" in code
        assert "# This is markdown" not in code

    def test_extract_notebook_code_with_string_source(self, tmp_path):
        """Test extracting code when source is string not list"""
        import json

        validator = StatisticalValidator(tmp_path)

        notebook = {
            "cells": [
                {
                    "cell_type": "code",
                    "source": "import scipy.stats"
                }
            ]
        }

        nb_file = tmp_path / "stats.ipynb"
        nb_file.write_text(json.dumps(notebook))

        code = validator.extract_notebook_code(nb_file)

        assert code is not None
        assert "scipy.stats" in code

    def test_validate_with_notebooks(self, tmp_path):
        """Test validation including notebook files"""
        import json

        validator = StatisticalValidator(tmp_path)

        # Create notebook with power analysis
        notebook = {
            "cells": [
                {
                    "cell_type": "code",
                    "source": [
                        "from statsmodels.stats.power import TTestPower\n",
                        "power_analysis = TTestPower()\n",
                        "sample_size = power_analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.80)"
                    ]
                }
            ]
        }

        nb_file = tmp_path / "power.ipynb"
        nb_file.write_text(json.dumps(notebook))

        results = validator.validate()

        # Should find power analysis
        power_results = [r for r in results if "Power Analysis" in r.check_name]
        assert len(power_results) > 0

    def test_validate_p_values_with_problematic_language(self, tmp_path):
        """Test detection of problematic p-value language"""
        validator = StatisticalValidator(tmp_path)

        # Create Python file with problematic language
        code_dir = tmp_path / "analysis"
        code_dir.mkdir()
        (code_dir / "results.py").write_text("""
# Statistical analysis results
# The effect was marginally significant (p = 0.07)
# Another finding approached significance (p = 0.06)
""")

        results = validator.validate()

        # Should warn about problematic language
        pval_results = [r for r in results if "P-Value" in r.check_name]
        assert len(pval_results) > 0

    def test_validate_confidence_intervals_present(self, tmp_path):
        """Test validation when CIs are present"""
        validator = StatisticalValidator(tmp_path, {"require_confidence_intervals": True})

        # Create file with CI calculation
        code_dir = tmp_path / "stats"
        code_dir.mkdir()
        (code_dir / "inference.py").write_text("""
import scipy.stats as stats

# Calculate 95% confidence interval
mean = 100
se = 5
ci = stats.t.interval(0.95, df=29, loc=mean, scale=se)
conf_int = model.conf_int(alpha=0.05)
""")

        results = validator.validate()

        # Should pass CI check
        ci_results = [r for r in results if "Confidence Interval" in r.check_name]
        assert len(ci_results) > 0
        assert ci_results[0].is_passing()

    def test_validate_multiple_comparisons_with_correction(self, tmp_path):
        """Test multiple comparisons with correction detected"""
        validator = StatisticalValidator(tmp_path)

        # Create file with multiple tests and correction
        code_dir = tmp_path / "analysis"
        code_dir.mkdir()
        (code_dir / "compare.py").write_text("""
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

pvalues = []
for group in groups:
    stat, pval = ttest_ind(group_a, group_b)
    pvalues.append(pval)

# Apply Bonferroni correction
reject, pvals_corrected, _, _ = multipletests(pvalues, method='bonferroni')
""")

        results = validator.validate()

        # Should pass multiple comparisons check
        mc_results = [r for r in results if "Multiple Comparison" in r.check_name]
        assert len(mc_results) > 0
        assert mc_results[0].is_passing()

    def test_validate_multiple_comparisons_without_correction(self, tmp_path):
        """Test multiple comparisons without correction"""
        validator = StatisticalValidator(tmp_path)

        # Create file with multiple tests but no correction
        code_dir = tmp_path / "analysis"
        code_dir.mkdir()
        (code_dir / "uncorrected.py").write_text("""
from scipy.stats import ttest_ind

# Multiple tests without correction
for condition in conditions:
    stat, pval = ttest_ind(control, condition)
    print(f"p-value: {pval}")
""")

        results = validator.validate()

        # Should warn about missing correction
        mc_results = [r for r in results if "Multiple Comparison" in r.check_name]
        assert len(mc_results) > 0
        assert mc_results[0].is_warning()

    def test_validate_assumptions_with_tests(self, tmp_path):
        """Test assumption validation when tests present"""
        validator = StatisticalValidator(tmp_path)

        # Create file with parametric test and assumption checks
        code_dir = tmp_path / "stats"
        code_dir.mkdir()
        (code_dir / "ttest.py").write_text("""
from scipy.stats import ttest_ind, shapiro, levene

# Check normality assumption
stat_norm, p_norm = shapiro(data)

# Check homogeneity of variance
stat_lev, p_lev = levene(group1, group2)

# If assumptions met, run t-test
stat, pval = ttest_ind(group1, group2)
""")

        results = validator.validate()

        # Should pass assumption check
        assumption_results = [r for r in results if "Assumption" in r.check_name]
        assert len(assumption_results) > 0
        assert assumption_results[0].is_passing()

    def test_validate_assumptions_without_tests(self, tmp_path):
        """Test assumption validation when tests missing"""
        validator = StatisticalValidator(tmp_path)

        # Create file with parametric test but no assumption checks
        code_dir = tmp_path / "stats"
        code_dir.mkdir()
        (code_dir / "anova.py").write_text("""
from scipy.stats import f_oneway

# Run ANOVA without checking assumptions
stat, pval = f_oneway(group1, group2, group3)
""")

        results = validator.validate()

        # Should warn about missing assumption checks
        assumption_results = [r for r in results if "Assumption" in r.check_name]
        assert len(assumption_results) > 0
        assert assumption_results[0].is_warning()

    def test_validate_empty_project(self, tmp_path):
        """Test validation on empty project"""
        validator = StatisticalValidator(tmp_path)

        results = validator.validate()

        # Should skip the statistical analysis check
        assert len(results) > 0
        # Check that at least one result has "No Python files" message
        skip_results = [r for r in results if "Statistical Analysis" in r.check_name]
        assert len(skip_results) > 0


class TestReproducibilityValidatorExtended:
    """Extended reproducibility validator tests"""

    def test_create_with_config(self, tmp_path):
        """Test creating validator with configuration"""
        validator = ReproducibilityValidator(tmp_path, {"require_docker": True})
        assert validator.project_root == tmp_path

    def test_validate_structure(self, tmp_path):
        """Test basic structure validation"""
        validator = ReproducibilityValidator(tmp_path)
        assert hasattr(validator, 'project_root')


class TestQAManagerExtended:
    """Extended QA manager tests"""

    def test_create_basic(self, tmp_path):
        """Test creating manager"""
        manager = QAManager(project_root=tmp_path)
        assert manager is not None

    def test_validate_structure(self, tmp_path):
        """Test basic structure validation"""
        manager = QAManager(project_root=tmp_path)
        assert hasattr(manager, 'project_root')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
