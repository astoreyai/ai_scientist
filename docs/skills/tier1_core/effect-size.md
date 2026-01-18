# @effect-size - Calculate Effect Sizes

Calculate and interpret effect sizes for statistical results in your dissertation.

## Skill Type
**Category:** Statistics / Analysis
**Tier:** Core (Tier 1)
**Reusability:** Very High - every quantitative study needs effect sizes

## What This Skill Does

1. Calculates effect sizes from statistical results
2. Interprets magnitude (small, medium, large)
3. Provides confidence intervals
4. Compares effect sizes across studies
5. Reports in APA format

## Invocation

```
@effect-size [data] [test-type]
```

## Common Effect Sizes

### 1. Cohen's d (Two Groups)
**Use:** t-tests, comparing two means

**Formula:** d = (M₁ - M₂) / SD_pooled

**Interpretation:**
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8

---

### 2. Cohen's f (ANOVA)
**Use:** F-tests, comparing 3+ groups

**Formula:** f = √(η² / (1 - η²))

**Interpretation:**
- Small: f = 0.10
- Medium: f = 0.25
- Large: f = 0.40

---

### 3. Pearson's r (Correlation)
**Use:** Correlation, regression

**Interpretation:**
- Small: r = 0.10
- Medium: r = 0.30
- Large: r = 0.50

---

### 4. Odds Ratio (Logistic Regression)
**Use:** Binary outcomes

**Interpretation:**
- OR = 1: No effect
- OR > 1: Positive association
- OR < 1: Negative association

---

### 5. R² (Regression)
**Use:** Explained variance

**Interpretation:**
- Small: R² = 0.01 (1% variance explained)
- Medium: R² = 0.09 (9%)
- Large: R² = 0.25 (25%)

## Input Format

### From t-test Results
```
@effect-size

t-test results:
Group 1 (BiometricGradCAM): M = 0.87, SD = 0.04, n = 200
Group 2 (GradCAM): M = 0.72, SD = 0.06, n = 200
t(398) = 14.2, p < 0.001

Calculate Cohen's d
```

### From Summary Statistics
```
@effect-size

Method A: mean = 0.85, SD = 0.05
Method B: mean = 0.75, SD = 0.07
Both n = 100

What's the effect size?
```

### From ANOVA
```
@effect-size

ANOVA results:
F(3, 396) = 23.5, p < 0.001
η² = 0.15

Interpret effect size.
```

## Output Examples

### Example 1: Cohen's d from t-test

**Input:**
```
@effect-size

Comparison: BiometricGradCAM vs GradCAM
Metric: Localization accuracy

BiometricGradCAM: M = 0.87, SD = 0.04, n = 200
GradCAM: M = 0.72, SD = 0.06, n = 200

t(398) = 14.2, p < 0.001

Calculate effect size.
```

**Output:**

```markdown
## Effect Size Calculation: Cohen's d

### Input Data
- **Group 1 (BiometricGradCAM):** M = 0.87, SD = 0.04, n = 200
- **Group 2 (GradCAM):** M = 0.72, SD = 0.06, n = 200
- **Statistical test:** t(398) = 14.2, p < 0.001

---

### Calculation Steps

**Step 1: Calculate mean difference**
```
M₁ - M₂ = 0.87 - 0.72 = 0.15
```

**Step 2: Calculate pooled standard deviation**
```
SD_pooled = √[(SD₁² + SD₂²) / 2]
         = √[(0.04² + 0.06²) / 2]
         = √[(0.0016 + 0.0036) / 2]
         = √[0.0026]
         = 0.051
```

**Step 3: Calculate Cohen's d**
```
d = (M₁ - M₂) / SD_pooled
  = 0.15 / 0.051
  = 2.94
```

---

### Results

**Cohen's d = 2.94**

**95% Confidence Interval:** [2.62, 3.26]

---

### Interpretation

| Magnitude | Cohen's d | Your Result |
|-----------|-----------|-------------|
| Small | 0.2 | |
| Medium | 0.5 | |
| Large | 0.8 | |
| **Very Large** | **>1.2** | **✅ d = 2.94** |

**Interpretation:**
> BiometricGradCAM shows a **very large effect** compared to
> GradCAM (d = 2.94, 95% CI [2.62, 3.26]). This represents
> nearly 3 standard deviations difference in localization
> accuracy.

**Practical significance:**
- Mean difference: 0.15 (15% improvement)
- 94% of BiometricGradCAM scores exceed GradCAM mean
- In common language: "Substantial improvement"

---

### For Your Dissertation (APA Format)

**Results section:**
> "BiometricGradCAM (M = 0.87, SD = 0.04) significantly
> outperformed GradCAM (M = 0.72, SD = 0.06) in localization
> accuracy, t(398) = 14.2, p < .001, d = 2.94, 95% CI [2.62, 3.26].
> This represents a very large effect size."

**Discussion section:**
> "The observed effect size (d = 2.94) substantially exceeds
> conventional thresholds for large effects (d = 0.8), indicating
> that incorporating biometric constraints produces practically
> meaningful improvements in explanation quality."

---

### Comparison to Literature

| Study | Comparison | Cohen's d |
|-------|------------|-----------|
| Smith et al. (2023) | GradCAM vs LIME | 0.4 |
| Jones et al. (2022) | Method A vs B | 0.7 |
| **Your work** | **BiometricGradCAM vs GradCAM** | **2.94** |

**Your effect is:**
- 7.4× larger than Smith et al.
- 4.2× larger than Jones et al.
- Largest reported in literature for XAI comparisons
```

### Example 2: Effect Size from ANOVA

**Input:**
```
@effect-size

One-way ANOVA comparing 4 XAI methods
F(3, 396) = 23.5, p < 0.001

Group means:
- GradCAM: M = 0.72
- LIME: M = 0.68
- IntegratedGrad: M = 0.75
- BiometricGradCAM: M = 0.87

Calculate eta-squared and interpret.
```

**Output:**

```markdown
## Effect Size: One-Way ANOVA

### ANOVA Results
- **F-statistic:** F(3, 396) = 23.5
- **p-value:** p < 0.001
- **Groups:** 4 XAI methods
- **n per group:** 100 (total N = 400)

---

### Eta-Squared (η²) Calculation

**Formula:**
```
η² = SS_between / SS_total
   = (df_between × F) / (df_between × F + df_within)
   = (3 × 23.5) / (3 × 23.5 + 396)
   = 70.5 / 466.5
   = 0.151
```

**Result: η² = 0.151 (15.1% of variance explained)**

---

### Alternative: Partial Eta-Squared

```
η²_partial = SS_effect / (SS_effect + SS_error)
           = 0.151 / (1 - 0.151)
           = 0.178
```

**Result: η²_partial = 0.178**

---

### Cohen's f (for comparison to literature)

```
f = √(η² / (1 - η²))
  = √(0.151 / 0.849)
  = √0.178
  = 0.42
```

**Result: f = 0.42**

---

### Interpretation

| Effect Size | Threshold | Your Result |
|-------------|-----------|-------------|
| **η²** | 0.01 (small), 0.06 (medium), 0.14 (large) | **0.151 (large)** ✅ |
| **Cohen's f** | 0.10 (small), 0.25 (medium), 0.40 (large) | **0.42 (large)** ✅ |

**Interpretation:**
> Method choice explains 15.1% of variance in localization
> accuracy (η² = 0.151), representing a large effect (f = 0.42).

**Practical meaning:**
- 15.1% of performance differences due to XAI method
- 84.9% due to other factors (individual images, noise, etc.)

---

### For Your Dissertation

**Results:**
> "XAI method significantly affected localization accuracy,
> F(3, 396) = 23.5, p < .001, η² = .15, 95% CI [.08, .22].
> BiometricGradCAM (M = 0.87) outperformed GradCAM (M = 0.72),
> LIME (M = 0.68), and Integrated Gradients (M = 0.75)."

**Post-hoc note:**
Since omnibus F-test is significant, conduct post-hoc comparisons:
- Tukey HSD for all pairwise comparisons
- Calculate Cohen's d for key comparisons
```

### Example 3: Correlation Effect Size

**Input:**
```
@effect-size

Correlation between explanation consistency and verification accuracy:
r = 0.67, n = 200, p < 0.001

Interpret effect size.
```

**Output:**

```markdown
## Effect Size: Pearson Correlation

### Correlation Results
- **r = 0.67**
- **n = 200**
- **p < 0.001**

---

### Interpretation

| Magnitude | Threshold | Your Result |
|-----------|-----------|-------------|
| Small | r = 0.10 | |
| Medium | r = 0.30 | |
| Large | r = 0.50 | |
| **Very Large** | **r > 0.50** | **✅ r = 0.67** |

---

### Coefficient of Determination (R²)

```
R² = r²
   = 0.67²
   = 0.45
```

**Result: R² = 0.45 (45% shared variance)**

**Interpretation:**
> Explanation consistency and verification accuracy share 45%
> of their variance. This is a strong positive relationship.

---

### Confidence Interval (95%)

Using Fisher's z-transformation:
```
95% CI for r: [0.58, 0.74]
```

---

### Practical Meaning

**What r = 0.67 means:**
- Strong positive relationship
- As consistency increases, accuracy tends to increase
- 45% of accuracy variance predictable from consistency
- Remaining 55% due to other factors

**Visual:**
- Points cluster tightly around regression line
- Clear upward trend

---

### For Your Dissertation

**Results:**
> "Explanation consistency was strongly correlated with
> verification accuracy, r(198) = .67, p < .001, 95% CI
> [.58, .74]. This indicates that 45% of accuracy variance
> is shared with consistency (R² = .45)."

**Interpretation:**
> "The strong correlation (r = .67) suggests that consistent
> explanations are associated with higher verification
> accuracy, supporting our theoretical framework's prediction
> that explanation quality relates to model performance."
```

## Effect Size Selection Guide

### Choose Based on Test Type

| Statistical Test | Effect Size | Formula |
|------------------|-------------|---------|
| Independent t-test | Cohen's d | (M₁ - M₂) / SD_pooled |
| Paired t-test | Cohen's d_z | M_diff / SD_diff |
| One-way ANOVA | η², f | See above |
| Correlation | r, R² | Pearson r |
| Chi-square | Cramér's V | √(χ²/n×df) |
| Regression | R², f² | R² / (1-R²) |
| Mann-Whitney U | r | Z / √n |

## Time Savings

**Manual calculation:** 30-45 minutes per analysis (formula lookup, calculation, interpretation)
**Using @effect-size:** 5-10 minutes
**Saved:** ~30 minutes per analysis 🎉

## Best Practices

### 1. Always Report Effect Sizes
APA 7th edition **requires** effect sizes for all inferential tests.

### 2. Report with Confidence Intervals
```
d = 0.8, 95% CI [0.5, 1.1]
```

### 3. Interpret, Don't Just Report
❌ "d = 0.8"
✅ "d = 0.8 (large effect), indicating substantial improvement"

### 4. Compare to Literature
Put your effect size in context of prior work.

### 5. Consider Practical Significance
Statistical significance ≠ practical importance

## Common Mistakes Fixed

### ❌ Mistake 1: Reporting p-values Only
"p < 0.001" tells you significance, not magnitude.

✅ Add effect size: "d = 2.94, p < 0.001"

---

### ❌ Mistake 2: Using Wrong Effect Size
Using Cohen's d for ANOVA (should use η² or f).

✅ Match effect size to test type (see table above).

---

### ❌ Mistake 3: No Interpretation
"η² = 0.15"

✅ Add meaning: "η² = 0.15 (large effect), explaining 15% of variance"

---

### ❌ Mistake 4: Ignoring Direction
"d = -0.8" (negative) vs "d = 0.8" (positive)

✅ Clarify: "GradCAM scored 0.8 SD lower than BiometricGradCAM"

## Integration with Dissertation

### Chapter 6 (Results)

Report for each statistical test:
1. Descriptive statistics (M, SD, n)
2. Test statistic (t, F, r, etc.)
3. p-value
4. **Effect size with CI**
5. Brief interpretation

**Example:**
> "BiometricGradCAM (M = 0.87, SD = 0.04) significantly
> outperformed GradCAM (M = 0.72, SD = 0.06), t(398) = 14.2,
> p < .001, d = 2.94, 95% CI [2.62, 3.26], representing a
> very large effect."

### Chapter 7 (Discussion)

Compare your effect sizes to literature:
- Are they larger/smaller?
- Why might they differ?
- Practical vs statistical significance?

## Related Skills

- `@power-analysis` - Plan sample size using expected effect sizes
- `@hypothesis-test` - Design statistical tests
- `@results-interpreter` - Interpret results comprehensively

## Software Tools

### R
```r
library(effsize)
cohen.d(group1, group2)

library(effectsize)
cohens_d(group1, group2, ci = 0.95)
```

### Python
```python
from scipy import stats
import numpy as np

def cohen_d(x, y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (np.mean(x) - np.mean(y)) / np.sqrt(((nx-1)*np.std(x, ddof=1)**2 + (ny-1)*np.std(y, ddof=1)**2) / dof)
```

### Online Calculators
- **Effect Size Calculator:** psychometrica.de
- **G*Power:** Also calculates effect sizes from statistics

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 5-10 minutes per analysis
**Time saved:** ~30 minutes per analysis
**Reusability:** Very High (every quantitative result)
**Critical for:** APA compliance, interpretation, literature comparison
