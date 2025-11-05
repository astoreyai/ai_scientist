# @hypothesis-test - Design Hypothesis Tests

Design rigorous statistical hypothesis tests for your dissertation research.

## Skill Type
**Category:** Statistics / Methodology
**Tier:** Core (Tier 1)
**Reusability:** Very High - every quantitative study needs hypothesis tests

## What This Skill Does

1. Formulates null and alternative hypotheses
2. Selects appropriate statistical tests
3. Specifies assumptions and validation
4. Determines significance level and power
5. Plans analysis workflow

## Invocation

```
@hypothesis-test [research-question] [data-type]
```

## Hypothesis Components

### 1. Null Hypothesis (H₀)
**States:** No effect, no difference, no relationship

**Examples:**
- H₀: μ₁ = μ₂ (means are equal)
- H₀: ρ = 0 (no correlation)
- H₀: p₁ = p₂ (proportions equal)

### 2. Alternative Hypothesis (H₁ or Hₐ)
**States:** There is an effect, difference, or relationship

**Types:**
- **Two-tailed:** H₁: μ₁ ≠ μ₂ (different, any direction)
- **One-tailed:** H₁: μ₁ > μ₂ (specific direction)

### 3. Test Statistic
The calculated value (t, F, Z, χ², etc.)

### 4. Significance Level (α)
Usually 0.05 (5% false positive rate)

### 5. Decision Rule
If p < α, reject H₀; otherwise, fail to reject H₀

## Test Selection Guide

### Continuous Outcomes

| Research Question | Test | Assumptions |
|-------------------|------|-------------|
| Compare 2 groups (independent) | Independent t-test | Normality, equal variance |
| Compare 2 groups (paired) | Paired t-test | Normality of differences |
| Compare 3+ groups | One-way ANOVA | Normality, homogeneity |
| Compare groups × conditions | Two-way ANOVA | Normality, homogeneity |
| Relationship between 2 variables | Pearson correlation | Linearity, normality |
| Predict outcome from predictors | Multiple regression | Linearity, independence, normality |

### Categorical Outcomes

| Research Question | Test | Assumptions |
|-------------------|------|-------------|
| Compare proportions (2 groups) | Chi-square test | Expected frequency ≥ 5 |
| Compare proportions (2 groups, small n) | Fisher's exact | None (exact test) |
| Association between variables | Chi-square test | Independence |
| Predict binary outcome | Logistic regression | Independence, linearity (logit) |

### Non-Parametric (No Normality Assumed)

| Research Question | Test | Use When |
|-------------------|------|----------|
| Compare 2 groups | Mann-Whitney U | Ordinal data, non-normal |
| Compare paired groups | Wilcoxon signed-rank | Paired, non-normal |
| Compare 3+ groups | Kruskal-Wallis | Non-normal, ordinal |
| Correlation (non-parametric) | Spearman's ρ | Monotonic, not linear |

## Input Format

### From Research Question
```
@hypothesis-test

RQ: Does BiometricGradCAM improve localization accuracy compared to GradCAM?

Data:
- DV: Localization accuracy (continuous, 0-1)
- IV: Method (2 levels: BiometricGradCAM, GradCAM)
- Design: Between-subjects
- n = 200 per method
```

### Multiple Hypotheses
```
@hypothesis-test

Study: XAI method comparison
Groups: 4 methods (GradCAM, LIME, IG, BiometricGradCAM)
Metrics: Localization accuracy, consistency, faithfulness

Design all hypothesis tests.
```

### Assumption Checking
```
@hypothesis-test

I want to run a t-test but not sure if data meets assumptions.
How do I check?
```

## Output Examples

### Example 1: Two-Group Comparison

**Input:**
```
@hypothesis-test

RQ: Does BiometricGradCAM achieve higher localization accuracy than GradCAM?

Data:
- Outcome: Localization accuracy (continuous, 0-1 scale)
- Groups: BiometricGradCAM (n=200), GradCAM (n=200)
- Design: Independent groups (different image pairs)
- Distribution: Approximately normal (will verify)
```

**Output:**

```markdown
## Hypothesis Test Design: BiometricGradCAM vs GradCAM

### Research Question
> Does BiometricGradCAM achieve higher localization accuracy than GradCAM?

---

### Step 1: Formulate Hypotheses

**Null Hypothesis (H₀):**
> There is no difference in mean localization accuracy between BiometricGradCAM and GradCAM.

**Formal:** H₀: μ_BiometricGradCAM = μ_GradCAM
OR: H₀: μ₁ - μ₂ = 0

**Alternative Hypothesis (H₁):**
> BiometricGradCAM has higher mean localization accuracy than GradCAM.

**Formal:** H₁: μ_BiometricGradCAM > μ_GradCAM
OR: H₁: μ₁ - μ₂ > 0

**Type:** One-tailed test (directional hypothesis)

**Rationale:** Theory predicts BiometricGradCAM should be better (not just different).

---

### Step 2: Select Statistical Test

**Recommended Test:** **Independent samples t-test** (one-tailed)

**Why this test?**
- ✅ Two independent groups
- ✅ Continuous outcome variable
- ✅ Approximately normal distribution (to verify)
- ✅ Large sample sizes (n=200 per group)

**Alternative if assumptions fail:**
- Mann-Whitney U test (if non-normal)

---

### Step 3: Check Assumptions

**Assumption 1: Independence**
- ✅ Each observation independent (different image pairs)
- ✅ No repeated measures

**Assumption 2: Normality**
Check with:
- Shapiro-Wilk test (if n < 50 per group)
- Q-Q plots (visual inspection)
- Histograms

**Code (R):**
```r
shapiro.test(biometric_scores)
shapiro.test(gradcam_scores)
qqnorm(biometric_scores)
qqline(biometric_scores)
```

**Code (Python):**
```python
from scipy import stats
stats.shapiro(biometric_scores)
stats.probplot(biometric_scores, plot=plt)
```

**If violated:** Use Mann-Whitney U (non-parametric alternative)

**Assumption 3: Homogeneity of Variance**
Check with Levene's test:

**Code (R):**
```r
car::leveneTest(accuracy ~ method)
```

**Code (Python):**
```python
stats.levene(biometric_scores, gradcam_scores)
```

**If violated:** Use Welch's t-test (does not assume equal variances)

---

### Step 4: Set Parameters

**Significance Level (α):** 0.05 (5% Type I error rate)

**Power (1-β):** 0.80 (80% probability of detecting true effect)

**Expected Effect Size:** d = 0.5 (medium, based on literature)

**Sample Size:** n = 200 per group
- ✅ Adequate for d = 0.5, α = 0.05, power = 0.80 (requires n = 64)
- ✅ Exceeds minimum, provides power > 0.94

---

### Step 5: Decision Rule

**If p < 0.05 (one-tailed):**
- Reject H₀
- Conclude: BiometricGradCAM has significantly higher localization accuracy
- Report: t-statistic, df, p-value, effect size (Cohen's d), 95% CI

**If p ≥ 0.05:**
- Fail to reject H₀
- Conclude: Insufficient evidence that BiometricGradCAM is better
- Report: t-statistic, df, p-value, effect size, 95% CI
- Consider: power analysis (was study adequately powered?)

---

### Step 6: Analysis Workflow

**1. Data preparation**
```r
# R example
data <- data.frame(
  accuracy = c(biometric_scores, gradcam_scores),
  method = c(rep("BiometricGradCAM", 200), rep("GradCAM", 200))
)
```

**2. Descriptive statistics**
```r
library(dplyr)
data %>%
  group_by(method) %>%
  summarize(
    mean = mean(accuracy),
    sd = sd(accuracy),
    n = n(),
    se = sd / sqrt(n)
  )
```

**3. Check assumptions**
```r
# Normality
shapiro.test(data$accuracy[data$method == "BiometricGradCAM"])
shapiro.test(data$accuracy[data$method == "GradCAM"])

# Homogeneity
car::leveneTest(accuracy ~ method, data = data)
```

**4. Conduct t-test**
```r
# One-tailed t-test
t.test(
  accuracy ~ method,
  data = data,
  alternative = "greater",  # BiometricGradCAM > GradCAM
  var.equal = TRUE  # or FALSE if Levene's test significant
)
```

**5. Calculate effect size**
```r
library(effsize)
cohen.d(
  data$accuracy[data$method == "BiometricGradCAM"],
  data$accuracy[data$method == "GradCAM"]
)
```

**6. Visualize**
```r
library(ggplot2)
ggplot(data, aes(x = method, y = accuracy)) +
  geom_boxplot() +
  geom_jitter(alpha = 0.2) +
  labs(title = "Localization Accuracy by Method",
       y = "Accuracy", x = "XAI Method")
```

---

### Step 7: Report Results (APA Format)

**If significant:**
> "An independent samples t-test revealed that BiometricGradCAM
> (M = 0.87, SD = 0.04) achieved significantly higher localization
> accuracy than GradCAM (M = 0.72, SD = 0.06), t(398) = 14.2,
> p < .001 (one-tailed), d = 2.94, 95% CI [2.62, 3.26]. This
> represents a very large effect size, indicating substantial
> improvement in explanation quality."

**If not significant:**
> "An independent samples t-test found no significant difference
> in localization accuracy between BiometricGradCAM (M = 0.75,
> SD = 0.08) and GradCAM (M = 0.72, SD = 0.07), t(398) = 1.5,
> p = .067 (one-tailed), d = 0.20, 95% CI [-0.02, 0.42]. The
> observed effect was small and not statistically significant
> at the α = .05 level."

---

### Step 8: Interpret & Discuss

**If significant:**
- What does the mean difference (0.15) mean practically?
- How does effect size (d = 2.94) compare to literature?
- Are results generalizable beyond this sample?
- What explains the large effect?

**If not significant:**
- Was the study adequately powered? (Check post-hoc)
- Could effect be too small to detect?
- Are there confounds or measurement issues?
- What does this mean for theory/practice?

---

### Assumptions Summary Table

| Assumption | Check | Result | Action if Violated |
|------------|-------|--------|-------------------|
| Independence | Study design | ✅ Met | N/A |
| Normality | Shapiro-Wilk, Q-Q plots | ✅ Met | Use Mann-Whitney U |
| Homogeneity | Levene's test | ✅ Met | Use Welch's t-test |

---

### For Your Dissertation

**Chapter 4 (Methodology):**
> "To test whether BiometricGradCAM achieves higher localization
> accuracy than GradCAM, we conducted an independent samples
> t-test (one-tailed, α = .05). We verified assumptions of
> normality (Shapiro-Wilk, p > .05) and homogeneity of variance
> (Levene's test, p > .05). Sample size (n = 200 per group)
> provided >94% power to detect medium effects (d = 0.5)."

**Chapter 6 (Results):**
[Report as shown in Step 7]

**Chapter 7 (Discussion):**
> "The observed large effect (d = 2.94) substantially exceeds
> prior comparisons in the XAI literature (typical d = 0.3-0.7),
> suggesting that accounting for biometric constraints produces
> practically meaningful improvements..."
```

### Example 2: Multiple Group Comparison

**Input:**
```
@hypothesis-test

RQ: Do the four XAI methods differ in localization accuracy?

Methods: GradCAM, LIME, IntegratedGradients, BiometricGradCAM
n = 100 per method (400 total)
DV: Localization accuracy (continuous)
```

**Output:**

```markdown
## Hypothesis Test: Four XAI Methods

### Step 1: Hypotheses

**H₀:** μ₁ = μ₂ = μ₃ = μ₄
(All four methods have equal mean accuracy)

**H₁:** At least one mean differs from the others

**Type:** Omnibus test (not directional)

---

### Step 2: Test Selection

**Primary Test:** **One-way ANOVA**

**Why?**
- ✅ More than 2 groups (k = 4)
- ✅ Continuous DV
- ✅ Independent groups

**Post-Hoc Tests (if ANOVA significant):**
- Tukey HSD (all pairwise comparisons)
- Bonferroni correction (conservative)
- Dunnett's test (if comparing all to control)

---

### Step 3: ANOVA Assumptions

1. **Independence:** ✅ Different images per method
2. **Normality:** Check per group (n=100 is robust)
3. **Homogeneity of variance:** Levene's test

---

### Step 4: Analysis Plan

**1. Omnibus ANOVA**
```r
model <- aov(accuracy ~ method, data = data)
summary(model)
```

**2. If significant, post-hoc**
```r
TukeyHSD(model)
```

**3. Effect size**
```r
# Eta-squared
library(effectsize)
eta_squared(model)
```

---

### Step 5: Report

**If significant:**
> "A one-way ANOVA revealed a significant effect of XAI method
> on localization accuracy, F(3, 396) = 23.5, p < .001, η² = .15.
> Post-hoc comparisons using Tukey HSD indicated that
> BiometricGradCAM (M = 0.87) significantly outperformed all
> other methods: GradCAM (M = 0.72, p < .001), LIME (M = 0.68,
> p < .001), and Integrated Gradients (M = 0.75, p < .001)."
```

## Common Mistakes Fixed

### ❌ Mistake 1: Vague Hypotheses
"H₀: There is no effect"

✅ Specific: "H₀: μ_treatment = μ_control"

---

### ❌ Mistake 2: Wrong Test Choice
Using t-test for 4 groups (inflates Type I error)

✅ Use ANOVA for 3+ groups

---

### ❌ Mistake 3: Ignoring Assumptions
Running t-test without checking normality

✅ Always validate assumptions first

---

### ❌ Mistake 4: One-Tailed Without Justification
Using one-tailed test just to get p < 0.05

✅ Only use if strong directional hypothesis a priori

## Time Savings

**Manual hypothesis design:** 2-3 hours (test selection, assumption planning, analysis workflow)
**Using @hypothesis-test:** 15-20 minutes
**Saved:** ~2 hours 🎉

## Best Practices

### 1. Preregister Hypotheses
Specify hypotheses BEFORE data collection (avoids p-hacking).

### 2. Match Test to Data Type
Continuous → t-test/ANOVA
Categorical → Chi-square
Non-normal → Non-parametric

### 3. Check Assumptions
Always validate before running parametric tests.

### 4. Report Everything
Test statistic, df, p-value, effect size, CI

### 5. Interpret, Don't Just Report
What does this mean for your research question?

## Integration with Dissertation

### Chapter 4 (Methodology)

```markdown
## 4.5 Statistical Analysis

### 4.5.1 Hypothesis 1: BiometricGradCAM vs GradCAM
H₀: μ_BiometricGradCAM = μ_GradCAM

Test: Independent t-test (one-tailed, α = .05)

### 4.5.2 Hypothesis 2: Method Comparison
H₀: μ₁ = μ₂ = μ₃ = μ₄

Test: One-way ANOVA (α = .05), Tukey HSD post-hoc

### 4.5.3 Assumption Validation
All assumptions verified prior to analysis (see Section 4.5.4).
```

## Related Skills

- `@power-analysis` - Determine sample size for hypothesis tests
- `@effect-size` - Calculate and interpret effect sizes
- `@research-questions` - RQs inform hypotheses
- `@results-interpreter` - Interpret test results

## Software Integration

### R
```r
# t-test
t.test(group1, group2)

# ANOVA
aov(DV ~ IV, data = df)

# Check assumptions
shapiro.test(data)
car::leveneTest(DV ~ IV, data = df)
```

### Python
```python
from scipy import stats

# t-test
stats.ttest_ind(group1, group2)

# ANOVA
stats.f_oneway(group1, group2, group3)

# Assumptions
stats.shapiro(data)
stats.levene(group1, group2)
```

---

**Status:** Documented
**Complexity:** Medium-High
**Time to use:** 15-20 minutes
**Time saved:** ~2 hours
**Reusability:** Very High (every quantitative study)
**Critical for:** Methodology design, statistical rigor, results interpretation
