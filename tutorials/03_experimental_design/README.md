# Tutorial 3: Designing a Randomized Controlled Trial

**Duration**: 40 minutes
**Prerequisites**: Tutorial 1 completed, basic understanding of experimental design
**What you'll learn**: Complete RCT design from research question to registered protocol, NIH rigor standards, power analysis, randomization, CONSORT compliance

---

## Overview

This tutorial guides you through designing a rigorous randomized controlled trial (RCT) that meets **NIH rigor and reproducibility standards** and **CONSORT 2010 guidelines**. You'll learn:

1. Formulating a testable research hypothesis
2. Justifying sample size with power analysis
3. Implementing proper randomization
4. Ensuring allocation concealment
5. Planning blinding procedures
6. Writing a pre-registration protocol
7. Registering on ClinicalTrials.gov/OSF
8. Using the `experiment-designer` agent
9. Addressing sex as a biological variable (SABV)
10. Planning for CONSORT compliance

**Running Example**: We'll design an RCT to test:
*"Does an 8-week online mindfulness-based cognitive therapy (MBCT) program reduce depressive symptoms in college students compared to a wait-list control?"*

---

## Part 1: Research Question Formulation (5 minutes)

### Step 1.1: Assess Research Question Quality

Use the **FINER criteria** to evaluate your research question:

- **F**easible (time, resources, participants available)
- **I**nteresting (will advance knowledge, clinical relevance)
- **N**ovel (fills a gap)
- **E**thical (safe, IRB approvable)
- **R**elevant (impacts field, clinical practice)

**Our Example**:

```
Research Question:
"Does an 8-week online MBCT program reduce depressive symptoms in college
students compared to a wait-list control?"

FINER Assessment:
─────────────────────────────────────────────────
Feasible: Yes
  - Online delivery (scalable)
  - College population (accessible at university)
  - 8 weeks (manageable duration for students)
  - Wait-list control (ethical - all participants eventually receive intervention)

Interesting: Yes
  - Depression is leading cause of disability in college students
  - Online interventions could increase access to treatment
  - Mindfulness shows promise but evidence in students is limited

Novel: Yes
  - Most MBCT studies focus on adults with recurrent depression
  - Few RCTs of online MBCT specifically for college students
  - Gap identified from Tutorial 2 systematic review

Ethical: Yes
  - Low-risk behavioral intervention
  - Wait-list control ensures all receive treatment
  - Screening for suicidal ideation with safety protocol
  - IRB approval feasible

Relevant: Yes
  - College mental health crisis (25% prevalence)
  - Scalable intervention addresses treatment access barriers
  - Informs university counseling services
```

**Checkpoint**: All FINER criteria should be met before proceeding.

---

### Step 1.2: Convert to PICOS Format

From Tutorial 2, you learned PICOS for systematic reviews. Now use it for experimental design:

```
P - Population: College students (ages 18-25) with mild-to-moderate depressive
                symptoms (PHQ-9 score 10-19)

I - Intervention: 8-week online MBCT program
                  - Weekly 1-hour modules
                  - Guided meditations
                  - Cognitive therapy exercises
                  - Daily home practice (15 min)

C - Comparison: Wait-list control (8 weeks)
                - Access to MBCT after primary endpoint
                - Monthly check-in emails (attention control)

O - Outcome: Depressive symptoms (PHQ-9 score)
             - Primary: Change from baseline to 8 weeks
             - Secondary: Anxiety (GAD-7), mindfulness (FFMQ), functioning

S - Study design: Parallel-group randomized controlled trial
                  - 1:1 allocation ratio
                  - Superiority trial
                  - Assessments: Baseline, 8 weeks (primary), 16 weeks (follow-up)
```

**Checkpoint**: PICOS should be specific enough to calculate sample size.

---

## Part 2: Power Analysis and Sample Size (10 minutes)

### Step 2.1: Use RCT Template Power Analysis Tool

**Action**: Copy the RCT template and run power analysis

```bash
# Copy template
cp -r templates/rct_study my_mbct_trial
cd my_mbct_trial

# Run interactive power analysis
python code/power_analysis.py
```

**Interactive Prompts**:

```
═══════════════════════════════════════════════
    NIH-Compliant Power Analysis Tool
═══════════════════════════════════════════════

Study Design: Two-group parallel RCT

Primary Outcome: Change in PHQ-9 score (continuous)

Expected Effect Size
────────────────────────────────────────────────
How will you justify the expected effect size?

Options:
  1. Prior studies (meta-analysis)
  2. Pilot data
  3. Minimally clinically important difference (MCID)
  4. Clinical consensus

Your choice: 1

Meta-Analysis Summary:
- Prior MBCT trials for depression: Cohen's d = 0.50 (95% CI: 0.35-0.65)
- College student interventions: Cohen's d = 0.35 (95% CI: 0.20-0.50)
- Online delivery: Cohen's d = 0.40 (95% CI: 0.25-0.55)

Conservative estimate (lower bound of CI for online): d = 0.40

Enter expected effect size (Cohen's d): 0.40

Statistical Parameters
────────────────────────────────────────────────
Significance level (α): 0.05 (default, two-tailed)
Desired power (1-β): 0.80 (default, 80%)
Allocation ratio: 1:1 (default, equal groups)

Attrition Estimation
────────────────────────────────────────────────
Expected attrition rate (%): 20
(typical for online behavioral trials with students)
```

**Generated Output**:

```
═══════════════════════════════════════════════
           POWER ANALYSIS RESULTS
═══════════════════════════════════════════════

Sample Size Calculation:
────────────────────────────────────────────────
Effect size (Cohen's d): 0.40
Significance level (α): 0.05 (two-tailed)
Power (1-β): 0.80
Test: Independent samples t-test

Required sample size (per group): 100
Total sample size needed: 200

Accounting for Attrition:
────────────────────────────────────────────────
Expected attrition: 20%
Adjusted sample size (per group): 125
Total to recruit: 250

Recruitment Plan:
────────────────────────────────────────────────
MBCT group: 125 participants
Wait-list group: 125 participants
Total enrollment: 250 participants

Power Curve Analysis:
────────────────────────────────────────────────
If attrition is lower (10%): Power = 0.85
If attrition is higher (30%): Power = 0.75
If effect size is d=0.50: Power = 0.92
If effect size is d=0.30: Power = 0.65

Justification for NIH Application:
────────────────────────────────────────────────
Sample size of 250 (125 per group) provides 80% power to detect a moderate
effect (Cohen's d = 0.40) at α = 0.05 (two-tailed). Effect size is based on
conservative estimates from meta-analyses of online mindfulness interventions
(d = 0.40, 95% CI: 0.25-0.55). Assuming 20% attrition (typical for online
studies), we will recruit 250 participants to ensure 200 completers for
adequate power.

Sensitivity Analysis:
Even with higher attrition (30%), power remains acceptable (75%). If the true
effect is larger (d = 0.50), power exceeds 90%.

Power analysis report saved: docs/power_analysis_report.pdf
NIH biosketches justification: docs/nih_sample_size_justification.docx
```

**Checkpoint**: Sample size justified with documented assumptions.

---

### Step 2.2: Verify Power Analysis Manually

**Action**: Understand the calculation

```python
from statsmodels.stats.power import TTestIndPower

# Create power analysis object
analysis = TTestIndPower()

# Calculate sample size per group
n_per_group = analysis.solve_power(
    effect_size=0.40,    # Cohen's d
    alpha=0.05,          # Significance level
    power=0.80,          # Desired power
    ratio=1.0,           # 1:1 allocation
    alternative='two-sided'
)

print(f"Sample size per group: {int(np.ceil(n_per_group))}")
# Output: 100

# Adjust for attrition
attrition_rate = 0.20
n_adjusted = int(np.ceil(n_per_group / (1 - attrition_rate)))
print(f"Adjusted for 20% attrition: {n_adjusted}")
# Output: 125

total_n = n_adjusted * 2
print(f"Total to recruit: {total_n}")
# Output: 250
```

**Checkpoint**: Manually verified calculation matches tool output.

---

## Part 3: Randomization Strategy (10 minutes)

### Step 3.1: Choose Randomization Method

**Options**:

1. **Simple Randomization** (flip a coin for each participant)
   - Easy to implement
   - ✗ Risk of imbalance in small samples
   
2. **Block Randomization** (ensure balance in blocks)
   - Guarantees balance throughout recruitment
   - Useful for sequential enrollment
   - RECOMMENDED for most RCTs

3. **Stratified Randomization** (balance within subgroups)
   - Ensures balance on important covariates
   - ✗ More complex
   - Use if strong prognostic factors known

**Our Choice**: **Block randomization with block size 4**

**Why**:
- Ensures 1:1 balance throughout recruitment
- Protects against imbalance if recruitment stops early
- Block size 4 is small enough for balance, large enough to maintain concealment

---

### Step 3.2: Generate Randomization Sequence

**Action**: Run randomization tool

```bash
python code/randomization.py \
  --total 250 \
  --groups MBCT WaitList \
  --block-size 4 \
  --seed 20241110 \
  --output data/randomization_sequence.csv
```

**What It Does**:

1. **Sets Random Seed**: Ensures reproducibility (NIH requirement)
2. **Generates Blocks**: Creates blocks of 4 (2 MBCT, 2 WaitList in random order)
3. **Allocates Sequentially**: Participant 1 gets first allocation, etc.
4. **Conceals Sequence**: Saves in encrypted format until allocation

**Output**:

```
═══════════════════════════════════════════════
      RANDOMIZATION SEQUENCE GENERATED
═══════════════════════════════════════════════

Total participants: 250
Groups: MBCT (n=125), WaitList (n=125)
Allocation ratio: 1:1
Block size: 4
Random seed: 20241110

First block (4 participants):
  Participant 001: WaitList
  Participant 002: MBCT
  Participant 003: MBCT
  Participant 004: WaitList

Verification:
─────────────────────────────────────────────────
Total MBCT: 125 (50.0%)
Total WaitList: 125 (50.0%)
Balance achieved

Allocation Concealment:
─────────────────────────────────────────────────
Sequence saved in SEALED format:
- File: data/randomization_sequence_SEALED.csv (encrypted)
- Decryption key held by: statistician@university.edu
- Study coordinator will access via web portal (one at a time)

Randomization Log:
─────────────────────────────────────────────────
Sequence generation documented: docs/randomization_protocol.pdf
CONSORT flow diagram template: docs/consort_flow_template.md

═══════════════════════════════════════════════
```

**Checkpoint**: Randomization sequence generated and concealed.

---

### Step 3.3: Implement Allocation Concealment

**Allocation Concealment** prevents researchers from predicting assignments before enrollment (prevents selection bias).

**Methods** (choose one):

1. **Sequentially Numbered Opaque Sealed Envelopes (SNOSE)**
   - Low-tech but effective
   - Envelope opened only after participant enrolled

2. **Central Randomization** (RECOMMENDED)
   - Web-based system
   - Study coordinator logs in after enrollment
   - System reveals assignment (one at a time)

3. **Pharmacy-Controlled** (for drug trials)
   - Pharmacist holds sequence
   - Dispenses medication by participant number

**Our Implementation**: **Central randomization via REDCap**

```yaml
# docs/allocation_concealment_protocol.yaml

system: REDCap randomization module

access_control:
  - Study coordinator: Can randomize participants (web portal)
  - PI: Cannot access sequence (prevents bias)
  - Statistician: Holds master list (locked until analysis)

procedure:
  1. Participant completes baseline assessment
  2. Study coordinator confirms eligibility
  3. Coordinator logs into REDCap
  4. Enters participant ID
  5. REDCap reveals assignment
  6. Coordinator notifies participant

safeguards:
  - Sequence locked after generation
  - Audit trail of all randomizations (timestamps, user IDs)
  - Cannot skip or reverse assignments
```

**Checkpoint**: Allocation concealment method documented.

---

## Part 4: Blinding Procedures (5 minutes)

### Step 4.1: Determine Who Can Be Blinded

**Triple-Blind** (participants, providers, outcome assessors):
- Ideal for drug trials
- NOT possible for behavioral interventions (participants know what they're doing)

**Our Trial** (online MBCT):

```
Can we blind...?

Participants: ✗ NO
  - Impossible to blind participants to MBCT vs. wait-list
  - They know they're meditating or waiting

Intervention Providers: ✗ NO (but N/A for online self-guided)
  - No live providers in this study
  - Automated online modules

Outcome Assessors: YES
  - Outcome is self-report questionnaires
  - Can blind data analysts to group assignment

Data Analysts: YES
  - Code groups as "Group A" and "Group B" during analysis
  - Reveal assignment only after analysis complete
```

**Our Blinding Plan**: **Single-blind (outcome assessors)**

---

### Step 4.2: Mitigate Risk of Bias from Lack of Blinding

When blinding is impossible, use these strategies:

1. **Objective Outcomes** (less susceptible to bias)
   - PHQ-9 is validated self-report (objective scoring)
   - Not subject to assessor interpretation

2. **Automated Data Collection**
   - Online surveys (no assessor interaction)
   - Participants complete independently

3. **Blinded Statistical Analysis**
   - Statistician analyzes "Group A vs. Group B"
   - Code broken only after results finalized

4. **Pre-Registration** (prevents outcome switching)
   - All outcomes and analyses pre-specified
   - Reduces opportunity for bias

**Checkpoint**: Blinding plan documented with risk mitigation strategies.

---

## Part 5: Protocol Writing (5 minutes)

### Step 5.1: Generate CONSORT-Compliant Protocol

**Action**: Use template generator

```bash
python code/generate_protocol.py \
  --picos docs/picos.yaml \
  --power docs/power_analysis_report.pdf \
  --randomization docs/randomization_protocol.pdf \
  --output docs/trial_protocol_v1.0.docx
```

**Generated Protocol Sections** (25-30 pages):

```
1. Title and Trial Registration
   - Full title
   - ClinicalTrials.gov ID (placeholder - register in Step 6)

2. Introduction
   - Background and rationale
   - Objectives and hypotheses

3. Methods - Participants
   - Inclusion criteria
   - Exclusion criteria
   - Recruitment methods
   - Setting

4. Methods - Interventions
   - MBCT intervention (detailed description)
   - Wait-list control (detailed description)
   - Intervention fidelity monitoring

5. Methods - Outcomes
   - Primary outcome: PHQ-9 change (baseline to 8 weeks)
   - Secondary outcomes: GAD-7, FFMQ, functioning
   - Assessment schedule: Baseline, 8 weeks, 16 weeks

6. Methods - Sample Size
   - Power analysis (from Part 2)
   - Justification of assumptions

7. Methods - Randomization
   - Sequence generation (block randomization, block size 4)
   - Allocation concealment (REDCap central randomization)
   - Implementation (study coordinator)

8. Methods - Blinding
   - Participants: Not blinded
   - Outcome assessors: Blinded (automated self-report)
   - Data analysts: Blinded

9. Methods - Statistical Analysis
   - Primary analysis: ANCOVA (8-week PHQ-9 adjusted for baseline)
   - Intention-to-treat (ITT) principle
   - Missing data: Multiple imputation
   - Significance level: α = 0.05

10. Methods - Data Management
    - REDCap database
    - Quality control procedures
    - Data security

11. Ethics
    - IRB approval (pending)
    - Informed consent process
    - Safety monitoring (suicidal ideation protocol)

12. Dissemination
    - Publication plan
    - Data sharing plan (de-identified data on OSF after publication)
```

**Checkpoint**: Protocol should be 25-30 pages, ready for IRB submission.

---

### Step 5.2: Address Sex as a Biological Variable (SABV)

**NIH Requirement**: All vertebrate animal and human studies must consider sex as a biological variable.

**Our Plan**:

```yaml
# docs/sabv_plan.yaml

sex_consideration:
  will_enroll_both_sexes: yes
  justification: |
    Depression affects both male and female college students. Including both
    sexes increases generalizability and allows exploration of sex differences
    in MBCT response.

  planned_enrollment:
    female: 150 (60% - reflects depression prevalence in college students)
    male: 100 (40%)
  
  recruitment_strategy:
    - No sex-based enrollment restrictions
    - Recruitment materials gender-neutral
    - Monitor enrollment monthly to ensure adequate representation

  analysis_plan:
    primary_analysis: |
      Primary analysis will pool both sexes (powered for main effect).
    
    exploratory_sex_analysis: |
      Exploratory analysis will test intervention × sex interaction to examine
      whether MBCT effects differ by sex. NOTE: Study is not powered for this
      subgroup analysis (would require n=1000 for 80% power to detect
      interaction). Results will be interpreted cautiously and considered
      hypothesis-generating for future research.

  reporting: |
    CONSORT diagram will show enrollment, allocation, and outcomes separately
    for male and female participants. Baseline characteristics table will
    report sex distribution. Results section will report exploratory sex
    interaction analysis.
```

**Checkpoint**: SABV addressed per NIH policy.

---

## Part 6: Pre-Registration (5 minutes)

### Step 6.1: Register on ClinicalTrials.gov

**Why Register**:
- Required for publication in most journals
- Prevents outcome switching
- Increases transparency
- WHO Trial Registration Data Set (20 items) requirement

**Action**: Complete registration before enrolling first participant

**Platform Options**:
1. **ClinicalTrials.gov** (USA, clinical trials)
2. **OSF Registries** (any discipline, free)
3. **AsPredicted** (social science, short form)

**Our Choice**: **ClinicalTrials.gov** (clinical trial, USA-based)

---

### Step 6.2: Complete WHO 20-Item Dataset

**Action**: Go to https://clinicaltrials.gov/ct2/manage-recs/how-register

**Required Information**:

```
1. Primary Registry ID: (auto-generated, e.g., NCT05123456)
2. Trial Registration Date: 2024-11-10
3. Secondary IDs: IRB-2024-1234 (university IRB number)

4. Funding Source: National Institute of Mental Health (NIMH)

5. Primary Sponsor: University of Example

6. Secondary Sponsors: None

7. Contact for Public Queries:
   - Dr. Jane Smith, PI
   - jane.smith@university.edu

8. Contact for Scientific Queries:
   - Dr. Jane Smith
   - jane.smith@university.edu

9. Public Title:
   "Online Mindfulness Therapy for College Student Depression"

10. Scientific Title:
    "Efficacy of an 8-Week Online Mindfulness-Based Cognitive Therapy Program
     for Depressive Symptoms in College Students: A Randomized Controlled Trial"

11. Countries of Recruitment: United States

12. Health Condition:
    - Depression
    - Depressive Symptoms
    - Mental Health

13. Intervention:
    - Behavioral: Mindfulness-Based Cognitive Therapy (MBCT) - Online

14. Key Inclusion Criteria:
    - College students (ages 18-25)
    - Mild-to-moderate depressive symptoms (PHQ-9: 10-19)
    - Internet access
    - English fluency

15. Key Exclusion Criteria:
    - Severe depression (PHQ-9 ≥20)
    - Active suicidal ideation
    - Current psychotherapy
    - Psychotropic medication change in past 4 weeks

16. Study Type: Interventional

17. Study Design:
    - Allocation: Randomized
    - Intervention Model: Parallel Assignment
    - Masking: Single (Outcomes Assessor)
    - Primary Purpose: Treatment

18. Primary Outcome:
    - Outcome: Change in PHQ-9 Score
    - Timeframe: Baseline to 8 weeks
    - Description: Patient Health Questionnaire-9 (0-27 scale, lower is better)

19. Secondary Outcomes:
    - Anxiety symptoms (GAD-7): Baseline to 8 weeks
    - Mindfulness (FFMQ): Baseline to 8 weeks
    - Functional impairment (SDS): Baseline to 8 weeks

20. Target Sample Size: 250
```

**Checkpoint**: Trial registered on ClinicalTrials.gov with NCT number received.

---

### Step 6.3: Register Analysis Plan on OSF

For additional transparency, pre-register your **statistical analysis plan** on OSF.

**Action**: Go to https://osf.io/registries

```yaml
# Statistical Analysis Plan (OSF Pre-Registration)

study_title: "MBCT for College Student Depression RCT"

hypotheses:
  primary: |
    H1: Participants randomized to MBCT will show greater reduction in PHQ-9
    scores from baseline to 8 weeks compared to wait-list control.
  
  secondary: |
    H2: MBCT will reduce anxiety symptoms (GAD-7) more than wait-list.
    H3: MBCT will increase mindfulness (FFMQ) more than wait-list.

sample_size: 250 (125 per group)

analysis_plan:
  primary_analysis:
    outcome: Change in PHQ-9 (baseline to 8 weeks)
    model: ANCOVA
    formula: PHQ9_8wk ~ group + PHQ9_baseline + sex
    software: R 4.3.1, lm() function
    significance: α = 0.05 (two-tailed)
    effect_estimate: Adjusted mean difference with 95% CI
  
  missing_data:
    method: Multiple imputation (m=20 imputations)
    software: mice package in R
    auxiliary_variables: [PHQ9_baseline, age, sex, GAD7_baseline]
  
  sensitivity_analyses:
    - Complete case analysis (no imputation)
    - Per-protocol analysis (≥6 of 8 modules completed)
    - Baseline-adjusted change analysis (difference-in-differences)
  
  subgroup_analyses:
    - Intervention × sex interaction (exploratory, underpowered)
    - Intervention × baseline severity interaction (PHQ-9 < 15 vs. ≥15)
  
  adjustment_for_multiple_comparisons:
    primary_outcome: No adjustment (single primary hypothesis)
    secondary_outcomes: Report raw p-values and adjust using Holm-Bonferroni

deviations_from_plan:
  - Any deviations will be documented in CONSORT diagram
  - Protocol amendments will be uploaded to ClinicalTrials.gov
```

**Checkpoint**: Analysis plan registered on OSF before data collection begins.

---

## Part 7: Using Experiment-Designer Agent (5 minutes)

### Step 7.1: Invoke Agent for Protocol Review

The `experiment-designer` agent can review your protocol for NIH rigor compliance.

**Action**:

```
/agent experiment-designer

I've designed an RCT for online MBCT for college student depression. Can you
review my protocol for NIH rigor and reproducibility standards?

Protocol: [Attach docs/trial_protocol_v1.0.docx]

Please check:
1. Power analysis justification
2. Randomization method
3. Allocation concealment
4. Blinding procedures
5. SABV consideration
6. Pre-registration completeness
```

**Agent Response** (example):

```
═══════════════════════════════════════════════
    NIH RIGOR CHECKLIST - PROTOCOL REVIEW
═══════════════════════════════════════════════

Overall Assessment: STRONG - Meets NIH Rigor Standards
Revision Needed: MINOR (see recommendations)

POWER ANALYSIS ✓
─────────────────────────────────────────────────
Sample size justified with power calculation
Effect size based on prior evidence (conservative)
Attrition accounted for (20%)
Sensitivity analysis provided

Recommendation: Consider adding stopping rule for futility (e.g., interim
analysis at n=125 to assess if continuing is warranted).

RANDOMIZATION ✓
─────────────────────────────────────────────────
Method clearly specified (block randomization, block size 4)
Random seed documented (20241110)
Allocation ratio justified (1:1)
Sequence generation reproducible

No changes needed.

ALLOCATION CONCEALMENT ✓
─────────────────────────────────────────────────
Central randomization via REDCap
Sequence concealed until enrollment
Study coordinator cannot predict assignments

No changes needed.

BLINDING 
─────────────────────────────────────────────────
Appropriate for behavioral intervention (single-blind)
Outcome assessors blinded (automated self-report)
Data analysts blinded during analysis

Recommendation: Specify in protocol how you will assess success of blinding
(e.g., ask participants at end of study what group they think they were in,
though this may not be feasible for MBCT vs. wait-list given obvious difference).

SEX AS BIOLOGICAL VARIABLE (SABV) ✓
─────────────────────────────────────────────────
Both sexes enrolled
Enrollment targets justified (60F/40M reflects prevalence)
Analysis plan includes exploratory sex interaction
Acknowledges underpowered for subgroup analysis

Excellent. Consider adding language about potential sex differences in help-
seeking behavior that might affect recruitment.

PRE-REGISTRATION ✓
─────────────────────────────────────────────────
Registered on ClinicalTrials.gov
WHO 20-item dataset complete
Statistical analysis plan pre-registered (OSF)
All outcomes and analyses pre-specified

No changes needed.

ADDITIONAL NIH REQUIREMENTS ✓
─────────────────────────────────────────────────
Outcome measures validated
Data sharing plan specified (de-identified data on OSF)
Timeline realistic
Rigor and reproducibility addressed throughout

Recommendation: Add data monitoring plan (even though low-risk study, specify
interim safety reviews).

═══════════════════════════════════════════════
FINAL RECOMMENDATION: APPROVE WITH MINOR REVISIONS
═══════════════════════════════════════════════

Priority Revisions:
1. Add data monitoring plan (safety reviews every 3 months)
2. Consider futility stopping rule (optional but recommended)

Optional Enhancements:
3. Blinding assessment (ask participants to guess group assignment)
4. Note sex differences in help-seeking in recruitment plan

This protocol demonstrates excellent rigor and would score highly in NIH review.
```

**Checkpoint**: Agent review complete with recommendations.

---

### Step 7.2: Incorporate Agent Feedback

**Action**: Update protocol based on agent recommendations

```bash
# Create version 1.1 with revisions
python code/generate_protocol.py \
  --version 1.1 \
  --add-section "Data Monitoring Plan" \
  --add-section "Futility Stopping Rule" \
  --output docs/trial_protocol_v1.1.docx
```

**Added Section: Data Monitoring Plan**

```
DATA MONITORING PLAN

Safety Monitoring:
- PI will review all adverse events monthly
- Safety committee (PI + 2 independent faculty) will meet every 3 months
- Serious adverse events (suicidal ideation) reported to IRB within 24 hours

Suicidal Ideation Protocol:
- PHQ-9 item 9 (suicidal thoughts) screened at all timepoints
- Score ≥2 triggers immediate contact by licensed clinician
- Safety plan created, referral to campus counseling
- Participant may continue in study if deemed safe

Data Monitoring:
- No formal Data and Safety Monitoring Board (DSMB) required (low-risk
  behavioral intervention)
- Data quality checks monthly (missing data, out-of-range values)
- Enrollment monitoring (sex balance, recruitment timeline)

Interim Analysis (Optional):
- At n=125 (50% enrollment), conduct blinded interim analysis
- If between-group difference is d < 0.10, consider stopping for futility
- Decision made by independent statistician (not study team)
```

**Checkpoint**: Protocol updated to v1.1 incorporating all feedback.

---

## Part 8: CONSORT Planning (5 minutes)

### Step 8.1: Generate CONSORT Flow Diagram Template

Even before starting the trial, plan your CONSORT diagram.

**Action**:

```bash
python code/generate_consort_template.py \
  --sample-size 250 \
  --groups MBCT WaitList \
  --timepoints Baseline 8wk 16wk \
  --output docs/consort_flow_template.md
```

**Generated Template**:

```
CONSORT 2010 Flow Diagram
═══════════════════════════════════════════════

ENROLLMENT
─────────────────────────────────────────────────
Assessed for eligibility (n = ___ )

  Excluded (n = ___ )
    • Did not meet inclusion criteria (n = ___ )
    • Declined to participate (n = ___ )
    • Other reasons (n = ___ )

Randomized (n = 250)

ALLOCATION
─────────────────────────────────────────────────
Allocated to MBCT (n = 125)           Allocated to Wait-List (n = 125)
  • Received allocated intervention     • Received allocated intervention
    (n = ___ )                            (n = ___ )
  • Did not receive allocated           • Did not receive allocated
    intervention (give reasons)           intervention (give reasons)
    (n = ___ )                            (n = ___ )

FOLLOW-UP (8 weeks)
─────────────────────────────────────────────────
Lost to follow-up (n = ___ )          Lost to follow-up (n = ___ )
  (give reasons)                        (give reasons)

Discontinued intervention (n = ___ )   Discontinued intervention (n = ___ )
  (give reasons)                        (give reasons)

FOLLOW-UP (16 weeks)
─────────────────────────────────────────────────
Lost to follow-up (n = ___ )          Lost to follow-up (n = ___ )
  (give reasons)                        (give reasons)

ANALYSIS
─────────────────────────────────────────────────
Analyzed (n = ___ )                   Analyzed (n = ___ )
  • Excluded from analysis (n = ___ )   • Excluded from analysis (n = ___ )
    (give reasons)                        (give reasons)

INTENTION-TO-TREAT
Primary analysis includes all randomized participants (n = 250)
```

**Checkpoint**: CONSORT template ready for completion during trial.

---

### Step 8.2: Plan CONSORT Checklist Compliance

**Action**: Review CONSORT 2010 checklist (30 items for parallel-group trials)

```bash
python code/consort_checklist.py --generate-template
```

**Key Items to Address in Protocol**:

```
Item 1: Title - "Randomized Controlled Trial" in title
Item 2: Abstract - Structured abstract with trial design
Item 3: Trial design - Parallel-group, 1:1 allocation
Item 4: Participants - Eligibility criteria clearly defined
Item 5: Interventions - Detailed description of MBCT and wait-list
Item 6: Outcomes - Primary (PHQ-9) and secondary outcomes specified
Item 7: Sample size - Power analysis documented
Item 8: Randomization - Sequence generation and allocation concealment
Item 9: Blinding - Who is blinded, how maintained
Item 10: Statistical methods - ANCOVA, ITT, missing data handling

... [Items 11-30 will be completed after trial completion] ...
```

**Checkpoint**: Protocol addresses all applicable CONSORT items for planning.

---

## Summary and Next Steps

### What You've Learned

**Completed RCT Design**:
- Formulated testable research question (FINER criteria)
- Converted to PICOS format
- Conducted NIH-compliant power analysis (n=250)
- Generated reproducible randomization sequence (block randomization)
- Implemented allocation concealment (REDCap central randomization)
- Planned blinding procedures (single-blind, outcome assessors)
- Wrote CONSORT-compliant protocol (30 pages)
- Addressed sex as biological variable (SABV)
- Pre-registered on ClinicalTrials.gov and OSF
- Used experiment-designer agent for rigor review
- Planned CONSORT flow diagram and checklist compliance

**Key Files Generated**:
```
my_mbct_trial/
├── docs/
│   ├── trial_protocol_v1.1.docx (30 pages, IRB-ready)
│   ├── power_analysis_report.pdf
│   ├── randomization_protocol.pdf
│   ├── sabv_plan.yaml
│   └── consort_flow_template.md
├── data/
│   └── randomization_sequence_SEALED.csv (encrypted)
└── code/
    ├── power_analysis.py
    ├── randomization.py
    └── generate_protocol.py
```

---

### NIH Rigor Compliance Verified

```
═══════════════════════════════════════════════
         NIH RIGOR CHECKLIST - FINAL
═══════════════════════════════════════════════

Scientific Premise: Gap identified from systematic review (Tutorial 2)
Rigorous Experimental Design: RCT with proper randomization and blinding
Consideration of Sex: SABV plan addresses enrollment and analysis
Authentication of Key Resources: Validated outcome measures (PHQ-9, GAD-7)
Transparent Reporting: Pre-registered, CONSORT compliance planned
Statistical Analysis: Pre-specified, power justified, missing data handled

RIGOR SCORE: EXCELLENT
Ready for NIH grant submission or IRB approval.
```

---

### Next Steps (After IRB Approval)

1. **Recruit Participants**
   - Post study flyer on campus
   - Contact student health services
   - Social media recruitment

2. **Enroll and Randomize**
   - Screen eligibility
   - Obtain informed consent
   - Randomize via REDCap

3. **Conduct Trial**
   - Deliver MBCT modules
   - Monitor engagement
   - Collect outcome data

4. **Analyze Data**
   - Follow pre-registered analysis plan
   - Conduct ITT analysis
   - Sensitivity analyses

5. **Report Results**
   - Complete CONSORT flow diagram
   - Write manuscript following CONSORT guidelines
   - Share de-identified data on OSF

**See**: Tutorial 5 (Complete Workflow) for data analysis and manuscript writing.

---

### Using Experiment-Designer Agent Effectively

**Best Practices**:

1. **Early Consultation**: Engage agent during design phase, not after enrollment
2. **Provide Context**: Share research question, constraints, resources
3. **Iterate**: Revise protocol based on agent feedback
4. **Verify**: Double-check agent recommendations against NIH/CONSORT guidelines
5. **Document**: Save all agent interactions for audit trail

**Example Advanced Prompt**:

```
/agent experiment-designer

I'm designing an RCT with these constraints:
- Budget: $50,000
- Timeline: 12 months recruitment + 6 months follow-up
- Population: College students (local university, 15,000 enrollment)
- Intervention: 8-week online program

Expected effect: d = 0.40
Desired power: 0.80

Please help me determine:
1. Is this feasible?
2. What's the optimal sample size given budget?
3. Should I use wait-list or active control?
4. How do I minimize attrition?
```

---

### Troubleshooting

**Problem**: Sample size too large for budget/timeline

**Solution**:
1. Consider more efficient designs (e.g., within-subjects, crossover)
2. Seek larger effect (stronger intervention, more severe population)
3. Accept lower power (0.70 instead of 0.80) with justification
4. Seek additional funding

---

**Problem**: Cannot blind participants (behavioral intervention)

**Solution**:
1. Use objective outcomes (physiological measures, behavioral observations)
2. Blind outcome assessors and data analysts
3. Use active control (attention-matched) instead of wait-list
4. Pre-register all analyses to prevent bias

---

**Problem**: Randomization sequence gets broken (researcher sees assignments)

**Solution**:
1. Re-generate new sequence with different seed
2. Exclude participants already enrolled (analyze separately)
3. Document deviation in CONSORT diagram
4. Consider implications for internal validity

---

### Additional Resources

**NIH Rigor and Reproducibility**:
- Guidelines: https://grants.nih.gov/policy/reproducibility/guidance.htm
- SABV Policy: https://orwh.od.nih.gov/sex-gender/nih-policy-sex-biological-variable

**CONSORT Statement**:
- Checklist: http://www.consort-statement.org/consort-2010
- Extensions: http://www.consort-statement.org/extensions (for specific trial types)

**Trial Registration**:
- ClinicalTrials.gov: https://clinicaltrials.gov/ct2/manage-recs/how-register
- OSF Registries: https://osf.io/registries
- WHO Registry Network: https://www.who.int/clinical-trials-registry-platform

---

**Tutorial Complete!** You now know how to design a rigorous RCT from research question to registered protocol, meeting NIH and CONSORT standards.

**Next**: Tutorial 5 (Complete Workflow) for end-to-end project from idea to publication.
