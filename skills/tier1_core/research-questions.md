# @research-questions - Formulate Research Questions

Develop clear, answerable, and rigorous research questions for your dissertation.

## Skill Type
**Category:** Topic Development / Planning
**Tier:** Core (Tier 1)
**Reusability:** Very High - every dissertation needs research questions

## What This Skill Does

1. Transforms broad topics into specific research questions
2. Ensures questions are answerable and rigorous
3. Aligns questions with methodology
4. Validates feasibility
5. Structures questions hierarchically (main + sub-questions)

## Invocation

```
@research-questions [topic] [context]
```

## Research Question Types

### 1. Descriptive Questions
**Ask:** What is X? How does X work? What are the characteristics of X?

**Example:**
> "What are the current explainability methods for biometric face recognition systems?"

**When to use:** Literature review, establishing baseline knowledge

### 2. Comparative Questions
**Ask:** How does X compare to Y? What are the differences between X and Y?

**Example:**
> "How does BiometricGradCAM compare to standard GradCAM in terms of localization accuracy for face verification tasks?"

**When to use:** When you have multiple methods/conditions to compare

### 3. Relationship Questions
**Ask:** What is the relationship between X and Y? Does X influence Y?

**Example:**
> "What is the relationship between explanation consistency and verification accuracy in biometric systems?"

**When to use:** Exploring correlations, associations, dependencies

### 4. Causal Questions
**Ask:** Does X cause Y? What effect does X have on Y?

**Example:**
> "Does incorporating biometric constraints into XAI methods improve explanation faithfulness?"

**When to use:** Experimental studies with controlled manipulations

### 5. Theoretical Questions
**Ask:** Why does X happen? What framework explains X?

**Example:**
> "What theoretical framework characterizes explanation quality in biometric verification systems?"

**When to use:** Developing new theory, establishing theoretical foundations

## FINER Criteria

Good research questions are **FINER:**

- **F**easible - Can you actually answer it with available resources?
- **I**nteresting - Does it matter to the field?
- **N**ovel - Has it not been definitively answered?
- **E**thical - Can it be studied ethically?
- **R**elevant - Does it advance knowledge/practice?

## Input Format

### Broad Topic
```
@research-questions

Topic: Explainable AI for face recognition
I'm interested in making biometric systems more trustworthy through better explanations.
```

### With Context
```
@research-questions

Topic: XAI for biometrics
Gap: Current XAI methods don't account for biometric constraints
Resources: Access to VGGFace2, LFW datasets (n=200 each)
Timeline: 2 years
Contribution goal: Theoretical + empirical
```

### Refinement
```
@research-questions

Current question: "How can we make XAI better for face recognition?"

This is too vague. Help me refine it.
```

## Output Examples

### Example 1: From Broad Topic to Specific Questions

**Input:**
```
@research-questions

Broad topic: I want to work on explainable AI for biometric systems.
I have access to VGGFace2 and LFW datasets.
Timeline: 2-3 years for PhD
```

**Output:**

```markdown
## Research Question Development: XAI for Biometric Systems

### Step 1: Identify the Gap

**Current state:** XAI methods (GradCAM, LIME, etc.) exist for image classification.

**Gap:** These methods don't account for biometric-specific requirements:
- Verification vs classification task
- Similarity metrics
- Consistency across identity

**Opportunity:** Develop biometric-aware XAI methods

---

### Step 2: Formulate Main Research Question

**Main RQ:**
> "How can explainable AI methods be adapted to provide faithful, consistent explanations for biometric face verification systems?"

**FINER Check:**
- ✅ **Feasible:** Yes - VGGFace2/LFW available, methods exist to extend
- ✅ **Interesting:** Yes - biometric security is high-stakes domain
- ✅ **Novel:** Yes - gap in accounting for biometric constraints
- ✅ **Ethical:** Yes - using public datasets, improving trust/transparency
- ✅ **Relevant:** Yes - biometric systems widely deployed, need trust

---

### Step 3: Break Down into Sub-Questions

**RQ1 (Theoretical):**
> "What properties must explanation methods satisfy to be faithful to biometric verification decisions?"

- Addresses: Theoretical foundation
- Methodology: Mathematical analysis, proof
- Deliverable: Formal framework (Chapter 3)

**RQ2 (Empirical - Method Development):**
> "Can incorporating verification constraints into gradient-based attribution improve explanation quality for face recognition?"

- Addresses: Develop new method (BiometricGradCAM)
- Methodology: Algorithm design, implementation
- Deliverable: Novel XAI method (Chapter 4-5)

**RQ3 (Empirical - Evaluation):**
> "How do biometric-aware XAI methods compare to standard XAI methods in terms of localization accuracy and consistency?"

- Addresses: Validation of proposed method
- Methodology: Experiments on VGGFace2 + LFW (n=200 each)
- Deliverable: Quantitative evaluation (Chapter 6)

**RQ4 (Empirical - Generalization):**
> "Do the findings generalize across different datasets and face verification models?"

- Addresses: External validity
- Methodology: Cross-dataset validation (VGGFace2 vs LFW)
- Deliverable: Robustness analysis (Chapter 6)

---

### Step 4: Map to Dissertation Structure

| Research Question | Chapter | Contribution Type | Time Est. |
|-------------------|---------|-------------------|-----------|
| RQ1: Properties | Ch 3-4 | Theoretical (8 theorems) | 6 months |
| RQ2: Method | Ch 4-5 | Methodological (BiometricGradCAM) | 4 months |
| RQ3: Evaluation | Ch 6 | Empirical (experiments) | 6 months |
| RQ4: Generalization | Ch 6 | Empirical (cross-validation) | 3 months |

Total: ~19 months (leaves buffer for writing/revision)

---

### Step 5: Feasibility Check

**Resources Required:**
- ✅ Datasets: VGGFace2, LFW (publicly available)
- ✅ Compute: GPU for face recognition model (available)
- ✅ Software: Python, PyTorch (open source)
- ✅ Expertise: XAI, deep learning (can acquire)

**Risks:**
- ⚠️ Theoretical work (RQ1) might take longer than 6 months
- ⚠️ Need validation that n=200 has adequate power

**Mitigation:**
- Start theoretical work early (Year 1)
- Run power analysis before data collection

---

### Final Research Questions (For Proposal/Defense)

**Overarching Question:**
> How can explainable AI methods be adapted to provide faithful, consistent explanations for biometric face verification systems?

**Specific Questions:**

1. **RQ1 (Theoretical):** What formal properties characterize explanation quality in biometric verification systems?

2. **RQ2 (Methodological):** Can biometric constraints be integrated into gradient-based attribution methods to improve explanation faithfulness?

3. **RQ3 (Empirical):** How do biometric-aware XAI methods compare to standard methods in localization accuracy and consistency?

4. **RQ4 (Generalization):** Do these findings generalize across datasets and face verification architectures?

**Expected Contributions:**
- Theoretical framework (8 formal properties)
- Novel XAI method (BiometricGradCAM)
- Empirical validation (2 datasets, 400 pairs total)
- Practical guidelines for biometric XAI deployment
```

### Example 2: Refining Vague Questions

**Input:**
```
@research-questions

My current question: "How can we improve biometric systems?"

My advisor says this is too broad. Help me refine it.
```

**Output:**

```markdown
## Refining Research Question: Biometric Systems

### ❌ Original Question
> "How can we improve biometric systems?"

**Problems:**
1. Too broad - "improve" in what way? (accuracy, speed, fairness, trust?)
2. Not specific - which biometric modality? (face, fingerprint, iris?)
3. Not answerable - infinite ways to "improve"
4. No clear methodology
5. Not novel - everything "improves" systems

---

### ✅ Refinement Process

**Step 1: Specify the domain**
- Biometric modality: Face recognition
- Specific aspect: Explainability/interpretability
- Context: Verification (not identification)

**Step 2: Identify the problem**
- What's wrong with current systems? Lack of trust due to opacity
- What gap exists? XAI methods don't account for biometric constraints

**Step 3: Define "improve"**
- Improve what metric? Explanation faithfulness, consistency
- How to measure? Localization accuracy, attribution consistency

**Step 4: Consider feasibility**
- What data? VGGFace2, LFW (public)
- What timeline? 2-3 years
- What skills? Machine learning, XAI methods

---

### ✅ Refined Question Options

**Option A (Focused on Method):**
> "Can incorporating biometric verification constraints into GradCAM improve explanation faithfulness for face recognition systems?"

- ✅ Specific: GradCAM method, verification constraints
- ✅ Answerable: Yes/no with quantitative evidence
- ✅ Novel: Current GradCAM doesn't use verification constraints
- ✅ Feasible: Implementable modification

**Option B (Focused on Evaluation):**
> "How do explanation consistency and localization accuracy differ between standard and biometric-aware XAI methods for face verification?"

- ✅ Comparative structure
- ✅ Clear metrics (consistency, localization accuracy)
- ✅ Specific task (face verification)
- ✅ Answerable through experiments

**Option C (Focused on Theory):**
> "What formal properties must XAI methods satisfy to provide faithful explanations for biometric face verification decisions?"

- ✅ Theoretical contribution
- ✅ Establishes foundation for evaluation
- ✅ Novel framework
- ✅ Provable with mathematical analysis

---

### Recommendation

Use **multi-level structure:**

**Main Question (Option B):**
How do biometric-aware XAI methods compare to standard methods for face verification?

**Sub-Questions:**
1. What properties should biometric XAI methods satisfy? (Theory - Option C)
2. Can GradCAM be modified for biometric verification? (Method - Option A)
3. How do methods compare empirically? (Evaluation - Option B)

This gives you:
- Clear overarching question
- Theoretical depth (RQ1)
- Methodological contribution (RQ2)
- Empirical validation (RQ3)
```

### Example 3: Alignment with Methodology

**Input:**
```
@research-questions

Check if my research questions align with my planned methodology.

RQ: "Why do deep learning models misclassify certain face identities?"
Methodology: Quantitative experiments on VGGFace2 (n=200)
```

**Output:**

```markdown
## Research Question - Methodology Alignment Check

### ⚠️ **Misalignment Detected**

**Your RQ:** "Why do deep learning models misclassify certain face identities?"

**Your Methodology:** Quantitative experiments (n=200)

**Problem:** Question asks "why" (causal/mechanistic) but methodology is quantitative/correlational.

---

### Alignment Analysis

| Aspect | RQ Implies | Methodology Provides | Aligned? |
|--------|-----------|---------------------|----------|
| **Type** | Causal ("why") | Descriptive/comparative | ❌ |
| **Depth** | Mechanistic understanding | Quantitative metrics | ❌ |
| **Approach** | Qualitative/interpretive | Quantitative/statistical | ❌ |
| **Sample** | In-depth case studies | Large-scale patterns | ❌ |

---

### Option 1: Revise Question to Match Methodology

**Revised RQ:**
> "What face attributes are associated with higher misclassification rates in deep learning face recognition models?"

**Why this works:**
- ✅ "What" question (descriptive) matches quantitative approach
- ✅ Can be answered with n=200 experiments
- ✅ Statistical analysis appropriate
- ✅ Clear measurable outcome

**Methodology:**
1. Run face recognition on n=200 pairs
2. Identify misclassifications
3. Analyze attributes (age, pose, lighting, etc.)
4. Statistical tests (chi-square, logistic regression)

---

### Option 2: Revise Methodology to Match Question

**Keep RQ:** "Why do deep learning models misclassify certain face identities?"

**Revised Methodology:**
- Mixed methods approach
- Quantitative: n=200 pairs (identify misclassification patterns)
- Qualitative: Deep dive into 10-20 cases
- Mechanistic: Ablation studies, activation analysis
- Theoretical: Develop causal model

**Why this works:**
- ✅ "Why" questions need mechanistic investigation
- ✅ Combines pattern detection with deep analysis
- ✅ Triangulation of evidence

---

### Recommendation

**For PhD dissertation timeline (2-3 years):**

Choose **Option 1** (revise question to match methodology):

**Main RQ:**
> "What face attributes and conditions are associated with misclassification in deep learning face recognition?"

**Sub-RQs:**
1. Which face attributes (age, pose, lighting) correlate with errors?
2. How do misclassification patterns differ across datasets?
3. Can we predict misclassification likelihood from image attributes?

**This is:**
- ✅ Answerable with planned methodology
- ✅ Feasible within timeline
- ✅ Contributory (empirical patterns)
- ✅ Publishable (clear metrics, results)
```

## Question Quality Checklist

### ✅ Good Research Question
- [ ] **Specific:** Not vague or overly broad
- [ ] **Answerable:** Can be addressed with available methods
- [ ] **Focused:** Single clear focus (not 3 questions in one)
- [ ] **Complex:** Not answerable with yes/no
- [ ] **Novel:** Hasn't been definitively answered
- [ ] **Feasible:** Resources available (data, time, expertise)
- [ ] **Aligned:** Matches your planned methodology
- [ ] **Relevant:** Matters to the field
- [ ] **Ethical:** Can be studied without harm

### ❌ Poor Research Question
- [ ] Too broad ("How can we improve X?")
- [ ] Too narrow ("What is the mean age in this dataset?")
- [ ] Vague ("What is the impact of Y?")
- [ ] Multiple questions in one
- [ ] Already definitively answered
- [ ] Requires unavailable resources
- [ ] Purely descriptive (for PhD - needs insight)

## Common Patterns

### Pattern 1: The "Too Broad" Question
**Original:** "How does AI impact society?"

**Refined:** "How does facial recognition deployment in airports affect traveler privacy perceptions?"

---

### Pattern 2: The "Hidden Multiple" Question
**Original:** "What are the effects of XAI on user trust, decision quality, and system adoption?"

**Refined:** Split into 3 separate sub-questions under main RQ

---

### Pattern 3: The "Obvious Answer" Question
**Original:** "Is more data better for training models?"

**Refined:** "What is the relationship between training data size and model fairness across demographic groups?"

## Time Savings

**Manual development:** 4-8 hours (multiple advisor meetings, iterations)
**Using @research-questions:** 30-60 minutes
**Saved:** ~5 hours 🎉

## Best Practices

### 1. Start Broad, Refine Iteratively
Don't expect perfection on first try.

### 2. Check FINER Criteria
Every question must pass all five criteria.

### 3. Align with Methodology
Question type must match planned methods.

### 4. Get Feedback Early
Share with advisor before committing.

### 5. Revisit During Research
Questions may evolve as you learn more.

## Integration with Dissertation

### Chapter 1 (Introduction)
State research questions clearly:
> "This dissertation addresses three research questions:
>
> RQ1: [Theoretical question]
> RQ2: [Methodological question]
> RQ3: [Empirical question]"

### Chapter 3-6 (Body Chapters)
Structure around RQs:
- Chapter 3: Addresses RQ1
- Chapter 4-5: Addresses RQ2
- Chapter 6: Addresses RQ3

### Chapter 7 (Discussion)
Revisit RQs:
> "Returning to our research questions:
>
> RQ1 was addressed through... We found that...
> RQ2 was addressed through... Results show...
> RQ3 was addressed through... Evidence suggests..."

## Related Skills

- `@lit-gap` - Identify research gaps (feeds into RQs)
- `@power-analysis` - Ensure RQs are answerable with available n
- `@experiment-design` - Design studies to answer RQs
- `@hypothesis-test` - Convert RQs to testable hypotheses

## Field-Specific Notes

### STEM/Engineering
- Focus on measurable outcomes
- Clear independent/dependent variables
- Often comparative or causal questions

### Social Sciences
- May include exploratory questions
- Mixed methods common
- Theory-testing questions important

### Humanities
- Interpretive questions acceptable
- "How" and "Why" questions common
- Focus on meaning, context

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 30-60 minutes
**Time saved:** ~5 hours
**Reusability:** Very High (every dissertation)
**Critical for:** Proposal, defense, Chapter 1
