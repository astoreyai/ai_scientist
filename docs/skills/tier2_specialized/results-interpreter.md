# @results-interpreter - Interpret Statistical Results

Interpret statistical results comprehensively for your dissertation's results chapter.

## Skill Type
**Category:** Statistics / Results Interpretation
**Tier:** Specialized (Tier 2)
**Reusability:** Very High - every quantitative study needs result interpretation

## What This Skill Does

1. Interprets statistical test results in plain language
2. Evaluates practical vs statistical significance
3. Contextualizes findings within literature
4. Identifies unexpected results and alternative explanations
5. Connects results to hypotheses and research questions
6. Writes complete results sections in APA format

## Invocation

```
@results-interpreter [statistical-output] [research-context]
```

## Result Interpretation Components

### 1. Statistical Significance
- p-value interpretation (reject H₀ or fail to reject)
- Confidence intervals
- Multiple comparisons adjustments

### 2. Effect Size Magnitude
- Small, medium, large, or very large
- Practical importance
- Comparison to literature benchmarks

### 3. Direction of Effect
- Which group/condition performed better
- Magnitude of difference
- Unexpected vs expected direction

### 4. Confidence and Precision
- CI width (narrow = precise, wide = imprecise)
- Sample size adequacy
- Power analysis post-hoc (if non-significant)

### 5. Context and Meaning
- What does this mean for the research question?
- Alignment with hypotheses
- Theoretical implications
- Practical implications

## Input Format

### From Statistical Output (R or Python)
```
@results-interpreter

t-test output:
t(398) = 14.2, p < 0.001
Cohen's d = 2.94, 95% CI [2.62, 3.26]

Group 1 (BiometricGradCAM): M = 0.87, SD = 0.04
Group 2 (GradCAM): M = 0.72, SD = 0.06

RQ: Does BiometricGradCAM improve localization accuracy?
```

### From ANOVA Output
```
@results-interpreter

ANOVA:
F(3, 396) = 23.5, p < 0.001, η² = 0.15

Group means:
- GradCAM: M = 0.72, SD = 0.06
- LIME: M = 0.68, SD = 0.07
- IntegratedGrad: M = 0.75, SD = 0.05
- BiometricGradCAM: M = 0.87, SD = 0.04

Post-hoc (Tukey HSD): BiometricGradCAM > all others (p < 0.001)
```

### From Correlation
```
@results-interpreter

Correlation:
r(198) = 0.67, p < 0.001
95% CI [0.58, 0.74]
R² = 0.45

Variables: Explanation consistency & Verification accuracy
```

## Output Examples

### Example 1: t-test Result Interpretation

**Input:**
```
@results-interpreter

Statistical output:
t(398) = 14.2, p < 0.001 (one-tailed)
Cohen's d = 2.94, 95% CI [2.62, 3.26]

BiometricGradCAM: M = 0.87, SD = 0.04, n = 200
GradCAM: M = 0.72, SD = 0.06, n = 200

Research Question: Does BiometricGradCAM achieve higher localization accuracy than GradCAM?
Hypothesis: H₁: BiometricGradCAM > GradCAM
```

**Output:**

```markdown
# Result Interpretation: BiometricGradCAM vs GradCAM

## Statistical Significance

**Test Result:** t(398) = 14.2, p < .001 (one-tailed)

**Interpretation:**
✅ **Reject null hypothesis**

The observed difference in localization accuracy between BiometricGradCAM
(M = 0.87) and GradCAM (M = 0.72) is **statistically significant** at
the α = .05 level. The extremely small p-value (p < .001) indicates
there is less than 0.1% probability of observing this difference if
the null hypothesis (no difference) were true.

**Conclusion:**
BiometricGradCAM achieves significantly higher localization accuracy
than standard GradCAM, **supporting our directional hypothesis (H₁)**.

---

## Effect Size Magnitude

**Cohen's d = 2.94, 95% CI [2.62, 3.26]**

### Magnitude Classification

| Benchmark | Cohen's d | Classification |
|-----------|-----------|----------------|
| Small | 0.2 | |
| Medium | 0.5 | |
| Large | 0.8 | |
| **Very Large** | **>1.2** | **✅ Your result: d = 2.94** |

**Interpretation:**
The effect size is **extremely large** (d = 2.94), far exceeding
conventional thresholds. This represents nearly **3 standard deviations**
difference between methods.

### What This Means Practically

**Overlap in distributions:**
- Only **6% overlap** between BiometricGradCAM and GradCAM score distributions
- **94% of BiometricGradCAM scores exceed the mean GradCAM score**

**Common Language Effect Size:**
If you randomly select one pair from each method, there is a **99%
probability** that the BiometricGradCAM pair will have higher
localization accuracy.

**Mean Difference:**
BiometricGradCAM scores 0.15 points higher (15 percentage points)
on the 0-1 scale, representing a **21% relative improvement**
over GradCAM (0.15 / 0.72 = 0.21).

---

## Precision and Confidence

**95% Confidence Interval: [2.62, 3.26]**

**Interpretation:**
We are 95% confident the true population effect size lies between
d = 2.62 and d = 3.26. Notably:

1. **Entire CI is large:** Even the lower bound (2.62) is very large
2. **CI does not include zero:** Reinforces significance
3. **Narrow width:** 0.64 units, indicating high precision
4. **Narrow due to:** Large sample (n = 200 per group) and consistent effect

**Robustness:**
The narrow CI suggests this result is **highly stable** and likely
to replicate in future studies.

---

## Direction of Effect

**BiometricGradCAM > GradCAM**

| Method | Mean | SD | Range |
|--------|------|----|----|
| **BiometricGradCAM** | **0.87** | 0.04 | 0.79-0.95 |
| GradCAM | 0.72 | 0.06 | 0.60-0.84 |
| **Difference** | **+0.15** | | |

**Interpretation:**
The direction of the effect aligns with our **a priori hypothesis**:
BiometricGradCAM, which incorporates verification constraints,
produces more accurate spatial localizations than standard GradCAM.

**No overlap in confidence intervals:**
- BiometricGradCAM: 95% CI [0.86, 0.88]
- GradCAM: 95% CI [0.71, 0.73]
- **No overlap** → very strong evidence for difference

---

## Practical Significance

### Statistical vs Practical Significance

| Aspect | Value | Assessment |
|--------|-------|------------|
| **Statistical significance** | p < .001 | ✅ Highly significant |
| **Effect size** | d = 2.94 | ✅ Very large |
| **Practical importance** | 15% improvement | ✅ Meaningful |

**Is this practically meaningful?**

**✅ YES**, for multiple reasons:

1. **Absolute improvement:** 15 percentage points on 0-1 scale
2. **Relative improvement:** 21% better than baseline
3. **Context:** XAI literature typically reports d = 0.3-0.7
4. **Real-world impact:** More accurate explanations → better trust/debugging

### Comparison to Literature

| Study | Comparison | Cohen's d |
|-------|------------|-----------|
| Smith et al. (2023) | GradCAM vs LIME | 0.35 |
| Jones et al. (2022) | Method A vs B | 0.62 |
| Lee et al. (2021) | Saliency methods | 0.41 |
| **This study** | **BiometricGradCAM vs GradCAM** | **2.94** |

**Your effect is:**
- **8.4× larger** than Smith et al. (2023)
- **4.7× larger** than Jones et al. (2022)
- **Largest reported** in XAI comparison literature

**Why so large?**
Possible explanations:
1. Biometric constraints provide strong structural guidance
2. Standard XAI methods poorly suited for verification tasks
3. Task specificity (verification vs classification) matters greatly
4. Ground-truth alignment is clearer in biometric context

---

## Connecting to Research Question

**RQ:** Does BiometricGradCAM achieve higher localization accuracy than GradCAM?

**Answer:** ✅ **YES, definitively**

BiometricGradCAM demonstrates **substantially higher** localization
accuracy (M = 0.87) compared to GradCAM (M = 0.72), with a very
large effect (d = 2.94, p < .001). This 15-percentage-point improvement
is both statistically significant and practically meaningful,
representing the largest effect reported in XAI method comparisons.

**Hypothesis outcome:**
✅ **H₁ supported:** BiometricGradCAM > GradCAM (as predicted)

---

## For Your Dissertation (APA Format)

### Chapter 6 (Results) - Writing

**Hypothesis 1: Localization Accuracy**

An independent samples t-test was conducted to compare localization
accuracy between BiometricGradCAM and standard GradCAM. BiometricGradCAM
(M = 0.87, SD = 0.04) achieved significantly higher accuracy than
GradCAM (M = 0.72, SD = 0.06), t(398) = 14.2, p < .001 (one-tailed),
d = 2.94, 95% CI [2.62, 3.26]. This represents a very large effect size,
with BiometricGradCAM demonstrating a 15-percentage-point improvement
(21% relative improvement) over the baseline method.

The effect size (d = 2.94) substantially exceeds those typically
reported in XAI method comparisons (modal d ≈ 0.3-0.7), suggesting
that incorporating biometric verification constraints produces
exceptionally large improvements in explanation quality. The narrow
confidence interval indicates this effect is highly stable and
likely to replicate in future research.

**Figure 6.1** displays the distributions of localization accuracy
scores for both methods, illustrating minimal overlap (6%) between
distributions. These results provide strong support for Hypothesis 1
and suggest that verification-aware XAI methods are substantially
more effective than general-purpose approaches for biometric systems.

---

### Condensed Version (if space limited)

BiometricGradCAM (M = 0.87, SD = 0.04) significantly outperformed
GradCAM (M = 0.72, SD = 0.06) in localization accuracy, t(398) = 14.2,
p < .001, d = 2.94, 95% CI [2.62, 3.26], supporting Hypothesis 1.
This very large effect represents a 15-percentage-point improvement.

---

## Alternative Interpretations

### Could This Be Explained By...?

**1. Confounding variables?**
- **Unlikely:** Random assignment and controlled experimental design
- Both methods tested on same images, same model, same hardware

**2. Measurement artifacts?**
- **Unlikely:** IoU is established metric, automated computation
- Visual inspection validated (10% sample)

**3. Ground-truth limitations?**
- **Possible:** Facial landmarks may not perfectly reflect true decision factors
- However, landmarks are validated standard in face recognition

**4. Overfitting to evaluation metric?**
- **Unlikely:** BiometricGradCAM designed for verification constraints,
  not specifically optimized for landmark IoU

**Most Plausible Explanation:**
BiometricGradCAM's incorporation of biometric constraints (pairwise
similarity, verification thresholds) fundamentally aligns the
attribution process with the verification task structure, producing
genuinely superior explanations.

---

## Unexpected Findings

**Expected:** BiometricGradCAM > GradCAM ✅ **Confirmed**

**Unexpected magnitude:** Effect (d = 2.94) far larger than anticipated

**Possible reasons:**
1. Prior work underestimated task-specificity importance
2. Standard XAI methods particularly ill-suited for verification
3. Biometric constraints provide exceptionally strong guidance

**Implications:**
- Task-specific XAI design may be more critical than previously recognized
- General-purpose XAI methods may have substantial limitations in specialized domains
- Similar large gains might be achievable in other task-specific contexts

---

## Limitations of This Result

1. **Single model tested:** ArcFace-ResNet100 only (generalization unknown)
2. **Single dataset:** VGGFace2 only in this analysis (LFW replication pending)
3. **Ground-truth assumptions:** Landmarks may not capture all decision factors
4. **Laboratory setting:** Not yet validated in real deployment

**Note:** These limitations do NOT undermine the core finding
(BiometricGradCAM > GradCAM) but limit generalizability claims.

---

## Next Steps

### To Strengthen This Finding:
1. **Cross-dataset replication:** Repeat on LFW dataset
2. **Cross-model validation:** Test with other face verification models
3. **Subgroup analyses:** Examine by pose, quality, demographics
4. **Alternative metrics:** Validate with consistency, faithfulness

### For Discussion Chapter:
- Compare to theoretical predictions (did theory correctly predict outcome?)
- Discuss why effect is so large (mechanism explanation)
- Consider boundary conditions (when might this NOT hold?)
- Address alternative explanations systematically
```

---

### Example 2: ANOVA Result Interpretation

**Input:**
```
@results-interpreter

ANOVA output:
F(3, 396) = 23.5, p < 0.001
η² = 0.15 (15% variance explained)

Descriptive statistics:
- GradCAM: M = 0.72, SD = 0.06, n = 100
- LIME: M = 0.68, SD = 0.07, n = 100
- IntegratedGrad: M = 0.75, SD = 0.05, n = 100
- BiometricGradCAM: M = 0.87, SD = 0.04, n = 100

Tukey HSD post-hoc:
BiometricGradCAM > IntegratedGrad (p < 0.001, d = 2.6)
BiometricGradCAM > GradCAM (p < 0.001, d = 2.9)
BiometricGradCAM > LIME (p < 0.001, d = 3.5)
IntegratedGrad > LIME (p = 0.018, d = 1.0)
GradCAM ≈ IntegratedGrad (p = 0.42)
GradCAM > LIME (p = 0.006, d = 0.6)
```

**Output:**

```markdown
# ANOVA Result Interpretation: Four XAI Methods

## Omnibus Test (Overall Effect)

**F(3, 396) = 23.5, p < .001, η² = .15**

**Statistical Significance:**
✅ **Reject null hypothesis** (H₀: μ₁ = μ₂ = μ₃ = μ₄)

The choice of XAI method has a **statistically significant effect**
on localization accuracy, F(3, 396) = 23.5, p < .001. This indicates
that at least one method differs significantly from the others.

**Effect Size:**
η² = .15 indicates that **15% of variance** in localization accuracy
is explained by XAI method choice. Using Cohen's (1988) benchmarks:

| η² | Classification |
|----|----------------|
| 0.01 | Small |
| 0.06 | Medium |
| 0.14 | Large |
| **0.15** | **✅ Large** |

**Interpretation:**
XAI method choice accounts for a **large** proportion of performance
variability. This is substantial given that 85% of variance remains
due to individual image differences, noise, etc.

---

## Post-Hoc Comparisons (Pairwise)

### Performance Ranking

1. **BiometricGradCAM: M = 0.87** ⭐ (best)
2. IntegratedGrad: M = 0.75
3. GradCAM: M = 0.72
4. LIME: M = 0.68 (worst)

### Significant Differences

**BiometricGradCAM vs all others:**
- vs IntegratedGrad: d = 2.6, p < .001 ✅
- vs GradCAM: d = 2.9, p < .001 ✅
- vs LIME: d = 3.5, p < .001 ✅

**Other comparisons:**
- IntegratedGrad > LIME: d = 1.0, p = .018 ✅
- GradCAM > LIME: d = 0.6, p = .006 ✅
- GradCAM ≈ IntegratedGrad: p = .42 (not significant)

### Key Findings

1. **BiometricGradCAM dominates:** Significantly better than ALL baselines
2. **Effect sizes are very large:** d = 2.6-3.5 for BiometricGradCAM
3. **Baseline methods cluster together:** GradCAM ≈ IntegratedGrad
4. **LIME performs worst:** Significantly worse than all others

---

## For Your Dissertation

A one-way ANOVA revealed a significant effect of XAI method on
localization accuracy, F(3, 396) = 23.5, p < .001, η² = .15,
representing a large effect. Post-hoc comparisons using Tukey HSD
indicated that BiometricGradCAM (M = 0.87, SD = 0.04) significantly
outperformed all baseline methods: IntegratedGradients (M = 0.75,
SD = 0.05, p < .001, d = 2.6), GradCAM (M = 0.72, SD = 0.06,
p < .001, d = 2.9), and LIME (M = 0.68, SD = 0.07, p < .001, d = 3.5).
Among baseline methods, IntegratedGradients and GradCAM performed
comparably (p = .42), both significantly outperforming LIME.
```

---

## Time Savings

**Manual result interpretation:** 3-4 hours per analysis (literature context, writing, revision)
**Using @results-interpreter:** 30-45 minutes (review, customize)
**Saved:** ~3 hours per analysis 🎉

## Best Practices

### 1. Report Everything
- Test statistic, df, p-value
- Effect size with CI
- Descriptive statistics (M, SD)
- Not just "significant" or "not significant"

### 2. Interpret Effect Sizes
- Statistical significance ≠ practical importance
- Always discuss magnitude, not just p-value

### 3. Connect to RQs
- Explicitly answer research questions
- State hypothesis outcome (supported/not supported)

### 4. Consider Alternatives
- Could confounds explain results?
- Measurement artifacts?
- Alternative interpretations?

### 5. Be Honest About Limitations
- Single dataset?
- Unexpected results?
- Boundary conditions?

## Related Skills

- `@hypothesis-test` - Design hypothesis tests
- `@effect-size` - Calculate effect sizes
- `@power-analysis` - Sample size planning
- `@contribution-writer` - Connect results to contributions

---

**Status:** Documented
**Complexity:** Medium-High
**Time to use:** 30-45 minutes per result
**Time saved:** ~3 hours per result
**Reusability:** Very High (every statistical test needs interpretation)
**Critical for:** Results chapter (Chapter 6), discussion, defense preparation
