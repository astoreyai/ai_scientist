# @experiment-design - Design Rigorous Experiments

Design scientifically rigorous experiments for your dissertation research.

## Skill Type
**Category:** Methodology / Experimental Design
**Tier:** Specialized (Tier 2)
**Reusability:** High - every empirical study needs experiment design

## What This Skill Does

1. Designs complete experimental protocols
2. Identifies independent and dependent variables
3. Specifies experimental conditions and controls
4. Plans data collection procedures
5. Ensures internal and external validity
6. Creates preregistration documents

## Invocation

```
@experiment-design [research-question] [variables]
```

## Experimental Design Components

### 1. Research Question
Clear, specific, testable question

### 2. Variables
- **Independent Variable (IV):** What you manipulate
- **Dependent Variable (DV):** What you measure
- **Control Variables:** What you hold constant
- **Confounding Variables:** What you need to address

### 3. Design Type
- **Between-subjects:** Different participants in each condition
- **Within-subjects:** Same participants in all conditions
- **Mixed design:** Combination of between and within
- **Factorial:** Multiple IVs crossed

### 4. Experimental Conditions
- **Treatment groups:** Different levels of IV
- **Control group:** Baseline comparison
- **Sample size:** Per condition (from power analysis)

### 5. Procedure
- Step-by-step protocol
- Randomization strategy
- Blinding (if applicable)
- Data collection method

### 6. Validity Considerations
- **Internal validity:** Can you claim causation?
- **External validity:** Can you generalize?
- **Construct validity:** Are you measuring what you intend?
- **Statistical conclusion validity:** Appropriate analysis?

## Input Format

### Simple Research Question
```
@experiment-design

RQ: Does BiometricGradCAM improve localization accuracy compared to GradCAM?

Context:
- Face verification system
- XAI method comparison
- Continuous outcome (accuracy)
```

### Complex Multi-Factor Design
```
@experiment-design

RQ: How do XAI method and dataset affect explanation quality?

Factors:
- Method: 4 levels (GradCAM, LIME, IG, BiometricGradCAM)
- Dataset: 2 levels (VGGFace2, LFW)
- Design: 4×2 factorial
```

### With Detailed Context
```json
{
  "research_question": "Does verification-aware XAI improve explanation consistency?",
  "iv": {
    "name": "XAI method",
    "levels": ["BiometricGradCAM", "GradCAM"],
    "type": "categorical"
  },
  "dv": {
    "name": "Explanation consistency",
    "scale": "continuous (0-1)",
    "metric": "cosine similarity"
  },
  "sample_size": 200,
  "control_variables": ["model architecture", "image resolution"]
}
```

## Output Examples

### Example 1: Two-Group Comparison Experiment

**Input:**
```
@experiment-design

RQ: Does BiometricGradCAM achieve higher localization accuracy than GradCAM in face verification?

Variables:
- IV: XAI method (BiometricGradCAM vs GradCAM)
- DV: Localization accuracy (IoU with ground-truth)
- Context: Face verification using ArcFace model
```

**Output:**

```markdown
# Experimental Design: BiometricGradCAM vs GradCAM

## 1. Research Question

**Primary RQ:**
> Does BiometricGradCAM achieve higher localization accuracy than GradCAM when applied to face verification systems?

**Directional Hypothesis:**
> H₁: BiometricGradCAM will achieve significantly higher localization accuracy (measured by IoU) compared to standard GradCAM.

**Justification:**
BiometricGradCAM explicitly incorporates verification constraints (pairwise similarity, biometric decision boundaries), which should produce more accurate spatial attributions aligned with facial features.

---

## 2. Variables

### Independent Variable (IV)
- **Name:** XAI Method
- **Type:** Categorical (2 levels)
- **Levels:**
  1. **BiometricGradCAM** (experimental condition)
  2. **GradCAM** (baseline/control)
- **Operationalization:**
  - Both methods applied to same ArcFace-ResNet100 model
  - Same layer for attribution extraction (layer4)
  - Same post-processing (resize, normalize)

### Dependent Variable (DV)
- **Name:** Localization Accuracy
- **Type:** Continuous (ratio scale)
- **Range:** 0-1 (0% to 100% overlap)
- **Metric:** Intersection over Union (IoU)
- **Formula:** IoU = (Attribution ∩ Ground-Truth) / (Attribution ∪ Ground-Truth)
- **Ground Truth:** Facial landmark regions (eyes, nose, mouth)

### Control Variables (Held Constant)
1. **Model architecture:** ArcFace-ResNet100 (same weights)
2. **Image resolution:** 112×112 pixels
3. **Face alignment:** MTCNN preprocessing
4. **Dataset:** VGGFace2 test set
5. **Hardware:** Same GPU (NVIDIA A100)
6. **Software versions:** PyTorch 2.0.1, Python 3.9

### Potential Confounding Variables
1. **Image quality:** Control via inclusion criteria (resolution >112px, face visible)
2. **Face pose:** Stratify by pose variation (frontal, profile)
3. **Identity difficulty:** Balance genuine/impostor similarities

---

## 3. Experimental Design Type

**Design:** Between-subjects (independent groups)

**Why Between-Subjects?**
- Each verification pair evaluated with ONE XAI method
- Prevents carryover effects
- Ensures independence assumption for t-test
- Simpler implementation (no counterbalancing needed)

**Alternative Considered:**
- Within-subjects (same pairs, both methods) → rejected due to increased complexity without clear benefit

---

## 4. Experimental Conditions

### Condition 1: BiometricGradCAM
- **n = 200** verification pairs
- Method: BiometricGradCAM (verification-aware)
- Procedure: Generate attributions for both images in each pair
- Output: Localization accuracy (IoU) per pair

### Condition 2: GradCAM (Baseline)
- **n = 200** verification pairs (different from Condition 1)
- Method: Standard GradCAM
- Procedure: Generate attributions for both images in each pair
- Output: Localization accuracy (IoU) per pair

**Total sample:** N = 400 verification pairs

---

## 5. Sampling and Assignment

### Population
Face verification pairs from VGGFace2 test set

### Sampling Strategy
**Stratified random sampling:**
- 100 genuine pairs (same identity)
- 100 impostor pairs (different identities)
- Per condition (total: 200 genuine + 200 impostor)

**Stratification Criteria:**
1. **Identity representation:** No identity appears in >5 pairs
2. **Pose variation:** 60% frontal, 40% non-frontal
3. **Similarity distribution:**
   - Genuine: Cosine similarity 0.65-0.80
   - Impostor: Cosine similarity 0.15-0.30

### Random Assignment
- **Step 1:** Sample 400 verification pairs (200 genuine + 200 impostor)
- **Step 2:** Randomly assign to conditions (200 per method)
- **Step 3:** Ensure stratification maintained in both groups
- **Verification:** Check balance on confounds (pose, similarity)

---

## 6. Procedure

### Phase 1: Data Preparation (Before Experiment)
1. **Select VGGFace2 pairs** using stratified sampling
2. **Preprocess images** (MTCNN alignment, resize to 112×112)
3. **Obtain ground-truth landmarks** (facial keypoints)
4. **Define ROIs** from landmarks (eyes, nose, mouth regions)
5. **Randomly assign** pairs to BiometricGradCAM or GradCAM condition
6. **Verify balance** (t-test on similarity distributions)

### Phase 2: Attribution Generation (Experiment Execution)
**Per verification pair:**

**Step 1:** Load image pair (img1, img2)

**Step 2:** Extract embeddings
```python
emb1 = model.extract_features(img1)
emb2 = model.extract_features(img2)
```

**Step 3:** Compute verification similarity
```python
similarity = cosine_similarity(emb1, emb2)
```

**Step 4:** Generate attribution (method-specific)

**For GradCAM:**
```python
attribution1 = gradcam.generate(img1, target_layer='layer4')
attribution2 = gradcam.generate(img2, target_layer='layer4')
```

**For BiometricGradCAM:**
```python
attribution1, attribution2 = biometric_gradcam.generate_pair(
    img1, img2,
    similarity=similarity,
    verification_threshold=0.5
)
```

**Step 5:** Compute IoU with ground-truth ROIs
```python
iou1 = compute_iou(attribution1, ground_truth_roi1)
iou2 = compute_iou(attribution2, ground_truth_roi2)
mean_iou = (iou1 + iou2) / 2
```

**Step 6:** Record results
```python
results.append({
    'pair_id': pair_id,
    'method': method,
    'genuine': is_genuine,
    'iou': mean_iou,
    'similarity': similarity
})
```

### Phase 3: Data Analysis (After Data Collection)
1. **Descriptive statistics** (M, SD, range per condition)
2. **Assumption checking** (normality, homogeneity)
3. **Hypothesis test** (independent t-test, one-tailed)
4. **Effect size** (Cohen's d with 95% CI)
5. **Visualization** (boxplots, violin plots)

---

## 7. Sample Size Justification

**A priori power analysis:**
- Test: Independent t-test (one-tailed)
- Effect size: d = 0.5 (medium, based on XAI literature)
- α = 0.05, Power = 0.80
- **Required n:** 64 per group

**Actual sample size:** n = 200 per group

**Achieved power:** >0.94 (very high)

**Rationale for oversample:**
- Accounts for potential outliers
- Enables subgroup analyses (genuine vs impostor)
- Strengthens statistical conclusion validity

---

## 8. Validity Considerations

### Internal Validity (Can we claim causation?)
**Threats:**
1. **Selection bias:** Random assignment ensures equivalence
2. **History effects:** All data collected simultaneously (no temporal confound)
3. **Instrumentation:** Same model/hardware for all conditions ✅

**Addressed By:**
- Random assignment to conditions
- Standardized procedure (automated pipeline)
- Blinded evaluation (automated IoU calculation)

### External Validity (Can we generalize?)
**Considerations:**
1. **Population:** VGGFace2 test set (diverse, realistic)
2. **Setting:** Computational experiment (replicable)
3. **Measurement:** IoU is standard metric in XAI literature

**Limitations:**
- Single model (ArcFace-ResNet100)
- Single modality (face verification)
- Laboratory data (not real-world deployment)

**Addressed by:**
- Cross-dataset replication (LFW in separate experiment)
- Comparison to literature benchmarks

### Construct Validity (Are we measuring what we intend?)
**DV - Localization Accuracy:**
- ✅ IoU is established metric
- ✅ Ground-truth landmarks validated
- ✅ Aligned with definition of "localization"

**IV - XAI Method:**
- ✅ Both methods implemented correctly
- ✅ Same interface and post-processing
- ✅ Only difference is attribution algorithm

### Statistical Conclusion Validity
**Addressed By:**
- A priori power analysis (n exceeds requirement)
- Assumption checking before tests
- Effect size reporting (not just p-values)
- Multiple comparisons correction (if needed)

---

## 9. Data Collection Plan

### Timeline
- **Week 1:** Data preparation (sampling, preprocessing)
- **Week 2-3:** Attribution generation (200 pairs/day)
- **Week 4:** Quality checks, outlier analysis
- **Week 5:** Statistical analysis

### Data Recording
**Per verification pair:**
```json
{
  "pair_id": "VGG_000123",
  "img1_path": "/data/vggface2/n000123/0001.jpg",
  "img2_path": "/data/vggface2/n000123/0002.jpg",
  "genuine": true,
  "method": "BiometricGradCAM",
  "similarity": 0.72,
  "iou_img1": 0.85,
  "iou_img2": 0.83,
  "mean_iou": 0.84,
  "computation_time_ms": 42.3,
  "timestamp": "2024-10-18T14:32:01"
}
```

### Quality Control
1. **Visual inspection:** Review 10% of attributions (random sample)
2. **Range checks:** IoU ∈ [0,1], similarity ∈ [-1,1]
3. **Outlier detection:** IoU > 3 SD from mean (investigate)
4. **Replication:** Re-run 5% of pairs to verify consistency

---

## 10. Analysis Plan

### Primary Analysis
**Hypothesis 1:** BiometricGradCAM > GradCAM (localization accuracy)

**Test:** Independent samples t-test (one-tailed)
```r
t.test(
  iou ~ method,
  data = results,
  alternative = "greater",  # BiometricGradCAM > GradCAM
  var.equal = TRUE
)
```

**Report:**
- t-statistic, df, p-value
- Cohen's d with 95% CI
- Mean difference with 95% CI
- Interpretation (reject H₀ if p < 0.05)

### Secondary Analyses (Exploratory)
1. **Subgroup analysis:** Genuine vs impostor pairs
   - Test: 2 (method) × 2 (pair type) ANOVA

2. **Correlation:** IoU vs verification similarity
   - Test: Pearson correlation

3. **Robustness:** Exclude outliers and re-test
   - Sensitivity analysis

### Assumption Checks (Before Primary Analysis)
```r
# Normality (Shapiro-Wilk test)
shapiro.test(results$iou[results$method == "BiometricGradCAM"])
shapiro.test(results$iou[results$method == "GradCAM"])

# Homogeneity of variance (Levene's test)
car::leveneTest(iou ~ method, data = results)

# If violated: Use Welch's t-test or Mann-Whitney U
```

---

## 11. Preregistration Document

**Register BEFORE data collection:**

### Preregistration Components
1. **Research question** (exact wording)
2. **Hypotheses** (directional, pre-specified)
3. **Variables** (operationalizations)
4. **Sample size** (with justification)
5. **Sampling strategy** (stratification criteria)
6. **Procedure** (step-by-step)
7. **Analysis plan** (tests, α level, one-tailed vs two-tailed)
8. **Exclusion criteria** (what data to remove)

**Platform:** OSF (osf.io) or AsPredicted (aspredicted.org)

**Timestamp:** Must be before data collection begins

---

## 12. Ethical Considerations

### Data Ethics
- **Dataset:** VGGFace2 (public, consent obtained by dataset creators)
- **Privacy:** No collection of new face images
- **IRB:** Not required (secondary analysis of public data)

### Research Integrity
- **Preregistration:** Prevents p-hacking and HARKing
- **Reproducibility:** Code and data publicly available
- **Transparency:** Report all results (not just significant)

---

## 13. Limitations and Threats

### Known Limitations
1. **Single model:** Results may not generalize to other architectures
2. **Ground-truth assumption:** Facial landmarks may not reflect true decision factors
3. **Computational setting:** Not tested in real-world deployment

### Mitigation Strategies
1. **Cross-dataset replication:** Run same experiment on LFW
2. **Ablation studies:** Test with different layers, thresholds
3. **Comparison to literature:** Context within prior XAI research

---

## For Your Dissertation

### Chapter 4 (Methodology) - Section 4.1

```markdown
## 4.1 Experimental Design

### 4.1.1 Research Question
This experiment tested whether BiometricGradCAM achieves higher
localization accuracy than standard GradCAM when applied to face
verification systems.

### 4.1.2 Variables
The independent variable was XAI method (BiometricGradCAM vs GradCAM).
The dependent variable was localization accuracy, operationalized as
Intersection over Union (IoU) between generated attributions and
ground-truth facial landmark regions. Control variables included model
architecture (ArcFace-ResNet100), image resolution (112×112), and
preprocessing (MTCNN alignment).

### 4.1.3 Design
We employed a between-subjects design with two conditions
(n = 200 verification pairs per condition, N = 400 total).
Verification pairs were randomly assigned to conditions following
stratified sampling to ensure balanced representation of genuine/impostor
pairs and pose variations.

### 4.1.4 Sample Size Justification
A priori power analysis (α = .05, power = .80, d = 0.5) indicated
a minimum sample size of 64 per group. Our sample (n = 200)
substantially exceeded this requirement (power > .94), enabling
detection of medium-to-large effects with high confidence.

### 4.1.5 Procedure
[Detail from Section 6 above]

### 4.1.6 Validity
Internal validity was ensured through random assignment and
standardized procedures. External validity considerations included
use of realistic datasets (VGGFace2) and cross-dataset replication
(LFW). Construct validity was supported by established metrics (IoU)
and validated ground-truth annotations.
```

---

## Common Mistakes Fixed

### ❌ Mistake 1: Confusing IV and DV
"I'm measuring XAI method performance"
✅ IV = XAI method, DV = performance metric

### ❌ Mistake 2: No Power Analysis
Starting data collection without sample size justification
✅ Always conduct a priori power analysis

### ❌ Mistake 3: Ignoring Confounds
"Both methods tested, should be fair"
✅ Must control model, data, hardware, etc.

### ❌ Mistake 4: No Preregistration
Deciding analyses after seeing results (HARKing)
✅ Preregister hypotheses and analyses

### ❌ Mistake 5: Weak Operationalization
"Measure explanation quality"
✅ Specific: "IoU between attribution and landmark ROIs"

---

## Time Savings

**Manual experiment design:** 10-15 hours (literature review, planning, validation)
**Using @experiment-design:** 2-3 hours (review, customize, finalize)
**Saved:** ~10 hours 🎉

## Best Practices

### 1. Preregister Everything
Before collecting data, preregister RQ, hypotheses, analyses.

### 2. Power Your Study
Don't collect data without power analysis.

### 3. Control Confounds
Identify and address alternative explanations.

### 4. Use Established Metrics
Don't invent new metrics without validation.

### 5. Plan Analyses A Priori
Specify tests, α levels, one-tailed vs two-tailed BEFORE data collection.

## Related Skills

- `@power-analysis` - Determine required sample size
- `@hypothesis-test` - Design statistical tests
- `@research-questions` - Formulate testable questions
- `@methodology-writer` - Write methodology chapter

## Integration with Dissertation

### Chapter 4 (Methodology)
**Section 4.1:** Experimental Design (use this skill's output)
**Section 4.2:** Participants and Sampling (stratification details)
**Section 4.3:** Procedure (step-by-step protocol)

### Chapter 6 (Results)
Reference design when reporting results:
> "Consistent with our preregistered design (OSF: osf.io/abc123),
> we conducted an independent t-test..."

### Appendices
**Appendix B:** Full preregistration document
**Appendix C:** Detailed procedure with code snippets

---

**Status:** Documented
**Complexity:** High
**Time to use:** 2-3 hours
**Time saved:** ~10 hours
**Reusability:** Very High (every empirical study)
**Critical for:** Methodology chapter, research rigor, reproducibility
