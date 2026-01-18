# Systematic Review Template

**Purpose**: PRISMA 2020-compliant systematic review and meta-analysis  
**Reporting Standard**: PRISMA 2020 (27-item checklist)  
**Includes**: Complete workflow from protocol to publication

---

## Quick Start

1. **Copy this template**:
   ```bash
   cp -r templates/systematic_review my_systematic_review
   cd my_systematic_review
   ```

2. **Register your protocol** (CRITICAL - do this FIRST):
   ```bash
   python code/register_protocol.py
   # Guides you through PROSPERO or OSF registration
   ```

3. **Define your research question** (PICOS):
   ```bash
   # Edit docs/picos_framework.yaml
   population: "Adults with major depressive disorder"
   intervention: "Cognitive behavioral therapy"
   comparison: "Usual care or waitlist control"
   outcome: "Depression symptom reduction"
   study_design: "Randomized controlled trials"
   ```

4. **Develop search strategy**:
   ```bash
   python code/search_strategy_builder.py
   # Interactive search string builder with syntax translation
   ```

5. **Execute searches**:
   ```bash
   python code/search_databases.py
   # Searches OpenAlex, PubMed, arXiv, trial registries
   ```

6. **Screen and extract**:
   ```bash
   python code/screening_tracker.py
   python code/data_extraction.py
   ```

7. **Analyze and synthesize**:
   ```bash
   python code/meta_analysis.py
   Rscript code/meta_analysis.R  # Alternative R implementation
   ```

---

## Directory Structure

```
systematic_review/
├── README.md                           # This file
├── docs/
│   ├── picos_framework.yaml            # Research question definition
│   ├── protocol.md                     # Complete review protocol
│   ├── protocol_registration.md        # PROSPERO/OSF registration record
│   ├── search_strategy.md              # Documented search strings
│   ├── screening_protocol.md           # Inclusion/exclusion criteria
│   ├── data_extraction_form.md         # Extraction schema
│   ├── rob_assessment_guide.md         # Risk of bias procedures
│   ├── grade_assessment.md             # GRADE procedures
│   └── prisma_checklist.md             # 27-item compliance tracker
│
├── code/
│   ├── register_protocol.py            # Protocol registration helper
│   ├── search_strategy_builder.py      # Interactive search builder
│   ├── search_translation.py           # Cross-database syntax translation
│   ├── search_databases.py             # Multi-database search execution
│   ├── deduplication.py                # Advanced duplicate detection
│   ├── screening_tracker.py            # Title/abstract & full-text screening
│   ├── inter_rater_reliability.py      # Cohen's kappa calculator
│   ├── data_extraction.py              # Structured extraction tool
│   ├── rob_assessment.py               # RoB 2 / ROBINS-I tools
│   ├── prisma_diagram.py               # Flow diagram generator
│   ├── meta_analysis.py                # Python meta-analysis (statsmodels)
│   ├── meta_analysis.R                 # R meta-analysis (metafor)
│   ├── sensitivity_analysis.py         # Leave-one-out, subgroups
│   ├── publication_bias.py             # Funnel plots, Egger's test
│   ├── grade_assessment.py             # GRADE evidence rating
│   └── prisma_validator.py             # Auto-check 27-item compliance
│
├── data/
│   ├── search_results/
│   │   ├── openalex_results.csv
│   │   ├── pubmed_results.csv
│   │   ├── arxiv_results.csv
│   │   ├── clinicaltrials_results.csv
│   │   └── deduplicated_results.csv
│   ├── screening/
│   │   ├── title_abstract_screening.csv
│   │   ├── full_text_screening.csv
│   │   ├── exclusion_reasons.csv
│   │   └── screening_conflicts.csv
│   └── extracted_data/
│       ├── study_characteristics.csv
│       ├── outcome_data.csv
│       ├── rob_assessments.csv
│       └── grade_assessments.csv
│
├── results/
│   ├── prisma_flow_diagram.png
│   ├── forest_plots/
│   ├── funnel_plots/
│   ├── sensitivity_analyses/
│   ├── meta_analysis_results.json
│   └── grade_summary_of_findings.csv
│
└── manuscript/
    ├── systematic_review.md            # Draft manuscript
    ├── supplementary_materials.md
    └── prisma_checklist_completed.md
```

---

## PRISMA 2020 Compliance

This template ensures **27/27 PRISMA items** are addressed:

### Title & Abstract
- ✅ Item 1: Title identifies as systematic review
- ✅ Item 2: Structured abstract (background, methods, results, conclusions)

### Introduction  
- ✅ Item 3: Rationale with knowledge gap
- ✅ Item 4: Explicit objectives (PICOS)

### Methods
- ✅ Item 5: Eligibility criteria (PICOS framework)
- ✅ Item 6: Information sources (databases, dates, citation searching)
- ✅ Item 7: Search strategy (full strings + translation)
- ✅ Item 8: Selection process (screening workflow + κ)
- ✅ Item 9: Data collection process (extraction forms)
- ✅ Item 10: Data items (all variables extracted)
- ✅ Item 11: Study risk of bias (RoB 2, ROBINS-I)
- ✅ Item 12: Effect measures (OR, RR, SMD, etc.)
- ✅ Item 13: Synthesis methods (meta-analysis approach)
- ✅ Item 14: Reporting bias assessment (funnel plots)
- ✅ Item 15: Certainty assessment (GRADE)

### Results
- ✅ Item 16: Study selection (PRISMA flow diagram)
- ✅ Item 17: Study characteristics (table with citations)
- ✅ Item 18: Risk of bias (summary + individual assessments)
- ✅ Item 19: Results of syntheses (forest plots)
- ✅ Item 20: Reporting biases (funnel plot analysis)
- ✅ Item 21: Certainty of evidence (GRADE table)

### Discussion
- ✅ Item 22: Discussion framework (interpretation, limitations, implications)

### Other
- ✅ Item 23: Registration and protocol (PROSPERO/OSF)
- ✅ Item 24: Support/funding disclosure
- ✅ Item 25: Competing interests
- ✅ Item 26: Availability of data/code
- ✅ Item 27: Protocol amendments documented

---

## Workflow Phases

### Phase 1: Protocol Development (BEFORE searching)

**CRITICAL**: Protocol must be finalized and registered BEFORE database searches.

1. **Define PICOS** (`docs/picos_framework.yaml`)
2. **Write protocol** (`docs/protocol.md`)
3. **Register protocol**:
   ```bash
   python code/register_protocol.py
   # Options: PROSPERO (health), OSF (any field)
   ```
4. **Develop search strategy** (`code/search_strategy_builder.py`)
5. **Pilot screening criteria** (test on 20 abstracts)

**Quality Gate**: Protocol registered before proceeding ✅

---

### Phase 2: Search Execution

1. **Run database searches**:
   ```bash
   python code/search_databases.py --databases all
   # Searches: OpenAlex, PubMed, arXiv, ClinicalTrials.gov
   ```

2. **Search translation** (automatic):
   ```python
   # PubMed syntax automatically translated to:
   # - Embase syntax
   # - Web of Science syntax
   # - Scopus syntax
   ```

3. **Citation chasing** (optional):
   ```bash
   python code/citation_chasing.py --backward --forward
   # Backward: References of included studies
   # Forward: Studies citing included studies
   ```

4. **Grey literature**:
   - Trial registries: ClinicalTrials.gov, WHO ICTRP
   - Dissertations: ProQuest
   - Conference proceedings (manual)

**Deliverable**: `data/search_results/*.csv` with full metadata

---

### Phase 3: Deduplication

```bash
python code/deduplication.py
```

**Features**:
- Exact duplicate detection (DOI, title+author+year)
- Near-duplicate detection (fuzzy title matching 90% similarity)
- Manual verification sample (10% of removed duplicates)

**Output**: `data/search_results/deduplicated_results.csv`

**Quality Gate**: Deduplication log reviewed ✅

---

### Phase 4: Screening

#### Title/Abstract Screening

```bash
python code/screening_tracker.py --phase title_abstract
```

**Process**:
1. Dual independent screening (10% sample minimum per PRISMA-S)
2. Calculate Cohen's κ (target ≥0.6)
3. If κ <0.6: Clarify criteria, re-pilot on 20 new abstracts
4. Resolve conflicts through discussion
5. Single reviewer completes remainder if κ ≥0.8

**Output**: `data/screening/title_abstract_screening.csv`

#### Full-Text Screening

```bash
python code/screening_tracker.py --phase full_text
```

**Process**:
1. Retrieve full texts (Unpaywall API integration)
2. Dual screening of all full texts
3. Document exclusion reasons for EVERY excluded study
4. Resolve conflicts with third reviewer if needed

**Output**: 
- `data/screening/full_text_screening.csv`
- `data/screening/exclusion_reasons.csv` (required for PRISMA)

**Quality Gate**: Inter-rater reliability κ ≥0.6 ✅

---

### Phase 5: Data Extraction

```bash
python code/data_extraction.py
```

**Extraction Schema** (customizable):
- Study characteristics: Author, year, country, design, sample size
- Population: Demographics, diagnosis criteria
- Intervention: Type, duration, intensity, delivery
- Comparison: Type, characteristics
- Outcomes: Measures, time points, effect estimates
- Funding source
- Conflicts of interest

**Process**:
1. Pilot extraction on 5 studies (2 reviewers independently)
2. Refine extraction form based on pilot
3. Dual extraction for all studies (or single + verification)
4. Resolve discrepancies through discussion

**Output**: 
- `data/extracted_data/study_characteristics.csv`
- `data/extracted_data/outcome_data.csv`

**Quality Gate**: Extraction form piloted and validated ✅

---

### Phase 6: Risk of Bias Assessment

```bash
python code/rob_assessment.py --tool rob2
# or
python code/rob_assessment.py --tool robins_i
```

**Tools Included**:
- **RoB 2** (Cochrane tool for RCTs)
  - Randomization process
  - Deviations from intended interventions
  - Missing outcome data
  - Measurement of outcomes
  - Selection of reported results

- **ROBINS-I** (for non-randomized studies)
  - Confounding
  - Selection of participants
  - Classification of interventions
  - Deviations from intended interventions
  - Missing data
  - Measurement of outcomes
  - Selection of reported results

**Process**:
1. Define signaling questions upfront
2. Pilot assessment on 5 studies
3. Dual assessment for all studies
4. Resolve disagreements through discussion

**Output**: `data/extracted_data/rob_assessments.csv`

**Quality Gate**: All RoB domains assessed for all studies ✅

---

### Phase 7: Meta-Analysis

#### Python Implementation

```bash
python code/meta_analysis.py --outcome primary --model random
```

**Features**:
- Random-effects meta-analysis (DerSimonian-Laird)
- Heterogeneity assessment (I², τ², Q-test)
- Forest plot generation
- Prediction intervals

#### R Implementation (recommended for advanced features)

```bash
Rscript code/meta_analysis.R
```

**Features** (using `metafor` package):
- Multiple models: random-effects, fixed-effect, mixed-effects
- Meta-regression for moderators
- Subgroup analyses
- Influence diagnostics
- Publication bias tests (funnel plot, Egger's, trim-and-fill)

**Output**:
- `results/meta_analysis_results.json`
- `results/forest_plots/primary_outcome.png`

---

### Phase 8: Sensitivity Analyses

```bash
python code/sensitivity_analysis.py
```

**Analyses Included**:
1. **Leave-one-out**: Remove each study iteratively, re-run meta-analysis
2. **Fixed vs random effects**: Compare models
3. **Risk of bias subgroups**: High vs low RoB studies
4. **Publication year**: Recent vs older studies
5. **Sample size**: Small vs large studies
6. **Trim-and-fill**: Adjust for publication bias

**Output**: `results/sensitivity_analyses/`

**Quality Gate**: All pre-specified sensitivity analyses completed ✅

---

### Phase 9: Publication Bias Assessment

```bash
python code/publication_bias.py
```

**Tests Included**:
- Funnel plot (visual inspection)
- Egger's test (asymmetry test) - requires ≥10 studies
- Trim-and-fill analysis (impute missing studies)
- P-curve analysis (selective reporting)

**Interpretation**:
- <10 studies: "Too few studies for meaningful publication bias assessment"
- ≥10 studies: Full battery of tests

**Output**: `results/funnel_plots/`

---

### Phase 10: GRADE Assessment

```bash
python code/grade_assessment.py
```

**GRADE Domains**:
1. Risk of bias (downgrade if serious limitations)
2. Inconsistency (downgrade if I² >50% and unexplained)
3. Indirectness (downgrade if PICO doesn't match)
4. Imprecision (downgrade if wide CIs crossing null)
5. Publication bias (downgrade if suspected)

**Upgrades** (observational studies only):
- Large effect (RR >2 or <0.5)
- Dose-response gradient
- All plausible confounding would reduce effect

**Certainty Levels**:
- High: ⊕⊕⊕⊕
- Moderate: ⊕⊕⊕○
- Low: ⊕⊕○○
- Very low: ⊕○○○

**Output**: `results/grade_summary_of_findings.csv`

**Quality Gate**: GRADE assessed for all synthesized outcomes ✅

---

### Phase 11: PRISMA Flow Diagram

```bash
python code/prisma_diagram.py
```

**Auto-generates** from screening data:
- Records identified from databases
- Records removed (duplicates, other reasons)
- Records screened (title/abstract)
- Records excluded (with reasons)
- Full texts assessed
- Full texts excluded (with reasons)
- Studies included in review
- Studies included in meta-analysis

**Output**: `results/prisma_flow_diagram.png` (publication-ready)

---

### Phase 12: Manuscript Preparation

```bash
python code/prisma_validator.py
# Checks manuscript against 27-item PRISMA checklist
```

**Structure** (`manuscript/systematic_review.md`):
1. Title: "...A Systematic Review and Meta-Analysis"
2. Abstract: Structured (Background, Methods, Results, Conclusions)
3. Introduction: Rationale, objectives (PICOS)
4. Methods: All PRISMA items 5-15
5. Results: PRISMA flow diagram, characteristics, RoB, syntheses, GRADE
6. Discussion: Interpretation, limitations, implications
7. Conclusion
8. References
9. Supplementary Materials

**Required Supplements**:
- Full search strings for all databases
- PRISMA checklist with page numbers
- Excluded studies with reasons
- Risk of bias assessments (all studies)
- GRADE evidence profiles

**Quality Gate**: 27/27 PRISMA items addressed ✅

---

## Using Research Assistant Agents

### Agent: literature-reviewer

**Use for complete workflow guidance**:

```
/agent literature-reviewer

I'm conducting a systematic review on [your topic].
PICOS:
- Population: [specific]
- Intervention: [specific]
- Comparison: [specific]
- Outcome: [specific]
- Study design: [specific]

Please help me:
1. Develop search strategy
2. Guide screening process
3. Assist with data extraction
4. Interpret meta-analysis results
```

### Agent: data-analyst

**Use for meta-analysis**:

```
/agent data-analyst

I have extracted data from [N] RCTs on [intervention] vs [control].
Outcome: [outcome name]
Data file: data/extracted_data/outcome_data.csv

Please conduct:
- Random-effects meta-analysis
- Heterogeneity assessment
- Sensitivity analyses
- Publication bias tests
```

### Agent: manuscript-writer

**Use for writing**:

```
/agent manuscript-writer

I need to write a systematic review manuscript following PRISMA 2020.
Review: [brief description]
Results: [main findings]
Target journal: [journal name]

Please draft the manuscript ensuring all 27 PRISMA items are addressed.
```

---

## Pre-configured Scripts

### Protocol Registration

`code/register_protocol.py` - Interactive registration helper:

```python
"""
Protocol Registration Helper

Guides through PROSPERO or OSF registration.
Generates registration-ready protocol document.
"""

# Asks:
# - Review title
# - PICOS details
# - Search strategy
# - Analysis plan
# - Team members

# Outputs:
# - docs/protocol_registration.md
# - Registration form (PROSPERO XML or OSF project)
```

### Search Strategy Builder

`code/search_strategy_builder.py` - Interactive search development:

```python
"""
Search Strategy Builder

Interactive tool for building Boolean search strings.
Includes:
- Concept mapping (PICOS → search terms)
- Synonym expansion
- MeSH/Emtree suggestions
- Syntax validation
- Cross-database translation
"""

# Example session:
# Population concepts: depression, depressive disorder
# Intervention concepts: CBT, cognitive therapy
# → Generates optimized Boolean search
# → Translates to PubMed, Embase, Scopus syntax
```

### Search Translation Engine

`code/search_translation.py` - Automatic syntax conversion:

```python
"""
Cross-Database Search Translation

Translates search strings between database syntaxes.
Handles:
- Field codes (ti,ab vs [tiab])
- Proximity operators (NEAR/3 vs ADJ3)
- Wildcards (* vs $)
- Subject headings (MeSH vs Emtree)
"""

# Example:
# Input (PubMed):
#   ("cognitive therapy"[MeSH] OR CBT[tiab]) AND depression[tiab]
# 
# Output (Embase):
#   ('cognitive therapy'/exp OR CBT:ab,ti) AND depression:ab,ti
```

---

## Advanced Features

### 1. Living Systematic Review Mode

**Enable continuous updating**:

```bash
python code/search_databases.py --living --schedule monthly
```

- Automated monthly re-searches
- New study alerts
- Incremental screening
- Version-controlled updates
- Changelog generation

### 2. Citation Chasing

**Backward + forward citation tracking**:

```bash
python code/citation_chasing.py \
  --backward \
  --forward \
  --max-depth 1
```

- Extracts references from included studies
- Finds citing papers via Semantic Scholar API
- Auto-deduplicates with main search
- Typically adds 10-20% more studies

### 3. Full-Text Retrieval Automation

**Automated PDF retrieval**:

```bash
python code/full_text_retrieval.py
```

- Unpaywall API (open access)
- Institutional repository searches
- Author contact automation (email templates)
- Success rate: ~70-85%

### 4. Machine Learning Screening (v1.3 feature)

**AI-assisted title/abstract screening** (coming soon):

```bash
python code/ml_screening.py --train --assist
```

- Train on first 200 human decisions
- Predict relevance for remaining abstracts
- Prioritize likely-relevant studies
- Human verification required

---

## Quality Assurance Checklist

### Before Protocol Registration
- [ ] PICOS defined with specific inclusion/exclusion criteria
- [ ] Search strategy developed and peer-reviewed
- [ ] Screening process defined with pilot plan
- [ ] Data extraction form drafted
- [ ] Risk of bias tool selected
- [ ] Analysis plan pre-specified (primary/secondary outcomes)
- [ ] GRADE assessment planned

### During Review Execution
- [ ] All database searches within 1 month of each other
- [ ] Search results exported with full metadata
- [ ] Deduplication verified (10% sample checked)
- [ ] Inter-rater reliability κ ≥0.6 for screening
- [ ] Full texts retrieved for >90% of eligible studies
- [ ] Dual extraction for all included studies
- [ ] Risk of bias assessed independently by 2 reviewers

### Before Manuscript Submission
- [ ] PRISMA flow diagram complete with exact counts
- [ ] All excluded full-text studies listed with reasons
- [ ] Risk of bias assessments for all included studies
- [ ] GRADE certainty assessment for all outcomes
- [ ] Sensitivity analyses completed as planned
- [ ] Publication bias assessed (if ≥10 studies)
- [ ] PRISMA checklist: 27/27 items addressed
- [ ] Protocol registration number included
- [ ] Protocol amendments documented
- [ ] All co-authors approved

---

## Common Pitfalls Prevented

✅ **Search not reproducible** → Full search documentation + syntax translation log  
✅ **Missed duplicates** → Advanced deduplication with near-duplicate detection  
✅ **Low inter-rater reliability** → Automated κ calculation + criteria refinement workflow  
✅ **Selective outcome reporting** → Pre-specified outcomes in registered protocol  
✅ **Unclear exclusion reasons** → Required documentation for every excluded study  
✅ **Risk of bias not assessed** → RoB 2/ROBINS-I tools with all domains  
✅ **GRADE not conducted** → Mandatory certainty assessment  
✅ **Incomplete PRISMA compliance** → Auto-validator checks all 27 items  
✅ **No protocol registration** → Registration enforced before search execution  
✅ **Conflicts of interest not reported** → Automated disclosure forms  

---

## Citation

When using this template, cite:

```
Research Assistant for Claude Code. (2025). Systematic Review Template. 
Retrieved from https://github.com/astoreyai/ai_scientist
```

---

## Support

- **Agent Help**: Use `/agent literature-reviewer` for PRISMA-specific guidance
- **Documentation**: See main repository `docs/`
- **Issues**: https://github.com/astoreyai/ai_scientist/issues

---

*Template version: 1.2.0*  
*PRISMA 2020 compliant: 27/27 items*  
*Last updated: 2025-11-10*
