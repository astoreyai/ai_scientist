# Data Management & Versioning Architecture

**Version:** 1.0
**Date:** November 5, 2025
**Status:** Design Document

---

## Overview

The Data Management & Versioning system provides comprehensive tracking, versioning, and reproducibility for all research artifacts including data, code, experiments, and publications.

---

## Architecture Components

### 1. DVC (Data Version Control)
- Track large data files without storing in git
- Version datasets and models
- Remote storage support (S3, GCS, Azure)
- Reproducible pipelines

### 2. MLflow (Experiment Tracking)
- Log experiments and parameters
- Track metrics over time
- Model registry
- Artifact storage
- Experiment comparison

### 3. Git Workflow
- Research-specific branching strategies
- Version tagging conventions
- Commit message standards
- Integration with research phases

### 4. Artifact Management
- DOI generation via Zenodo/OSF
- Archival to permanent repositories
- Metadata management
- Reproducibility packages

---

## DVC Integration

### Directory Structure

```
project/
├── data/
│   ├── raw/              # DVC tracked
│   │   └── dataset.csv.dvc
│   ├── processed/        # DVC tracked
│   │   └── cleaned.csv.dvc
│   └── external/         # Third-party data
│
├── models/               # DVC tracked
│   └── model.pkl.dvc
│
├── results/              # DVC tracked
│   ├── figures/
│   └── tables/
│
└── .dvc/
    ├── config
    └── .gitignore
```

### DVC Configuration

```yaml
# .dvc/config
[core]
    remote = myremote
    autostage = true

['remote "myremote"']
    url = s3://my-bucket/dvc-storage

['remote "backup"']
    url = /mnt/backup/dvc-storage
```

### DVC Workflow

1. **Initialize DVC**
   ```bash
   dvc init
   dvc remote add -d myremote s3://bucket/path
   ```

2. **Track Data Files**
   ```bash
   dvc add data/raw/dataset.csv
   git add data/raw/dataset.csv.dvc .gitignore
   git commit -m "Track dataset with DVC"
   ```

3. **Push to Remote**
   ```bash
   dvc push
   ```

4. **Pull Data**
   ```bash
   dvc pull
   ```

5. **Create Pipeline**
   ```yaml
   # dvc.yaml
   stages:
     prepare:
       cmd: python code/prepare.py
       deps:
         - data/raw/dataset.csv
         - code/prepare.py
       outs:
         - data/processed/cleaned.csv

     train:
       cmd: python code/train.py
       deps:
         - data/processed/cleaned.csv
         - code/train.py
       outs:
         - models/model.pkl
       metrics:
         - results/metrics.json:
             cache: false
   ```

---

## MLflow Integration

### MLflow Setup

```python
# code/mlflow_config.py
import mlflow
from pathlib import Path

MLFLOW_TRACKING_URI = "file://./mlruns"
EXPERIMENT_NAME = "research_experiment"

def setup_mlflow():
    """Configure MLflow tracking"""
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)
```

### Experiment Logging Pattern

```python
import mlflow
import mlflow.sklearn
from mlflow_config import setup_mlflow

setup_mlflow()

# Start MLflow run
with mlflow.start_run(run_name="experiment_001"):

    # Log parameters
    mlflow.log_param("sample_size", 100)
    mlflow.log_param("alpha", 0.05)
    mlflow.log_param("random_seed", 42)

    # Log metrics
    mlflow.log_metric("effect_size", 0.65)
    mlflow.log_metric("power", 0.85)
    mlflow.log_metric("p_value", 0.003)

    # Log artifacts
    mlflow.log_artifact("results/figures/plot.png")
    mlflow.log_artifact("results/primary_results.json")

    # Log model (if applicable)
    # mlflow.sklearn.log_model(model, "model")

    # Log dataset info
    mlflow.log_dict({
        "dataset": "college_students_depression",
        "n_participants": 150,
        "collection_date": "2025-11-05"
    }, "dataset_info.json")
```

### MLflow Queries

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Get experiment
experiment = client.get_experiment_by_name("research_experiment")

# Search runs
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    filter_string="metrics.power >= 0.8",
    order_by=["metrics.effect_size DESC"]
)

for run in runs:
    print(f"Run ID: {run.info.run_id}")
    print(f"Effect size: {run.data.metrics['effect_size']}")
    print(f"P-value: {run.data.metrics['p_value']}")
```

---

## Git Workflow Patterns

### Branch Strategy for Research

```
main (protected)
  └── phase/literature-review
  └── phase/experimental-design
  └── phase/analysis
      └── feature/sensitivity-analysis
      └── feature/subgroup-analysis
  └── phase/writing
```

**Branch Naming Convention:**
- `phase/<phase-name>` - Main phase branches
- `feature/<feature-name>` - Specific features or analyses
- `fix/<issue-description>` - Bug fixes
- `docs/<topic>` - Documentation updates

### Commit Message Convention

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature or analysis
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `data`: Data updates
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

**Examples:**
```
feat(analysis): Add sensitivity analysis for outliers

Implemented sensitivity analysis removing top/bottom 5% of observations
to assess robustness of primary results.

- Created code/analysis/sensitivity.py
- Added results to results/sensitivity_analysis.json
- Effect size remains significant (d=0.58, p=0.005)

Refs: Phase 8 (Analysis)

---

data(collection): Add wave 2 participant data

Added follow-up data for 142 of original 150 participants.

- data/raw/wave2_responses.csv (tracked with DVC)
- 8 participants lost to follow-up (5.3% attrition)

DVC: dvc push required
```

### Version Tagging

**Pattern:** `v<major>.<minor>.<patch>-<phase>`

**Examples:**
- `v0.1.0-problem-formulation` - Problem formulation complete
- `v0.2.0-literature-review` - Literature review complete
- `v1.0.0-analysis-complete` - Analysis phase complete
- `v2.0.0-manuscript-submitted` - Manuscript submitted

**Creating Tags:**
```bash
git tag -a v1.0.0-analysis-complete -m "Analysis phase complete, all hypotheses tested"
git push origin v1.0.0-analysis-complete
```

---

## Artifact Management

### Zenodo Integration

```python
# code/artifact_management/zenodo_uploader.py
import requests
import json
from pathlib import Path

class ZenodoUploader:
    """Upload research artifacts to Zenodo for DOI generation"""

    def __init__(self, access_token: str, sandbox: bool = True):
        """
        Args:
            access_token: Zenodo API token
            sandbox: Use sandbox environment (testing)
        """
        self.access_token = access_token
        self.base_url = (
            "https://sandbox.zenodo.org/api" if sandbox
            else "https://zenodo.org/api"
        )

    def create_deposition(self, metadata: dict) -> dict:
        """Create new deposition (upload container)"""
        headers = {"Content-Type": "application/json"}
        params = {"access_token": self.access_token}

        response = requests.post(
            f"{self.base_url}/deposit/depositions",
            params=params,
            json={},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def upload_file(self, deposition_id: int, filepath: Path):
        """Upload file to deposition"""
        params = {"access_token": self.access_token}

        with open(filepath, 'rb') as f:
            response = requests.put(
                f"{self.base_url}/deposit/depositions/{deposition_id}/files",
                params=params,
                data={"name": filepath.name},
                files={"file": f}
            )
        response.raise_for_status()
        return response.json()

    def add_metadata(self, deposition_id: int, metadata: dict):
        """Add metadata to deposition"""
        headers = {"Content-Type": "application/json"}
        params = {"access_token": self.access_token}

        response = requests.put(
            f"{self.base_url}/deposit/depositions/{deposition_id}",
            params=params,
            json={"metadata": metadata},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def publish(self, deposition_id: int) -> dict:
        """Publish deposition (generates DOI)"""
        params = {"access_token": self.access_token}

        response = requests.post(
            f"{self.base_url}/deposit/depositions/{deposition_id}/actions/publish",
            params=params
        )
        response.raise_for_status()
        return response.json()
```

### Metadata Standards

```python
# Example metadata for data deposition
metadata = {
    "title": "Exercise Intervention Study - Raw Data",
    "upload_type": "dataset",
    "description": (
        "Raw data from RCT testing effect of 12-week exercise program "
        "on depression symptoms in college students. N=150 participants, "
        "randomized to exercise (n=75) or waitlist control (n=75)."
    ),
    "creators": [
        {
            "name": "Researcher, Jane",
            "affiliation": "University Name",
            "orcid": "0000-0001-2345-6789"
        }
    ],
    "access_right": "open",
    "license": "cc-by-4.0",
    "keywords": ["depression", "exercise", "RCT", "college students"],
    "related_identifiers": [
        {
            "identifier": "10.1234/preregistration",
            "relation": "isSupplementedBy",
            "scheme": "doi"
        }
    ],
    "version": "1.0.0",
    "language": "eng"
}
```

### Reproducibility Package

```python
# code/artifact_management/reproducibility_package.py
from pathlib import Path
import shutil
import subprocess
import json

def create_reproducibility_package(output_dir: Path):
    """
    Create complete reproducibility package for archival.

    Includes:
    - All code
    - Data (via DVC)
    - Environment specification
    - README with instructions
    - Results
    """

    # Create directory structure
    pkg_dir = output_dir / "reproducibility_package"
    pkg_dir.mkdir(parents=True, exist_ok=True)

    # Copy code
    shutil.copytree("code", pkg_dir / "code")

    # Copy DVC files
    shutil.copytree("data", pkg_dir / "data",
                    ignore=shutil.ignore_patterns("*.csv", "*.pkl"))

    # Export environment
    subprocess.run(
        ["pip", "freeze"],
        stdout=open(pkg_dir / "requirements.txt", 'w')
    )

    # Copy results
    shutil.copytree("results", pkg_dir / "results")

    # Create README
    readme = """# Reproducibility Package

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Pull data from DVC:
   ```bash
   dvc pull
   ```

3. Run analysis:
   ```bash
   python code/analysis/primary_analysis.py
   ```

## Contents

- `code/` - All analysis code
- `data/` - Data files (DVC tracked)
- `results/` - Pre-computed results
- `requirements.txt` - Exact package versions

## Citation

[Include paper citation and DOI]
"""

    (pkg_dir / "README.md").write_text(readme)

    # Create manifest
    manifest = {
        "created": "2025-11-05",
        "study": "Exercise and Depression RCT",
        "pre_registration": "https://osf.io/xxxxx",
        "data_doi": "10.5281/zenodo.xxxxx",
        "code_repository": "https://github.com/user/repo"
    }

    with open(pkg_dir / "MANIFEST.json", 'w') as f:
        json.dump(manifest, f, indent=2)

    # Create archive
    shutil.make_archive(
        str(output_dir / "reproducibility_package"),
        'zip',
        pkg_dir
    )

    return pkg_dir
```

---

## Integration with Research Workflow

### Phase-Specific Data Management

**Phase 7: Data Collection**
```python
# When data collection completes:
1. Add raw data to DVC tracking
2. Create initial MLflow run
3. Commit with data(collection) type
4. Tag version: v0.7.0-data-collected
```

**Phase 8: Analysis**
```python
# During analysis:
1. Log all experiments to MLflow
2. Track analysis scripts with git
3. Version intermediate results with DVC
4. Create analysis branch
5. Tag significant milestones
```

**Phase 11: Publication**
```python
# At publication:
1. Create reproducibility package
2. Upload to Zenodo (get DOI)
3. Publish MLflow experiment
4. Tag final version: v2.0.0-published
5. Archive complete project
```

---

## Automation Scripts

### Auto-DVC Tracking

```python
# code/data_management/auto_dvc.py
from pathlib import Path
import subprocess

def auto_track_large_files(directory: Path, size_threshold_mb: int = 10):
    """
    Automatically track large files with DVC.

    Args:
        directory: Directory to scan
        size_threshold_mb: File size threshold for DVC tracking
    """
    threshold_bytes = size_threshold_mb * 1024 * 1024

    for file in directory.rglob("*"):
        if not file.is_file():
            continue

        # Skip already tracked files
        if (file.parent / f"{file.name}.dvc").exists():
            continue

        # Check size
        if file.stat().st_size >= threshold_bytes:
            print(f"Tracking {file} with DVC ({file.stat().st_size / 1024 / 1024:.1f} MB)")
            subprocess.run(["dvc", "add", str(file)])
            subprocess.run(["git", "add", f"{file}.dvc", ".gitignore"])
```

### Auto-Experiment Logging

```python
# code/data_management/auto_mlflow.py
import mlflow
from functools import wraps

def track_experiment(experiment_name: str = None):
    """
    Decorator to automatically log function execution to MLflow.

    Usage:
        @track_experiment("my_analysis")
        def run_analysis(data, alpha=0.05):
            # Analysis code
            return results
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set experiment
            if experiment_name:
                mlflow.set_experiment(experiment_name)

            # Start run
            with mlflow.start_run(run_name=func.__name__):
                # Log parameters
                for key, value in kwargs.items():
                    mlflow.log_param(key, value)

                # Execute function
                result = func(*args, **kwargs)

                # Log result metrics if dict
                if isinstance(result, dict):
                    for key, value in result.items():
                        if isinstance(value, (int, float)):
                            mlflow.log_metric(key, value)

                return result

        return wrapper
    return decorator
```

---

## Best Practices

### Data Management
1. **Never commit raw data to git** - Use DVC for data >10MB
2. **Always version data transformations** - Track processing scripts
3. **Document data provenance** - Where data came from, how collected
4. **Validate data quality** - Check for missing values, outliers

### Experiment Tracking
1. **Log everything** - Parameters, metrics, artifacts
2. **Use meaningful run names** - Describe what the experiment tests
3. **Compare experiments** - Use MLflow UI for visualization
4. **Archive failed experiments** - Learn from what didn't work

### Version Control
1. **Commit frequently** - Small, logical commits
2. **Write clear messages** - Follow commit convention
3. **Tag milestones** - Mark phase completions
4. **Never force push to main** - Protect main branch

### Reproducibility
1. **Pin dependencies** - requirements.txt with exact versions
2. **Document random seeds** - All stochastic processes
3. **Test reproducibility** - Can someone else run your code?
4. **Share everything** - Code, data (if possible), results

---

## Monitoring & Alerts

### DVC Remote Status

```python
def check_dvc_status():
    """Check if all DVC-tracked files are pushed to remote"""
    result = subprocess.run(
        ["dvc", "status", "-c"],
        capture_output=True,
        text=True
    )

    if result.stdout.strip():
        print("⚠️ Warning: DVC files not pushed to remote")
        print(result.stdout)
        return False

    print("✅ All DVC files pushed to remote")
    return True
```

### MLflow Experiment Health

```python
def check_experiment_logging():
    """Verify recent experiments are being logged"""
    client = MlflowClient()
    experiments = client.list_experiments()

    for exp in experiments:
        runs = client.search_runs(exp.experiment_id, max_results=1)
        if runs:
            last_run = runs[0]
            print(f"Experiment: {exp.name}")
            print(f"  Last run: {last_run.info.start_time}")
            print(f"  Metrics logged: {len(last_run.data.metrics)}")
```

---

## Success Criteria

Phase 6 complete when:
- ✅ DVC initialized and configured with remote storage
- ✅ MLflow tracking operational with experiment logging
- ✅ Git workflow patterns documented and implemented
- ✅ Artifact management system (Zenodo integration) functional
- ✅ Automated tracking scripts operational
- ✅ All components tested
- ✅ Documentation complete
- ✅ Integration with research workflow phases
- ✅ Zero placeholders (R2)

---

**Architecture Status:** ✅ Design Complete
**Next Step:** Implementation
