# Chapter 3: Theoretical Foundation

## Overview

This chapter presents the theoretical basis for your research. It establishes the formal foundation upon which your methodology and implementation are built. The goal is to:
- Define key concepts and notation precisely
- Present original theoretical contributions (theorems, proofs, analyses)
- Establish the correctness and properties of your approach
- Connect theory to the methodology that follows

**Target Length:** 6,000-9,000 words (adjust based on field)

**Note for Non-Mathematical Fields:** If your field doesn't emphasize formal theory, adapt this chapter to "Conceptual Framework" focusing on models, hypotheses, and theoretical underpinnings. See Field-Specific Adaptations section below.

---

## 3.1 Introduction

**Purpose:** Provide a roadmap of the theoretical contributions in this chapter and connect them to your research questions.

**What to Include:**
- Brief overview of what theoretical foundations will be presented
- Why this theory is necessary (motivation)
- How it connects to your research questions (from Chapter 1)
- Organization of this chapter (what comes in which section)
- Connection to methodology (preview how theory → practice)

**Writing Template:**

```markdown
## 3.1 Introduction

[OPENING: State the purpose]
This chapter establishes the theoretical foundation for [YOUR APPROACH]. We develop [MAIN THEORETICAL CONTRIBUTION] that enables [KEY CAPABILITY/BENEFIT].

[MOTIVATION: Why is theory needed?]
The [PROBLEM/CHALLENGE] introduced in Chapter 1 requires [THEORETICAL RESULT] because [REASON]. Existing approaches rely on [EXISTING THEORY], which [LIMITATION]. Our theoretical contribution addresses this by [YOUR INNOVATION].

[ROADMAP: Organization]
The chapter is organized as follows:
- Section 3.2 establishes preliminaries (notation, definitions, background results)
- Section 3.3 presents our main theoretical contribution: [MAIN RESULT NAME]
- Section 3.4 develops [ADDITIONAL CONTRIBUTION 1]
- Section 3.5 analyzes computational complexity and approximation guarantees
- Section 3.6 summarizes the theoretical results and their implications

[CONNECTION: Theory → Methodology]
These theoretical results form the basis for the [METHODOLOGY/ALGORITHM] presented in Chapter 4, which [HOW THEORY IS USED IN PRACTICE].
```

**Example from Computer Science:**
> This chapter establishes the theoretical foundation for FastSHAP-ViT, our real-time explainability framework for vision transformers. We develop a novel formulation of Shapley values for hypersphere embeddings that enables efficient computation without sacrificing faithfulness.
>
> The real-time explainability challenge requires reducing computational complexity from O(2^M) to O(M log M) while maintaining theoretical guarantees. Existing SHAP formulations assume Euclidean feature spaces, which are inadequate for ArcFace embeddings on hyperspheres. Our theoretical contribution extends Shapley value theory to non-Euclidean manifolds.
>
> The chapter proceeds as follows: Section 3.2 establishes preliminaries on Shapley values and hypersphere geometry. Section 3.3 presents our main result—a Shapley formulation for hypersphere embeddings with proved axioms. Section 3.4 develops the hierarchical approximation framework. Section 3.5 proves complexity reduction to O(M log M) with bounded approximation error.
>
> These theoretical results form the basis for the FastSHAP algorithm in Chapter 4, which implements the hierarchical approximation in GPU-accelerated form.

**Word Count Target:** 500-800 words

**📚 CITATION CHECK:**
- [ ] Existing theory approaches are cited
- [ ] Background Shapley/theoretical frameworks are cited
- [ ] Limitations of prior theory are cited with sources
- [ ] See [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md)

---

## 3.2 Preliminaries

**Purpose:** Establish all notation, definitions, and background results needed to understand your contributions.

**What to Include:**
- Notation conventions (Section 3.2.1)
- Key definitions (Section 3.2.2)
- Background results from literature (Section 3.2.3)

**Important:** Define BEFORE using. If you use a symbol or concept later, it must be defined here.

---

### 3.2.1 Notation

**Purpose:** Define all mathematical symbols and conventions used in this chapter.

**Structure:** Create a notation table with Symbol, Description, Example columns.

**LaTeX Template:**

```latex
\begin{table}[h]
\centering
\caption{Notation used in this chapter}
\begin{tabular}{ll}
\toprule
\textbf{Symbol} & \textbf{Description} \\
\midrule
$x \in \mathbb{R}^d$ & Input vector in $d$-dimensional Euclidean space \\
$\mathcal{X}$ & Input space (domain of inputs) \\
$f: \mathcal{X} \to \mathcal{Y}$ & Model function mapping inputs to outputs \\
$\phi(x)$ & Feature representation (embedding) \\
$S \subseteq M$ & Subset $S$ of feature set $M$ \\
$\nu(S)$ & Value function for coalition $S$ \\
$\mathbb{S}^{d-1}$ & Unit hypersphere in $d$ dimensions \\
$\langle \cdot, \cdot \rangle$ & Inner product \\
$\|\cdot\|_2$ & Euclidean (L2) norm \\
$\mathcal{O}(\cdot)$ & Big-O notation (asymptotic complexity) \\
\bottomrule
\end{tabular}
\end{table}
```

**Markdown Alternative (if not using LaTeX yet):**

| Symbol | Description |
|--------|-------------|
| $x \in \mathbb{R}^d$ | Input vector in $d$-dimensional Euclidean space |
| $\mathcal{X}$ | Input space (domain of inputs) |
| $f: \mathcal{X} \to \mathcal{Y}$ | Model function mapping inputs to outputs |
| $\phi(x)$ | Feature representation (embedding) |
| $S \subseteq M$ | Subset $S$ of feature set $M$ |

**Conventions:**
- Scalars: lowercase italic ($x, y, \alpha, \beta$)
- Vectors: lowercase bold ($\mathbf{x}, \mathbf{w}$)
- Matrices: uppercase bold ($\mathbf{X}, \mathbf{W}$)
- Sets: uppercase calligraphic ($\mathcal{X}, \mathcal{S}$)
- Functions: lowercase ($f, g, h$)
- Spaces: uppercase blackboard bold ($\mathbb{R}, \mathbb{S}$)

**Word Count:** 200-400 words (including table)

---

### 3.2.2 Definitions

**Purpose:** Provide precise, formal definitions of key concepts.

**LaTeX Definition Environment:**

```latex
\begin{definition}[Name of Concept]
\label{def:concept-name}
[Formal definition goes here, using precise mathematical language]
\end{definition}
```

**Structure for Each Definition:**
1. **Definition statement** (formal, precise)
2. **Intuitive explanation** (1-2 sentences explaining what it means)
3. **Example** (concrete instance illustrating the definition)
4. **Remark** (optional: additional context, special cases, connections)

**Template:**

```markdown
### Definition 3.1: [Concept Name]

**Formal Definition:**
[Precise mathematical statement]

**Intuition:**
[What does this mean in plain language?]

**Example:**
[Concrete instance showing the definition in action]

**Remark:**
[Additional context, special cases, or connections to other concepts]
```

**Example:**

```markdown
### Definition 3.1: Shapley Value

**Formal Definition:**
Given a cooperative game $(M, \nu)$ where $M$ is the set of players and $\nu: 2^M \to \mathbb{R}$ is a value function, the Shapley value $\phi_i$ for player $i \in M$ is:

$$\phi_i = \sum_{S \subseteq M \setminus \{i\}} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)]$$

**Intuition:**
The Shapley value distributes a total value fairly among players based on their marginal contributions to all possible coalitions. It represents the average marginal contribution of player $i$ across all permutations of players.

**Example:**
Consider a 3-player game $M = \{1, 2, 3\}$ with value function $\nu(\{1\}) = 2$, $\nu(\{2\}) = 3$, $\nu(\{1,2\}) = 7$, $\nu(\{1,2,3\}) = 12$. The Shapley value for player 1 accounts for their contribution when joining alone, with player 2, or last.

**Remark:**
The Shapley value is the unique value function satisfying four axioms: efficiency, symmetry, dummy player, and additivity (Shapley, 1953). In explainability, players are features and $\nu(S)$ is the model's prediction using feature subset $S$.
```

**How Many Definitions?**
- Include 3-8 key definitions
- Only define concepts YOU USE in your theory
- Don't define standard concepts everyone knows (define novel or field-specific ones)

**Word Count:** 600-1,000 words (all definitions combined)

**📚 CITATION CHECK:**
- [ ] Every definition from literature is cited
- [ ] Original sources for concepts are cited
- [ ] Standard textbook definitions can cite a reference textbook

---

### 3.2.3 Background Results

**Purpose:** State theorems, lemmas, or propositions from the literature that your work builds upon.

**LaTeX Theorem Environment (for background results):**

```latex
\begin{theorem}[Shapley Uniqueness (Shapley 1953)]
\label{thm:shapley-unique}
The Shapley value is the unique value function satisfying efficiency, symmetry, dummy player, and additivity.
\end{theorem}
```

**Template for Background Results:**

```markdown
### Theorem 3.1 (Background): [Name] (Citation)

**Statement:**
[Formal theorem statement]

**Reference:** [Author, Year]

**Relevance:**
[Why do we need this result? How does it connect to your work?]
```

**Example:**

```markdown
### Theorem 3.1 (Background): Shapley Axiom Characterization (Shapley, 1953)

**Statement:**
The Shapley value is the unique attribution method satisfying:
1. **Efficiency:** $\sum_{i \in M} \phi_i = \nu(M)$
2. **Symmetry:** If $\nu(S \cup \{i\}) = \nu(S \cup \{j\})$ for all $S$, then $\phi_i = \phi_j$
3. **Dummy Player:** If $\nu(S \cup \{i\}) = \nu(S)$ for all $S$, then $\phi_i = 0$
4. **Additivity:** For games $\nu_1, \nu_2$, we have $\phi(\nu_1 + \nu_2) = \phi(\nu_1) + \phi(\nu_2)$

**Reference:** Shapley (1953)

**Relevance:**
Our extension to hypersphere embeddings (Theorem 3.2) must preserve these axioms to remain a valid Shapley formulation.
```

**How Many Background Results?**
- Include 2-5 background theorems/lemmas
- Only include results you DIRECTLY USE in your proofs
- Don't include entire textbook chapters—be selective

**Important:** For background results, you do NOT need to provide proofs (they're proven in the cited work). Just state them clearly and cite the source.

**Word Count:** 400-800 words (all background results)

**📚 CITATION CHECK:**
- [ ] EVERY background theorem is cited with original source
- [ ] Page numbers included if from a book
- [ ] DOI or URL if available

---

## 3.3 [Core Theoretical Contribution 1]

**Purpose:** Present your MAIN original theoretical result.

**Rename this section** to reflect your actual contribution (e.g., "3.3 Shapley Values for Hypersphere Embeddings" or "3.3 Optimal Control Policy for Robotic Manipulation").

**Structure:**
- 3.3.1 Problem Formulation
- 3.3.2 Main Result (Theorem + Proof)
- 3.3.3 Implications (Corollaries, Discussion)
- 3.3.4 Example (Concrete Illustration)

---

### 3.3.1 Problem Formulation

**Purpose:** Formally state the problem your theory solves.

**Template:**

```markdown
### 3.3.1 Problem Formulation

**Given:** [What are the inputs/assumptions?]

**Goal:** [What do we want to achieve/compute?]

**Constraints:** [What restrictions or requirements must be satisfied?]

**Challenges:** [Why is this non-trivial? What makes it difficult?]
```

**Example:**

```markdown
### 3.3.1 Problem Formulation

**Given:**
- A face recognition model $f: \mathbb{R}^{h \times w \times 3} \to \mathbb{S}^{511}$ mapping images to L2-normalized embeddings on a 512-dimensional hypersphere
- An input face image $x$ with embedding $\phi(x) = f(x)$
- A set of $M$ interpretable features (facial regions)

**Goal:**
Compute a fair attribution $\phi_i$ for each feature $i \in M$ that quantifies its contribution to the model's prediction.

**Constraints:**
- Must satisfy Shapley axioms (efficiency, symmetry, dummy player, additivity)
- Must respect the hypersphere geometry (geodesic distances, not Euclidean)
- Must be computable in <50ms for real-time deployment

**Challenges:**
- Standard SHAP assumes Euclidean feature spaces, which violates the geometry of ArcFace embeddings
- Computing exact Shapley values requires $O(2^M)$ evaluations (intractable for $M > 20$)
- Hypersphere metric is non-linear, complicating value function definition
```

**Word Count:** 300-500 words

---

### 3.3.2 Main Result

**Purpose:** State and prove your main theoretical contribution.

**Structure:**
1. **Theorem Statement** (clear, precise, formal)
2. **Proof Strategy** (outline before diving into details)
3. **Proof** (step-by-step with justifications)
4. **QED symbol** (□ or ∎)

**LaTeX Theorem Environment:**

```latex
\begin{theorem}[Your Main Result]
\label{thm:main-result}
[Formal statement of your theorem]
\end{theorem}

\begin{proof}
[Proof goes here, step by step]
\qed
\end{proof}
```

**Template:**

```markdown
### Theorem 3.2: [Name of Your Main Result]

**Statement:**
[Formal, precise statement of what you're proving]

**Proof Strategy:**
We prove this in three steps:
1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]

**Proof:**

*Step 1: [First part of proof]*

[Detailed argument for step 1, with justifications]

*Step 2: [Second part of proof]*

[Detailed argument for step 2, with justifications]

*Step 3: [Third part of proof]*

[Detailed argument for step 3, with justifications]

Therefore, [conclusion]. □
```

**Proof Writing Best Practices:**

1. **State what you're proving clearly at the start**
   - "We will show that..." or "To prove this, we establish..."

2. **Break into labeled steps**
   - Makes proof easier to follow
   - Allows referencing steps later

3. **Justify each step**
   - Cite which definition/theorem you're using
   - Make logical connections explicit
   - Don't skip steps (no "it's obvious that...")

4. **Use equations strategically**
   - Display important equations
   - Number equations you'll reference later
   - Explain what equations mean after showing them

5. **End with QED symbol**
   - □ (open box) or ∎ (closed box)
   - Signals the proof is complete

**Example:**

```markdown
### Theorem 3.2: Shapley Values for Hypersphere Embeddings

**Statement:**
Let $f: \mathcal{X} \to \mathbb{S}^{d-1}$ be a model mapping inputs to a unit hypersphere. Define the value function $\nu(S) = \exp(-\theta \cdot d_g(\phi(x_S), \phi(x)))$ where $d_g$ is the geodesic distance on $\mathbb{S}^{d-1}$ and $x_S$ is the input with only features in $S$ present. Then the Shapley value:

$$\phi_i = \sum_{S \subseteq M \setminus \{i\}} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)]$$

satisfies all four Shapley axioms (efficiency, symmetry, dummy player, additivity) and is the unique such attribution.

**Proof Strategy:**
We prove this by verifying each axiom:
1. Efficiency: Show $\sum_{i} \phi_i = \nu(M) - \nu(\emptyset)$
2. Symmetry: Show symmetric features receive equal attributions
3. Dummy Player: Show features with no impact receive zero attribution
4. Additivity: Show linearity over value functions

**Proof:**

*Step 1: Efficiency*

By the definition of Shapley values, we have:
$$\sum_{i \in M} \phi_i = \sum_{i \in M} \sum_{S \subseteq M \setminus \{i\}} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)]$$

Rearranging the double summation by collecting terms with the same set $T = S \cup \{i\}$, we can rewrite this as:
$$\sum_{T \subseteq M} \nu(T) \cdot c_T$$

where $c_T$ counts how many times $\nu(T)$ appears with positive sign minus how many times it appears with negative sign. By combinatorial identities (see Shapley 1953, Lemma 2), we have $c_M = 1$ and $c_\emptyset = -1$, while $c_T = 0$ for all other $T$. Therefore:
$$\sum_{i \in M} \phi_i = \nu(M) - \nu(\emptyset)$$

This satisfies efficiency.

*Step 2: Symmetry*

Suppose features $i$ and $j$ are symmetric: $\nu(S \cup \{i\}) = \nu(S \cup \{j\})$ for all $S \subseteq M \setminus \{i, j\}$.

Then for any coalition $S$, the terms in the Shapley value summation for $i$ and $j$ are identical:
$$\frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)] = \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{j\}) - \nu(S)]$$

Since the summation is over all subsets $S$, we have $\phi_i = \phi_j$. This satisfies symmetry.

*Step 3: Dummy Player*

Suppose feature $i$ has no impact: $\nu(S \cup \{i\}) = \nu(S)$ for all $S \subseteq M \setminus \{i\}$.

Then every term in the Shapley value summation for $i$ is zero:
$$\nu(S \cup \{i\}) - \nu(S) = 0$$

Therefore $\phi_i = 0$. This satisfies the dummy player axiom.

*Step 4: Additivity*

Consider two value functions $\nu_1$ and $\nu_2$, and their sum $\nu = \nu_1 + \nu_2$.

The Shapley value for $\nu$ is:
$$\phi_i(\nu) = \sum_{S \subseteq M \setminus \{i\}} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)]$$

Expanding $\nu = \nu_1 + \nu_2$:
$$\phi_i(\nu) = \sum_{S} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [(\nu_1(S \cup \{i\}) + \nu_2(S \cup \{i\})) - (\nu_1(S) + \nu_2(S))]$$

$$= \sum_{S} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu_1(S \cup \{i\}) - \nu_1(S)] + \sum_{S} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu_2(S \cup \{i\}) - \nu_2(S)]$$

$$= \phi_i(\nu_1) + \phi_i(\nu_2)$$

This satisfies additivity.

Since our formulation satisfies all four axioms, it is a valid Shapley value. By Theorem 3.1 (Shapley 1953), it is the unique such attribution. □
```

**Word Count:** 1,000-2,000 words (depends on proof complexity)

**📚 CITATION CHECK:**
- [ ] Background results used in the proof are cited
- [ ] Proof techniques borrowed from literature are cited
- [ ] Lemmas from other papers are cited with theorem numbers

---

### 3.3.3 Implications

**Purpose:** Derive corollaries and discuss what the main result means.

**Structure:**
1. **Corollaries** (immediate consequences of the theorem)
2. **Discussion** (what does it mean? why is it significant?)

**LaTeX Corollary Environment:**

```latex
\begin{corollary}
\label{cor:corollary-name}
[Statement of corollary]
\end{corollary}

\begin{proof}
[Proof, often brief since it follows from the main theorem]
\qed
\end{proof}
```

**Template:**

```markdown
### 3.3.3 Implications

**Corollary 3.1:** [Statement]

*Proof:* [Brief proof following from Theorem 3.2]

**Discussion:**

Our main result (Theorem 3.2) has several significant implications:

1. **[Implication 1]:** [Explanation]

2. **[Implication 2]:** [Explanation]

3. **[Implication 3]:** [Explanation]

**Comparison with Existing Approaches:**

[How does your theoretical result compare to prior work? What advantages does it have?]
```

**Example:**

```markdown
### 3.3.3 Implications

**Corollary 3.1:** The hypersphere Shapley value reduces to standard SHAP when the embedding space is Euclidean (geodesic distance = Euclidean distance).

*Proof:* On a Euclidean space, geodesic distance $d_g(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|_2$. Substituting into the value function $\nu(S) = \exp(-\theta \cdot d_g(\phi(x_S), \phi(x)))$ yields the standard SHAP value function for additive models. By uniqueness (Theorem 3.2), the resulting Shapley values are identical to standard SHAP. □

**Discussion:**

Our main result (Theorem 3.2) has several significant implications:

1. **Generalization of SHAP:** Our formulation extends SHAP beyond Euclidean feature spaces to hypersphere geometries commonly used in metric learning (ArcFace, CosFace, SphereFace). This enables explainability for face recognition systems without violating their geometric structure.

2. **Theoretical Guarantees:** By preserving all four Shapley axioms, our method inherits the fairness properties of game theory. Explanations are guaranteed to be fair allocations of prediction "credit" among features.

3. **Metric-Agnostic Framework:** The geodesic distance can be replaced with other metrics (e.g., hyperbolic distance for hierarchical embeddings), making this framework applicable to diverse representation spaces.

**Comparison with Existing Approaches:**

Existing SHAP methods (Lundberg & Lee 2017; Lundberg et al. 2020) assume additive feature contributions in Euclidean space. When applied to hypersphere embeddings:
- They violate the geometry of the embedding space (treating $\|\phi(x) - \phi(x_S)\|_2$ as meaningful when $\phi$ lives on a hypersphere)
- They lose theoretical guarantees (axioms no longer hold)
- They produce misleading explanations (attributions don't sum correctly)

Our approach addresses these issues by respecting the native geometry of the embedding space.
```

**Word Count:** 500-800 words

---

### 3.3.4 Example

**Purpose:** Illustrate the main result with a concrete, worked-out example.

**Template:**

```markdown
### 3.3.4 Example

**Setup:**
[Describe the concrete scenario]

**Application:**
[Apply your theorem to this scenario step-by-step]

**Result:**
[What is the outcome? What does it show?]

**Interpretation:**
[What does this example demonstrate about your theory?]
```

**Example:**

```markdown
### 3.3.4 Example: Face Recognition with Three Features

**Setup:**
Consider a simplified face recognition model with $M = 3$ features: eyes (E), nose (N), mouth (M). The model produces embeddings on a unit circle (2D hypersphere): $\mathbb{S}^1$.

Suppose:
- Full face embedding: $\phi(x_{ENM}) = (1, 0)$ (angle 0°)
- Eyes only: $\phi(x_E) = (0.707, 0.707)$ (angle 45°)
- Nose only: $\phi(x_N) = (0, 1)$ (angle 90°)
- Mouth only: $\phi(x_M) = (0.707, 0.707)$ (angle 45°)

**Application:**
Using our hypersphere SHAP formulation (Theorem 3.2) with $\theta = 1$:

1. Compute geodesic distances (angles on circle):
   - $d_g(\phi(x_E), \phi(x_{ENM})) = 45° = \pi/4$ radians
   - $d_g(\phi(x_N), \phi(x_{ENM})) = 90° = \pi/2$ radians
   - $d_g(\phi(x_M), \phi(x_{ENM})) = 45° = \pi/4$ radians

2. Compute value function:
   - $\nu(E) = \exp(-\pi/4) = 0.456$
   - $\nu(N) = \exp(-\pi/2) = 0.208$
   - $\nu(M) = \exp(-\pi/4) = 0.456$
   - $\nu(ENM) = \exp(0) = 1.000$

3. Apply Shapley formula:
   $$\phi_E = \frac{1}{3!} \sum_{\text{permutations}} \text{marginal contribution of E}$$

   Working through all 6 permutations and averaging marginal contributions:
   - $\phi_E = 0.312$
   - $\phi_N = 0.145$
   - $\phi_M = 0.312$

4. Verify efficiency: $\phi_E + \phi_N + \phi_M = 0.769 \approx \nu(ENM) - \nu(\emptyset) = 1.0 - 0.208 = 0.792$ ✓

**Result:**
Eyes and mouth receive equal attribution (0.312 each) while the nose receives less (0.145), reflecting their relative importance in the geodesic distance to the full-face embedding.

**Interpretation:**
This example demonstrates:
- Symmetry: Eyes and mouth have equivalent geodesic distances, so they receive equal Shapley values
- Geometry-awareness: The nose's larger angle (90° vs 45°) results in lower attribution
- Efficiency: Attributions sum to the total value (within numerical precision)
- Contrast with Euclidean SHAP: If we used Euclidean distances instead, we'd violate the circular geometry and get incorrect attributions
```

**Word Count:** 400-700 words

---

## 3.4 [Core Theoretical Contribution 2]

**Purpose:** Present a secondary theoretical result (if applicable).

**Structure:** Follow the same structure as Section 3.3:
- 3.4.1 Problem Formulation
- 3.4.2 Main Result (Theorem + Proof)
- 3.4.3 Implications
- 3.4.4 Example

**When to Include Section 3.4:**
- If you have multiple independent theoretical contributions
- If you have a second major result building on Section 3.3
- If your work has distinct theoretical components

**When to Skip Section 3.4:**
- If you have only one main theoretical contribution (just use Section 3.3)
- If additional results are minor (include as corollaries in 3.3.3 instead)

**Rename this section** to reflect your actual contribution (e.g., "3.4 Hierarchical Approximation Framework" or "3.4 Convergence Guarantees").

**Word Count (if included):** 1,500-2,500 words

---

## 3.5 Computational Analysis

**Purpose:** Analyze the computational properties of your theoretical contributions (complexity, approximation bounds, etc.).

**What to Include:**
- Time and space complexity analysis
- Approximation guarantees (if applicable)
- Scalability properties

**Note:** If your work is not computational, adapt this to "Theoretical Properties" (e.g., convergence rates, sample complexity, statistical properties).

---

### 3.5.1 Complexity Analysis

**Purpose:** Prove the computational complexity of your method.

**Template:**

```markdown
### 3.5.1 Complexity Analysis

**Theorem 3.X: Time Complexity**

*Statement:* [Formal complexity bound]

*Proof:*

[Step-by-step analysis counting operations]

**Theorem 3.Y: Space Complexity**

*Statement:* [Formal space bound]

*Proof:*

[Analysis of memory requirements]

**Comparison with Baselines:**

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| Baseline 1 | $O(...)$ | $O(...)$ |
| Baseline 2 | $O(...)$ | $O(...)$ |
| **Our Method** | **$O(...)$** | **$O(...)$** |

**Discussion:**
[What does this complexity mean in practice? How does it scale?]
```

**Example:**

```markdown
### 3.5.1 Complexity Analysis

**Theorem 3.3: Hierarchical SHAP Time Complexity**

*Statement:* The hierarchical SHAP approximation computes Shapley values in $O(M \log M + K \cdot D)$ time, where $M$ is the number of features, $K$ is the number of samples per level, and $D$ is the model forward pass time.

*Proof:*

1. **Hierarchical Structure:** The feature set $M$ is organized into $L = \lceil \log_2 M \rceil$ levels of a binary tree.

2. **Samples Per Level:** At each level $\ell$, we sample $K$ coalitions. Total samples = $K \cdot L = K \log_2 M$.

3. **Model Evaluations:** Each sample requires one forward pass taking $O(D)$ time. Total model evaluation time = $O(K \log M \cdot D)$.

4. **Shapley Aggregation:** Combining results from all levels requires summing $L$ values per feature, taking $O(M \log M)$ time.

5. **Total:** $O(M \log M + K \log M \cdot D) = O(M \log M + K \cdot D)$ since $D$ dominates and $K$ is constant. □

**Theorem 3.4: Space Complexity**

*Statement:* The hierarchical SHAP approximation requires $O(M + K)$ space.

*Proof:*

1. **Feature Hierarchy:** Storing the binary tree structure requires $O(M)$ space (2 pointers per node).

2. **Sample Storage:** At each level, we store $K$ coalition samples and their values, requiring $O(K)$ space.

3. **Reuse Across Levels:** We process levels sequentially and reuse sample storage, so space is not multiplied by $L$.

4. **Total:** $O(M + K)$ space. □

**Comparison with Baselines:**

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| Exact SHAP | $O(2^M \cdot D)$ | $O(2^M)$ |
| KernelSHAP (Lundberg & Lee 2017) | $O(K \cdot M \cdot D)$ | $O(M)$ |
| **Hierarchical SHAP (Ours)** | **$O(M \log M + K \cdot D)$** | **$O(M + K)$** |

**Discussion:**
Our method achieves exponential speedup over exact SHAP ($2^M \to M \log M$) while maintaining linear space complexity. Compared to KernelSHAP, we reduce the sample dependency from $O(K \cdot M)$ to $O(K)$ by exploiting hierarchical structure. For typical values ($M = 20$, $K = 100$, $D = 10$ ms), our method computes Shapley values in ~15 ms compared to KernelSHAP's ~200 ms.
```

**Word Count:** 600-1,000 words

---

### 3.5.2 Approximation Guarantees

**Purpose:** Prove bounds on approximation error (if your method is approximate).

**Template:**

```markdown
### 3.5.2 Approximation Guarantees

**Theorem 3.X: Approximation Error Bound**

*Statement:* [Formal bound on error]

*Proof:*

[Step-by-step analysis deriving the bound]

**Discussion:**
[What does this bound mean? Under what conditions is error small?]
```

**Example:**

```markdown
### 3.5.2 Approximation Guarantees

**Theorem 3.5: Hierarchical SHAP Approximation Error**

*Statement:* Let $\phi_i^{\text{exact}}$ be the exact Shapley value and $\phi_i^{\text{approx}}$ be the hierarchical approximation using $K$ samples per level. With probability at least $1 - \delta$:

$$|\phi_i^{\text{exact}} - \phi_i^{\text{approx}}| \leq \epsilon = O\left(\frac{R}{\sqrt{K}} \log \frac{1}{\delta}\right)$$

where $R$ is the range of the value function.

*Proof:*

1. **Monte Carlo Sampling Error:** At each level $\ell$, we estimate the expected marginal contribution by sampling $K$ coalitions. By Hoeffding's inequality, the sampling error for level $\ell$ is bounded:
   $$P(|\mathbb{E}[\Delta_i^\ell] - \hat{\mathbb{E}}[\Delta_i^\ell]| > \epsilon_\ell) \leq 2 \exp\left(-\frac{2K\epsilon_\ell^2}{R^2}\right)$$

2. **Setting $\epsilon_\ell$:** To achieve probability $1 - \delta/L$ at level $\ell$, set:
   $$\epsilon_\ell = R\sqrt{\frac{\log(2L/\delta)}{2K}}$$

3. **Union Bound:** The total error across $L = \log_2 M$ levels is:
   $$|\phi_i^{\text{exact}} - \phi_i^{\text{approx}}| \leq \sum_{\ell=1}^{L} |\mathbb{E}[\Delta_i^\ell] - \hat{\mathbb{E}}[\Delta_i^\ell]| \leq L \cdot \epsilon_\ell$$

4. **Substituting $L = \log M$:**
   $$\epsilon = L \cdot R\sqrt{\frac{\log(2L/\delta)}{2K}} = O\left(\frac{R}{\sqrt{K}} \log M \log \frac{1}{\delta}\right)$$

   For typical values ($R = 1$, $\delta = 0.05$), this simplifies to $O(R/\sqrt{K})$. □

**Discussion:**
The approximation error decreases as $O(1/\sqrt{K})$, meaning 4× more samples halve the error. For $K = 100$ samples and $R = 1$, the error is ~0.1, which is acceptable for explanations (exact values are rarely needed—relative rankings are more important). The logarithmic dependence on $M$ shows the hierarchical structure limits error growth as feature count increases.
```

**Word Count (if included):** 500-800 words

---

## 3.6 Summary

**Purpose:** Recap the key theoretical results and connect them to the next chapter.

**What to Include:**
- List of main contributions (theorems proven)
- Key properties established
- Preview of how theory is implemented (transition to Chapter 4)

**Template:**

```markdown
## 3.6 Summary

This chapter established the theoretical foundation for [YOUR APPROACH]. We presented the following contributions:

1. **[Contribution 1]:** [Brief description]
   - Theorem 3.X: [Result]
   - Key property: [What was shown]

2. **[Contribution 2]:** [Brief description]
   - Theorem 3.Y: [Result]
   - Key property: [What was shown]

3. **[Contribution 3]:** [Brief description]
   - Theorem 3.Z: [Result]
   - Key property: [What was shown]

**Key Properties Established:**
- [Property 1]: [Description]
- [Property 2]: [Description]
- [Property 3]: [Description]

**Theoretical Guarantees:**
Our formulation provides [GUARANTEES] while achieving [COMPLEXITY/EFFICIENCY RESULT].

**Connection to Methodology:**
These theoretical results form the basis for the [SYSTEM/ALGORITHM] described in Chapter 4. Specifically:
- Theorem 3.X enables [PRACTICAL COMPONENT 1]
- Theorem 3.Y enables [PRACTICAL COMPONENT 2]
- The complexity analysis (Section 3.5) guides [IMPLEMENTATION CHOICES]

In the next chapter, we describe how these theoretical contributions are implemented in a practical system and evaluate their real-world performance.
```

**Example:**

```markdown
## 3.6 Summary

This chapter established the theoretical foundation for FastSHAP-ViT, our real-time explainability framework for vision transformers. We presented the following contributions:

1. **Shapley Values for Hypersphere Embeddings (Section 3.3):**
   - Theorem 3.2: Extended SHAP to hypersphere geometries using geodesic distances
   - Key property: Preserves all four Shapley axioms (efficiency, symmetry, dummy, additivity)
   - Corollary 3.1: Reduces to standard SHAP in Euclidean case

2. **Hierarchical Approximation Framework (Section 3.4):**
   - Theorem 3.3: Binary tree structure reduces complexity from $O(2^M)$ to $O(M \log M)$
   - Key property: Preserves relative importance rankings with bounded error

3. **Computational Guarantees (Section 3.5):**
   - Theorem 3.4: $O(M \log M + K \cdot D)$ time complexity with $O(M + K)$ space
   - Theorem 3.5: Approximation error bounded by $O(R/\sqrt{K})$ with high probability
   - Comparison: 100× speedup over exact SHAP, 10× over KernelSHAP

**Key Properties Established:**
- **Theoretical Validity:** Our formulation is a true Shapley value (satisfies all axioms)
- **Geometric Correctness:** Respects hypersphere geometry (geodesic distances)
- **Computational Efficiency:** Achieves real-time performance (<50ms target feasible)
- **Approximation Quality:** Error decreases as $O(1/\sqrt{K})$ with sample count

**Theoretical Guarantees:**
Our formulation provides fairness guarantees from game theory (Shapley axioms) while achieving $O(M \log M)$ complexity, making real-time explainability tractable for production face recognition systems.

**Connection to Methodology:**
These theoretical results form the basis for the FastSHAP-ViT system described in Chapter 4. Specifically:
- Theorem 3.2 guides the design of the hypersphere-aware value function
- Theorem 3.3 enables the hierarchical sampling strategy for feature coalitions
- The complexity analysis (Section 3.5) informs GPU parallelization choices and memory management
- Theorem 3.5 determines the number of samples $K$ needed to achieve target accuracy (0.7 insertion AUC)

In the next chapter, we describe how these theoretical contributions are implemented in a GPU-accelerated PyTorch framework and integrated into the E-ViT architecture.
```

**Word Count:** 400-600 words

---

## MATHEMATICAL WRITING GUIDELINES

### LaTeX Environments

**Definition Environment:**
```latex
\begin{definition}[Concept Name]
\label{def:concept-name}
Formal definition text here.
\end{definition}
```

**Theorem Environment:**
```latex
\begin{theorem}[Theorem Name]
\label{thm:theorem-name}
Formal theorem statement here.
\end{theorem}
```

**Lemma Environment:**
```latex
\begin{lemma}[Lemma Name]
\label{lem:lemma-name}
Auxiliary result statement here.
\end{lemma}
```

**Proof Environment:**
```latex
\begin{proof}
Proof text here, step by step.
\qed
\end{proof}
```

**Corollary Environment:**
```latex
\begin{corollary}
\label{cor:corollary-name}
Immediate consequence of theorem.
\end{corollary}
```

**Remark Environment:**
```latex
\begin{remark}
Additional context or special cases.
\end{remark}
```

### Proof Writing Tips

1. **State what you're proving:**
   - "We will show that..."
   - "To prove this, we establish..."
   - "It suffices to show that..."

2. **Break into labeled steps:**
   ```markdown
   *Step 1: Establish X*
   [Argument for X]

   *Step 2: Show Y follows from X*
   [Argument for Y]

   *Step 3: Conclude Z*
   [Final argument]
   ```

3. **Justify each step:**
   - "By Definition 3.1, we have..."
   - "Applying Theorem 3.2 with $S = ...$, we get..."
   - "From the triangle inequality, ..."

4. **End with QED:**
   - Use □ (open box) or ∎ (closed box)
   - In LaTeX: `\qed` inside proof environment
   - Signals the proof is complete

5. **Avoid "Obviously" and "Clearly":**
   - If it's obvious, prove it briefly
   - What's clear to you may not be clear to readers
   - Better: "By direct computation, ..." or "It follows immediately that..."

### Common Proof Techniques

**Direct Proof:**
```markdown
**Theorem:** If P, then Q.

**Proof:**
Assume P. [Show Q follows step by step]. Therefore Q. □
```

**Proof by Contradiction:**
```markdown
**Theorem:** Statement S is true.

**Proof:**
Assume for contradiction that S is false. [Derive a contradiction]. This contradicts [known fact]. Therefore S must be true. □
```

**Proof by Induction:**
```markdown
**Theorem:** Property P(n) holds for all n ≥ 1.

**Proof:**

*Base Case:* P(1) is true because [verification].

*Inductive Step:* Assume P(k) is true for some k ≥ 1. We show P(k+1).
[Proof that P(k) implies P(k+1)]

By induction, P(n) holds for all n ≥ 1. □
```

**Proof by Construction:**
```markdown
**Theorem:** There exists an X such that property P holds.

**Proof:**
We construct X as follows: [explicit construction].
We verify P: [check that P holds for constructed X]. □
```

### Equation Formatting

**Inline Equations:** Use $...$ for inline math:
```markdown
Let $x \in \mathbb{R}^d$ be a vector.
```

**Display Equations:** Use $$...$$ for centered, important equations:
```markdown
$$\phi_i = \sum_{S \subseteq M \setminus \{i\}} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)]$$
```

**Numbered Equations:** Use `\begin{equation}` for equations you'll reference:
```latex
\begin{equation}
\label{eq:shapley-formula}
\phi_i = \sum_{S \subseteq M \setminus \{i\}} \frac{|S|! (|M| - |S| - 1)!}{|M|!} [\nu(S \cup \{i\}) - \nu(S)]
\end{equation}
```

**Multi-line Equations:** Use `align` for multi-step derivations:
```latex
\begin{align}
\phi_i &= \sum_{S \subseteq M \setminus \{i\}} w(|S|) [\nu(S \cup \{i\}) - \nu(S)] \label{eq:step1} \\
       &= \sum_{S} w(|S|) \cdot \Delta_i(S) \label{eq:step2} \\
       &= \mathbb{E}_S[\Delta_i(S)] \label{eq:step3}
\end{align}
```

**Equation Referencing:**
```markdown
As shown in Equation \ref{eq:shapley-formula}, the Shapley value...
```

### Common Mathematical Symbols

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $\in$ | `\in` | Element of |
| $\subseteq$ | `\subseteq` | Subset of |
| $\mathbb{R}$ | `\mathbb{R}` | Real numbers |
| $\mathbb{S}^{d-1}$ | `\mathbb{S}^{d-1}` | (d-1)-sphere |
| $\mathcal{X}$ | `\mathcal{X}` | Space/set (calligraphic) |
| $\sum_{i=1}^{n}$ | `\sum_{i=1}^{n}` | Summation |
| $\prod_{i=1}^{n}$ | `\prod_{i=1}^{n}` | Product |
| $\langle \mathbf{u}, \mathbf{v} \rangle$ | `\langle \mathbf{u}, \mathbf{v} \rangle` | Inner product |
| $\|\mathbf{x}\|_2$ | `\|\mathbf{x}\|_2` | L2 norm |
| $\mathcal{O}(n)$ | `\mathcal{O}(n)` | Big-O notation |
| $\Theta(n)$ | `\Theta(n)` | Theta notation |
| $\Omega(n)$ | `\Omega(n)` | Omega notation |
| $\forall$ | `\forall` | For all |
| $\exists$ | `\exists` | There exists |
| $\implies$ | `\implies` | Implies |
| $\iff$ | `\iff` | If and only if |
| $\emptyset$ | `\emptyset` | Empty set |
| $\approx$ | `\approx` | Approximately equal |
| $\leq, \geq$ | `\leq, \geq` | Less/greater than or equal |

---

## FIELD-SPECIFIC ADAPTATIONS

### Computer Science / Machine Learning

**Emphasis:**
- Algorithms and pseudocode
- Complexity analysis (time, space, sample complexity)
- Worst-case and average-case analysis
- Approximation guarantees
- Convergence proofs

**Structure:**
- Section 3.3: Algorithm design and correctness
- Section 3.4: Complexity analysis
- Section 3.5: Approximation or convergence guarantees

**Example Theorems:**
- Theorem: Algorithm X computes Y in O(n log n) time
- Theorem: The approximation error is bounded by ε with probability 1-δ
- Theorem: The neural network converges to a local minimum under conditions Z

### Pure Mathematics

**Emphasis:**
- Full formal rigor
- More proofs, fewer examples
- Detailed derivations
- Connections to existing theory
- Axioms and foundations

**Structure:**
- Section 3.3: Main theorem with complete proof
- Section 3.4: Corollaries and special cases
- Section 3.5: Extensions and generalizations

**Example Theorems:**
- Theorem: A function with property P satisfies Q
- Lemma: Under assumptions X, result Y holds
- Corollary: As a special case of Theorem 3.2, we have Z

### Engineering / Applied Sciences

**Emphasis:**
- Practical implications
- Numerical results and simulations
- Design trade-offs
- Robustness and stability
- Performance bounds

**Structure:**
- Section 3.3: System model and equations
- Section 3.4: Stability analysis
- Section 3.5: Performance bounds and trade-offs

**Example Theorems:**
- Theorem: The control system is stable for gains in range [a, b]
- Proposition: The filter attenuates noise by at least X dB
- Lemma: The system converges within T time units

### Social Sciences / Qualitative Fields

**Adaptation:** Replace "Theoretical Foundation" with **"Conceptual Framework"**

**Emphasis:**
- Theoretical models and frameworks
- Hypotheses and propositions (not theorems)
- Conceptual relationships
- Literature-based frameworks
- Operationalization of concepts

**Structure:**
- Section 3.2: Key concepts and definitions (from literature)
- Section 3.3: Conceptual model (diagram showing relationships)
- Section 3.4: Hypotheses or propositions
- Section 3.5: Operationalization (how concepts are measured)

**Example Propositions:**
- Proposition: Variable X influences variable Y through mediator Z
- Hypothesis: Intervention A will increase outcome B
- Framework: The relationship between C and D is moderated by E

---

## QUALITY CHECKLIST

### Mathematical Rigor
- [ ] All notation is defined before use (Section 3.2.1)
- [ ] All technical terms have precise definitions (Section 3.2.2)
- [ ] Theorems are clearly stated with hypotheses and conclusions
- [ ] Proofs are correct and complete (no logical gaps)
- [ ] Assumptions are explicitly stated
- [ ] Edge cases are addressed
- [ ] Special cases are noted (e.g., when does theorem not apply?)

### Clarity
- [ ] Intuition provided before formal statements
- [ ] Examples illustrate abstract concepts (Section 3.3.4, etc.)
- [ ] Figures visualize key ideas (see Figure Recommendations below)
- [ ] Notation is consistent throughout
- [ ] Proofs are broken into labeled steps
- [ ] Technical jargon is explained

### Citations
- [ ] Background results are cited (Section 3.2.3)
- [ ] Definitions from literature are cited
- [ ] Proof techniques from other papers are cited
- [ ] Similar results in literature are acknowledged
- [ ] Notation conventions are cited (if borrowed)
- [ ] All citations have complete information (author, year, venue)

### Organization
- [ ] Results build logically (dependencies clear)
- [ ] Each theorem/lemma is necessary (no redundant results)
- [ ] No circular reasoning (don't use Theorem X to prove Lemma Y if Lemma Y is used in Theorem X)
- [ ] Dependency structure is clear (lemmas before theorems that use them)
- [ ] Sections flow naturally (introduction → preliminaries → contributions → summary)

### Connections
- [ ] Chapter 1 research questions are addressed
- [ ] Connection to methodology (Chapter 4) is explicit
- [ ] Contributions listed in Chapter 1 match what's proven here
- [ ] Consistent with claims in abstract and conclusion

### Completeness
- [ ] All main theoretical contributions are presented
- [ ] Complexity analysis is included (if applicable)
- [ ] Approximation bounds are provided (if approximate method)
- [ ] Examples illustrate key results
- [ ] Summary ties everything together

---

## FIGURE RECOMMENDATIONS

### Figure 3.1: Conceptual Framework Diagram

**Purpose:** High-level visualization of the theoretical framework

**What to Include:**
- Key components of your theory
- Relationships between components
- Inputs and outputs
- Flow of information or dependencies

**Tool Recommendations:**
- Draw.io (free, web-based)
- PowerPoint/Keynote (good for block diagrams)
- TikZ (LaTeX, professional quality)

**Example:** Block diagram showing "Feature Space → Value Function → Shapley Computation → Attribution Scores" with mathematical notation on arrows.

---

### Figure 3.2: Visualization of Main Result

**Purpose:** Visual proof or illustration of the main theorem

**What to Include:**
- Geometric interpretation (if applicable)
- Before/after comparison
- Visualization of proof idea

**Examples:**
- Geometric diagram showing geodesic distance on a hypersphere
- Tree diagram showing hierarchical structure
- Plot showing convergence behavior

---

### Figure 3.3: Example Illustration

**Purpose:** Concrete example from Section 3.3.4 visualized

**What to Include:**
- Input and output of example
- Step-by-step process
- Key values labeled

**Example:** Face image with three highlighted regions (eyes, nose, mouth) and their Shapley values shown as bars.

---

### Figure 3.4: Comparison with Alternatives

**Purpose:** Show advantages of your approach vs. existing methods

**What to Include:**
- Comparison matrix or table
- Performance plots (complexity vs. accuracy)
- Venn diagram showing which properties each method satisfies

**Example:** Table showing which methods satisfy Shapley axioms (checkmarks and X marks).

---

### TikZ Examples for Common Diagrams

**Tree Diagram:**
```latex
\begin{tikzpicture}
\node {Root}
  child {node {Left Subtree}}
  child {node {Right Subtree}};
\end{tikzpicture}
```

**Block Diagram:**
```latex
\begin{tikzpicture}
\node[draw, rectangle] (A) {Component A};
\node[draw, rectangle, right=of A] (B) {Component B};
\draw[->] (A) -- (B) node[midway, above] {Flow};
\end{tikzpicture}
```

**Geometric Diagram:**
```latex
\begin{tikzpicture}
\draw (0,0) circle (2cm);
\draw[->] (0,0) -- (45:2) node[midway, above] {$\phi(x)$};
\draw[->] (0,0) -- (90:2) node[midway, left] {$\phi(x_S)$};
\end{tikzpicture}
```

---

## REVISION ITERATION PROCESS

### Iteration 1: Proof Correctness (Week 1)
**Goal:** Ensure all proofs are logically sound

**Checklist:**
- [ ] Every theorem has a complete proof
- [ ] Every step in each proof is justified
- [ ] No logical gaps ("it's obvious" → make it explicit)
- [ ] Check for circular reasoning
- [ ] Verify base cases in inductive proofs
- [ ] Test proofs with edge cases
- [ ] **Advisor review checkpoint:** Send Section 3.3 for feedback on proof correctness

**Output:** Mathematically correct proofs

---

### Iteration 2: Mathematical Rigor (Week 2)
**Goal:** Verify all formal elements are precise

**Checklist:**
- [ ] All notation defined in Section 3.2.1
- [ ] All terms defined in Section 3.2.2
- [ ] Theorem statements are precise (no ambiguity)
- [ ] Assumptions are explicit (not hidden)
- [ ] Constraints are stated clearly
- [ ] Domain and range specified for all functions
- [ ] Quantifiers used correctly (∀, ∃)

**Output:** Formally rigorous chapter with no undefined terms

---

### Iteration 3: Clarity and Intuition (Week 3)
**Goal:** Make the theory accessible and understandable

**Checklist:**
- [ ] Intuitive explanation before formal statements
- [ ] Examples illustrate abstract concepts
- [ ] Figures visualize key ideas (create 3-4 figures)
- [ ] Proof strategies outlined before diving into details
- [ ] Complex proofs broken into labeled steps
- [ ] Technical jargon explained or defined
- [ ] Transitions between sections are smooth

**Output:** Clear chapter that non-experts can follow

---

### Iteration 4: Organization and Flow (Week 4)
**Goal:** Ensure logical structure and dependencies

**Checklist:**
- [ ] Introduction provides clear roadmap
- [ ] Preliminaries include all needed background
- [ ] Results build in logical order (lemmas → theorems)
- [ ] No forward references (don't use Theorem 3.5 before stating it)
- [ ] Section 3.6 summary ties everything together
- [ ] Connection to Chapter 4 is explicit
- [ ] Dependency structure is clear (draw dependency graph if needed)

**Output:** Well-organized chapter with natural flow

---

### Iteration 5: Citations and Formatting (Week 5)
**Goal:** Complete references and polish presentation

**Checklist:**
- [ ] Every background result cited (Section 3.2.3)
- [ ] Definitions from literature cited
- [ ] Proof techniques from other papers cited
- [ ] Similar results acknowledged and cited
- [ ] All citations have complete information
- [ ] LaTeX formatting is correct (compile without errors)
- [ ] Equation numbers are correct and referenced
- [ ] Figures have captions and are referenced in text
- [ ] Consistent notation throughout
- [ ] Grammar and spelling checked

**Output:** Polished, publication-ready chapter

---

### Iteration 6: Final Advisor Review (Week 6)
**Goal:** Incorporate final feedback

**Actions:**
- [ ] Send complete draft to advisor
- [ ] Prepare list of specific questions
- [ ] Address all advisor comments
- [ ] Verify correctness of any changes
- [ ] Update other chapters if theory changed

**Output:** Advisor-approved theoretical foundation

---

## WHEN TO STOP ITERATING

**Stop when:**
✅ All proofs are correct and complete
✅ All notation and terms are defined
✅ Examples illustrate key concepts
✅ Figures visualize main ideas
✅ Advisor has reviewed and approved
✅ Citations are complete and accurate
✅ Chapter connects clearly to methodology (Chapter 4)

**Don't stop if:**
❌ Proofs have logical gaps
❌ Assumptions are unstated or unclear
❌ Theorems are ambiguous
❌ Advisor has unresolved concerns
❌ Citations are missing
❌ Notation is inconsistent

---

## ESTIMATED TIME INVESTMENT

| Task | Time Estimate |
|------|---------------|
| Section 3.1 (Introduction) | 2-4 hours |
| Section 3.2 (Preliminaries) | 4-8 hours |
| Section 3.3 (Main Contribution) | 15-30 hours |
| Section 3.4 (Additional Contribution) | 10-20 hours |
| Section 3.5 (Computational Analysis) | 6-12 hours |
| Section 3.6 (Summary) | 2-4 hours |
| Figures (3-4 figures) | 4-8 hours |
| Revision Iterations 1-5 | 15-25 hours |
| Advisor review and revisions | 5-10 hours |
| **Total** | **63-121 hours** |

**Note:** Time varies significantly based on:
- Complexity of theory (simple algorithm vs. novel mathematical framework)
- Your proof-writing experience
- Advisor feedback cycles
- Figure creation complexity

---

## RESOURCES

### Recommended Reading on Mathematical Writing

1. **"Writing Mathematics Well"** by Leonard Gillman (1987)
   - Short, practical guide to mathematical exposition

2. **"A Primer of Mathematical Writing"** by Steven G. Krantz (1997)
   - Comprehensive guide with examples

3. **"How to Write Mathematics"** by Norman Steenrod et al. (1973)
   - Classic advice from leading mathematicians

4. **"Mathematical Writing"** by Donald Knuth, Tracy Larrabee, Paul Roberts (1989)
   - From Stanford's mathematical writing course

### Online Resources

- **LaTeX Tutorial:** Overleaf Learn (overleaf.com/learn)
- **Proof Writing:** MIT OpenCourseWare "Mathematics for Computer Science"
- **TikZ Examples:** TeXample.net
- **Symbol Lookup:** Detexify (detexify.kirelabs.org/classify.html)

### Example Dissertations (Theory-Heavy)

- Look for dissertations in your field with "Theoretical Foundations" chapters
- Check your advisor's former students' theses
- Search ProQuest Dissertations & Theses database

---

## WORD COUNT TARGET

**Overall Target:** 6,000-9,000 words

**Breakdown by Section:**
- Section 3.1 (Introduction): 500-800 words
- Section 3.2 (Preliminaries): 1,200-2,200 words
- Section 3.3 (Main Contribution): 2,500-4,000 words
- Section 3.4 (Additional Contribution, if included): 1,500-2,500 words
- Section 3.5 (Computational Analysis): 1,000-1,800 words
- Section 3.6 (Summary): 400-600 words

**Current Word Count:** [TRACK HERE]

**Note:** Word counts include equations, but not figure captions or references.

---

## NOTES TO SELF

**[YOUR NOTES]**

Use this space to track:
- Theorems to prove:
- Proofs that need revision:
- Figures to create:
- Advisor questions:
- TODOs:

---

## 📚 UNIVERSAL CITATION REMINDER

**RULE 1: SCIENTIFIC TRUTH COMES FIRST**

⚠️ **CRITICAL:** Before submitting ANY section of this chapter:

- [ ] Every definition from literature is cited
- [ ] Every background theorem is cited with source
- [ ] Every proof technique borrowed from other work is cited
- [ ] Similar results in literature are acknowledged
- [ ] Notation conventions are cited if borrowed
- [ ] No "well-known" statements without citations

**"Well-known" ≠ No citation needed**

Even if something is standard in your field, cite a reference (textbook or original paper).

**See:** [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md) for detailed guidance.

---

**END OF TEMPLATE**

---

**STATUS:** ✅ Enhanced from 40% → 95% (October 10, 2025)
**Improvements:** Complete rewrite with comprehensive guidance, templates, examples, proof-writing tips, field adaptations, quality checklists, figure recommendations, and 6-iteration revision process
