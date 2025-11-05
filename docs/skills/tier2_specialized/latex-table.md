# @latex-table - Generate Publication-Quality LaTeX Tables

Generate professional, publication-ready LaTeX tables for your dissertation.

## Skill Type
**Category:** Writing / LaTeX Formatting
**Tier:** Specialized (Tier 2)
**Reusability:** Very High - every dissertation needs professional tables

## What This Skill Does

1. Converts data to LaTeX table format
2. Applies professional formatting (booktabs)
3. Handles complex tables (multi-row, multi-column)
4. Generates captions and labels
5. Ensures APA/academic style compliance
6. Creates camera-ready tables for publication

## Invocation

```
@latex-table [data] [table-type]
```

## LaTeX Table Types

### 1. Simple Descriptive Statistics Table
Mean, SD, n for multiple groups

### 2. Results Table (Statistical Tests)
Test statistics, p-values, effect sizes, CIs

### 3. Comparison Table (Methods/Studies)
Compare multiple methods or prior studies

### 4. Correlation Matrix
Pairwise correlations between variables

### 5. Confusion Matrix / Performance Metrics
Classification accuracy, precision, recall, F1

### 6. ANOVA Table
Source, SS, df, MS, F, p

## Best Practices

### Use `booktabs` Package
```latex
\usepackage{booktabs}
```
- `\toprule` - Top of table
- `\midrule` - Between header and data
- `\bottomrule` - Bottom of table
- `\cmidrule` - Partial horizontal lines

### Number Formatting
- **Align decimals** using `siunitx` package
- **Consistency:** Same decimal places throughout
- **p-values:** 3 decimals (p = .042), or p < .001

### Captions
- **Above table** (APA style)
- **Descriptive:** Explain what table shows
- **Note section:** Asterisks, abbreviations, explanations

## Input Format

### From Descriptive Statistics
```
@latex-table

Descriptive statistics:
Group 1 (BiometricGradCAM): M = 0.87, SD = 0.04, n = 200
Group 2 (GradCAM): M = 0.72, SD = 0.06, n = 200
Group 3 (LIME): M = 0.68, SD = 0.07, n = 200
Group 4 (IntegratedGrad): M = 0.75, SD = 0.05, n = 200

DV: Localization Accuracy (IoU)
```

### From Statistical Test Results
```
@latex-table

ANOVA results:
Method: F(3, 396) = 23.5, p < 0.001, η² = 0.15
Post-hoc comparisons (Tukey HSD) with Cohen's d

Create results table with means, SDs, and pairwise comparisons.
```

### From JSON/CSV Data
```json
{
  "table_type": "method_comparison",
  "rows": [
    {"Method": "GradCAM", "Accuracy": 0.72, "Consistency": 0.65, "Time_ms": 35},
    {"Method": "LIME", "Accuracy": 0.68, "Consistency": 0.58, "Time_ms": 120},
    {"Method": "IntegratedGrad", "Accuracy": 0.75, "Consistency": 0.71, "Time_ms": 250},
    {"Method": "BiometricGradCAM", "Accuracy": 0.87, "Consistency": 0.92, "Time_ms": 42}
  ]
}
```

## Output Examples

### Example 1: Descriptive Statistics Table

**Input:**
```
@latex-table

Descriptive statistics for localization accuracy by XAI method:

BiometricGradCAM: M = 0.87, SD = 0.04, n = 200, Min = 0.79, Max = 0.95
GradCAM: M = 0.72, SD = 0.06, n = 200, Min = 0.60, Max = 0.84
LIME: M = 0.68, SD = 0.07, n = 200, Min = 0.52, Max = 0.82
IntegratedGrad: M = 0.75, SD = 0.05, n = 200, Min = 0.65, Max = 0.85
```

**Output:**

```latex
\begin{table}[htbp]
\centering
\caption{Descriptive Statistics for Localization Accuracy by XAI Method}
\label{tab:descriptive_stats}
\begin{tabular}{lcccccc}
\toprule
\textbf{XAI Method} & \textbf{$n$} & \textbf{$M$} & \textbf{$SD$} & \textbf{Min} & \textbf{Max} & \textbf{95\% CI} \\
\midrule
BiometricGradCAM    & 200 & 0.87 & 0.04 & 0.79 & 0.95 & [0.86, 0.88] \\
IntegratedGradients & 200 & 0.75 & 0.05 & 0.65 & 0.85 & [0.74, 0.76] \\
GradCAM             & 200 & 0.72 & 0.06 & 0.60 & 0.84 & [0.71, 0.73] \\
LIME                & 200 & 0.68 & 0.07 & 0.52 & 0.82 & [0.67, 0.69] \\
\bottomrule
\end{tabular}

\vspace{0.5em}
\begin{tablenotes}[flushleft]
\small
\item \textit{Note.} $n$ = sample size; $M$ = mean; $SD$ = standard deviation;
CI = confidence interval. Localization accuracy measured as Intersection over
Union (IoU) between generated attributions and ground-truth facial landmark regions.
Higher values indicate better localization.
\end{tablenotes}
\end{table}
```

**Rendered Appearance:**
```
───────────────────────────────────────────────────────────────────
Table 1
Descriptive Statistics for Localization Accuracy by XAI Method

XAI Method           n    M     SD    Min   Max   95% CI
───────────────────────────────────────────────────────────────────
BiometricGradCAM    200  0.87  0.04  0.79  0.95  [0.86, 0.88]
IntegratedGradients 200  0.75  0.05  0.65  0.85  [0.74, 0.76]
GradCAM             200  0.72  0.06  0.60  0.84  [0.71, 0.73]
LIME                200  0.68  0.07  0.52  0.82  [0.67, 0.69]
───────────────────────────────────────────────────────────────────
Note. n = sample size; M = mean; SD = standard deviation...
```

---

### Example 2: Statistical Results Table (t-tests)

**Input:**
```
@latex-table

Pairwise t-test comparisons (BiometricGradCAM vs baselines):

BiometricGradCAM vs GradCAM:
  t(398) = 14.2, p < 0.001, d = 2.94, 95% CI [2.62, 3.26]

BiometricGradCAM vs LIME:
  t(398) = 18.3, p < 0.001, d = 3.54, 95% CI [3.18, 3.90]

BiometricGradCAM vs IntegratedGrad:
  t(398) = 12.1, p < 0.001, d = 2.61, 95% CI [2.30, 2.92]
```

**Output:**

```latex
\begin{table}[htbp]
\centering
\caption{Pairwise Comparisons: BiometricGradCAM vs Baseline XAI Methods}
\label{tab:pairwise_comparisons}
\begin{tabular}{lccccc}
\toprule
\textbf{Comparison} & \textbf{$t$} & \textbf{$df$} & \textbf{$p$} & \textbf{Cohen's $d$} & \textbf{95\% CI for $d$} \\
\midrule
BiometricGradCAM vs GradCAM         & 14.2 & 398 & $<.001$ & 2.94 & [2.62, 3.26] \\
BiometricGradCAM vs LIME            & 18.3 & 398 & $<.001$ & 3.54 & [3.18, 3.90] \\
BiometricGradCAM vs IntegratedGrad  & 12.1 & 398 & $<.001$ & 2.61 & [2.30, 2.92] \\
\bottomrule
\end{tabular}

\vspace{0.5em}
\begin{tablenotes}[flushleft]
\small
\item \textit{Note.} All tests were independent samples t-tests (one-tailed) with
$\alpha = .05$. Effect sizes (Cohen's $d$) represent standardized mean differences.
All comparisons favor BiometricGradCAM (higher localization accuracy).
CI = confidence interval.
\end{tablenotes}
\end{table}
```

---

### Example 3: Method Comparison Table

**Input:**
```
@latex-table

Method comparison across multiple metrics:

Method            | Accuracy | Consistency | Faithfulness | Time (ms)
BiometricGradCAM  | 0.87     | 0.92        | 0.88         | 42
GradCAM           | 0.72     | 0.65        | 0.70         | 35
LIME              | 0.68     | 0.58        | 0.65         | 120
IntegratedGrad    | 0.75     | 0.71        | 0.73         | 250

Best values should be in bold.
```

**Output:**

```latex
\begin{table}[htbp]
\centering
\caption{Performance Comparison of XAI Methods Across Multiple Metrics}
\label{tab:method_comparison}
\begin{tabular}{lcccc}
\toprule
\textbf{XAI Method} & \textbf{Localization} & \textbf{Consistency} & \textbf{Faithfulness} & \textbf{Time (ms)} \\
                    & \textbf{Accuracy}     &                     &                       &                    \\
\midrule
BiometricGradCAM    & \textbf{0.87} & \textbf{0.92} & \textbf{0.88} & 42         \\
IntegratedGradients & 0.75          & 0.71          & 0.73          & 250        \\
GradCAM             & 0.72          & 0.65          & 0.70          & \textbf{35} \\
LIME                & 0.68          & 0.58          & 0.65          & 120        \\
\bottomrule
\end{tabular}

\vspace{0.5em}
\begin{tablenotes}[flushleft]
\small
\item \textit{Note.} All metrics on 0-1 scale (higher = better), except Time
(lower = faster). \textbf{Bold} indicates best performance per metric. Localization
accuracy measured via IoU; consistency via cosine similarity; faithfulness via
model parameter randomization test. Time averaged over 200 verification pairs on
NVIDIA A100 GPU.
\end{tablenotes}
\end{table}
```

---

### Example 4: ANOVA Summary Table

**Input:**
```
@latex-table

One-way ANOVA results:

Source        | SS      | df  | MS     | F     | p       | η²
Between groups| 2.456   | 3   | 0.819  | 23.5  | <0.001  | 0.15
Within groups | 13.824  | 396 | 0.035  |       |         |
Total         | 16.280  | 399 |        |       |         |
```

**Output:**

```latex
\begin{table}[htbp]
\centering
\caption{One-Way ANOVA: Effect of XAI Method on Localization Accuracy}
\label{tab:anova_results}
\begin{tabular}{lccccc}
\toprule
\textbf{Source} & \textbf{$SS$} & \textbf{$df$} & \textbf{$MS$} & \textbf{$F$} & \textbf{$p$} \\
\midrule
Between Groups (Method) & 2.456  & 3   & 0.819 & 23.5 & $<.001$ \\
Within Groups (Error)   & 13.824 & 396 & 0.035 &      &         \\
\midrule
Total                   & 16.280 & 399 &       &      &         \\
\bottomrule
\end{tabular}

\vspace{0.5em}
\begin{tablenotes}[flushleft]
\small
\item \textit{Note.} $SS$ = sum of squares; $df$ = degrees of freedom;
$MS$ = mean square; $F$ = F-statistic. Effect size $\eta^2 = .15$ (large effect).
\end{tablenotes}
\end{table}
```

---

### Example 5: Correlation Matrix

**Input:**
```
@latex-table

Correlation matrix:

Variables: Accuracy, Consistency, Faithfulness, VerificationAccuracy

Correlations (with p-values):
Accuracy - Consistency: r = 0.67, p < 0.001
Accuracy - Faithfulness: r = 0.52, p < 0.001
Accuracy - VerificationAccuracy: r = 0.71, p < 0.001
Consistency - Faithfulness: r = 0.48, p < 0.001
Consistency - VerificationAccuracy: r = 0.65, p < 0.001
Faithfulness - VerificationAccuracy: r = 0.59, p < 0.001
```

**Output:**

```latex
\begin{table}[htbp]
\centering
\caption{Intercorrelations Between Explanation Quality Metrics and Verification Accuracy}
\label{tab:correlation_matrix}
\begin{tabular}{lcccc}
\toprule
\textbf{Variable} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} \\
\midrule
1. Localization Accuracy    & ---     &         &         &         \\
2. Consistency              & .67***  & ---     &         &         \\
3. Faithfulness             & .52***  & .48***  & ---     &         \\
4. Verification Accuracy    & .71***  & .65***  & .59***  & ---     \\
\bottomrule
\end{tabular}

\vspace{0.5em}
\begin{tablenotes}[flushleft]
\small
\item \textit{Note.} $n = 200$ verification pairs. All correlations are Pearson
product-moment correlations.
\item ***$p < .001$
\end{tablenotes}
\end{table}
```

---

### Example 6: Literature Comparison Table

**Input:**
```
@latex-table

Compare this study to prior work:

Study                 | Method              | Dataset    | n   | Cohen's d
Smith et al. (2023)   | GradCAM vs LIME     | ImageNet  | 100 | 0.35
Jones et al. (2022)   | Saliency methods    | VGGFace2  | 150 | 0.62
Lee et al. (2021)     | Attribution compare | COCO      | 80  | 0.41
This study (2024)     | BiometricGradCAM    | VGGFace2  | 200 | 2.94
```

**Output:**

```latex
\begin{table}[htbp]
\centering
\caption{Comparison of Effect Sizes in XAI Method Evaluation Studies}
\label{tab:literature_comparison}
\begin{tabular}{llccc}
\toprule
\textbf{Study} & \textbf{Comparison} & \textbf{Dataset} & \textbf{$n$} & \textbf{Cohen's $d$} \\
\midrule
Smith et al. (2023)   & GradCAM vs LIME           & ImageNet  & 100 & 0.35 \\
Lee et al. (2021)     & Saliency methods          & COCO      & 80  & 0.41 \\
Jones et al. (2022)   & Attribution comparison    & VGGFace2  & 150 & 0.62 \\
\midrule
\textbf{Present study} & \textbf{BiometricGradCAM vs GradCAM} & \textbf{VGGFace2} & \textbf{200} & \textbf{2.94} \\
\bottomrule
\end{tabular}

\vspace{0.5em}
\begin{tablenotes}[flushleft]
\small
\item \textit{Note.} Effect sizes (Cohen's $d$) represent magnitude of performance
differences between XAI methods. Present study's effect size substantially exceeds
prior work (2.94 vs. median of 0.41), suggesting that task-specific XAI design
yields larger improvements than general-purpose method comparisons.
\end{tablenotes}
\end{table}
```

---

## Advanced Features

### Multi-Row and Multi-Column Headers

```latex
\begin{tabular}{lcccccc}
\toprule
                     & \multicolumn{3}{c}{\textbf{VGGFace2 Dataset}} & \multicolumn{3}{c}{\textbf{LFW Dataset}} \\
\cmidrule(lr){2-4} \cmidrule(lr){5-7}
\textbf{XAI Method}  & \textbf{$M$} & \textbf{$SD$} & \textbf{$d$} & \textbf{$M$} & \textbf{$SD$} & \textbf{$d$} \\
\midrule
BiometricGradCAM     & 0.87 & 0.04 & 2.94 & 0.83 & 0.05 & 2.10 \\
GradCAM              & 0.72 & 0.06 & ---  & 0.70 & 0.07 & ---  \\
\bottomrule
\end{tabular}
```

### Rotated Headers (for Space)

```latex
\usepackage{rotating}

\begin{tabular}{l*{6}{c}}
\toprule
\textbf{Method} & \rotatebox{90}{\textbf{Accuracy}} & \rotatebox{90}{\textbf{Consistency}} \\
\midrule
BiometricGradCAM & 0.87 & 0.92 \\
\bottomrule
\end{tabular}
```

### Aligned Decimals (siunitx Package)

```latex
\usepackage{siunitx}

\begin{tabular}{lS[table-format=1.2]S[table-format=1.2]}
\toprule
\textbf{Method} & {\textbf{Mean}} & {\textbf{SD}} \\
\midrule
BiometricGradCAM & 0.87 & 0.04 \\
GradCAM          & 0.72 & 0.06 \\
\bottomrule
\end{tabular}
```

### Color Highlighting (Best Values)

```latex
\usepackage{xcolor,colortbl}

\begin{tabular}{lcc}
\toprule
\textbf{Method} & \textbf{Accuracy} & \textbf{Time (ms)} \\
\midrule
BiometricGradCAM & \cellcolor{green!25}0.87 & 42 \\
GradCAM          & 0.72 & \cellcolor{green!25}35 \\
\bottomrule
\end{tabular}
```

---

## Common Mistakes Fixed

### ❌ Mistake 1: Vertical Lines
Don't use vertical lines in tables (not professional).

```latex
% BAD
\begin{tabular}{|l|c|c|}
\hline
```

✅ Use booktabs (no vertical lines):
```latex
% GOOD
\begin{tabular}{lcc}
\toprule
```

---

### ❌ Mistake 2: Inconsistent Decimal Places
```
0.87 vs 0.7 vs 0.721
```

✅ Consistent:
```
0.87 vs 0.70 vs 0.72
```

---

### ❌ Mistake 3: Too Many Significant Figures
```
Cohen's d = 2.9439281
```

✅ 2-3 significant figures:
```
Cohen's d = 2.94
```

---

### ❌ Mistake 4: Caption Below Table
APA style requires caption ABOVE table.

---

### ❌ Mistake 5: No Table Notes
Missing explanation of abbreviations, asterisks, etc.

✅ Always include notes section.

---

## Time Savings

**Manual LaTeX table creation:** 30-60 minutes per table (formatting, alignment, debugging)
**Using @latex-table:** 5-10 minutes (copy, paste, compile)
**Saved:** ~45 minutes per table 🎉

**If 10-15 tables in dissertation:** 7.5-11 hours saved total

## Best Practices

### 1. Use Booktabs
Professional, publication-ready appearance.

### 2. Align Decimals
Use `siunitx` package for automatic alignment.

### 3. Consistent Formatting
Same decimal places, same font size, same style throughout.

### 4. Clear Captions
Should be self-contained (reader understands without reading text).

### 5. Meaningful Notes
Explain abbreviations, asterisks, data sources.

## Required LaTeX Packages

Add to dissertation preamble:
```latex
\usepackage{booktabs}   % Professional tables
\usepackage{siunitx}    % Aligned decimals
\usepackage{threeparttable}  % Table notes
\usepackage{multirow}   % Multi-row cells
\usepackage{array}      % Enhanced columns
```

## Integration with Dissertation

### Chapter 6 (Results)
- **Table 6.1:** Descriptive statistics
- **Table 6.2:** ANOVA results
- **Table 6.3:** Post-hoc pairwise comparisons
- **Table 6.4:** Method comparison across metrics

### Chapter 2 (Literature Review)
- **Table 2.1:** Summary of reviewed studies
- **Table 2.2:** Comparison to prior work

### Appendices
- **Table A.1:** Full correlation matrix
- **Table A.2:** Additional analyses

## Related Skills

- `@results-interpreter` - Interpret results to populate tables
- `@effect-size` - Calculate values for results tables
- `@methodology-writer` - Design tables for methodology section
- `@figure-table` - Combine tables with figures

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 5-10 minutes per table
**Time saved:** ~45 minutes per table
**Reusability:** Very High (every dissertation needs tables)
**Critical for:** Results presentation, literature review, appendices
