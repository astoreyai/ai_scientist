# @power-analysis - Statistical Power Analysis

Calculate required sample sizes and statistical power for rigorous experimental design.

## Skill Type
**Category:** Statistics / Methodology
**Tier:** Core (Tier 1)
**Reusability:** Very High - every experimental study needs this

## What This Skill Does

1. Calculates required sample size for desired power
2. Estimates power given sample size
3. Determines minimum detectable effect size
4. Validates experimental design feasibility
5. Supports multiple statistical tests

## Invocation

```
@power-analysis [test-type] [parameters]
```

## Statistical Tests Supported

### 1. Two-Sample t-test
**Use case:** Compare means between two groups

**Parameters:**
- Effect size (Cohen's d)
- Significance level (α)
- Power (1 - β)
- Sample allocation ratio

### 2. ANOVA (One-Way)
**Use case:** Compare means across 3+ groups

**Parameters:**
- Effect size (Cohen's f)
- Number of groups
- Significance level
- Power

### 3. Correlation
**Use case:** Test relationship between variables

**Parameters:**
- Expected correlation (ρ)
- Significance level
- Power

### 4. Proportion Test
**Use case:** Compare proportions/percentages

**Parameters:**
- p₁, p₂ (proportions in each group)
- Significance level
- Power

### 5. Chi-Square Test
**Use case:** Categorical data association

**Parameters:**
- Effect size (w)
- Degrees of freedom
- Significance level
- Power

## Input Format

### Simple Query
```
@power-analysis t-test

I want to detect a medium effect (d=0.5) with 80% power.
What sample size do I need?
```

### Detailed Specification
```json
{
  "test": "two-sample-t-test",
  "effect_size": 0.5,
  "alpha": 0.05,
  "power": 0.80,
  "tails": "two-tailed",
  "allocation_ratio": 1
}
```

### Reverse Calculation
```
@power-analysis

I have n=50 per group. What power do I have to detect d=0.5?
```

## Output Examples

### Example 1: Sample Size Calculation

**Input:**
```
@power-analysis t-test

Research question: Does my XAI method improve localization accuracy?
Expected effect: Medium (Cohen's d = 0.5)
Desired power: 80%
Alpha: 0.05
Groups: 2 (baseline vs proposed method)
```

**Output:**
```markdown
## Statistical Power Analysis: Two-Sample t-test

### Parameters
- Test: Independent two-sample t-test (two-tailed)
- Effect size: d = 0.5 (medium)
- Significance level: α = 0.05
- Desired power: 1 - β = 0.80
- Allocation ratio: 1:1 (equal groups)

### Results
**Required sample size:**
- **n = 64 per group**
- **Total N = 128**

### Interpretation
To detect a medium effect (d = 0.5) with 80% power at α = 0.05:
- You need at least **64 samples per group**
- Total dataset: **128 samples**

### Robustness Check
Power at different sample sizes:
| n per group | Total N | Power |
|-------------|---------|-------|
| 40          | 80      | 0.65  |
| 50          | 100     | 0.70  |
| **64**      | **128** | **0.80** ✅ |
| 80          | 160     | 0.88  |
| 100         | 200     | 0.94  |

### Recommendations
1. ✅ Target n = 64 per group minimum
2. ✅ Consider n = 80 per group for safety margin
3. ⚠️ With n < 64, you risk underpowered study
4. 💡 If resources constrained, reconsider effect size expectations

### For Your Dissertation
In Chapter 4 (Methodology), include:
> "A priori power analysis using G*Power 3.1 indicated that a
> sample size of 64 per group would provide 80% power to detect
> a medium effect (d = 0.5) using a two-tailed independent
> samples t-test with α = 0.05."
```

### Example 2: Power Given Sample Size

**Input:**
```
@power-analysis

I have VGGFace2 dataset with n = 200 verification pairs.
What power do I have to detect:
- Small effect (d = 0.2)
- Medium effect (d = 0.5)
- Large effect (d = 0.8)
```

**Output:**
```markdown
## Power Analysis: Given Sample Size

### Your Dataset
- Sample size: n = 200 per group
- Test: Two-sample t-test (two-tailed)
- Alpha: 0.05

### Statistical Power by Effect Size

| Effect Size | Cohen's d | Power | Interpretation |
|-------------|-----------|-------|----------------|
| Small       | 0.2       | 0.29  | ❌ Underpowered |
| Medium      | 0.5       | 0.94  | ✅ Well-powered |
| Large       | 0.8       | >0.99 | ✅ Excellent |

### Minimum Detectable Effect Size
With n = 200 and power = 0.80:
- **MDE = 0.40** (between small and medium)

### Implications for Your Study
✅ **Strengths:**
- Excellent power (94%) for medium effects
- Can detect effects as small as d = 0.40

⚠️ **Limitations:**
- Insufficient power (29%) for small effects (d = 0.2)
- Cannot make claims about subtle differences

### For Your Dissertation
In Chapter 4 (Methodology) - Sample Size Justification:
> "With n = 200 verification pairs, our study achieves 94%
> power to detect medium effects (d = 0.5) at α = 0.05.
> The minimum detectable effect size is d = 0.40, ensuring
> adequate sensitivity for practically meaningful differences
> in XAI method performance."

In Chapter 7 (Limitations):
> "Our sample size provides insufficient power (29%) to
> detect small effects (d < 0.4). Future work should employ
> larger samples to detect more subtle performance differences."
```

### Example 3: Multiple Comparisons

**Input:**
```
@power-analysis ANOVA

Study design:
- 4 XAI methods (GradCAM, LIME, IntegratedGradients, BiometricGradCAM)
- Outcome: Localization accuracy (0-1 scale)
- Expected effect: Medium (f = 0.25)
- Power: 0.80
- Alpha: 0.05
```

**Output:**
```markdown
## Power Analysis: One-Way ANOVA

### Study Design
- Number of groups: k = 4
- Test: One-way ANOVA (omnibus F-test)
- Effect size: f = 0.25 (medium)
- Alpha: α = 0.05
- Desired power: 0.80

### Results
**Required sample size:**
- **n = 45 per group**
- **Total N = 180**

### Breakdown
| Samples per group | Total N | Power |
|-------------------|---------|-------|
| 30                | 120     | 0.63  |
| 40                | 160     | 0.75  |
| **45**            | **180** | **0.80** ✅ |
| 50                | 200     | 0.85  |
| 60                | 240     | 0.92  |

### Post-Hoc Considerations

**Important:** ANOVA tells you groups differ, not which groups.

For pairwise comparisons (Tukey HSD):
- Each comparison needs adequate power
- With 4 groups: 6 pairwise comparisons
- Recommend n = 50 per group (Total N = 200)

### Multiple Comparisons Correction
If using Bonferroni correction (6 tests):
- Adjusted α = 0.05 / 6 = 0.0083
- Requires larger sample: **n = 60 per group**

### Recommendations
1. **Omnibus test only:** n = 45 per group (N = 180)
2. **With post-hoc tests:** n = 50 per group (N = 200)
3. **With Bonferroni:** n = 60 per group (N = 240)

### For Your Dissertation
Chapter 4 (Methodology):
> "A priori power analysis for one-way ANOVA with four
> groups indicated that 50 participants per group (N = 200)
> would provide 85% power to detect medium effect sizes
> (f = 0.25) at α = 0.05, with adequate power for subsequent
> post-hoc pairwise comparisons using Tukey HSD."
```

## Effect Size Guidelines

### Cohen's d (Two groups)
- **Small:** d = 0.2
- **Medium:** d = 0.5
- **Large:** d = 0.8

### Cohen's f (ANOVA)
- **Small:** f = 0.10
- **Medium:** f = 0.25
- **Large:** f = 0.40

### Correlation (r)
- **Small:** r = 0.10
- **Medium:** r = 0.30
- **Large:** r = 0.50

### Proportion Difference (h)
- **Small:** h = 0.20
- **Medium:** h = 0.50
- **Large:** h = 0.80

## Common Scenarios

### Scenario 1: Pilot Study
```
@power-analysis

I'm running a pilot with n=20. What can I detect?
```

**Answer:** With n=20 per group, you can only reliably detect very large effects (d > 1.0). Pilots are for feasibility, not hypothesis testing.

### Scenario 2: Constrained Resources
```
@power-analysis

I can only collect n=30 per group. Is this enough?
```

**Analysis:**
- d = 0.5, power = 0.47 (underpowered)
- d = 0.8, power = 0.80 (adequate for large effects)

**Recommendation:** Either increase n or adjust expectations to detect only large effects.

### Scenario 3: Non-Inferiority
```
@power-analysis

I want to show my method is "not worse" than baseline.
Margin: d = -0.3 (non-inferiority margin)
```

**Special case:** Requires different calculation (TOST: Two One-Sided Tests). Typically needs 30-40% larger sample than superiority test.

## Validation Checks

The skill validates:
- ✅ Effect size is reasonable (not impossibly large)
- ✅ Power between 0.05 and 0.99
- ✅ Alpha is standard (0.05, 0.01, 0.10)
- ✅ Sample size is feasible (not millions)
- ✅ Allocation ratio makes sense (1:1, 1:2, etc.)

## Advanced Features

### Sensitivity Analysis
Shows power across range of effect sizes:
```
n = 64 per group:
- d = 0.3 → Power = 0.35
- d = 0.5 → Power = 0.80
- d = 0.7 → Power = 0.95
```

### Sample Size Curves
Plots required n vs effect size vs power.

### Cost-Benefit Analysis
If data collection costs provided:
- Cost per sample: $X
- Total cost: N × $X
- Budget feasibility check

## Integration with Dissertation

### Chapter 4: Methodology

#### Required Elements
1. **A priori power analysis** (before data collection)
2. Justify sample size choice
3. State effect size assumptions
4. Report power achieved
5. Cite software used (G*Power, R, Python)

#### Template
```markdown
### 4.3 Sample Size Determination

An a priori power analysis was conducted using G*Power 3.1
(Faul et al., 2007) to determine the required sample size.
Based on previous research in XAI evaluation (cite), we
anticipated a medium effect size (Cohen's d = 0.5). To
achieve 80% power with a two-tailed test at α = 0.05,
a minimum of 64 verification pairs per condition was
required (total N = 128).

To ensure adequate power for secondary analyses and account
for potential data quality issues, we collected 200
verification pairs per dataset (VGGFace2 and LFW), providing
94% power to detect medium effects.
```

### Chapter 7: Discussion - Limitations

```markdown
### 7.4 Statistical Limitations

While our sample size (N = 200 per dataset) provided
excellent power (>0.90) for detecting medium to large
effects, we had insufficient power (0.29) to detect
small effects (d < 0.4). Thus, we cannot rule out
subtle differences between methods that may be
practically meaningful in some contexts.
```

## Software Options

### G*Power (Recommended)
- Free, GUI-based
- Gold standard for dissertations
- Comprehensive test coverage
- **Cite:** Faul, F., Erdfelder, E., Lang, A. G., & Buchner, A. (2007). G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behavior Research Methods*, 39(2), 175-191.

### R (pwr package)
```r
library(pwr)
pwr.t.test(d = 0.5, sig.level = 0.05, power = 0.80)
```

### Python (statsmodels)
```python
from statsmodels.stats.power import TTestIndPower
analysis = TTestIndPower()
n = analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.80)
```

## Common Mistakes Fixed

### Mistake 1: Post-Hoc Power Analysis
❌ **Wrong:** "We found p = 0.06 with n = 30. Post-hoc power was 0.45."

✅ **Right:** A priori power analysis before data collection. Post-hoc power is controversial and not informative.

### Mistake 2: No Effect Size Justification
❌ **Wrong:** "We used n = 100 because that seemed reasonable."

✅ **Right:** "Based on Smith et al. (2020) reporting d = 0.4, we powered our study to detect d = 0.5."

### Mistake 3: Ignoring Multiple Comparisons
❌ **Wrong:** Power for 4 groups, but 6 pairwise tests.

✅ **Right:** Account for post-hoc tests in sample size calculation.

### Mistake 4: Unrealistic Effect Sizes
❌ **Wrong:** "We expect d = 2.0" (almost never true in real research)

✅ **Right:** "Based on literature, we conservatively estimate d = 0.5."

## Time Savings

**Manual calculation:** 2-3 hours (learning software, running analyses, interpreting)
**Using @power-analysis:** 10-15 minutes
**Saved:** ~2 hours per study 🎉

## Best Practices

### 1. Always Do A Priori
Calculate power BEFORE data collection, not after.

### 2. Justify Effect Size
Base on:
- Prior literature
- Pilot data
- Smallest effect of practical interest

### 3. Report Fully
Include:
- Test type
- Effect size
- Alpha level
- Power
- Sample size
- Software used

### 4. Build in Safety Margin
If you need n = 64, collect n = 80 to account for:
- Data quality issues
- Outliers
- Attrition

### 5. Consider Secondary Analyses
Your primary analysis might need n = 64, but subgroup analyses need more.

## Field-Specific Notes

### Computer Science / Engineering
- Often large datasets (n > 1000)
- Effect sizes tend to be small-medium
- Multiple comparisons common
- Consider computational cost vs statistical power

### Psychology / Social Sciences
- Smaller samples typical (n = 30-100)
- Gold standard: 80% power
- Always report power analysis in methodology

### Medicine / Clinical
- Often aim for 90% power (higher stakes)
- May need 1:2 allocation (control:treatment)
- Regulatory requirements (FDA guidelines)

## Related Skills

- `@effect-size` - Calculate effect sizes from results
- `@hypothesis-test` - Design hypothesis tests
- `@experiment-design` - Overall experimental design
- `@results-interpreter` - Interpret statistical results

## Quality Checklist

Before finalizing sample size:
- [ ] A priori calculation (before data collection)
- [ ] Effect size justified from literature/pilot
- [ ] Power ≥ 0.80 (or justify lower)
- [ ] Alpha = 0.05 (or justify different)
- [ ] Multiple comparisons considered
- [ ] Sample size feasible with resources
- [ ] Safety margin included
- [ ] Software cited

## Example Workflow

```
1. Review literature for expected effect sizes
2. Use @power-analysis to calculate required n
3. Check resource feasibility (budget, time, data availability)
4. If infeasible, adjust design or expectations
5. Document in Chapter 4 (Methodology)
6. Cite G*Power or equivalent
7. Include in IRB/ethics application (if applicable)
```

## Citation

When using power analysis in your dissertation, cite the appropriate software:

**G*Power:**
> Faul, F., Erdfelder, E., Lang, A. G., & Buchner, A. (2007). G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behavior Research Methods*, 39(2), 175-191.

**R pwr package:**
> Champely, S. (2020). pwr: Basic functions for power analysis. R package version 1.3-0.

**Python statsmodels:**
> Seabold, S., & Perktold, J. (2010). statsmodels: Econometric and statistical modeling with python. *Proceedings of the 9th Python in Science Conference*, 57, 10-25080.

---

**Status:** Documented
**Complexity:** Medium-High
**Time to use:** 10-15 minutes
**Time saved:** ~2 hours
**Reusability:** Very High (any experimental study)
**Critical for:** Methodology chapter, IRB applications, grant proposals
