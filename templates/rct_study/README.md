# RCT Study Template

**Purpose**: Complete template for Randomized Controlled Trial research projects  
**Reporting Standard**: CONSORT 2010  
**Includes**: Protocol, power analysis, randomization, analysis pipeline, manuscript structure

---

## Quick Start

1. **Copy this template** to your project directory:
   ```bash
   cp -r templates/rct_study my_rct_project
   cd my_rct_project
   ```

2. **Configure your study** in `docs/study_config.yaml`:
   ```yaml
   study:
     title: "Your study title"
     pi: "Your name"
     population: "Target population"
     intervention: "Intervention description"
     control: "Control condition"
     primary_outcome: "Primary outcome measure"
   ```

3. **Run power analysis**:
   ```bash
   python code/power_analysis.py
   ```

4. **Generate randomization sequence**:
   ```bash
   python code/randomization.py
   ```

5. **Start data collection** using forms in `data/forms/`

---

## Directory Structure

```
rct_study/
├── README.md                    # This file
├── docs/
│   ├── study_config.yaml        # Study configuration
│   ├── protocol.md              # Complete study protocol
│   ├── pre_registration.md      # Pre-registration document (OSF-ready)
│   ├── consort_checklist.md     # CONSORT 2010 checklist
│   └── informed_consent.md      # Informed consent template
│
├── data/
│   ├── forms/
│   │   ├── screening_form.csv   # Participant screening
│   │   ├── baseline_form.csv    # Baseline assessment
│   │   └── followup_form.csv    # Follow-up assessment
│   ├── raw/                     # Raw data (DVC tracked)
│   ├── processed/               # Cleaned data
│   └── codebook.md              # Variable codebook
│
├── code/
│   ├── power_analysis.py        # Sample size calculation
│   ├── randomization.py         # Allocation sequence generator
│   ├── data_cleaning.py         # Data preparation
│   ├── primary_analysis.py      # Pre-specified primary analysis
│   ├── secondary_analysis.py    # Secondary outcomes
│   └── sensitivity_analysis.py  # Robustness checks
│
├── results/
│   ├── consort_flow.md          # CONSORT flow diagram data
│   ├── primary_results.json     # Primary outcome results
│   ├── tables/                  # Publication tables
│   └── figures/                 # Publication figures
│
└── figures/
    └── .gitkeep
```

---

## Workflow Steps

### Phase 1: Planning (Before IRB)

1. **Define research question** using FINER criteria
2. **Run power analysis** (code/power_analysis.py)
3. **Complete protocol** (docs/protocol.md)
4. **Create pre-registration** (docs/pre_registration.md)
5. **Submit to IRB**

### Phase 2: Preparation (After IRB approval)

1. **Generate randomization sequence** (code/randomization.py)
2. **Prepare data collection forms** (data/forms/)
3. **Train research staff**
4. **Pilot test procedures**

### Phase 3: Enrollment & Data Collection

1. **Screen participants** (screening_form.csv)
2. **Obtain informed consent**
3. **Collect baseline data** (baseline_form.csv)
4. **Randomize participants**
5. **Deliver intervention/control**
6. **Collect follow-up data** (followup_form.csv)
7. **Monitor data quality**

### Phase 4: Analysis

1. **Clean data** (code/data_cleaning.py)
2. **Run primary analysis** (code/primary_analysis.py)
3. **Run secondary analyses** (code/secondary_analysis.py)
4. **Perform sensitivity analyses** (code/sensitivity_analysis.py)
5. **Generate tables and figures**

### Phase 5: Reporting

1. **Complete CONSORT checklist** (docs/consort_checklist.md)
2. **Draft manuscript** using `/agent manuscript-writer`
3. **Run AI-check** on all sections
4. **Prepare submission materials**

---

## Using Research Assistant Agents

### Agent: experiment-designer

Use when planning your RCT:

```
/agent experiment-designer

I need to design an RCT for [your intervention] in [your population].
Help me with:
- Power analysis
- Randomization strategy
- Blinding procedures
- Timeline planning
```

### Agent: data-analyst

Use when analyzing collected data:

```
/agent data-analyst

I have RCT data (N=[your N], intervention vs control).
Primary outcome: [your outcome]
Data file: data/processed/analysis_dataset.csv

Please conduct:
- Assumption checks
- Primary analysis (with effect size and 95% CI)
- Sensitivity analysis
```

### Agent: manuscript-writer

Use when writing up results:

```
/agent manuscript-writer

I need to write an RCT manuscript following CONSORT guidelines.
Study: [brief description]
Results: [main findings]
Target journal: [journal name]

Please help draft the manuscript sections.
```

---

## Pre-configured Files

### 1. Power Analysis Script

`code/power_analysis.py` calculates required sample size:

```python
"""
Power analysis for RCT.

Calculates required N for primary outcome.
Generates NIH-formatted justification.
"""

# Edit these parameters:
EXPECTED_EFFECT_SIZE = 0.5  # Cohen's d (0.2=small, 0.5=medium, 0.8=large)
ALPHA = 0.05
POWER = 0.80
ANTICIPATED_ATTRITION = 0.20

# Run: python code/power_analysis.py
```

### 2. Randomization Script

`code/randomization.py` generates allocation sequence:

```python
"""
Randomization sequence generator.

Creates block randomization with concealed allocation.
Saves sequence for implementation.
"""

# Edit these parameters:
TOTAL_N = 100
GROUPS = ["Intervention", "Control"]
ALLOCATION_RATIO = [1, 1]  # 1:1
BLOCK_SIZE = 4
RANDOM_SEED = 12345  # For reproducibility

# Run: python code/randomization.py
```

### 3. CONSORT Checklist

`docs/consort_checklist.md` tracks compliance:

```markdown
# CONSORT 2010 Checklist

- [ ] 1a. Title: Identifies as randomized trial
- [ ] 1b. Abstract: Structured format
- [ ] 2a. Background: Scientific rationale
...
- [ ] 25. Registration: Trial registration number
```

### 4. Study Protocol Template

`docs/protocol.md` complete protocol structure:

```markdown
# Study Protocol: [Title]

## 1. Background and Rationale
## 2. Objectives and Hypotheses
## 3. Study Design
## 4. Participant Selection
## 5. Interventions
## 6. Outcomes
## 7. Sample Size
## 8. Randomization
## 9. Statistical Analysis
## 10. Data Management
## 11. Ethics
## 12. Timeline
```

---

## Data Collection Forms

### Screening Form

`data/forms/screening_form.csv`:

```csv
participant_id,screening_date,age,meets_inclusion,meets_exclusion,eligible,notes
001,2025-11-10,25,yes,no,yes,"Meets all criteria"
002,2025-11-10,17,no,no,no,"Under 18"
```

### Baseline Form

`data/forms/baseline_form.csv`:

```csv
participant_id,baseline_date,outcome_baseline,covariate1,covariate2
001,2025-11-11,45.2,yes,male
```

### Follow-up Form

`data/forms/followup_form.csv`:

```csv
participant_id,followup_date,outcome_followup,completed,notes
001,2025-12-11,38.5,yes,""
```

---

## Analysis Pipeline

### Step 1: Data Cleaning

```bash
python code/data_cleaning.py
# Reads: data/raw/*.csv
# Writes: data/processed/analysis_dataset.csv
# Logs: data/cleaning_log.txt
```

### Step 2: Primary Analysis

```bash
python code/primary_analysis.py
# Reads: data/processed/analysis_dataset.csv
# Writes: results/primary_results.json
# Generates: results/tables/table1_baseline.csv
#            results/tables/table2_outcomes.csv
#            results/figures/fig1_consort.png
```

### Step 3: Secondary Analyses

```bash
python code/secondary_analysis.py
# Analyzes secondary outcomes
# Writes: results/secondary_results.json
```

### Step 4: Sensitivity Analyses

```bash
python code/sensitivity_analysis.py
# Tests robustness:
#   - Complete case analysis
#   - Per-protocol analysis
#   - Different missing data assumptions
# Writes: results/sensitivity_results.json
```

---

## Quality Assurance

### Before Data Collection

- [ ] IRB approval obtained
- [ ] Pre-registration completed (OSF/ClinicalTrials.gov)
- [ ] Randomization sequence generated and sealed
- [ ] Data collection forms finalized
- [ ] Staff training completed
- [ ] Pilot testing done

### During Data Collection

- [ ] Regular data quality checks
- [ ] Adverse event monitoring
- [ ] Protocol adherence tracking
- [ ] Blinding maintenance verification

### Before Analysis

- [ ] Data cleaning script reviewed
- [ ] Analysis plan matches pre-registration
- [ ] No p-hacking or data fishing
- [ ] All analyses pre-specified

### Before Submission

- [ ] CONSORT checklist complete (25/25)
- [ ] All tables/figures referenced
- [ ] AI-check passed (<30% all sections)
- [ ] Reproducibility verified
- [ ] Co-authors approved

---

## Citation

When using this template, cite:

```
Research Assistant for Claude Code. (2025). RCT Study Template. 
Retrieved from https://github.com/astoreyai/ai_scientist
```

---

## Support

- **Full Documentation**: See main repository docs/
- **Agent Help**: Use `/agent experiment-designer` for study-specific guidance
- **Issues**: https://github.com/astoreyai/ai_scientist/issues

---

*Template version: 1.1.0*  
*Last updated: 2025-11-10*
