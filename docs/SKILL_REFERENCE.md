# Skill Reference - Research Assistant Plugin

Complete reference for all 22 research methodology skills.

---

## Skill Categories

### Core Research Skills (6)
1. **ai-check** - AI-generated text detection
2. **citation-format** - Multi-style citation formatting  
3. **power-analysis** - Statistical power calculations
4. **effect-size** - Effect size calculations
5. **prisma-diagram** - PRISMA flow diagrams
6. **hypothesis-test** - Statistical test selection

### Research Planning Skills (4)
7. **research-questions** - FINER criteria application
8. **literature-gap** - Gap identification
9. **synthesis-matrix** - Evidence synthesis
10. **inclusion-criteria** - Eligibility criteria application

### Study Design Skills (4)
11. **experiment-design** - Rigorous experimental design
12. **pre-registration** - Pre-registration documents
13. **randomization** - Randomization procedures
14. **blinding** - Blinding procedures

### Analysis Skills (5)
15. **data-visualization** - Publication-quality figures
16. **results-interpretation** - Statistical interpretation
17. **meta-analysis** - Quantitative synthesis
18. **sensitivity-analysis** - Robustness testing
19. **subgroup-analysis** - Moderator analysis

### Quality & Ethics Skills (3)
20. **irb-protocol** - Ethics protocols
21. **risk-of-bias** - Study quality assessment
22. **publication-prep** - Manuscript preparation

---

## Quick Reference Table

| Skill | Use When | Key Output |
|-------|----------|------------|
| ai-check | Checking writing authenticity | Confidence score, suggestions |
| citation-format | Converting citation styles | Formatted references |
| power-analysis | Planning sample size | Required N with justification |
| effect-size | Quantifying effects | d, r, η² with CI |
| prisma-diagram | Documenting screening | PRISMA flow diagram |
| hypothesis-test | Choosing statistical test | Test recommendation |
| research-questions | Formulating questions | FINER-validated questions |
| literature-gap | Identifying gaps | Prioritized gap list |
| synthesis-matrix | Organizing evidence | Evidence table |
| inclusion-criteria | Screening studies | Eligibility decisions |
| experiment-design | Planning studies | Complete protocol |
| pre-registration | Pre-registering | Pre-reg document |
| randomization | Assigning participants | Allocation sequence |
| blinding | Reducing bias | Blinding protocol |
| data-visualization | Creating figures | Publication-ready plots |
| results-interpretation | Reporting results | Interpretation text |
| meta-analysis | Pooling results | Summary effect size |
| sensitivity-analysis | Testing robustness | Robustness assessment |
| subgroup-analysis | Testing moderators | Subgroup effects |
| irb-protocol | Ethics approval | IRB application |
| risk-of-bias | Assessing quality | RoB ratings |
| publication-prep | Preparing manuscripts | Submission-ready paper |

---

## Detailed Skill Descriptions

### 1. ai-check

**Purpose:** Detect AI-generated text patterns to ensure writing authenticity.

**Detection Methods:**
- Grammar perfection (excessive correctness)
- Sentence uniformity (15-25 word sweet spot)
- Paragraph structure (mechanical 4-6 sentences)
- AI-typical words ("delve", "leverage", "robust")
- Punctuation patterns (perfect semicolon usage)

**Confidence Levels:**
- 0-30%: Likely human ✅
- 30-70%: Possible AI assistance ⚠️
- 70-100%: Likely AI-generated 🚫

**Usage:**
```
Please run ai-check on manuscript.tex
```

**Integrations:**
- Pre-commit hook (automatic)
- QA validation
- Manuscript review agent
- Standalone CLI tool

---

### 2. citation-format

**Purpose:** Format citations in multiple academic styles.

**Supported Styles:**
- APA 7th Edition
- IEEE
- Chicago (Author-Date & Notes)
- Harvard
- MLA 9th Edition
- Nature
- Science

**Usage:**
```
Please convert these citations to APA 7th edition:
[paste citations]
```

**Features:**
- BibTeX parsing and cleaning
- DOI-based retrieval
- Duplicate detection
- Validation checking

---

### 3. power-analysis

**Purpose:** Calculate statistical power and required sample sizes.

**Study Designs:**
- Independent t-test
- Paired t-test
- One-way ANOVA
- Factorial ANOVA
- Chi-square test
- Correlation
- Multiple regression

**Usage:**
```
Calculate sample size for:
- Design: Independent t-test
- Effect size: d = 0.5
- Alpha: 0.05
- Power: 0.80
```

**Output:**
- Required N
- Power curves
- Sensitivity analysis
- NIH-formatted justification

---

### 4. effect-size

**Purpose:** Calculate and interpret standardized effect sizes.

**Effect Size Types:**
- Cohen's d (mean differences)
- Pearson's r (correlations)
- Eta-squared (variance explained)
- Odds ratios
- Risk ratios

**Usage:**
```
Calculate Cohen's d:
Group 1: M=45, SD=8, N=50
Group 2: M=38, SD=9, N=50
```

**Always Reports:**
- Point estimate
- 95% confidence interval
- Interpretation (small/medium/large)

---

### 5. prisma-diagram

**Purpose:** Generate PRISMA 2020 flow diagrams for systematic reviews.

**Usage:**
```
Generate PRISMA diagram with counts:
- Database records: 1250
- Duplicates removed: 320
- Screened: 930
- Full-text assessed: 120
- Included: 28
```

**Output:** Properly formatted PRISMA 2020 flow diagram

---

### 6. hypothesis-test

**Purpose:** Guide selection of appropriate statistical tests.

**Decision Factors:**
- Number of variables
- Variable types (continuous, categorical)
- Study design (independent, paired)
- Assumption violations

**Usage:**
```
Help me choose a statistical test:
- 2 groups (experimental, control)
- Continuous outcome (anxiety scores)
- Independent groups
- N=50 per group
```

**Output:**
- Recommended test
- Assumptions to check
- Alternative tests if assumptions violated

---

### 7. research-questions

**Purpose:** Formulate research questions using FINER criteria.

**FINER:**
- **F**easible
- **I**nteresting
- **N**ovel
- **E**thical
- **R**elevant

**Usage:**
```
Help me refine this research question:
"Does stress affect health?"
```

**Output:** FINER-validated, specific research question

---

### 8. literature-gap

**Purpose:** Systematically identify research gaps.

**Gap Types:**
- Knowledge gaps (unstudied phenomena)
- Methodological gaps (design limitations)
- Theoretical gaps (mechanisms unknown)
- Practice gaps (interventions untested)
- Evidence quality gaps (high risk of bias)

**Usage:**
```
Analyze my synthesis matrix and identify gaps:
[provide synthesis matrix]
```

**Output:** Prioritized list of gaps with justifications

---

### 9. synthesis-matrix

**Purpose:** Create structured evidence synthesis tables.

**Components:**
- Study characteristics
- Methods
- Results
- Quality ratings

**Usage:**
```
Create synthesis matrix for these studies:
[provide extracted data]
```

**Output:** Formatted evidence table

---

### 10. inclusion-criteria

**Purpose:** Apply eligibility criteria systematically.

**PICOS Framework:**
- Population
- Intervention
- Comparison
- Outcome
- Study design

**Usage:**
```
Apply these criteria to studies:
Inclusion: Adults, RCTs, published 2010-2024
Exclusion: Animal studies, no control group
[provide study list]
```

**Output:** Eligibility decisions with rationales

---

### 11. experiment-design

**Purpose:** Design methodologically rigorous experiments.

**Key Elements:**
- Research question
- Study design (RCT, quasi-experimental)
- Sample size justification
- Randomization method
- Blinding procedures
- Control groups
- Outcome measures
- Analysis plan

**Usage:**
```
Help me design an RCT:
- Population: College students with anxiety
- Intervention: 8-week mindfulness program
- Control: Waitlist
- Outcome: GAD-7 scores
- Budget: $40k, 12 months
```

**Output:** Complete experimental protocol

---

### 12. pre-registration

**Purpose:** Create pre-registration documents.

**Components:**
- Hypotheses (primary, secondary, exploratory)
- Design and blinding
- Sample size with power analysis
- Variables and measures
- Analysis plan (primary, secondary)
- Data handling (missing data, outliers)

**Usage:**
```
Create pre-registration for my RCT:
[provide study details]
```

**Output:** Complete pre-registration document (OSF-ready)

---

### 13. randomization

**Purpose:** Implement proper randomization procedures.

**Methods:**
- Simple randomization
- Block randomization
- Stratified randomization
- Minimization

**Usage:**
```
Generate randomization sequence:
- N=100
- 2 groups (1:1)
- Block size: 4
- Stratify by: sex
```

**Output:** Allocation sequence with documentation

---

### 14. blinding

**Purpose:** Implement blinding procedures.

**Types:**
- Single-blind (participants)
- Double-blind (participants + researchers)
- Triple-blind (+ analysts)

**Usage:**
```
Design blinding for drug trial:
- Active drug vs placebo
- Who to blind: participants, assessors
```

**Output:** Blinding protocol with implementation steps

---

### 15. data-visualization

**Purpose:** Create publication-quality figures.

**Figure Types:**
- Bar plots (means + error bars)
- Box plots (distributions)
- Scatter plots (correlations)
- Line graphs (time series)
- Forest plots (meta-analysis)

**Best Practices:**
- Clear labels
- 95% CI error bars
- Color-blind friendly
- High resolution (≥300 DPI)

---

### 16. results-interpretation

**Purpose:** Correctly interpret and report statistical results.

**Key Principles:**
- Effect size > p-value
- Report 95% confidence intervals
- Avoid p-value misinterpretation
- Adjust for multiple comparisons

**Usage:**
```
Help me interpret these results:
t(98) = 3.45, p < .001, d = 0.69, 95% CI [0.29, 1.09]
```

**Output:** Proper statistical reporting text

---

### 17. meta-analysis

**Purpose:** Quantitatively synthesize multiple studies.

**Steps:**
- Extract effect sizes
- Choose model (fixed vs random)
- Pool results
- Assess heterogeneity (I²)
- Publication bias check

**Usage:**
```
Conduct meta-analysis:
[provide extracted effect sizes]
```

**Output:** Summary effect with heterogeneity assessment

---

### 18. sensitivity-analysis

**Purpose:** Test robustness of findings.

**Analyses:**
- Remove outliers
- Remove high risk-of-bias studies
- Different statistical tests
- Missing data scenarios

**Usage:**
```
Conduct sensitivity analysis:
- Remove studies with RoB concerns
- Use non-parametric tests
- Best/worst case for missing data
```

**Output:** Robustness assessment

---

### 19. subgroup-analysis

**Purpose:** Test effect moderators.

**Considerations:**
- Pre-specify subgroups
- Limit number (Type I error)
- Test interactions
- Adjust for multiple comparisons

**Usage:**
```
Subgroup analysis by:
- Age (<50 vs ≥50)
- Sex (male vs female)
- Severity (mild vs moderate/severe)
```

**Output:** Subgroup effects with interaction tests

---

### 20. irb-protocol

**Purpose:** Develop ethics protocols for IRB approval.

**Components:**
- Study purpose and justification
- Design and methods
- Participant selection
- Risks and benefits
- Informed consent
- Privacy and confidentiality
- Compensation

**Usage:**
```
Create IRB protocol for:
[provide study details]
```

**Output:** Complete IRB application

---

### 21. risk-of-bias

**Purpose:** Assess methodological quality of studies.

**Tools:**
- RoB 2 (RCTs)
- ROBINS-I (non-randomized)
- QUADAS-2 (diagnostic)

**Domains:**
- Randomization
- Deviations from protocol
- Missing data
- Outcome measurement
- Selective reporting

**Usage:**
```
Assess risk of bias for:
[provide study details]
```

**Output:** RoB ratings with justifications

---

### 22. publication-prep

**Purpose:** Prepare manuscripts for submission.

**Components:**
- Title page
- Structured abstract
- Reporting checklist (CONSORT, PRISMA)
- References formatted
- Tables and figures
- Supplementary materials

**Usage:**
```
Prepare manuscript for submission to:
Journal: JAMA
Type: RCT
Guidelines: CONSORT
```

**Output:** Submission-ready manuscript with checklist

---

## Using Skills Effectively

### Explicit Invocation

```
Please use the power-analysis skill to calculate required sample size for...
```

### Natural Invocation

Skills are also invoked automatically during relevant tasks:
```
I need to calculate sample size for my RCT...
# power-analysis skill automatically used
```

### Skill Combinations

Many tasks use multiple skills:
```
Study Planning:
1. research-questions (formulate)
2. power-analysis (sample size)
3. experiment-design (protocol)
4. pre-registration (document)
```

---

*Skill reference last updated: 2025-11-09*
