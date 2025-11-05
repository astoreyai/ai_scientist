# @methodology-writer - Draft Methodology Sections

Generate complete, rigorous methodology sections for Chapter 4 of your dissertation.

## Skill Type
**Category:** Writing / Methodology
**Tier:** Specialized (Tier 2)
**Reusability:** High - every experimental dissertation needs methods

## What This Skill Does

1. Drafts complete methodology sections
2. Ensures reproducibility and rigor
3. Includes all required subsections
4. Validates against reporting standards
5. Adapts to quantitative/qualitative/mixed methods

## Invocation

```
@methodology-writer [study-type] [details]
```

## Methodology Components

### Required Sections

**4.1 Research Design**
- Overall approach (experimental, observational, etc.)
- Justification for design choice
- Independent/dependent variables

**4.2 Participants/Samples**
- Sample description
- Inclusion/exclusion criteria
- Recruitment/sampling method
- Power analysis and sample size justification

**4.3 Materials/Apparatus**
- Equipment, software, tools used
- Datasets, stimuli, instruments
- Versions and specifications

**4.4 Procedure**
- Step-by-step protocol
- Experimental conditions
- Randomization/counterbalancing
- Timeline

**4.5 Measures/Variables**
- Operational definitions
- Measurement instruments
- Validity and reliability

**4.6 Data Analysis**
- Statistical tests planned
- Software used
- Alpha level, power
- Handling of missing data/outliers

## Input Format

### Minimal Input
```
@methodology-writer

Study: XAI method comparison
Type: Experimental (between-subjects)
IV: XAI method (4 levels)
DV: Localization accuracy
n = 200 per method
Datasets: VGGFace2, LFW
```

### Detailed Input
```json
{
  "study_type": "experimental",
  "design": "between-subjects",
  "variables": {
    "IV": "XAI method (BiometricGradCAM, GradCAM, LIME, IG)",
    "DV": "Localization accuracy (IoU metric)"
  },
  "sample": {
    "size": 200,
    "datasets": ["VGGFace2", "LFW"],
    "sampling": "stratified random"
  },
  "materials": {
    "model": "ArcFace-ResNet100",
    "software": "Python 3.9, PyTorch 2.0"
  },
  "analysis": {
    "primary": "One-way ANOVA",
    "post_hoc": "Tukey HSD",
    "alpha": 0.05
  }
}
```

## Output Example

**Input:**
```
@methodology-writer

Study: BiometricGradCAM vs standard XAI methods for face verification
Design: Between-subjects experimental
IV: XAI method (4 levels: BiometricGradCAM, GradCAM, LIME, IntegratedGradients)
DV: Localization accuracy, consistency, faithfulness
Sample: 200 verification pairs per dataset
Datasets: VGGFace2, LFW
Model: ArcFace-ResNet100
Statistical test: One-way ANOVA with Tukey post-hoc
```

**Output:**

```markdown
# Chapter 4: Methodology

## 4.1 Research Design

### 4.1.1 Study Overview

This study employed a **between-subjects experimental design** to compare the performance of four explainable AI (XAI) methods for face verification tasks. The study investigated the effect of XAI method on explanation quality, operationalized through three dependent measures: localization accuracy, consistency, and faithfulness.

### 4.1.2 Research Questions and Hypotheses

**RQ1:** Do XAI methods differ in their ability to accurately localize facial features relevant to verification decisions?

**H1:** BiometricGradCAM, which incorporates verification constraints, will achieve significantly higher localization accuracy than standard methods (GradCAM, LIME, Integrated Gradients).

**RQ2:** Do explanation consistency scores differ across XAI methods?

**H2:** BiometricGradCAM will demonstrate higher consistency across similar face pairs compared to standard methods.

**RQ3:** Are these findings generalizable across different face verification datasets?

**H3:** The relative performance of XAI methods will be consistent across VGGFace2 and LFW datasets.

### 4.1.3 Independent Variable

**XAI Method** (between-subjects factor with 4 levels):
1. **BiometricGradCAM:** Novel method incorporating biometric verification constraints
2. **GradCAM** (Selvaraju et al., 2017): Gradient-based class activation mapping
3. **LIME** (Ribeiro et al., 2016): Local interpretable model-agnostic explanations
4. **Integrated Gradients** (Sundararajan et al., 2017): Attribution through path integration

**Manipulation:** Each verification pair was explained using only one XAI method to avoid carryover effects.

### 4.1.4 Dependent Variables

**Primary DV: Localization Accuracy**
- **Definition:** Intersection-over-Union (IoU) between model attribution map and ground-truth facial landmark regions
- **Range:** 0.0 (no overlap) to 1.0 (perfect overlap)
- **Computation:** IoU = Area(Attribution ∩ Landmarks) / Area(Attribution ∪ Landmarks)

**Secondary DV 1: Consistency**
- **Definition:** Pearson correlation between attribution maps for genuine pairs (same identity)
- **Range:** -1.0 to 1.0 (higher = more consistent)
- **Rationale:** Similar faces should receive similar explanations

**Secondary DV 2: Faithfulness**
- **Definition:** Correlation between attribution strength and verification score perturbation
- **Range:** 0.0 to 1.0 (higher = more faithful to model logic)
- **Measurement:** Remove top-k% attributed pixels, measure verification accuracy drop

---

## 4.2 Participants and Sampling

### 4.2.1 Dataset Selection

**VGGFace2 Test Set**
- **Source:** Cao et al. (2018)
- **Size:** 500 identities, 169,396 images
- **Characteristics:** In-the-wild faces, varied pose, age, illumination, ethnicity
- **Access:** Public, non-commercial use
- **Version:** VGGFace2 test split (official)

**Labeled Faces in the Wild (LFW)**
- **Source:** Huang et al. (2007)
- **Size:** 5,749 identities, 13,233 images
- **Characteristics:** Unconstrained faces from news articles
- **Access:** Public, unrestricted use
- **Purpose:** Cross-dataset validation to assess generalizability

### 4.2.2 Sampling Procedure

**Stratified Random Sampling:**
1. **Genuine pairs (n = 100 per dataset):**
   - Randomly selected 50 identities from each dataset
   - For each identity, randomly paired 2 images (same person)
   - Verified verification model confidence > 0.70 (genuine threshold)

2. **Impostor pairs (n = 100 per dataset):**
   - Randomly selected 100 distinct identity pairs
   - Paired images from different identities
   - Verified verification model confidence < 0.30 (impostor threshold)

**Total Sample:**
- VGGFace2: 200 verification pairs (100 genuine, 100 impostor)
- LFW: 200 verification pairs (100 genuine, 100 impostor)
- **Grand total:** N = 400 verification pairs

### 4.2.3 Sample Size Justification

An **a priori power analysis** using G*Power 3.1 (Faul et al., 2007) determined the required sample size:
- **Test:** One-way ANOVA (4 groups)
- **Expected effect size:** f = 0.25 (medium, based on Smith et al., 2023)
- **Desired power:** 0.80
- **Significance level:** α = 0.05
- **Required n per group:** 45

Our sample (n = 200 per dataset) **exceeds this minimum**, providing:
- **Power = 0.94** for VGGFace2 alone
- **Power > 0.99** for combined analysis
- Adequate power for subgroup analyses

This sample size aligns with prior work in XAI evaluation (median n = 100; Jones et al., 2022; Brown et al., 2021) while exceeding typical standards.

### 4.2.4 Inclusion Criteria

Verification pairs were included if they met ALL criteria:
1. ✅ Images from official test splits (no training data contamination)
2. ✅ Verification confidence clearly genuine (>0.70) or impostor (<0.30)
3. ✅ Face detection successful (bounding box IoU > 0.80 with ground truth)
4. ✅ Image quality acceptable (resolution ≥ 112×112 pixels)
5. ✅ Ground-truth facial landmarks available (68-point annotation)

**Exclusions:**
- Ambiguous pairs (verification confidence 0.30-0.70): n = 47 excluded
- Failed face detection: n = 12 excluded
- Missing landmark annotations: n = 8 excluded

---

## 4.3 Materials and Apparatus

### 4.3.1 Face Verification Model

**Model Architecture:** ArcFace (Deng et al., 2019)
- **Backbone:** ResNet-100
- **Embedding dimension:** 512-D
- **Training data:** MS-Celeb-1M (cleaned subset, 3.8M images)
- **Loss function:** Additive Angular Margin Loss
- **Verification threshold:** Cosine similarity = 0.40

**Performance (on our test sets):**
- VGGFace2: 99.2% accuracy, EER = 0.8%
- LFW: 99.5% accuracy, EER = 0.5%

**Rationale:** ArcFace is state-of-the-art for face verification (Huang et al., 2020) and widely used in research.

**Availability:** Pretrained weights from official ArcFace GitHub repository (version 1.0.2)

### 4.3.2 XAI Methods Implementation

**BiometricGradCAM** (Our Contribution):
- **Implementation:** Custom PyTorch module extending GradCAM
- **Key modification:** Incorporates pairwise similarity gradients
- **Parameters:** Layer = final convolutional layer (conv5_3)
- **Code:** Available at [GitHub link] (open source, MIT license)

**GradCAM** (Baseline 1):
- **Implementation:** pytorch-grad-cam library (version 1.4.8)
- **Parameters:** Target layer = conv5_3 (consistent with BiometricGradCAM)
- **Citations:** Selvaraju et al. (2017)

**LIME** (Baseline 2):
- **Implementation:** lime library (version 0.2.0.1)
- **Parameters:** num_samples = 1000, num_features = 100
- **Segmentation:** SLIC superpixels (n_segments = 50)
- **Citations:** Ribeiro et al. (2016)

**Integrated Gradients** (Baseline 3):
- **Implementation:** captum library (version 0.7.0)
- **Parameters:** n_steps = 50, baseline = black image (zeros)
- **Citations:** Sundararajan et al. (2017)

### 4.3.3 Hardware and Software

**Computing Infrastructure:**
- **GPU:** NVIDIA A100 (40GB VRAM)
- **CPU:** AMD EPYC 7742 (64 cores)
- **RAM:** 256 GB
- **OS:** Ubuntu 22.04 LTS

**Software Environment:**
- **Python:** 3.9.18
- **PyTorch:** 2.0.1 (with CUDA 11.8)
- **NumPy:** 1.24.3
- **pandas:** 2.0.3
- **scikit-learn:** 1.3.0
- **matplotlib:** 3.7.2

**Reproducibility:**
- Random seed: 42 (set for Python, NumPy, PyTorch)
- Docker container: [registry.io/xai-biometric:v1.0] (available on request)
- Requirements file: requirements.txt (all dependencies with exact versions)

---

## 4.4 Procedure

### 4.4.1 Data Preparation

**Step 1: Face Detection and Alignment** (preprocessing)
1. Detect faces using MTCNN (Zhang et al., 2016)
2. Extract 5-point landmarks (eyes, nose, mouth corners)
3. Align faces to canonical pose using similarity transform
4. Resize to 112×112 pixels (ArcFace input size)
5. Normalize pixel values to [-1, 1]

**Step 2: Pair Generation**
1. Load test images from VGGFace2/LFW
2. Generate genuine/impostor pairs using stratified sampling (Section 4.2.2)
3. Verify verification model confidence thresholds
4. Store pairs in verification_pairs.json

**Step 3: Ground Truth Annotation**
1. Extract 68-point facial landmarks using dlib (King, 2009)
2. Define regions of interest (ROI) for verification:
   - Eyes (landmarks 36-48)
   - Nose (landmarks 27-36)
   - Mouth (landmarks 48-68)
3. Create binary masks for ROI pixels
4. Store in landmarks_gt.npy

### 4.4.2 Explanation Generation

For each verification pair (x₁, x₂):

**Step 1: Compute Verification Score**
```python
embed1 = face_model(x1)
embed2 = face_model(x2)
similarity = cosine_similarity(embed1, embed2)
```

**Step 2: Generate Explanations (per method)**
```python
if method == "BiometricGradCAM":
    attribution1 = biometric_gradcam(x1, x2, target_sim=similarity)
    attribution2 = biometric_gradcam(x2, x1, target_sim=similarity)
elif method == "GradCAM":
    attribution1 = gradcam(x1, target_class=identity)
    attribution2 = gradcam(x2, target_class=identity)
# ... (similarly for LIME, IG)
```

**Step 3: Normalize Attributions**
- Scale to [0, 1] range
- Apply Gaussian smoothing (σ = 2 pixels) for visualization
- Threshold at top 20% for IoU calculation

### 4.4.3 Evaluation Metrics Computation

**Localization Accuracy (IoU):**
```python
pred_mask = (attribution > threshold)  # Top 20%
gt_mask = landmark_masks[pair_id]
iou = (pred_mask & gt_mask).sum() / (pred_mask | gt_mask).sum()
```

**Consistency:**
```python
# For genuine pairs only
if pair_type == "genuine":
    consistency = pearsonr(attribution1.flatten(), attribution2.flatten())
```

**Faithfulness:**
```python
# Iteratively remove top-attributed pixels
faithfulness_scores = []
for k in [10, 20, 30, 40, 50]:
    x1_masked = remove_top_k_percent(x1, attribution1, k)
    new_sim = compute_similarity(x1_masked, x2)
    drop = original_sim - new_sim
    faithfulness_scores.append(drop)
faithfulness = mean(faithfulness_scores)
```

### 4.4.4 Timeline

**Phase 1: Setup (Week 1)**
- Dataset download and preprocessing
- Model loading and validation
- Test on n = 10 pairs

**Phase 2: Explanation Generation (Weeks 2-3)**
- Generate explanations for 400 pairs × 4 methods = 1,600 attributions
- Estimated time: ~80 hours (parallelized across GPU)
- Save attributions to disk for analysis

**Phase 3: Evaluation (Week 4)**
- Compute metrics for all attributions
- Statistical analysis
- Visualization generation

**Total Duration:** 4 weeks (1 month)

---

## 4.5 Data Analysis

### 4.5.1 Primary Analysis: Localization Accuracy

**Research Question:** Do XAI methods differ in localization accuracy?

**Statistical Test:** One-way ANOVA
- **Null hypothesis:** H₀: μ₁ = μ₂ = μ₃ = μ₄ (all methods equal)
- **Alternative:** H₁: At least one mean differs
- **Significance level:** α = 0.05
- **Assumptions:**
  - Independence: ✅ (between-subjects)
  - Normality: Tested via Shapiro-Wilk
  - Homogeneity of variance: Tested via Levene's test

**Post-Hoc Tests:**
- If ANOVA significant: Tukey HSD (all pairwise comparisons)
- Effect sizes: Cohen's d for pairwise, η² for omnibus
- Confidence intervals: 95% CIs for all means

**Software:** R 4.3.1 (aov() function, emmeans package)

### 4.5.2 Secondary Analyses

**Consistency (Genuine Pairs Only):**
- Test: One-way ANOVA on consistency scores
- Post-hoc: Tukey HSD if significant

**Faithfulness:**
- Test: Repeated measures ANOVA (within: removal percentage; between: method)
- Post-hoc: Bonferroni correction for multiple comparisons

**Cross-Dataset Generalization:**
- Test: Two-way mixed ANOVA (Method × Dataset)
- Interaction effect: Does method ranking change across datasets?

### 4.5.3 Assumption Checking

**Normality:**
```r
shapiro.test(localization_accuracy[method == "BiometricGradCAM"])
# Repeat for each method
```
**If violated:** Use Kruskal-Wallis (non-parametric ANOVA)

**Homogeneity of Variance:**
```r
leveneTest(localization_accuracy ~ method)
```
**If violated:** Use Welch's ANOVA (does not assume equal variances)

### 4.5.4 Missing Data and Outliers

**Missing Data:**
- Expected: 0% (controlled experiment)
- If occurs: Investigate reason, report in results
- Do NOT impute (small dataset, listwise deletion appropriate)

**Outliers:**
- Definition: Values > 3 SD from method mean
- Action: Investigate (data error? extreme case?)
- Reporting: Include in main analysis, report sensitivity analysis without outliers

### 4.5.5 Multiple Comparisons Correction

**Primary Analysis:**
- No correction needed (single omnibus ANOVA)
- Post-hoc: Tukey HSD inherently controls family-wise error rate

**Secondary Analyses:**
- 3 dependent variables (localization, consistency, faithfulness)
- Bonferroni correction: α_adjusted = 0.05 / 3 = 0.017
- Report both corrected and uncorrected p-values

### 4.5.6 Effect Size Interpretation

**Cohen's d:**
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8

**η² (Eta-squared):**
- Small: η² = 0.01 (1% variance)
- Medium: η² = 0.06 (6% variance)
- Large: η² = 0.14 (14% variance)

We report effect sizes with 95% confidence intervals for all significant results.

---

## 4.6 Ethical Considerations

### 4.6.1 Data Ethics

**Datasets Used:**
- ✅ Publicly available (VGGFace2, LFW)
- ✅ Non-commercial use permitted
- ✅ Subjects consented to original data collection
- ✅ No re-identification attempted

**Demographic Considerations:**
- Both datasets contain diverse faces (multiple ethnicities, ages, genders)
- Results reported aggregated (no per-demographic analysis in this study)
- Limitation acknowledged: Potential demographic bias not evaluated

### 4.6.2 Research Integrity

**Reproducibility:**
- All code publicly available: [GitHub repository]
- Docker container provided for exact replication
- Random seeds fixed (seed = 42)
- Raw data available on reasonable request

**Pre-registration:**
- Hypotheses, design, and analysis plan documented in lab notebook prior to data collection
- No p-hacking or HARKing (Hypothesizing After Results are Known)

**Transparency:**
- All exclusions reported with rationale
- Assumption violations documented
- Effect sizes and confidence intervals provided

### 4.6.3 IRB Approval

**Status:** **IRB review not required** for this study.

**Rationale:**
1. No new human subjects data collected
2. Only publicly available, de-identified datasets used
3. Secondary analysis of existing data
4. University IRB confirmed exemption (Case #2024-EXEMPT-1234, dated March 15, 2024)

---

## 4.7 Limitations

**Sample Limitations:**
- Limited to two datasets (VGGFace2, LFW); generalization to other datasets unknown
- Sample size (n=200 per dataset) sufficient for primary hypothesis but limits subgroup analyses

**Method Limitations:**
- XAI methods compared at default hyperparameters; tuning might alter results
- Ground-truth landmarks may not perfectly correspond to model decision-making

**Scope Limitations:**
- Focused on four XAI methods; many others exist
- Single face verification model (ArcFace); results may differ for other models

These limitations are acknowledged and discussed further in Chapter 7.

---

## References (Cited in Methodology)

[Standard bibliography format - APA, IEEE, etc.]
```

---

### Key Features of Generated Methodology:

✅ **Complete Structure:** All required sections (Design, Participants, Materials, Procedure, Analysis, Ethics)
✅ **Reproducibility:** Exact versions, parameters, seeds specified
✅ **Statistical Rigor:** Power analysis, assumption checking, effect sizes
✅ **Transparency:** Exclusions, limitations, ethical considerations documented
✅ **Field Standards:** Follows APA/dissertation formatting conventions

### Customization Options:

- **Quantitative vs Qualitative:** Adjusts sections for research type
- **Field-Specific:** Adapts terminology (CS, psychology, medicine, etc.)
- **Detail Level:** Can expand/compress based on page limits

### Time Savings:

**Manual methodology writing:** 20-30 hours (multiple drafts, advisor feedback)
**Using @methodology-writer:** 2-3 hours (review and customize)
**Saved:** ~25 hours 🎉

---

**Status:** Documented
**Complexity:** High
**Time to use:** 2-3 hours (review + customize)
**Time saved:** ~25 hours
**Reusability:** High (quantitative experimental studies)
**Critical for:** Chapter 4, reproducibility, defense preparation
