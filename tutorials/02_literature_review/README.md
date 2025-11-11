# Tutorial 2: Conducting a Systematic Literature Review

**Duration**: 45 minutes
**Prerequisites**: Tutorial 1 completed, basic understanding of research questions
**What you'll learn**: Complete PRISMA 2020 workflow, multi-database searching, screening, data extraction, risk of bias assessment

---

## Overview

This tutorial walks you through conducting a complete systematic literature review following **PRISMA 2020 guidelines** (27-item checklist). You'll learn:

1. Protocol registration and research question formulation (PICOS)
2. Multi-database search strategy development
3. Search translation across databases
4. Deduplication process
5. Title/abstract screening
6. Full-text screening with exclusion tracking
7. Data extraction from included studies
8. Risk of bias assessment
9. PRISMA flow diagram generation
10. Using the `literature-reviewer` agent effectively

**Running Example**: We'll conduct a systematic review answering:
*"In adolescents with anxiety disorders, do mindfulness-based interventions compared to usual care reduce anxiety symptoms?"*

---

## Part 1: Protocol Registration (10 minutes)

### Why Register?

Protocol registration **before** conducting your review:
- Prevents outcome switching and cherry-picking
- Increases transparency
- Required by most journals
- Demonstrates rigor

**Platforms**: PROSPERO (health), OSF (all fields), Cochrane CENTRAL (RCTs)

---

### Step 1.1: Run Protocol Registration Tool

The systematic review template includes an interactive protocol builder.

**Action**:

```bash
# Copy the systematic review template
cp -r templates/systematic_review my_review
cd my_review

# Run protocol registration tool
python code/register_protocol.py
```

**✓ Checkpoint**: You should see an interactive prompt asking for PICOS components.

---

### Step 1.2: Complete PICOS Framework

The tool will guide you through defining:

**Interactive Prompts** (use our running example):

```
Research Question Topic: mindfulness interventions for adolescent anxiety

PICOS Components:
─────────────────────
Population: Adolescents (ages 12-18) with diagnosed anxiety disorders

Intervention/Exposure: Mindfulness-based interventions (MBSR, MBCT, mindfulness meditation)

Comparison: Usual care, waitlist control, or active control interventions

Outcome: Anxiety symptom reduction (measured by validated scales like GAD-7, SCARED, STAI-C)

Study design: Randomized controlled trials (RCTs)

Timeframe: Publications from 2010-2024 (last 14 years)

Language: English language publications

Exclusion criteria:
- Non-randomized studies
- Adult populations (18+)
- Mindfulness as part of multi-component intervention
- Conference abstracts without full text
```

**Generated Research Question**:

> In adolescents (ages 12-18) with diagnosed anxiety disorders, do mindfulness-based interventions (MBSR, MBCT) compared to usual care or active controls reduce anxiety symptoms as measured by validated scales?

**✓ Checkpoint**: The tool generates a protocol file at `docs/protocol.md` with all PICOS components.

---

### Step 1.3: Review Auto-Generated Protocol

**Action**: Open `docs/protocol.md`

```bash
cat docs/protocol.md
```

**Expected Sections**:
- Title
- Review team and affiliations
- Research question (PICOS)
- Background and rationale
- Objectives
- Eligibility criteria
- Search strategy (placeholder - we'll build this next)
- Study selection process
- Data extraction plan
- Risk of bias assessment method
- Data synthesis approach
- Timeline

**✓ Checkpoint**: Protocol should be 3-5 pages with all required sections.

---

### Step 1.4: Register on PROSPERO/OSF

The tool provides a pre-filled registration form.

**Action**:

```bash
# Generate PROSPERO registration form
python code/register_protocol.py --export prospero
# Output: prospero_registration.pdf

# OR generate OSF registration
python code/register_protocol.py --export osf
# Output: osf_registration.json (upload to osf.io)
```

**Manual Steps** (do this yourself):
1. Go to https://www.crd.york.ac.uk/prospero/ (PROSPERO) or https://osf.io (OSF)
2. Create account if needed
3. Upload generated registration form
4. Receive registration ID (e.g., CRD42024123456)

**✓ Checkpoint**: Add registration ID to `docs/protocol.md` header.

---

## Part 2: Search Strategy Development (10 minutes)

### Step 2.1: Build PubMed Search

We'll start with PubMed, then translate to other databases.

**Key Concepts**:
- **MeSH terms**: Controlled vocabulary (e.g., "Anxiety Disorders"[Mesh])
- **Text words**: Free text in title/abstract (e.g., anxiety[tiab])
- **Boolean operators**: AND, OR, NOT
- **Truncation**: `mindful*` matches mindful, mindfulness, mindfully

**Action**: Create `data/search_strategies/pubmed_search.txt`

```
# PubMed Search Strategy (2024-11-10)
# Database: PubMed via NCBI
# Date range: 2010/01/01 - 2024/12/31

#1 "Anxiety Disorders"[Mesh] OR anxiety[tiab] OR anxious[tiab] OR "generalized anxiety"[tiab] OR GAD[tiab]

#2 "Adolescent"[Mesh] OR adolescent*[tiab] OR teen*[tiab] OR youth[tiab] OR "high school"[tiab]

#3 "Mindfulness"[Mesh] OR mindfulness[tiab] OR "mindfulness based"[tiab] OR MBSR[tiab] OR MBCT[tiab] OR "mindfulness meditation"[tiab]

#4 "Randomized Controlled Trial"[Publication Type] OR randomized[tiab] OR randomised[tiab] OR RCT[tiab] OR "controlled trial"[tiab]

#5 #1 AND #2 AND #3 AND #4

#6 #5 AND 2010:2024[pdat] AND english[la]

Final: #6
```

**✓ Checkpoint**: Search strategy should combine all PICOS elements with Boolean logic.

---

### Step 2.2: Test Search in PubMed

**Action**: Copy the final search string and paste into PubMed:

```
("Anxiety Disorders"[Mesh] OR anxiety[tiab] OR anxious[tiab]) AND ("Adolescent"[Mesh] OR adolescent*[tiab] OR teen*[tiab]) AND ("Mindfulness"[Mesh] OR mindfulness[tiab] OR MBSR[tiab] OR MBCT[tiab]) AND ("Randomized Controlled Trial"[pt] OR randomized[tiab] OR RCT[tiab]) AND (2010:2024[pdat]) AND (english[la])
```

**Expected Results**: 150-300 records (if fewer than 50, search too narrow; if more than 1000, too broad)

**Save Results**:
1. Click "Send to" → "File" → "Format: CSV"
2. Save as `data/search_results/pubmed_results.csv`

**✓ Checkpoint**: CSV file should have columns: PMID, Title, Authors, Journal, Year, Abstract

---

### Step 2.3: Translate Search to Other Databases

Now we'll translate the PubMed search to Embase, Web of Science, and PsycINFO using the automated translation tool.

**Action**:

```bash
# Translate to Embase syntax
python code/search_translation.py \
  --input data/search_strategies/pubmed_search.txt \
  --from pubmed \
  --to embase \
  --output data/search_strategies/embase_search.txt
```

**What the Tool Does**:
- `[Mesh]` → `/exp` (Emtree terms)
- `[tiab]` → `:ab,ti` (abstract/title)
- `[pt]` → `:it` (publication type)
- Adjusts Boolean operator syntax

**✓ Checkpoint**: Generated Embase search at `data/search_strategies/embase_search.txt`

---

**Repeat for other databases**:

```bash
# Web of Science
python code/search_translation.py \
  --input data/search_strategies/pubmed_search.txt \
  --from pubmed \
  --to webofscience \
  --output data/search_strategies/wos_search.txt

# PsycINFO
python code/search_translation.py \
  --input data/search_strategies/pubmed_search.txt \
  --from pubmed \
  --to psycinfo \
  --output data/search_strategies/psycinfo_search.txt

# Scopus
python code/search_translation.py \
  --input data/search_strategies/pubmed_search.txt \
  --from pubmed \
  --to scopus \
  --output data/search_strategies/scopus_search.txt
```

**✓ Checkpoint**: You should have 5 search strategy files (PubMed + 4 translations).

---

### Step 2.4: Execute Searches Across Databases

**Manual Steps** (you do this):

1. **Embase** (via Ovid): https://ovidsp.ovid.com
   - Paste translated search
   - Export as RIS
   - Save as `data/search_results/embase_results.ris`

2. **Web of Science**: https://www.webofscience.com
   - Paste translated search
   - Export as "Full Record and Cited References" (Plain Text)
   - Save as `data/search_results/wos_results.txt`

3. **PsycINFO** (via EBSCOhost): https://search.ebscohost.com
   - Paste translated search
   - Export as RIS
   - Save as `data/search_results/psycinfo_results.ris`

4. **Scopus**: https://www.scopus.com
   - Paste translated search
   - Export as CSV
   - Save as `data/search_results/scopus_results.csv`

**✓ Checkpoint**: You should have 5 result files in `data/search_results/`

---

### Step 2.5: Document Search Metadata

**Action**: Create `data/search_results/search_log.csv`

```csv
database,search_date,records_retrieved,search_strategy_file,results_file
PubMed,2024-11-10,247,pubmed_search.txt,pubmed_results.csv
Embase,2024-11-10,312,embase_search.txt,embase_results.ris
Web of Science,2024-11-10,198,wos_search.txt,wos_results.txt
PsycINFO,2024-11-10,156,psycinfo_search.txt,psycinfo_results.ris
Scopus,2024-11-10,203,scopus_search.txt,scopus_results.csv
```

**Total Records**: 247 + 312 + 198 + 156 + 203 = **1,116 records**

**✓ Checkpoint**: Search log documents all databases, dates, and record counts.

---

## Part 3: Deduplication (5 minutes)

### Step 3.1: Combine All Search Results

**Action**: Convert all formats to standardized CSV

```bash
# Tool auto-converts RIS, TXT, CSV to unified format
python code/deduplicate.py \
  --input data/search_results/ \
  --output data/search_results/combined_results.csv
```

**What the Tool Does**:
- Parses RIS, BibTeX, CSV, plain text formats
- Extracts: Title, Authors, Year, DOI, Abstract, Source
- Standardizes to common format

**✓ Checkpoint**: `combined_results.csv` should have 1,116 rows.

---

### Step 3.2: Run Deduplication Algorithm

**Action**:

```bash
python code/deduplicate.py \
  --input data/search_results/combined_results.csv \
  --output data/search_results/deduplicated_results.csv \
  --report data/search_results/deduplication_report.txt
```

**Deduplication Algorithm**:
1. **Exact DOI match** (if DOI present)
2. **Fuzzy title match** (Levenshtein distance < 0.9)
3. **Author + year match** (same first author, same year)

**✓ Checkpoint**: Check the deduplication report:

```bash
cat data/search_results/deduplication_report.txt
```

**Expected Report**:

```
═══════════════════════════════════════════════
         DEDUPLICATION REPORT
═══════════════════════════════════════════════

Records before deduplication:  1,116
Duplicates removed:             342
Records after deduplication:    774

Deduplication methods:
  Exact DOI match:              218
  Fuzzy title match:            97
  Author + year match:          27

Final dataset: data/search_results/deduplicated_results.csv
```

**✓ Checkpoint**: Duplicates removed = ~30% (typical range 20-40%).

---

## Part 4: Title/Abstract Screening (10 minutes)

### Step 4.1: Set Up Screening Workflow

**Action**: Initialize screening dataset

```bash
python code/screening.py \
  --input data/search_results/deduplicated_results.csv \
  --output data/screening/title_abstract_screening.csv \
  --mode initialize
```

**Generated File**: `data/screening/title_abstract_screening.csv`

```csv
id,title,abstract,year,authors,source,reviewer1_decision,reviewer1_reason,reviewer2_decision,reviewer2_reason
1,"Mindfulness-Based Stress Reduction for Adolescents with Anxiety: A Randomized Trial","...",2022,"Smith J, Jones K","J Adolesc Health",,,,
2,"Effects of Meditation on Stress in College Students","...",2021,"Brown A","Stress Health",,,,
...
```

**✓ Checkpoint**: CSV should have 774 rows with blank decision columns.

---

### Step 4.2: Use Literature-Reviewer Agent for Screening

**Action**: Invoke the agent to help with screening decisions

```
/agent literature-reviewer

I'm screening 774 studies for my systematic review on mindfulness interventions
for adolescent anxiety. Can you help me apply the eligibility criteria?

Inclusion criteria:
- Adolescents ages 12-18
- Diagnosed anxiety disorder
- Mindfulness-based intervention (MBSR, MBCT)
- RCT design
- Anxiety outcome measured

I'll provide titles/abstracts one at a time for your assessment.
```

**Agent Response**:

```
I'll help you screen studies using your eligibility criteria. For each study,
I'll evaluate against your PICOS framework and provide:

1. Include/Exclude decision
2. Specific reason referencing eligibility criteria
3. Confidence level (high/medium/low)

Please provide the first title and abstract.
```

**✓ Checkpoint**: Agent should be ready to assist with screening decisions.

---

### Step 4.3: Screen First 10 Studies

**Action**: Provide studies to the agent

**Example Study 1**:

```
Title: "Mindfulness-Based Stress Reduction for Adolescents with Generalized
Anxiety Disorder: A Randomized Controlled Trial"

Abstract: "Background: Anxiety disorders are prevalent in adolescents. This
study evaluated MBSR effectiveness. Methods: 120 adolescents (ages 13-17) with
GAD were randomized to MBSR (n=60) or usual care (n=60). Primary outcome:
GAD-7 score at 8 weeks. Results: MBSR group showed significant reduction
(mean difference: -4.2 points, 95% CI: -6.1 to -2.3, p<0.001). Conclusion:
MBSR effective for adolescent anxiety."
```

**Agent Assessment**:

```
✅ INCLUDE - High Confidence

Rationale:
- Population: ✓ Adolescents ages 13-17 (within 12-18 range)
- Condition: ✓ Diagnosed GAD (anxiety disorder)
- Intervention: ✓ MBSR (mindfulness-based)
- Comparison: ✓ Usual care control
- Outcome: ✓ GAD-7 (validated anxiety measure)
- Design: ✓ RCT (randomized controlled trial explicitly stated)

All inclusion criteria met. No exclusion criteria triggered.
```

**Action**: Record decision in CSV

```csv
1,"Mindfulness-Based Stress Reduction for...","...",2022,"Smith J",include,All PICOS criteria met,,
```

---

**Example Study 2**:

```
Title: "Meditation and Yoga for Stress Reduction in High School Students"

Abstract: "We conducted a quasi-experimental study with 80 high school students
(ages 15-18) experiencing academic stress. Participants self-selected into
meditation/yoga (n=45) or no intervention (n=35). Stress levels measured by
Perceived Stress Scale at baseline and 12 weeks. Results showed 23% stress
reduction in intervention group (p=0.04)."
```

**Agent Assessment**:

```
❌ EXCLUDE - High Confidence

Rationale:
- Population: ✓ Adolescents ages 15-18
- Condition: ✗ "Academic stress" - not diagnosed anxiety disorder
- Intervention: ✓ Meditation component present
- Comparison: ✓ No intervention control
- Outcome: ✗ Perceived Stress Scale - not anxiety-specific
- Design: ✗ Quasi-experimental, not RCT (self-selection bias)

Fails 3 critical criteria: not diagnosed anxiety, not anxiety outcome, not RCT.
```

**Action**: Record exclusion

```csv
2,"Meditation and Yoga for Stress...","...",2021,"Brown A",exclude,Non-RCT design; no diagnosed anxiety disorder; stress not anxiety outcome,,
```

**✓ Checkpoint**: You should understand how to apply eligibility criteria systematically.

---

### Step 4.4: Complete Screening with Second Reviewer

**PRISMA Requirement**: At least 2 independent reviewers for validity.

**Action**: Simulate second reviewer using the agent in a new session

```
/agent literature-reviewer

I'm the second independent reviewer for a systematic review. I need to screen
the same 774 studies without seeing the first reviewer's decisions. Please
help me apply the eligibility criteria independently.

[Provide same studies as before]
```

**Calculate Inter-Rater Reliability**:

```bash
# After both reviewers complete screening
python code/screening.py \
  --input data/screening/title_abstract_screening.csv \
  --calculate-kappa
```

**Expected Output**:

```
═══════════════════════════════════════════════
    INTER-RATER RELIABILITY (Cohen's κ)
═══════════════════════════════════════════════

Reviewer 1 decisions: 774
Reviewer 2 decisions: 774

Agreement:
  Both include:   127
  Both exclude:   618
  Disagreement:    29

Cohen's κ = 0.82 (95% CI: 0.78-0.86)

Interpretation: Substantial agreement (κ > 0.6 acceptable for systematic reviews)

Conflicts requiring resolution: 29 studies
```

**✓ Checkpoint**: Cohen's κ should be > 0.6 (substantial agreement).

---

### Step 4.5: Resolve Conflicts

**Action**: Review the 29 conflicting decisions

```bash
python code/screening.py \
  --input data/screening/title_abstract_screening.csv \
  --show-conflicts
```

**Conflict Resolution Process**:
1. Both reviewers discuss rationale
2. Attempt consensus
3. If no consensus, third reviewer decides

**Use Agent as Third Reviewer**:

```
/agent literature-reviewer

I'm serving as the third reviewer to resolve conflicts between two reviewers.
Here's a study where Reviewer 1 included but Reviewer 2 excluded:

[Provide study details and both reviewers' reasoning]

Please provide your independent assessment and final decision.
```

**✓ Checkpoint**: All 774 studies should have final decisions (include/exclude).

---

### Step 4.6: Results After Title/Abstract Screening

**Final Counts**:
- Records screened: 774
- Records excluded: 643
- Records proceeding to full-text: 131

**✓ Checkpoint**: ~15-20% inclusion rate is typical for title/abstract screening.

---

## Part 5: Full-Text Screening (5 minutes)

### Step 5.1: Retrieve Full-Text Articles

**Action**: For the 131 included studies, obtain full PDFs

**Sources**:
1. PubMed Central (free full text)
2. University library access
3. Direct contact with authors (if needed)
4. Legal interlibrary loan

**Save PDFs**: `data/full_text_pdfs/`

**Track Retrieval**:

```csv
# data/screening/full_text_retrieval.csv
id,title,retrieval_status,source,date_retrieved,pdf_file
1,"Mindfulness-Based Stress Reduction for...",retrieved,PMC,2024-11-10,001_smith_2022.pdf
2,"MBCT for Adolescent GAD...",retrieved,university_library,2024-11-10,002_jones_2021.pdf
3,"Mindfulness Meditation RCT...",unable_to_retrieve,contacted_authors,2024-11-10,
...
```

**✓ Checkpoint**: Retrieved at least 95% of full texts (125+ out of 131).

---

### Step 5.2: Full-Text Screening

**Action**: Apply same eligibility criteria to full text

```bash
python code/screening.py \
  --input data/full_text_pdfs/ \
  --output data/screening/full_text_screening.csv \
  --mode full-text
```

**Common Exclusion Reasons at Full-Text Stage**:
- Intervention not purely mindfulness (multi-component)
- Outcomes not reported for adolescent subgroup
- Wrong study design (secondary analysis of RCT)
- Insufficient data for meta-analysis

**Example Full-Text Exclusion**:

```
Study: "Mindfulness for Anxiety Across Lifespan"
Decision: EXCLUDE
Reason: Data not reported separately for adolescent age group (12-18).
         Combined ages 12-25, unable to extract adolescent-specific outcomes.
```

**Final Counts**:
- Full-text articles assessed: 131
- Full-text articles excluded: 88
- Studies included in review: 43

**✓ Checkpoint**: ~30-40% of full texts typically excluded.

---

## Part 6: Data Extraction (5 minutes)

### Step 6.1: Create Data Extraction Form

**Action**: Define variables to extract from each study

```yaml
# data/extraction/extraction_form.yaml

study_characteristics:
  - study_id
  - first_author
  - publication_year
  - country
  - funding_source

participant_characteristics:
  - sample_size_total
  - sample_size_intervention
  - sample_size_control
  - mean_age
  - age_range
  - percent_female
  - anxiety_diagnosis_method
  - baseline_anxiety_severity

intervention_characteristics:
  - intervention_name
  - intervention_duration_weeks
  - session_frequency
  - session_length_minutes
  - delivery_format  # individual, group, online
  - mindfulness_components  # meditation, body scan, yoga, etc.

comparison_characteristics:
  - control_type  # usual care, waitlist, active control
  - control_description

outcome_data:
  - primary_outcome_measure  # GAD-7, SCARED, STAI-C, etc.
  - assessment_timepoint  # post-intervention, 3mo follow-up, etc.
  - intervention_mean_post
  - intervention_sd_post
  - control_mean_post
  - control_sd_post
  - between_group_difference
  - confidence_interval_95
  - p_value

risk_of_bias:
  - random_sequence_generation  # low/high/unclear
  - allocation_concealment
  - blinding_participants
  - blinding_outcome_assessment
  - incomplete_outcome_data
  - selective_reporting
```

**✓ Checkpoint**: Extraction form should capture all data needed for synthesis.

---

### Step 6.2: Extract Data from First Study

**Action**: Use literature-reviewer agent to assist

```
/agent literature-reviewer

I need to extract data from this RCT for my systematic review. Here's the study:

[Paste full text or provide PDF path]

Please extract the following information:
[Paste extraction form fields]
```

**Agent Response** (example):

```
Data Extraction: Smith et al. (2022)
───────────────────────────────────────────

Study Characteristics:
- Study ID: Smith_2022
- First Author: Smith, Jennifer
- Publication Year: 2022
- Country: United States
- Funding: NIMH Grant R01-MH123456

Participant Characteristics:
- Total N: 120
- Intervention N: 60
- Control N: 60
- Mean Age: 15.3 years (SD=1.4)
- Age Range: 13-17 years
- Female %: 58%
- Diagnosis: GAD diagnosed via K-SADS-PL interview
- Baseline GAD-7: Intervention M=14.2 (SD=3.1), Control M=14.5 (SD=2.9)

Intervention:
- Name: Mindfulness-Based Stress Reduction (MBSR)
- Duration: 8 weeks
- Frequency: Weekly group sessions
- Session Length: 90 minutes
- Format: In-person group (8-12 adolescents)
- Components: Sitting meditation, body scan, mindful movement, home practice

Control:
- Type: Usual care
- Description: Continued standard treatment (therapy as usual)

Outcomes (Primary: GAD-7 at 8 weeks post-baseline):
- Intervention Post: M=8.7 (SD=3.8)
- Control Post: M=12.9 (SD=3.2)
- Mean Difference: -4.2 (95% CI: -6.1 to -2.3)
- p-value: <0.001
```

**✓ Checkpoint**: Extracted data should be precise with page numbers for verification.

---

### Step 6.3: Complete Extraction for All 43 Studies

**Action**: Extract data into structured CSV

```bash
# Export to CSV for analysis
python code/extract_data.py \
  --studies data/full_text_pdfs/ \
  --form data/extraction/extraction_form.yaml \
  --output data/extraction/extracted_data.csv
```

**Final Dataset**: `data/extraction/extracted_data.csv` with 43 rows (one per study)

**✓ Checkpoint**: All 43 studies should have complete data extraction.

---

## Part 7: Risk of Bias Assessment (5 minutes)

### Step 7.1: Apply Cochrane RoB 2 Tool

For RCTs, use **RoB 2** (Risk of Bias 2) tool with 5 domains:

1. **Randomization process** (sequence generation, allocation concealment)
2. **Deviations from intended interventions** (blinding, adherence)
3. **Missing outcome data** (attrition, ITT analysis)
4. **Measurement of outcome** (blinding of assessors)
5. **Selection of reported result** (selective reporting)

**Action**: Assess each study

```bash
python code/risk_of_bias.py \
  --studies data/extraction/extracted_data.csv \
  --tool rob2 \
  --output data/risk_of_bias/rob2_assessments.csv
```

**Example Assessment** (Smith 2022):

```
Study: Smith_2022

Domain 1: Randomization Process
  1.1 Sequence generation: LOW RISK
      "Computer-generated random sequence using permuted blocks of 4"
  1.2 Allocation concealment: LOW RISK
      "Sequentially numbered, opaque, sealed envelopes"
  → Domain Rating: LOW RISK

Domain 2: Deviations from Intended Interventions
  2.1 Participant blinding: HIGH RISK
      "Participants aware of group assignment (not possible to blind mindfulness)"
  2.2 Adherence to intervention: LOW RISK
      "83% attended ≥6 of 8 sessions"
  → Domain Rating: SOME CONCERNS (typical for behavioral interventions)

Domain 3: Missing Outcome Data
  3.1 Data availability: LOW RISK
      "Follow-up: 87% intervention, 90% control; ITT analysis conducted"
  → Domain Rating: LOW RISK

Domain 4: Measurement of Outcome
  4.1 Assessor blinding: LOW RISK
      "Outcomes assessed by blinded research assistants"
  4.2 Objective measure: LOW RISK
      "GAD-7 self-report (validated scale)"
  → Domain Rating: LOW RISK

Domain 5: Selection of Reported Result
  5.1 Pre-registration: LOW RISK
      "Trial registered ClinicalTrials.gov NCT01234567 before enrollment"
  5.2 All outcomes reported: LOW RISK
      "All pre-specified outcomes reported"
  → Domain Rating: LOW RISK

═══════════════════════════════════════════════
OVERALL RISK OF BIAS: SOME CONCERNS
═══════════════════════════════════════════════
(Due to inability to blind participants in behavioral intervention)
```

**✓ Checkpoint**: All 43 studies assessed with domain-level ratings.

---

### Step 7.2: Summarize Risk of Bias

**Action**: Generate summary table

```bash
python code/risk_of_bias.py \
  --input data/risk_of_bias/rob2_assessments.csv \
  --summary data/risk_of_bias/rob2_summary.csv
```

**Summary Output**:

```
═══════════════════════════════════════════════
      RISK OF BIAS SUMMARY (n=43 studies)
═══════════════════════════════════════════════

Domain 1 (Randomization):
  Low risk:        37 (86%)
  Some concerns:    4 (9%)
  High risk:        2 (5%)

Domain 2 (Deviations):
  Low risk:         8 (19%)
  Some concerns:   32 (74%)
  High risk:        3 (7%)

Domain 3 (Missing data):
  Low risk:        35 (81%)
  Some concerns:    6 (14%)
  High risk:        2 (5%)

Domain 4 (Measurement):
  Low risk:        41 (95%)
  Some concerns:    2 (5%)
  High risk:        0 (0%)

Domain 5 (Selective reporting):
  Low risk:        38 (88%)
  Some concerns:    5 (12%)
  High risk:        0 (0%)

Overall Risk of Bias:
  Low risk:        12 (28%)
  Some concerns:   29 (67%)
  High risk:        2 (5%)
```

**✓ Checkpoint**: Most studies should be "Low" or "Some concerns" (exclude "High risk" in sensitivity analysis).

---

## Part 8: Generate PRISMA Flow Diagram (5 minutes)

### Step 8.1: Run Auto-Generator

The template includes a tool to create publication-ready PRISMA diagrams.

**Action**:

```bash
python code/prisma_diagram.py
```

**What It Does**:
1. Loads counts from screening files
2. Calculates deduplication statistics
3. Tracks exclusion reasons
4. Generates diagram following PRISMA 2020 template

**Output**:

```
═══════════════════════════════════════════════
          PRISMA FLOW DIAGRAM SUMMARY
═══════════════════════════════════════════════

IDENTIFICATION:
  Records identified: 1,116
  Duplicates removed: 342
  After deduplication: 774

SCREENING:
  Records screened: 774
  Records excluded: 643

ELIGIBILITY:
  Full-text assessed: 131
  Full-text excluded: 88
  Exclusion reasons:
    • Multi-component intervention (not pure mindfulness): 32
    • Age range not restricted to adolescents: 24
    • No anxiety-specific outcome: 18
    • Not RCT design: 14

INCLUDED:
  Studies in review: 43

═══════════════════════════════════════════════

✓ PRISMA diagram saved: results/prisma_flow_diagram.png
✓ PRISMA diagram saved (editable): results/prisma_flow_diagram.svg
```

**✓ Checkpoint**: Check `results/prisma_flow_diagram.png` - should be publication-ready.

---

### Step 8.2: Verify PRISMA 2020 Compliance

**Action**: Use built-in checklist validator

```bash
python code/prisma_checklist.py \
  --protocol docs/protocol.md \
  --data data/ \
  --results results/ \
  --output docs/prisma_compliance_report.md
```

**Compliance Report**:

```
PRISMA 2020 Checklist Compliance
═══════════════════════════════════════════════

✅ Title (Item 1): Systematic review identified in title
✅ Abstract (Item 2): Structured abstract following PRISMA format
✅ Introduction - Rationale (Item 3): Background documented
✅ Introduction - Objectives (Item 4): Research question with PICOS
✅ Methods - Eligibility (Item 5): Inclusion/exclusion criteria specified
✅ Methods - Information sources (Item 6): All databases documented with dates
✅ Methods - Search strategy (Item 7): Full search strategy for ≥1 database
✅ Methods - Selection process (Item 8): 2 independent reviewers, κ=0.82
✅ Methods - Data collection (Item 9): Extraction form provided
✅ Methods - Data items (Item 10): All variables defined
✅ Methods - Risk of bias (Item 11): RoB 2 tool applied
✅ Methods - Synthesis (Item 12): Meta-analysis plan specified
✅ Results - Study selection (Item 13): PRISMA flow diagram included
✅ Results - Study characteristics (Item 14): Characteristics table complete
✅ Results - Risk of bias (Item 15): RoB summary table included
✅ Results - Results of syntheses (Item 16): Effect estimates with CI
... [Items 17-27 would be completed after meta-analysis]

Current Compliance: 27/27 items (100%)
```

**✓ Checkpoint**: Should have 27/27 items addressed.

---

## Summary and Next Steps

### What You've Learned

**Completed**:
- ✅ Protocol registration with PICOS framework
- ✅ Multi-database search strategy development
- ✅ Automated search translation across databases
- ✅ Systematic deduplication (1,116 → 774 records)
- ✅ Two-reviewer screening with inter-rater reliability (κ=0.82)
- ✅ Full-text screening (131 → 43 studies)
- ✅ Structured data extraction (43 studies)
- ✅ Risk of bias assessment (RoB 2 tool)
- ✅ PRISMA flow diagram generation
- ✅ Full PRISMA 2020 compliance verification

**Key Files Generated**:
```
my_review/
├── docs/
│   ├── protocol.md (registered)
│   └── prisma_compliance_report.md
├── data/
│   ├── search_strategies/ (5 databases)
│   ├── search_results/ (1,116 → 774 records)
│   ├── screening/ (title/abstract + full-text)
│   ├── extraction/ (43 studies)
│   └── risk_of_bias/ (RoB 2 assessments)
└── results/
    └── prisma_flow_diagram.png
```

---

### Next Steps (Not Covered in This Tutorial)

**Meta-Analysis**:
- Pool effect sizes across studies
- Calculate summary effect with 95% CI
- Assess heterogeneity (I² statistic)
- Conduct sensitivity analyses

**Manuscript Writing**:
- Use `manuscript-writer` agent
- Follow PRISMA 2020 reporting guidelines
- Generate publication-ready tables

**See**: Tutorial 5 (Complete Workflow) for meta-analysis and manuscript writing.

---

### Using Literature-Reviewer Agent Effectively

**Best Practices**:

1. **Be Specific**: Provide complete eligibility criteria upfront
2. **Iterate**: Review agent suggestions, refine criteria if needed
3. **Document**: Save all agent interactions for audit trail
4. **Verify**: Agent assists but human makes final decisions
5. **Batch Processing**: Provide multiple studies per prompt for efficiency

**Example Efficient Prompt**:

```
/agent literature-reviewer

I'm screening studies for [research question]. Eligibility criteria:
[Paste PICOS]

Please assess these 10 studies (include/exclude with reasoning):

1. [Title/Abstract]
2. [Title/Abstract]
...
10. [Title/Abstract]
```

---

### Troubleshooting

**Problem**: Inter-rater reliability (κ) < 0.6

**Solution**:
1. Review eligibility criteria - are they too vague?
2. Conduct calibration exercise (both reviewers screen same 20 studies, discuss discrepancies)
3. Refine criteria based on calibration
4. Re-screen with refined criteria

---

**Problem**: Too few studies after screening (<10)

**Solution**:
1. Broaden eligibility criteria (e.g., expand age range, include more study designs)
2. Add more databases
3. Search gray literature (dissertations, conference proceedings)
4. Contact experts for unpublished studies

---

**Problem**: Search returns thousands of records

**Solution**:
1. Add more specific terms to reduce recall
2. Restrict to recent years if appropriate
3. Use more precise MeSH/controlled vocabulary
4. Consider narrowing population or intervention

---

### Additional Resources

**PRISMA 2020**:
- Checklist: https://www.prisma-statement.org/prisma-2020-checklist
- Explanation: https://www.bmj.com/content/372/bmj.n71

**Cochrane Handbook**:
- RoB 2 Tool: https://methods.cochrane.org/risk-bias-2
- Meta-analysis: https://training.cochrane.org/handbook

**Search Strategies**:
- PubMed Search Builder: https://pubmed.ncbi.nlm.nih.gov/advanced/
- Cochrane Library: https://www.cochranelibrary.com/

---

**Tutorial Complete!** You now know how to conduct a rigorous PRISMA 2020 systematic review from protocol to included studies.

**Next**: Tutorial 3 (Experimental Design) or Tutorial 5 (Complete Workflow with meta-analysis)
