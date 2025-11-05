# @lit-gap - Identify Research Gaps

Systematically identify research gaps and opportunities from literature review.

## Skill Type
**Category:** Literature Review
**Tier:** Core (Tier 1)
**Reusability:** Very High - every dissertation needs a gap

## What This Skill Does

1. Analyzes literature to find gaps
2. Categorizes gap types (theoretical, empirical, methodological)
3. Validates gap significance
4. Connects gaps to research questions
5. Justifies your dissertation contribution

## Invocation

```
@lit-gap [synthesis] [field]
```

## Types of Research Gaps

### 1. Knowledge Gap
**What's missing:** Basic understanding or information

**Example:**
> "While XAI methods exist for classification, their behavior in verification tasks (same/different judgments) remains unexplored."

### 2. Methodological Gap
**What's missing:** Better tools or approaches

**Example:**
> "Current XAI methods don't account for pairwise similarity metrics used in biometric verification."

### 3. Theoretical Gap
**What's missing:** Framework or theory

**Example:**
> "No formal framework exists to characterize explanation quality specific to biometric systems."

### 4. Empirical Gap
**What's missing:** Data or evidence

**Example:**
> "Cross-dataset validation of XAI methods for face recognition is rare (only 12% of studies)."

### 5. Population Gap
**What's missing:** Understudied groups

**Example:**
> "XAI evaluation focuses on majority demographics; cross-racial validation is absent in 85% of studies."

### 6. Application Gap
**What's missing:** Real-world use

**Example:**
> "Despite theoretical advances, deployment guidelines for biometric XAI in security systems don't exist."

## Input Format

### From Synthesis Matrix
```
@lit-gap

I've reviewed 52 papers on XAI for biometrics.

Key findings:
- 68% use only VGGFace2 dataset
- 86% lack theoretical grounding
- 27% report power analysis
- 5% do cross-racial evaluation

Identify significant gaps for my dissertation.
```

### From Literature Summary
```
@lit-gap

Literature summary:
[paste 3-5 paragraph summary of Chapter 2]

What gaps can I address in my dissertation?
```

### Specific Focus
```
@lit-gap

Focus: Explainable AI + biometric face recognition
Check for:
- Theoretical gaps
- Methodological gaps
- Empirical gaps
```

## Output Examples

### Example 1: Comprehensive Gap Analysis

**Input:**
```
@lit-gap

Field: XAI for biometric face recognition

Synthesis findings:
- 52 papers reviewed (2018-2024)
- Methods: GradCAM (45%), LIME (32%), SHAP (23%)
- Datasets: VGGFace2 (68%), LFW (41%), others (12%)
- Theory: 86% purely empirical, no formal frameworks
- Evaluation: Inconsistent metrics across studies
- Sample sizes: Median n=100, range 30-500
```

**Output:**

```markdown
## Research Gap Analysis: XAI for Biometric Face Recognition

### Gap 1: Theoretical Foundation ⭐⭐⭐ (High Priority)

**Type:** Theoretical Gap

**What's Missing:**
> "86% of studies are purely empirical with no theoretical framework for characterizing explanation quality in biometric contexts."

**Why It Matters:**
- Can't evaluate XAI methods systematically without theory
- Different studies use different metrics (no standardization)
- No principled way to design new biometric XAI methods

**Opportunity:**
Develop formal theoretical framework with provable properties.

**Potential Contribution:**
- Set of axioms/properties for biometric explanation quality
- Mathematical characterization of faithfulness
- Theoretical foundation for evaluation metrics

**Feasibility:** High (mathematical/theoretical work)

**Your Dissertation Could:**
- Propose falsifiable attribution framework
- Prove 6-8 theoretical properties
- Establish foundation for future work

---

### Gap 2: Dataset Concentration ⭐⭐ (Medium Priority)

**Type:** Empirical Gap

**What's Missing:**
> "68% of studies use only VGGFace2, limiting generalizability. Cross-dataset validation rare (12%)."

**Why It Matters:**
- Single-dataset evaluation risks overfitting
- Generalization claims unsupported
- Real-world deployment requires robustness

**Opportunity:**
Cross-dataset validation to test generalization.

**Potential Contribution:**
- Evaluate on multiple datasets (VGGFace2, LFW, CFP-FP, RFW)
- Compare performance across datasets
- Identify dataset-specific vs generalizable findings

**Feasibility:** High (datasets publicly available)

**Your Dissertation Could:**
- Test on 2+ datasets (VGGFace2 + LFW minimum)
- Report per-dataset and aggregated results
- Discuss generalization limitations

---

### Gap 3: Biometric-Specific Methods ⭐⭐⭐ (High Priority)

**Type:** Methodological Gap

**What's Missing:**
> "XAI methods designed for classification (GradCAM, LIME) don't account for biometric verification constraints (pairwise similarity, genuine/impostor distributions)."

**Why It Matters:**
- Verification ≠ classification (different task structure)
- Current methods ignore similarity metrics
- Explanations may not reflect actual verification logic

**Opportunity:**
Develop biometric-aware XAI method.

**Potential Contribution:**
- Modify GradCAM to incorporate verification constraints
- Integrate genuine/impostor similarity distributions
- Ensure explanations respect biometric decision boundary

**Feasibility:** Medium-High (requires method development + validation)

**Your Dissertation Could:**
- Propose BiometricGradCAM
- Integrate cosine similarity into attribution
- Validate on verification tasks

---

### Gap 4: Evaluation Consistency ⭐⭐ (Medium Priority)

**Type:** Methodological Gap

**What's Missing:**
> "No standardized evaluation protocol. Studies use different metrics:
> - Localization accuracy (59%)
> - Human agreement (32%)
> - Consistency (23%)
> - Faithfulness (18%)"

**Why It Matters:**
- Can't compare methods across studies
- Meta-analysis impossible
- Progress hard to measure

**Opportunity:**
Propose standardized evaluation framework.

**Potential Contribution:**
- Define core metrics for biometric XAI
- Validation protocol for face recognition
- Benchmark for future work

**Feasibility:** High (define + demonstrate in your work)

**Your Dissertation Could:**
- Use consistent metrics across all evaluations
- Report all standard metrics (localization, consistency, faithfulness)
- Provide benchmark code/datasets

---

### Gap 5: Small Sample Sizes ⭐ (Low Priority)

**Type:** Empirical Gap

**What's Missing:**
> "Median sample size n=100, range 30-500. Only 27% report power analysis."

**Why It Matters:**
- Underpowered studies risk false negatives
- Effect size estimates unreliable
- Replication crisis risk

**Opportunity:**
Conduct adequately powered study.

**Potential Contribution:**
- A priori power analysis
- Sample size n ≥ 200 per dataset
- Transparent reporting

**Feasibility:** High (use larger n)

**Your Dissertation Could:**
- Use n=200 per dataset (VGGFace2, LFW)
- Report power analysis in methods
- Provide effect sizes with confidence intervals

---

### Gap 6: Cross-Racial Evaluation ⭐ (Low Priority for Your Work)

**Type:** Population Gap

**What's Missing:**
> "Only 5% of studies evaluate XAI across racial demographics."

**Why It Matters:**
- Facial recognition has known racial biases
- XAI may also exhibit demographic differences
- Fairness/equity concerns

**Opportunity:**
Cross-racial XAI evaluation.

**Feasibility for You:** Low (requires specialized datasets: RFW, BFW)

**Recommendation:** Acknowledge as limitation, suggest for future work.

---

## Gap Prioritization for Your Dissertation

### High Priority (Address These)
1. **Theoretical Framework** - Core contribution
2. **Biometric-Specific Methods** - Methodological innovation
3. **Cross-Dataset Validation** - Empirical rigor

### Medium Priority (Nice to Have)
4. **Evaluation Standardization** - Propose framework
5. **Adequate Sample Sizes** - Use n=200+

### Low Priority (Future Work)
6. **Cross-Racial Evaluation** - Acknowledge limitation

---

## Justification for Your Dissertation

**Chapter 1 (Introduction) - Gap Statement:**

> "Despite significant advances in XAI for image classification,
> three critical gaps limit their application to biometric face
> verification systems:
>
> 1. **Theoretical Gap:** No formal framework characterizes
>    explanation quality specific to verification tasks (86%
>    of studies lack theory).
>
> 2. **Methodological Gap:** Current methods (GradCAM, LIME)
>    ignore biometric constraints like pairwise similarity,
>    potentially producing misleading explanations.
>
> 3. **Empirical Gap:** Cross-dataset validation is rare
>    (12% of studies), limiting generalizability claims.
>
> This dissertation addresses these gaps through: (1) a
> falsifiable attribution framework with formal properties,
> (2) BiometricGradCAM method integrating verification
> constraints, and (3) cross-dataset validation on VGGFace2
> and LFW (n=200 each)."

**Chapter 2 (Literature Review) - Gap Table:**

| Gap Type | Specific Gap | % Studies | This Dissertation |
|----------|-------------|-----------|-------------------|
| Theoretical | No formal framework | 86% | ✅ Falsifiable framework |
| Methodological | No biometric constraints | 100% | ✅ BiometricGradCAM |
| Empirical | Single dataset only | 88% | ✅ VGGFace2 + LFW |
| Empirical | Small samples (n<100) | 55% | ✅ n=200 per dataset |
| Empirical | No power analysis | 73% | ✅ A priori power |

**Chapter 7 (Discussion) - Gap Contribution:**

> "This work fills three critical gaps: ... (1) provides the
> first formal theoretical framework for biometric XAI, (2)
> demonstrates that biometric-aware methods outperform standard
> approaches, and (3) validates findings across datasets..."
```

### Example 2: Quick Gap Identification

**Input:**
```
@lit-gap

I've read 15 papers on GradCAM for biometrics.
All use classification tasks, none use verification.
What's the gap?
```

**Output:**

```markdown
## Gap Identified: Task Mismatch

### Type: Methodological + Knowledge Gap

**What's Missing:**
> "GradCAM has been extensively studied for classification
> (identifying whose face), but verification (same/different
> judgment) remains unexplored in your 15-paper sample."

**Why This is a Gap:**
1. **Different task structure:**
   - Classification: f(x) → class label
   - Verification: f(x₁, x₂) → similarity score

2. **Different decision processes:**
   - Classification: Which features identify this person?
   - Verification: Which features make these faces similar/dissimilar?

3. **Different evaluation criteria:**
   - Classification: Localize identity-specific features
   - Verification: Localize similarity-relevant regions

**Is This a Significant Gap?**
✅ **Yes**, because:
- Most deployed biometric systems use verification, not classification
- Explanations for "why same identity" differ from "which identity"
- Security applications need verification explanations

**Your Opportunity:**
First study to apply and evaluate GradCAM for face verification.

**Potential Contribution:**
- Adapt GradCAM for verification task
- Define evaluation metrics for verification XAI
- Compare verification vs classification explanations

**Feasibility:** High
- GradCAM code available
- Verification datasets public (LFW pairs, VGGFace2)
- Clear experimental design

**For Your Dissertation:**
> "While GradCAM has been extensively applied to face
> classification (Smith et al., 2023; Jones et al., 2022;
> 15 studies reviewed), its application to face verification
> tasks remains unexplored. This represents a significant
> gap because verification (not classification) is the
> predominant task in deployed biometric systems (ISO/IEC
> 29794-1:2016)."
```

## Gap Validation Criteria

A gap is significant if it meets **3+ criteria:**

✅ **Not trivial** - Requires substantial work to address
✅ **Feasible** - Can be addressed within PhD timeline/resources
✅ **Novel** - Not already extensively studied
✅ **Important** - Matters to field, not just academic exercise
✅ **Specific** - Clear what's missing and what would fill it
✅ **Connected** - Links to your research questions

## Common Mistakes

### ❌ Mistake 1: Gap = "No one did exactly my study"
That's always true. Need meaningful gap.

### ❌ Mistake 2: Gap too small
"Only 2 papers studied X" - Maybe X doesn't matter?

### ❌ Mistake 3: Gap too large
"We don't understand consciousness" - Can't solve in PhD.

### ❌ Mistake 4: Unfeasible gap
"No one has studied 1 million faces" - You can't either.

### ✅ Good Gap:
"XAI methods for classification don't account for verification constraints - I'll develop biometric-aware method."

## Integration with Dissertation

### Chapter 1 (Introduction)
Present 1-3 main gaps that motivate your work.

### Chapter 2 (Literature Review)
End with detailed gap analysis (2-3 pages).

### Chapter 3+ (Methods/Results)
Show how you address each gap.

### Chapter 7 (Discussion)
Return to gaps, explain how you filled them.

## Time Savings

**Manual gap identification:** 4-6 hours (reviewing notes, finding patterns)
**Using @lit-gap:** 30-45 minutes
**Saved:** ~4 hours 🎉

## Best Practices

### 1. Be Specific
"Little research exists" → "Only 3 of 52 studies (6%) examined..."

### 2. Show Significance
Why does this gap matter? What's the impact?

### 3. Demonstrate Feasibility
Could you actually fill this gap? With what resources?

### 4. Connect to RQs
Each gap should link to a research question.

### 5. Cite Evidence
"Gap exists" claims need evidence from synthesis.

## Related Skills

- `@synthesis-matrix` - Organize literature to spot patterns
- `/run-literature-search` - Ensure comprehensive coverage
- `@research-questions` - Gaps inform research questions
- `/screen-papers` - Include all relevant work

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 30-45 minutes
**Time saved:** ~4 hours
**Reusability:** Very High (every dissertation)
**Critical for:** Justifying your contribution (Chapter 1, 2, 7)
