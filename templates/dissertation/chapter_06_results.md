# Chapter 6: Results

## Overview

Present experimental findings objectively. Report what you observed, not your interpretation (save that for Chapter 7).

**Target Length:** 10,000-15,000 words

**⚠️ CRITICAL PRINCIPLE:** Results must be reported honestly. RULE 1 applies here more than anywhere: Scientific truth comes first. Report what you found, not what you hoped to find.

---

## 6.1 Overview

**[START WRITING HERE]**

Summary of experiments and key findings:
- What experiments you ran (aligned with RQs)
- Main results (high-level, objective)
- Organization of this chapter

**Template:**

> This chapter presents the results of our empirical evaluation. We conducted [N] experiments to address our research questions (Section 1.3). Section 6.2 reports results for RQ1 ([brief description]), Section 6.3 addresses RQ2 ([brief description]), and Section 6.4 covers RQ3 ([brief description]). Sections 6.5-6.6 provide additional analysis including ablation studies and computational performance. Section 6.7 presents qualitative analysis, and Section 6.8 summarizes findings.

---

### 📚 CITATION CHECK (Section 6.1)

Before moving to Section 6.2, verify:

- [ ] **Metrics are cited (or cross-referenced)**
  - Example: "We evaluate using insertion AUC (Petsiuk et al., 2018; see Section 4.6.2)"
  - Or: "Metrics are defined in Section 4.6.2"

- [ ] **Baselines are cited (or cross-referenced)**
  - Example: "We compare against GradCAM (Selvaraju et al., 2017) and LIME (Ribeiro et al., 2016)"
  - Or: "Baselines are described in Section 4.6.3"

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 6.2 [Experiment 1: RQ1 Validation]

**[CUSTOMIZE TITLE]** (e.g., "6.2 RQ1: Computational Efficiency")

### 6.2.1 Experimental Setup

**[Brief recap of setup specific to this experiment]**

**Research Question:** [Restate RQ1 from Section 1.3]

**Setup:**
- **Dataset**: [Name] (see Section 4.6.1)
- **Configuration**: [Specific settings for this experiment]
- **Metrics**: [Which metrics used]
- **Baselines**: [Which baselines compared against]
- **Hardware**: [Specific hardware used]
- **Number of runs**: [e.g., "3 runs with random seeds 42, 123, 456"]

### 6.2.2 Results

**[PRESENT RESULTS OBJECTIVELY]**

**Table 6.1: [Descriptive Title, e.g., "Computational Performance Comparison on LFW Dataset"]**

| Method | Latency (ms) | Throughput (FPS) | Memory (GB) |
|--------|--------------|------------------|-------------|
| Baseline 1 (Author, Year) | X.XX ± Y.YY | X.XX ± Y.YY | X.XX |
| Baseline 2 (Author, Year) | X.XX ± Y.YY | X.XX ± Y.YY | X.XX |
| **Our Method** | **X.XX ± Y.YY** | **X.XX ± Y.YY** | **X.XX** |

*Note: Results are mean ± standard deviation over [N] runs. Lower latency and higher throughput are better.*

**Statistical Significance:**
- Our method vs. Baseline 1: p < 0.001 (paired t-test)
- Our method vs. Baseline 2: p = 0.023 (paired t-test)

**Figure 6.1: [Descriptive Title, e.g., "Latency Distribution Across Methods"]**
[Box plot or violin plot showing distribution of latencies]

### 6.2.3 Analysis

**[Objective description of what the results show]**

Key observations:

1. **Latency**: Our method achieves [X.XX ms] mean latency, which is [Y]% faster than Baseline 1 ([Z.ZZ ms]) and [W]% faster than Baseline 2 ([V.VV ms]). The difference is statistically significant (p < 0.05) for both comparisons.

2. **Throughput**: At [X.XX FPS], our method processes [N]x more samples per second than Baseline 1.

3. **Memory**: Memory consumption is [comparable/lower/higher] at [X.XX GB], which is [Y]% [more/less] than baselines.

4. **Variance**: Standard deviation is [low/high] ([Y.YY ms]), indicating [stable/variable] performance across runs.

**Answer to RQ1:** [Direct answer to the research question based on these results]

---

### 📚 CITATION CHECK (Section 6.2)

Before moving to Section 6.3, verify:

- [ ] **Baselines are cited**
  - In Table 6.1, cite the paper for each baseline method
  - Example: "Baseline 1 (Selvaraju et al., 2017)"

- [ ] **Statistical tests are cited**
  - If using standard tests, cite the method or textbook
  - Example: "paired t-test (see Section 4.7.2)"

- [ ] **Comparison claims are supported by data**
  - If claiming "faster," show the numbers and significance test
  - Don't just assert; cite your own table

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

**⚠️ RULE 1 REMINDER:** Every claim must be supported by data shown in this chapter.

---

## 6.3 [Experiment 2: RQ2 Validation]

**[REPEAT STRUCTURE FROM 6.2]**

- 6.3.1 Experimental Setup
- 6.3.2 Results (with table and figure)
- 6.3.3 Analysis

**[IMPORTANT: Include statistical significance, effect sizes, confidence intervals]**

---

## 6.4 [Experiment 3: RQ3 Validation]

**[REPEAT STRUCTURE FROM 6.2]**

- 6.4.1 Experimental Setup
- 6.4.2 Results (with table and figure)
- 6.4.3 Analysis

---

### 📚 CITATION CHECK (Sections 6.3-6.4)

Before moving to Section 6.5, verify:

- [ ] **Same checks as Section 6.2** apply to all experiment sections
- [ ] **Cross-references are correct**
  - When referring to prior sections, verify section numbers
  - Example: "As shown in Section 6.2.2..."

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 6.5 Ablation Studies

**[START WRITING HERE]**

**Purpose:** Ablation studies isolate the contribution of each component by removing or modifying individual parts of the system.

### 6.5.1 Component Ablation

**[Test impact of removing each component]**

**Experimental Setup:**
- **Base configuration**: Full system (all components)
- **Ablations tested**: Remove Component A, B, C individually
- **Metric used**: [Primary metric, e.g., Insertion AUC]
- **Dataset**: [Which dataset]

**Table 6.X: Component Ablation Study**

| Configuration | Insertion AUC | Δ from Full | Statistical Significance |
|---------------|---------------|-------------|--------------------------|
| **Full System** | **0.XXX ± 0.YYY** | — | — |
| w/o Component A | 0.XXX ± 0.YYY | -Z.Z% | p < 0.001 |
| w/o Component B | 0.XXX ± 0.YYY | -W.W% | p = 0.012 |
| w/o Component C | 0.XXX ± 0.YYY | -V.V% | p < 0.001 |

*Note: "w/o" means "without". Results are mean ± std over 3 runs. Statistical significance is vs. full system using paired t-test.*

**Findings:**

1. **Component A** contributes [X.X]% to overall performance. Removing it causes a significant drop (p < 0.001), indicating it is critical for [reason based on what it does].

2. **Component B** contributes [Y.Y]% to performance. The impact is moderate but statistically significant (p = 0.012).

3. **Component C** contributes [Z.Z]% to performance. This is the largest single contribution, confirming its importance for [reason].

**Cumulative Ablation:**

**Table 6.Y: Cumulative Component Removal**

| Configuration | Metric | Δ from Full |
|---------------|--------|-------------|
| Full System | 0.XXX | — |
| w/o A | 0.XXX | -X% |
| w/o A, B | 0.XXX | -Y% |
| w/o A, B, C (Baseline) | 0.XXX | -Z% |

**Observation:** Removing components sequentially shows [cumulative/non-additive] effects, indicating [interaction/independence] between components.

### 6.5.2 Hyperparameter Sensitivity

**[Test sensitivity to key parameters]**

**Parameters Tested:**
1. **Parameter 1** (e.g., learning rate): [range tested]
2. **Parameter 2** (e.g., batch size): [range tested]
3. **Parameter 3** (e.g., number of iterations): [range tested]

**Figure 6.X: Hyperparameter Sensitivity Analysis**
[Line plots showing performance vs. parameter values, with error bars]

**Findings:**

- **Parameter 1**: Performance is [stable/sensitive] to changes. Optimal value is approximately [X], with performance degrading [slightly/significantly] outside the range [Y-Z].

- **Parameter 2**: Relatively [insensitive/sensitive]. Performance varies by [X]% across the tested range.

- **Parameter 3**: [Description of sensitivity]

**Robustness:** Our method is [robust/sensitive] to hyperparameter choices, requiring [minimal/careful] tuning.

---

### 📚 CITATION CHECK (Section 6.5)

Before moving to Section 6.6, verify:

- [ ] **Ablation methodology is cited (if following standard practices)**
  - If using established ablation approaches, cite papers that use similar methods
  - Example: "Following standard ablation practices (Author, Year)..."

- [ ] **Statistical tests for ablations are cited**
  - Cross-reference Section 4.7.2 or cite the test

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 6.6 Computational Performance

**[START WRITING HERE]**

### 6.6.1 Runtime Analysis

**Experimental Setup:**
- **Hardware**: [Exact specifications, e.g., "NVIDIA A100 80GB GPU"]
- **Batch size**: [e.g., 32]
- **Measurement**: [e.g., "Warm-up 10 iterations, then measure 100 iterations"]
- **Metric**: [e.g., "Mean ± std latency per sample (ms)"]

**Table 6.X: Computational Cost Comparison**

| Method | Latency (ms) | Memory (GB) | Throughput (samples/s) | GPU Utilization (%) |
|--------|--------------|-------------|------------------------|---------------------|
| Baseline 1 | X.XX ± Y.YY | X.XX | X.XX | X.XX |
| Baseline 2 | X.XX ± Y.YY | X.XX | X.XX | X.XX |
| **Our Method** | **X.XX ± Y.YY** | **X.XX** | **X.XX** | **X.XX** |

**Findings:**

- **Latency**: Our method achieves [X.XX ms] mean latency, which [meets/exceeds] our target of [Y ms] (stated in RQ1).

- **Memory**: Memory footprint is [X.XX GB], which is [acceptable/high/low] for deployment on [hardware type].

- **Throughput**: At [X.XX samples/s], our method can process [real-time/batch] workloads.

### 6.6.2 Scalability

**[How performance scales with data size/complexity]**

**Experimental Setup:**
- Vary input size: [e.g., "Image resolution from 224×224 to 1024×1024"]
- Measure latency and memory as size increases

**Figure 6.X: Scaling Behavior**
[Log-log plot showing latency and memory vs. input size, with fitted scaling curves]

**Findings:**

- **Time Complexity**: Latency scales as O([complexity]) empirically, matching our theoretical analysis (Section 4.3.3).

- **Memory Complexity**: Memory usage scales as O([complexity]).

- **Practical Implications**: Our method is [suitable/unsuitable] for [large-scale/real-time] applications up to input sizes of [X].

### 6.6.3 Comparison to Theoretical Bounds

**[Compare empirical performance to theoretical predictions]**

| Metric | Theoretical | Empirical | Match? |
|--------|-------------|-----------|--------|
| Time Complexity | O(M log M) | O(M^1.1) | ✓ Close |
| Space Complexity | O(M) | O(M) | ✓ Exact |

**Analysis:** Empirical complexity closely matches theoretical predictions, with minor deviations due to [implementation details/constant factors].

---

### 📚 CITATION CHECK (Section 6.6)

Before moving to Section 6.7, verify:

- [ ] **Hardware specifications are documented**
  - No citation needed, but ensure complete documentation

- [ ] **Complexity analysis references Chapter 3 or 4**
  - Example: "matching our theoretical analysis (Section 4.3.3)"

- [ ] **Comparison baselines are cited**
  - Same as previous sections

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 6.7 Qualitative Analysis

**[If applicable: case studies, visualizations, failure cases]**

### 6.7.1 Success Cases

**[Examples where your method works well]**

**Figure 6.X: Example Success Cases**
[Visual examples with input, output, ground truth, and explanation]

**Case Study 1:**
- **Input**: [Description]
- **Output**: [What your method produced]
- **Ground Truth/Expected**: [What should happen]
- **Analysis**: [Why it succeeded]

**Case Study 2:**
- [Repeat structure]

**Patterns:** Success cases share characteristics: [list common features, e.g., "high-contrast images," "clear facial features," etc.]

### 6.7.2 Failure Cases

**⚠️ CRITICAL SECTION:** Honest reporting of failures is essential for scientific integrity (RULE 1).

**[Honest reporting of where your method fails]**

**Figure 6.Y: Example Failure Cases**
[Visual examples showing failures, with honest analysis]

**Case Study 1:**
- **Input**: [Description]
- **Output**: [What your method produced]
- **Ground Truth/Expected**: [What should have happened]
- **Failure Type**: [Classification: e.g., "false negative," "incorrect explanation," "instability"]
- **Analysis**: [Why it failed - be specific and honest]

**Case Study 2:**
- [Repeat structure]

**Failure Patterns:**

1. **Failure Pattern 1**: [When and why it fails]
   - **Frequency**: [e.g., "Occurs in ~5% of test cases"]
   - **Cause**: [Root cause analysis]
   - **Potential Fix**: [Brief suggestion for future work]

2. **Failure Pattern 2**: [When and why it fails]
   - **Frequency**: [quantify]
   - **Cause**: [analysis]
   - **Potential Fix**: [suggestion]

**Limitation Acknowledgment:**

Our method has limitations in the following scenarios:
- [Scenario 1, e.g., "Low-resolution images (<64×64)"]
- [Scenario 2, e.g., "Extreme lighting conditions"]
- [Scenario 3, e.g., "Occlusions covering >30% of the face"]

**Comparison to Baselines:**

Do baselines also fail in these cases?
- **Baseline 1**: [also fails/succeeds] in similar scenarios
- **Baseline 2**: [also fails/succeeds] in similar scenarios

**Honest Assessment:** While our method improves on baselines overall (Section 6.2-6.4), it is not a complete solution and shares some failure modes with prior work.

### 6.7.3 Edge Cases and Robustness

**[Test behavior on edge cases]**

**Edge Cases Tested:**
1. **Adversarial perturbations**: [How robust is the method to adversarial attacks?]
2. **Noisy inputs**: [Performance with varying levels of noise]
3. **Out-of-distribution data**: [Behavior on data not in training set]

**Figure 6.Z: Robustness Analysis**
[Plot showing performance degradation vs. perturbation/noise level]

**Findings:**

- **Adversarial robustness**: [Description of results, honest about vulnerabilities]
- **Noise robustness**: Performance degrades [gradually/sharply] as noise increases
- **OOD generalization**: Method [generalizes well/poorly] to unseen domains

---

### 📚 CITATION CHECK (Section 6.7)

Before moving to Section 6.8, verify:

- [ ] **Failure analysis is honest (RULE 1)**
  - Don't hide or minimize failures
  - Report them objectively

- [ ] **Comparison to baselines is fair**
  - If baselines also fail, acknowledge it
  - If baselines succeed where you fail, report it honestly

- [ ] **Adversarial robustness methods are cited (if tested)**
  - Example: "We test using FGSM attacks (Goodfellow et al., 2015)"

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

**⚠️ RULE 1 REMINDER:** Failure cases must be reported honestly. Hiding failures is scientific misconduct.

---

## 6.8 Summary

**[START WRITING HERE]**

Summarize key findings objectively:

**RQ1 Results:** [Direct answer to RQ1 based on Section 6.2]
- Key finding: [Statement with numbers]
- Statistical significance: [p-value or confidence interval]
- Comparison to baselines: [How does it compare?]

**RQ2 Results:** [Direct answer to RQ2 based on Section 6.3]
- Key finding: [Statement with numbers]
- Statistical significance: [p-value or confidence interval]
- Comparison to baselines: [How does it compare?]

**RQ3 Results:** [Direct answer to RQ3 based on Section 6.4]
- Key finding: [Statement with numbers]
- Statistical significance: [p-value or confidence interval]
- Comparison to baselines: [How does it compare?]

**Additional Findings:**
- Ablation studies (Section 6.5) confirm that [key components contribute to performance]
- Computational performance (Section 6.6) shows [practical viability/limitations]
- Qualitative analysis (Section 6.7) reveals [success patterns and failure modes]

**Overall:** [High-level objective takeaway - what do these results tell us? Save interpretation for Chapter 7]

---

## Writing Guidelines

### Objectivity (RULE 1)
- Report what you observed, not what you hoped for
- Include both positive and negative results
- Don't cherry-pick data
- Be honest about failures
- No spin: "while our method failed in X cases" not "our method only failed in X cases"

### Statistical Rigor
- **Always report**: mean ± standard deviation (not just mean)
- **Include**: confidence intervals (95% CI)
- **Perform**: significance testing (t-test, Wilcoxon, ANOVA as appropriate)
- **Report**: effect sizes (Cohen's d, r², etc.)
- **State**: number of runs/trials (minimum 3, preferably 5-10)
- **Document**: random seeds used

**Example (Good):**
> Our method achieves 92.3 ± 1.2% accuracy (mean ± std over 5 runs), compared to baseline 89.7 ± 1.5%. The difference is statistically significant (p = 0.003, paired t-test, Cohen's d = 1.8, large effect).

**Example (Bad):**
> Our method achieves 92.3% accuracy, better than baseline 89.7%.

### Clarity
- Every table/figure must be referenced in text
- Captions should be self-explanatory (reader should understand without reading text)
- Use consistent formatting across all tables/figures
- Bold/highlight your results in tables
- Error bars in all plots
- Legends in all figures

### Reproducibility
- Report all hyperparameters
- Specify random seeds
- Note hardware used
- Provide enough detail that someone could reproduce your numbers exactly

### Negative Results
- Report all experiments you ran, not just successful ones
- If an approach didn't work, say so and explain why
- Negative results are valuable contributions (they prevent others from trying the same thing)

**Example:**
> We initially hypothesized that increasing K to 1000 would improve performance. However, results show no significant improvement (p = 0.42) while increasing computational cost by 10x. We therefore use K = 100 in all subsequent experiments.

---

## Writing Quality Checklist

### Content
- [ ] All research questions are addressed
- [ ] Results are presented objectively (no interpretation yet)
- [ ] Statistical significance is tested and reported
- [ ] Effect sizes are reported
- [ ] Confidence intervals are included
- [ ] Both successes and failures are reported honestly
- [ ] Ablation studies demonstrate component contributions
- [ ] Computational performance is analyzed

### Statistical Rigor
- [ ] Mean ± std reported for all metrics
- [ ] Significance tests performed (p-values reported)
- [ ] Number of runs/trials stated (≥3)
- [ ] Random seeds documented
- [ ] Corrections for multiple comparisons (if applicable)

### Tables and Figures
- [ ] All tables/figures are referenced in text
- [ ] Captions are self-explanatory
- [ ] Error bars included in all plots
- [ ] Consistent formatting
- [ ] High resolution (300 DPI for figures)
- [ ] Colorblind-friendly palettes

### Honesty (RULE 1)
- [ ] No cherry-picking of results
- [ ] Negative results reported
- [ ] Failure cases analyzed
- [ ] Limitations acknowledged
- [ ] No misleading visualizations

### Citations
- [ ] All baselines are cited in tables
- [ ] Statistical tests are cited or cross-referenced
- [ ] Ablation methods are cited (if standard)
- [ ] All 5 citation checks above are complete

---

### 📚 FINAL CITATION AUDIT (Entire Chapter)

Before submitting Chapter 6, perform a final audit:

- [ ] **Section 6.1**: Metrics and baselines cited or cross-referenced ✅
- [ ] **Sections 6.2-6.4**: All baselines cited in tables, statistical tests cited ✅
- [ ] **Section 6.5**: Ablation methods cited (if applicable) ✅
- [ ] **Section 6.6**: Complexity analysis cross-referenced to Chapter 3/4 ✅
- [ ] **Section 6.7**: Failure analysis is honest (RULE 1) ✅

**Total Citation Checks:** 5 strategic checkpoints

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md) for:
- How to cite your own prior chapters (cross-references)
- Citation formats for baselines in tables
- How to report statistical tests

**⚠️ RULE 1 REMINDER:** If you can't defend it with data, don't claim it.

---

## Word Count Target

**Target:** 10,000-15,000 words

**Suggested Breakdown:**
- 6.1 Overview: 300-500 words
- 6.2-6.4 Experiments (3 RQs): 6,000-9,000 words (2,000-3,000 per RQ)
- 6.5 Ablation Studies: 1,500-2,000 words
- 6.6 Computational Performance: 1,000-1,500 words
- 6.7 Qualitative Analysis: 1,000-1,500 words
- 6.8 Summary: 500-800 words

**Current:** [TRACK HERE]

---

## Revision Iteration Process

**Results chapters require meticulous attention to detail and honesty. Follow this 5-iteration process:**

### Iteration 1: Complete All Experiments (Weeks 1-2)
**Goal:** Run all experiments and collect data

**Tasks:**
- [ ] Run all experiments (RQ1, RQ2, RQ3)
- [ ] Run ablation studies
- [ ] Measure computational performance
- [ ] Collect qualitative examples (successes and failures)
- [ ] Record all data in spreadsheets/logs

**Checkpoint:** All experiments completed, data collected

---

### Iteration 2: Statistical Analysis (Week 3)
**Goal:** Perform rigorous statistical analysis

**Tasks:**
- [ ] Calculate mean ± std for all metrics
- [ ] Perform significance tests (t-tests, Wilcoxon, etc.)
- [ ] Calculate effect sizes (Cohen's d, r², etc.)
- [ ] Compute confidence intervals
- [ ] Check for multiple comparisons (apply Bonferroni correction if needed)
- [ ] Verify all numbers are correct (double-check calculations)

**Checkpoint:** All statistics computed and verified

---

### Iteration 3: Honest Reporting (Week 4)
**Goal:** Report results honestly (RULE 1)

**Tasks:**
- [ ] Draft all sections (6.1-6.8)
- [ ] Report both positive and negative results
- [ ] Include failure cases (Section 6.7.2)
- [ ] Don't cherry-pick data
- [ ] Don't spin negative results
- [ ] Verify no misleading claims

**Advisor Review:** **CRITICAL CHECKPOINT**
- Ask advisor: "Are there any results I should be more honest about?"
- Show failure cases and get feedback

**Checkpoint:** Results are reported honestly, no misleading claims

---

### Iteration 4: Tables and Figures (Week 5)
**Goal:** Create clear, high-quality visualizations

**Tasks:**
- [ ] Create all tables (with mean ± std, bolded results)
- [ ] Create all figures (with error bars, legends, captions)
- [ ] Ensure 300 DPI resolution
- [ ] Use colorblind-friendly palettes
- [ ] Make captions self-explanatory
- [ ] Reference every table/figure in text
- [ ] Check consistency of formatting

**Checkpoint:** All visualizations are clear and professional

---

### Iteration 5: Verification and Polish (Week 6)
**Goal:** Verify accuracy and polish writing

**Tasks:**
- [ ] Complete all 5 citation checks
- [ ] Verify all numbers match your data (no typos in tables)
- [ ] Check that p-values are correct
- [ ] Cross-check with raw data files
- [ ] Proofread for typos
- [ ] Ensure objective tone (no interpretation - save for Chapter 7)
- [ ] Complete writing quality checklist

**Advisor Review:** Submit complete chapter for final review

**Checkpoint:** Chapter is accurate, complete, and honest

---

### When to Stop Iterating

**You're done when:**
- [ ] Advisor approves the chapter
- [ ] All 5 citation checks pass
- [ ] Writing quality checklist is complete
- [ ] All experiments are reported (including negative results)
- [ ] Statistical rigor is evident (mean ± std, p-values, effect sizes)
- [ ] Failure cases are honestly analyzed
- [ ] All numbers are verified correct
- [ ] Tables and figures are publication-quality

**Estimated Time:** 6-7 weeks (including running experiments, analysis, writing, revisions)

---

## Recommended Visualizations

### Required Figures/Tables:
1. **Comparison tables** (your method vs. baselines) - At least one per RQ
2. **Performance plots** (bar charts with error bars, box plots)
3. **Ablation study results** (table and/or figure)
4. **Scalability analysis** (line plot showing scaling behavior)
5. **Success and failure examples** (qualitative visualizations)
6. **Statistical significance** (can be integrated into tables or separate figure)

### Figure Quality Standards:
- **Resolution**: 300 DPI minimum
- **Format**: PDF (vector) preferred, PNG (high-res) acceptable
- **Labels**: Clear axis labels with units
- **Legends**: Present and easy to read
- **Error bars**: Show std, 95% CI, or standard error
- **Colors**: Use colorblind-friendly palettes (e.g., Colorbrewer, viridis)
- **Consistency**: Same style (fonts, colors, sizes) across all figures
- **Caption**: Self-explanatory (reader can understand without text)

---

## Notes to Self

**[YOUR NOTES]**

- Missing experiments:
- Additional analyses needed:
- Figures to create:
- Statistical tests to run:
- Failure cases to document:

---

**END OF CHAPTER 6 TEMPLATE**
