# @inclusion-criteria - Define Paper Screening Criteria

Develop clear, systematic inclusion/exclusion criteria for literature review screening.

## Skill Type
**Category:** Literature Review
**Tier:** Core (Tier 1)
**Reusability:** Very High - every systematic review needs criteria

## What This Skill Does

1. Defines inclusion/exclusion criteria for PRISMA screening
2. Ensures systematic, reproducible paper selection
3. Reduces bias in literature selection
4. Documents screening rationale
5. Generates criteria table for Chapter 2

## Invocation

```
@inclusion-criteria [topic] [scope]
```

## PICO Framework

For structured criteria, use PICO:

- **P**opulation: What's being studied?
- **I**ntervention/Interest: What's being examined?
- **C**omparison: What's it compared to (if applicable)?
- **O**utcome: What results are measured?

## Input Format

### Simple Topic
```
@inclusion-criteria

Topic: Explainable AI for biometric face recognition
Goal: Systematic literature review
```

### With Scope
```
@inclusion-criteria

Topic: XAI methods for face verification
Scope:
- Date range: 2015-2024
- Language: English
- Study type: Peer-reviewed
- Methods: GradCAM, LIME, SHAP, etc.
- Datasets: Face recognition datasets
```

### From Research Questions
```
@inclusion-criteria

RQ: How do biometric-aware XAI methods compare to standard methods?

What papers should I include in my review?
```

## Output Examples

### Example 1: Comprehensive Criteria

**Input:**
```
@inclusion-criteria

Topic: XAI for biometric face recognition systems
Research questions:
1. What XAI methods exist for face recognition?
2. How are they evaluated?
3. What gaps exist?
```

**Output:**

```markdown
## Inclusion/Exclusion Criteria: XAI for Biometric Face Recognition

### Inclusion Criteria

Papers must meet **ALL** of the following:

#### 1. Population/Domain
✅ **Include:**
- Biometric face recognition systems
- Deep learning face models (CNNs, transformers)
- Face verification OR identification tasks

❌ **Exclude:**
- Non-face biometrics (fingerprint, iris, voice)
- Shallow models (e.g., eigenfaces, LBP)
- Face detection only (no recognition component)

---

#### 2. Intervention/Method
✅ **Include:**
- Explainable AI (XAI) methods
- Interpretability techniques
- Attribution methods
- Saliency/attention maps
- Feature visualization

**Examples:** GradCAM, LIME, SHAP, Integrated Gradients, attention mechanisms

❌ **Exclude:**
- No XAI component (just recognition performance)
- Intrinsically interpretable models (decision trees, linear models)
- General deep learning papers without explainability focus

---

#### 3. Comparison (if applicable)
✅ **Include:**
- Comparative studies of XAI methods
- Evaluation against baselines
- Quantitative performance metrics

⚠️ **Not required:** Single-method studies acceptable if well-evaluated

---

#### 4. Outcome/Metrics
✅ **Include:**
Papers reporting at least one of:
- Localization accuracy
- Human agreement/evaluation
- Faithfulness/fidelity metrics
- Consistency measures
- Attribution quality

❌ **Exclude:**
- Purely qualitative (no quantitative evaluation)
- No evaluation metrics reported

---

#### 5. Publication Type
✅ **Include:**
- Peer-reviewed journal articles
- Peer-reviewed conference papers (top-tier: CVPR, ICCV, ECCV, NeurIPS, ICML, etc.)
- Peer-reviewed workshop papers (if high quality)

❌ **Exclude:**
- Preprints (arXiv) without peer review
- Technical reports
- Theses/dissertations (cite original papers instead)
- Books/book chapters
- Posters/abstracts only

---

#### 6. Date Range
✅ **Include:** 2015-2024 (last 10 years)

**Rationale:**
- Deep learning for faces emerged ~2015 (FaceNet, VGGFace)
- GradCAM published 2017
- Captures modern XAI era

❌ **Exclude:** Pre-2015 (different model era)

---

#### 7. Language
✅ **Include:** English language only

**Rationale:**
- Predominant scientific language
- Feasibility constraint

❌ **Exclude:** Non-English papers

---

#### 8. Accessibility
✅ **Include:**
- Full text available (via institutional access, open access, or ILL)

❌ **Exclude:**
- Abstract-only
- Paywall with no access route

---

### Exclusion Criteria (Apply After Inclusions)

**Additional exclusions:**

1. **Duplicate studies:** Same dataset, method, authors → keep most comprehensive

2. **Insufficient detail:** Methods not reproducible, vague descriptions

3. **Non-empirical:** Opinion pieces, editorials, commentary (unless foundational theory)

4. **Off-topic:** Title/abstract seemed relevant but full-text reveals otherwise

---

### Screening Process

#### Stage 1: Title Screening
**Apply:** Publication type, date range, language, obvious off-topic

**Example decisions:**
- ✅ "GradCAM for Face Verification" (2023) → **Include**
- ❌ "Iris Recognition Systems" → **Exclude** (wrong biometric)
- ❌ "Face Recognition Survey" (2012) → **Exclude** (pre-2015)

---

#### Stage 2: Abstract Screening
**Apply:** Domain, method, outcome criteria

**Example decisions:**
- ✅ "We apply LIME to explain ArcFace..." → **Include**
- ❌ "We improve face recognition accuracy..." (no XAI) → **Exclude**
- ❌ "Qualitative analysis of explanations..." (no metrics) → **Exclude**

---

#### Stage 3: Full-Text Screening
**Apply:** All criteria, check quality and detail

**Example decisions:**
- ✅ Full methodology, datasets described, metrics reported → **Include**
- ❌ Methods vague, no quantitative results → **Exclude** (insufficient detail)
- ⚠️ Unclear → Discuss with advisor, document decision

---

### Decision Rules for Edge Cases

#### Edge Case 1: Borderline Date
**Paper from 2014 but highly cited foundational work?**

**Decision:** Include if foundational (e.g., original GradCAM)
**Document:** "Included 2 pre-2015 papers due to foundational importance"

---

#### Edge Case 2: Preprint Later Published
**arXiv version from 2022, published version 2023?**

**Decision:** Include only published version
**Document:** "Used peer-reviewed version when available"

---

#### Edge Case 3: Mixed Modalities
**Paper covers face + voice biometrics?**

**Decision:** Include if face results separable
**Exclusion:** If only combined results reported

---

#### Edge Case 4: Adjacent Domain
**General XAI paper that mentions faces as one example?**

**Decision:** Include if substantive face evaluation (>1 page, separate results)
**Exclusion:** If faces are token example (<1 paragraph)

---

### Criteria Table for Chapter 2

| Criterion | Inclusion | Exclusion |
|-----------|-----------|-----------|
| **Domain** | Biometric face recognition | Other biometrics, non-biometric |
| **Method** | XAI/interpretability | No explainability component |
| **Outcome** | Quantitative evaluation | Purely qualitative |
| **Publication** | Peer-reviewed journal/conference | Preprints, reports, theses |
| **Date** | 2015-2024 | Before 2015 |
| **Language** | English | Non-English |
| **Access** | Full text available | Abstract only |

---

### Documentation for Reproducibility

**In Chapter 2 (Methods section):**

> "We included peer-reviewed studies (2015-2024) that applied
> explainable AI methods to deep learning-based face recognition
> systems and reported quantitative evaluation metrics. Studies
> were excluded if they: (1) focused on non-face biometrics,
> (2) lacked explainability components, (3) provided only
> qualitative analysis, (4) were not peer-reviewed, or (5)
> were inaccessible. See Table 2.1 for complete criteria."

---

### Inter-Rater Reliability (if applicable)

If multiple reviewers:
- Screen 10% independently
- Calculate Cohen's kappa (κ)
- Target: κ > 0.70
- Resolve disagreements through discussion

---

### Expected Outcomes

Based on pilot search:
- **Initial identification:** ~500 papers
- **After title screening:** ~200 papers (60% excluded)
- **After abstract screening:** ~80 papers (60% excluded)
- **After full-text screening:** ~50 papers (38% excluded)

**Final inclusion:** ~50 papers for synthesis
```

### Example 2: Simple Criteria

**Input:**
```
@inclusion-criteria

Quick criteria for XAI + face recognition lit review.
I want recent, peer-reviewed, English papers.
```

**Output:**

```markdown
## Simple Inclusion Criteria: XAI for Face Recognition

### Include IF:
1. ✅ Topic: XAI methods applied to face recognition
2. ✅ Peer-reviewed (journal or top conference)
3. ✅ English language
4. ✅ Published 2018-2024 (last 7 years)
5. ✅ Quantitative results reported

### Exclude IF:
1. ❌ No face recognition component
2. ❌ No XAI/interpretability component
3. ❌ Preprint/unpublished
4. ❌ No quantitative evaluation
5. ❌ Published before 2018

---

### Screening Workflow

**Title screen:**
- Does title mention face recognition? (Yes → continue)
- Does title mention XAI/interpretability/explanation? (Yes → continue)

**Abstract screen:**
- Confirms face recognition task
- Confirms XAI method applied
- Reports quantitative results

**Full-text screen:**
- Methods described clearly
- Results presented with metrics
- Peer-reviewed publication confirmed

---

### Document for Chapter 2

> "We included peer-reviewed studies (2018-2024) applying
> explainable AI methods to face recognition systems with
> quantitative evaluation."
```

## Validation Checklist

Good criteria are:

- [ ] **Specific** - Clear what's in/out
- [ ] **Justified** - Rationale provided for each
- [ ] **Reproducible** - Another researcher would make same decisions
- [ ] **Aligned with RQs** - Criteria match research questions
- [ ] **Feasible** - Won't exclude everything (or include too much)
- [ ] **Documented** - Written down before screening

## Common Mistakes Fixed

### ❌ Mistake 1: Too Restrictive
"Only papers using GradCAM on VGGFace2"

**Problem:** May only find 3 papers.

✅ **Fix:** "Papers using any XAI method on any face dataset"

---

### ❌ Mistake 2: Too Broad
"Papers about AI or faces"

**Problem:** Will find 50,000 papers.

✅ **Fix:** "Papers applying XAI to face recognition"

---

### ❌ Mistake 3: Post-Hoc Criteria
Decide criteria AFTER seeing papers.

**Problem:** Selection bias, not systematic.

✅ **Fix:** Define criteria BEFORE searching.

---

### ❌ Mistake 4: Vague Criteria
"High quality papers"

**Problem:** What's "high quality"? Subjective.

✅ **Fix:** "Peer-reviewed in top-tier venues (CVPR, IEEE TPAMI...)"

## Time Savings

**Manual criteria development:** 2-3 hours (iterating, discussing with advisor)
**Using @inclusion-criteria:** 20-30 minutes
**Saved:** ~2 hours 🎉

## Best Practices

### 1. Define Before Searching
Criteria first, then search. Not the other way.

### 2. Pilot Test
Screen 20 papers, refine criteria if needed.

### 3. Document Decisions
Keep log of edge cases and decisions.

### 4. Independent Screening (if possible)
Two reviewers screen independently, resolve disagreements.

### 5. Be Systematic, Not Perfectionist
Aim for reproducibility, not finding every possible paper.

## Integration with Dissertation

### Chapter 2 (Methods Section)

```markdown
## 2.2 Literature Search Methodology

### 2.2.1 Search Strategy
We conducted a systematic literature review following PRISMA 2020
guidelines (Page et al., 2021).

### 2.2.2 Inclusion and Exclusion Criteria
[INSERT CRITERIA TABLE]

### 2.2.3 Screening Process
Papers were screened in three stages:

1. **Title screening:** Applied publication type, date, and
   language criteria (n=500 → 200)

2. **Abstract screening:** Applied domain, method, and outcome
   criteria (n=200 → 80)

3. **Full-text screening:** Applied quality and detail criteria
   (n=80 → 52 included)

See Figure 2.1 (PRISMA diagram) for details.
```

## Related Skills

- `/run-literature-search` - Execute search with criteria
- `/screen-papers` - Apply criteria systematically
- `@prisma-diagram` - Visualize screening process
- `@synthesis-matrix` - Organize included papers

## Field-Specific Notes

### STEM/Engineering
- Often methodological focus
- Datasets and metrics important
- Replication/reproducibility valued

### Social Sciences
- Population characteristics critical
- Study design important (RCT, observational, etc.)
- Theory/framework may be criterion

### Medical/Health
- PICO framework standard
- Study quality assessment (risk of bias)
- Systematic review protocols registered

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 20-30 minutes
**Time saved:** ~2 hours
**Reusability:** Very High (every systematic review)
**Critical for:** PRISMA compliance, reproducible review
