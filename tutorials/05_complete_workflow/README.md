# Tutorial 5: Complete Research Workflow (Idea → Publication)

**Duration**: 60 minutes
**Prerequisites**: Tutorials 1, 2, 3, 4 completed
**What you'll learn**: End-to-end research project from gap identification to publication, combining systematic review, RCT design, data analysis, manuscript writing, and archival

---

## Overview

This capstone tutorial demonstrates a **complete research workflow** that integrates everything you've learned:

1. **Gap Identification** (from Tutorial 2: Systematic Review)
2. **RCT Design** (from Tutorial 3: Experimental Design)
3. **Data Collection** and quality monitoring
4. **Statistical Analysis** with pre-registered plan
5. **Meta-Analysis** basics (forest plots, heterogeneity)
6. **Manuscript Writing** (from Tutorial 4: AI-Check)
7. **Data/Code Sharing** on OSF
8. **Archival** and DOI generation

**Running Example**: We'll complete a full research project:
- **Systematic Review** (Tutorial 2): Mindfulness for adolescent anxiety
- **Gap Identified**: Limited evidence for online delivery
- **RCT** (Tutorial 3): Online MBCT for college student depression
- **Analysis**: Data analysis and meta-analysis
- **Publication**: CONSORT-compliant manuscript

**Timeline**: This tutorial shows a realistic 18-24 month research project compressed into 60 minutes.

---

## Part 1: From Systematic Review to Research Gap (10 minutes)

### Step 1.1: Review Systematic Review Results

From Tutorial 2, we completed a systematic review on mindfulness for adolescent anxiety.

**Key Findings from Our Review**:

```
═══════════════════════════════════════════════
  SYSTEMATIC REVIEW RESULTS (Tutorial 2)
═══════════════════════════════════════════════

Question: Do mindfulness interventions reduce anxiety in adolescents?

Studies Included: 43 RCTs
Total Participants: 5,247

Primary Outcome: Anxiety symptom reduction

Meta-Analysis Results:
─────────────────────────────────────────────────
Pooled Effect Size: SMD = -0.42 (95% CI: -0.58 to -0.26)
Interpretation: Moderate reduction in anxiety symptoms
p-value: <0.001
Heterogeneity: I² = 64% (substantial heterogeneity)

Conclusion: Mindfulness-based interventions are moderately effective for
reducing anxiety symptoms in adolescents.
```

**✓ Checkpoint**: We have strong evidence that mindfulness works for adolescents.

---

### Step 1.2: Conduct Subgroup Analysis to Identify Gaps

**Action**: Examine heterogeneity sources

```bash
# From Tutorial 2 systematic review data
cd ~/my_review

python code/subgroup_analysis.py \
  --input data/extraction/extracted_data.csv \
  --outcome anxiety_reduction \
  --moderators delivery_format age_group baseline_severity
```

**Subgroup Analysis Results**:

```
═══════════════════════════════════════════════
         SUBGROUP ANALYSIS - HETEROGENEITY
═══════════════════════════════════════════════

Moderator 1: Delivery Format
─────────────────────────────────────────────────
In-person (k=35):      SMD = -0.48 (95% CI: -0.62 to -0.34) | I² = 52%
Online (k=8):          SMD = -0.22 (95% CI: -0.45 to  0.01) | I² = 71%

Test of Moderation: Q = 5.42, p = 0.02
Interpretation: In-person delivery significantly more effective than online

GAP IDENTIFIED: Online delivery shows promise but:
  1. Fewer studies (8 vs. 35)
  2. Larger heterogeneity (I² = 71%)
  3. Effect size not significant (CI crosses zero)
  4. Need more RCTs to establish efficacy

Moderator 2: Age Group
─────────────────────────────────────────────────
Early adolescence 12-14 (k=18):  SMD = -0.51 (95% CI: -0.71 to -0.31)
Late adolescence 15-18 (k=17):   SMD = -0.39 (95% CI: -0.58 to -0.20)
College age 18-25 (k=8):         SMD = -0.28 (95% CI: -0.52 to -0.04)

Test of Moderation: Q = 3.12, p = 0.21 (ns)
Interpretation: Effects slightly smaller for older adolescents/young adults

GAP IDENTIFIED: College students (18-25) underrepresented:
  - Only 8 studies (19% of total)
  - Smallest effect size
  - High mental health need in this population
  - More research needed

Moderator 3: Baseline Severity
─────────────────────────────────────────────────
Mild-moderate symptoms (k=29):  SMD = -0.35 (95% CI: -0.48 to -0.22)
Severe symptoms (k=14):         SMD = -0.58 (95% CI: -0.81 to -0.35)

Test of Moderation: Q = 4.87, p = 0.03
Interpretation: Larger effects for severe symptoms (floor effects for mild)
```

**✓ Checkpoint**: Multiple gaps identified - we'll focus on online delivery for college students.

---

### Step 1.3: Formulate Research Question Based on Gap

**Identified Gap**:
- Online mindfulness interventions for college students are understudied
- Only 8 studies, inconclusive results
- College mental health crisis demands scalable interventions

**Our New Research Question**:

> "Is an 8-week online mindfulness-based cognitive therapy (MBCT) program effective for reducing depressive symptoms in college students compared to a wait-list control?"

**Why This Fills the Gap**:
1. **Population**: College students (underrepresented)
2. **Delivery**: Online (needs more evidence)
3. **Outcome**: Depression (comorbid with anxiety, high prevalence)
4. **Design**: RCT (gold standard)

**✓ Checkpoint**: Research question directly addresses identified gap from systematic review.

---

## Part 2: RCT Design and Pre-Registration (10 minutes)

### Step 2.1: Complete RCT Design

**Action**: Use RCT template and workflow from Tutorial 3

```bash
# Copy RCT template
cp -r templates/rct_study college_mbct_trial
cd college_mbct_trial

# Run complete design workflow
bash workflow/design_rct.sh
```

**Workflow Executes**:
1. ✅ Power analysis (n=250, d=0.40, power=0.80)
2. ✅ Randomization sequence (block randomization, size 4)
3. ✅ Protocol generation (30-page CONSORT-compliant)
4. ✅ SABV plan (60% female, 40% male enrollment)
5. ✅ Pre-registration forms (ClinicalTrials.gov + OSF)

**Generated Files**:
- `docs/trial_protocol_v1.0.docx` (IRB-ready)
- `docs/power_analysis_report.pdf`
- `data/randomization_sequence_SEALED.csv`
- `docs/clinicaltrials_registration.xml`

**✓ Checkpoint**: Complete RCT design ready for IRB submission (from Tutorial 3).

---

### Step 2.2: Submit to IRB and Register Trial

**IRB Submission** (simulated - you would do this for real):

```bash
# Generate IRB application materials
python code/generate_irb_application.py \
  --protocol docs/trial_protocol_v1.0.docx \
  --consent docs/informed_consent_v1.0.docx \
  --output irb_application/
```

**Wait for IRB Approval**: ~4-8 weeks

**Register on ClinicalTrials.gov**:
```
Trial ID: NCT05234567 (example)
Registration Date: 2024-01-15
First Posted: 2024-01-18
```

**✓ Checkpoint**: IRB approved, trial registered before enrolling first participant.

---

## Part 3: Data Collection and Quality Monitoring (5 minutes)

### Step 3.1: Enroll Participants

**Recruitment Timeline** (simulated):
- Months 1-12: Rolling enrollment
- Target: 250 participants (125 per group)
- Actual enrolled: 268 (accounting for expected 7% screen failure)

**Real-Time Enrollment Monitoring**:

```bash
# Track enrollment progress
python code/monitor_enrollment.py \
  --target 250 \
  --current data/enrollment_log.csv \
  --output dashboard/enrollment_dashboard.html
```

**Enrollment Dashboard** (simulated week 30):

```
═══════════════════════════════════════════════
         ENROLLMENT PROGRESS - WEEK 30
═══════════════════════════════════════════════

Screened: 312
  ├─ Ineligible: 37 (12%)
  │   ├─ PHQ-9 too low (<10): 18
  │   ├─ PHQ-9 too high (≥20): 11
  │   ├─ Current psychotherapy: 6
  │   └─ Other: 2
  ├─ Declined: 7 (2%)
  └─ ENROLLED: 268 (86%)

Randomized:
  ├─ MBCT: 134 (50%)
  └─ Wait-List: 134 (50%)

Sex Distribution:
  ├─ Female: 162 (60%) ✓ On target
  └─ Male: 106 (40%)   ✓ On target

Timeline:
  ├─ Target enrollment: 250
  ├─ Actual enrolled: 268 (107% of target) ✓
  └─ Weeks remaining: 22 weeks until primary endpoint

Projected Final N (accounting for 20% attrition):
  ├─ MBCT: 107 completers
  ├─ Wait-List: 107 completers
  └─ Total: 214 (85% retention) ✓ Adequate power
```

**✓ Checkpoint**: Enrollment on track, randomization balanced, sex distribution as planned.

---

### Step 3.2: Monitor Data Quality

**Real-Time Quality Checks**:

```bash
# Automated weekly data quality reports
python code/data_quality_checks.py \
  --data data/participant_data.csv \
  --schedule weekly \
  --email pi@university.edu
```

**Data Quality Report** (example week 35):

```
═══════════════════════════════════════════════
      DATA QUALITY REPORT - WEEK 35
═══════════════════════════════════════════════

Completeness:
  ├─ Baseline assessments: 268/268 (100%) ✓
  ├─ 8-week assessments: 182/218 due (83%) ✓
  └─ Engagement tracking: 268/268 (100%) ✓

Out-of-Range Values:
  ├─ PHQ-9 (0-27): 0 out-of-range ✓
  ├─ GAD-7 (0-21): 0 out-of-range ✓
  └─ Age (18-25): 0 out-of-range ✓

Missing Data Patterns:
  ├─ Random missingness: Yes ✓ (Little's MCAR test p=0.42)
  ├─ Differential attrition: No ✓ (MBCT 17%, Wait-List 18%, p=0.85)
  └─ Predictors of missingness: Baseline severity (OR=1.08, p=0.34)

Protocol Deviations:
  ├─ Randomization errors: 0 ✓
  ├─ Allocation concealment breaches: 0 ✓
  └─ Ineligible participants enrolled: 1 ⚠️
      (PHQ-9=9 at screen, 11 at baseline - retained per protocol)

Action Items:
  ✓ No critical issues
  ✓ Continue standard monitoring
```

**✓ Checkpoint**: Data quality excellent, no protocol violations.

---

## Part 4: Statistical Analysis (15 minutes)

### Step 4.1: Execute Pre-Registered Analysis Plan

**Timeline**: Month 18 (all participants completed 8-week primary endpoint)

**Action**: Run pre-specified statistical analysis

```bash
# Load pre-registered analysis plan from OSF
python code/run_preregistered_analysis.py \
  --osf-id abc123 \
  --data data/final_dataset_locked.csv \
  --output results/primary_analysis/
```

**What This Does**:
1. Locks dataset (no further changes allowed)
2. Loads exact analysis code from OSF pre-registration
3. Executes all pre-specified analyses
4. Generates structured results with 95% CIs
5. Creates publication-ready tables and figures

---

### Step 4.2: Primary Analysis Results

**Analysis**: ANCOVA (8-week PHQ-9 adjusted for baseline)

```
═══════════════════════════════════════════════
           PRIMARY ANALYSIS RESULTS
═══════════════════════════════════════════════

Model: PHQ9_8wk ~ group + PHQ9_baseline + sex

Sample:
  ├─ MBCT: 107 analyzed (134 randomized, 27 lost to follow-up)
  ├─ Wait-List: 107 analyzed (134 randomized, 27 lost to follow-up)
  └─ Total: 214 analyzed (268 randomized, 20% attrition as expected)

Baseline Characteristics (Table 1):
─────────────────────────────────────────────────
                      MBCT (n=107)    Wait-List (n=107)
Age (years)           20.3 (1.8)      20.1 (1.7)
Female (%)            64 (60%)        65 (61%)
PHQ-9 Baseline        14.2 (2.8)      14.4 (2.7)

Between-group differences at baseline: All p > 0.05 ✓

Primary Outcome (PHQ-9 at 8 weeks):
─────────────────────────────────────────────────
MBCT Group:
  ├─ Baseline Mean: 14.2 (SD=2.8)
  ├─ 8-week Mean: 9.1 (SD=4.2)
  └─ Change: -5.1 points

Wait-List Group:
  ├─ Baseline Mean: 14.4 (SD=2.7)
  ├─ 8-week Mean: 12.3 (SD=3.8)
  └─ Change: -2.1 points

Between-Group Difference (ANCOVA):
─────────────────────────────────────────────────
Adjusted Mean Difference: -3.2 points (95% CI: -4.5 to -1.9)
Cohen's d: 0.68 (95% CI: 0.41 to 0.95)
p-value: <0.001

Interpretation:
MBCT group improved 3.2 points more than wait-list on PHQ-9 (0-27 scale),
representing a MODERATE-TO-LARGE effect. This exceeds the minimally clinically
important difference (MCID = 2.5 points for PHQ-9).

Effect Size Realized: d = 0.68 (expected d = 0.40)
Study was OVERPOWERED - actual power achieved = 0.96
```

**✓ Checkpoint**: Primary outcome shows statistically and clinically significant benefit.

---

### Step 4.3: Secondary Analyses

**Action**: Analyze pre-specified secondary outcomes

```
Secondary Outcomes (8 weeks, ANCOVA adjusted for baseline):
═══════════════════════════════════════════════

1. Anxiety Symptoms (GAD-7):
   ├─ Adjusted Difference: -2.4 points (95% CI: -3.6 to -1.2)
   ├─ p-value: <0.001
   └─ Interpretation: MBCT reduces anxiety (secondary benefit)

2. Mindfulness (FFMQ total score):
   ├─ Adjusted Difference: +8.3 points (95% CI: 5.1 to 11.5)
   ├─ p-value: <0.001
   └─ Interpretation: MBCT increases mindfulness (mechanism confirmed)

3. Functional Impairment (SDS):
   ├─ Adjusted Difference: -1.2 points (95% CI: -2.3 to -0.1)
   ├─ p-value: 0.04
   └─ Interpretation: MBCT improves functioning (small effect)

Multiple Comparisons Adjustment (Holm-Bonferroni):
All secondary outcomes remain significant after adjustment.
```

**✓ Checkpoint**: All secondary outcomes favor MBCT.

---

### Step 4.4: Sensitivity Analyses

**Pre-Registered Sensitivity Analyses**:

```bash
python code/sensitivity_analyses.py \
  --data data/final_dataset_locked.csv \
  --output results/sensitivity/
```

**Results**:

```
Sensitivity Analysis 1: Complete Case Analysis
─────────────────────────────────────────────────
(No imputation for missing data, n=214 completers only)

Effect: d = 0.68 (95% CI: 0.41 to 0.95), p<0.001
Same as primary analysis (ITT with multiple imputation)
Conclusion: Results robust to missing data assumptions ✓

Sensitivity Analysis 2: Per-Protocol Analysis
─────────────────────────────────────────────────
(Only participants who completed ≥6 of 8 MBCT modules, n=89 in MBCT group)

Effect: d = 0.82 (95% CI: 0.51 to 1.13), p<0.001
Larger effect (dose-response relationship)
Conclusion: MBCT more effective when fully engaged ✓

Sensitivity Analysis 3: Baseline-Adjusted Change Scores
─────────────────────────────────────────────────
(Difference-in-differences analysis)

Effect: d = 0.65 (95% CI: 0.38 to 0.92), p<0.001
Nearly identical to ANCOVA
Conclusion: Analytic method doesn't materially affect results ✓

Sensitivity Analysis 4: Excluding High Attrition Sites
─────────────────────────────────────────────────
(One recruitment source had 35% attrition vs. 15% overall)

Effect: d = 0.71 (95% CI: 0.42 to 1.00), p<0.001
Slightly larger effect
Conclusion: Results not driven by differential attrition ✓

═══════════════════════════════════════════════
CONCLUSION: Results are ROBUST across all sensitivity analyses.
═══════════════════════════════════════════════
```

**✓ Checkpoint**: All sensitivity analyses confirm primary finding.

---

## Part 5: Meta-Analysis Update (10 minutes)

### Step 5.1: Combine Our RCT with Systematic Review

Now we'll update the meta-analysis from Tutorial 2 by adding our new RCT results.

**Action**: Add our study to the meta-analysis dataset

```bash
# Add our RCT to the systematic review data
cd ~/my_review

python code/add_new_study.py \
  --meta-data data/extraction/extracted_data.csv \
  --new-study ../college_mbct_trial/results/primary_analysis/study_data.json \
  --output data/extraction/extracted_data_updated.csv
```

---

### Step 5.2: Re-Run Meta-Analysis with Updated Dataset

```bash
python code/meta_analysis.py \
  --input data/extraction/extracted_data_updated.csv \
  --outcome anxiety_depression_combined \
  --subgroup delivery_format \
  --output results/meta_analysis_updated/
```

**Updated Meta-Analysis Results**:

```
═══════════════════════════════════════════════
     META-ANALYSIS (UPDATED WITH OUR RCT)
═══════════════════════════════════════════════

Question: Do mindfulness interventions reduce anxiety/depression in adolescents/
young adults?

Studies Included: 44 RCTs (was 43, +1 our study)
Total Participants: 5,461 (was 5,247, +214)

Overall Pooled Effect:
─────────────────────────────────────────────────
SMD = -0.44 (95% CI: -0.59 to -0.29)
Previous: SMD = -0.42 (95% CI: -0.58 to -0.26)

Change: +0.02 (stronger effect with our study included)
Heterogeneity: I² = 62% (was 64%, slightly reduced)

Subgroup: Online Delivery
─────────────────────────────────────────────────
PREVIOUS (8 studies, Tutorial 2):
  SMD = -0.22 (95% CI: -0.45 to 0.01), p = 0.06 (ns)
  I² = 71%

UPDATED (9 studies, with our RCT):
  SMD = -0.35 (95% CI: -0.54 to -0.16), p < 0.001 ✓
  I² = 58% (reduced heterogeneity)

Impact of Our Study:
  ✓ Online delivery NOW SHOWS SIGNIFICANT BENEFIT
  ✓ Confidence interval no longer crosses zero
  ✓ Heterogeneity reduced (more consistent findings)
  ✓ GAP FILLED

Test of Moderation (In-Person vs. Online):
─────────────────────────────────────────────────
In-person (k=35): SMD = -0.48 (95% CI: -0.62 to -0.34)
Online (k=9):     SMD = -0.35 (95% CI: -0.54 to -0.16)

Q = 1.82, p = 0.18 (ns)
Interpretation: Difference between in-person and online is NO LONGER significant
                (was p=0.02 in Tutorial 2)
                
CONCLUSION: Our RCT provides evidence that online delivery is comparably
            effective to in-person delivery.
```

**✓ Checkpoint**: Our RCT filled the identified gap and changed the meta-analytic conclusion.

---

### Step 5.3: Generate Forest Plot

**Action**: Create publication-ready forest plot

```bash
python code/forest_plot.py \
  --input data/extraction/extracted_data_updated.csv \
  --subgroup delivery_format \
  --highlight-study "Present Study (2024)" \
  --output results/figures/forest_plot_updated.png
```

**Forest Plot** (conceptual representation):

```
═══════════════════════════════════════════════
         FOREST PLOT - ONLINE DELIVERY
═══════════════════════════════════════════════

Study                        N     SMD (95% CI)         Weight
───────────────────────────────────────────────────────────────
Smith 2018                  120   -0.15 (-0.51, 0.21)   8.2%
Jones 2019                   80   -0.42 (-0.86, 0.02)   5.1%
Brown 2020                  156   -0.28 (-0.59, 0.03)  11.3%
Lee 2021                     92   -0.09 (-0.50, 0.32)   6.4%
Garcia 2021                 134   -0.51 (-0.85, -0.17) 10.1%
Taylor 2022                  78   -0.18 (-0.62, 0.26)   4.9%
Wilson 2023                 145   -0.37 (-0.69, -0.05) 10.8%
Chen 2023                   108   -0.29 (-0.67, 0.09)   7.4%
Present Study (2024)  ◄─── 214   -0.68 (-0.95, -0.41) 35.8% ◄── LARGEST
───────────────────────────────────────────────────────────────
Overall (Random Effects)         -0.35 (-0.54, -0.16)

                     -1.0    -0.5    0.0    0.5    1.0
                     ◄─────────┼─────────┼─────────┼─────────►
                     Favors         No          Favors
                     MBCT       Difference     Control

Heterogeneity: I² = 58%, Q = 19.2, p = 0.01
```

**Key Observations**:
- Our study has largest weight (35.8%) due to large sample size (n=214)
- Our effect (d=-0.68) is largest among online studies
- Pulls overall estimate toward stronger benefit
- Reduced heterogeneity by providing clearer signal

**✓ Checkpoint**: Forest plot ready for manuscript Figure 1.

---

## Part 6: Manuscript Writing (10 minutes)

### Step 6.1: Use Manuscript-Writer Agent

**Action**: Invoke agent to draft CONSORT-compliant manuscript

```
/agent manuscript-writer

I've completed an RCT on online MBCT for college student depression. Please
help me write a CONSORT-compliant manuscript.

Study Details:
- Design: Parallel-group RCT, 1:1 allocation
- N: 268 randomized (214 analyzed, 20% attrition)
- Intervention: 8-week online MBCT vs. wait-list
- Primary outcome: PHQ-9 at 8 weeks
- Result: Adjusted difference -3.2 points (95% CI: -4.5 to -1.9), d=0.68, p<0.001
- Registration: ClinicalTrials.gov NCT05234567

Please draft:
1. Structured abstract (CONSORT style)
2. Introduction (background, gap from systematic review, objectives)
3. Methods (CONSORT-compliant, all 25 items)
4. Results (with CONSORT flow diagram)
5. Discussion (interpretation, generalizability, limitations)

Target journal: JAMA Psychiatry
Word limit: 3,500 words (excluding abstract, tables, figures)
```

---

**Agent Response**: Drafts complete manuscript (excerpt):

```markdown
# Online Mindfulness-Based Cognitive Therapy for College Student Depression: 
# A Randomized Clinical Trial

## ABSTRACT

**Importance**: Depression is prevalent among college students, but scalable
evidence-based interventions are limited.

**Objective**: To determine whether an 8-week online mindfulness-based cognitive
therapy (MBCT) program reduces depressive symptoms in college students compared
with a wait-list control.

**Design, Setting, and Participants**: Parallel-group randomized clinical trial
conducted at a large public university from January 2024 to June 2024. Participants
were college students aged 18-25 years with mild-to-moderate depressive symptoms
(Patient Health Questionnaire-9 [PHQ-9] score 10-19). Of 312 assessed, 268 were
randomized.

**Interventions**: Participants were randomized 1:1 to receive 8-week online MBCT
(n=134) or wait-list control (n=134).

**Main Outcomes and Measures**: Primary outcome was change in PHQ-9 score from
baseline to 8 weeks. Secondary outcomes included anxiety (GAD-7), mindfulness
(FFMQ), and functional impairment (SDS).

**Results**: Of 268 randomized participants (mean age, 20.2 years; 129 [60%] female),
214 (80%) completed the 8-week assessment. MBCT participants showed greater
reduction in PHQ-9 scores (baseline mean, 14.2; 8-week mean, 9.1) compared with
wait-list (baseline mean, 14.4; 8-week mean, 12.3), with an adjusted between-group
difference of -3.2 points (95% CI, -4.5 to -1.9; Cohen d=0.68; P<.001). Similar
benefits were observed for anxiety (adjusted difference, -2.4; 95% CI, -3.6 to -1.2;
P<.001) and mindfulness (adjusted difference, 8.3; 95% CI, 5.1 to 11.5; P<.001).

**Conclusions and Relevance**: Among college students with mild-to-moderate depressive
symptoms, an 8-week online MBCT program, compared with wait-list control, resulted
in significantly greater reduction in depressive symptoms. These findings support
online MBCT as a scalable intervention for college mental health services.

**Trial Registration**: ClinicalTrials.gov Identifier: NCT05234567

[Methods, Results, Discussion sections follow with full CONSORT compliance...]
```

**✓ Checkpoint**: Draft manuscript generated by agent (3,487 words, within limit).

---

### Step 6.2: Run AI-Check on Manuscript

**Action**: Use AI-check skill (from Tutorial 4) to ensure human-written quality

```bash
python tools/ai_check.py \
  --input manuscript_draft_v1.docx \
  --output ai_check_report.json \
  --profile docs/writing_profile.json
```

**AI-Check Results**:

```
═══════════════════════════════════════════════
        AI-CHECK REPORT - MANUSCRIPT
═══════════════════════════════════════════════

Overall AI Confidence: 12% (LOW - likely human-written) ✓

Section-by-Section Analysis:
─────────────────────────────────────────────────
Abstract: 8% AI confidence ✓
  - Natural sentence variation
  - Appropriate use of transition words
  - No AI-typical phrases

Introduction: 15% AI confidence ✓
  - Good complexity variance
  - Citations distributed naturally
  - No generic frames

Methods: 6% AI confidence ✓
  - Technical precision (expected for Methods)
  - Appropriate complexity
  - No uniformity flags

Results: 4% AI confidence ✓
  - Data-driven content (naturally structured)
  - Statistical reporting (standard format)

Discussion: 18% AI confidence ⚠️
  - Some generic phrases detected:
    • "these findings suggest" (line 287)
    • "importantly, this study demonstrates" (line 314)
  - Recommendation: Vary transition phrases

Suggested Revisions:
─────────────────────────────────────────────────
1. Line 287: "these findings suggest" → "our results indicate"
2. Line 314: "importantly, this study demonstrates" → "notably, we found"
3. Add 2-3 shorter sentences in Discussion (complexity variance)

After Revisions, Projected AI Confidence: 8% ✓
```

**Action**: Apply AI-check suggestions

```bash
# Agent re-drafts Discussion with suggestions
/agent manuscript-writer

Please revise the Discussion section to address these AI-check flagged phrases:
[Paste AI-check suggestions]
```

**✓ Checkpoint**: Manuscript revised, AI-check confidence now 8% (excellent).

---

## Part 7: Data and Code Sharing (5 minutes)

### Step 7.1: Prepare Data for Sharing

**Action**: De-identify dataset and create data dictionary

```bash
python code/prepare_data_sharing.py \
  --input data/final_dataset_locked.csv \
  --remove-identifiers participant_id email consent_date \
  --output data_sharing/deidentified_data.csv \
  --dictionary data_sharing/data_dictionary.csv
```

**Data Dictionary** (excerpt):

```csv
variable,description,type,range,coding
group,Treatment group assignment,categorical,MBCT or WaitList,1=MBCT 0=WaitList
age,Age in years,continuous,18-25,
sex,Biological sex,categorical,M or F,1=Female 0=Male
phq9_baseline,PHQ-9 score at baseline,continuous,0-27,higher=more depressed
phq9_8wk,PHQ-9 score at 8 weeks,continuous,0-27,higher=more depressed
```

**✓ Checkpoint**: De-identified data and dictionary ready for public sharing.

---

### Step 7.2: Upload to OSF

**Action**: Create OSF project and upload all materials

```bash
# OSF CLI upload
osf upload data_sharing/deidentified_data.csv \
  --project abc123 \
  --public

osf upload data_sharing/data_dictionary.csv \
  --project abc123 \
  --public

osf upload code/analysis/primary_analysis.R \
  --project abc123 \
  --public

osf upload docs/trial_protocol_v1.0.pdf \
  --project abc123 \
  --public
```

**OSF Project Structure**:

```
OSF Project: "Online MBCT for College Student Depression RCT"
https://osf.io/abc123/

├── Data/
│   ├── deidentified_data.csv (public)
│   └── data_dictionary.csv (public)
├── Code/
│   ├── primary_analysis.R (public)
│   ├── sensitivity_analyses.R (public)
│   └── README.md (analysis instructions)
├── Protocol/
│   ├── trial_protocol_v1.0.pdf (public)
│   └── statistical_analysis_plan.pdf (public)
└── Results/
    ├── consort_flow_diagram.pdf (public)
    └── forest_plot.png (public)

License: CC-BY 4.0 (all materials open access)
```

**✓ Checkpoint**: All materials publicly available on OSF.

---

### Step 7.3: Generate DOI

**Action**: Mint DOI for permanent archival

```bash
osf generate-doi --project abc123
```

**Result**:

```
DOI Generated: 10.17605/OSF.IO/ABC123

Permanent Link: https://doi.org/10.17605/OSF.IO/ABC123

This DOI can now be cited in your manuscript's Data Availability statement:

"De-identified participant data, analysis code, and study protocol are publicly
available at https://doi.org/10.17605/OSF.IO/ABC123"
```

**✓ Checkpoint**: DOI minted, data permanently archived.

---

## Part 8: Manuscript Submission (5 minutes)

### Step 8.1: CONSORT Checklist Verification

**Action**: Verify all 25 CONSORT items addressed

```bash
python code/consort_checklist.py \
  --manuscript manuscript_final_v2.docx \
  --verify-compliance \
  --output consort_verification.pdf
```

**CONSORT Compliance Report**:

```
═══════════════════════════════════════════════
    CONSORT 2010 CHECKLIST - FINAL MANUSCRIPT
═══════════════════════════════════════════════

✅ Item 1a: Title - "Randomized Clinical Trial" in title
✅ Item 1b: Abstract - Structured abstract with CONSORT elements
✅ Item 2a: Introduction - Background and rationale
✅ Item 2b: Objectives - Specific hypothesis stated
✅ Item 3a: Trial design - Parallel-group RCT clearly stated
✅ Item 3b: Important changes - Protocol v1.0 → v1.1 documented
✅ Item 4a: Participants - Eligibility criteria specified
✅ Item 4b: Settings and locations - University setting described
✅ Item 5: Interventions - MBCT and wait-list described in detail
✅ Item 6a: Outcomes - Primary and secondary outcomes defined
✅ Item 6b: Changes to outcomes - No changes (pre-registered)
✅ Item 7a: Sample size - Power analysis justification provided
✅ Item 7b: Interim analyses - None conducted (as pre-specified)
✅ Item 8a: Randomization - Sequence generation method described
✅ Item 8b: Allocation concealment - REDCap central randomization
✅ Item 9: Implementation - Who generated, enrolled, assigned
✅ Item 10: Blinding - Single-blind (outcome assessors)
✅ Item 11a: Statistical methods - ANCOVA pre-specified
✅ Item 11b: Subgroup analyses - Sex interaction (exploratory)
✅ Item 12a: Participant flow - CONSORT diagram included (Figure 1)
✅ Item 12b: Losses and exclusions - All documented with reasons
✅ Item 13a: Baseline characteristics - Table 1 provided
✅ Item 13b: Numbers analyzed - ITT analysis (all 268 randomized)
✅ Item 14a: Outcomes - All pre-specified outcomes reported
✅ Item 14b: Binary outcomes - N/A (continuous outcomes)
✅ Item 15: Ancillary analyses - Sensitivity analyses reported
✅ Item 16: Harms - Adverse events monitored (Table S2)
✅ Item 17a: Interpretation - Consistent with results
✅ Item 17b: Generalizability - External validity discussed
✅ Item 18: Limitations - Addressed in Discussion
✅ Item 19: Trial registration - NCT05234567 provided
✅ Item 20: Protocol access - Available on OSF
✅ Item 21: Funding - NIMH grant acknowledged

═══════════════════════════════════════════════
CONSORT COMPLIANCE: 25/25 items (100%) ✓
READY FOR SUBMISSION
═══════════════════════════════════════════════
```

**✓ Checkpoint**: Full CONSORT compliance verified.

---

### Step 8.2: Submit to Journal

**Action**: Prepare submission package for JAMA Psychiatry

**Submission Materials**:

```
Submission Package:
├── Cover Letter (1 page)
├── Manuscript (3,487 words)
│   ├── Title Page
│   ├── Abstract (349 words)
│   ├── Main Text
│   └── References (43 citations)
├── Tables (3)
│   ├── Table 1: Baseline Characteristics
│   ├── Table 2: Primary and Secondary Outcomes
│   └── Table S1: Sensitivity Analyses (supplemental)
├── Figures (2)
│   ├── Figure 1: CONSORT Flow Diagram
│   └── Figure 2: Forest Plot (updated meta-analysis)
├── Supplemental Materials
│   ├── Trial Protocol (30 pages)
│   ├── Statistical Analysis Plan (8 pages)
│   ├── CONSORT Checklist (completed)
│   └── Data Availability Statement
└── Author Contributions (CRediT)
```

**Data Availability Statement** (in manuscript):

```
Data Availability

De-identified participant-level data, full trial protocol, statistical analysis
plan, and analytic code are publicly available at https://doi.org/10.17605/OSF.IO/ABC123
under a Creative Commons Attribution 4.0 International License. Data will be
available indefinitely beginning upon publication. Additional information can be
obtained by contacting the corresponding author.
```

**✓ Checkpoint**: Submitted to JAMA Psychiatry on 2024-11-10.

---

## Summary: Complete Research Lifecycle

### What You've Accomplished (60 Minutes)

**Phase 1: Gap Identification (Months 1-6)**
- ✅ Conducted PRISMA 2020 systematic review (Tutorial 2)
- ✅ Identified research gap (online delivery for college students)
- ✅ Formulated research question filling that gap

**Phase 2: Study Design (Months 7-9)**
- ✅ Designed rigorous RCT (Tutorial 3)
- ✅ Conducted NIH-compliant power analysis (n=250)
- ✅ Generated reproducible randomization sequence
- ✅ Wrote CONSORT-compliant protocol
- ✅ Pre-registered on ClinicalTrials.gov and OSF

**Phase 3: Ethical Approval (Months 10-11)**
- ✅ Submitted to IRB
- ✅ Obtained approval
- ✅ Registered trial publicly

**Phase 4: Data Collection (Months 12-18)**
- ✅ Enrolled 268 participants (107% of target)
- ✅ Maintained 1:1 allocation balance
- ✅ Achieved 60F/40M sex distribution (SABV)
- ✅ Monitored data quality in real-time
- ✅ Achieved 80% retention (214/268)

**Phase 5: Data Analysis (Month 19)**
- ✅ Executed pre-registered analysis plan
- ✅ Primary outcome: d=0.68, p<0.001 (significant)
- ✅ All secondary outcomes significant
- ✅ Sensitivity analyses confirmed robustness

**Phase 6: Meta-Analysis Update (Month 20)**
- ✅ Added our RCT to systematic review data
- ✅ Updated meta-analysis (9 online studies)
- ✅ Changed conclusion: online delivery NOW effective
- ✅ Filled identified gap

**Phase 7: Manuscript Writing (Months 21-22)**
- ✅ Drafted CONSORT-compliant manuscript
- ✅ AI-checked for human quality (8% confidence)
- ✅ Verified 25/25 CONSORT items addressed

**Phase 8: Data Sharing & Publication (Month 23)**
- ✅ De-identified and shared data on OSF
- ✅ Minted DOI for permanent archival
- ✅ Submitted to JAMA Psychiatry

**Total Timeline**: 23 months from idea to submission

---

### Impact of Your Research

**Scientific Contribution**:
- Filled identified gap in literature
- Provided strongest evidence for online MBCT in college students
- Changed meta-analytic conclusion (online now effective)
- Largest study in subgroup (n=214, weight=35.8%)

**Clinical Significance**:
- Effect size (d=0.68) exceeds MCID
- Scalable intervention (online delivery)
- Addresses college mental health crisis
- Can be implemented at university counseling centers

**Methodological Rigor**:
- Pre-registered before data collection
- NIH rigor standards met (power, randomization, SABV)
- CONSORT 2010 compliant (25/25 items)
- Open data and code (reproducible)

---

### Research Lifecycle Best Practices

**1. Start with a Systematic Review** (Tutorial 2)
- Understand existing evidence
- Identify gaps systematically
- Justify new study

**2. Design Rigorously** (Tutorial 3)
- Pre-register before data collection
- Justify sample size with power analysis
- Plan for reproducibility

**3. Monitor Quality in Real-Time**
- Weekly data quality checks
- Track enrollment progress
- Document deviations

**4. Follow Pre-Registered Plan**
- No post-hoc analyses without disclosure
- Report all pre-specified outcomes
- Sensitivity analyses confirm robustness

**5. Share Data and Code**
- De-identify responsibly
- Public archival (OSF, Dataverse)
- Mint DOI for citability

**6. Report Transparently** (Tutorial 4 + AI-check)
- Follow reporting guidelines (CONSORT, PRISMA)
- Ensure human-written quality
- Acknowledge limitations

---

### Tools Used Throughout

**Research Assistant Plugin Skills**:
- `/agent literature-reviewer` (systematic review, screening)
- `/agent experiment-designer` (RCT design, NIH compliance)
- `/agent data-analyst` (statistical analysis, assumption checking)
- `/agent manuscript-writer` (CONSORT-compliant drafting)
- `/skill ai-check` (manuscript quality assurance)
- `/skill power-analysis` (sample size justification)
- `/skill effect-size` (Cohen's d calculation)
- `/skill prisma-diagram` (flow diagram generation)
- `/skill forest-plot` (meta-analysis visualization)
- `/skill citation-format` (reference management)

**Templates Used**:
- `templates/systematic_review/` (Tutorial 2)
- `templates/rct_study/` (Tutorial 3)

**Automation**:
- `code/power_analysis.py` (n=250 justification)
- `code/randomization.py` (reproducible sequence)
- `code/run_preregistered_analysis.py` (locked analysis)
- `code/meta_analysis.py` (updated forest plot)
- `code/consort_checklist.py` (compliance verification)

---

### Next Steps After Publication

**1. Dissemination**
- Present at conferences (e.g., ABCT, APA)
- Write plain-language summary for university news
- Share on social media (Twitter thread)
- Contact media relations office

**2. Implementation**
- Share MBCT program with university counseling centers
- Create training materials for counselors
- Develop implementation guide

**3. Future Research**
- Long-term follow-up (1-year outcomes)
- Mechanisms study (mindfulness as mediator)
- Effectiveness trial (real-world implementation)
- Cost-effectiveness analysis

**4. Replication**
- Encourage others to use OSF materials
- Multi-site replication study
- Different populations (community colleges, non-students)

---

## Conclusion

You've now completed an **entire research project lifecycle** from gap identification to publication. This workflow demonstrates:

- **Systematic approach**: Each phase builds on previous work
- **Rigor**: NIH and CONSORT standards met throughout
- **Reproducibility**: Pre-registration, open data, reproducible analysis
- **Impact**: Filled gap, changed meta-analytic conclusion
- **Efficiency**: Research Assistant tools automate repetitive tasks

**Congratulations!** You now have the skills to conduct publication-ready research from start to finish.

**For advanced workflows**, see:
- Tutorial 6 (coming soon): Multi-site collaborative trials
- Tutorial 7 (coming soon): Qualitative + quantitative mixed methods
- Tutorial 8 (coming soon): Grant proposal writing with budget justification

---

*Tutorial 5 Complete - You are now a Research Assistant power user!*
