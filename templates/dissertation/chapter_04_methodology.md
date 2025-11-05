# Chapter 4: Methodology

## Overview

Describe your research approach in detail. Explain WHAT you did, HOW you did it, and WHY you made these choices.

**Target Length:** 6,000-8,000 words

---

## 4.1 Overview

**[START WRITING HERE]**

Brief summary of your methodology:
- Research approach (theoretical/experimental/computational/mixed)
- Key components of your system/method
- Datasets/benchmarks used
- Evaluation metrics
- Experimental design

**Template:**

> This chapter describes our methodology in detail. We employ a [theoretical/computational/experimental/mixed] approach consisting of [N] main components (Sections 4.3-4.5). We validate our approach through experiments on [datasets] (Section 4.6), evaluated using [metrics], and compared against [baselines]. This methodology directly addresses our research questions (Section 1.3) and enables us to [what it accomplishes].

---

## 4.2 Research Approach

**[START WRITING HERE]**

**What to Include:**
- Overall strategy (theory + implementation + experiments)
- Justification for approach
- How you answer each research question

**Structure:**

**Alignment with Research Questions:**

- **RQ1**: [State RQ1] → Addressed by [which component/experiment]
- **RQ2**: [State RQ2] → Addressed by [which component/experiment]
- **RQ3**: [State RQ3] → Addressed by [which component/experiment]

**Research Design:**

We employ a [qualitative/quantitative/mixed-methods/computational/theoretical] research design. Our approach consists of the following phases:

1. **Phase 1: [Name]** (Sections 4.3-4.X)
   - Purpose: [What this accomplishes]
   - Output: [What is produced]

2. **Phase 2: [Name]** (Sections 4.Y-4.Z)
   - Purpose: [What this accomplishes]
   - Output: [What is produced]

3. **Phase 3: Validation** (Section 4.6)
   - Purpose: Empirical evaluation
   - Output: Results presented in Chapter 6

**Methodological Justification:**

We chose this approach because [rationale]. Alternative approaches such as [alternative] were considered but not adopted because [reason].

---

### 📚 CITATION CHECK (Section 4.2)

Before moving to Section 4.3, verify:

- [ ] **Research design is cited**
  - If using established research methodology (e.g., design science, action research), cite methodological literature
  - Example: "We employ a design science approach (Hevner et al., 2004)"

- [ ] **Justification for approach is supported**
  - If claiming your approach is "standard in the field," cite papers that use it
  - If defending against alternative approaches, cite them

- [ ] **Connection to RQs is explicit**
  - Show how each component addresses specific research questions

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 4.3 [Component 1: Your Main Contribution]

**[CUSTOMIZE TITLE]** (e.g., "4.3 Hierarchical SHAP Framework" or "4.3 Novel Feature Extraction Method")

### 4.3.1 Problem Formulation

**[Mathematical formulation of the problem]**

- Define variables and notation
- State the problem formally
- Specify constraints and assumptions

**Example Structure:**

> Let $X = \{x_1, x_2, \ldots, x_n\}$ denote [input space]. We define [problem] as follows: Given [input], find [output] such that [objective] is optimized subject to [constraints].
>
> **Notation:**
> - $x_i$: [description]
> - $f(x)$: [description]
> - $\mathcal{L}$: [description]

### 4.3.2 Proposed Approach

**[Describe your method/algorithm/system]**

- High-level design
- Key innovations
- Algorithmic steps (use pseudocode if helpful)
- Design rationale

**Guidance:**
- Be precise and complete
- Include pseudocode for complex algorithms
- Explain intuition behind design choices
- Reference related work where you build on prior methods

### 4.3.3 Theoretical Analysis (if applicable)

**[Complexity analysis, proofs, guarantees]**

- Time/space complexity
- Convergence guarantees
- Approximation bounds
- Correctness proofs

**Note:** If you have extensive proofs, put them in Chapter 3 (Theoretical Foundation) and summarize here.

---

### 📚 CITATION CHECK (Section 4.3 - Component 1)

Before moving to Section 4.4, verify:

- [ ] **Prior work is cited**
  - If your method builds on or modifies prior work, cite it
  - Example: "Building on [Author, Year], we extend their approach by..."

- [ ] **Notation follows established conventions**
  - If using standard notation from your field, cite the seminal paper that introduced it

- [ ] **Related methods are cited**
  - If comparing your design choices to alternatives, cite those alternatives

- [ ] **Theoretical results cite sources**
  - If using theorems from prior work, cite them
  - If proving new theorems, reference Chapter 3

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 4.4 [Component 2]

**[REPEAT STRUCTURE ABOVE]**

- 4.4.1 Problem Formulation
- 4.4.2 Proposed Approach
- 4.4.3 Theoretical Analysis (if applicable)

---

## 4.5 [Component 3]

**[REPEAT STRUCTURE ABOVE]**

---

### 📚 CITATION CHECK (Sections 4.4-4.5 - Remaining Components)

Before moving to Section 4.6, verify:

- [ ] **All components cite related work** (same as Section 4.3)
- [ ] **Design trade-offs are explained**
  - If choosing approach A over approach B, cite both and explain why

- [ ] **Integration with prior work is clear**
  - If combining multiple techniques, cite each

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 4.6 Experimental Design

### 4.6.1 Datasets and Benchmarks

**[START WRITING HERE]**

**Dataset 1: [Name] (Author, Year)**
- **Source**: [URL or paper citation]
- **Size**: [Number of samples, e.g., 13,233 images]
- **Characteristics**: [Key properties, e.g., "Unconstrained facial images in natural settings"]
- **Split**: [Train/val/test split, e.g., "60%/20%/20%"]
- **Usage**: [Why this dataset, e.g., "Standard benchmark for face recognition"]
- **Preprocessing**: [Any preprocessing applied]

**Dataset 2: [Name] (Author, Year)**
**[Repeat for each dataset]**

**Justification:**

We chose these datasets because [reason]. They are widely used in [field] and allow for direct comparison with prior work (Author1, Year; Author2, Year).

---

### 📚 CITATION CHECK (Section 4.6.1 - Datasets)

Before moving to Section 4.6.2, verify:

- [ ] **Every dataset is cited**
  - Cite the paper that introduced the dataset
  - Example: "ImageNet (Deng et al., 2009)" or "LFW (Huang et al., 2007)"

- [ ] **Dataset characteristics are accurate**
  - Verify sizes, splits, and properties against the original paper

- [ ] **Justification cites prior work**
  - If claiming "widely used," cite papers that use it
  - Example: "LFW is a standard benchmark for face recognition (Author1, Year; Author2, Year)"

- [ ] **Preprocessing cites methods**
  - If using standard preprocessing (e.g., normalization), cite the method if applicable

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

**⚠️ RULE 1 REMINDER:** Accurately represent dataset properties.

---

### 4.6.2 Evaluation Metrics

**[START WRITING HERE]**

We evaluate our approach using the following metrics:

**Metric 1: [Name] (Author, Year if applicable)**
- **Definition**: [Formula or precise description]
- **Interpretation**: [What it measures, higher/lower is better]
- **Range**: [e.g., [0, 1] or (-∞, +∞)]
- **Justification**: [Why this metric is appropriate for your research]

**Metric 2: [Name]**
**[Repeat for each metric]**

**Example:**

> **Insertion AUC (Petsiuk et al., 2018)**
> - **Definition**: Area under the curve when progressively adding features in order of importance
> - **Interpretation**: Measures faithfulness of explanations; higher is better
> - **Range**: [0, 1]
> - **Justification**: Standard metric for evaluating explanation quality in XAI literature

### 4.6.3 Baselines

**[START WRITING HERE]**

We compare against the following baselines:

**Baseline 1: [Name] (Author, Year)**
- **Description**: [Brief description of the method]
- **Source**: [Original paper citation + implementation source]
- **Configuration**: [Hyperparameters used, e.g., "Default settings from official implementation"]
- **Rationale**: [Why compare against this, e.g., "Current state-of-the-art for X"]

**Baseline 2: [Name] (Author, Year)**
**[Repeat for each baseline]**

**Example:**

> **GradCAM (Selvaraju et al., 2017)**
> - **Description**: Gradient-weighted Class Activation Mapping for CNNs
> - **Source**: Original paper (Selvaraju et al., 2017), implementation from [pytorch-gradcam repository]
> - **Configuration**: Default settings with final convolutional layer
> - **Rationale**: Widely used baseline for visual explanations in CNNs

---

### 📚 CITATION CHECK (Sections 4.6.2-4.6.3 - Metrics & Baselines)

Before moving to Section 4.6.4, verify:

- [ ] **Every metric is cited**
  - If metric is from literature, cite the paper that introduced it
  - If metric is standard (e.g., accuracy), still define it precisely
  - Example: "F1-score (Powers, 2011)" or "Accuracy (# correct / # total)"

- [ ] **Every baseline is cited**
  - Cite the original paper that proposed the baseline method
  - Cite the implementation source if using existing code

- [ ] **Baseline configurations are documented**
  - If using default settings, state it
  - If modifying settings, explain why and cite justification

- [ ] **Rationale for baselines is supported**
  - If claiming "state-of-the-art," cite evidence (e.g., leaderboards, surveys)
  - If claiming "widely used," cite papers that use it

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

### 4.6.4 Experimental Protocol

**[START WRITING HERE]**

**Experiment 1: [Purpose, e.g., "RQ1 Validation - Latency Benchmarking"]**
- **Goal**: [What are you testing, e.g., "Measure inference time of our method vs. baselines"]
- **Setup**: [Configuration, e.g., "Single NVIDIA A100 GPU, batch size 32"]
- **Procedure**: [Steps, e.g., "1. Warm-up 10 iterations, 2. Measure 100 iterations, 3. Report mean ± std"]
- **Expected outcome**: [What should happen, e.g., "Our method should be <50ms per sample"]

**Experiment 2: [Purpose]**
**[Repeat for each experiment]**

**Reproducibility:**
- Random seeds: [e.g., "42, 123, 456 for three runs"]
- Code availability: [e.g., "Available at [URL] under MIT license"]

### 4.6.5 Implementation Details

**[START WRITING HERE]**

- **Programming language**: [e.g., Python 3.11]
- **Frameworks/libraries**: [e.g., PyTorch 2.0, NumPy 1.24, scikit-learn 1.3]
- **Hardware**: [e.g., NVIDIA A100 80GB GPU, 64GB RAM]
- **Hyperparameters**: [List key settings]
  - Learning rate: [value]
  - Batch size: [value]
  - Epochs: [value]
  - Optimizer: [e.g., Adam (Kingma & Ba, 2015)]
- **Training procedure**: [If applicable, describe training process]
- **Reproducibility**:
  - Random seeds: [values]
  - Code: [availability, e.g., "Provided in supplementary materials"]
  - Environment: [e.g., "requirements.txt included"]

---

## 4.7 Validation Strategy

**[START WRITING HERE]**

How you ensure your results are valid:

### 4.7.1 Cross-Validation (if applicable)

If using cross-validation:
- Type: [k-fold, leave-one-out, stratified]
- Configuration: [k=5, k=10, etc.]
- Rationale: [why this approach]

### 4.7.2 Statistical Significance Testing

- Tests used: [e.g., paired t-test, Wilcoxon signed-rank test]
- Significance level: [e.g., α = 0.05]
- Correction for multiple comparisons: [e.g., Bonferroni correction]
- Software: [e.g., scipy.stats in Python]

### 4.7.3 Ablation Studies

List of ablation experiments:
1. **Ablation 1**: [Remove component X] → Measure impact on [metric Y]
2. **Ablation 2**: [Replace component A with alternative B] → Measure impact
3. [etc.]

**Purpose:** Ablation studies verify that each component contributes to overall performance.

### 4.7.4 Sensitivity Analysis

Analyze sensitivity to:
- Hyperparameters: [which ones, e.g., learning rate, batch size]
- Data quality: [e.g., noise, missing values]
- Random seeds: [report variance across multiple runs]

---

### 📚 CITATION CHECK (Section 4.7 - Validation Strategy)

Before finalizing Chapter 4, verify:

- [ ] **Cross-validation methods are cited**
  - If using standard CV, cite methodological literature (e.g., Stone, 1974)

- [ ] **Statistical tests are cited**
  - Example: "paired t-test (Student, 1908)" or reference to stats textbook

- [ ] **Ablation study design is justified**
  - If following established ablation practices, cite papers that use similar approaches

- [ ] **Software and tools are cited**
  - Cite libraries used (PyTorch, TensorFlow, scikit-learn, etc.)
  - Example: "scikit-learn (Pedregosa et al., 2011)"

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md)

---

## 4.8 Ethics and IRB

**[INCLUDE THIS SECTION IF APPLICABLE]**

### Human Subjects Research

- [ ] **Does your research involve human subjects?**
  - YES → **IRB approval required**
  - NO → State: "This research does not involve human subjects."

**If YES:**

**IRB Approval:**
- Institution: [Your university's IRB]
- Approval number: [Protocol #]
- Approval date: [Date]
- Consent process: [How participants were informed and consented]

**Ethical Considerations:**
- Privacy: [How you protect participant data]
- Anonymization: [How you de-identify data]
- Data storage: [Secure storage practices]
- Potential harms: [Risks and mitigation]

**If NO (most computational dissertations):**

> This research does not involve human subjects. All experiments are conducted on publicly available datasets that have been previously published and do not contain personally identifiable information.

### Data Ethics

**Even if no human subjects, consider:**

- **Dataset ethics**: [Were datasets collected ethically? Cite original papers]
- **Bias**: [Does your dataset have known biases? Acknowledge them]
- **Dual use**: [Could your work be misused? Discuss responsibly]

**Example:**

> We use the FairFace dataset (Kärkkäinen & Joo, 2021), which was collected with consideration for demographic balance and ethical data practices. We acknowledge potential biases in facial recognition systems (Buolamwini & Gebru, 2018) and include fairness analysis (Section 6.X) to evaluate demographic parity.

---

## 4.9 Reproducibility

**[IMPORTANT SECTION FOR MODERN DISSERTATIONS]**

To ensure reproducibility of our work, we provide:

### Code Availability

- **Repository**: [GitHub URL or "Provided in supplementary materials"]
- **License**: [e.g., MIT, Apache 2.0]
- **Documentation**: [README with setup instructions]
- **Dependencies**: [requirements.txt or environment.yml]

### Data Availability

- **Datasets**: [All datasets are publicly available at [URLs]]
- **Preprocessing scripts**: [Included in repository]
- **Train/test splits**: [Exact splits provided]

### Model Checkpoints

- **Pre-trained models**: [Available at [URL] or provided in supplementary materials]
- **Training logs**: [Included for transparency]

### Random Seeds and Determinism

- All experiments use fixed random seeds (42, 123, 456)
- PyTorch deterministic mode enabled: `torch.use_deterministic_algorithms(True)`
- NumPy seed set: `np.random.seed(42)`

### Hardware and Software Environment

- **Hardware**: [Exact specifications]
- **Software**: [Python 3.11, PyTorch 2.0, CUDA 11.8]
- **OS**: [Ubuntu 22.04]
- **Docker**: [Dockerfile provided for exact environment reproduction]

### Estimated Computational Cost

- **Training time**: [e.g., "48 GPU-hours on NVIDIA A100"]
- **Inference time**: [e.g., "10ms per sample"]
- **Storage requirements**: [e.g., "50GB for datasets, 2GB for model checkpoints"]

**Goal:** Another researcher should be able to reproduce our results exactly using the provided code, data, and environment specifications.

---

## Writing Quality Checklist

### Content
- [ ] All components of your method are described
- [ ] Design choices are justified (and alternatives cited)
- [ ] Experimental protocol is reproducible
- [ ] All datasets, metrics, and baselines are clearly defined and cited
- [ ] Ethics/IRB section is complete (or states "not applicable")
- [ ] Reproducibility section provides all necessary details

### Technical Rigor
- [ ] Mathematical notation is consistent
- [ ] Algorithms are precisely described
- [ ] Complexity analysis is included (if applicable)
- [ ] Assumptions and limitations are stated

### Citations
- [ ] Research approach/design is cited
- [ ] All prior work that you build on is cited
- [ ] All datasets are cited
- [ ] All metrics are cited (or precisely defined)
- [ ] All baselines are cited
- [ ] All software libraries are cited
- [ ] All 5 citation checks above are complete

### Clarity
- [ ] Figures/diagrams illustrate your approach
- [ ] Pseudocode is included where helpful
- [ ] Transitions between sections are smooth
- [ ] Writing is precise and unambiguous

---

### 📚 FINAL CITATION AUDIT (Entire Chapter)

Before submitting Chapter 4, perform a final audit:

- [ ] **Section 4.2**: Research approach cited ✅
- [ ] **Sections 4.3-4.5**: All components cite prior work and related methods ✅
- [ ] **Section 4.6.1**: All datasets cited ✅
- [ ] **Sections 4.6.2-4.6.3**: All metrics and baselines cited ✅
- [ ] **Section 4.7**: Validation methods and software cited ✅

**Total Citation Checks:** 5 strategic checkpoints

**📖 See:** [`/tools/bibliography/citation_guidelines.md`](../../tools/bibliography/citation_guidelines.md) for:
- How to cite datasets, software, and tools
- Citation formats for different source types
- Best practices for methodology chapters

**⚠️ RULE 1 REMINDER:** Methodology must be reproducible and accurately represent all sources.

---

## Word Count Target

**Target:** 6,000-8,000 words

**Suggested Breakdown:**
- 4.1 Overview: 300-400 words
- 4.2 Research Approach: 600-800 words
- 4.3-4.5 Components: 2,500-3,500 words (800-1,200 per component)
- 4.6 Experimental Design: 1,500-2,000 words
- 4.7 Validation Strategy: 600-800 words
- 4.8 Ethics and IRB: 200-400 words
- 4.9 Reproducibility: 300-600 words

**Current:** [TRACK HERE]

---

## Revision Iteration Process

**Methodology chapters require precision and completeness. Follow this 5-iteration process:**

### Iteration 1: Complete Description (Week 1)
**Goal:** Describe all components

**Tasks:**
- [ ] Draft all sections (4.1-4.9)
- [ ] Describe all components (4.3-4.5)
- [ ] List datasets, metrics, baselines
- [ ] Don't worry about citations yet

**Checkpoint:** All methodological components are described

---

### Iteration 2: Add Citations (Week 2)
**Goal:** Support every method and design choice

**Tasks:**
- [ ] Complete all 5 citation checks
- [ ] Cite all datasets, metrics, baselines
- [ ] Cite prior work that you build on
- [ ] Cite justifications for design choices

**Checkpoint:** All citation check boxes are complete ✅

---

### Iteration 3: Reproducibility Check (Week 3)
**Goal:** Ensure another researcher can reproduce your work

**Tasks:**
- [ ] Verify Section 4.9 (Reproducibility) is complete
- [ ] Check that all hyperparameters are specified
- [ ] Ensure random seeds are documented
- [ ] Verify code/data availability statements are accurate
- [ ] Add missing implementation details

**Checkpoint:** Another researcher could reproduce your experiments

---

### Iteration 4: Technical Precision (Week 4)
**Goal:** Ensure mathematical and algorithmic correctness

**Tasks:**
- [ ] Verify all mathematical notation is consistent
- [ ] Check that algorithms are precisely specified
- [ ] Ensure complexity analysis is correct
- [ ] Add pseudocode where helpful
- [ ] Cross-check with Chapter 3 (Theory) if applicable

**Checkpoint:** Methodology is technically rigorous

---

### Iteration 5: Clarity and Figures (Week 5)
**Goal:** Make methodology easy to understand

**Tasks:**
- [ ] Add/improve figures (system architecture, flowcharts)
- [ ] Improve transitions between sections
- [ ] Simplify complex sentences
- [ ] Check that rationale for choices is clear
- [ ] Proofread for typos

**Advisor Review:** Submit complete chapter for final review

**Checkpoint:** Methodology is clear, complete, and reproducible

---

### When to Stop Iterating

**You're done when:**
- [ ] Advisor approves the chapter
- [ ] All 5 citation checks pass
- [ ] Writing quality checklist is complete
- [ ] Another researcher could reproduce your experiments from this chapter
- [ ] All design choices are justified
- [ ] Ethics/IRB section is complete (or not applicable)
- [ ] Reproducibility section provides all necessary information

**Estimated Time:** 5-6 weeks for complete methodology chapter (including revisions)

---

## Recommended Figures

- **Figure 4.1**: System architecture diagram
  - Show all components and how they connect
  - Label inputs/outputs

- **Figure 4.2**: Algorithm flowchart
  - Visualize key algorithmic steps
  - Show decision points

- **Figure 4.3**: Experimental pipeline
  - Data flow from datasets → preprocessing → model → evaluation
  - Show train/val/test splits

- **Figure 4.4**: Dataset examples/statistics
  - Sample images or data
  - Histograms of key properties

---

## Notes to Self

**[YOUR NOTES]**

- Key papers to cite:
- Implementation details to add:
- Figures to create:
- Questions for advisor:

---

**END OF CHAPTER 4 TEMPLATE**
