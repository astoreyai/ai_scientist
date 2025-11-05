# @abstract-writer - Draft Academic Abstracts

Generate structured, publication-quality abstracts for papers, dissertations, and proposals.

## Skill Type
**Category:** Writing
**Tier:** Core (Tier 1)
**Reusability:** Very High - every paper needs an abstract

## What This Skill Does

1. Generates structured abstracts from research summary
2. Follows journal/conference formatting requirements
3. Stays within word limits (150-300 words typical)
4. Includes all required elements
5. Optimizes for clarity and impact

## Invocation

```
@abstract-writer [type] [word-limit] [content]
```

## Abstract Types

### 1. Structured Abstract
**Used in:** Medical journals, some science journals

**Structure:**
- **Background:** Context and motivation
- **Methods:** What you did
- **Results:** What you found
- **Conclusions:** What it means

### 2. Unstructured Abstract
**Used in:** Most CS/engineering journals, conferences

**Structure:**
- Single paragraph
- Flows: Context → Gap → Contribution → Results → Impact

### 3. Dissertation Abstract
**Used in:** PhD dissertations

**Structure:**
- Research problem
- Methodology
- Key findings
- Contributions
- Implications

## Input Format

### Minimal Input
```
@abstract-writer structured 250

My research is about explainable AI for face recognition.
I developed a new method called X.
I tested it on 2 datasets.
Results show 15% improvement.
```

### Detailed Input
```json
{
  "type": "structured",
  "limit": 300,
  "background": "Current XAI methods for biometrics lack...",
  "methods": "We propose a novel framework...",
  "results": "Experiments on VGGFace2 and LFW show...",
  "conclusions": "This work demonstrates..."
}
```

## Output Examples

### Example 1: Conference Paper (Unstructured)

**Input:**
```
@abstract-writer unstructured 250

Topic: Explainable AI for face recognition
Problem: Current methods don't account for biometric constraints
Solution: New framework called BiometricGradCAM
Datasets: VGGFace2, LFW (n=200 pairs each)
Results: 15% better localization, maintains 99% accuracy
Impact: Enables trustworthy biometric systems
```

**Output:**
```
Explainable AI (XAI) methods for face recognition systems often fail
to account for biometric-specific constraints, leading to explanations
that may not reflect the true decision-making process. We introduce
BiometricGradCAM, a novel framework that incorporates biometric
verification constraints into gradient-based attribution methods.
Our approach generates explanations that are both faithful to the
model's decisions and aligned with biometric similarity metrics.
Experiments on VGGFace2 and LFW datasets (n=200 verification pairs
each) demonstrate that BiometricGradCAM achieves 15% better
localization accuracy compared to standard GradCAM while maintaining
99% face verification accuracy. This work enables more trustworthy
deployment of AI-based biometric systems by providing interpretable
explanations that respect biometric constraints.

[248 words]
```

### Example 2: Journal Paper (Structured)

**Input:**
```
@abstract-writer structured 300

Background: Biometric systems need explainability for trust
Methods: Proposed falsifiable attribution framework, tested on 2 datasets
Results: 8 theoretical properties proved, experiments validate framework
Conclusions: Provides rigorous foundation for biometric XAI
```

**Output:**
```
Background: Biometric authentication systems increasingly rely on
deep learning, yet their decision-making processes remain opaque.
Current explainable AI (XAI) methods lack rigorous theoretical
foundations specific to biometric constraints, limiting their
trustworthiness in security-critical applications.

Methods: We propose a falsifiable attribution framework for
biometric face recognition that integrates verification constraints
into explanation generation. The framework consists of eight
theoretical properties governing explanation quality, attribution
consistency, and biometric faithfulness. We validate the framework
through experiments on VGGFace2 and LFW datasets using multiple
XAI methods.

Results: All eight theoretical properties are formally proved and
empirically validated across 400 face verification pairs. The
framework successfully identifies explanation inconsistencies in
three out of four tested XAI methods, with BiometricGradCAM
achieving the highest consistency score (0.92) and attribution
quality (0.87).

Conclusions: The falsifiable attribution framework provides the
first rigorous theoretical foundation for evaluating XAI methods
in biometric systems, enabling more trustworthy deployment of
AI-based authentication.

[169 words]
```

### Example 3: PhD Dissertation

**Input:**
```
@abstract-writer dissertation 350

Research problem: Need rigorous XAI for biometrics
Contributions: (1) Theoretical framework, (2) Novel method, (3) Evaluation protocol
Methodology: Mathematical proofs + empirical validation
Findings: 8 theorems proved, 2 datasets tested, new method outperforms baselines
Impact: Enables trustworthy biometric AI systems
```

**Output:**
```
This dissertation addresses the critical need for rigorous explainable
AI (XAI) methods in biometric face recognition systems. While deep
learning has achieved remarkable accuracy in biometrics, the lack of
interpretability hinders trust and limits deployment in security-critical
applications. Existing XAI approaches fail to account for biometric-specific
constraints, resulting in explanations that may misrepresent the model's
true decision-making process.

The research makes three primary contributions: (1) a falsifiable
attribution framework establishing eight theoretical properties for
biometric explanation quality, (2) BiometricGradCAM, a novel XAI method
incorporating verification constraints, and (3) a comprehensive evaluation
protocol for assessing explanation faithfulness in biometric contexts.

The methodology combines mathematical rigor with empirical validation.
Eight theorems formally characterize explanation requirements for
biometric systems, proved using measure theory and information geometry.
Experimental validation on VGGFace2 and LFW datasets (400 verification
pairs total) demonstrates that BiometricGradCAM achieves 15% better
localization accuracy and 12% higher consistency compared to standard
methods while maintaining 99% verification accuracy.

This work provides the first rigorous theoretical foundation for XAI
in biometrics, enabling trustworthy deployment of AI-based authentication
systems with interpretable, verifiable explanations.

[198 words]
```

## Required Elements

### All Abstracts Must Include
- ✅ Problem/motivation (why)
- ✅ Approach/methods (how)
- ✅ Results (what)
- ✅ Significance (impact)

### Good Abstracts Also Have
- ✅ Specific numbers (quantitative results)
- ✅ Clear contribution statement
- ✅ Context (1-2 sentences)
- ✅ No citations (usually)
- ✅ Keywords implicit

## Word Limits by Venue

| Venue Type | Typical Limit | Notes |
|------------|---------------|-------|
| Conference paper | 150-250 words | ACM, IEEE |
| Journal article | 200-300 words | Elsevier, Springer |
| PhD dissertation | 300-350 words | University specific |
| Grant proposal | 200-500 words | NSF, NIH |
| Extended abstract | 1000-1500 words | Workshops |

## Quality Checks

The skill validates:
- ✅ Word count within limit
- ✅ All required elements present
- ✅ No vague language ("novel", "significant")
- ✅ Specific, quantitative results
- ✅ Clear contribution
- ✅ Proper tense usage
- ✅ No citations (unless required)

## Common Fixes

### Too Vague
**Before:**
```
We propose a novel method that significantly improves results.
```

**After:**
```
We propose BiometricGradCAM, achieving 15% better localization
accuracy (p < 0.001) on VGGFace2 dataset.
```

### Missing Results
**Before:**
```
We evaluated our method on standard datasets.
```

**After:**
```
Experiments on VGGFace2 (n=200) and LFW (n=200) show 15%
improvement in localization accuracy and 99% verification accuracy.
```

### Too Long
**Before:** 312 words
**After:** Trim to 250 by:
- Remove redundant phrases
- Combine sentences
- Cut less critical details
- Use precise language

## Tense Usage

### Present Tense
- Established facts
- Paper organization

**Example:** "Biometric systems require interpretability."

### Past Tense
- What you did
- Your experiments

**Example:** "We evaluated the framework on two datasets."

### Present Perfect
- Recent work
- Ongoing relevance

**Example:** "Previous work has addressed..."

## Writing Tips

### Strong Opening
❌ "This paper presents..."
✅ "Biometric systems lack interpretability, limiting trust..."

### Specific Numbers
❌ "Significant improvement"
✅ "15% improvement (p < 0.001, n=200)"

### Active Voice
❌ "The method was evaluated..."
✅ "We evaluated the method..."

### Concise Language
❌ "In order to address the issue of..."
✅ "To address..."

## Keywords Integration

Good abstracts naturally include keywords:
- Research area (biometrics, XAI)
- Methods (GradCAM, attribution)
- Datasets (VGGFace2, LFW)
- Metrics (accuracy, EER)

## Field-Specific Patterns

### Computer Science
- Emphasize: Algorithm, efficiency, novelty
- Include: Dataset sizes, performance metrics
- Typical length: 150-250 words

### Engineering
- Emphasize: Practical application, validation
- Include: Specifications, test conditions
- Typical length: 200-300 words

### Social Sciences
- Emphasize: Theory, implications
- Include: Sample characteristics, findings
- Typical length: 200-300 words

## Time Savings

**Manual writing:** 2-4 hours (multiple drafts)
**Using @abstract-writer:** 15-30 minutes (with refinement)
**Saved:** ~3 hours 🎉

## Best Practices

### 1. Write Last
Draft abstract after completing paper.

### 2. Iterate
Generate, refine, polish.

### 3. Get Feedback
Have advisor/colleagues review.

### 4. Check Requirements
Verify journal/conference format.

### 5. Be Specific
Numbers > adjectives.

## Integration Workflow

```
1. Complete paper/dissertation
2. Summarize key points
3. Use @abstract-writer to generate draft
4. Refine for specificity
5. Check word count
6. Verify all elements present
7. Proofread
8. Get feedback
9. Finalize
```

## Common Use Cases

### Conference Submission
```
@abstract-writer unstructured 250
[paste paper summary]
```

### Journal Article
```
@abstract-writer structured 300
[paste background, methods, results, conclusions]
```

### Dissertation
```
@abstract-writer dissertation 350
[paste research summary]
```

## Related Skills

- `@keywords-develop` - Generate keywords
- `@contribution-writer` - Articulate contributions
- `@academic-grammar` - Polish language

## Quality Checklist

Before submitting:
- [ ] Word count within limit
- [ ] All required elements present
- [ ] Specific, quantitative results
- [ ] Clear contribution stated
- [ ] No vague language
- [ ] Proper tense usage
- [ ] No typos
- [ ] Reads smoothly

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 15-30 minutes
**Time saved:** ~3 hours
**Reusability:** Very High (every paper/dissertation)
