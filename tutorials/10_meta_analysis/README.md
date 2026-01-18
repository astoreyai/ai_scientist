# Tutorial 10: Meta-Analysis Deep Dive

**Duration**: 55 minutes
**Prerequisites**: Tutorial 2 completed (systematic review), basic statistics knowledge
**What you'll learn**: Forest plots, fixed vs. random effects, heterogeneity assessment, publication bias, subgroup analysis, meta-regression, PRISMA-MA reporting

---

## Overview

This tutorial demonstrates **meta-analysis** - quantitatively synthesizing evidence across studies. You'll learn:

1. When meta-analysis is appropriate (and when it's not)
2. Effect size calculation and standardization
3. Fixed effect vs. random effects models
4. Creating and interpreting forest plots
5. Assessing heterogeneity (I², Q-statistic, τ²)
6. Detecting publication bias (funnel plots, Egger's test, trim-and-fill)
7. Subgroup and meta-regression analyses
8. Sensitivity analyses
9. PRISMA-MA reporting guidelines
10. Using R packages (metafor, meta) or RevMan software

**Running Example**: Meta-analysis from Tutorial 2:
*"Effectiveness of Mindfulness-Based Interventions for Reducing Anxiety in Adolescents: A Meta-Analysis of 43 RCTs"*

**Why Meta-Analysis**:
- **Increase power**: Combine small studies
- **Resolve conflicts**: What works when studies disagree?
- **Precision**: Narrow confidence intervals
- **Generalizability**: Pooled estimate across populations

---

## Part 1: When to Conduct Meta-Analysis (5 minutes)

### Step 1.1: Appropriateness Criteria

**Meta-Analysis is Appropriate When**:

```
PICO similarity: Studies address same question
Outcome similarity: Same or comparable outcomes measured
Design similarity: Similar study designs (RCTs with RCTs)
Sufficient studies: At least 3-4 studies (more is better)
Data availability: Effect sizes and variance reported

DO NOT meta-analyze when:
✗ Apples and oranges: Studies too heterogeneous
✗ Poor quality: Studies have fatal flaws
✗ Inappropriate comparison: Different interventions/populations
```

**Our Example** (from Tutorial 2):
- PICO: Adolescents with anxiety, mindfulness interventions, anxiety outcomes
- Studies: 43 RCTs
- Outcome: Anxiety reduction (various scales, convertible to SMD)
- **Decision**: Meta-analysis appropriate ✓

**Checkpoint**: Confirmed meta-analysis is suitable.

---

### Step 1.2: Choose Effect Size Metric

**Common Effect Size Measures**:

```
═══════════════════════════════════════════════
        EFFECT SIZE SELECTION GUIDE
═══════════════════════════════════════════════

Continuous Outcomes (e.g., anxiety scores):
─────────────────────────────────────────────────
1. Standardized Mean Difference (SMD) - Cohen's d or Hedges' g
   When: Different scales measuring same construct
   Example: Some studies use GAD-7, others use SCARED
   → Convert all to SMD (scale-free)
   
   Formula: SMD = (Mean1 - Mean2) / Pooled SD

2. Mean Difference (MD)
   When: All studies use same scale
   Example: All studies use GAD-7
   → Interpret in original scale units

Binary Outcomes (e.g., remission yes/no):
─────────────────────────────────────────────────
3. Risk Ratio (RR) or Odds Ratio (OR)
   When: Event occurrence compared between groups
   Example: Proportion achieving remission

4. Risk Difference (RD)
   When: Absolute risk important
   Example: Number needed to treat (NNT)

Our Choice: SMD (Standardized Mean Difference)
Reason: Studies use different anxiety scales (GAD-7, SCARED, STAI-C)
```

**Checkpoint**: Effect size metric chosen (SMD).

---

## Part 2: Fixed vs. Random Effects Models (10 minutes)

### Step 2.1: Understanding the Models

**Two Fundamental Approaches**:

```
FIXED EFFECT MODEL
═══════════════════════════════════════════════

Assumption: One true effect size, variation is sampling error only

When to use:
  Studies very similar (same population, intervention, setting)
  Low heterogeneity (I² < 25%)
  
Interpretation: "The effect in THESE specific studies is..."

Weighting: Larger studies get more weight (inverse variance)
  Weight = 1 / SE²

RANDOM EFFECTS MODEL
═══════════════════════════════════════════════

Assumption: True effect varies across studies (distribution of effects)

When to use:
  Studies differ in populations, interventions, or settings
  Moderate-high heterogeneity (I² > 25%)
  Most systematic reviews (safer assumption)
  
Interpretation: "The average effect across similar studies is..."

Weighting: Accounts for between-study variance + within-study variance
  Weight = 1 / (SE² + τ²)
  τ² = between-study variance
```

**Visual Comparison**:

```
Fixed Effect: Studies estimate ONE true effect
     Study 1  ----[===]----
     Study 2 -----[==]-----
     Study 3  ---[====]---
              ↓
         TRUE EFFECT (single point)


Random Effects: Studies sample from a DISTRIBUTION of effects
     Study 1  ----[===]----
     Study 2 -----[==]-----
     Study 3  ---[====]---
              ↓
  DISTRIBUTION OF TRUE EFFECTS
     ●       ●   ●●  ●    ●
  ─────────────────────────────
```

**Our Example**:
- 43 RCTs across different countries, age ranges, interventions
- **Model**: Random effects (studies heterogeneous)

**Checkpoint**: Random effects model selected.

---

### Step 2.2: Calculate Pooled Effect

**Action**: Combine studies using random effects

```python
# Meta-analysis in R using metafor package

library(metafor)

# Data: 43 studies with effect sizes (SMD) and variances
data <- read.csv("mindfulness_anxiety_studies.csv")

# Calculate random effects meta-analysis
meta_result <- rma(yi = SMD, vi = variance, data = data, method = "REML")

summary(meta_result)
```

**Output**:

```
═══════════════════════════════════════════════
      RANDOM EFFECTS META-ANALYSIS RESULTS
═══════════════════════════════════════════════

Model: Random Effects (REML estimator)
k = 43 studies
n = 5,247 participants total

Pooled Effect Size:
  SMD = -0.42 (95% CI: -0.58 to -0.26)
  Z = -5.12, p < 0.001

Interpretation:
  Mindfulness interventions reduce anxiety by 0.42 standard deviations
  compared to control (moderate effect per Cohen's guidelines)

Heterogeneity:
  Q(df=42) = 116.67, p < 0.001 (significant heterogeneity)
  I² = 64.0% (moderate-to-high heterogeneity)
  τ² = 0.089 (between-study variance)
  τ = 0.298 (between-study SD)

Prediction Interval: -1.01 to 0.17
  (95% of true effects expected in this range)
```

**Interpretation Guide**:

```
Cohen's d Effect Sizes:
  Small:    d = 0.20
  Medium:   d = 0.50
  Large:    d = 0.80

Our SMD = -0.42 → Between small and medium (closer to medium)
Negative = favors mindfulness (anxiety reduction)
```

**Checkpoint**: Pooled effect calculated, statistically significant.

---

## Part 3: Forest Plots (10 minutes)

### Step 3.1: Creating a Forest Plot

**Forest Plot**: Visual display of meta-analysis results

```python
# Generate forest plot in R
forest(meta_result, 
       slab = data$study,  # Study labels
       xlab = "Standardized Mean Difference (SMD)",
       header = "Study",
       mlab = "Random Effects Model")
```

**Conceptual Forest Plot**:

```
═══════════════════════════════════════════════════════════════════════════
                    FOREST PLOT - Mindfulness for Adolescent Anxiety
═══════════════════════════════════════════════════════════════════════════

Study                        N      SMD (95% CI)            Weight
─────────────────────────────────────────────────────────────────────────────
Smith 2018                 120    -0.15 (-0.51,  0.21)      2.1% ──┼──
Jones 2019                  80    -0.42 (-0.86,  0.02)      1.6% ──┼──
Brown 2020                 156    -0.28 (-0.59,  0.03)      2.5% ──┼──
Lee 2021                    92    -0.09 (-0.50,  0.32)      1.8% ──┼──
Garcia 2021                134    -0.51 (-0.85, -0.17)  ◆   2.4% ──┼──
Taylor 2022                 78    -0.18 (-0.62,  0.26)      1.5% ──┼──
Wilson 2023                145    -0.37 (-0.69, -0.05)  ◆   2.5% ──┼──
Chen 2023                  108    -0.68 (-1.06, -0.30)  ◆   2.1% ──┼──
... [35 more studies]
─────────────────────────────────────────────────────────────────────────────
RE Model                 5,247    -0.42 (-0.58, -0.26)  ◆  100%  ──◆──

Heterogeneity: I² = 64%, τ² = 0.089, Q(42) = 116.67, p < 0.001

                     -1.0    -0.5     0.0     0.5     1.0
                     ◄─────────┼─────────┼─────────┼─────────►
                     Favors         No          Favors
                     Mindfulness  Difference    Control
═══════════════════════════════════════════════════════════════════════════

Key Elements:
─────────────────────────────────────────────────────────────────────────────
● Each row = one study
● Box size = study weight (larger box = more weight)
● Horizontal line = 95% confidence interval
● Diamond = pooled estimate (random effects)
● Vertical line at 0 = null effect (no difference)
● Studies crossing 0 = not statistically significant individually
● Diamond not crossing 0 = overall effect significant
```

**Checkpoint**: Forest plot visually summarizes all studies.

---

### Step 3.2: Interpreting Forest Plots

**Key Questions to Ask**:

```
1. Overall Effect:
   Q: Does the diamond cross zero?
   A: No → Significant effect
   
   Our plot: Diamond at -0.42, CI (-0.58 to -0.26) → Doesn't cross zero ✓

2. Consistency:
   Q: Are most studies on the same side of zero?
   A: Yes → Consistent direction
   
   Our plot: 38/43 studies favor mindfulness (left side) → Consistent ✓

3. Heterogeneity (visual):
   Q: Do confidence intervals overlap?
   A: Some overlap, some don't → Moderate heterogeneity
   
   Our plot: CIs range from -1.06 to +0.32 → Heterogeneous ✓

4. Influential Studies:
   Q: Are there outliers with very different effects?
   A: Yes → Sensitivity analysis needed
   
   Our plot: Chen 2023 (SMD = -0.68) larger than others → Investigate
```

**Checkpoint**: Forest plot interpreted correctly.

---

## Part 4: Heterogeneity Assessment (10 minutes)

### Step 4.1: Three Heterogeneity Statistics

**Why Heterogeneity Matters**: If studies differ substantially, pooled estimate may be misleading

```
═══════════════════════════════════════════════
      HETEROGENEITY STATISTICS EXPLAINED
═══════════════════════════════════════════════

1. Q-Statistic (Cochran's Q)
   Purpose: Test if heterogeneity exists
   Interpretation: 
     Q > df → Heterogeneity present
     p < 0.05 → Significant heterogeneity
   
   Our result: Q(42) = 116.67, p < 0.001
   Conclusion: Significant heterogeneity exists

   Limitation: Depends on number of studies (low power with few studies)

2. I² (I-squared)
   Purpose: Quantify proportion of variance due to heterogeneity
   Formula: I² = (Q - df) / Q × 100%
   
   Interpretation guidelines (Higgins & Thompson):
     0-25%:   Low heterogeneity (might not matter)
     25-50%:  Moderate heterogeneity (explore sources)
     50-75%:  Substantial heterogeneity (explain or stratify)
     75-100%: Considerable heterogeneity (meta-analysis questionable)
   
   Our result: I² = 64%
   Conclusion: Substantial heterogeneity → Need to explore sources

3. τ² (tau-squared) and τ (tau)
   Purpose: Estimate between-study variance
   Units: Same as effect size (SMD scale)
   
   Our result: τ² = 0.089, τ = 0.298
   
   Interpretation: 
     Prediction interval = -0.42 ± 1.96 × 0.298 = (-1.01 to 0.17)
     Future study effect expected between -1.01 and +0.17
     (Includes null effect! High uncertainty)
```

**Decision Tree**:

```
Is I² > 50%?
     │
     ├─ NO (I² ≤ 50%) → Proceed with pooled estimate confidently
     │
     └─ YES (I² > 50%) → EXPLORE HETEROGENEITY
              │
              ├─ Subgroup analysis (categorical moderators)
              ├─ Meta-regression (continuous moderators)
              ├─ Sensitivity analysis (exclude outliers)
              └─ Consider NOT pooling if I² > 75% and unexplained
```

**Checkpoint**: Substantial heterogeneity detected, requires exploration.

---

### Step 4.2: Exploring Sources of Heterogeneity

**Subgroup Analysis**: Compare effect by categorical variable

```python
# Subgroup analysis: Delivery format (in-person vs. online)

subgroup_result <- rma(yi = SMD, vi = variance, 
                       mods = ~ factor(delivery_format), 
                       data = data, method = "REML")
```

**Result**:

```
Subgroup Analysis: Delivery Format
═══════════════════════════════════════════════

In-Person (k=35):     SMD = -0.48 (95% CI: -0.62 to -0.34)  I² = 52%
Online (k=8):         SMD = -0.22 (95% CI: -0.45 to  0.01)  I² = 71%

Test of Moderation:   Q_between = 5.42, p = 0.02

Interpretation: Delivery format explains some heterogeneity
  - In-person more effective than online
  - Online effect not statistically significant (CI crosses zero)
  - I² still moderate within subgroups (other sources exist)
```

**Meta-Regression**: Continuous moderator

```python
# Meta-regression: Age as moderator

meta_reg <- rma(yi = SMD, vi = variance, 
                mods = ~ mean_age, 
                data = data, method = "REML")
```

**Result**:

```
Meta-Regression: Mean Age
═══════════════════════════════════════════════

Coefficient for age: β = 0.03 (SE = 0.02), p = 0.12
Interpretation: Older adolescents show slightly smaller effects, 
                but not statistically significant

R²: 12% of between-study variance explained by age
Residual I²: 57% (heterogeneity partially explained)
```

**Checkpoint**: Identified delivery format as moderator.

---

## Part 5: Publication Bias Assessment (10 minutes)

### Step 5.1: Funnel Plot

**Funnel Plot**: Scatter plot of effect size vs. precision

```python
# Create funnel plot
funnel(meta_result, xlab = "SMD")
```

**Conceptual Funnel Plot**:

```
═══════════════════════════════════════════════
              FUNNEL PLOT
═══════════════════════════════════════════════

Precision
(1/SE)
   ↑
   │
   │                    ●
 5 │                 ●  ●  ●
   │              ●  ● ●●● ●  ●
 4 │            ●  ●●●●●●●●●  ●
   │          ●  ●●●●●●●●●●●  ●  ●
 3 │        ●  ●●●●●●●●●●●●●●  ●
   │      ●  ●●●●●●●●●●●●●●●●  ●
 2 │    ●  ●●●●●●●●●●●●●●●●●●  ●
   │  ●  ●●●●●●●●●●●●●●●●●●●●  ●
 1 │●  ●●●●●●●●●●●●●●●●●●●●●●  ●
   │
   └────────────────────────────────→
   -1.5  -1.0  -0.5   0.0   0.5   1.0
              Effect Size (SMD)

Interpretation:
─────────────────────────────────────────────────
SYMMETRIC funnel: No obvious publication bias
  - Studies distributed evenly on both sides
  - Smaller studies (bottom) show wider spread (expected)

✗ ASYMMETRIC funnel: Possible publication bias
  - Missing studies on one side (usually null/negative)
  - "Gap" on bottom right = small studies with null effects missing

Our plot: Slight asymmetry (fewer small studies on right)
  → Possible publication bias (small negative studies published more than small null)
```

**Checkpoint**: Visual inspection suggests possible publication bias.

---

### Step 5.2: Egger's Test

**Egger's Regression Test**: Statistical test for funnel plot asymmetry

```python
# Egger's test
regtest(meta_result, model = "lm")
```

**Result**:

```
Egger's Test for Funnel Plot Asymmetry
═══════════════════════════════════════════════

Regression intercept: 1.24 (SE = 0.51)
t(41) = 2.43, p = 0.02

Interpretation: Significant asymmetry (p < 0.05)
  → Evidence of publication bias or small-study effects
```

**Alternative**: Trim-and-Fill Method

```python
# Trim-and-fill: Impute missing studies
trimfill_result <- trimfill(meta_result)
```

**Result**:

```
Trim-and-Fill Analysis
═══════════════════════════════════════════════

Estimated missing studies: 7 (on the right side, null effects)

Original pooled effect:   SMD = -0.42 (95% CI: -0.58 to -0.26)
Adjusted pooled effect:   SMD = -0.35 (95% CI: -0.51 to -0.19)

Interpretation: After imputing missing studies, effect remains significant
                but slightly attenuated (publication bias present but
                doesn't change overall conclusion)
```

**Checkpoint**: Publication bias detected but effect remains robust.

---

## Part 6: Sensitivity Analyses (5 minutes)

### Step 6.1: Common Sensitivity Analyses

**Purpose**: Test if results are robust to methodological decisions

```
Sensitivity Analysis 1: Exclude Low-Quality Studies
═══════════════════════════════════════════════

Original (k=43):           SMD = -0.42 (95% CI: -0.58 to -0.26)
High-quality only (k=28):  SMD = -0.48 (95% CI: -0.65 to -0.31)

Conclusion: Effect stronger when limited to high-quality studies ✓

Sensitivity Analysis 2: Exclude Outliers
═══════════════════════════════════════════════

Original (k=43):        SMD = -0.42 (95% CI: -0.58 to -0.26), I² = 64%
Without Chen 2023 (k=42): SMD = -0.40 (95% CI: -0.55 to -0.25), I² = 59%

Conclusion: Outlier has minimal impact ✓

Sensitivity Analysis 3: Fixed vs. Random Effects
═══════════════════════════════════════════════

Random effects (default): SMD = -0.42 (95% CI: -0.58 to -0.26)
Fixed effect:             SMD = -0.39 (95% CI: -0.47 to -0.31)

Conclusion: Model choice doesn't materially change result ✓

Sensitivity Analysis 4: Leave-One-Out Analysis
═══════════════════════════════════════════════

Remove each study sequentially, recalculate pooled effect:

  Range: SMD = -0.39 to -0.44
  Median: SMD = -0.42

Conclusion: No single study drives the overall effect ✓
```

**Checkpoint**: Results robust across sensitivity analyses.

---

## Part 7: PRISMA-MA Reporting (5 minutes)

### Step 7.1: PRISMA for Meta-Analysis

**Additional Items Beyond PRISMA 2020**:

```
═══════════════════════════════════════════════
         PRISMA-MA CHECKLIST (Extensions)
═══════════════════════════════════════════════

Beyond standard PRISMA 2020, report:

Effect Size Metric: Standardized mean difference (Hedges' g)
Meta-Analysis Model: Random effects (REML estimator)
Weighting: Inverse variance
Heterogeneity Statistics: Q, I², τ²
Subgroup Analyses: Delivery format, age (pre-specified)
Meta-Regression: Age as moderator
Publication Bias: Funnel plot, Egger's test, trim-and-fill
Sensitivity Analyses: Quality, outliers, model choice, leave-one-out
Software: R metafor package v3.8-1
Data Availability: Effect sizes and code on OSF (DOI: 10.17605/OSF.IO/ABC123)

Forest Plot: Figure 2
Funnel Plot: Figure 3
Subgroup Forest Plots: Supplemental Figures S1-S3
```

**Manuscript Checklist**:

```
Abstract:
  Number of studies and participants
  Pooled effect with 95% CI
  Heterogeneity (I²)
  Key moderator

Results Section:
  Forest plot (main analysis)
  Heterogeneity statistics table
  Subgroup analysis table
  Funnel plot
  Sensitivity analysis table

Discussion:
  Interpret pooled effect (clinical significance)
  Explain heterogeneity (moderators identified)
  Address publication bias (limitations)
  Implications for practice
```

**Checkpoint**: PRISMA-MA compliance ensured.

---

## Summary and Next Steps

### What You've Learned

**Meta-Analysis Essentials**:
- Determined appropriateness (PICO similarity, sufficient studies)
- Chose effect size metric (SMD for different scales)
- Selected model (random effects for heterogeneous studies)
- Calculated pooled effect (SMD = -0.42, p < 0.001)
- Created forest plot (visual summary of 43 studies)
- Assessed heterogeneity (I² = 64%, substantial)
- Explored moderators (subgroup analysis, meta-regression)
- Detected publication bias (Egger's test, trim-and-fill)
- Conducted sensitivity analyses (robust results)
- Reported per PRISMA-MA guidelines

**Key Insights**:
- Random effects model safer for heterogeneous studies
- I² > 50% requires exploration of heterogeneity
- Publication bias doesn't always invalidate results
- Sensitivity analyses test robustness

**Our Example Results**:
- Mindfulness reduces adolescent anxiety (SMD = -0.42, moderate effect)
- In-person delivery more effective than online
- Results robust to publication bias and quality restrictions

---

### Tools and Resources

**Software**:
- **R metafor package**: Most flexible, publication-quality
- **R meta package**: User-friendly alternative
- **RevMan** (Cochrane): Free, GUI-based
- **Stata**: metan command
- **JASP**: Free GUI alternative

**Reporting**:
- **PRISMA-MA**: Extension for meta-analyses
- **Cochrane Handbook**: Comprehensive methods guide

**Books**:
- Borenstein et al. (2021): *Introduction to Meta-Analysis*
- Harrer et al. (2021): *Doing Meta-Analysis with R*

---

### Next Steps

**After This Tutorial**:
1. Pre-register meta-analysis protocol (PROSPERO)
2. Extract effect sizes systematically
3. Use R or RevMan for analysis
4. Report transparently per PRISMA-MA
5. Share data and code on OSF

**See Also**:
- Tutorial 2: Systematic Review (foundation for meta-analysis)
- Network Meta-Analysis Template (comparing multiple interventions)

---

**Tutorial Complete!** You now know how to conduct, interpret, and report rigorous meta-analyses with heterogeneity assessment and publication bias detection.
