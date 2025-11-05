# @figure-table - Create Publication-Quality Figures and Tables

Design professional figures and tables for your dissertation with proper formatting and captions.

## Skill Type
**Category:** Data Visualization / Writing
**Tier:** Specialized (Tier 2)
**Reusability:** Very High - every dissertation needs figures and tables

## What This Skill Does

1. Designs effective data visualizations
2. Creates figure captions and table titles
3. Ensures APA/academic formatting compliance
4. Selects appropriate chart types
5. Provides color schemes for accessibility
6. Generates figure/table numbering and references

## Invocation

```
@figure-table [data-type] [purpose]
```

## Figure vs Table Decision Guide

### Use a FIGURE when:
- Showing **trends** over time
- Displaying **distributions** (histograms, box plots)
- **Spatial relationships** (heatmaps, scatter plots)
- **Comparisons** are easier to see visually
- **Complex patterns** that are hard to describe in words

### Use a TABLE when:
- **Exact values** are important
- **Multiple metrics** per condition
- **Reference lookup** (reader may search for specific values)
- **Small datasets** (< 20 data points)
- **Statistical results** (t-tests, ANOVA, etc.)

## Common Figure Types

### 1. Bar Chart
**Use:** Compare categories (e.g., method performance)

### 2. Line Chart
**Use:** Show trends over time or continuous variable

### 3. Scatter Plot
**Use:** Show relationship between two continuous variables

### 4. Box Plot / Violin Plot
**Use:** Show distributions and outliers

### 5. Heatmap
**Use:** Show matrix data (correlations, confusion matrices)

### 6. Error Bars / Confidence Intervals
**Use:** Show uncertainty in measurements

## Input Format

### Simple Data Visualization
```
@figure-table

Create bar chart:
BiometricGradCAM: M = 0.87, SD = 0.04
GradCAM: M = 0.72, SD = 0.06
LIME: M = 0.68, SD = 0.07
IntegratedGrad: M = 0.75, SD = 0.05

Y-axis: Localization Accuracy (IoU)
X-axis: XAI Method
Include error bars (95% CI)
```

### Complex Visualization
```
@figure-table

Create 2×2 subplot figure:
Top-left: Bar chart (accuracy by method)
Top-right: Box plot (distributions)
Bottom-left: Scatter plot (consistency vs accuracy)
Bottom-right: Heatmap (correlation matrix)
```

### From Research Question
```
@figure-table

RQ: Does BiometricGradCAM improve across both datasets?

Create grouped bar chart:
- X-axis: Dataset (VGGFace2, LFW)
- Y-axis: Accuracy
- Groups: BiometricGradCAM, GradCAM
- Show that BiometricGradCAM better on both datasets
```

## Output Examples

### Example 1: Bar Chart with Error Bars

**Input:**
```
@figure-table

Bar chart comparing 4 XAI methods on localization accuracy:

BiometricGradCAM: M = 0.87, SE = 0.003, 95% CI [0.86, 0.88]
IntegratedGrad: M = 0.75, SE = 0.004, 95% CI [0.74, 0.76]
GradCAM: M = 0.72, SE = 0.004, 95% CI [0.71, 0.73]
LIME: M = 0.68, SE = 0.005, 95% CI [0.67, 0.69]

Include error bars (95% CI).
```

**Output:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['BiometricGradCAM', 'IntegratedGrad', 'GradCAM', 'LIME']
means = [0.87, 0.75, 0.72, 0.68]
ci_lower = [0.86, 0.74, 0.71, 0.67]
ci_upper = [0.88, 0.76, 0.73, 0.69]
errors = [(u - l) / 2 for l, u in zip(ci_lower, ci_upper)]

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Bar chart
x_pos = np.arange(len(methods))
bars = ax.bar(x_pos, means, yerr=errors, capsize=5,
               color=['#2E7D32', '#1976D2', '#D32F2F', '#F57C00'],
               alpha=0.8, edgecolor='black', linewidth=1.2)

# Formatting
ax.set_xlabel('XAI Method', fontsize=14, fontweight='bold')
ax.set_ylabel('Localization Accuracy (IoU)', fontsize=14, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(methods, rotation=15, ha='right')
ax.set_ylim(0, 1.0)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Significance indicators (optional)
# Add asterisks above bars for significant differences
ax.text(0, 0.89, '***', ha='center', fontsize=16)

plt.tight_layout()
plt.savefig('figure_localization_accuracy.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_localization_accuracy.pdf', bbox_inches='tight')
plt.show()
```

**Caption:**
```markdown
**Figure 1.** Localization accuracy (Intersection over Union) by XAI method.
Error bars represent 95% confidence intervals. BiometricGradCAM significantly
outperformed all baseline methods (***p < .001, Tukey HSD). n = 200 verification
pairs per method. Higher values indicate more accurate spatial localization.
```

**LaTeX Integration:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/figure_localization_accuracy.pdf}
\caption{Localization accuracy (Intersection over Union) by XAI method.
Error bars represent 95\% confidence intervals. BiometricGradCAM significantly
outperformed all baseline methods (***$p < .001$, Tukey HSD). $n = 200$
verification pairs per method. Higher values indicate more accurate spatial
localization.}
\label{fig:localization_accuracy}
\end{figure}
```

---

### Example 2: Box Plot (Distributions)

**Input:**
```
@figure-table

Create box plot showing distribution of localization accuracy scores for each method.
Show median, quartiles, outliers.
```

**Output:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Simulated data (replace with actual data)
np.random.seed(42)
biometric_data = np.random.normal(0.87, 0.04, 200)
integrated_data = np.random.normal(0.75, 0.05, 200)
gradcam_data = np.random.normal(0.72, 0.06, 200)
lime_data = np.random.normal(0.68, 0.07, 200)

data = [biometric_data, integrated_data, gradcam_data, lime_data]
labels = ['BiometricGradCAM', 'IntegratedGrad', 'GradCAM', 'LIME']

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Box plot
bp = ax.boxplot(data, labels=labels, patch_artist=True,
                notch=True, showmeans=True,
                boxprops=dict(facecolor='lightblue', alpha=0.7),
                medianprops=dict(color='red', linewidth=2),
                meanprops=dict(marker='D', markerfacecolor='green', markersize=8))

# Formatting
ax.set_ylabel('Localization Accuracy (IoU)', fontsize=14, fontweight='bold')
ax.set_xlabel('XAI Method', fontsize=14, fontweight='bold')
ax.set_ylim(0.5, 1.0)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add horizontal reference line at baseline
ax.axhline(y=0.72, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='GradCAM median')

plt.tight_layout()
plt.savefig('figure_distributions.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_distributions.pdf', bbox_inches='tight')
plt.show()
```

**Caption:**
```markdown
**Figure 2.** Distribution of localization accuracy scores by XAI method.
Box plots show median (red line), interquartile range (box), and outliers (circles).
Green diamonds indicate means. Notches represent 95% confidence intervals around
the median. BiometricGradCAM shows highest median and narrowest distribution
(smallest variance), indicating consistently superior performance. n = 200 per method.
```

---

### Example 3: Scatter Plot (Correlation)

**Input:**
```
@figure-table

Scatter plot:
X-axis: Explanation consistency (0-1)
Y-axis: Verification accuracy (0-1)

Show positive correlation, fit regression line.
Pearson r = 0.67, p < 0.001
```

**Output:**

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Simulated data (replace with actual)
np.random.seed(42)
n = 200
consistency = np.random.beta(8, 2, n)  # Skewed towards higher values
accuracy = 0.5 + 0.4 * consistency + np.random.normal(0, 0.05, n)
accuracy = np.clip(accuracy, 0, 1)

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(consistency, accuracy)

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Scatter plot
ax.scatter(consistency, accuracy, alpha=0.6, s=50, color='steelblue', edgecolors='black', linewidth=0.5)

# Regression line
x_line = np.array([consistency.min(), consistency.max()])
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, color='red', linewidth=2, label=f'r = {r_value:.2f}, p < .001')

# Formatting
ax.set_xlabel('Explanation Consistency (Cosine Similarity)', fontsize=14, fontweight='bold')
ax.set_ylabel('Verification Accuracy', fontsize=14, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(alpha=0.3, linestyle='--')
ax.legend(loc='lower right', fontsize=12, frameon=True, shadow=True)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('figure_correlation.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_correlation.pdf', bbox_inches='tight')
plt.show()
```

**Caption:**
```markdown
**Figure 3.** Relationship between explanation consistency and verification accuracy.
Each point represents one verification pair (n = 200). Red line shows linear
regression fit. Strong positive correlation (r = .67, p < .001, R² = .45) indicates
that consistent explanations for same-identity pairs are associated with higher
verification accuracy. Consistency measured via cosine similarity between attributions
for genuine pairs.
```

---

### Example 4: Grouped Bar Chart (Cross-Dataset)

**Input:**
```
@figure-table

Grouped bar chart showing BiometricGradCAM vs GradCAM across two datasets:

VGGFace2:
- BiometricGradCAM: 0.87 ± 0.04
- GradCAM: 0.72 ± 0.06

LFW:
- BiometricGradCAM: 0.83 ± 0.05
- GradCAM: 0.70 ± 0.07
```

**Output:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
datasets = ['VGGFace2', 'LFW']
biometric_means = [0.87, 0.83]
biometric_errors = [0.04, 0.05]
gradcam_means = [0.72, 0.70]
gradcam_errors = [0.06, 0.07]

# Bar positions
x = np.arange(len(datasets))
width = 0.35

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Grouped bars
bars1 = ax.bar(x - width/2, biometric_means, width, yerr=biometric_errors,
               label='BiometricGradCAM', capsize=5, color='#2E7D32', alpha=0.8, edgecolor='black')
bars2 = ax.bar(x + width/2, gradcam_means, width, yerr=gradcam_errors,
               label='GradCAM', capsize=5, color='#D32F2F', alpha=0.8, edgecolor='black')

# Formatting
ax.set_ylabel('Localization Accuracy (IoU)', fontsize=14, fontweight='bold')
ax.set_xlabel('Dataset', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(datasets)
ax.set_ylim(0, 1.0)
ax.legend(fontsize=12, frameon=True, shadow=True)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add significance indicators
ax.text(-width/2, 0.90, '***', ha='center', fontsize=16)
ax.text(1-width/2, 0.86, '***', ha='center', fontsize=16)

plt.tight_layout()
plt.savefig('figure_cross_dataset.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_cross_dataset.pdf', bbox_inches='tight')
plt.show()
```

**Caption:**
```markdown
**Figure 4.** Cross-dataset validation: BiometricGradCAM vs GradCAM on VGGFace2
and LFW datasets. Error bars represent standard deviations. BiometricGradCAM
significantly outperformed GradCAM on both datasets (***p < .001, independent t-tests).
Effect sizes remained large (VGGFace2: d = 2.94, LFW: d = 2.10), demonstrating
robust generalization. n = 200 verification pairs per method per dataset.
```

---

### Example 5: Heatmap (Correlation Matrix)

**Input:**
```
@figure-table

Correlation matrix heatmap:

Variables: Accuracy, Consistency, Faithfulness, VerifAccuracy

Correlations:
Accuracy - Consistency: 0.67
Accuracy - Faithfulness: 0.52
Accuracy - VerifAccuracy: 0.71
Consistency - Faithfulness: 0.48
Consistency - VerifAccuracy: 0.65
Faithfulness - VerifAccuracy: 0.59
```

**Output:**

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Correlation matrix
variables = ['Localization\nAccuracy', 'Consistency', 'Faithfulness', 'Verification\nAccuracy']
corr_matrix = np.array([
    [1.00, 0.67, 0.52, 0.71],
    [0.67, 1.00, 0.48, 0.65],
    [0.52, 0.48, 1.00, 0.59],
    [0.71, 0.65, 0.59, 1.00]
])

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Heatmap
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            vmin=0, vmax=1, center=0.5,
            xticklabels=variables, yticklabels=variables,
            square=True, linewidths=1, cbar_kws={'label': 'Pearson r'},
            ax=ax)

# Formatting
ax.set_title('Intercorrelations Between Explanation Quality Metrics',
             fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('figure_correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.savefig('figure_correlation_matrix.pdf', bbox_inches='tight')
plt.show()
```

**Caption:**
```markdown
**Figure 5.** Heatmap of intercorrelations between explanation quality metrics
and verification accuracy. Color intensity represents correlation strength
(red = strong positive). All correlations significant at p < .001 (n = 200).
Strongest correlations observed between localization accuracy and verification
accuracy (r = .71) and between consistency and localization accuracy (r = .67),
supporting theoretical predictions that explanation quality relates to model performance.
```

---

## Table Design Best Practices

### 1. Descriptive Statistics Table

```markdown
**Table 1**
*Descriptive Statistics for Localization Accuracy by XAI Method*

| XAI Method         | n   | M    | SD   | Min  | Max  | 95% CI        |
|:-------------------|----:|-----:|-----:|-----:|-----:|:--------------|
| BiometricGradCAM   | 200 | 0.87 | 0.04 | 0.79 | 0.95 | [0.86, 0.88]  |
| IntegratedGrad     | 200 | 0.75 | 0.05 | 0.65 | 0.85 | [0.74, 0.76]  |
| GradCAM            | 200 | 0.72 | 0.06 | 0.60 | 0.84 | [0.71, 0.73]  |
| LIME               | 200 | 0.68 | 0.07 | 0.52 | 0.82 | [0.67, 0.69]  |

*Note.* n = sample size; M = mean; SD = standard deviation; CI = confidence interval.
Localization accuracy measured as Intersection over Union (IoU). Higher values
indicate better localization.
```

### 2. Statistical Results Table

```markdown
**Table 2**
*Pairwise Comparisons: BiometricGradCAM vs Baseline XAI Methods*

| Comparison                      | t      | df  | p      | Cohen's d | 95% CI for d  |
|:--------------------------------|-------:|----:|:-------|----------:|:--------------|
| BiometricGradCAM vs GradCAM     | 14.2   | 398 | <.001  | 2.94      | [2.62, 3.26]  |
| BiometricGradCAM vs LIME        | 18.3   | 398 | <.001  | 3.54      | [3.18, 3.90]  |
| BiometricGradCAM vs IntegratedGrad | 12.1 | 398 | <.001  | 2.61      | [2.30, 2.92]  |

*Note.* All tests were independent samples t-tests (one-tailed, α = .05).
Effect sizes represent standardized mean differences. All comparisons favor
BiometricGradCAM.
```

---

## Figure/Table Numbering and Referencing

### In LaTeX
```latex
% Figure
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/my_figure.pdf}
  \caption{Caption text here.}
  \label{fig:my_figure}
\end{figure}

% Reference in text
As shown in Figure~\ref{fig:my_figure}, BiometricGradCAM...

% Table
\begin{table}[htbp]
  \caption{Table caption here.}
  \label{tab:my_table}
  % Table content
\end{table}

% Reference in text
Table~\ref{tab:my_table} presents descriptive statistics...
```

### In Markdown
```markdown
**Figure 1.** Caption text here.

In the text:
As shown in Figure 1, BiometricGradCAM...

**Table 1**
*Table title here*

In the text:
Table 1 presents descriptive statistics...
```

---

## Color Schemes (Accessibility)

### Colorblind-Friendly Palettes

**Palette 1 (4 colors):**
```python
colors = ['#0072B2', '#D55E00', '#009E73', '#F0E442']  # Blue, Orange, Green, Yellow
```

**Palette 2 (Grayscale-safe):**
```python
colors = ['#1B9E77', '#D95F02', '#7570B3', '#E7298A']  # Teal, Orange, Purple, Pink
```

**Use High Contrast:**
- Avoid red-green combinations (8% of men are colorblind)
- Use patterns/textures in addition to colors
- Test figures in grayscale

---

## Common Mistakes Fixed

### ❌ Mistake 1: Unclear Axis Labels
"Accuracy" (which accuracy?)

✅ Clear: "Localization Accuracy (IoU)"

### ❌ Mistake 2: Missing Error Bars
Bar chart with no indication of uncertainty.

✅ Add error bars (CI or SE)

### ❌ Mistake 3: Caption Too Short
"Results for four methods."

✅ Detailed: "Localization accuracy (IoU) by XAI method. Error bars represent 95% CI. n = 200 per method."

### ❌ Mistake 4: No Figure Numbers
Figures not numbered sequentially.

✅ Number all: Figure 1, Figure 2, etc.

### ❌ Mistake 5: Low Resolution
Saving at 72 DPI (screen resolution).

✅ Save at 300 DPI minimum for print.

---

## Time Savings

**Manual figure/table creation:** 1-2 hours per figure (design, coding, formatting)
**Using @figure-table:** 15-30 minutes (template, customize)
**Saved:** ~1.5 hours per figure 🎉

**If 15-20 figures in dissertation:** 22.5-30 hours saved total

## Best Practices

### Figures
1. **High resolution:** 300 DPI minimum
2. **Vector formats:** PDF for LaTeX (scalable)
3. **Clear labels:** Large fonts (≥12pt)
4. **Error bars:** Always show uncertainty
5. **Colorblind-safe:** Use accessible palettes

### Tables
1. **Alignment:** Left-align text, right-align numbers
2. **Consistent decimals:** Same places throughout
3. **Notes section:** Explain abbreviations
4. **Minimalist design:** No excessive lines/colors
5. **Self-contained:** Understandable without reading text

### Captions
1. **Placement:** Above tables, below figures (APA)
2. **Descriptive:** What, how, n, key takeaway
3. **Abbreviations:** Define all (or reference note)
4. **Statistical info:** Include p-values, effect sizes

## Integration with Dissertation

### Chapter 6 (Results)
- **Figure 6.1:** Bar chart (primary result)
- **Figure 6.2:** Box plots (distributions)
- **Figure 6.3:** Scatter plot (correlation)
- **Figure 6.4:** Grouped bar (cross-dataset)
- **Table 6.1:** Descriptive statistics
- **Table 6.2:** Statistical test results

### Chapter 4 (Methodology)
- **Figure 4.1:** Experimental procedure flowchart
- **Table 4.1:** Sample characteristics

### Chapter 2 (Literature Review)
- **Table 2.1:** Summary of reviewed studies

## Related Skills

- `@latex-table` - LaTeX-specific table generation
- `@results-interpreter` - Interpret data for figures/tables
- `@methodology-writer` - Design figures for methodology
- `@experiment-design` - Plan what figures/tables needed

---

**Status:** Documented
**Complexity:** Medium-High
**Time to use:** 15-30 minutes per figure/table
**Time saved:** ~1.5 hours per figure
**Reusability:** Very High (every dissertation needs visualizations)
**Critical for:** Results presentation, data communication, defense slides
