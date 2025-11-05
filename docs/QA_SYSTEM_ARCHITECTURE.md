# Quality Assurance System Architecture

**Phase 7: Comprehensive Quality Assurance for Research**

## Overview

The QA system ensures research integrity, reproducibility, and rigor through automated validation checks at multiple levels.

## Architecture Principles

1. **Multi-Layer Validation**: Checks at commit, phase transition, and publication stages
2. **Non-Blocking by Default**: QA checks warn but don't block unless critical
3. **Configurable Rigor**: Adjust validation strictness based on research phase
4. **Automated Where Possible**: Minimize manual validation burden
5. **Audit Trail**: Track all QA checks and results

## System Components

```
┌─────────────────────────────────────────────────────────┐
│                   QA System Manager                      │
│  - Orchestrates all QA components                       │
│  - Aggregates validation results                        │
│  - Generates QA reports                                  │
└─────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────┴────────────────────┐
        ↓                   ↓                     ↓
┌──────────────┐   ┌──────────────┐    ┌──────────────┐
│Reproducibility│   │  Citation    │    │ Statistical  │
│  Validator   │   │  Verifier    │    │  Validator   │
└──────────────┘   └──────────────┘    └──────────────┘
        ↓                   ↓                     ↓
┌──────────────────────────────────────────────────────┐
│           Pre-commit Hooks Configuration              │
│  - Code quality checks                                │
│  - Automated QA on commit                             │
└──────────────────────────────────────────────────────┘
```

---

## 1. Reproducibility Validator

### Purpose
Ensure research can be reproduced by validating environment, dependencies, seeds, and data provenance.

### Checks

#### 1.1 Environment Validation
```python
class EnvironmentValidator:
    """Validates computational environment reproducibility."""

    def validate_python_version(self) -> ValidationResult:
        """Check Python version is documented."""

    def validate_dependencies(self) -> ValidationResult:
        """Check all dependencies are pinned with versions."""

    def validate_system_info(self) -> ValidationResult:
        """Check OS, hardware specs are documented."""
```

**Requirements:**
- Python version documented in requirements.txt or pyproject.toml
- All dependencies with pinned versions (no `>=` or `*`)
- System info captured (OS, CPU, GPU if used)

#### 1.2 Random Seed Validation
```python
class SeedValidator:
    """Validates random seed usage for reproducibility."""

    def check_seed_usage(self, code_files: List[Path]) -> ValidationResult:
        """Check that random seeds are set in code."""

    def check_seed_documentation(self) -> ValidationResult:
        """Check that seed values are documented."""
```

**Requirements:**
- Random seeds set for: numpy, random, torch, tensorflow
- Seed values documented in code and methods section
- Deterministic algorithms enabled where possible

#### 1.3 Data Provenance Validation
```python
class ProvenanceValidator:
    """Validates data provenance and lineage."""

    def validate_data_sources(self) -> ValidationResult:
        """Check all data sources are documented with URLs/DOIs."""

    def validate_data_versions(self) -> ValidationResult:
        """Check data versions/checksums are recorded."""

    def validate_preprocessing_steps(self) -> ValidationResult:
        """Check all preprocessing is documented and versioned."""
```

**Requirements:**
- All data sources documented with URLs or DOIs
- Data versions/hashes recorded (MD5, SHA256)
- Preprocessing steps documented in code and DVC pipeline
- Raw data preserved (never overwritten)

#### 1.4 Container Validation
```python
class ContainerValidator:
    """Validates containerization for reproducibility."""

    def check_dockerfile_exists(self) -> ValidationResult:
        """Check Dockerfile or container spec exists."""

    def validate_container_build(self) -> ValidationResult:
        """Check container builds successfully."""

    def validate_container_docs(self) -> ValidationResult:
        """Check container usage is documented."""
```

**Requirements:**
- Dockerfile or Singularity recipe present
- Container builds without errors
- Container usage documented in README

---

## 2. Citation Verification System

### Purpose
Ensure citations are valid, not retracted, and properly formatted.

### Checks

#### 2.1 DOI Validation
```python
class DOIValidator:
    """Validates DOIs using Crossref API."""

    def validate_doi(self, doi: str) -> ValidationResult:
        """Check DOI is valid and resolves."""

    def batch_validate_dois(self, dois: List[str]) -> List[ValidationResult]:
        """Validate multiple DOIs efficiently."""
```

**Requirements:**
- All DOIs resolve successfully
- DOI metadata matches citation details (authors, title, year)
- Rate limiting respected (Crossref: 50/second with backoff)

#### 2.2 Retraction Checking
```python
class RetractionChecker:
    """Checks for retracted papers using RetractionWatch."""

    def check_retraction(self, doi: str) -> ValidationResult:
        """Check if paper has been retracted."""

    def check_retraction_notice(self, doi: str) -> ValidationResult:
        """Check for expressions of concern or corrections."""
```

**Requirements:**
- Query RetractionWatch database or Crossref
- Flag retracted papers as critical errors
- Flag corrections/concerns as warnings
- Cache results to avoid repeated API calls

#### 2.3 Citation Format Validation
```python
class CitationFormatValidator:
    """Validates citation formatting."""

    def validate_bibtex(self, bib_file: Path) -> ValidationResult:
        """Check BibTeX file is valid and complete."""

    def validate_inline_citations(self, text: str) -> ValidationResult:
        """Check inline citations match bibliography."""
```

**Requirements:**
- BibTeX entries are valid and parseable
- All required fields present (author, title, year, journal/venue)
- Inline citations match bibliography entries
- No dangling references or missing citations

#### 2.4 Citation Completeness
```python
class CitationCompletenessChecker:
    """Checks citation completeness and coverage."""

    def check_key_papers_cited(self, field: str) -> ValidationResult:
        """Check highly-cited foundational papers are referenced."""

    def check_recent_literature(self) -> ValidationResult:
        """Check recent papers (last 2-5 years) are included."""
```

**Requirements:**
- Literature review includes papers from last 2-5 years
- Foundational/seminal papers in field are cited
- Citation count reasonable for field (e.g., 30-100 for empirical paper)

---

## 3. Statistical Validation System

### Purpose
Ensure statistical analyses are rigorous, properly reported, and interpretable.

### Checks

#### 3.1 Power Analysis Validation
```python
class PowerAnalysisValidator:
    """Validates statistical power analyses."""

    def validate_power_calculation(self, analysis: Dict) -> ValidationResult:
        """Check power analysis is present and appropriate."""

    def validate_sample_size_justification(self) -> ValidationResult:
        """Check sample size is justified with power analysis."""
```

**Requirements:**
- A priori power analysis conducted (before data collection)
- Target power ≥ 0.80 (80%)
- Effect size assumptions justified
- Sample size matches power analysis recommendation

#### 3.2 Effect Size Reporting
```python
class EffectSizeValidator:
    """Validates effect size reporting."""

    def check_effect_size_present(self, results: Dict) -> ValidationResult:
        """Check effect sizes are reported."""

    def validate_effect_size_interpretation(self) -> ValidationResult:
        """Check effect sizes are interpreted appropriately."""
```

**Requirements:**
- Effect sizes reported for all primary analyses
- Appropriate measures used (Cohen's d, η², r, odds ratio, etc.)
- Confidence intervals provided for effect sizes
- Effect sizes interpreted (small/medium/large using field standards)

#### 3.3 P-Value Interpretation
```python
class PValueValidator:
    """Validates p-value reporting and interpretation."""

    def check_p_value_reporting(self, results: Dict) -> ValidationResult:
        """Check p-values are reported appropriately."""

    def validate_significance_statements(self, text: str) -> ValidationResult:
        """Check significance statements are accurate."""
```

**Requirements:**
- Exact p-values reported (not just p < .05)
- Significance threshold pre-specified (α = 0.05 typical)
- No "marginally significant" or "trending" language
- P-values not interpreted as effect magnitude

#### 3.4 Multiple Comparison Corrections
```python
class MultipleComparisonValidator:
    """Validates corrections for multiple comparisons."""

    def detect_multiple_comparisons(self, analysis: Dict) -> ValidationResult:
        """Detect if multiple comparisons are present."""

    def validate_correction_method(self, method: str) -> ValidationResult:
        """Check appropriate correction method applied."""
```

**Requirements:**
- Multiple comparisons detected and corrected
- Correction method specified (Bonferroni, Holm, FDR, etc.)
- Adjusted p-values or alpha levels reported
- Family-wise error rate or FDR controlled

#### 3.5 Confidence Interval Validation
```python
class ConfidenceIntervalValidator:
    """Validates confidence interval reporting."""

    def check_ci_reported(self, results: Dict) -> ValidationResult:
        """Check confidence intervals are reported."""

    def validate_ci_width(self, ci: Tuple[float, float]) -> ValidationResult:
        """Check CI width is reasonable."""
```

**Requirements:**
- 95% CIs reported for all estimates
- CI level specified (90%, 95%, 99%)
- CIs interpreted appropriately
- Wide CIs flagged for insufficient power

#### 3.6 Assumption Checking
```python
class AssumptionValidator:
    """Validates statistical assumption checking."""

    def validate_normality_checks(self, test: str) -> ValidationResult:
        """Check normality assumptions tested."""

    def validate_homogeneity_checks(self, test: str) -> ValidationResult:
        """Check variance homogeneity tested."""
```

**Requirements:**
- Assumptions checked for parametric tests
- Diagnostic plots provided
- Violations addressed (transformations, non-parametric alternatives)
- Robustness checks conducted

---

## 4. Pre-commit Hooks Configuration

### Purpose
Automate QA checks at commit time to catch issues early.

### Hook Pipeline

```yaml
# .pre-commit-config.yaml

repos:
  # Code formatting
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  # Linting
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.14
    hooks:
      - id: ruff
        args: [--fix]

  # Type checking
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]

  # Security
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]

  # Testing
  - repo: local
    hooks:
      - id: pytest-check
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true

  # Research-specific QA
  - repo: local
    hooks:
      - id: reproducibility-check
        name: Reproducibility Validation
        entry: python -m code.quality_assurance.reproducibility_validator
        language: system
        pass_filenames: false

      - id: citation-check
        name: Citation Verification
        entry: python -m code.quality_assurance.citation_verifier
        language: system
        files: \.(bib|tex|md)$

      - id: statistical-check
        name: Statistical Validation
        entry: python -m code.quality_assurance.statistical_validator
        language: system
        files: \.(py|ipynb)$
```

### Hook Behavior

- **Non-blocking warnings**: Most QA checks warn but don't block commits
- **Critical errors**: Retracted citations, security issues block commits
- **Selective execution**: Only run relevant hooks based on changed files
- **Performance**: Hooks run in parallel where possible

---

## 5. QA Manager Integration

### Orchestration

```python
class QAManager:
    """
    Central manager for all QA components.

    Orchestrates validation across:
    - Reproducibility
    - Citations
    - Statistics
    - Pre-commit checks
    """

    def __init__(self, project_root: Path):
        self.reproducibility = ReproducibilityValidator(project_root)
        self.citations = CitationVerifier(project_root)
        self.statistics = StatisticalValidator(project_root)

    def run_full_qa(self) -> QAReport:
        """Run all QA checks and aggregate results."""

    def run_phase_qa(self, phase: str) -> QAReport:
        """Run phase-specific QA checks."""

    def generate_qa_report(self, results: List[ValidationResult]) -> QAReport:
        """Generate comprehensive QA report."""
```

### QA Report Structure

```python
@dataclass
class ValidationResult:
    """Result from a single validation check."""
    check_name: str
    status: str  # 'pass', 'warning', 'error'
    message: str
    details: Optional[Dict] = None
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class QAReport:
    """Comprehensive QA report."""
    timestamp: datetime
    project: str
    phase: Optional[str]

    # Results by category
    reproducibility_results: List[ValidationResult]
    citation_results: List[ValidationResult]
    statistical_results: List[ValidationResult]

    # Summary statistics
    total_checks: int
    passed: int
    warnings: int
    errors: int

    # Overall status
    status: str  # 'pass', 'warning', 'error'

    def to_markdown(self) -> str:
        """Export report as markdown."""

    def to_json(self) -> str:
        """Export report as JSON."""
```

---

## 6. Integration with Workflow System

### Phase Transition QA

QA checks are integrated into phase transitions:

```python
# In workflow orchestrator
def transition_to_phase(self, target_phase: Phase) -> bool:
    """Transition with QA validation."""

    # Run phase-specific QA
    qa_report = self.qa_manager.run_phase_qa(target_phase.name)

    # Check for blocking errors
    if qa_report.errors > 0:
        self.log_qa_failure(qa_report)
        return False

    # Warn about issues but allow transition
    if qa_report.warnings > 0:
        self.log_qa_warnings(qa_report)

    # Proceed with transition
    return True
```

### Phase-Specific QA Requirements

| Phase | Required QA Checks |
|-------|-------------------|
| Problem Formulation | Statistical planning (power analysis) |
| Literature Review | Citation verification, completeness |
| Experimental Design | Statistical validation, power analysis |
| Data Collection | Reproducibility (seeds, versions) |
| Analysis | Statistical validation, reproducibility |
| Writing | Citations, statistics, reproducibility |
| Publication | Full QA suite |

---

## 7. Configuration

### QA Configuration File

```yaml
# .qa_config.yaml

reproducibility:
  require_pinned_deps: true
  require_seed_docs: true
  require_docker: false  # Optional for computational studies
  check_data_provenance: true

citations:
  check_retractions: true
  validate_dois: true
  min_citation_count: 20
  require_recent_papers: true  # Last 5 years
  recent_paper_threshold_years: 5

statistics:
  require_power_analysis: true
  min_power: 0.80
  require_effect_sizes: true
  require_confidence_intervals: true
  check_multiple_comparisons: true
  require_assumption_checks: true

pre_commit:
  enable_formatting: true
  enable_linting: true
  enable_type_checking: false  # Optional, can be slow
  enable_testing: true
  enable_security: true

qa_manager:
  block_on_critical: true  # Block commits/transitions on critical errors
  report_format: markdown  # markdown, json, html
  report_dir: qa_reports/
```

---

## 8. Error Handling and Logging

### Validation Error Hierarchy

```python
class QAException(Exception):
    """Base exception for QA system."""

class CriticalQAError(QAException):
    """Critical QA error that blocks progress."""

class QAWarning(QAException):
    """Non-blocking QA warning."""

class ValidationTimeoutError(QAException):
    """Validation took too long."""
```

### Logging

```python
import logging

logger = logging.getLogger("qa_system")
logger.setLevel(logging.INFO)

# Log all QA checks
handler = logging.FileHandler("qa_checks.log")
handler.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)
logger.addHandler(handler)
```

---

## 9. Testing Strategy

### Unit Tests
- Test each validator independently
- Mock external API calls (DOI validation, retraction checks)
- Test validation logic thoroughly

### Integration Tests
- Test QA manager orchestration
- Test pre-commit hook execution
- Test phase transition QA integration

### End-to-End Tests
- Test full QA suite on sample project
- Test QA report generation
- Test error handling paths

---

## 10. Performance Considerations

### Optimization Strategies

1. **Caching**: Cache DOI validations, retraction checks for 24 hours
2. **Parallel Execution**: Run independent validators concurrently
3. **Incremental Checks**: Only validate changed files/citations
4. **Timeout Handling**: Set reasonable timeouts (30s per validator)
5. **Lazy Loading**: Load validators only when needed

### Performance Targets

- Full QA suite: < 2 minutes
- Pre-commit hooks: < 30 seconds
- Individual validators: < 10 seconds
- Citation verification: < 5 seconds per 100 citations

---

## 11. Future Extensions

### Planned Enhancements

1. **Data Quality Validation**: Check data distributions, outliers, missingness
2. **Code Quality Metrics**: Cyclomatic complexity, test coverage thresholds
3. **Notebook Validation**: Check Jupyter notebooks are reproducible
4. **Preprint/Publication Tracking**: Track paper versions, updates
5. **Peer Review Integration**: Track reviewer comments and responses

### Research-Specific Extensions

1. **Domain-Specific Validators**: Psychology (preregistration), Medicine (trial registration)
2. **Ethics Checkers**: IRB approval, consent forms, data sharing plans
3. **Reporting Checkers**: CONSORT, PRISMA, STROBE compliance
4. **Conflict of Interest**: Check for undeclared conflicts

---

## References

- PRISMA 2020: https://www.prisma-statement.org/
- CONSORT 2010: http://www.consort-statement.org/
- NIH Rigor and Reproducibility: https://grants.nih.gov/policy/reproducibility/
- Retraction Watch: http://retractionwatch.com/
- pre-commit framework: https://pre-commit.com/
- Crossref API: https://www.crossref.org/documentation/retrieve-metadata/rest-api/

---

**Architecture Version:** 1.0
**Last Updated:** 2025-01-05
**Status:** Design Complete, Implementation Pending
