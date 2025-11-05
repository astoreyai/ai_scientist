# Chapter 7: Discussion

## Overview

This chapter interprets your results, discusses their implications, addresses limitations, and answers your research questions. The key difference from Chapter 6 (Results):
- **Chapter 6:** "What did we observe?" (objective reporting)
- **Chapter 7:** "What does it mean?" (interpretation and implications)

**Target Length:** 9,000-12,000 words

**Important:** This is where you demonstrate critical thinking. Don't just repeat results—explain why you observed what you did, what it means for theory and practice, and what the limitations are.

---

## 7.1 Introduction

**Purpose:** Orient readers to what will be discussed and how this chapter is organized.

**What to Include:**
- Brief recap of main findings (1-2 paragraphs)
- Preview of discussion topics
- Organization of the chapter

**Writing Template:**

```markdown
## 7.1 Introduction

[RECAP OF FINDINGS]
In Chapter 6, we evaluated [SYSTEM NAME] on [DATASETS] to answer [N] research questions. Our key findings were:
- **RQ1:** [Brief summary of result]
- **RQ2:** [Brief summary of result]
- **RQ3:** [Brief summary of result]

[PURPOSE OF DISCUSSION]
In this chapter, we interpret these results and discuss their implications. We address:
- What these results mean and why we observed them (Section 7.2)
- How our findings compare to prior work (Section 7.3)
- Theoretical implications (Section 7.4)
- Practical implications (Section 7.5)
- Limitations of our work (Section 7.6)
- Threats to validity (Section 7.7)

[THESIS STATEMENT - optional but powerful]
Our findings suggest that [KEY TAKEAWAY MESSAGE]. This has important implications for [FIELD/COMMUNITY].
```

**Example:**

> In Chapter 6, we evaluated FastSHAP-ViT on LFW and FairFace datasets to answer three research questions about real-time explainability, architectural integration, and demographic fairness. Our key findings were:
> - **RQ1 (Computational Optimization):** FastSHAP-ViT achieves 58ms latency with 0.76 insertion AUC, meeting our <50ms and >0.7 targets
> - **RQ2 (Architectural Integration):** E-ViT with E-MHA maintains 99.2% accuracy on LFW, matching baseline ViT performance
> - **RQ3 (Demographic Fairness):** Calibration reduces explanation variance from 24% to 8.7% across seven demographic groups
>
> In this chapter, we interpret these results and discuss their implications. We address: what these results mean and why we observed them (Section 7.2), how our findings compare to prior work (Section 7.3), theoretical implications (Section 7.4), practical implications (Section 7.5), limitations of our work (Section 7.6), and threats to validity (Section 7.7).
>
> Our findings suggest that real-time, fair, and theoretically-grounded explainability for vision transformers is achievable through hierarchical approximation and demographic calibration. This has important implications for deploying face recognition systems in regulated domains.

**Word Count Target:** 300-500 words

**📚 CITATION CHECK:**
- [ ] Results referenced from Chapter 6 are accurate
- [ ] Prior work mentioned in comparison is cited
- [ ] See [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md)

---

## 7.2 Interpretation of Results

**Purpose:** Explain what your results mean and why you observed what you did.

**Important Distinction:**
- **Results (Chapter 6):** "Accuracy was 99.2%"
- **Interpretation (Chapter 7):** "The 99.2% accuracy indicates that E-MHA does not degrade recognition performance because the sparse attention mechanism preserves discriminative features in the CLS token embedding"

**What to Include:**
- Overall interpretation (Section 7.2.0 - optional introductory subsection)
- Answer to each research question (Sections 7.2.1, 7.2.2, 7.2.3, ...)
- Mechanisms explaining observations
- Connections to theory (Chapter 3)

---

### 7.2.0 Overall Interpretation (Optional)

**Purpose:** Big-picture interpretation before diving into each RQ.

**Template:**

```markdown
### 7.2.0 Overall Interpretation

[WHAT DO RESULTS COLLECTIVELY MEAN?]
Taken together, our results demonstrate that [HIGH-LEVEL FINDING]. The [X%] improvement in [METRIC] compared to baselines indicates [INTERPRETATION]. This suggests [BROADER MEANING].

[WHY DID WE OBSERVE THIS?]
We attribute these results to [MECHANISM 1] and [MECHANISM 2]. Specifically:
- [MECHANISM 1]: [Explanation with evidence from Chapter 6]
- [MECHANISM 2]: [Explanation with evidence from Chapter 6]

[CONNECTION TO THEORY]
These findings align with the theoretical predictions from Chapter 3. Theorem 3.X predicted [PREDICTION], and our empirical results confirm this with [EVIDENCE].
```

**Example:**

> Taken together, our results demonstrate that hierarchical SHAP with demographic calibration achieves the "triple constraint" of real-time performance (<50ms), faithfulness (>0.7 insertion AUC), and fairness (<10% demographic variance). The 36× speedup over KernelSHAP while maintaining comparable faithfulness indicates that attention-guided sampling successfully reduces approximation error by focusing on high-importance coalitions.
>
> We attribute these results to two key mechanisms:
> 1. **Hierarchical Approximation:** By organizing features into a binary tree and sampling K coalitions per level (not K for the entire space), we reduce both computational cost and variance. The O(M log M) complexity (vs. O(2^M) for exact SHAP) makes real-time computation feasible.
> 2. **Demographic Calibration:** Statistical bias correction reduces systematic differences in attribution magnitudes across demographic groups while preserving relative rankings. This addresses the inherent bias in ViT attention (center-focused) that disproportionately attributes importance to central facial features.
>
> These findings align with the theoretical predictions from Chapter 3. Theorem 3.3 predicted O(M log M) complexity with O(1/√K) approximation error, and our empirical results confirm this: complexity scales log-linearly with M (Figure 6.2), and error decreases as 1/√K (Figure 6.3).

**Word Count:** 400-700 words

---

### 7.2.1 RQ1: [Research Question 1]

**Purpose:** Directly answer the first research question based on results.

**Structure:**
1. Restate the research question
2. Direct answer (yes/no or quantitative result)
3. Evidence from results (cite Chapter 6 sections/tables/figures)
4. Interpretation beyond surface findings
5. Connection to theory or methodology

**Template:**

```markdown
### 7.2.1 RQ1: [Restate Research Question]

**Research Question:**
[FULL TEXT OF RQ1 from Chapter 1]

**Answer:**
[DIRECT, CLEAR ANSWER - yes/no or quantitative result with specifics]

**Evidence:**
Our results (Section 6.X) show:
- [METRIC 1]: [Value] (Table 6.Y)
- [METRIC 2]: [Value] (Figure 6.Z)
- [COMPARISON]: [Our method vs. baseline, with % difference]

[CITE SPECIFIC RESULTS]
In Table 6.Y, we observe that [SPECIFIC OBSERVATION]. Figure 6.Z demonstrates [SPECIFIC PATTERN].

**Interpretation:**

*What does this mean?*
The [RESULT] indicates [INTERPRETATION]. This is significant because [WHY IT MATTERS].

*Why did we observe this?*
We attribute this outcome to [MECHANISM/REASON]. Specifically:
1. **[Factor 1]:** [Explanation]
2. **[Factor 2]:** [Explanation]

*How does it connect to theory?*
This finding validates Theorem 3.X from Chapter 3, which predicted [PREDICTION]. Our empirical result ([VALUE]) closely matches the theoretical bound ([VALUE]).

*Unexpected aspects:*
[IF APPLICABLE: Discuss any surprising findings or deviations from expectations]
```

**Example:**

```markdown
### 7.2.1 RQ1: Computational Optimization

**Research Question:**
Can hierarchical SHAP with GPU acceleration reduce complexity from O(2^M) to O(M log M) while maintaining faithfulness >0.7 (insertion AUC)?

**Answer:**
Yes. Hierarchical SHAP achieves O(M log M) complexity with 58ms latency (M=8 features, K=100 samples) and maintains 0.76 insertion AUC, exceeding our 0.7 target.

**Evidence:**
Our results (Section 6.2) show:
- **Latency:** 58ms per explanation (Table 6.1)
- **Faithfulness:** 0.76 insertion AUC (Table 6.2)
- **Speedup:** 36× faster than KernelSHAP (2,100ms → 58ms)

In Table 6.1, we observe that latency scales log-linearly with M (log-log slope = 0.98, close to theoretical 1.0). Figure 6.2 demonstrates that insertion AUC remains stable (0.74-0.78) across different feature counts (M = 4, 8, 16, 32).

**Interpretation:**

*What does this mean?*
The 58ms latency indicates that real-time explainability (<50ms strict, <100ms acceptable) is achievable for production face recognition systems. The 0.76 insertion AUC demonstrates that approximate Shapley values are sufficiently faithful—users can trust that highly-attributed features genuinely contribute to predictions.

*Why did we observe this?*
We attribute this outcome to three factors:
1. **Hierarchical Sampling:** By sampling K coalitions per level (not per feature), we reduce the total evaluations from O(K·M) (KernelSHAP) to O(K·log M) (ours). For M=8, log M ≈ 3, yielding 3× fewer evaluations.
2. **Attention-Guided Sampling:** Using ViT attention weights to bias coalition sampling reduces variance by 30% (Table 6.3), improving faithfulness without increasing K.
3. **GPU Batching:** Evaluating K coalitions in parallel on GPU (vs. sequential CPU) provides 53× speedup (1,850ms → 35ms, Table 6.4).

*How does it connect to theory?*
This finding validates Theorem 3.3 from Chapter 3, which predicted O(M log M + K·D) complexity. Our empirical scaling (Figure 6.2) closely matches the theoretical prediction: doubling M increases latency by ~2× (log-linear), not 4× (which would indicate quadratic). The 0.76 insertion AUC also aligns with Theorem 3.5's approximation bound: for K=100, ε ≈ 0.1, implying >0.7 faithfulness.

*Unexpected aspects:*
We initially expected K=200 samples would be needed for 0.7 insertion AUC based on pilot experiments (Section 4.6). However, attention-guided sampling proved more effective than anticipated, achieving target faithfulness with K=100. This suggests that ViT attention weights provide a strong prior for feature importance, reducing the need for exhaustive coalition sampling.
```

**Word Count per RQ:** 800-1,200 words

---

### 7.2.2 RQ2: [Research Question 2]

**Follow the same structure as 7.2.1**

---

### 7.2.3 RQ3: [Research Question 3]

**Follow the same structure as 7.2.1**

---

### 7.2.X Additional Findings (Optional)

**Purpose:** Interpret unexpected or secondary findings not tied to specific RQs.

**Template:**

```markdown
### 7.2.X Additional Findings

Beyond our research questions, we observed [ADDITIONAL FINDING]. This is notable because [WHY IT'S INTERESTING].

[EVIDENCE, INTERPRETATION, EXPLANATION]
```

**Example:**

> Beyond our research questions, we observed that E-MHA attention patterns differ qualitatively from standard MHA. E-MHA exhibits 40% more attention concentration in the last layer (Figure 6.8), suggesting that sparse attention forces earlier layers to distribute attention more broadly. This is notable because it contradicts prior work (Dosovitskiy et al. 2021) showing that ViT attention becomes *more* concentrated in deeper layers.
>
> We attribute this to the explainability constraint: E-MHA's auxiliary explanation head penalizes overly concentrated attention (entropy regularization), encouraging attention diversity. This may explain why E-ViT maintains accuracy despite sparse attention—diverse early-layer attention compensates for focused late-layer attention.

---

## 7.3 Comparison with Prior Work

**Purpose:** Situate your results in the context of existing literature. Explain how your findings relate to (agree with / disagree with / extend) prior work.

**What to Include:**
- Agreement with previous findings (and why)
- Disagreement with previous findings (and why—without unfairly criticizing)
- Extension of previous findings (new domains, scales, conditions)
- Novelty of your approach (what's truly new)

**Important:** Be fair to prior work. Acknowledge their contributions and limitations. Avoid strawman arguments.

**Template:**

```markdown
## 7.3 Comparison with Prior Work

[OVERVIEW]
Our findings both corroborate and extend prior research on [TOPIC]. We discuss how our results relate to existing work in four areas: [Area 1], [Area 2], [Area 3], [Area 4].

### 7.3.1 Agreement with Prior Work

**[Topic/Finding]:**

Our finding that [YOUR RESULT] aligns with prior work by [Authors, Year], who observed [THEIR RESULT]. For example:
- [Author 1 et al., Year] found [FINDING 1], consistent with our [YOUR FINDING 1]
- [Author 2 et al., Year] reported [FINDING 2], which we also observe ([YOUR EVIDENCE])

This agreement suggests that [IMPLICATION]. The consistency across studies ([THEIRS] and ours) strengthens the evidence that [BROADER CONCLUSION].

### 7.3.2 Disagreement with Prior Work

**[Topic/Finding]:**

Our finding that [YOUR RESULT] appears to contradict [Authors, Year], who reported [THEIR RESULT]. However, we argue that this difference is explained by [REASON]:

1. **Methodological Differences:** Our work uses [YOUR METHOD], while [Authors, Year] used [THEIR METHOD]. This may account for [EXPLANATION].
2. **Scope Differences:** We evaluate on [YOUR DOMAIN/DATASET], whereas [Authors, Year] focused on [THEIR DOMAIN/DATASET]. The difference may be domain-specific.
3. **Alternative Explanation:** It's possible that [THEIR FINDING] holds under [CONDITIONS], but [YOUR FINDING] holds under [DIFFERENT CONDITIONS].

**Fair Assessment:**
[Authors, Year]'s work was pioneering in [CONTRIBUTION], and our findings do not diminish their contribution. Instead, our results suggest that [NUANCED CONCLUSION ACKNOWLEDGING BOTH FINDINGS].

### 7.3.3 Extension of Prior Work

**[Topic/Finding]:**

Our work extends [Authors, Year] in several ways:
- **Scale:** We demonstrate that their approach [SCALES/DOESN'T SCALE] to [NEW SCALE, e.g., larger models, more data]
- **Generalization:** We show that their findings hold [HOLD/DON'T HOLD] in [NEW DOMAIN]
- **Combination:** We integrate their approach with [NEW COMPONENT], improving [METRIC] by [X%]

For example, [Authors, Year] showed that [THEIR FINDING] on [THEIR DATASET]. We replicate this finding on [YOUR DATASET] and further show that [EXTENSION]. This suggests that [GENERALIZATION OR BOUNDARY CONDITION].

### 7.3.4 Novel Contributions

**[Topic/Finding]:**

To our knowledge, our work is the first to [NOVEL ASPECT]. While [Authors, Year] addressed [RELATED PROBLEM], they did not [WHAT THEY DIDN'T DO]. Our approach differs in [KEY DIFFERENCES]:

1. **[Difference 1]:** [Explanation]
2. **[Difference 2]:** [Explanation]

This novelty enables [CAPABILITY], which was not possible with prior methods.
```

**Example:**

```markdown
## 7.3 Comparison with Prior Work

Our findings both corroborate and extend prior research on explainability for vision transformers. We discuss how our results relate to existing work in four areas: SHAP for deep learning, ViT explainability, fairness in explanations, and real-time XAI.

### 7.3.1 Agreement with Prior Work

**SHAP Faithfulness:**

Our finding that hierarchical SHAP maintains 0.76 insertion AUC aligns with prior work by Lundberg & Lee (2017), who demonstrated that SHAP's game-theoretic foundation yields faithful explanations. For example:
- Lundberg & Lee (2017) reported 0.78-0.82 insertion AUC for KernelSHAP on image classifiers, consistent with our 0.76 (within approximation error)
- Covert et al. (2020) showed that sampling-based SHAP achieves comparable faithfulness to exact SHAP with K=100-200 samples, which we also observe (Table 6.2)

This agreement suggests that hierarchical approximation preserves SHAP's theoretical properties. The consistency across studies (Euclidean SHAP and our hypersphere SHAP) strengthens the evidence that Shapley values provide faithful feature attributions regardless of embedding geometry.

### 7.3.2 Disagreement with Prior Work

**ViT Attention as Explanation:**

Our finding that ViT attention exhibits demographic bias (24% variance across groups, Table 6.5) appears to contradict Chefer et al. (2021), who reported that transformer attention is "inherently interpretable" for ViT. However, we argue that this difference is explained by:

1. **Methodological Differences:** Our work evaluates fairness across demographic groups, while Chefer et al. (2021) evaluated localization accuracy (IoU with ground-truth boxes). Attention may be locally accurate but globally biased.
2. **Scope Differences:** We evaluate on face recognition (ArcFace-trained ViT on FairFace), whereas Chefer et al. (2021) focused on ImageNet classification (supervised ViT). Face recognition's hypersphere embeddings may amplify bias.
3. **Alternative Explanation:** It's possible that attention is interpretable (high IoU) but biased (differential sensitivity across groups). These are orthogonal properties.

**Fair Assessment:**
Chefer et al.'s work was pioneering in showing that ViT attention can localize objects, and our findings do not diminish this contribution. Instead, our results suggest that attention interpretability does not guarantee fairness—additional calibration is needed for equitable explanations.

### 7.3.3 Extension of Prior Work

**Hierarchical SHAP:**

Our work extends Mitchell et al. (2022) who introduced hierarchical sampling for SHAP but did not:
- **Attention-Guided Sampling:** We integrate ViT attention weights to bias coalition sampling, reducing variance by 30% (Table 6.3) compared to uniform sampling
- **Hypersphere Geometry:** We adapt SHAP to geodesic distances (Theorem 3.2), whereas Mitchell et al. used Euclidean SHAP
- **Real-Time Performance:** We achieve 58ms latency via GPU batching and JIT compilation, whereas Mitchell et al. reported 200-500ms (CPU-only)

For example, Mitchell et al. (2022) showed that hierarchical sampling reduces complexity to O(M log M) on tabular data. We replicate this finding on vision transformers (Figure 6.2) and further show that attention-guided sampling improves faithfulness by 8% (0.70 → 0.76 insertion AUC). This suggests that domain-specific priors (attention weights) enhance hierarchical approximation effectiveness.

### 7.3.4 Novel Contributions

**Demographic Calibration for Explanations:**

To our knowledge, our work is the first to apply statistical calibration to reduce demographic bias in feature attributions. While Buolamwini & Gebru (2018) addressed fairness in face recognition accuracy, they did not address explanation fairness. Our approach differs in:

1. **Explanation-Level Fairness:** We calibrate attributions (not predictions), ensuring explanations are equally meaningful across demographics
2. **Rank-Preserving Calibration:** Our method subtracts demographic-specific bias while preserving feature rankings (>0.95 rank correlation), maintaining faithfulness

This novelty enables fair explanations for regulated applications (EU AI Act Article 13: "right to explanation"). Prior fairness work focused on accuracy parity, which does not guarantee explanation equity.
```

**Word Count:** 1,500-2,000 words

**📚 CITATION CHECK:**
- [ ] Every prior work mentioned is cited correctly
- [ ] Comparisons are fair (no strawman arguments)
- [ ] Acknowledging contributions of prior work before critiquing
- [ ] See [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md)

---

## 7.4 Theoretical Implications

**Purpose:** Discuss what your findings mean for theory in your field.

**What to Include:**
- Support for existing theories
- Challenges to existing theories
- New theoretical insights
- Boundary conditions

**Template:**

```markdown
## 7.4 Theoretical Implications

Our findings have several implications for [THEORETICAL FRAMEWORK/AREA]:

### 7.4.1 Support for Existing Theory

[THEORY/FRAMEWORK]

Our results provide empirical support for [THEORY] (Author, Year). Specifically:
- **Prediction:** [THEORY] predicts that [X]
- **Evidence:** We observe [X] in our results (Section 6.Y)
- **Implication:** This corroborates [THEORY] in the context of [YOUR DOMAIN]

[EXPLAIN WHY THIS SUPPORT IS SIGNIFICANT]

### 7.4.2 Challenges to Existing Theory

[THEORY/ASSUMPTION]

Our results challenge the assumption that [ASSUMPTION] from [FRAMEWORK]. We observe [CONTRADICTORY EVIDENCE]:
- **Assumption:** [EXISTING THEORY] assumes [X]
- **Contradiction:** Our results show [NOT X] (Section 6.Z)
- **Explanation:** This discrepancy may be explained by [REASON]

[PROPOSE REFINEMENT OR ALTERNATIVE]

### 7.4.3 New Theoretical Insights

[INSIGHT]

Our work suggests a new theoretical insight: [INSIGHT STATEMENT]. This insight:
- **Explains:** [PHENOMENON] observed in our results (Section 6.A)
- **Generalizes:** Beyond our specific domain to [BROADER CONTEXT]
- **Predicts:** [FUTURE PREDICTION]

[ELABORATE ON THE INSIGHT]

### 7.4.4 Boundary Conditions

[CONDITIONS]

Our findings establish boundary conditions for [THEORY/APPROACH]:
- **Holds when:** [CONDITION 1]
- **Fails when:** [CONDITION 2]
- **Example:** In our results, [APPROACH] works well for [CASE 1] but poorly for [CASE 2]

[EXPLAIN THE BOUNDARY]
```

**Example:**

```markdown
## 7.4 Theoretical Implications

Our findings have several implications for explainability theory and Shapley value applications:

### 7.4.1 Support for Shapley Value Theory

Our results provide empirical support for the theoretical properties of Shapley values. Specifically:
- **Prediction:** Shapley uniqueness theorem (Shapley 1953) predicts that Shapley values are the only attribution satisfying efficiency, symmetry, dummy player, and additivity
- **Evidence:** Our empirical verification (Section 6.2.3) confirms all four axioms hold for hierarchical SHAP (within ε=1e-6 tolerance)
- **Implication:** This corroborates Shapley theory in the context of hypersphere embeddings and hierarchical approximation

This support is significant because it extends Shapley theory beyond traditional game-theoretic settings (coalition games with explicit payoffs) to modern ML systems (neural networks with implicit, learned representations). The fact that axioms hold even with geodesic distances (non-Euclidean geometry) and hierarchical approximation (sampling-based estimation) suggests that Shapley theory is robust to these adaptations.

### 7.4.2 Challenges to Existing Assumptions

Our results challenge the implicit assumption that raw model internals (attention weights, gradients) are inherently interpretable. We observe:
- **Assumption:** Prior work (Chefer et al. 2021; Vaswani et al. 2017) assumes attention weights reflect feature importance
- **Contradiction:** Our results show 24% demographic variance in attention-based attributions (Table 6.5), indicating bias
- **Explanation:** This discrepancy arises because attention is learned from training data (ImageNet/face datasets), which contains demographic imbalances. Attention learns dataset biases, not "true" feature importance.

This suggests a refinement: **Raw model internals should not be used as explanations without calibration**. While attention/gradients provide useful signals (e.g., for sampling in our hierarchical SHAP), they require post-processing (fairness calibration) to ensure equitable explanations.

### 7.4.3 New Theoretical Insights

Our work suggests a new theoretical insight: **Hierarchical approximation with domain priors achieves better variance-bias trade-off than uniform sampling**. This insight:
- **Explains:** Why attention-guided sampling reduces variance by 30% (Table 6.3) without increasing bias (faithfulness remains 0.76)
- **Generalizes:** Beyond ViT attention to other domain priors (saliency maps, gradient norms, learned importance weights)
- **Predicts:** Combining hierarchical structure (reduces complexity) with domain priors (reduces variance) should outperform flat sampling with priors or hierarchical sampling without priors

Formally, we hypothesize that approximation error decreases as ε ∝ 1/(√K · prior_quality), where prior_quality measures how well the prior correlates with true Shapley values. This extends Theorem 3.5 (which assumes uniform sampling) to incorporate prior information.

### 7.4.4 Boundary Conditions

Our findings establish boundary conditions for hierarchical SHAP:
- **Holds when:** Features have interpretable hierarchical structure (e.g., facial regions: eyes → left-eye, right-eye)
- **Fails when:** Features are atomic or unstructured (e.g., pixel-level explanations—no natural hierarchy)
- **Example:** In our results, hierarchical SHAP works well for 8 semantic facial regions (M=8, log M=3 levels) but would be ineffective for 50,176 pixels (M=50,176, log M=16 levels—too deep hierarchy)

This boundary suggests that hierarchical SHAP is best suited for structured feature spaces (superpixels, semantic regions, modular components), not raw low-level features. For unstructured spaces, flat approximation methods (KernelSHAP, FastSHAP) may be more appropriate.
```

**Word Count:** 1,000-1,500 words

---

## 7.5 Practical Implications

**Purpose:** Discuss what your findings mean for practice, applications, and real-world deployment.

**What to Include:**
- Who benefits from your work
- How to use your findings in practice
- Practical recommendations
- Implementation considerations

**Balance Aspirations with RULE 1:**
- ✅ "Our method is designed for production deployment"
- ✅ "Based on our results, practitioners could..."
- ❌ "We have deployed this in 5 hospitals" (unless you actually have—no false claims)

**Template:**

```markdown
## 7.5 Practical Implications

Our findings have practical implications for [STAKEHOLDER GROUPS]:

### 7.5.1 Implications for Practitioners

**Who Benefits:**
[PRACTITIONER GROUP, e.g., "ML engineers deploying face recognition systems"]

**How to Use These Findings:**

1. **[Recommendation 1]:** [Actionable guidance]
   - **When:** [Under what conditions]
   - **How:** [Step-by-step or high-level approach]
   - **Trade-offs:** [Costs/benefits]

2. **[Recommendation 2]:** [...]

**Example Use Case:**
[Concrete scenario illustrating how practitioners would apply your work]

### 7.5.2 Implications for Policy

**Who Benefits:**
[POLICY GROUP, e.g., "Regulators implementing AI Act compliance"]

**Policy Recommendations:**

1. **[Recommendation 1]:** [Policy guidance based on findings]
   - **Evidence:** [Your result supporting this recommendation]
   - **Rationale:** [Why this policy makes sense]

2. **[Recommendation 2]:** [...]

### 7.5.3 Implementation Considerations

**When to Use This Approach:**
- ✅ Use when: [Condition 1]
- ✅ Use when: [Condition 2]
- ❌ Don't use when: [Condition 3]
- ❌ Don't use when: [Condition 4]

**Deployment Checklist:**
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

**Performance Expectations:**
Based on our results, practitioners should expect:
- **Latency:** [X ms] for [condition]
- **Accuracy:** [Y%] on [dataset type]
- **Fairness:** [Z%] variance for [demographic groups]
```

**Example:**

```markdown
## 7.5 Practical Implications

Our findings have practical implications for ML engineers, product managers, and AI regulators:

### 7.5.1 Implications for ML Engineers

**Who Benefits:**
ML engineers deploying face recognition systems in regulated domains (finance, healthcare, law enforcement)

**How to Use These Findings:**

1. **Replace Post-Hoc Explanations with E-ViT:**
   - **When:** Building new face recognition systems (not retrofitting existing models)
   - **How:** Use E-ViT architecture (open-source implementation) instead of baseline ViT. Train with ArcFace loss + auxiliary explanation head (see Chapter 5).
   - **Trade-offs:** +12ms latency (46ms → 58ms) for E-ViT vs. post-hoc GradCAM. Benefit: Inherently interpretable model (no separate explanation step).

2. **Apply Demographic Calibration to Existing Explanations:**
   - **When:** Explanation fairness is required (e.g., EU AI Act compliance) and retraining is impractical
   - **How:** Collect demographic labels for calibration set (can use off-the-shelf demographic classifier). Compute group-specific bias statistics. Subtract bias from explanations (Algorithm 4.3 in Chapter 4).
   - **Trade-offs:** Requires demographic labels (may raise privacy concerns). Benefit: 63% reduction in explanation variance (24% → 8.7%).

3. **Use Attention-Guided Sampling for Custom Explainers:**
   - **When:** Building SHAP-based explainers for any ViT model (not just face recognition)
   - **How:** Extract attention weights from last layer. Use softmax(attention / T) with T=0.5 to bias coalition sampling.
   - **Trade-offs:** Minimal cost (attention is already computed). Benefit: 30% variance reduction vs. uniform sampling.

**Example Use Case:**
A bank deploying face recognition for customer authentication must provide explanations under EU AI Act Article 13. The bank's ML engineer:
1. Integrates E-ViT for new customer enrollments (real-time explanations during onboarding)
2. Applies demographic calibration to legacy system explanations (fairness retrofit)
3. Logs explanations for audit trail (5-year retention requirement)

### 7.5.2 Implications for Product Managers

**Who Benefits:**
Product managers deciding whether to adopt explainable AI systems

**Product Recommendations:**

1. **Real-Time Explanations Are Feasible:**
   - **Evidence:** 58ms latency meets interactive system requirements (<100ms)
   - **Rationale:** Users can receive explanations at query time without noticeable delay. Enables "explain on demand" UX (button click → instant explanation).

2. **Fairness Calibration Should Be Default:**
   - **Evidence:** Uncalibrated explanations show 24% demographic variance (Table 6.5)
   - **Rationale:** Biased explanations erode user trust and violate anti-discrimination laws. Calibration is a low-cost "fairness gate" (3ms overhead).

3. **Budget for Explanation Infrastructure:**
   - **Evidence:** E-ViT requires +35% GPU memory vs. baseline ViT (8.2GB vs. 6.1GB)
   - **Rationale:** Explanation-capable models have higher infrastructure costs. Plan for 1.5× GPU capacity.

### 7.5.3 Implementation Considerations

**When to Use This Approach:**
- ✅ Use when: Deploying face recognition in regulated domains (GDPR, AI Act)
- ✅ Use when: User-facing applications requiring interpretability (customer authentication, access control)
- ✅ Use when: Real-time performance is critical (<100ms latency requirement)
- ✅ Use when: Fairness across demographic groups is required
- ❌ Don't use when: Offline batch processing (exact SHAP is feasible)
- ❌ Don't use when: Features have no hierarchical structure (pixel-level explanations)
- ❌ Don't use when: M > 50 features (hierarchical tree becomes too deep)

**Deployment Checklist:**
- [ ] GPU with ≥8GB memory (for E-ViT + hierarchical SHAP)
- [ ] PyTorch 2.0+ for JIT compilation support
- [ ] Demographic calibration set with ≥100 samples per group (for statistical calibration)
- [ ] Explanation storage infrastructure (for audit trail)
- [ ] User consent for demographic labeling (if using calibration)

**Performance Expectations:**
Based on our results, practitioners should expect:
- **Latency:** 58ms for M=8 features, K=100 samples (scales to ~90ms for M=16, ~150ms for M=32)
- **Faithfulness:** 0.74-0.78 insertion AUC (comparable to KernelSHAP's 0.78-0.82)
- **Fairness:** <10% variance for 7 demographic groups (after calibration)
- **Accuracy:** 99.2% on LFW (no degradation vs. baseline ViT)
```

**Word Count:** 1,000-1,500 words

---

## 7.6 Limitations

**Purpose:** Honestly discuss what your work does NOT do, what you cannot claim, and where your approach may fail.

**Why This Matters:**
- Demonstrates scientific integrity (RULE 1: truth first)
- Helps future researchers avoid the same pitfalls
- Frames your contributions appropriately
- Shows you understand the scope of your work

**Important:** Frame limitations as boundaries, not failures. Every study has limitations—acknowledging them strengthens your work.

**Structure:**
- 7.6.1 Methodological Limitations
- 7.6.2 Scope Limitations
- 7.6.3 Generalization Limitations

---

### 7.6.1 Methodological Limitations

**Purpose:** Limitations related to your research design, methods, or measurements.

**Template:**

```markdown
### 7.6.1 Methodological Limitations

Our methodology has several limitations:

1. **[Limitation 1]:**
   - **Description:** [What is the limitation?]
   - **Impact:** [How does this affect results/conclusions?]
   - **Mitigation:** [What did you do to minimize impact, if anything?]
   - **Future Work:** [How could this be addressed?]

2. **[Limitation 2]:**
   - [...]

**Example:**
```

**Example:**

```markdown
### 7.6.1 Methodological Limitations

Our methodology has several limitations:

1. **Insertion AUC as Faithfulness Metric:**
   - **Description:** We evaluate faithfulness using insertion AUC (adding features by importance), which measures correlation between attributions and model behavior. However, insertion AUC does not directly measure whether attributions reflect *causal* relationships.
   - **Impact:** High insertion AUC indicates that top-attributed features improve predictions when added, but doesn't prove they *cause* predictions. Spurious correlations could inflate insertion AUC.
   - **Mitigation:** We also report deletion AUC (removing features) as a complementary metric (Table 6.2). Convergence of insertion and deletion AUC (0.76 vs. 0.74) suggests attributions are not purely spurious.
   - **Future Work:** Causal faithfulness metrics (e.g., interventional SHAP, Chen et al. 2023) could provide stronger evidence.

2. **Demographic Classifier Accuracy:**
   - **Description:** Demographic calibration relies on a pretrained FairFace classifier (92% accuracy) to predict demographic groups. Misclassification introduces noise into calibration.
   - **Impact:** If a face is misclassified (e.g., predicted as Asian when actually White), wrong calibration bias is applied. This could inadvertently introduce new biases.
   - **Mitigation:** We use high-confidence predictions only (softmax > 0.9), reducing misclassification rate to 3%. We also report uncalibrated results (Table 6.5) for comparison.
   - **Future Work:** User-provided demographic labels (with consent) would eliminate classification errors.

3. **Limited Baseline Comparisons:**
   - **Description:** We compare against 3 baselines (KernelSHAP, GradCAM, LIME). Other explanation methods (Integrated Gradients, LRP, attention rollout) were not evaluated.
   - **Impact:** We cannot conclusively claim hierarchical SHAP is superior to *all* methods, only to the three we tested.
   - **Mitigation:** We selected baselines representing different paradigms (Shapley-based, gradient-based, perturbation-based) to cover diverse approaches.
   - **Future Work:** Comprehensive comparison with 10+ methods would strengthen generalizability claims.

4. **Fixed Feature Granularity:**
   - **Description:** We use 8 predefined facial regions (eyes, nose, mouth, etc.) as features. The choice of granularity (8 vs. 68 landmarks vs. superpixels) affects results.
   - **Impact:** Attributions are tied to the chosen feature definition. Different granularities would yield different explanations.
   - **Mitigation:** We chose 8 regions based on facial action coding system (FACS) literature (Ekman & Friesen 1978), providing semantic meaningfulness.
   - **Future Work:** Multi-scale explanations (hierarchical: face → regions → landmarks) could provide richer interpretability.
```

---

### 7.6.2 Scope Limitations

**Purpose:** Limitations related to what aspects of the problem you did/didn't address.

**Template:**

```markdown
### 7.6.2 Scope Limitations

Our work has several scope limitations:

1. **[Limitation 1]:**
   - **What We Did:** [What you covered]
   - **What We Didn't Do:** [What was excluded]
   - **Justification:** [Why this scope was chosen]
   - **Boundary:** [Under what conditions does your work apply?]

2. **[Limitation 2]:**
   - [...]
```

**Example:**

```markdown
### 7.6.2 Scope Limitations

Our work has several scope limitations:

1. **Face Recognition Only:**
   - **What We Did:** Evaluated on face recognition tasks (LFW, FairFace)
   - **What We Didn't Do:** Other ViT applications (object detection, medical imaging, NLP transformers)
   - **Justification:** Face recognition is a high-stakes domain with strict fairness requirements (GDPR, AI Act), making it a critical use case.
   - **Boundary:** Our approach applies to vision transformers with spatial features (images). Extension to non-spatial domains (text, time-series) requires adaptation.

2. **Static Images Only:**
   - **What We Did:** Explain single-image predictions (1-to-1 verification)
   - **What We Didn't Do:** Video-based face recognition (temporal aggregation, tracking)
   - **Justification:** Static images are the base case; video introduces additional complexity (temporal coherence, motion)
   - **Boundary:** For video, explanations would need to account for temporal dependencies (e.g., frame-level attributions + temporal importance)

3. **Closed-Set Recognition:**
   - **What We Did:** Evaluate on datasets with fixed identity sets (LFW: 5,749 identities)
   - **What We Didn't Do:** Open-set recognition (unknown identities), one-shot learning
   - **Justification:** Closed-set is more controlled for fairness evaluation (balanced demographics per identity)
   - **Boundary:** Open-set may exhibit different biases (threshold-based decisions introduce additional fairness concerns)

4. **English Documentation Only:**
   - **What We Did:** Provide explanation visualizations with English labels
   - **What We Didn't Do:** Multilingual support, accessibility for non-English speakers
   - **Justification:** Focused on algorithmic fairness first; interface fairness is future work
   - **Boundary:** Global deployment requires localization (translated labels, culturally appropriate visualizations)
```

---

### 7.6.3 Generalization Limitations

**Purpose:** Limitations related to how broadly your findings apply.

**Template:**

```markdown
### 7.6.3 Generalization Limitations

Our findings may not generalize to:

1. **[Limitation 1: Population/Context]:**
   - **Our Study:** [What population/context you studied]
   - **May Not Generalize To:** [Other populations/contexts]
   - **Reason:** [Why generalization is uncertain]
   - **Evidence Needed:** [What would be needed to establish generalization]

2. **[Limitation 2: Time/Temporal]:**
   - [...]

3. **[Limitation 3: Scale/Setting]:**
   - [...]
```

**Example:**

```markdown
### 7.6.3 Generalization Limitations

Our findings may not generalize to:

1. **Non-Western Faces:**
   - **Our Study:** LFW and FairFace are predominantly Western faces (60% White, 20% Black, 15% Asian, 5% other)
   - **May Not Generalize To:** Faces from underrepresented regions (Middle East, Pacific Islands, Indigenous populations)
   - **Reason:** Demographic calibration is dataset-specific—bias statistics are computed from FairFace's demographic distribution
   - **Evidence Needed:** Evaluation on geographically diverse datasets (e.g., African Face Database, Indian Face Database) would establish generalization

2. **Occluded or Low-Quality Faces:**
   - **Our Study:** High-quality, frontal faces (LFW: studio photos, FairFace: web-scraped but filtered for quality)
   - **May Not Generalize To:** Occluded faces (masks, sunglasses), extreme poses, low-resolution surveillance footage
   - **Reason:** Feature extraction (facial landmarks) may fail for occluded faces, making explanations unreliable
   - **Evidence Needed:** Evaluation on real-world surveillance data (e.g., SCface, MEDS) with occlusions and quality variations

3. **Larger Feature Sets:**
   - **Our Study:** 8 features (semantic facial regions)
   - **May Not Generalize To:** M > 50 features (pixel-level, 68 landmarks, superpixels)
   - **Reason:** Hierarchical tree depth scales as log M. For M=50,176 pixels, log M ≈ 16 levels, making hierarchical sampling impractical
   - **Evidence Needed:** Scalability experiments with M=16, 32, 64, 128 would establish upper bound

4. **Other ViT Architectures:**
   - **Our Study:** ViT-Base/16 (12 layers, 12 heads, 197 patches)
   - **May Not Generalize To:** ViT-Large, ViT-Huge, hybrid CNNs + ViT (e.g., Swin Transformer)
   - **Reason:** Attention patterns differ across architectures. E-MHA's sparse attention design is tuned for ViT-Base.
   - **Evidence Needed:** Ablation studies with different ViT variants (ViT-Small, ViT-Large, DeiT) would assess architecture sensitivity

5. **Temporal Stability:**
   - **Our Study:** Evaluation in 2025 with current ViT models and datasets
   - **May Not Generalize To:** Future ViT architectures, evolving demographic distributions, new face recognition paradigms
   - **Reason:** Model architectures and datasets evolve. Today's biases may differ from future biases.
   - **Evidence Needed:** Longitudinal study re-evaluating fairness as models/datasets change would assess temporal generalization
```

---

## 7.7 Threats to Validity

**Purpose:** Identify factors that could invalidate or weaken your findings.

**Structure:**
- Internal validity (causal relationships)
- External validity (generalizability)
- Construct validity (measurements)
- Statistical conclusion validity (statistical inferences)

**Template:**

```markdown
## 7.7 Threats to Validity

We identify threats to validity following Wohlin et al. (2012):

### 7.7.1 Internal Validity

**Threats to Causal Inferences:**

1. **[Threat 1]:**
   - **Description:** [What could confound causal relationships?]
   - **Impact:** [How would this affect conclusions?]
   - **Mitigation:** [What did you do to address this?]

2. **[Threat 2]:**
   - [...]

### 7.7.2 External Validity

**Threats to Generalizability:**

1. **[Threat 1]:**
   - **Description:** [What limits generalizability?]
   - **Impact:** [To what populations/settings might findings not apply?]
   - **Mitigation:** [What did you do to enhance generalizability?]

2. **[Threat 2]:**
   - [...]

### 7.7.3 Construct Validity

**Threats to Measurement:**

1. **[Threat 1]:**
   - **Description:** [Are you measuring what you think you're measuring?]
   - **Impact:** [How would mismeasurement affect conclusions?]
   - **Mitigation:** [What did you do to validate measurements?]

2. **[Threat 2]:**
   - [...]

### 7.7.4 Statistical Conclusion Validity

**Threats to Statistical Inferences:**

1. **[Threat 1]:**
   - **Description:** [What statistical assumptions might be violated?]
   - **Impact:** [How would this affect significance testing?]
   - **Mitigation:** [What statistical controls did you use?]

2. **[Threat 2]:**
   - [...]
```

**Example:**

```markdown
## 7.7 Threats to Validity

We identify threats to validity following Wohlin et al. (2012):

### 7.7.1 Internal Validity

**Threats to Causal Inferences:**

1. **Confounding from Hyperparameter Tuning:**
   - **Description:** We tuned hyperparameters (K=100 samples, T=0.5 temperature) on a validation set drawn from the same distribution as the test set. This could inflate performance estimates.
   - **Impact:** Reported performance (0.76 insertion AUC) may be optimistic; generalization to unseen distributions is uncertain.
   - **Mitigation:** We use separate datasets for tuning (LFW val split) and evaluation (LFW test split). We report results on FairFace (independent dataset) to assess generalization.

2. **Selection Bias in Face Detection:**
   - **Description:** Our input processor uses Dlib face detector, which may have different accuracy across demographic groups (lower recall for darker skin tones, per Buolamwini & Gebru 2018).
   - **Impact:** If certain demographics are underrepresented due to detection failures, fairness results may be biased (e.g., reported fairness is only for successfully detected faces, not all faces).
   - **Mitigation:** We report detection rates per demographic group (Table 6.A in Appendix). Rates are high (>95%) across all groups in FairFace, suggesting minimal selection bias.

3. **Implementation Bugs:**
   - **Description:** Despite 87% test coverage, bugs may remain in the implementation that affect results.
   - **Impact:** Incorrect implementation could invalidate all findings.
   - **Mitigation:** We validated implementation against theory (Section 6.2.3): Shapley axioms hold within ε=1e-6 tolerance, suggesting correctness. We also replicated KernelSHAP baseline (our implementation: 0.78 AUC vs. Lundberg's: 0.79 AUC, within margin of error).

### 7.7.2 External Validity

**Threats to Generalizability:**

1. **Dataset Representativeness:**
   - **Description:** LFW and FairFace may not represent global face diversity (skewed toward Western faces, web-scraped biases).
   - **Impact:** Findings may not generalize to underrepresented populations (Middle Eastern, Indigenous, elderly).
   - **Mitigation:** We report demographic distributions (Table 6.B in Appendix). We acknowledge this limitation (Section 7.6.3) and recommend evaluation on diverse datasets.

2. **Task Specificity:**
   - **Description:** Face recognition is a specific computer vision task. Findings may not transfer to other ViT applications (object detection, segmentation).
   - **Impact:** Our fairness results may be face-specific (e.g., demographic bias in face recognition may not exist in ImageNet classification).
   - **Mitigation:** We focus claims on face recognition specifically. We discuss applicability to other domains in Section 7.5 (practical implications).

3. **Temporal Validity:**
   - **Description:** ViT architectures and training practices evolve. Our results are specific to ViT-Base/16 in 2025.
   - **Impact:** Future ViT variants (e.g., ViT-2026 with new attention mechanisms) may behave differently.
   - **Mitigation:** We open-source our evaluation framework (Chapter 5) to enable future studies to replicate experiments on new models.

### 7.7.3 Construct Validity

**Threats to Measurement:**

1. **Insertion AUC as Faithfulness Proxy:**
   - **Description:** Insertion AUC measures correlation between attributions and model behavior, not causal faithfulness. A high AUC could result from spurious correlations.
   - **Impact:** We may overestimate faithfulness if attributions capture correlations (not causes).
   - **Mitigation:** We use multiple faithfulness metrics (insertion AUC, deletion AUC, rank correlation) to triangulate. Convergence across metrics (0.76, 0.74, 0.95) suggests robust faithfulness.

2. **Demographic Classification Errors:**
   - **Description:** Fairness metrics rely on demographic labels predicted by a classifier (92% accuracy). Misclassifications introduce measurement error.
   - **Impact:** Fairness variance may be under- or over-estimated due to label noise.
   - **Mitigation:** We use high-confidence predictions (softmax > 0.9), reducing error to 3%. We also analyze sensitivity to classification confidence (Figure 6.C in Appendix).

3. **User Perception of Fairness:**
   - **Description:** We measure statistical fairness (variance ratio), not perceived fairness. Users may perceive explanations as unfair even if statistically balanced.
   - **Impact:** Our fairness results may not align with user experience.
   - **Mitigation:** We acknowledge this limitation (Section 7.6.1). Future work should include human evaluation of explanation fairness.

### 7.7.4 Statistical Conclusion Validity

**Threats to Statistical Inferences:**

1. **Multiple Comparisons:**
   - **Description:** We perform multiple hypothesis tests (e.g., comparing our method to 3 baselines on 5 metrics = 15 tests). This inflates Type I error (false positives).
   - **Impact:** Some "significant" differences may be spurious (p < 0.05 by chance).
   - **Mitigation:** We apply Bonferroni correction (α = 0.05/15 = 0.003). All reported significant differences remain significant after correction.

2. **Non-Normal Distributions:**
   - **Description:** Some metrics (e.g., insertion AUC) may not follow normal distributions, violating t-test assumptions.
   - **Impact:** p-values may be inaccurate if distributional assumptions are violated.
   - **Mitigation:** We use non-parametric tests (Wilcoxon signed-rank) for non-normal metrics. Results are consistent with parametric tests (Table 6.D in Appendix).

3. **Small Sample Sizes:**
   - **Description:** Some demographic groups have small sample sizes in FairFace (e.g., Middle Eastern: n=150).
   - **Impact:** Fairness estimates for small groups have high variance (wide confidence intervals).
   - **Mitigation:** We report confidence intervals (95% CI) for all fairness metrics. We flag groups with n<200 as "low confidence" (Table 6.5).

4. **P-Hacking Risk:**
   - **Description:** We explored multiple fairness metrics (variance ratio, demographic parity, equalized odds) before selecting variance ratio for primary reporting.
   - **Impact:** Selecting the "best" metric post-hoc could inflate significance.
   - **Mitigation:** We pre-registered variance ratio as primary metric in methodology (Section 4.7). We report all explored metrics in Appendix (Table 6.E).
```

**Word Count:** 800-1,200 words

---

## 7.8 Summary

**Purpose:** Recap the main points of the discussion chapter.

**Template:**

```markdown
## 7.8 Summary

This chapter interpreted the results from Chapter 6 and discussed their implications.

**Main Interpretations:**

Our findings demonstrate that:
1. **RQ1:** [Brief answer and interpretation]
2. **RQ2:** [Brief answer and interpretation]
3. **RQ3:** [Brief answer and interpretation]

**Comparison with Prior Work:**

Our results [agree with / extend / contradict] existing literature:
- **Agreement:** [Key agreement]
- **Extension:** [Key extension]
- **Novelty:** [Key novel contribution]

**Implications:**

Our work has implications for:
- **Theory:** [Main theoretical insight]
- **Practice:** [Main practical recommendation]

**Limitations:**

We acknowledge limitations in:
- **Methodology:** [Key methodological limitation]
- **Scope:** [Key scope limitation]
- **Generalization:** [Key generalization limitation]

These limitations do not invalidate our findings but establish their boundaries.

**Connection to Conclusion:**

In the next chapter (Chapter 8), we synthesize these findings into broader conclusions, discuss future work directions, and reflect on the contributions of this research.
```

**Example:**

> This chapter interpreted the results from Chapter 6 and discussed their implications.
>
> **Main Interpretations:**
>
> Our findings demonstrate that:
> 1. **RQ1 (Computational Optimization):** Hierarchical SHAP achieves real-time performance (58ms) with faithful explanations (0.76 insertion AUC) by combining binary tree structure, attention-guided sampling, and GPU batching
> 2. **RQ2 (Architectural Integration):** E-ViT with E-MHA maintains accuracy (99.2% on LFW) by using sparse attention that preserves discriminative features in the CLS token embedding
> 3. **RQ3 (Demographic Fairness):** Calibration reduces explanation variance from 24% to 8.7% by subtracting demographic-specific bias while preserving feature rankings (0.97 rank correlation)
>
> **Comparison with Prior Work:**
>
> Our results extend existing literature:
> - **Agreement:** Shapley values provide faithful explanations (corroborates Lundberg & Lee 2017)
> - **Extension:** Hierarchical sampling with attention guidance reduces variance by 30% (extends Mitchell et al. 2022)
> - **Novelty:** First work to apply demographic calibration to feature attributions (novel contribution to fairness in XAI)
>
> **Implications:**
>
> Our work has implications for:
> - **Theory:** Hierarchical approximation with domain priors achieves better variance-bias trade-off than uniform sampling (new theoretical insight)
> - **Practice:** ML engineers can achieve real-time, fair explanations for face recognition using E-ViT + calibration (practical recommendation)
>
> **Limitations:**
>
> We acknowledge limitations in:
> - **Methodology:** Insertion AUC measures correlation (not causation), demographic classifier has 8% error rate
> - **Scope:** Face recognition only, static images only, 8 features only
> - **Generalization:** May not generalize to non-Western faces, occluded faces, or M > 50 features
>
> These limitations do not invalidate our findings but establish their boundaries. Our work provides strong evidence for real-time, fair explainability within these bounds.
>
> **Connection to Conclusion:**
>
> In the next chapter (Chapter 8), we synthesize these findings into broader conclusions, discuss future work directions, and reflect on the contributions of this research.

**Word Count:** 400-600 words

---

## WRITING QUALITY GUIDELINES

### Interpretation vs. Speculation

**✅ Good Interpretation (Grounded in Results):**
> "The 0.76 insertion AUC indicates that our method is faithful because highly-attributed features improve predictions when added (Section 6.2)"

**❌ Over-Interpretation (Speculation):**
> "The 0.76 insertion AUC proves that users will trust our explanations"

**✅ Hedged Speculation (Acknowledges Uncertainty):**
> "The 0.76 insertion AUC suggests that users may trust our explanations, though user studies are needed to confirm this"

### Hedging Language

Use appropriate hedging when discussing implications:

| Confidence | Language |
|------------|----------|
| **Strong evidence** | "demonstrates," "shows," "indicates" |
| **Moderate evidence** | "suggests," "implies," "supports the idea that" |
| **Weak evidence** | "may suggest," "could indicate," "potentially implies" |
| **Speculation** | "we hypothesize that," "one possibility is that," "future work could explore whether" |

### Avoiding Over-Claims

**❌ Over-Claim:**
> "Our method solves the bias problem in face recognition"

**✅ Appropriate Claim:**
> "Our method reduces explanation bias across demographic groups (from 24% to 8.7% variance), though model prediction bias remains a separate concern"

**❌ Over-Claim:**
> "This proves that hierarchical SHAP is the best explainability method"

**✅ Appropriate Claim:**
> "Our results show that hierarchical SHAP outperforms the three baselines we tested (KernelSHAP, GradCAM, LIME) on face recognition tasks"

---

## QUALITY CHECKLIST

### Content Completeness
- [ ] All research questions are answered (Section 7.2)
- [ ] Answers are supported by evidence from Chapter 6
- [ ] Interpretations go beyond surface findings (explain "why")
- [ ] Comparisons with prior work are fair and comprehensive (Section 7.3)
- [ ] Theoretical implications are discussed (Section 7.4)
- [ ] Practical implications are discussed (Section 7.5)
- [ ] Limitations are honestly addressed (Section 7.6)
- [ ] Threats to validity are identified (Section 7.7)

### Interpretation Quality
- [ ] Interpretations are grounded in results (not speculation)
- [ ] Mechanisms are proposed to explain observations
- [ ] Connections to theory (Chapter 3) are explicit
- [ ] Unexpected findings are acknowledged and explained
- [ ] Hedging language is used appropriately

### Comparison with Prior Work
- [ ] Prior work is cited accurately
- [ ] Comparisons are fair (no strawman arguments)
- [ ] Contributions of prior work are acknowledged
- [ ] Differences are explained (not just stated)
- [ ] Novel contributions are clearly identified

### Limitations and Validity
- [ ] Limitations are framed as boundaries (not failures)
- [ ] Impact of each limitation is discussed
- [ ] Mitigation strategies are mentioned
- [ ] Threats to validity are categorized (internal, external, construct, statistical)
- [ ] Each threat includes description, impact, and mitigation

### Writing Quality
- [ ] Clear, concise prose
- [ ] Logical flow (introduction → interpretation → comparison → implications → limitations → summary)
- [ ] Transitions between sections are smooth
- [ ] No repetition from Chapter 6 (interpret, don't just report)
- [ ] Appropriate tone (critical but not defensive)

---

## REVISION ITERATION PROCESS

### Iteration 1: Completeness (Week 1)
**Goal:** Ensure all discussion elements are present

**Checklist:**
- [ ] All RQs have dedicated subsections (7.2.1, 7.2.2, ...)
- [ ] Each RQ answer includes: restatement, answer, evidence, interpretation
- [ ] Comparison with prior work covers agreement, disagreement, extension, novelty
- [ ] Theoretical and practical implications are discussed
- [ ] Limitations and threats to validity are identified

**Output:** Complete draft with all required sections

---

### Iteration 2: Depth of Interpretation (Week 2)
**Goal:** Move from surface to deep interpretation

**Checklist:**
- [ ] Every result has a "why did we observe this?" explanation
- [ ] Mechanisms are proposed with supporting evidence
- [ ] Connections to theory are explicit (cite Chapter 3 theorems/predictions)
- [ ] Unexpected findings are explained (not just acknowledged)
- [ ] Interpretations go beyond paraphrasing results

**Output:** Deep, mechanistic interpretations

---

### Iteration 3: Fair Comparison (Week 3)
**Goal:** Ensure prior work is treated fairly

**Checklist:**
- [ ] Every prior work mentioned is cited correctly
- [ ] Contributions of prior work are acknowledged before critiquing
- [ ] Disagreements are explained (not just stated as contradictions)
- [ ] Alternative explanations for disagreements are considered
- [ ] No strawman arguments (don't misrepresent prior work to make yours look better)

**Output:** Balanced, scholarly comparison

---

### Iteration 4: Honest Limitations (Week 4)
**Goal:** Comprehensive, honest limitation discussion

**Checklist:**
- [ ] Methodological limitations are identified (design, measurement, analysis)
- [ ] Scope limitations are explicit (what was excluded and why)
- [ ] Generalization limitations are realistic (who/what/where may findings not apply)
- [ ] Each limitation includes impact and mitigation
- [ ] Limitations don't undermine the work (frame as boundaries, not failures)
- [ ] Threats to validity cover all four types (internal, external, construct, statistical)

**Output:** Honest, comprehensive limitation section

---

### Iteration 5: Clarity and Flow (Week 5)
**Goal:** Polish writing quality

**Checklist:**
- [ ] Clear, concise prose (no jargon without definition)
- [ ] Logical section order (interpretation → comparison → implications → limitations)
- [ ] Smooth transitions between sections
- [ ] Consistent terminology (use same terms as Chapters 1-6)
- [ ] Appropriate hedging language (don't over-claim or under-claim)
- [ ] No repetition from Chapter 6 (discuss, don't just report)

**Output:** Polished, publication-ready chapter

---

### Iteration 6: Advisor Review (Week 6)
**Goal:** Incorporate advisor feedback

**Actions:**
- [ ] Send complete draft to advisor
- [ ] Ask specific questions about interpretation depth and fairness of comparisons
- [ ] Address all advisor comments
- [ ] Verify that limitations are appropriately framed
- [ ] Ensure implications are realistic (RULE 1: no false claims)

**Output:** Advisor-approved discussion chapter

---

## WHEN TO STOP ITERATING

**Stop when:**
✅ All research questions are answered
✅ Results are interpreted (not just reported)
✅ Comparisons with prior work are fair
✅ Limitations are honestly discussed
✅ Threats to validity are addressed
✅ Advisor has reviewed and approved

**Don't stop if:**
❌ RQ answers are incomplete or superficial
❌ Results are reported without interpretation
❌ Prior work is misrepresented or unfairly criticized
❌ Limitations are missing or downplayed
❌ Over-claims are present (violates RULE 1)

---

## ESTIMATED TIME INVESTMENT

| Task | Time Estimate |
|------|---------------|
| Section 7.1 (Introduction) | 2-4 hours |
| Section 7.2 (Interpretation) | 15-25 hours (main effort) |
| Section 7.3 (Comparison) | 8-12 hours |
| Section 7.4 (Theoretical Implications) | 6-10 hours |
| Section 7.5 (Practical Implications) | 6-10 hours |
| Section 7.6 (Limitations) | 6-10 hours |
| Section 7.7 (Threats to Validity) | 4-8 hours |
| Section 7.8 (Summary) | 2-4 hours |
| Revision Iterations 1-5 | 15-25 hours |
| Advisor review and revisions | 5-10 hours |
| **Total** | **69-118 hours** |

**Note:** Time varies based on:
- Complexity of results (more findings → more interpretation)
- Prior work familiarity (extensive literature review takes longer)
- Advisor feedback cycles

---

## RESOURCES

### Recommended Reading

1. **"Discussing Your Findings"** by John W. Creswell (2014)
   - Chapter in *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*

2. **"Threats to Validity"** by Wohlin et al. (2012)
   - *Experimentation in Software Engineering*

3. **"Writing the Discussion Section"** by Belcher (2009)
   - *Writing Your Journal Article in 12 Weeks*

4. **"Interpretation vs. Speculation"** by Booth et al. (2016)
   - *The Craft of Research*

### Online Resources

- **APA Style Guide:** Discussing research implications
- **Nature Author Guidelines:** Discussion section advice
- **IEEE Writing Guide:** Interpretation best practices

---

## WORD COUNT TARGET

**Overall Target:** 9,000-12,000 words

**Breakdown by Section:**
- Section 7.1 (Introduction): 300-500 words
- Section 7.2 (Interpretation of Results): 3,000-4,500 words
- Section 7.3 (Comparison with Prior Work): 1,500-2,000 words
- Section 7.4 (Theoretical Implications): 1,000-1,500 words
- Section 7.5 (Practical Implications): 1,000-1,500 words
- Section 7.6 (Limitations): 1,500-2,000 words
- Section 7.7 (Threats to Validity): 800-1,200 words
- Section 7.8 (Summary): 400-600 words

**Current Word Count:** [TRACK HERE]

---

## NOTES TO SELF

**[YOUR NOTES]**

Use this space to track:
- RQ answers to write:
- Prior work to compare:
- Limitations to address:
- Advisor questions:
- TODOs:

---

## 📚 UNIVERSAL CITATION REMINDER

**RULE 1: SCIENTIFIC TRUTH COMES FIRST**

⚠️ **CRITICAL:** Before submitting ANY section of this chapter:

- [ ] All results cited from Chapter 6 are accurate
- [ ] All prior work mentioned is cited correctly
- [ ] All theoretical connections reference Chapter 3 theorems
- [ ] Limitations are honestly stated (no hiding unfavorable findings)
- [ ] No over-claims (practical implications are realistic)
- [ ] Threats to validity are acknowledged (scientific integrity)

**"Well-known" ≠ No citation needed**

Even if a finding is well-established, cite the original source.

**See:** [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md) for detailed guidance.

---

**END OF TEMPLATE**

---

**STATUS:** ✅ Enhanced from 35% → 95% (October 10, 2025)
**Improvements:** Complete rewrite with comprehensive guidance, interpretation frameworks, comparison templates, limitation structures, validity threat analysis, quality checklists, writing guidelines, and 6-iteration revision process
