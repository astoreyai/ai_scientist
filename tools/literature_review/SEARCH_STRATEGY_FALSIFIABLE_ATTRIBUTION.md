# Systematic Literature Review Search Strategy
## Dissertation: "Falsifiable Attribution for Face Verification"

**Date:** October 16, 2025
**Researcher:** [Your Name]
**Search Queries File:** `scopus_search_queries_falsifiable_attribution.yaml`

---

## Executive Summary

This document describes the systematic literature review search strategy for a PhD dissertation investigating the falsifiability of explainable AI (XAI) methods in face verification systems.

**Key Statistics:**
- **Total Searches:** 7 comprehensive queries
- **Expected Results:** 685-1,530 papers (before deduplication)
- **Estimated Final Corpus:** 80-150 papers (after screening)
- **Date Range:** 2014-2025 (varies by search)
- **Primary Database:** Scopus

---

## Research Context

### Dissertation Topic
Testing whether explainable AI (XAI) methods produce falsifiable, faithful explanations for face verification systems.

### Core Research Problem
Current XAI methods (Grad-CAM, SHAP, LIME, Integrated Gradients) lack **falsifiability** - there is no systematic way to test whether explanations are actually faithful to model behavior.

### Proposed Solution
Counterfactual score prediction framework: if an attribution says feature X is important, perturbing X should predictably change verification scores.

### Research Questions
1. **RQ1:** Can attribution techniques satisfy formal falsifiability criteria?
2. **RQ2:** What are theoretical/empirical limits of attribution faithfulness in face verification?
3. **RQ3:** How do current methods (Grad-CAM, IG, SHAP, LIME) perform under falsifiability testing?
4. **RQ4:** What constitutes sufficient faithfulness for legal/forensic deployment?

---

## Search Strategy Overview

### Coverage Areas

The 7 searches systematically cover:

1. **PRIMARY INTERSECTION** - XAI methods in face verification (search_001)
2. **SPECIFIC METHODS** - Grad-CAM, SHAP, LIME, Integrated Gradients (search_002)
3. **EVALUATION** - Faithfulness, fidelity, counterfactual explanations (search_003)
4. **ARCHITECTURE** - ArcFace, CosFace, metric learning (search_004)
5. **LEGAL/FORENSIC** - Wrongful arrests, GDPR, EU AI Act (search_005)
6. **THEORETICAL** - Manifold learning, hypersphere embeddings (search_006)
7. **GAP ANALYSIS** - Falsifiability in XAI (search_007)

### Rationale for Multiple Searches

Rather than one broad search, we use 7 targeted searches because:

1. **Comprehensive coverage** - Each search targets a specific aspect
2. **Quality control** - Narrower searches = more relevant results
3. **Transparency** - Clear documentation of search logic
4. **Reproducibility** - Other researchers can validate/replicate
5. **Gap identification** - Search 7 explicitly identifies the novelty gap

---

## Search Descriptions

### SEARCH 1: XAI in Face Recognition/Verification
**Priority:** HIGH | **Expected Results:** 100-300 papers

**What it covers:**
- Core intersection of XAI and face biometrics
- Attribution methods applied to face recognition
- Explainability techniques for facial analysis systems

**RQs addressed:** RQ1, RQ2, RQ3, RQ4

**Key concept combinations:**
- Explainability methods × Face verification systems

**Date range:** 2016-2025 (modern deep learning + XAI era)

---

### SEARCH 2: Specific XAI Techniques
**Priority:** HIGH | **Expected Results:** 200-500 papers

**What it covers:**
- Literature on Grad-CAM, SHAP, LIME, Integrated Gradients
- Gradient-based and perturbation-based attribution methods
- Applications across computer vision tasks

**RQs addressed:** RQ2, RQ3

**Key concept combinations:**
- Specific XAI methods (Grad-CAM, SHAP, LIME, IG) × Computer vision

**Date range:** 2016-2025 (foundational XAI methods published 2016-2017)

**Note:** Broader than face-specific to capture foundational literature on these methods.

---

### SEARCH 3: Faithfulness and Fidelity Evaluation
**Priority:** HIGH | **Expected Results:** 100-250 papers

**What it covers:**
- Evaluation metrics for attribution faithfulness
- Sanity checks for saliency maps
- Counterfactual and contrastive explanations
- Perturbation-based evaluation (insertion/deletion, ROAR)

**RQs addressed:** RQ1, RQ2, RQ3

**Key concept combinations:**
- Faithfulness evaluation metrics × XAI methods

**Date range:** 2018-2025 (systematic XAI evaluation emerged after initial methods)

**Key papers expected:**
- "Sanity Checks for Saliency Maps" (2018)
- "The (Un)reliability of saliency methods" (2019)
- Counterfactual explanation frameworks

---

### SEARCH 4: Face Verification Architectures
**Priority:** HIGH | **Expected Results:** 150-400 papers

**What it covers:**
- ArcFace, CosFace, SphereFace architectures
- Metric learning and deep metric learning
- Hypersphere embeddings and angular margins
- Face embedding spaces

**RQs addressed:** RQ2, RQ3

**Key concept combinations:**
- Metric learning architectures × Face verification

**Date range:** 2014-2025 (DeepFace 2014 → modern angular margin methods)

**Key papers expected:**
- DeepFace (2014), FaceNet (2015)
- SphereFace (2017), CosFace (2018), ArcFace (2019)

---

### SEARCH 5: Legal and Forensic Context
**Priority:** MEDIUM | **Expected Results:** 80-200 papers

**What it covers:**
- GDPR compliance and right to explanation
- EU AI Act requirements
- Wrongful arrests and false identifications
- Forensic face recognition standards (Daubert)
- Algorithmic accountability and transparency

**RQs addressed:** RQ4

**Key concept combinations:**
- Legal/regulatory frameworks × Face recognition × Law enforcement

**Date range:** 2016-2025 (GDPR enforcement 2018, EU AI Act 2021-2024)

**Note:** Includes social sciences literature on AI ethics and policy.

---

### SEARCH 6: Theoretical Foundations
**Priority:** MEDIUM | **Expected Results:** 50-150 papers

**What it covers:**
- Manifold learning theory
- Hypersphere geometry and angular distances
- Representation learning and embedding spaces
- Theoretical foundations of attribution methods

**RQs addressed:** RQ1, RQ2

**Key concept combinations:**
- Manifold learning / embedding geometry × Attribution theory

**Date range:** 2014-2025

**Purpose:** Understand why standard attribution methods may fail in metric learning contexts with angular margins.

---

### SEARCH 7: Falsifiability Gap Analysis
**Priority:** HIGH | **Expected Results:** 5-30 papers

**What it covers:**
- Falsifiability and Popperian demarcation in XAI
- Testability and refutability of ML explanations
- Scientific validity of attribution methods

**RQs addressed:** RQ1

**Key concept combinations:**
- Falsifiability / Popper / testability × XAI / interpretability

**Date range:** 2016-2025

**CRITICAL:** This is a **gap analysis search**. Expected to return **very few papers**, which:
1. Demonstrates novelty of the research
2. Establishes that falsifiability has not been systematically applied to XAI
3. Justifies the dissertation's contribution

**If this search returns 100+ papers, the novelty claim is weakened.**
**If this search returns <20 papers, the novelty claim is strengthened.**

---

## Keyword Development Strategy

### Principles Applied

1. **Main terms + synonyms** - Cover all ways concepts are described
2. **Acronyms + full expansions** - "XAI" and "explainable AI"
3. **Technical variants** - "saliency map" vs "attribution map"
4. **UK/US spellings** - (less relevant for technical terms)
5. **Related concepts** - Include closely associated terms

### Example: XAI Concept

```yaml
xai_keywords:
  - "explainable AI"           # Main term
  - "XAI"                      # Acronym
  - "interpretable AI"         # Synonym
  - "interpretability"         # Noun form
  - "transparent AI"           # Related concept
  - "attribution method"       # Specific technique
  - "saliency map"             # Technical variant
  - "feature attribution"      # Broader term
```

### Concept Grouping Logic

Each search uses **2-4 concepts** connected with AND:
- **Within concepts:** Keywords connected with OR (any match)
- **Between concepts:** Concepts connected with AND (all must appear)

**Example:**
```
(Concept 1: explainability OR interpretability OR XAI)
AND
(Concept 2: face recognition OR face verification)
```

Result: Papers must mention BOTH XAI AND face systems.

---

## Boolean Query Structure

### Scopus Syntax Used

**Field code:**
```
TITLE-ABS-KEY("term")
```
Searches in title, abstract, and author keywords (recommended for comprehensiveness).

**Boolean operators:**
- `OR` - Within concept (any term matches)
- `AND` - Between concepts (all concepts required)
- `"quotes"` - Exact phrase matching

**Example query:**
```
TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretability")
AND TITLE-ABS-KEY("face recognition" OR "face verification")
```

### Wildcards (Minimal Use)

Wildcards are used sparingly to avoid noise:
- `comput*` → computer, computing, computation
- `interpret*` → interpretable, interpretation, interpreted

**Avoided:**
- `data*` - Too broad (database, datasheet, etc.)
- `AI*` - Too broad (AIDS, air, etc.)

---

## Date Ranges and Rationale

| Search | Start Year | Rationale |
|--------|------------|-----------|
| 1, 2, 5, 7 | 2016 | XAI methods (Grad-CAM, LIME, SHAP) published 2016-2017 |
| 3 | 2018 | Systematic XAI evaluation emerged after initial methods |
| 4, 6 | 2014 | Modern deep face recognition (DeepFace 2014) |

**End year:** All searches end at 2025 (current year).

---

## Subject Area Filters

**Primary areas:**
- `COMP` - Computer Science
- `ENGI` - Engineering
- `MATH` - Mathematics (for theoretical work)
- `MULT` - Multidisciplinary

**Additional areas (search 5 only):**
- `SOCI` - Social Sciences (for legal/policy papers)
- `DECI` - Decision Sciences

### Why these areas?
- Face verification is primarily computer science/engineering
- Theoretical foundations require mathematics
- Legal/forensic context requires social sciences

---

## Document Types

All searches include:
- `ar` - Journal articles (peer-reviewed)
- `cp` - Conference papers (peer-reviewed)
- `re` - Review articles (systematic reviews, surveys)

**Excluded:**
- Editorials, opinion pieces, news articles
- Books (searched separately if needed)
- Dissertations (searched separately if needed)

---

## Expected Results and Quality Estimates

### Before Deduplication

| Search | Expected Results |
|--------|------------------|
| 1 | 100-300 papers |
| 2 | 200-500 papers |
| 3 | 100-250 papers |
| 4 | 150-400 papers |
| 5 | 80-200 papers |
| 6 | 50-150 papers |
| 7 | 5-30 papers |
| **TOTAL** | **685-1,530 papers** |

### After Processing

1. **After deduplication:** 400-800 unique papers (40-50% overlap expected)
2. **After title screening:** 250-450 papers (50-60% relevant titles)
3. **After abstract screening:** 150-300 papers (60% relevant abstracts)
4. **After full-text screening:** 80-150 papers (50-60% meet inclusion criteria)

### Quality Indicators

**Good signs:**
- Search 1 returns 150-250 papers (sufficient coverage, not overwhelming)
- Search 7 returns <30 papers (confirms novelty gap)
- First 20 results from each search are highly relevant
- Overlap between searches is 30-50% (validates search strategy)

**Warning signs:**
- Search 1 returns <50 papers (too narrow, missing key terms)
- Search 1 returns >500 papers (too broad, needs refinement)
- Search 7 returns >100 papers (novelty claim weakened)
- First 20 results are mostly irrelevant (poor keyword choice)

---

## Execution Plan

### Step-by-Step Process

#### Phase 1: Query Validation (Day 1)
1. **Test each query in Scopus web interface**
   - Go to https://www.scopus.com/
   - Click "Advanced search"
   - Paste query from YAML file
   - Review first 20 results for relevance

2. **Check result counts**
   - Are they within expected ranges?
   - If too high/low, refine keywords

3. **Document any modifications**
   - Update YAML file if queries are changed
   - Note reasons for changes

#### Phase 2: Automated Execution (Day 2)
1. **Set up Scopus API** (if using automated pipeline)
   ```bash
   cd /home/aaron/projects/xai/PHD_PIPELINE/tools/literature_review/automated_scopus
   python scopus_search.py --dry-run  # Test configuration
   ```

2. **Execute searches** in priority order:
   - Search 1 (primary)
   - Search 7 (gap analysis)
   - Searches 2-6 (supporting)

3. **Export results** to reference manager (Zotero/Mendeley)

#### Phase 3: Deduplication (Day 3)
1. **Import all results** to reference manager
2. **Remove duplicates** (automatic + manual check)
3. **Export deduplicated set** for screening

#### Phase 4: Title Screening (Days 4-5)
- Screen all titles
- Decision: Include / Exclude / Uncertain
- Move "Include" and "Uncertain" to abstract screening

#### Phase 5: Abstract Screening (Days 6-8)
- Read abstracts for remaining papers
- Apply inclusion/exclusion criteria
- Document reasons for exclusion

#### Phase 6: Full-Text Screening (Days 9-14)
- Obtain full texts
- Apply full inclusion criteria
- Extract to synthesis matrix

---

## Priority Execution Order

**Recommended order:**

1. **Search 1** - Primary search (XAI in face verification)
   - Establishes core literature base
   - Highest relevance to all RQs

2. **Search 7** - Gap analysis (falsifiability)
   - Confirms novelty claim
   - Critical for establishing contribution

3. **Search 2** - Specific XAI techniques
   - Foundational literature on methods being tested

4. **Search 3** - Faithfulness evaluation
   - Core to RQ1, RQ2, RQ3

5. **Search 4** - Face verification architectures
   - Technical background for models being used

6. **Search 5** - Legal/forensic context
   - Motivation and application context

7. **Search 6** - Theoretical foundations
   - Deepest technical background

---

## Quality Assurance Checklist

### Before Execution
- [ ] All 7 queries tested in Scopus web interface
- [ ] Result counts within expected ranges (see table above)
- [ ] First 20 results from each search reviewed for relevance
- [ ] No Boolean syntax errors
- [ ] Date ranges appropriate for each search
- [ ] Subject areas cover all relevant disciplines
- [ ] All RQs covered by at least one search

### During Execution
- [ ] Search date and time documented for each query
- [ ] Exact result count recorded
- [ ] Any error messages or warnings noted
- [ ] Results exported in standard format (RIS/BibTeX)

### After Execution
- [ ] PRISMA flow diagram completed
- [ ] Deduplication rate calculated
- [ ] Screening decisions documented
- [ ] Inter-rater reliability calculated (if applicable)
- [ ] All exclusions justified with specific criteria

---

## Inclusion/Exclusion Criteria

### Inclusion Criteria (Papers MUST meet ALL)

**Time Period:**
- Published 2014-2025 (varies by search, see date ranges)

**Publication Types:**
- Peer-reviewed journal articles
- Peer-reviewed conference papers
- Systematic reviews / meta-analyses

**Language:**
- English only (standard for computer science)

**Content Criteria (at least one):**
- Discusses XAI methods in face recognition/verification
- Evaluates faithfulness/fidelity of attribution methods
- Describes face verification architectures (ArcFace, CosFace, etc.)
- Addresses legal/forensic use of face recognition
- Provides theoretical foundations for attribution or metric learning

### Exclusion Criteria (Papers EXCLUDED if)

- Editorials, opinion pieces, news articles
- Not peer-reviewed (unless gray literature is justified)
- Duplicate publications (same study, multiple venues)
- Non-English language
- No full text available (note for potential gray literature search)
- Focus on non-face biometrics (fingerprint, iris, etc.) without transferable insights
- Focus on face recognition for non-verification tasks (e.g., emotion recognition, age estimation) unless XAI methods are discussed
- Retracted or withdrawn publications
- No clear relevance to any of the 4 research questions

---

## Research Question Mapping

Each search explicitly addresses specific RQs:

| Search | RQ1 | RQ2 | RQ3 | RQ4 |
|--------|-----|-----|-----|-----|
| 1. XAI in face verification | ✓ | ✓ | ✓ | ✓ |
| 2. Specific XAI techniques | | ✓ | ✓ | |
| 3. Faithfulness evaluation | ✓ | ✓ | ✓ | |
| 4. Face verification architectures | | ✓ | ✓ | |
| 5. Legal/forensic context | | | | ✓ |
| 6. Theoretical foundations | ✓ | ✓ | | |
| 7. Falsifiability gap | ✓ | | | |

**Coverage validation:**
- ✓ RQ1 covered by searches 1, 3, 6, 7
- ✓ RQ2 covered by searches 1, 2, 3, 4, 6
- ✓ RQ3 covered by searches 1, 2, 3, 4
- ✓ RQ4 covered by searches 1, 5

---

## Validation and Refinement

### Testing in Scopus Web Interface

**Before automating, manually test each query:**

1. Go to https://www.scopus.com/
2. Click "Advanced search"
3. Paste query exactly as in YAML file
4. Review results

**What to check:**
- Result count within expected range?
- First 10-20 papers highly relevant?
- Key papers you know should be included are captured?
- Obvious irrelevant papers appearing?

### Refinement Rules

**If too many results (>expected upper bound):**
- Add more specific terms
- Use narrower date range (if justified)
- Add subject area filter
- Use TITLE() instead of TITLE-ABS-KEY() for key terms

**If too few results (<expected lower bound):**
- Add synonyms and related terms
- Remove overly specific terms
- Expand date range (if justified)
- Check for typos in keywords

**If irrelevant papers appearing:**
- Add more specific terms to clarify concepts
- Consider using AND NOT to exclude common false positives
- Use proximity operators (W/n) for phrase-like concepts

### Example Refinement

**Original query (too broad, 800 results):**
```
TITLE-ABS-KEY("explainability" OR "interpretability")
AND TITLE-ABS-KEY("face")
```

**Refined query (more specific, 200 results):**
```
TITLE-ABS-KEY("explainable AI" OR "XAI" OR "attribution method" OR "saliency map")
AND TITLE-ABS-KEY("face recognition" OR "face verification" OR "facial recognition")
```

---

## Integration with PhD Pipeline

### Where This Fits in Your Dissertation

**Workflow 02: Literature Review** (`PHD_PIPELINE/workflows/02_literature_review.md`)

This search strategy is **Step 2** of the literature review workflow:

1. Define research questions ✓ (already done)
2. **Develop search strategy ✓** (this document)
3. Execute searches (next step)
4. Screen results
5. Synthesize findings
6. Write Chapter 2

### Next Steps After Search Execution

1. **Import to reference manager** (Zotero recommended)
2. **Complete PRISMA flow diagram** (`tools/literature_review/prisma_flow_diagram_template.md`)
3. **Screen titles and abstracts** (use `tools/literature_review/inclusion_exclusion_criteria_template.md`)
4. **Extract data to synthesis matrix** (`tools/literature_review/synthesis_matrix_template.csv`)
5. **Write Chapter 2: Literature Review** (`templates/dissertation/chapter_02_literature_review.md`)

### Expected Timeline

- **Query validation:** 1 day
- **Search execution:** 1 day
- **Deduplication:** 1 day
- **Title screening:** 2 days
- **Abstract screening:** 3 days
- **Full-text screening:** 5-7 days
- **Data extraction:** 7-10 days
- **Synthesis and writing:** 14-21 days

**Total:** 5-7 weeks for complete literature review

---

## Documentation and Reproducibility

### Required Documentation

Create/update these files:

1. **Search protocol** - `search_protocol_template.md`
   - Document all decisions
   - Record search dates
   - Note any deviations

2. **PRISMA flow diagram** - `prisma_flow_diagram_template.md`
   - Track papers at each stage
   - Document exclusion reasons

3. **Synthesis matrix** - `synthesis_matrix_template.csv`
   - Extract key information from each paper
   - Map to research questions

4. **Search log** - Create new file
   - Date and time of each search
   - Exact query used
   - Result count
   - Any errors or issues

### Version Control

**Critical:** If you modify queries after execution:
1. **Do NOT edit existing queries** in YAML file
2. **Create new query IDs** (e.g., search_001_v2)
3. **Document why modification was needed**
4. **Keep old queries for transparency**

This ensures complete transparency and reproducibility.

---

## Contingency Plans

### If Search 1 Returns Too Few Papers (<50)

**Possible causes:**
- Keywords too specific
- Date range too narrow
- Missing key synonyms

**Solutions:**
1. Expand XAI keywords (add "visual explanation", "model explanation")
2. Expand face keywords (add "biometric", "facial analysis")
3. Test with broader date range (start 2014 instead of 2016)

### If Search 7 Returns Too Many Papers (>100)

**Implications:**
- Falsifiability may already be well-explored in XAI
- Novelty claim weakened

**Actions:**
1. Review papers carefully - are they actually about falsifiability?
2. Refine to Popperian falsifiability specifically
3. May need to narrow contribution to "falsifiability in face verification" specifically
4. Discuss with advisor - may need to adjust research framing

### If Overall Results Are Overwhelming (>2000 papers)

**Solutions:**
1. Add more restrictive filters (TITLE-only for key terms)
2. Narrow date ranges
3. Focus on journal articles only (exclude conference papers)
4. Add subject area restrictions
5. Consider two-stage screening (quick initial filter, then detailed)

### If Key Papers Are Missing

**Check:**
1. Are they in a different database? (Web of Science, IEEE Xplore)
2. Are they books/dissertations? (search separately)
3. Are they too recent? (arXiv, preprints)
4. Are they in excluded subject areas?

**Solutions:**
- Add backward/forward citation searching
- Add hand-searching of key venues
- Add gray literature search if needed

---

## Key Papers to Validate Search

Your searches **should** capture these foundational papers:

**XAI Methods:**
- Grad-CAM: Selvaraju et al. (2017) - "Grad-CAM: Visual Explanations..."
- LIME: Ribeiro et al. (2016) - "Why Should I Trust You?"
- SHAP: Lundberg & Lee (2017) - "A Unified Approach to Interpreting..."
- Integrated Gradients: Sundararajan et al. (2017) - "Axiomatic Attribution..."

**XAI Evaluation:**
- Adebayo et al. (2018) - "Sanity Checks for Saliency Maps"
- Hooker et al. (2019) - "A Benchmark for Interpretability Methods"

**Face Verification:**
- Taigman et al. (2014) - "DeepFace"
- Schroff et al. (2015) - "FaceNet"
- Deng et al. (2019) - "ArcFace"

**If any of these are missing, investigate and refine queries.**

---

## Contact and Support

**For questions about:**
- Scopus search syntax: https://dev.elsevier.com/sc_search_tips.html
- PRISMA methodology: http://prisma-statement.org/
- PhD pipeline tools: See `PHD_PIPELINE/README.md`

**For help with:**
- Query refinement: Test in Scopus web interface first
- API issues: Check `automated_scopus/README.md`
- Screening decisions: Use inclusion/exclusion criteria template

---

## Final Checklist Before Execution

- [ ] All 7 queries tested manually in Scopus
- [ ] Result counts are reasonable (685-1,530 total expected)
- [ ] First 20 results from each search are relevant
- [ ] All RQs covered by at least one search
- [ ] PRISMA flow diagram template ready
- [ ] Reference manager set up (Zotero/Mendeley)
- [ ] Search protocol documented
- [ ] Timeline allocated for screening (5-7 weeks)
- [ ] Inclusion/exclusion criteria finalized
- [ ] Synthesis matrix template ready

---

## Expected Outcomes

**After completing this systematic literature review, you will have:**

1. **Comprehensive coverage** of XAI in face verification (150-300 papers)
2. **Evidence of novelty gap** from search 7 (<30 papers on falsifiability)
3. **Strong theoretical foundation** from searches 2, 3, 4, 6
4. **Contextual motivation** from search 5 (legal/forensic)
5. **Transparent, reproducible methodology** for Chapter 2
6. **Clear positioning** of your contribution within existing literature

**This forms the foundation for a rigorous, defensible literature review chapter.**

---

## Status

**Current Status:** Search strategy complete, ready for execution

**Next Steps:**
1. Validate queries in Scopus web interface
2. Execute searches (manual or automated)
3. Begin PRISMA screening process

**Estimated Completion:** 5-7 weeks from search execution

---

**Good luck with your systematic literature review! 📚**
