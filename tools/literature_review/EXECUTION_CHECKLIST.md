# Literature Review Execution Checklist
## Dissertation: "Falsifiable Attribution for Face Verification"

**Date:** October 16, 2025
**Status:** Ready for execution
**Estimated Time:** 5-7 weeks total

---

## PRE-EXECUTION CHECKLIST

### Week 0: Preparation (2-3 days)

#### Day 1: Setup and Validation
- [ ] **Reference manager installed** (Zotero or Mendeley recommended)
- [ ] **Scopus access confirmed** (university subscription or API key)
- [ ] **PRISMA flow diagram template** ready (`prisma_flow_diagram_template.md`)
- [ ] **Inclusion/exclusion criteria** finalized (`inclusion_exclusion_criteria_template.md`)
- [ ] **Synthesis matrix template** prepared (`synthesis_matrix_template.csv`)
- [ ] **Search protocol documented** (`search_protocol_template.md`)

#### Day 2: Query Testing
- [ ] **Open Scopus** → https://www.scopus.com/
- [ ] **Test Search 1** (XAI in face verification)
  - [ ] Copy query from `SCOPUS_QUERIES_QUICK_REFERENCE.md`
  - [ ] Paste into Advanced Search
  - [ ] Apply filters (date: 2016-2025, subjects: COMP/ENGI/MATH/MULT, types: ar/cp/re)
  - [ ] Result count: _____ (expected 100-300)
  - [ ] First 20 results relevant? YES / NO
  - [ ] Key papers captured? (DeepFace, FaceNet, Grad-CAM, LIME, SHAP) YES / NO

- [ ] **Test Search 7** (Falsifiability gap)
  - [ ] Copy query from quick reference
  - [ ] Apply filters (date: 2016-2025)
  - [ ] Result count: _____ (expected 5-30) ★ CRITICAL ★
  - [ ] If >100 papers → Note for discussion with advisor
  - [ ] First 20 results relevant? YES / NO

- [ ] **Test Search 2** (Specific XAI techniques)
  - [ ] Result count: _____ (expected 200-500)
  - [ ] First 20 results relevant? YES / NO

- [ ] **Test Search 3** (Faithfulness evaluation)
  - [ ] Result count: _____ (expected 100-250)
  - [ ] First 20 results relevant? YES / NO

- [ ] **Test Search 4** (Face verification architectures)
  - [ ] Result count: _____ (expected 150-400)
  - [ ] First 20 results relevant? YES / NO

- [ ] **Test Search 5** (Legal/forensic context)
  - [ ] Result count: _____ (expected 80-200)
  - [ ] First 20 results relevant? YES / NO

- [ ] **Test Search 6** (Theoretical foundations)
  - [ ] Result count: _____ (expected 50-150)
  - [ ] First 20 results relevant? YES / NO

#### Day 3: Refinement (if needed)
- [ ] **Review all test results**
  - [ ] Any queries returned 0 results? → Check for typos
  - [ ] Any queries returned way too many results? → Add narrowing terms
  - [ ] Any queries returned way too few results? → Add synonyms
  - [ ] First 20 results >80% relevant across all searches? → Good to go

- [ ] **Document any query modifications**
  - [ ] Create new query IDs if changes made (don't overwrite)
  - [ ] Note reasons for modifications in search protocol
  - [ ] Update YAML file if needed

- [ ] **Finalize execution plan**
  - [ ] Priority order confirmed: 1 → 7 → 2 → 3 → 4 → 5 → 6
  - [ ] Timeline allocated (see below)
  - [ ] All tools ready

---

## EXECUTION PHASE

### Week 1: Search Execution and Deduplication

#### Day 1-2: Execute All 7 Searches

**SEARCH 1: XAI in Face Verification (PRIMARY)**
- [ ] Open Scopus Advanced Search
- [ ] Copy query from `SCOPUS_QUERIES_QUICK_REFERENCE.md`
- [ ] Apply filters:
  - [ ] Date range: 2016 to 2025
  - [ ] Subject areas: COMP, ENGI, MATH, MULT
  - [ ] Document types: ar, cp, re
- [ ] **Execute search**
- [ ] **Record details:**
  - Date/time: ________________
  - Result count: _____ (expected 100-300)
  - Actual relevance: _____% (estimate from first 20)
- [ ] **Export results:**
  - [ ] Format: RIS or BibTeX
  - [ ] Filename: `search_001_xai_face_verification.ris`
  - [ ] Fields: Authors, Title, Year, Source, DOI, Abstract, Keywords
- [ ] **Save search in Scopus** (for reproducibility)

**SEARCH 7: Falsifiability Gap (NOVELTY)**
- [ ] Copy query from quick reference
- [ ] Apply filters (date: 2016-2025, subjects: COMP/MULT/DECI/MATH, types: ar/cp/re)
- [ ] **Execute search**
- [ ] **Record details:**
  - Date/time: ________________
  - Result count: _____ (expected 5-30) ★
  - Actual relevance: _____%
- [ ] **Export:** `search_007_falsifiability_gap.ris`
- [ ] **Save search in Scopus**
- [ ] **CRITICAL CHECK:** If >100 papers → Schedule advisor meeting

**SEARCH 2: Specific XAI Techniques**
- [ ] Copy query, apply filters (date: 2016-2025, subjects: COMP/ENGI/MATH, types: ar/cp/re)
- [ ] Execute, record (expected 200-500), export: `search_002_xai_techniques.ris`

**SEARCH 3: Faithfulness Evaluation**
- [ ] Copy query, apply filters (date: 2018-2025, subjects: COMP/ENGI/MATH/MULT, types: ar/cp/re)
- [ ] Execute, record (expected 100-250), export: `search_003_faithfulness_eval.ris`

**SEARCH 4: Face Verification Architectures**
- [ ] Copy query, apply filters (date: 2014-2025, subjects: COMP/ENGI/MATH, types: ar/cp/re)
- [ ] Execute, record (expected 150-400), export: `search_004_face_architectures.ris`

**SEARCH 5: Legal/Forensic Context**
- [ ] Copy query, apply filters (date: 2016-2025, subjects: COMP/SOCI/DECI/MULT/ENGI, types: ar/cp/re)
- [ ] Execute, record (expected 80-200), export: `search_005_legal_forensic.ris`

**SEARCH 6: Theoretical Foundations**
- [ ] Copy query, apply filters (date: 2014-2025, subjects: COMP/MATH/ENGI/MULT, types: ar/cp/re)
- [ ] Execute, record (expected 50-150), export: `search_006_theoretical.ris`

**TOTALS:**
- [ ] **Total papers retrieved:** _____ (expected 685-1,530)
- [ ] **All exports saved** to literature_review/ folder
- [ ] **All searches saved in Scopus** for reproducibility

#### Day 3: Import and Deduplication

**Import to Reference Manager:**
- [ ] Open Zotero/Mendeley
- [ ] Create collection: "Falsifiable_Attribution_Lit_Review"
- [ ] Import `search_001_xai_face_verification.ris`
- [ ] Import `search_002_xai_techniques.ris`
- [ ] Import `search_003_faithfulness_eval.ris`
- [ ] Import `search_004_face_architectures.ris`
- [ ] Import `search_005_legal_forensic.ris`
- [ ] Import `search_006_theoretical.ris`
- [ ] Import `search_007_falsifiability_gap.ris`

**Deduplication:**
- [ ] **Run automatic deduplication** in reference manager
- [ ] **Manual review** for missed duplicates (check titles, DOIs)
- [ ] **Record counts:**
  - Papers before deduplication: _____
  - Papers after deduplication: _____ (expected 400-800)
  - Deduplication rate: _____% (expected 30-50%)

**Quality Check:**
- [ ] **30-50% deduplication rate?** YES / NO
  - If <20% → Searches may be too disconnected (review strategy)
  - If >70% → Searches may be too overlapping (acceptable but note)
- [ ] **Export deduplicated set** for screening
  - Filename: `deduplicated_corpus.ris`

---

### Week 2: Title Screening

**Setup:**
- [ ] **Open spreadsheet** (Excel/Google Sheets)
- [ ] **Create columns:**
  - ID, Author, Year, Title, Decision (Include/Exclude/Uncertain), Reason, Screener

**Screening Process:**
- [ ] **Screen all titles** (_____ papers)
  - [ ] Decision rules:
    - **Include:** Mentions XAI/explainability AND face/biometric/verification
    - **Exclude:** Clearly off-topic (non-face, non-XAI, non-vision)
    - **Uncertain:** Move to abstract screening
  - [ ] **Daily target:** 100-150 titles/day
  - [ ] **Track progress:**
    - Day 1: _____ titles screened
    - Day 2: _____ titles screened
    - Day 3: _____ titles screened
    - Day 4: _____ titles screened
    - Day 5: _____ titles screened

**Results:**
- [ ] **Titles after screening:**
  - Include: _____ (expected 250-450)
  - Exclude: _____
  - Uncertain: _____
  - Total: _____

**Quality Check:**
- [ ] **50-60% retained?** YES / NO
  - If <30% → Too restrictive (review criteria)
  - If >80% → Too lenient (review criteria)

---

### Week 3: Abstract Screening

**Setup:**
- [ ] **Add abstract column** to spreadsheet
- [ ] **Retrieve abstracts** for Include + Uncertain papers

**Screening Process:**
- [ ] **Screen all abstracts** (_____ papers)
  - [ ] **Apply inclusion criteria:**
    - [ ] Published 2014-2025
    - [ ] Peer-reviewed (journal/conference)
    - [ ] Addresses at least one RQ
    - [ ] Sufficient methodological detail
  - [ ] **Apply exclusion criteria:**
    - [ ] Editorials, opinions, news
    - [ ] Non-English
    - [ ] Duplicate publications
    - [ ] No relevance to any RQ
  - [ ] **Daily target:** 50-80 abstracts/day
  - [ ] **Track progress:**
    - Day 1: _____ abstracts screened
    - Day 2: _____ abstracts screened
    - Day 3: _____ abstracts screened
    - Day 4: _____ abstracts screened
    - Day 5: _____ abstracts screened

**Results:**
- [ ] **Abstracts after screening:**
  - Include: _____ (expected 150-300)
  - Exclude: _____
  - Total: _____

**Quality Check:**
- [ ] **60% retained from abstract screening?** YES / NO

---

### Week 4: Full-Text Retrieval

**Obtain Full Texts:**
- [ ] **Download from publisher** (via university access)
  - [ ] Journal articles: _____ downloaded
  - [ ] Conference papers: _____ downloaded
- [ ] **Request via interlibrary loan** (if not accessible)
  - [ ] Requests submitted: _____
  - [ ] Received: _____
- [ ] **Check preprint servers** (arXiv, bioRxiv)
  - [ ] Papers found: _____
- [ ] **Contact authors** (if necessary)
  - [ ] Emails sent: _____
  - [ ] Responses: _____

**Document Access Issues:**
- [ ] **Papers not accessible:** _____ (list)
  - [ ] Mark as "excluded - no full text available"
  - [ ] Consider gray literature search if critical

**Organize Files:**
- [ ] **Create folder structure:**
  ```
  literature_review/
    full_texts/
      included/
      excluded/
      uncertain/
  ```
- [ ] **Rename files consistently:** `AuthorYear_ShortTitle.pdf`

---

### Week 5-6: Full-Text Screening

**Setup:**
- [ ] **Open synthesis matrix** (`synthesis_matrix_template.csv`)
- [ ] **Prepare extraction fields:**
  - Bibliographic info (author, year, title, venue)
  - Research question/hypothesis
  - Methodology (design, sample, measures)
  - Key findings (results, effect sizes)
  - Relevance to RQs (which RQs addressed?)
  - Quality assessment (high/medium/low)
  - Notes

**Screening Process:**
- [ ] **Read full texts** (_____ papers)
  - [ ] **Apply full inclusion/exclusion criteria**
  - [ ] **Extract data** to synthesis matrix for included papers
  - [ ] **Assess quality** using checklist
  - [ ] **Daily target:** 8-12 papers/day
  - [ ] **Track progress:**
    - Week 5, Day 1: _____ papers
    - Week 5, Day 2: _____ papers
    - Week 5, Day 3: _____ papers
    - Week 5, Day 4: _____ papers
    - Week 5, Day 5: _____ papers
    - Week 6, Day 1: _____ papers
    - Week 6, Day 2: _____ papers
    - Week 6, Day 3: _____ papers
    - Week 6, Day 4: _____ papers
    - Week 6, Day 5: _____ papers

**Results:**
- [ ] **Full-text screening results:**
  - Include: _____ (expected 80-150)
  - Exclude: _____
  - Reasons for exclusion (document):
    - Wrong topic: _____
    - Insufficient detail: _____
    - Non-peer-reviewed: _____
    - Duplicate: _____
    - Other: _____

**Quality Check:**
- [ ] **50-60% retained from full-text screening?** YES / NO
- [ ] **All exclusions documented with reasons?** YES / NO

---

### Week 7: Synthesis and Documentation

#### Complete PRISMA Flow Diagram
- [ ] **Fill in numbers at each stage:**
  - Records identified through database searching: _____
  - Records after duplicates removed: _____
  - Records screened (title): _____
  - Records excluded (title): _____
  - Full-text articles assessed: _____
  - Full-text articles excluded (with reasons): _____
  - Studies included in qualitative synthesis: _____

- [ ] **Create diagram** using `prisma_flow_diagram_template.md`
- [ ] **Save as figure** for Chapter 2

#### Finalize Synthesis Matrix
- [ ] **All included papers extracted?** YES / NO
- [ ] **Quality assessment complete?** YES / NO
- [ ] **RQ mapping complete?** YES / NO
- [ ] **Export to Excel/CSV** for analysis

#### Document Search Process
- [ ] **Update search protocol** with actual results
- [ ] **Note any deviations** from original plan
- [ ] **Calculate inter-rater reliability** (if applicable)
- [ ] **Archive all search files** (queries, exports, logs)

---

## POST-EXECUTION CHECKLIST

### Validation and Quality Assurance

**Coverage Validation:**
- [ ] **All 4 RQs covered?**
  - [ ] RQ1 (Falsifiability): _____ papers
  - [ ] RQ2 (Limits of faithfulness): _____ papers
  - [ ] RQ3 (Current methods): _____ papers
  - [ ] RQ4 (Legal/forensic): _____ papers

**Key Papers Captured:**
- [ ] **XAI Methods:**
  - [ ] Selvaraju et al. (2017) - Grad-CAM
  - [ ] Ribeiro et al. (2016) - LIME
  - [ ] Lundberg & Lee (2017) - SHAP
  - [ ] Sundararajan et al. (2017) - Integrated Gradients
- [ ] **XAI Evaluation:**
  - [ ] Adebayo et al. (2018) - Sanity Checks
  - [ ] Hooker et al. (2019) - Benchmark for Interpretability
- [ ] **Face Verification:**
  - [ ] Taigman et al. (2014) - DeepFace
  - [ ] Schroff et al. (2015) - FaceNet
  - [ ] Liu et al. (2017) - SphereFace
  - [ ] Wang et al. (2018) - CosFace
  - [ ] Deng et al. (2019) - ArcFace

**If key papers missing:**
- [ ] Add via backward citation search
- [ ] Add via forward citation search
- [ ] Add via hand search of key venues

**Novelty Gap Confirmed:**
- [ ] **Search 7 returned <30 papers?** YES / NO
  - If YES → Novelty claim strong
  - If NO (>100 papers) → Review novelty positioning with advisor

**Final Corpus Statistics:**
- [ ] **Total papers in final corpus:** _____ (expected 80-150)
- [ ] **Publication years:**
  - 2014-2016: _____
  - 2017-2019: _____
  - 2020-2022: _____
  - 2023-2025: _____
- [ ] **Document types:**
  - Journal articles: _____
  - Conference papers: _____
  - Reviews: _____
- [ ] **Top venues** (list top 5):
  1. _____
  2. _____
  3. _____
  4. _____
  5. _____

---

## WRITE CHAPTER 2: LITERATURE REVIEW

**Use template:** `PHD_PIPELINE/templates/dissertation/chapter_02_literature_review.md`

### Writing Phases (3-4 weeks)

**Week 1: Structure and Outline**
- [ ] **Map papers to sections** of chapter template
- [ ] **Create detailed outline**
- [ ] **Identify key themes** and organizing principles
- [ ] **Plan synthesis approach** (chronological? thematic? by RQ?)

**Week 2-3: First Draft**
- [ ] **Section 2.1:** Introduction to literature review
- [ ] **Section 2.2:** XAI methods (Grad-CAM, SHAP, LIME, IG)
- [ ] **Section 2.3:** Faithfulness evaluation
- [ ] **Section 2.4:** Face verification systems (ArcFace, CosFace)
- [ ] **Section 2.5:** Legal/forensic context
- [ ] **Section 2.6:** Theoretical foundations
- [ ] **Section 2.7:** Research gap (falsifiability)
- [ ] **Section 2.8:** Conclusion and positioning

**Week 4: Revision**
- [ ] **Check all citations** are accurate
- [ ] **Ensure all claims** are supported
- [ ] **Verify synthesis** (not just summarizing)
- [ ] **Check quality checklist** from template
- [ ] **Advisor review** and feedback

---

## TROUBLESHOOTING

### If Search 1 Returns <50 Papers
**Problem:** Too restrictive
**Solution:**
- [ ] Add synonyms (e.g., "visual explanation", "model explanation")
- [ ] Expand date range to 2014
- [ ] Broaden face terms (add "biometric", "facial analysis")

### If Search 7 Returns >100 Papers
**Problem:** Novelty claim weakened
**Solution:**
- [ ] Review papers - are they actually about falsifiability?
- [ ] Narrow to Popperian falsifiability specifically
- [ ] Focus on face verification context
- [ ] Discuss with advisor - may need to reframe contribution

### If Overall Results >2000 Papers
**Problem:** Too many to screen
**Solution:**
- [ ] Add TITLE-only searches for key terms
- [ ] Narrow date ranges
- [ ] Exclude conference papers (keep journals + reviews only)
- [ ] Add more restrictive subject area filters

### If Key Papers Missing
**Problem:** Search not comprehensive
**Solution:**
- [ ] Check other databases (Web of Science, IEEE Xplore)
- [ ] Run backward citation search (check references of key papers)
- [ ] Run forward citation search (who cited key papers?)
- [ ] Hand search key venues (CVPR, ICCV, NeurIPS, ICML)

---

## TIMELINE SUMMARY

| Phase | Duration | Status |
|-------|----------|--------|
| Preparation | 2-3 days | [ ] |
| Search execution | 2 days | [ ] |
| Deduplication | 1 day | [ ] |
| Title screening | 5 days | [ ] |
| Abstract screening | 5 days | [ ] |
| Full-text retrieval | 5 days | [ ] |
| Full-text screening | 10 days | [ ] |
| Synthesis & documentation | 5 days | [ ] |
| Writing Chapter 2 | 21-28 days | [ ] |
| **TOTAL** | **7-9 weeks** | [ ] |

---

## FINAL DELIVERABLES

**By end of literature review, you will have:**

- [ ] **PRISMA flow diagram** (Figure for Chapter 2)
- [ ] **Synthesis matrix** (80-150 papers extracted)
- [ ] **Search protocol** (fully documented)
- [ ] **Bibliography** (150-200 references in BibTeX)
- [ ] **Chapter 2 draft** (15,000-20,000 words)
- [ ] **Research gap identified** (novelty confirmed)
- [ ] **Positioning statement** (how your work fits)

---

## NOTES SECTION

Use this space to document issues, decisions, or observations:

```
Date: ___________
Note: ____________________________________________
_______________________________________________
_______________________________________________

Date: ___________
Note: ____________________________________________
_______________________________________________
_______________________________________________

Date: ___________
Note: ____________________________________________
_______________________________________________
_______________________________________________
```

---

**Status:** Ready for execution ✅

**Next step:** Begin Week 0, Day 1 (Setup and Validation)

**Good luck! 📚**
