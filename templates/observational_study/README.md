# Observational Study Template

**Purpose**: STROBE-compliant cohort, case-control, and cross-sectional studies  
**Reporting Standard**: STROBE (Strengthening the Reporting of Observational Studies in Epidemiology)  
**Includes**: Study design, variable definitions, DAGs, analysis pipeline

---

## Quick Start

1. **Copy template**:
   ```bash
   cp -r templates/observational_study my_study
   cd my_study
   ```

2. **Choose study design**:
   ```bash
   python code/design_selector.py
   # Interactive tool guides you through:
   # - Cohort study (follow people forward in time)
   # - Case-control study (start with outcome, look back)
   # - Cross-sectional study (single time point)
   ```

3. **Define variables**:
   ```bash
   # Edit docs/variable_definitions.yaml
   exposure: "Smoking status"
   outcome: "Lung cancer incidence"
   confounders: ["Age", "Sex", "Socioeconomic status"]
   effect_modifiers: ["Genetic variants"]
   ```

4. **Create DAG** (Directed Acyclic Graph):
   ```bash
   python code/dag_builder.py
   # Visual tool for mapping causal relationships
   # Identifies confounders and mediators
   ```

5. **Develop analysis plan**:
   ```bash
   python code/statistical_plan_builder.py
   # Pre-specifies all analyses before seeing data
   ```

6. **Analyze data**:
   ```bash
   python code/run_analysis.py
   ```

---

## Directory Structure

```
observational_study/
├── README.md
├── docs/
│   ├── study_design.md              # Cohort/case-control/cross-sectional
│   ├── variable_definitions.yaml    # Complete variable codebook
│   ├── dag.png                      # Directed acyclic graph
│   ├── statistical_plan.md          # Pre-specified analysis plan
│   ├── confounding_analysis.md      # Confounding assessment strategy
│   └── strobe_checklist.md          # 22-item compliance tracker
│
├── code/
│   ├── design_selector.py           # Interactive design chooser
│   ├── dag_builder.py               # DAG visualization tool
│   ├── statistical_plan_builder.py  # Analysis plan generator
│   ├── variable_creation.py         # Derive variables from raw data
│   ├── descriptive_stats.py         # Table 1 generator
│   ├── regression_analysis.py       # Main analysis (logistic/Cox/linear)
│   ├── confounding_analysis.py      # Change-in-estimate method
│   ├── sensitivity_analysis.py      # Robustness checks
│   └── strobe_validator.py          # Check 22-item compliance
│
├── data/
│   ├── raw/                         # Original data (DVC tracked)
│   ├── processed/                   # Cleaned data
│   └── analysis_dataset.csv         # Final analysis file
│
└── results/
    ├── descriptive_statistics.csv   # Table 1
    ├── main_results.csv             # Primary analysis
    ├── sensitivity_analyses/        # Robustness checks
    └── strobe_compliance_report.md
```

---

## Study Design Types

### Cohort Study (Prospective/Retrospective)

**Use when**: Following people forward in time to see who develops outcome

**Example**: Following 10,000 smokers and non-smokers for 20 years to compare lung cancer rates

**Advantages**:
- Can calculate incidence
- Multiple outcomes
- Temporal sequence clear

**Analysis**: Cox proportional hazards, Poisson regression

### Case-Control Study

**Use when**: Outcome is rare, need to start with cases and find controls

**Example**: 500 lung cancer cases matched with 500 controls, compare smoking history

**Advantages**:
- Efficient for rare outcomes
- Faster than cohort
- Lower cost

**Analysis**: Conditional logistic regression, odds ratios

### Cross-Sectional Study

**Use when**: Single time point, prevalence questions

**Example**: Survey 5,000 people about current smoking and current health status

**Advantages**:
- Quick
- Inexpensive
- Good for prevalence

**Analysis**: Logistic regression, prevalence ratios

---

## STROBE Compliance (22 Items)

This template ensures **22/22 STROBE items** addressed:

### Title & Abstract
- ✅ Item 1: Design indicated in title/abstract

### Introduction
- ✅ Item 2: Background/rationale
- ✅ Item 3: Objectives

### Methods
- ✅ Item 4: Study design (cohort/case-control/cross-sectional)
- ✅ Item 5: Setting, locations, dates
- ✅ Item 6: Eligibility criteria
- ✅ Item 7: Data sources/measurements
- ✅ Item 8: Assessment of exposure
- ✅ Item 9: Assessment of outcome
- ✅ Item 10: Variable definitions
- ✅ Item 11: Data sources and methods
- ✅ Item 12: Statistical methods (confounding, interactions, sensitivity)

### Results
- ✅ Item 13: Participants (flow diagram)
- ✅ Item 14: Descriptive data (Table 1)
- ✅ Item 15: Outcome data
- ✅ Item 16: Main results (effect estimates with CIs)
- ✅ Item 17: Other analyses (sensitivity, subgroups)

### Discussion
- ✅ Item 18: Interpretation
- ✅ Item 19: Limitations
- ✅ Item 20: Generalizability

### Other
- ✅ Item 21: Funding
- ✅ Item 22: Availability of data/code

---

## Confounding Analysis

### DAG-Based Approach

**1. Build DAG** (`code/dag_builder.py`):
```python
# Define causal structure
dag = DAG()
dag.add_edge("Smoking", "LungCancer")
dag.add_edge("Age", "Smoking")
dag.add_edge("Age", "LungCancer")  # Age confounds Smoking→LungCancer
dag.add_edge("SES", "Smoking")
dag.add_edge("SES", "Healthcare")
dag.add_edge("Healthcare", "LungCancer")

# DAG identifies minimal sufficient adjustment set:
# Control for: {Age, SES} to block backdoor paths
```

**2. Change-in-Estimate Method**:
```python
# code/confounding_analysis.py
# Crude model
OR_crude = logistic_regression(outcome ~ exposure)

# Adjusted model
OR_adjusted = logistic_regression(outcome ~ exposure + confounders)

# If OR changes >10%, confounder present
change = abs((OR_adjusted - OR_crude) / OR_crude)
if change > 0.10:
    print(f"Confounding detected: {change:.1%} change in estimate")
```

**3. Stratification**:
```python
# Examine exposure-outcome relationship within strata
for age_group in ["<50", "50-65", ">65"]:
    OR = calculate_OR(subset=age_group)
    # Check for effect modification
```

---

## Pre-configured Scripts

### Design Selector

`code/design_selector.py` - Choose appropriate study design:

```python
"""
Interactive study design selector.

Asks about:
- Research question
- Outcome frequency
- Timeline
- Resources available

Recommends:
- Cohort, case-control, or cross-sectional
- Sample size estimate
- Timeline estimate
"""
```

### DAG Builder

`code/dag_builder.py` - Visual DAG tool:

```python
"""
Directed Acyclic Graph builder.

Features:
- Drag-and-drop variable placement
- Arrow drawing for causal paths
- Automatic backdoor path identification
- Minimal adjustment set calculation
- Export as PNG/SVG
"""
```

### Statistical Analysis Pipeline

`code/regression_analysis.py`:

```python
"""
Main analysis script.

Supports:
- Logistic regression (binary outcomes)
- Linear regression (continuous outcomes)
- Cox proportional hazards (time-to-event)
- Poisson regression (count outcomes)

Outputs:
- Effect estimates with 95% CIs
- Adjusted for confounders
- Tests for effect modification
- Diagnostic plots
"""
```

---

## Example Workflow: Cohort Study

### Step 1: Define Study

```yaml
# docs/variable_definitions.yaml
study_design: "prospective_cohort"

exposure:
  name: "Physical activity level"
  type: "categorical"
  levels: ["Sedentary", "Moderate", "High"]
  measurement: "Questionnaire at baseline"

outcome:
  name: "Cardiovascular disease"
  type: "binary"
  definition: "MI, stroke, or CV death"
  ascertainment: "Medical records review"

confounders:
  - name: "Age"
    type: "continuous"
  - name: "Sex"
    type: "binary"
  - name: "Smoking status"
    type: "categorical"
  - name: "BMI"
    type: "continuous"

follow_up:
  duration: "10 years"
  assessment_points: ["Baseline", "5 years", "10 years"]
```

### Step 2: Build DAG

```python
# code/dag_builder.py identifies:
# - Direct path: PhysicalActivity → CVD
# - Confounders: Age, Sex, Smoking, BMI
# - Mediators: None (don't adjust for these)
# - Colliders: None (don't adjust for these)
```

### Step 3: Analysis

```bash
python code/regression_analysis.py

# Runs Cox proportional hazards:
# outcome: time to CVD event
# exposure: physical activity (ref: Sedentary)
# adjusted for: age, sex, smoking, BMI

# Output:
# Moderate activity: HR = 0.75 (95% CI: 0.65-0.87), p < 0.001
# High activity: HR = 0.58 (95% CI: 0.48-0.70), p < 0.001
```

### Step 4: Sensitivity Analyses

```bash
python code/sensitivity_analysis.py

# Runs:
# 1. Complete case analysis (no missing data)
# 2. Multiple imputation for missing data
# 3. Exclusion of first 2 years (reverse causation)
# 4. Propensity score matching
# 5. E-value calculation (unmeasured confounding)
```

---

## Using Research Assistant Agents

### Agent: experiment-designer

```
/agent experiment-designer

I'm planning an observational cohort study on physical activity and cardiovascular disease.
Please help me:
1. Determine required sample size
2. Define exposure and outcome precisely
3. Identify confounders
4. Plan statistical analysis
```

### Agent: data-analyst

```
/agent data-analyst

I have cohort data (N=10,000, 15-year follow-up).
Exposure: Physical activity (3 levels)
Outcome: CVD events
Confounders: Age, sex, smoking, BMI

Please conduct:
- Cox proportional hazards analysis
- Check proportional hazards assumption
- Sensitivity analyses
```

---

## Common Pitfalls Prevented

✅ **Confounding not addressed** → DAG-based confounder identification  
✅ **Unclear temporal sequence** → Design selector ensures appropriate design  
✅ **Missing data not handled** → Multiple imputation + sensitivity analyses  
✅ **Effect modification not tested** → Automatic interaction tests  
✅ **Assumptions not checked** → Diagnostic plots for all models  
✅ **Selection bias** → Participant flow diagram  
✅ **Incomplete STROBE** → Auto-validator checks 22 items  

---

## Citation

```
Research Assistant for Claude Code. (2025). Observational Study Template. 
Retrieved from https://github.com/astoreyai/ai_scientist
```

---

*Template version: 1.2.0*  
*STROBE compliant: 22/22 items*  
*Last updated: 2025-11-10*
