# Scopus Search Queries - Quick Reference
## Dissertation: "Falsifiable Attribution for Face Verification"

**Date:** October 16, 2025
**Total Searches:** 7
**Expected Results:** 685-1,530 papers (before deduplication)

---

## How to Use This Document

1. **Copy the query** from the search you want to execute
2. **Go to** https://www.scopus.com/
3. **Click** "Advanced search"
4. **Paste** the query exactly as written
5. **Add filters** (date range, subject areas, document types)
6. **Execute** and review results

---

## SEARCH 1: XAI in Face Verification
**Priority:** HIGH | **Expected:** 100-300 papers | **RQs:** RQ1, RQ2, RQ3, RQ4

**QUERY:**
```
TITLE-ABS-KEY("explainable AI" OR "explainability" OR "XAI" OR "interpretable AI" OR "interpretability" OR "transparent AI" OR "attribution method" OR "attribution technique" OR "saliency map" OR "attention map" OR "feature attribution" OR "explanation method" OR "visual explanation" OR "heatmap explanation") AND TITLE-ABS-KEY("face recognition" OR "face verification" OR "face identification" OR "facial recognition" OR "facial verification" OR "face matching" OR "face biometric" OR "facial biometric" OR "face authentication" OR "facial analysis" OR "face comparison")
```

**FILTERS:**
- **Date:** 2016 to 2025
- **Subject areas:** Computer Science, Engineering, Mathematics, Multidisciplinary
- **Document types:** Article, Conference Paper, Review

---

## SEARCH 2: Specific XAI Techniques
**Priority:** HIGH | **Expected:** 200-500 papers | **RQs:** RQ2, RQ3

**QUERY:**
```
TITLE-ABS-KEY("Grad-CAM" OR "GradCAM" OR "Gradient-weighted Class Activation Mapping" OR "Class Activation Map" OR "SHAP" OR "Shapley" OR "Shapley value" OR "SHapley Additive exPlanations" OR "LIME" OR "Local Interpretable Model-agnostic Explanations" OR "Integrated Gradients" OR "integrated gradient" OR "gradient-based attribution" OR "DeepLIFT" OR "Layer-wise Relevance Propagation" OR "LRP" OR "SmoothGrad") AND TITLE-ABS-KEY("computer vision" OR "image classification" OR "image recognition" OR "visual recognition" OR "deep learning" OR "convolutional neural network" OR "CNN" OR "neural network")
```

**FILTERS:**
- **Date:** 2016 to 2025
- **Subject areas:** Computer Science, Engineering, Mathematics
- **Document types:** Article, Conference Paper, Review

---

## SEARCH 3: Faithfulness Evaluation
**Priority:** HIGH | **Expected:** 100-250 papers | **RQs:** RQ1, RQ2, RQ3

**QUERY:**
```
TITLE-ABS-KEY("faithfulness" OR "fidelity" OR "attribution faithfulness" OR "explanation faithfulness" OR "sanity check" OR "sensitivity analysis" OR "perturbation-based evaluation" OR "counterfactual" OR "counterfactual explanation" OR "contrastive explanation" OR "attribution evaluation" OR "explanation evaluation" OR "insertion deletion" OR "deletion metric" OR "infidelity" OR "ROAR") AND TITLE-ABS-KEY("explainable AI" OR "interpretability" OR "attribution method" OR "saliency map" OR "feature importance" OR "explanation method" OR "neural network explanation" OR "deep learning explanation")
```

**FILTERS:**
- **Date:** 2018 to 2025
- **Subject areas:** Computer Science, Engineering, Mathematics, Multidisciplinary
- **Document types:** Article, Conference Paper, Review

---

## SEARCH 4: Face Verification Architectures
**Priority:** HIGH | **Expected:** 150-400 papers | **RQs:** RQ2, RQ3

**QUERY:**
```
TITLE-ABS-KEY("ArcFace" OR "CosFace" OR "SphereFace" OR "FaceNet" OR "DeepFace" OR "metric learning" OR "deep metric learning" OR "angular margin" OR "additive margin" OR "triplet loss" OR "contrastive loss" OR "angular softmax" OR "cosine margin" OR "hypersphere embedding" OR "face embedding" OR "facial embedding") AND TITLE-ABS-KEY("face verification" OR "face recognition" OR "face identification" OR "facial recognition" OR "one-shot learning" OR "few-shot learning" OR "face matching" OR "face similarity")
```

**FILTERS:**
- **Date:** 2014 to 2025
- **Subject areas:** Computer Science, Engineering, Mathematics
- **Document types:** Article, Conference Paper, Review

---

## SEARCH 5: Legal and Forensic Context
**Priority:** MEDIUM | **Expected:** 80-200 papers | **RQs:** RQ4

**QUERY:**
```
TITLE-ABS-KEY("GDPR" OR "General Data Protection Regulation" OR "EU AI Act" OR "AI Act" OR "algorithmic accountability" OR "algorithmic transparency" OR "right to explanation" OR "Daubert standard" OR "wrongful arrest" OR "false identification" OR "misidentification" OR "forensic standard" OR "legal standard" OR "evidentiary standard") AND TITLE-ABS-KEY("face recognition" OR "facial recognition" OR "biometric" OR "face identification" OR "facial identification" OR "face matching" OR "biometric identification") AND TITLE-ABS-KEY("law enforcement" OR "forensic" OR "criminal justice" OR "police" OR "surveillance" OR "border control" OR "security" OR "investigative")
```

**FILTERS:**
- **Date:** 2016 to 2025
- **Subject areas:** Computer Science, Social Sciences, Decision Sciences, Multidisciplinary, Engineering
- **Document types:** Article, Conference Paper, Review

---

## SEARCH 6: Theoretical Foundations
**Priority:** MEDIUM | **Expected:** 50-150 papers | **RQs:** RQ1, RQ2

**QUERY:**
```
TITLE-ABS-KEY("manifold learning" OR "hypersphere" OR "unit hypersphere" OR "embedding space" OR "representation learning" OR "feature space" OR "latent space" OR "metric space" OR "angular distance" OR "cosine similarity" OR "embedding geometry") AND TITLE-ABS-KEY("attribution theory" OR "gradient analysis" OR "sensitivity analysis" OR "influence function" OR "feature importance" OR "neural network theory" OR "interpretability" OR "explainability" OR "attribution method")
```

**FILTERS:**
- **Date:** 2014 to 2025
- **Subject areas:** Computer Science, Mathematics, Engineering, Multidisciplinary
- **Document types:** Article, Conference Paper, Review

---

## SEARCH 7: Falsifiability Gap Analysis
**Priority:** HIGH | **Expected:** 5-30 papers | **RQs:** RQ1

**QUERY:**
```
TITLE-ABS-KEY("falsifiability" OR "falsifiable" OR "Popper" OR "Popperian" OR "demarcation criterion" OR "demarcation problem" OR "testability" OR "refutability" OR "empirical testability") AND TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretability" OR "machine learning explanation" OR "neural network explanation" OR "attribution method" OR "saliency map" OR "feature attribution" OR "model explanation")
```

**FILTERS:**
- **Date:** 2016 to 2025
- **Subject areas:** Computer Science, Multidisciplinary, Decision Sciences, Mathematics
- **Document types:** Article, Conference Paper, Review

**NOTE:** This is a **gap analysis search**. Expected to return very few papers (<30), which establishes the novelty of applying falsifiability criteria to XAI evaluation.

---

## Execution Checklist

### Before Running Each Search

- [ ] Copy query exactly as written (no modifications)
- [ ] Paste into Scopus Advanced Search
- [ ] Apply date range filter
- [ ] Apply subject area filter
- [ ] Apply document type filter
- [ ] Review first 10-20 results for relevance
- [ ] Record exact result count
- [ ] Record date and time of search

### After Running Each Search

- [ ] Export results to reference manager (RIS or BibTeX format)
- [ ] Save search in Scopus (for reproducibility)
- [ ] Document any issues or unexpected results
- [ ] Check that key papers are captured (see validation list below)

---

## Key Papers Validation List

**Your searches SHOULD capture these papers:**

**XAI Methods:**
- Selvaraju et al. (2017) - "Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization"
- Ribeiro et al. (2016) - "Why Should I Trust You? Explaining the Predictions of Any Classifier" (LIME)
- Lundberg & Lee (2017) - "A Unified Approach to Interpreting Model Predictions" (SHAP)
- Sundararajan et al. (2017) - "Axiomatic Attribution for Deep Networks" (Integrated Gradients)

**XAI Evaluation:**
- Adebayo et al. (2018) - "Sanity Checks for Saliency Maps"
- Hooker et al. (2019) - "A Benchmark for Interpretability Methods in Deep Neural Networks"

**Face Verification:**
- Taigman et al. (2014) - "DeepFace: Closing the Gap to Human-Level Performance"
- Schroff et al. (2015) - "FaceNet: A Unified Embedding for Face Recognition and Clustering"
- Liu et al. (2017) - "SphereFace: Deep Hypersphere Embedding for Face Recognition"
- Wang et al. (2018) - "CosFace: Large Margin Cosine Loss for Deep Face Recognition"
- Deng et al. (2019) - "ArcFace: Additive Angular Margin Loss for Deep Face Recognition"

**If these papers are missing, check:**
1. Date range filters
2. Subject area restrictions
3. Spelling of author names or titles (for manual search)

---

## Troubleshooting

### Query Returns 0 Results
- Check for typos in search query
- Verify date range is correct
- Remove subject area filters temporarily
- Test individual keywords separately

### Query Returns Too Many Results (>500)
- Add more specific terms to narrow scope
- Reduce date range (if justified)
- Use TITLE() instead of TITLE-ABS-KEY() for critical terms
- Add AND NOT to exclude common false positives

### Query Returns Too Few Results (<20, except Search 7)
- Add synonyms and related terms
- Expand date range
- Check for overly restrictive filters
- Test broader keyword combinations

### First 20 Results Are Irrelevant
- Keywords may be too broad or ambiguous
- Add more specific qualifying terms
- Use phrase matching ("exact phrase") instead of individual words
- Consider using proximity operators (W/n)

---

## Priority Execution Order

**Recommended sequence:**

1. **Search 1** (Primary - XAI in face verification) - Establishes core literature base
2. **Search 7** (Gap analysis - falsifiability) - Confirms novelty claim
3. **Search 2** (Specific XAI techniques) - Foundational methods literature
4. **Search 3** (Faithfulness evaluation) - Core evaluation literature
5. **Search 4** (Face verification architectures) - Technical background
6. **Search 5** (Legal/forensic context) - Application motivation
7. **Search 6** (Theoretical foundations) - Deep technical background

---

## Expected Total Results Summary

| Search | Expected Results | Priority |
|--------|------------------|----------|
| 1. XAI in face verification | 100-300 | HIGH |
| 2. Specific XAI techniques | 200-500 | HIGH |
| 3. Faithfulness evaluation | 100-250 | HIGH |
| 4. Face verification architectures | 150-400 | HIGH |
| 5. Legal/forensic context | 80-200 | MEDIUM |
| 6. Theoretical foundations | 50-150 | MEDIUM |
| 7. Falsifiability gap | 5-30 | HIGH |
| **TOTAL** | **685-1,530** | |

**After deduplication:** 400-800 unique papers expected

---

## Export Settings

**Recommended export format:** RIS or BibTeX

**Fields to export:**
- Authors
- Title
- Year
- Source (journal/conference)
- Volume, Issue, Pages
- DOI
- Abstract
- Keywords
- Cited by count

**Export in batches of 200** (Scopus limit for single export)

---

## Scopus Subject Area Codes

For reference when applying filters:

- **COMP** - Computer Science
- **ENGI** - Engineering
- **MATH** - Mathematics
- **MULT** - Multidisciplinary
- **SOCI** - Social Sciences
- **DECI** - Decision Sciences

---

## Document Type Codes

For reference when applying filters:

- **ar** - Article (journal article)
- **cp** - Conference Paper
- **re** - Review (systematic review, survey)

**Not included:**
- **ed** - Editorial
- **le** - Letter
- **no** - Note
- **sh** - Short Survey
- **bk** - Book
- **ch** - Book Chapter

---

## Quick Tips

1. **Always test in web interface first** before automating
2. **Save each search in Scopus** for reproducibility
3. **Document result counts immediately** - they may change over time
4. **Export in standard format** (RIS/BibTeX) for reference managers
5. **Check for duplicates** within and across searches
6. **Review first 20 results** to validate search quality
7. **Adjust queries if needed** and create new IDs (don't overwrite)

---

## Next Steps After Search Execution

1. **Import** results to reference manager (Zotero/Mendeley)
2. **Deduplicate** across all 7 searches
3. **Begin title screening** using inclusion/exclusion criteria
4. **Complete PRISMA flow diagram** documenting the process
5. **Extract data** to synthesis matrix for included papers

---

**All queries ready for execution. Good luck! 🔍**
