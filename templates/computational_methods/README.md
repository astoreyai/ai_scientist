# Computational Methods Template

**Purpose**: Algorithm development, ML/AI research, reproducible computational methods  
**Reporting Standard**: arXiv best practices, ACM/IEEE guidelines  
**Includes**: Benchmark evaluation, ablation studies, reproducibility framework

---

## Quick Start

```bash
cp -r templates/computational_methods my_algorithm
cd my_algorithm

# Run benchmarks
python experiments/run_benchmarks.py

# Ablation study
python experiments/ablation_study.py

# Generate paper figures
python experiments/visualize_results.py
```

---

## Structure

```
computational_methods/
├── src/
│   ├── algorithm/              # Your algorithm implementation
│   ├── baselines/              # Baseline methods for comparison
│   └── evaluation/             # Metrics and evaluation code
├── experiments/
│   ├── benchmark_datasets/     # Standard datasets
│   ├── run_benchmarks.py       # Systematic evaluation
│   ├── ablation_study.py       # Component analysis
│   └── parameter_tuning.py     # Hyperparameter search
├── docker/
│   └── Dockerfile              # Reproducible environment
└── docs/
    ├── algorithm_description.md
    └── reproducibility_checklist.md
```

---

## Key Features

- **Reproducibility**: Docker + pinned dependencies + seeds
- **Benchmarks**: Systematic comparison against baselines
- **Ablation Studies**: Component-wise analysis
- **Visualization**: Publication-ready figures
- **Statistical Tests**: Significance testing of improvements

---

*Template version: 1.2.0*
