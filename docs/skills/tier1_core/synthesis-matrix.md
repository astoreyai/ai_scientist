# @synthesis-matrix - Literature Synthesis Matrix

Create structured matrices to synthesize and compare research papers systematically.

## Skill Type
**Category:** Literature Review
**Tier:** Core (Tier 1)
**Reusability:** Very High - every systematic review needs this

## What This Skill Does

1. Organizes literature into comparison matrices
2. Extracts key information systematically
3. Identifies patterns and gaps across studies
4. Supports synthesis for Chapter 2
5. Generates publication-ready tables

## Invocation

```
@synthesis-matrix [papers] [dimensions]
```

## Matrix Types

### 1. Methods Comparison Matrix
Compare methodological approaches across studies.

**Dimensions:**
- Authors/Year
- Methods used
- Datasets
- Sample sizes
- Evaluation metrics
- Key findings

### 2. Results Synthesis Matrix
Compare quantitative results.

**Dimensions:**
- Study
- Performance metric 1 (e.g., accuracy)
- Performance metric 2 (e.g., F1-score)
- Dataset
- Notes/limitations

### 3. Theoretical Framework Matrix
Compare theoretical contributions.

**Dimensions:**
- Study
- Theoretical lens
- Key concepts
- Propositions/hypotheses
- Evidence provided

### 4. Gap Analysis Matrix
Identify what's missing in literature.

**Dimensions:**
- Topic area
- What's covered
- What's missing
- Opportunities
- References

## Input Format

### Simple List
```
@synthesis-matrix

Create a comparison matrix for these XAI papers:
1. Smith et al. 2023 - GradCAM for face recognition
2. Jones et al. 2022 - LIME for biometrics
3. Brown et al. 2021 - Integrated Gradients survey
```

### Structured Data
```json
{
  "papers": [
    {
      "authors": "Smith et al.",
      "year": 2023,
      "title": "GradCAM for Face Recognition",
      "method": "GradCAM",
      "dataset": "VGGFace2",
      "n": 200,
      "accuracy": 0.95,
      "limitation": "Small sample"
    },
    ...
  ],
  "dimensions": ["Method", "Dataset", "Sample Size", "Accuracy", "Limitations"]
}
```

### From Bibliography
```
@synthesis-matrix

Use my BibTeX file: chapter2_references.bib
Create methods comparison matrix
Focus on: XAI methods for face recognition (2020-2024)
```

## Output Examples

### Example 1: XAI Methods Comparison

**Input:**
```
@synthesis-matrix

Papers:
1. Selvaraju et al. 2017 - Grad-CAM
2. Ribeiro et al. 2016 - LIME
3. Sundararajan et al. 2017 - Integrated Gradients
4. Lundberg et al. 2017 - SHAP

Dimensions: Method type, Input type, Model-agnostic?, Computational cost, Interpretability level
```

**Output:**

```markdown
# XAI Methods Comparison Matrix

| Study | Method | Method Type | Model-Agnostic? | Computational Cost | Interpretability | Key Strength | Main Limitation |
|-------|--------|-------------|-----------------|--------------------|--------------------|--------------|-----------------|
| Selvaraju et al. (2017) | Grad-CAM | Gradient-based | No (CNNs only) | Low | Heatmap (visual) | Fast, visually intuitive | Requires gradients |
| Ribeiro et al. (2016) | LIME | Perturbation-based | Yes | High | Feature importance | Flexible, any model | Unstable, slow |
| Sundararajan et al. (2017) | Integrated Gradients | Attribution | No (differentiable) | Medium | Pixel importance | Theoretically grounded | Baseline selection |
| Lundberg & Lee (2017) | SHAP | Game-theoretic | Yes | Very High | Feature importance | Consistent, theory-backed | Computationally expensive |

**Summary:**
- **Fastest:** Grad-CAM (gradient-based)
- **Most flexible:** LIME, SHAP (model-agnostic)
- **Best theoretical foundation:** SHAP (Shapley values)
- **Most practical for CNNs:** Grad-CAM

**Gap identified:** No method combines speed (Grad-CAM) with model-agnosticism (LIME/SHAP).
```

### Example 2: Biometric XAI Performance

**Input:**
```
@synthesis-matrix

Topic: XAI for face recognition verification
Papers: 15 papers from my PRISMA review
Output: Performance comparison table
```

**Output:**

```markdown
# Biometric Face Recognition XAI - Performance Synthesis

| Study | XAI Method | Dataset | n (pairs) | Verification Accuracy | Localization Accuracy | Consistency Score | Human Agreement |
|-------|------------|---------|-----------|----------------------|----------------------|-------------------|-----------------|
| Zhang et al. (2023) | BiometricGrad | VGGFace2 | 500 | 0.99 | 0.87 | 0.92 | 0.78 |
| Smith et al. (2023) | GradCAM | LFW | 200 | 0.97 | 0.72 | 0.65 | 0.71 |
| Jones et al. (2022) | LIME | CFP-FP | 150 | 0.96 | 0.68 | 0.58 | 0.65 |
| Brown et al. (2022) | IG-Biometric | VGGFace2 | 300 | 0.98 | 0.81 | 0.84 | 0.75 |
| Lee et al. (2021) | SHAP-Face | LFW | 400 | 0.98 | 0.75 | 0.79 | 0.73 |

**Observations:**
- Verification accuracy uniformly high (0.96-0.99)
- Localization accuracy varies widely (0.68-0.87)
- BiometricGrad achieves highest consistency (0.92)
- Sample sizes range 150-500 (median: 300)

**Research Gap:**
Most studies use VGGFace2 or LFW. Need evaluation on:
- Cross-racial datasets (RFW)
- Age-varied datasets (AgeDB-30)
- Challenging conditions (CFP-FP)

**Implications for my work:**
- Target n ≥ 200 per dataset (current standard)
- Report both localization and consistency
- Cross-dataset validation essential
```

### Example 3: Methodology Synthesis

**Input:**
```
@synthesis-matrix

Create methodology comparison for my Chapter 2
Papers: All papers tagged "methodology" in Zotero (n=22)
Focus: Experimental design choices
```

**Output:**

```markdown
# Methodology Synthesis Matrix: XAI Evaluation Studies

| Study | Study Design | IV (Independent Variable) | DV (Dependent Variable) | Sample Size | Statistical Test | Effect Size Reported? | Limitations Noted |
|-------|--------------|---------------------------|-------------------------|-------------|------------------|-----------------------|-------------------|
| Smith et al. (2023) | Between-subjects | XAI method (4 levels) | Localization accuracy | n=200/method | ANOVA + Tukey | Yes (η²=0.42) | Small sample |
| Jones et al. (2022) | Within-subjects | XAI method (3 levels) | User trust (Likert) | n=50 users | Friedman test | No | No power analysis |
| Brown et al. (2021) | Mixed design | Method × Dataset | Multiple DVs | n=100/dataset | Mixed ANOVA | Yes (partial η²) | Order effects |
| Lee et al. (2020) | Quasi-experimental | Before/After XAI | Decision accuracy | n=30 | Paired t-test | Yes (d=0.67) | No control group |

**Patterns Observed:**

**Study Designs:**
- Between-subjects: 45% (n=10)
- Within-subjects: 32% (n=7)
- Mixed: 18% (n=4)
- Other: 5% (n=1)

**Sample Size:**
- Median: n=100
- Range: 30-500
- 68% had n < 200

**Statistical Rigor:**
- Power analysis reported: 27% (6/22)
- Effect sizes reported: 59% (13/22)
- Assumptions tested: 41% (9/22)

**Common Limitations:**
1. Small sample sizes (77%)
2. Single dataset (64%)
3. No cross-validation (55%)
4. Selection bias (41%)

**Gap for my dissertation:**
Most studies lack:
- A priori power analysis (73% don't report)
- Cross-dataset validation (64% single dataset)
- Theoretical grounding (86% purely empirical)

**Opportunity:** Rigorous, theoretically-grounded evaluation with adequate power.
```

## Matrix Dimensions by Field

### Computer Science / Engineering
- Algorithm/method
- Dataset/benchmark
- Metrics (accuracy, F1, etc.)
- Computational cost
- Scalability
- Open source?

### Social Sciences
- Theoretical framework
- Study design
- Sample characteristics
- Measures/instruments
- Statistical approach
- Effect sizes

### Medicine / Health
- Population
- Intervention
- Comparison
- Outcome (PICO format)
- Study quality score
- Risk of bias

## Advanced Features

### Color Coding
```markdown
| Study | Sample Size | Power |
|-------|-------------|-------|
| Study A | 200 | ✅ 0.94 |
| Study B | 50 | ⚠️ 0.62 |
| Study C | 30 | ❌ 0.31 |
```

### Aggregation
```markdown
**Summary Statistics:**
- Mean sample size: 156.4 (SD=89.2)
- Median accuracy: 0.87 (IQR: 0.82-0.91)
- % reporting effect sizes: 59%
```

### Gap Identification
```markdown
**What's Covered:**
- VGGFace2 dataset: 68% of studies
- Grad-CAM: 45% of studies

**What's Missing:**
- Cross-racial evaluation: 5%
- Temporal stability: 0%
- Real-world deployment: 9%
```

## Output Formats

### 1. Markdown Table
For GitHub, dissertations, informal sharing.

### 2. LaTeX Table
For Chapter 2 in dissertation.

```latex
\begin{table}[h]
\centering
\caption{XAI Methods Comparison}
\label{tab:xai-comparison}
\begin{tabular}{llccl}
\toprule
Study & Method & Dataset & n & Key Finding \\
\midrule
Smith et al. (2023) & GradCAM & VGGFace2 & 200 & 0.87 loc. acc. \\
Jones et al. (2022) & LIME & LFW & 150 & 0.72 loc. acc. \\
\bottomrule
\end{tabular}
\end{table}
```

### 3. CSV/Excel
For further analysis, sorting, filtering.

### 4. Systematic Review Table
PRISMA-compliant format with quality assessment.

## Integration with Chapter 2

### Typical Usage

```markdown
# 2.3 Literature Synthesis

To systematically compare XAI methods for biometric systems, we
synthesized findings from 52 included studies (see Section 2.2).
Table 2.1 presents a comparison of XAI methods, datasets, and
performance metrics.

[INSERT MATRIX HERE]

Several patterns emerge from this synthesis:

1. **Dataset concentration:** 68% of studies use VGGFace2,
   limiting generalizability.

2. **Metric inconsistency:** Only 41% report localization
   accuracy, hindering cross-study comparison.

3. **Sample size variability:** Sample sizes range from 30
   to 500 (median: 100), with only 27% reporting power
   analysis.

4. **Theoretical gaps:** 86% of studies are purely empirical,
   lacking theoretical frameworks for explanation quality.

These gaps motivate our work (see Section 2.5).
```

### Table Numbering
- Table 2.1: Methods Comparison
- Table 2.2: Performance Synthesis
- Table 2.3: Methodology Summary
- Table 2.4: Gap Analysis

## Time Savings

**Manual synthesis:** 6-8 hours (reading, extracting, organizing)
**Using @synthesis-matrix:** 30-60 minutes
**Saved:** ~6 hours per review 🎉

## Best Practices

### 1. Start Early
Build matrix as you read papers, not after.

### 2. Consistent Dimensions
Use same categories across all papers for comparison.

### 3. Cite Every Cell
Each claim in matrix should trace to specific paper.

### 4. Note Missing Data
Use "NR" (not reported) when info unavailable.

### 5. Quality Assessment
Include study quality column (risk of bias).

### 6. Keep Raw Data
Maintain detailed extraction sheet, summarize for dissertation.

## Common Errors Fixed

### Error 1: Too Many Dimensions
❌ 15 columns - impossible to read

✅ 5-7 key dimensions - focus on what matters

### Error 2: Inconsistent Categories
❌ "GradCAM" vs "Grad-CAM" vs "GRADCAM"

✅ Standardize terminology

### Error 3: No Summary
❌ Just a table with no interpretation

✅ Always synthesize patterns and gaps

### Error 4: Cherry-Picking
❌ Only include papers supporting your view

✅ Systematic inclusion based on PRISMA criteria

## Quality Checklist

Before using in dissertation:
- [ ] All included papers in matrix
- [ ] Dimensions aligned with research questions
- [ ] Consistent terminology across rows
- [ ] Missing data marked clearly ("NR")
- [ ] Summary/synthesis provided
- [ ] Gaps explicitly identified
- [ ] Table properly formatted
- [ ] Caption and label added
- [ ] Cross-referenced in text

## Example Workflow

```
1. Complete PRISMA search (/run-literature-search)
2. Screen papers (/screen-papers)
3. Read and extract key info from included papers
4. Use @synthesis-matrix to create comparison tables
5. Identify patterns, gaps, contradictions
6. Write synthesis narrative around matrix
7. Format for Chapter 2
8. Cross-reference in text
```

## Software Integration

### Reference Managers
- **Zotero:** Export to CSV, feed to @synthesis-matrix
- **Mendeley:** Extract metadata
- **EndNote:** Custom field extraction

### Spreadsheets
- Start in Excel/Google Sheets for flexibility
- Export to LaTeX for dissertation
- Export to CSV for archiving

### Systematic Review Tools
- **Covidence:** Built-in extraction forms
- **Rayyan:** Tag-based organization
- **DistillerSR:** Customizable extraction

## Related Skills

- `/run-literature-search` - Find papers
- `/screen-papers` - PRISMA screening
- `@prisma-diagram` - Flow diagram
- `@lit-gap` - Identify research gaps
- `@inclusion-criteria` - Define screening rules

## Field-Specific Tips

### STEM Fields
Focus on:
- Quantitative metrics
- Datasets/benchmarks
- Reproducibility (code available?)
- Computational costs

### Social Sciences
Focus on:
- Theoretical frameworks
- Sample characteristics
- Measurement instruments
- Statistical rigor

### Humanities
Focus on:
- Theoretical lens
- Methodological approach
- Primary sources
- Interpretive frameworks

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 30-60 minutes
**Time saved:** ~6 hours
**Reusability:** Very High (any systematic review)
**Critical for:** Chapter 2 (Literature Review)
