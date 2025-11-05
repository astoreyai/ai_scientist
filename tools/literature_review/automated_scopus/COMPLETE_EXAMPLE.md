# Complete End-to-End Literature Review Example

**Example Topic:** "Explainable AI Methods for Face Recognition Systems"
**User:** PhD Student in Computer Science
**Goal:** Systematic literature review for dissertation Chapter 2

---

## Phase 1: Planning (Before Any Searching)

### Step 1.1: Define Research Questions

**From dissertation Chapter 1:**

- **RQ1:** What explainable AI methods have been applied to face recognition systems?
- **RQ2:** How is the quality of XAI explanations evaluated in face recognition?
- **RQ3:** What are the limitations of current XAI approaches in face recognition?

### Step 1.2: Define Inclusion/Exclusion Criteria

**📄 File:** `PHD_PIPELINE/falsifiable_attribution_dissertation/literature_review/inclusion_exclusion_criteria.md`

```markdown
# Inclusion/Exclusion Criteria

**Date Defined:** 2025-10-16 (BEFORE executing searches)
**Last Modified:** 2025-10-16

## Inclusion Criteria

A paper is **INCLUDED** if it meets ALL of the following:

### 1. Publication Characteristics
- ✅ Published in peer-reviewed journal OR conference
- ✅ Published 2015-2025 (last 10 years)
- ✅ Written in English
- ✅ Full text available via institutional access

### 2. Topic Relevance
- ✅ Discusses explainable AI / interpretable ML methods
- ✅ Applied to face recognition, face verification, OR facial biometrics
- ✅ Presents empirical results OR theoretical framework

### 3. Quality Threshold
- ✅ Conference: CORE rank A or above, OR top-tier venue (CVPR, ICCV, NeurIPS, etc.)
- ✅ Journal: Q1 or Q2 in relevant subject area
- ✅ Clear methodology described

## Exclusion Criteria

A paper is **EXCLUDED** if ANY of the following apply:

### 1. Out of Scope
- ❌ Not about explainable AI (even if about face recognition)
- ❌ Not about face recognition (even if about XAI)
- ❌ Only mentions face recognition/XAI tangentially
- ❌ Focus is on different biometric (fingerprint, iris, etc.)

### 2. Methodology Issues
- ❌ No clear methodology described
- ❌ Only opinion/editorial (no empirical evaluation)
- ❌ Survey/review paper without original contribution

### 3. Publication Type
- ❌ Book chapter (unless seminal work)
- ❌ Preprint without peer review
- ❌ Workshop paper (unless highly cited)
- ❌ Technical report, white paper
- ❌ Patent

### 4. Quality Issues
- ❌ Conference: Below CORE B ranking
- ❌ Journal: Below Q2 ranking
- ❌ Insufficient detail to reproduce

### 5. Accessibility
- ❌ Full text not accessible via institutional access or author contact

## Decision Tree

```
Paper Found
    │
    ├─ Is it peer-reviewed? ───────────────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ Published 2015-2025? ───────────────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ English language? ──────────────────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ About XAI methods? ─────────────────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ Applied to face recognition? ───────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ Empirical results OR theory? ───────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ Meets quality threshold? ───────────────► NO → EXCLUDE
    │                                             YES ↓
    ├─ Full text accessible? ──────────────────► NO → EXCLUDE (try author)
    │                                             YES ↓
    └─ → INCLUDE for full-text screening
```

## Edge Cases

### Case 1: Survey papers
**Decision:** INCLUDE if they provide comprehensive synthesis
**Rationale:** Useful for understanding field, but note as "review" in data extraction

### Case 2: Papers about face recognition that mention XAI briefly
**Decision:** Title screen: UNCERTAIN → Abstract screen: Likely EXCLUDE
**Rationale:** Focus must be on XAI methods, not just mentioning them

### Case 3: Preprints on arXiv that are highly cited
**Decision:** EXCLUDE, but note if accepted version exists
**Rationale:** Only peer-reviewed work for systematic quality

### Case 4: Related biometric (e.g., iris recognition with XAI)
**Decision:** EXCLUDE
**Rationale:** Scope is face recognition only, but note for related work

### Case 5: Papers before 2015 that are seminal
**Decision:** Add via citation search, not systematic search
**Rationale:** Date filter ensures manageability, but don't ignore foundational work
```

---

### Step 1.3: Develop Keywords

**📄 File:** `config/search_queries.yaml`

```yaml
# Literature Review for "Falsifiable Attribution for Face Verification"
# PhD Dissertation - Computer Science
# Date: 2025-10-16

searches:
  # PRIMARY SEARCH - Main topic
  - id: "search_001_xai_face"
    name: "XAI Methods in Face Recognition"
    description: "Explainable AI methods applied to face recognition and verification systems"
    enabled: true

    # Keywords organized by concept
    keywords:
      concept_1_explainability:
        # Main terms
        - "explainable AI"
        - "explainability"
        - "interpretable"
        - "interpretability"
        # Acronyms
        - "XAI"
        - "IML"  # Interpretable Machine Learning
        # Related terms
        - "transparent"
        - "transparency"
        - "attribution method"
        - "saliency map"
        - "feature importance"
        # Specific methods
        - "SHAP"
        - "LIME"
        - "Grad-CAM"
        - "integrated gradients"
        - "attention mechanism"

      concept_2_face_recognition:
        # Main terms
        - "face recognition"
        - "face verification"
        - "face identification"
        # Variants
        - "facial recognition"
        - "facial verification"
        - "facial identification"
        # Related
        - "facial biometrics"
        - "face matching"
        - "face authentication"
        # Technical
        - "face embedding"
        - "face representation"

    # Scopus query built from keywords
    query: >
      TITLE-ABS-KEY("explainable AI" OR "explainability" OR "interpretable" OR "interpretability" OR "XAI" OR "transparent" OR "attribution method" OR "saliency map" OR "SHAP" OR "LIME" OR "Grad-CAM" OR "integrated gradients")
      AND TITLE-ABS-KEY("face recognition" OR "face verification" OR "face identification" OR "facial recognition" OR "facial biometrics" OR "face matching" OR "face authentication")

    # Filters
    date_range:
      start: 2015
      end: 2025

    subject_areas:
      - COMP  # Computer Science
      - ENGI  # Engineering

    document_types:
      - "ar"  # Article
      - "cp"  # Conference Paper
      - "re"  # Review

    # Link to research questions
    research_questions:
      - "RQ1: What XAI methods are applied to face recognition?"
      - "RQ2: How is XAI quality evaluated in face recognition?"

    expected_results: "100-200 papers"
    priority: "high"
    notes: "Primary search covering main dissertation topic"


  # SECONDARY SEARCH - Evaluation metrics
  - id: "search_002_xai_evaluation"
    name: "XAI Evaluation Metrics"
    description: "How explainable AI methods are evaluated and measured"
    enabled: true

    keywords:
      concept_1_xai:
        - "explainable AI"
        - "XAI"
        - "interpretability"
        - "saliency map"
        - "attribution method"

      concept_2_evaluation:
        - "evaluation"
        - "metric"
        - "measure"
        - "quality assessment"
        - "fidelity"
        - "faithfulness"
        - "stability"
        - "robustness"
        - "human evaluation"
        - "user study"

    query: >
      TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretability" OR "saliency map" OR "attribution method")
      AND TITLE-ABS-KEY("evaluation" OR "metric" OR "measure" OR "quality" OR "fidelity" OR "faithfulness" OR "stability" OR "human evaluation")

    date_range:
      start: 2015
      end: 2025

    subject_areas:
      - COMP

    document_types:
      - "ar"
      - "cp"
      - "re"

    research_questions:
      - "RQ2: How is XAI quality evaluated?"

    expected_results: "50-150 papers"
    priority: "high"
    notes: "Covers evaluation methodology for RQ2"


  # TERTIARY SEARCH - Gap identification (falsifiability)
  - id: "search_003_falsifiability_xai"
    name: "Falsifiability in XAI"
    description: "Falsifiability criterion applied to explainable AI (gap analysis)"
    enabled: true

    keywords:
      concept_1_falsifiability:
        - "falsifiability"
        - "falsifiable"
        - "Popper"
        - "demarcation"
        - "testability"
        - "refutability"
        - "scientific method"

      concept_2_xai:
        - "explainable AI"
        - "XAI"
        - "interpretability"
        - "machine learning"
        - "deep learning"

    query: >
      TITLE-ABS-KEY("falsifiability" OR "falsifiable" OR "Popper" OR "demarcation" OR "testability")
      AND TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretability" OR "machine learning")

    date_range:
      start: 2010  # Broader range for gap analysis
      end: 2025

    subject_areas:
      - COMP
      - MULT  # Multidisciplinary

    document_types:
      - "ar"
      - "re"

    research_questions:
      - "RQ1: Has falsifiability been applied to XAI?"

    expected_results: "5-20 papers"
    priority: "high"
    notes: "Gap analysis - expect few papers to establish novelty"
```

---

## Phase 2: Execute Searches (10 minutes total)

### Step 2.1: Validate Queries

```bash
cd /home/aaron/projects/xai/PHD_PIPELINE/tools/literature_review/automated_scopus/scripts

# Dry run to validate
python scopus_search.py --dry-run
```

**Output:**
```
[2025-10-16 09:15:30] INFO: Loading configuration...
[2025-10-16 09:15:30] INFO: Loading queries... Found 3 queries
[2025-10-16 09:15:30] INFO: DRY RUN - Query would be executed with parameters:
{
  "apiKey": "***",
  "query": "TITLE-ABS-KEY(\"explainable AI\" OR ...)",
  "count": 25,
  "start": 0,
  "view": "COMPLETE",
  "date": "2015-2025",
  "subj": "COMP,ENGI"
}
[2025-10-16 09:15:30] INFO: ✅ All queries validated successfully
```

### Step 2.2: Execute Searches

```bash
# Execute all enabled searches
python scopus_search.py
```

**Output:**
```
============================================================
Scopus Search Pipeline Starting
============================================================
[2025-10-16 09:20:15] INFO: Loaded 3 enabled queries

[2025-10-16 09:20:15] INFO: Executing query search_001_xai_face: XAI Methods in Face Recognition
[2025-10-16 09:20:17] INFO: Total results: 146
[2025-10-16 09:20:17] INFO: Page 1: Retrieved 25 results (Total: 25/146)
[2025-10-16 09:20:18] INFO: Page 2: Retrieved 25 results (Total: 50/146)
[2025-10-16 09:20:19] INFO: Page 3: Retrieved 25 results (Total: 75/146)
[2025-10-16 09:20:20] INFO: Page 4: Retrieved 25 results (Total: 100/146)
[2025-10-16 09:20:21] INFO: Page 5: Retrieved 25 results (Total: 125/146)
[2025-10-16 09:20:22] INFO: Page 6: Retrieved 21 results (Total: 146/146)
[2025-10-16 09:20:22] INFO: Results saved to: results/search_001_xai_face_2025-10-16_09-20-15.json
[2025-10-16 09:20:22] INFO: Successfully retrieved 146 results for query search_001_xai_face

[2025-10-16 09:20:23] INFO: Executing query search_002_xai_evaluation: XAI Evaluation Metrics
[2025-10-16 09:20:24] INFO: Total results: 87
[2025-10-16 09:20:24] INFO: Page 1: Retrieved 25 results (Total: 25/87)
[2025-10-16 09:20:25] INFO: Page 2: Retrieved 25 results (Total: 50/87)
[2025-10-16 09:20:26] INFO: Page 3: Retrieved 25 results (Total: 75/87)
[2025-10-16 09:20:27] INFO: Page 4: Retrieved 12 results (Total: 87/87)
[2025-10-16 09:20:27] INFO: Results saved to: results/search_002_xai_evaluation_2025-10-16_09-20-15.json
[2025-10-16 09:20:27] INFO: Successfully retrieved 87 results for query search_002_xai_evaluation

[2025-10-16 09:20:28] INFO: Executing query search_003_falsifiability_xai: Falsifiability in XAI
[2025-10-16 09:20:29] INFO: Total results: 12
[2025-10-16 09:20:29] INFO: Page 1: Retrieved 12 results (Total: 12/12)
[2025-10-16 09:20:29] INFO: Results saved to: results/search_003_falsifiability_xai_2025-10-16_09-20-15.json
[2025-10-16 09:20:29] INFO: Successfully retrieved 12 results for query search_003_falsifiability_xai

============================================================
Search Pipeline Complete
Queries Executed: 3/3
Total Papers Retrieved: 245
Total API Calls: 14
============================================================

✅ Search complete! Next steps:
1. Run: python result_exporter.py
2. Run: python deduplication.py
3. Import results to reference manager
============================================================
```

**📄 Generated File:** `logs/search_log_2025-10-16.md` (excerpt)

```markdown
# Scopus Search Execution Log

**Date:** 2025-10-16 09:20:30
**Execution Duration:** 14.5 seconds
**Total API Calls:** 14

---

## Search 1: XAI Methods in Face Recognition

**Query ID:** `search_001_xai_face`
**Description:** Explainable AI methods applied to face recognition and verification systems

**Query String:**
```
TITLE-ABS-KEY("explainable AI" OR "explainability" OR "interpretable" OR "interpretability" OR "XAI" OR "transparent" OR "attribution method" OR "saliency map" OR "SHAP" OR "LIME" OR "Grad-CAM" OR "integrated gradients")
AND TITLE-ABS-KEY("face recognition" OR "face verification" OR "face identification" OR "facial recognition" OR "facial biometrics" OR "face matching" OR "face authentication")
```

**Date Range:** 2015 - 2025
**Subject Areas:** COMP, ENGI
**Results:** 146 papers
**API Calls:** 6
**Timestamp:** 2025-10-16T09:20:22

**Research Questions:**
- RQ1: What XAI methods are applied to face recognition?
- RQ2: How is XAI quality evaluated in face recognition?

---

[... additional searches ...]

## Summary

**Total Queries Executed:** 3
**Total Results Retrieved:** 245 papers
**Total API Calls:** 14
**Average Results per Query:** 81.7
```

---

### Step 2.3: Export Results

```bash
python result_exporter.py
```

**Output:**
```
============================================================
Result Exporter
============================================================
[2025-10-16 09:25:00] INFO: Loaded 3 result files

Exporting results...
- exports/search_001_xai_face_2025-10-16.bib (146 entries)
- exports/search_001_xai_face_2025-10-16.ris (146 entries)
- exports/search_001_xai_face_2025-10-16.csv (146 rows)

- exports/search_002_xai_evaluation_2025-10-16.bib (87 entries)
- exports/search_002_xai_evaluation_2025-10-16.ris (87 entries)
- exports/search_002_xai_evaluation_2025-10-16.csv (87 rows)

- exports/search_003_falsifiability_xai_2025-10-16.bib (12 entries)
- exports/search_003_falsifiability_xai_2025-10-16.ris (12 entries)
- exports/search_003_falsifiability_xai_2025-10-16.csv (12 rows)

- exports/all_results_2025-10-16.bib (245 entries)
- exports/all_results_2025-10-16.ris (245 entries)
- exports/screening_2025-10-16.csv (245 rows)
- exports/all_results_2025-10-16.json

[2025-10-16 09:25:05] INFO: All exports complete!
============================================================
✅ Export complete!

Next step: python deduplication.py
============================================================
```

**📄 Generated Files:**
- `exports/all_results_2025-10-16.bib` - For LaTeX bibliography
- `exports/all_results_2025-10-16.ris` - For Zotero/Mendeley/EndNote
- `exports/screening_2025-10-16.csv` - For manual screening
- Individual exports per search

---

### Step 2.4: Deduplicate

```bash
python deduplication.py
```

**Output:**
```
============================================================
Deduplication
============================================================
[2025-10-16 09:30:00] INFO: Loading papers from: exports/screening_2025-10-16.csv
[2025-10-16 09:30:00] INFO: Loaded 245 papers

[2025-10-16 09:30:01] INFO: Finding duplicates...
[2025-10-16 09:30:02] INFO: Found 8 exact DOI duplicates
[2025-10-16 09:30:03] INFO: Found 5 title+author duplicates
[2025-10-16 09:30:05] INFO: Found 3 fuzzy title matches (review recommended)
[2025-10-16 09:30:05] INFO: Total duplicates found: 16 (6.5%)
[2025-10-16 09:30:05] INFO: Unique papers: 229

[2025-10-16 09:30:06] INFO: Deduplication report saved to: reports/deduplication_report_2025-10-16.md
[2025-10-16 09:30:06] INFO: Duplicates CSV saved to: reports/duplicates_2025-10-16.csv
[2025-10-16 09:30:07] INFO: Deduplicated screening CSV saved to: exports/deduplicated/screening_deduplicated_2025-10-16.csv

============================================================
✅ Deduplication complete!

Original papers: 245
Duplicates found: 16 (6.5%)
Unique papers: 229

Reports saved to: ../reports/
Deduplicated exports saved to: ../exports/deduplicated/
============================================================

⚠️  3 duplicates flagged for manual review
Check: ../reports/duplicates_2025-10-16.csv
```

**📄 Generated File:** `reports/deduplication_report_2025-10-16.md` (excerpt)

```markdown
# Deduplication Report

**Date:** 2025-10-16 09:30:07

---

## Summary

- **Original Papers:** 245
- **Duplicates Found:** 16 (6.5%)
- **Unique Papers:** 229

### Duplicates by Strategy

- **doi_exact:** 8 duplicates
- **title_author:** 5 duplicates
- **title_fuzzy:** 3 duplicates

## Duplicate Details

### DOI Exact Match (8 duplicates)

#### Duplicate 1

**Original (kept):** Explainable AI for Face Recognition: A Comprehensive Survey
**Duplicate (removed):** Explainable AI for Face Recognition: A Comprehensive Survey

**Reason:** Same paper retrieved from multiple searches (search_001 and search_002)

[... more duplicates ...]

## Next Steps

1. Review duplicates marked for manual review
2. Import deduplicated results to reference manager
3. Begin title/abstract screening
```

---

### Step 2.5: Update PRISMA

```bash
python prisma_updater.py --report
```

**Output:**
```
============================================================
PRISMA Diagram Updater
============================================================
[2025-10-16 09:35:00] INFO: Loaded 3 search results
[2025-10-16 09:35:00] INFO: Loaded deduplication stats
[2025-10-16 09:35:01] INFO: PRISMA diagram updated: ../prisma_flow_diagram.md
[2025-10-16 09:35:02] INFO: PRISMA report saved to: reports/prisma_report_2025-10-16.md

============================================================
✅ PRISMA diagram updated!

Records identified: 245
Duplicates removed: 16
Records after deduplication: 229

PRISMA file: ../prisma_flow_diagram.md
============================================================
```

**📄 Generated File:** `prisma_flow_diagram.md` (complete PRISMA diagram)

```markdown
# PRISMA Flow Diagram

**Last Updated:** 2025-10-16 09:35:01
**Auto-generated by:** Automated Scopus Pipeline

---

## Identification

**Records identified from Scopus:**
- XAI Methods in Face Recognition (`search_001_xai_face`): 146 records (searched: 2025-10-16)
- XAI Evaluation Metrics (`search_002_xai_evaluation`): 87 records (searched: 2025-10-16)
- Falsifiability in XAI (`search_003_falsifiability_xai`): 12 records (searched: 2025-10-16)

**Total records identified:** 245

**Records identified from other sources:**
- Citation searching: *[To be filled after manual citation search]*
- Hand searching: *[To be filled if applicable]*

---

## Screening

**Duplicates removed:** 16

**Records screened (title/abstract):** 229

**Records excluded at title/abstract screening:** *[To be filled after manual screening]*

**Records sought for full-text retrieval:** *[To be filled after abstract screening]*

**Records not retrieved:** *[To be filled if papers are inaccessible]*

---

## Eligibility

**Full-text articles assessed for eligibility:** *[To be filled after retrieving full texts]*

**Full-text articles excluded with reasons:** *[To be filled after full-text screening]*
- Reason 1: [count]
- Reason 2: [count]
- Reason 3: [count]

---

## Included

**Studies included in review:** *[To be filled after all screening complete]*

**Studies included in synthesis/analysis:** *[To be filled - may be same as above]*

---

## PRISMA Diagram (Text Format)

```
┌──────────────────────────────────────────────────────────────┐
│                      IDENTIFICATION                           │
├──────────────────────────────────────────────────────────────┤
│  Records from Scopus: 245                                    │
│    - Search 001 (XAI Methods): 146                           │
│    - Search 002 (Evaluation): 87                             │
│    - Search 003 (Falsifiability): 12                         │
│  Records from other sources: [TBD]                           │
│                                                              │
│  Total records identified: 245                               │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                       SCREENING                              │
├──────────────────────────────────────────────────────────────┤
│  Duplicates removed: 16                                      │
│                                                              │
│  Records screened: 229                                       │
│  ├─► Excluded (title/abstract): [TBD]                       │
│  │                                                           │
│  └─► Records for full-text retrieval: [TBD]                 │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                      ELIGIBILITY                             │
├──────────────────────────────────────────────────────────────┤
│  Full-text articles assessed: [TBD]                         │
│  ├─► Excluded (with reasons): [TBD]                          │
│  │                                                           │
│  └─► Articles not retrieved: [TBD]                           │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                        INCLUDED                              │
├──────────────────────────────────────────────────────────────┤
│  Studies included in review: [TBD]                          │
│  Studies included in synthesis: [TBD]                       │
└──────────────────────────────────────────────────────────────┘
```

---

## Search Provenance

**Search Execution Details:**

### XAI Methods in Face Recognition (`search_001_xai_face`)

- **Query:**
  ```
  TITLE-ABS-KEY("explainable AI" OR "explainability" OR ...)
  AND TITLE-ABS-KEY("face recognition" OR "face verification" OR ...)
  ```
- **Date Range:** 2015 - 2025
- **Subject Areas:** COMP, ENGI
- **Document Types:** ar, cp, re
- **Execution Date:** 2025-10-16T09:20:22
- **Results:** 146 papers
- **API Calls:** 6

[... additional searches ...]

---

## Notes

- This PRISMA diagram is automatically updated from Scopus search results
- Manual screening phases (title/abstract, full-text) must be updated manually
- Citation searching and hand searching must be documented separately
- All search queries are version-controlled in `config/search_queries.yaml`
- Complete reproducibility: execute `python scopus_search.py` with same config
```

---

## Phase 3: Import to Reference Manager (5 minutes)

### Step 3.1: Import to Zotero

1. Open Zotero
2. File → Import
3. Choose: `exports/deduplicated/all_results_2025-10-16.ris`
4. Select: "Literature Review - Falsifiable Attribution"
5. Import

**Result:** 229 papers imported to Zotero

### Step 3.2: Verify Import

```
Zotero Library: Literature Review - Falsifiable Attribution
├─ Search 001: XAI Methods (138 papers after dedup)
├─ Search 002: XAI Evaluation (79 papers after dedup)
└─ Search 003: Falsifiability (12 papers)

Total: 229 unique papers
```

---

## Phase 4: Manual Screening (Weeks 3-5)

### Step 4.1: Title Screening

**📄 File:** `exports/deduplicated/screening_deduplicated_2025-10-16.csv`

Open in Excel/Google Sheets and add screening decisions:

| EID | Title | Authors | Year | Title_Screen | Exclusion_Reason |
|-----|-------|---------|------|--------------|------------------|
| 2-s2.0-85123... | Explainable Face Recognition... | Smith et al. | 2023 | Include | |
| 2-s2.0-85124... | Neural Networks for Image... | Jones | 2022 | Exclude | Not about XAI |
| 2-s2.0-85125... | SHAP Values in Deep Learning | Brown et al. | 2021 | Uncertain | |

**After Title Screening:**
- Included: 78 papers
- Excluded: 142 papers (reasons documented)
- Uncertain: 9 papers → move to abstract screening

### Step 4.2: Abstract Screening

For 78 + 9 = 87 papers, read abstracts:

- Included for full-text: 52 papers
- Excluded at abstract: 35 papers

**Common Exclusion Reasons:**
1. Not about XAI (just face recognition) - 58 papers
2. Not about face recognition (just XAI in general) - 47 papers
3. Survey paper without original contribution - 12 papers
4. Insufficient methodological detail - 15 papers
5. Below quality threshold - 10 papers

### Step 4.3: Full-Text Screening

Retrieve full texts for 52 papers:
- Institutional access: 48 papers
- Author contact needed: 4 papers (sent requests)

After full-text screening:
- **Final included:** 38 papers
- Excluded at full-text: 14 papers (reasons: methodology unclear, duplicate study, etc.)

**Update PRISMA diagram manually with these numbers**

---

## Phase 5: Data Extraction (Weeks 6-7)

### Step 5.1: Setup Synthesis Matrix

**📄 File:** Use `PHD_PIPELINE/tools/literature_review/synthesis_matrix_template.csv`

Modified for this review:

| Citation | Year | XAI_Method | Face_System | Evaluation_Metric | Key_Finding | Relevance_RQ1 | Relevance_RQ2 | Quality |
|----------|------|------------|-------------|-------------------|-------------|---------------|---------------|---------|
| Smith 2023 | 2023 | Grad-CAM | ArcFace | Fidelity | ... | High | Medium | A |
| Jones 2022 | 2022 | SHAP | FaceNet | User study | ... | High | High | A |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

Extract data from all 38 papers systematically.

---

## Phase 6: Documentation for Dissertation

### Methodology Chapter (Section 2.3)

**📄 File:** `chapters/chapter_02_literature_review.md` (excerpt)

```markdown
### 2.3.1 Systematic Literature Search

A systematic literature search was conducted following PRISMA guidelines
(Page et al., 2021) to identify papers on explainable AI methods for
face recognition systems. The search was executed on October 16, 2025,
using the Scopus database via the Scopus Search API (Elsevier, 2025).

**Search Strategy:**

Three complementary searches were designed to capture different aspects
of the research topic:

1. **Search 001: XAI Methods in Face Recognition** - Primary search
   covering explainable AI methods applied to face recognition systems
2. **Search 002: XAI Evaluation Metrics** - Supplementary search
   focusing on evaluation methodologies for explainable AI
3. **Search 003: Falsifiability in XAI** - Gap analysis search to
   establish novelty of our approach

Complete search strings are provided in Appendix A. All searches were
limited to peer-reviewed articles and conference papers published
between 2015-2025 in Computer Science and Engineering domains.

**Search Execution:**

The automated pipeline executed 245 initial searches across three
queries, with all queries, parameters, and results fully documented
for reproducibility. Deduplication using three strategies (exact DOI
matching, title+author matching, and fuzzy title matching with 85%
threshold) identified 16 duplicates (6.5%), resulting in 229 unique
papers for screening.

**Screening Process:**

Papers were screened in three phases following predefined
inclusion/exclusion criteria (see Appendix B):

- **Title screening:** 229 papers reviewed, 87 advanced to abstract
  screening (142 excluded: 58 not about XAI, 47 not about face
  recognition, 37 other reasons)
- **Abstract screening:** 87 papers reviewed, 52 advanced to full-text
  screening (35 excluded: insufficient detail, below quality threshold)
- **Full-text screening:** 52 full texts assessed, 38 included in final
  review (14 excluded: methodology unclear, duplicate data)

Figure 2.1 shows the complete PRISMA flow diagram documenting this process.

**Reproducibility:**

All search queries, API parameters, execution logs, and screening decisions
are archived in version-controlled files. The search can be reproduced by
executing the provided scripts with archived configuration files. Raw API
responses are preserved in JSON format with complete metadata and timestamps.

[References to: Appendix A (Search Strings), Appendix B (Criteria), Figure 2.1 (PRISMA)]
```

### Appendix A: Complete Search Strings

```markdown
# Appendix A: Systematic Search Strings

**Database:** Scopus (via Search API)
**Date Executed:** October 16, 2025
**Total Results:** 245 papers (229 unique after deduplication)

---

## Search 001: XAI Methods in Face Recognition

**Query ID:** search_001_xai_face
**Description:** Primary search for explainable AI methods in face recognition

**Search String:**
```
TITLE-ABS-KEY("explainable AI" OR "explainability" OR "interpretable" OR
"interpretability" OR "XAI" OR "transparent" OR "attribution method" OR
"saliency map" OR "SHAP" OR "LIME" OR "Grad-CAM" OR "integrated gradients")
AND TITLE-ABS-KEY("face recognition" OR "face verification" OR
"face identification" OR "facial recognition" OR "facial biometrics" OR
"face matching" OR "face authentication")
```

**Filters:**
- Date Range: 2015-2025
- Subject Areas: COMP (Computer Science), ENGI (Engineering)
- Document Types: ar (Article), cp (Conference Paper), re (Review)

**Results:** 146 papers
**Research Questions:** RQ1, RQ2

---

## Search 002: XAI Evaluation Metrics

[... similar format ...]

---

## Search 003: Falsifiability in XAI

[... similar format ...]
```

### Appendix B: Inclusion/Exclusion Criteria

[Include the full criteria from Phase 1, Step 1.2]

### Figure 2.1: PRISMA Flow Diagram

[Include visual PRISMA diagram generated from prisma_flow_diagram.md - can be created using http://prisma.thetacollaborative.ca/ or LaTeX/TikZ]

---

## Complete File Tree

```
falsifiable_attribution_dissertation/
├── config.yaml
├── literature_review/
│   ├── inclusion_exclusion_criteria.md   ← Phase 1
│   ├── search_queries.yaml               ← Phase 1
│   ├── results/                          ← Phase 2
│   │   ├── search_001_*.json
│   │   ├── search_002_*.json
│   │   └── search_003_*.json
│   ├── exports/                          ← Phase 2
│   │   ├── all_results_2025-10-16.bib
│   │   ├── all_results_2025-10-16.ris
│   │   ├── screening_2025-10-16.csv
│   │   └── deduplicated/
│   │       └── screening_deduplicated_2025-10-16.csv
│   ├── logs/                             ← Phase 2
│   │   ├── search_log_2025-10-16.md
│   │   └── search_queries_2025-10-16.yaml
│   ├── reports/                          ← Phase 2
│   │   ├── deduplication_report_2025-10-16.md
│   │   ├── duplicates_2025-10-16.csv
│   │   └── prisma_report_2025-10-16.md
│   ├── prisma_flow_diagram.md            ← Phase 2
│   ├── synthesis_matrix.csv              ← Phase 5
│   └── synthesis_by_theme.md             ← Phase 5
├── chapters/
│   └── chapter_02_literature_review.md   ← Phase 6
└── appendices/
    ├── appendix_a_search_strings.md      ← Phase 6
    └── appendix_b_criteria.md            ← Phase 6
```

---

## Summary Statistics

### Search Execution
- **Databases Searched:** 1 (Scopus)
- **Search Queries:** 3
- **Total Records Retrieved:** 245
- **Execution Time:** 14.5 seconds
- **API Calls:** 14

### Deduplication
- **Duplicates Found:** 16 (6.5%)
- **Unique Records:** 229
- **DOI Matches:** 8
- **Title+Author Matches:** 5
- **Fuzzy Matches:** 3

### Screening
- **Title Screening:** 229 → 87 (142 excluded)
- **Abstract Screening:** 87 → 52 (35 excluded)
- **Full-Text Screening:** 52 → 38 (14 excluded)
- **Final Included:** 38 papers

### Timeline
- **Week 1:** Planning and keyword development (5 hours)
- **Week 2:** Search execution and deduplication (30 minutes)
- **Weeks 3-4:** Title/abstract screening (15 hours)
- **Week 5:** Full-text screening (20 hours)
- **Weeks 6-7:** Data extraction (25 hours)
- **Weeks 8-10:** Synthesis and writing (30 hours)
- **Total:** 10 weeks, ~95 hours

---

## References for Methodology

**Cite in your dissertation:**

```bibtex
@misc{Elsevier2025Scopus,
  author = {Elsevier},
  title = {Scopus Search {API}},
  year = {2025},
  url = {https://dev.elsevier.com/},
  note = {Accessed: 2025-10-16}
}

@article{Page2021PRISMA,
  author = {Page, Matthew J and McKenzie, Joanne E and Bossuyt, Patrick M and others},
  title = {The {PRISMA} 2020 statement: an updated guideline for reporting systematic reviews},
  journal = {BMJ},
  volume = {372},
  pages = {n71},
  year = {2021},
  doi = {10.1136/bmj.n71}
}
```

---

**✅ This completes a full end-to-end literature review from search execution to dissertation documentation, all fully automated and reproducible!**
