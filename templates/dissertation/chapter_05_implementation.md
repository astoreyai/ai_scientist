# Chapter 5: Implementation

## Overview

This chapter describes how you implemented your system, algorithm, or method. The goal is to provide sufficient detail that another researcher in your field could reproduce your work. Focus on:
- Architecture and design decisions
- Key implementation details (not trivial boilerplate)
- Challenges encountered and solutions
- Testing and validation strategies
- Code availability and reproducibility

**Target Length:** 7,000-10,000 words

**Important:** This chapter bridges the gap between theory (Chapter 3), methodology (Chapter 4), and results (Chapter 6). Explain HOW you built what you designed, not just WHAT you built.

---

## 5.1 Introduction

**Purpose:** Provide an overview of the implementation and orient readers to what they'll learn in this chapter.

**What to Include:**
- High-level summary of what was implemented
- Technologies, languages, and frameworks used
- System scale (lines of code, modules, etc.)
- Code availability statement
- Chapter organization

**Writing Template:**

```markdown
## 5.1 Introduction

[OVERVIEW: What was implemented?]
This chapter describes the implementation of [SYSTEM/ALGORITHM NAME], the [BRIEF DESCRIPTION] presented in Chapter 4. We developed [SUMMARY OF WHAT YOU BUILT] that [KEY CAPABILITY].

[TECHNOLOGIES: What did you use?]
The system is implemented in [LANGUAGE] using [FRAMEWORK/LIBRARY]. Key technologies include:
- **[Technology 1]:** [Purpose, e.g., PyTorch for neural network training]
- **[Technology 2]:** [Purpose, e.g., NumPy for numerical computation]
- **[Technology 3]:** [Purpose, e.g., Docker for reproducible environments]

[SCALE: How big is the implementation?]
The complete implementation consists of:
- [X] lines of Python code (excluding tests and comments)
- [Y] key modules organized into [Z] packages
- [A] unit tests achieving [B]% coverage
- [C] integration tests for end-to-end validation

[CODE AVAILABILITY: Where can others access this?]
**Code Availability:** The complete implementation is publicly available under the [LICENSE] license at [REPOSITORY URL]. See Appendix [X] for installation instructions and usage examples.

[ORGANIZATION: What's in this chapter?]
This chapter is organized as follows:
- Section 5.2 describes the system architecture and component design
- Sections 5.3-5.X detail the implementation of each major component
- Section 5.Y discusses challenges encountered and solutions
- Section 5.Z describes code organization and testing strategy
- Section 5.W provides a summary and connection to Chapter 6 (Results)
```

**Example from Computer Science/ML:**

> This chapter describes the implementation of FastSHAP-ViT, the real-time explainability framework for vision transformers presented in Chapter 4. We developed a GPU-accelerated PyTorch system that computes Shapley value explanations in <50ms while maintaining >0.7 insertion AUC faithfulness.
>
> **Technologies Used:**
> - **PyTorch 2.0:** Neural network training and inference with CUDA acceleration
> - **timm:** Vision Transformer (ViT) backbone implementation
> - **NumPy/SciPy:** Numerical computation for Shapley calculations
> - **Dlib:** Facial landmark detection for feature extraction
> - **Docker:** Reproducible development and deployment environment
>
> **Implementation Scale:**
> - 5,927 lines of Python code (excluding tests and comments)
> - 8 key modules organized into 4 packages (models, explainers, fairness, utils)
> - 142 unit tests achieving 87% code coverage
> - 12 integration tests for end-to-end validation
>
> **Code Availability:** The complete implementation is publicly available under the MIT license at https://github.com/username/fastshap-vit. See Appendix A for installation instructions and usage examples.
>
> **Organization:** Section 5.2 describes the system architecture. Sections 5.3-5.5 detail the implementation of E-ViT, hierarchical SHAP, and demographic calibration. Section 5.6 discusses challenges (GPU memory management, numerical stability). Section 5.7 describes code organization and testing. Section 5.8 summarizes the implementation.

**Word Count Target:** 500-800 words

**📚 CITATION CHECK:**
- [ ] Technologies/libraries used are cited (PyTorch, timm, etc.)
- [ ] Code availability statement includes repository URL
- [ ] License is specified
- [ ] See [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md)

---

## 5.2 System Architecture

**Purpose:** Provide a high-level view of how your system is structured and how components interact.

**What to Include:**
- Architecture diagram (Figure 5.1)
- Component breakdown with responsibilities
- Data flow through the system
- Design patterns used

---

### 5.2.1 Overview

**Purpose:** Present the high-level architecture visually and conceptually.

**Template:**

```markdown
### 5.2.1 Overview

[ARCHITECTURE DESCRIPTION]
The system follows a [ARCHITECTURE STYLE] architecture consisting of [N] major components (Figure 5.1):

1. **[Component 1]:** [Brief description of purpose]
2. **[Component 2]:** [Brief description of purpose]
3. **[Component 3]:** [Brief description of purpose]
...

**Figure 5.1: System Architecture**
[INSERT ARCHITECTURE DIAGRAM HERE]

*Caption: High-level architecture showing the [N] major components and their interactions. [DESCRIBE KEY FLOWS, e.g., "Input flows from left to right through preprocessing, model inference, explanation generation, and output visualization."]*

[DESIGN PHILOSOPHY]
The architecture is designed for [KEY PROPERTIES, e.g., "modularity, extensibility, and performance"]. Each component is:
- **Modular:** Clear interfaces and single responsibility
- **Testable:** Unit tests for each component
- **Documented:** Docstrings and usage examples
- **Efficient:** Performance-critical paths optimized
```

**Example:**

```markdown
### 5.2.1 Overview

The FastSHAP-ViT system follows a pipeline architecture consisting of 5 major components (Figure 5.1):

1. **Input Processor:** Loads images, detects faces, extracts facial landmarks
2. **E-ViT Model:** Vision transformer with explainable multi-head attention (E-MHA)
3. **Hierarchical SHAP Explainer:** Computes Shapley values using hierarchical approximation
4. **Demographic Calibrator:** Adjusts explanations to reduce demographic bias
5. **Visualization Generator:** Creates heatmaps and attribution overlays

**Figure 5.1: FastSHAP-ViT System Architecture**
```
┌──────────────┐   ┌──────────────┐   ┌─────────────────────┐   ┌──────────────────┐   ┌─────────────┐
│ Input        │──▶│ E-ViT Model  │──▶│ Hierarchical SHAP   │──▶│ Demographic      │──▶│ Visualization│
│ Processor    │   │ (E-MHA)      │   │ Explainer           │   │ Calibrator       │   │ Generator    │
└──────────────┘   └──────────────┘   └─────────────────────┘   └──────────────────┘   └─────────────┘
      │                    │                     │                        │                      │
   [Image]           [Embedding]             [Shapley]              [Calibrated]            [Heatmap]
                    [Attention]              [Values]               [Shapley]               [Overlay]
```

*Caption: High-level architecture showing the 5 major components. Input flows from left to right through preprocessing, model inference, explanation generation, calibration, and visualization.*

**Design Philosophy:**
The architecture is designed for modularity, real-time performance, and fairness. Each component is:
- **Modular:** Clear interfaces (e.g., Explainer base class, Calibrator interface)
- **Testable:** 142 unit tests covering each component independently
- **Documented:** Comprehensive docstrings with usage examples
- **Efficient:** GPU-accelerated critical paths (E-ViT, SHAP sampling)
- **Fair:** Calibration pipeline ensures <10% demographic variance
```

**Diagram Creation Tips:**
- Use ASCII art for simple pipelines (as above)
- Use draw.io, PowerPoint, or similar for complex architectures
- Use PlantUML for UML diagrams (class, sequence, component)
- Include legend if using symbols or colors
- Reference diagram in text: "As shown in Figure 5.1, ..."

**Word Count:** 300-500 words (excluding diagram)

---

### 5.2.2 Component Breakdown

**Purpose:** Describe each component's responsibilities, inputs, outputs, and implementation approach.

**Template for Each Component:**

```markdown
### 5.2.2 Component Breakdown

#### Component 1: [Component Name]

**Purpose:**
[What does this component do? Why is it needed?]

**Input:**
- [Input 1]: [Description, e.g., "RGB image of size 224×224"]
- [Input 2]: [Description]

**Output:**
- [Output 1]: [Description, e.g., "512-dimensional L2-normalized embedding"]
- [Output 2]: [Description]

**Implementation:**
[High-level description of how it's implemented. Technologies used. Key algorithms.]

**Key Classes/Functions:**
- `ClassName` (module_name.py): [Description]
- `function_name()` (module_name.py): [Description]

**Complexity:**
- Time: [O(?) complexity with explanation]
- Space: [O(?) complexity with explanation]

**Dependencies:**
[Libraries or other components this depends on]

---

[REPEAT FOR EACH COMPONENT]
```

**Example:**

```markdown
### 5.2.2 Component Breakdown

#### Component 1: Input Processor

**Purpose:**
Preprocesses raw images for face recognition and feature extraction. Detects faces, normalizes to standard size, and identifies facial landmarks for interpretable features.

**Input:**
- RGB image of arbitrary size (e.g., 1920×1080)
- Optional: Pre-detected bounding box

**Output:**
- Normalized face crop (224×224×3)
- 68 facial landmark coordinates (x, y pairs)
- Feature masks for 8 regions (eyes, nose, mouth, etc.)

**Implementation:**
Uses Dlib's HOG-based face detector to locate faces in the image. Applies geometric normalization (align by eye centers, scale to 224×224). Runs dlib's 68-point landmark predictor. Groups landmarks into 8 semantic regions using predefined mappings.

**Key Classes/Functions:**
- `InputProcessor` (data/preprocessing.py): Main class orchestrating preprocessing
- `detect_face()`: Face detection wrapper (Dlib HOG or MTCNN)
- `align_face()`: Geometric normalization using eye centers
- `extract_landmarks()`: 68-point landmark detection
- `create_feature_masks()`: Groups landmarks into semantic regions

**Complexity:**
- Time: O(HW) for face detection + O(1) for landmark detection = O(HW)
- Space: O(HW) for image storage + O(1) for landmarks = O(HW)

**Dependencies:**
- dlib 19.24 (face detection, landmark prediction)
- OpenCV 4.7 (image I/O, geometric transforms)
- NumPy 1.24 (array operations)

---

#### Component 2: E-ViT Model

**Purpose:**
Vision Transformer backbone with Explainable Multi-Head Attention (E-MHA) for face recognition. Produces embeddings on a hypersphere and attention maps for interpretability.

**Input:**
- Normalized face image (224×224×3)

**Output:**
- Face embedding (512-dimensional, L2-normalized)
- Attention maps for each layer and head (197×197 for ViT-Base)

**Implementation:**
Extends timm's ViT-Base/16 architecture with custom E-MHA layers (sparse attention with explainability routing). Uses ArcFace loss during training to produce hypersphere embeddings. Stores attention weights during forward pass for explanation generation.

**Key Classes/Functions:**
- `ExplainableViT` (models/evit.py): Main model class extending timm.VisionTransformer
- `ExplainableMHA` (models/emha.py): E-MHA layer with sparse attention
- `ArcFaceHead` (models/arcface.py): Hypersphere embedding head
- `forward_with_attn()`: Forward pass storing attention weights

**Complexity:**
- Time: O(N²D) where N=197 patches, D=768 hidden dim (standard ViT complexity)
- Space: O(N²L) for storing attention weights (L=12 layers)

**Dependencies:**
- PyTorch 2.0 (neural network framework)
- timm 0.9.2 (ViT backbone)
- Custom E-MHA implementation (models/emha.py)

---

[Continue for remaining components...]
```

**How Many Components?**
- Typically 3-6 major components
- Break down complex components into sub-components if needed
- Focus on novel or non-trivial components (skip standard library wrappers)

**Word Count:** 150-250 words per component × [N] components = 600-1,500 words total

---

### 5.2.3 Data Flow

**Purpose:** Trace how data moves through the system from input to output.

**Template:**

```markdown
### 5.2.3 Data Flow

The data flow through the system follows these steps:

**Step 1: Input → [Component 1]**
- **Input:** [Description]
- **Processing:** [What happens]
- **Output:** [Result]

**Step 2: [Component 1] → [Component 2]**
- **Input:** [Previous output]
- **Processing:** [What happens]
- **Output:** [Result]

**Step 3: [Component 2] → [Component 3]**
- **Input:** [Previous output]
- **Processing:** [What happens]
- **Output:** [Result]

[CONTINUE FOR ALL STEPS]

**Final Output:**
[Description of final system output]

**Intermediate Data:**
[Any intermediate results stored for debugging, analysis, or visualization]
```

**Example:**

```markdown
### 5.2.3 Data Flow

The data flow through FastSHAP-ViT follows these steps:

**Step 1: Raw Image → Input Processor**
- **Input:** RGB image (e.g., 1920×1080×3)
- **Processing:** Face detection (Dlib HOG), geometric normalization (align by eyes), landmark detection (68 points), feature mask creation (8 regions)
- **Output:** Normalized face crop (224×224×3), landmarks (68×2), feature masks (8 binary masks)

**Step 2: Normalized Face → E-ViT Model**
- **Input:** Face crop (224×224×3)
- **Processing:** Patch embedding (16×16 patches), 12 transformer layers with E-MHA, ArcFace head
- **Output:** Face embedding (512-dim, L2-normalized), attention maps (12 layers × 12 heads × 197×197)

**Step 3: Embedding + Attention → Hierarchical SHAP Explainer**
- **Input:** Face embedding, attention maps, feature masks
- **Processing:** Hierarchical coalition sampling (K=100 per level, L=log M levels), GPU-accelerated model evaluation, Shapley aggregation
- **Output:** Shapley values (8 features)

**Step 4: Shapley Values → Demographic Calibrator**
- **Input:** Shapley values, predicted demographic (from separate classifier)
- **Processing:** Statistical calibration (subtracting demographic-specific bias), preserving ranking order
- **Output:** Calibrated Shapley values (8 features)

**Step 5: Calibrated Shapley → Visualization Generator**
- **Input:** Calibrated Shapley values, original face image, feature masks
- **Processing:** Heatmap generation (Gaussian smoothing), overlay creation (alpha blending), bar chart
- **Output:** Explanation visualization (heatmap + bar chart)

**Final Output:**
- Explanation heatmap (224×224×3 RGB image)
- Bar chart (feature names + Shapley values)
- JSON with numerical values

**Intermediate Data Stored:**
- Raw attention maps (for analysis, debugging)
- Uncalibrated Shapley values (for fairness evaluation)
- Coalition samples and their values (for approximation error analysis)
```

**Word Count:** 400-700 words

---

### 5.2.4 Design Patterns

**Purpose:** Document software design patterns used to solve common problems.

**Template:**

```markdown
### 5.2.4 Design Patterns

We employ the following design patterns to ensure code quality and maintainability:

#### Pattern 1: [Pattern Name]

**Where Used:** [Component/Module]

**Why Used:** [Problem this pattern solves]

**Implementation:**
[Brief description of how it's implemented]

**Example:**
```python
# [Code snippet illustrating the pattern]
```

---

[REPEAT FOR EACH PATTERN]
```

**Common Patterns to Consider:**

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Factory** | Creating objects with complex initialization | `ExplainerFactory.create(method='hierarchical')` |
| **Strategy** | Swappable algorithms | `Calibrator` interface with `StatisticalCalibrator`, `NeuralCalibrator` |
| **Observer** | Event-driven updates | Training progress callbacks |
| **Singleton** | Global configuration | `Config` object |
| **Template Method** | Consistent process with varying steps | `BaseExplainer` with `explain()` method |
| **Decorator** | Adding behavior dynamically | `@gpu_accelerated` decorator |
| **Adapter** | Interface compatibility | Wrapping timm ViT to expose attention |

**Example:**

```markdown
### 5.2.4 Design Patterns

We employ the following design patterns to ensure modularity and extensibility:

#### Pattern 1: Strategy Pattern (Explainers)

**Where Used:** `explainers/` module

**Why Used:** Allows swapping explanation methods (hierarchical SHAP, KernelSHAP, LIME, etc.) without changing client code. Supports easy addition of new explanation methods.

**Implementation:**
Define `BaseExplainer` abstract class with `explain()` method. Concrete implementations (`HierarchicalSHAP`, `KernelSHAP`, `GradCAM`) inherit and implement `explain()`.

**Example:**
```python
class BaseExplainer(ABC):
    @abstractmethod
    def explain(self, model, input, target):
        """Generate explanation for input."""
        pass

class HierarchicalSHAP(BaseExplainer):
    def explain(self, model, input, target):
        # Hierarchical SHAP implementation
        return shapley_values

# Usage: swap explainers transparently
explainer = HierarchicalSHAP(...)  # or KernelSHAP(...)
explanation = explainer.explain(model, input, target)
```

---

#### Pattern 2: Factory Pattern (Model Creation)

**Where Used:** `models/factory.py`

**Why Used:** Centralizes complex model instantiation logic. Supports loading pre-trained weights, configuring hyperparameters, and creating different model variants.

**Implementation:**
`ModelFactory.create()` takes model name and config dict, returns instantiated model. Handles checkpoint loading, device placement, and validation.

**Example:**
```python
class ModelFactory:
    @staticmethod
    def create(model_name, config):
        if model_name == 'evit_base':
            model = ExplainableViT(...)
            model.load_checkpoint(config['checkpoint'])
        elif model_name == 'evit_large':
            ...
        return model

# Usage
model = ModelFactory.create('evit_base', config)
```

---

#### Pattern 3: Decorator Pattern (GPU Acceleration)

**Where Used:** `utils/gpu.py`

**Why Used:** Automatically handles device placement (CPU/GPU), batch processing, and memory management without modifying core algorithm code.

**Implementation:**
`@gpu_accelerated` decorator wraps functions to move inputs to GPU, run computation, and move results back to CPU. Handles CUDA out-of-memory errors gracefully.

**Example:**
```python
@gpu_accelerated(device='cuda', batch_size=32)
def compute_coalitions(model, inputs):
    # This function automatically runs on GPU in batches
    return model(inputs)
```
```

**Word Count:** 100-200 words per pattern × [N] patterns = 300-800 words total

---

## 5.3 [Component 1 Implementation]

**Purpose:** Detailed implementation of the first major component.

**Rename this section** to match your actual component (e.g., "5.3 E-ViT Model Implementation" or "5.3 Data Preprocessing Pipeline").

**Structure:**
- 5.3.1 Algorithm Implementation
- 5.3.2 Edge Cases and Error Handling
- 5.3.3 Performance Optimization

---

### 5.3.1 Algorithm Implementation

**Purpose:** Show how you translated the algorithm from Chapter 4 into code.

**Template:**

```markdown
### 5.3.1 Algorithm Implementation

**From Methodology to Code:**

The [ALGORITHM NAME] presented in Chapter 4 (Algorithm 4.X) is implemented as follows:

**Pseudocode (from Chapter 4):**
```
Algorithm 4.X: [Name]
Input: [...]
Output: [...]

1: [Step 1]
2: [Step 2]
3: [Step 3]
...
```

**Implementation (Python):**
```python
def algorithm_name(input1, input2, ...):
    """
    [DOCSTRING: Brief description]

    Args:
        input1: [Description with type]
        input2: [Description with type]

    Returns:
        [Description with type]

    Reference:
        Algorithm 4.X in Chapter 4
    """
    # Step 1: [Comment matching pseudocode]
    result1 = ...

    # Step 2: [Comment matching pseudocode]
    result2 = ...

    # Step 3: [Comment matching pseudocode]
    final_result = ...

    return final_result
```

**Key Implementation Choices:**

1. **[Choice 1]:** [What you chose and why]
   - **Alternatives considered:** [What else you could have done]
   - **Rationale:** [Why this choice is better]

2. **[Choice 2]:** [What you chose and why]
   - **Alternatives considered:** [...]
   - **Rationale:** [...]

**Data Structures:**

- **[Structure 1]:** [Why this structure? Time/space trade-offs?]
- **[Structure 2]:** [...]
```

**Example:**

```markdown
### 5.3.1 Algorithm Implementation

**From Methodology to Code:**

The Hierarchical SHAP algorithm presented in Chapter 4 (Algorithm 4.2) is implemented in `explainers/hierarchical_shap.py`.

**Pseudocode (from Chapter 4):**
```
Algorithm 4.2: Hierarchical SHAP
Input: Model f, input x, features M, samples K
Output: Shapley values φ

1: Build binary tree over features M (L = log₂|M| levels)
2: For each level ℓ = 1 to L:
3:    Sample K coalitions S ~ P_ℓ (attention-guided)
4:    Evaluate ν(S) = value_function(f, x, S)
5:    Estimate E[Δᵢ | level ℓ] via Monte Carlo
6: Aggregate across levels: φᵢ = Σ_ℓ E[Δᵢ | level ℓ]
7: Return φ
```

**Implementation (Python):**
```python
def hierarchical_shap(model, input, features, K=100):
    """
    Compute Shapley values using hierarchical approximation.

    Args:
        model: PyTorch model (callable)
        input: Input tensor (B, C, H, W)
        features: Feature masks [(H, W) boolean tensors]
        K: Samples per level (default 100)

    Returns:
        shapley_values: (M,) tensor of Shapley values

    Reference:
        Algorithm 4.2 in Chapter 4
    """
    M = len(features)
    L = int(np.ceil(np.log2(M)))  # Number of levels

    # Step 1: Build binary tree
    tree = build_feature_tree(features)

    # Step 2-5: Sample and evaluate at each level
    marginal_contributions = torch.zeros(M, L)

    for level in range(L):
        # Step 3: Sample coalitions (attention-guided)
        coalitions = sample_coalitions(tree, level, K,
                                       attention_weights=model.get_attention())

        # Step 4: Evaluate value function (GPU-accelerated batch)
        values = evaluate_coalitions(model, input, coalitions, features)

        # Step 5: Estimate marginal contributions
        for i in range(M):
            marginal_contributions[i, level] = estimate_marginal(
                i, coalitions, values
            )

    # Step 6: Aggregate across levels
    shapley_values = marginal_contributions.sum(dim=1)

    return shapley_values
```

**Key Implementation Choices:**

1. **Binary Tree Structure:**
   - **Choice:** Balanced binary tree stored as list (heap structure)
   - **Alternatives considered:** Explicit tree nodes with pointers, k-d tree
   - **Rationale:** Heap structure uses O(M) space vs. O(2M) for explicit nodes. No pointer overhead. Cache-friendly sequential access.

2. **GPU Batch Evaluation:**
   - **Choice:** Batch K coalitions together, evaluate on GPU in single forward pass
   - **Alternatives considered:** Sequential CPU evaluation, adaptive batching
   - **Rationale:** Batching achieves 50× speedup (2s → 40ms per level). Fixed batch size simplifies memory management vs. adaptive.

3. **Attention-Guided Sampling:**
   - **Choice:** Use attention weights from E-ViT's last layer to bias coalition sampling
   - **Alternatives considered:** Uniform sampling, learned importance weights
   - **Rationale:** Attention provides meaningful feature importance signal without additional training. Reduces variance by 30% vs. uniform sampling.

**Data Structures:**

- **Feature Tree:** `List[Node]` where `Node = (feature_idx, parent_idx, left_child, right_child)`
  - Why: Heap-based tree avoids pointer overhead, enables vectorized operations
  - Complexity: O(M) space, O(log M) traversal

- **Coalition Mask:** `(K, M) boolean tensor` indicating which features are in each coalition
  - Why: GPU-friendly dense representation, enables parallel evaluation
  - Complexity: O(KM) space, O(1) indexing
```

**When to Include Code:**
- ✅ Core algorithm implementation (the "brain" of your system)
- ✅ Novel techniques or clever optimizations
- ✅ Tricky implementation details not obvious from pseudocode
- ❌ Boilerplate (imports, argument parsing, logging)
- ❌ Standard library usage (just mention "we use numpy.array")
- ❌ Trivial getters/setters

**Code Snippet Guidelines:**
- Keep snippets < 30 lines (link to repo for full code)
- Add comments explaining key lines
- Use syntax highlighting (markdown code blocks with language)
- Show function signatures with docstrings

**Word Count:** 800-1,500 words

---

### 5.3.2 Edge Cases and Error Handling

**Purpose:** Document how you handle unusual inputs and error conditions.

**Template:**

```markdown
### 5.3.2 Edge Cases and Error Handling

**Input Validation:**

The implementation validates inputs as follows:

```python
def validate_inputs(input, features):
    """Validate inputs before processing."""
    # Check 1: [Description]
    if [condition]:
        raise ValueError("[Error message with guidance]")

    # Check 2: [Description]
    if [condition]:
        raise ValueError("[Error message with guidance]")

    # [Additional checks...]
```

**Edge Cases Handled:**

1. **[Edge Case 1]:**
   - **Scenario:** [Description]
   - **Handling:** [How you handle it]
   - **Rationale:** [Why this approach?]

2. **[Edge Case 2]:**
   - **Scenario:** [...]
   - **Handling:** [...]
   - **Rationale:** [...]

**Numerical Stability:**

- **[Issue 1]:** [Description, e.g., "Division by zero in normalization"]
  - **Solution:** [e.g., "Add epsilon = 1e-8 to denominator"]

- **[Issue 2]:** [...]
  - **Solution:** [...]

**Error Recovery:**

- **[Error Type 1]:** [e.g., "CUDA out of memory"]
  - **Recovery Strategy:** [e.g., "Retry with half batch size"]

- **[Error Type 2]:** [...]
  - **Recovery Strategy:** [...]
```

**Example:**

```markdown
### 5.3.2 Edge Cases and Error Handling

**Input Validation:**

```python
def validate_inputs(input, features, K):
    """Validate inputs to hierarchical_shap()."""
    # Check 1: Input shape
    if input.ndim != 4:
        raise ValueError(f"Expected 4D input (B,C,H,W), got {input.ndim}D")

    # Check 2: Feature masks match input size
    H, W = input.shape[2:]
    if not all(f.shape == (H, W) for f in features):
        raise ValueError(f"Feature masks must match input size ({H},{W})")

    # Check 3: Number of features
    if len(features) < 2:
        raise ValueError(f"Need at least 2 features, got {len(features)}")

    # Check 4: Samples per level
    if K < 10:
        raise ValueError(f"K={K} too small, use K >= 10 for stable estimates")
```

**Edge Cases Handled:**

1. **Single Feature:**
   - **Scenario:** M = 1 (only one feature, trivial Shapley value)
   - **Handling:** Skip hierarchical sampling, return φ₁ = ν(M) - ν(∅)
   - **Rationale:** Avoids log₂(1) = 0 levels, provides instant result

2. **Power-of-Two Features:**
   - **Scenario:** M = 2^k exactly (e.g., M = 16)
   - **Handling:** Build perfectly balanced binary tree (all leaves at same depth)
   - **Rationale:** Optimal tree structure, equal variance per level

3. **Non-Power-of-Two Features:**
   - **Scenario:** M ≠ 2^k (e.g., M = 10)
   - **Handling:** Build unbalanced tree with some leaves at depth L-1
   - **Rationale:** Minimizes tree depth, groups features by importance

4. **Empty Coalition:**
   - **Scenario:** Coalition S = ∅ (no features present)
   - **Handling:** Return ν(∅) = baseline value (e.g., mean prediction)
   - **Rationale:** Defines reference point for Shapley values

5. **Full Coalition:**
   - **Scenario:** Coalition S = M (all features present)
   - **Handling:** Return ν(M) = f(x) (original model prediction)
   - **Rationale:** Upper bound for Shapley efficiency axiom

**Numerical Stability:**

- **Issue 1: Division by Zero in Shapley Formula**
  - **Solution:** Add epsilon = 1e-8 to factorial denominators: `factorial(k) + 1e-8`
  - **Rationale:** Prevents NaN when k=0 in some edge cases

- **Issue 2: Exponential Overflow in Value Function**
  - **Solution:** Use log-space computation: `log_value = -θ * d_g`, then `value = exp(log_value)`
  - **Rationale:** Prevents overflow for large geodesic distances (d_g > 20)

- **Issue 3: Floating Point Precision in Tree Traversal**
  - **Solution:** Use integer indices for tree nodes, not float pointers
  - **Rationale:** Avoids accumulation of rounding errors

**Error Recovery:**

- **Error: CUDA Out of Memory**
  - **Detection:** Catch `torch.cuda.OutOfMemoryError`
  - **Recovery:** Reduce batch size by half, retry. If K < 10, raise error (insufficient samples).
  - **Logging:** Warn user about reduced batch size

- **Error: Model Inference Failure**
  - **Detection:** Catch `RuntimeError` during `model(input)`
  - **Recovery:** Log error details, return NaN for failed coalitions, continue with valid samples
  - **Rationale:** Partial results better than complete failure (can warn user)

- **Error: Negative Shapley Values (Unexpected)**
  - **Detection:** Check `shapley_values.min() < -epsilon`
  - **Recovery:** Log warning, clip to zero if small (|φ| < 0.01), raise error if large
  - **Rationale:** Small negative values may be numerical error; large ones indicate bug
```

**Word Count:** 500-800 words

---

### 5.3.3 Performance Optimization

**Purpose:** Document optimizations that improve speed or memory usage.

**Template:**

```markdown
### 5.3.3 Performance Optimization

**Bottleneck Analysis:**

Profiling with [TOOL] revealed the following bottlenecks:

| Component | Time (ms) | Percentage | Bottleneck |
|-----------|-----------|------------|------------|
| [Component 1] | [X ms] | [Y%] | [Description] |
| [Component 2] | [X ms] | [Y%] | [Description] |
| **Total** | **[X ms]** | **100%** | — |

**Optimizations Applied:**

1. **[Optimization 1]:**
   - **Problem:** [What was slow?]
   - **Solution:** [What did you do?]
   - **Speedup:** [Before → After, e.g., "500ms → 50ms (10× faster)"]
   - **Trade-off:** [Any downsides? Memory increase?]

2. **[Optimization 2]:**
   - **Problem:** [...]
   - **Solution:** [...]
   - **Speedup:** [...]
   - **Trade-off:** [...]

**Final Performance:**

After optimization, the system achieves:
- **Latency:** [X ms per inference]
- **Throughput:** [Y inferences per second]
- **Memory:** [Z GB peak usage]

**Comparison with Baselines:**

| Method | Latency | Throughput | Memory |
|--------|---------|------------|--------|
| Baseline 1 | [X ms] | [Y/s] | [Z GB] |
| Baseline 2 | [...] | [...] | [...] |
| **Ours (Optimized)** | **[X ms]** | **[Y/s]** | **[Z GB]** |

**Profiling Results:**

**Figure 5.X: Performance Profiling**
[Bar chart showing time breakdown before/after optimization]
```

**Example:**

```markdown
### 5.3.3 Performance Optimization

**Bottleneck Analysis:**

Profiling with PyTorch Profiler revealed the following bottlenecks in initial implementation:

| Component | Time (ms) | Percentage | Bottleneck |
|-----------|-----------|------------|------------|
| Coalition Evaluation | 1,850 ms | 88% | Sequential CPU model calls |
| Shapley Aggregation | 120 ms | 6% | Python loop over features |
| Attention Sampling | 80 ms | 4% | CPU-GPU transfer |
| Other | 50 ms | 2% | Misc overhead |
| **Total** | **2,100 ms** | **100%** | — |

**Optimizations Applied:**

1. **GPU Batch Evaluation:**
   - **Problem:** Evaluating K coalitions sequentially on CPU took 1,850ms (88% of time)
   - **Solution:** Stack K coalition inputs into batch tensor, evaluate on GPU in single forward pass
   - **Speedup:** 1,850ms → 35ms (53× faster)
   - **Trade-off:** GPU memory increases from 2GB → 8GB (acceptable for V100)

2. **Vectorized Shapley Aggregation:**
   - **Problem:** Python loop summing marginal contributions across levels took 120ms
   - **Solution:** Use PyTorch tensor operations: `shapley = marginal_contributions.sum(dim=1)`
   - **Speedup:** 120ms → 3ms (40× faster)
   - **Trade-off:** None (pure improvement)

3. **Pinned Memory for Attention Transfer:**
   - **Problem:** Transferring attention weights from GPU to CPU for sampling took 80ms
   - **Solution:** Use pinned memory (`pin_memory=True`) for async CPU-GPU transfer
   - **Speedup:** 80ms → 12ms (7× faster)
   - **Trade-off:** 100MB extra CPU memory (negligible)

4. **JIT Compilation:**
   - **Problem:** PyTorch overhead in coalition masking operations
   - **Solution:** Use `torch.jit.script` to compile critical functions (mask_features, apply_coalition)
   - **Speedup:** 50ms → 8ms (6× faster)
   - **Trade-off:** Longer startup time (2s compilation, amortized)

**Final Performance:**

After optimization, the hierarchical SHAP component achieves:
- **Latency:** 58ms per explanation (M=8 features, K=100 samples)
- **Throughput:** 17 explanations per second
- **Memory:** 8.2 GB GPU peak usage (batch of 100 coalitions)

**Comparison with Baselines:**

| Method | Latency (ms) | Throughput (fps) | Memory (GB) |
|--------|--------------|------------------|-------------|
| Exact SHAP | 45,000 | 0.02 | 12.0 |
| KernelSHAP (Lundberg et al.) | 220 | 4.5 | 4.5 |
| GradCAM (Baseline) | 12 | 83.3 | 2.1 |
| **Hierarchical SHAP (Ours)** | **58** | **17.2** | **8.2** |

*Note: Exact SHAP is 2^8 = 256× slower. GradCAM is faster but not Shapley-based (different method).*

**Profiling Results:**

**Figure 5.4: Performance Profiling Before and After Optimization**
```
Before Optimization (2,100ms):
Coalition Eval ████████████████████████ 88%
Aggregation   ███ 6%
Attention     ██ 4%
Other         █ 2%

After Optimization (58ms):
Coalition Eval ███████████ 60%
Aggregation   █ 5%
Attention     ████ 21%
Other         ███ 14%
```

*Caption: Time breakdown showing 36× overall speedup. Coalition evaluation remains dominant but reduced from 1,850ms to 35ms via GPU batching.*
```

**Word Count:** 600-1,000 words

---

## 5.4 [Component 2 Implementation]

**Purpose:** Detailed implementation of the second major component.

**Structure:** Follow the same structure as Section 5.3:
- 5.4.1 Algorithm Implementation
- 5.4.2 Edge Cases and Error Handling
- 5.4.3 Performance Optimization

**Repeat for each major component** (Sections 5.5, 5.6, etc. as needed)

**Note:** You don't need identical depth for every component. Focus more detail on:
- Novel components (your contributions)
- Complex components (tricky algorithms)
- Components that had significant challenges

Standard components can be briefer:
- "The visualization component uses matplotlib to generate heatmaps (Section 5.4.1). It handles edge cases like extreme values via clipping (Section 5.4.2) and is optimized using cached colormaps (Section 5.4.3)."

**Word Count per Component:** 1,000-2,000 words for major novel components, 500-800 words for standard components

---

## 5.X Implementation Challenges

**Purpose:** Honestly discuss problems you encountered and how you solved them. This section demonstrates problem-solving skills and helps future researchers avoid the same pitfalls.

**What to Include:**
- 3-5 significant challenges
- Root cause analysis (why did it happen?)
- Solutions attempted (including failures)
- Final solution and lessons learned

**Template:**

```markdown
## 5.X Implementation Challenges

During implementation, we encountered several significant challenges:

### Challenge 1: [Problem Name]

**Problem Description:**
[What went wrong? When did you discover it?]

**Root Cause:**
[Why did this happen? Design flaw? Library limitation? Hardware constraint?]

**Solutions Attempted:**
1. **[Attempt 1]:** [What you tried] → [Why it didn't work]
2. **[Attempt 2]:** [What you tried] → [Why it didn't work]
3. **[Attempt 3]:** [What you tried] → [Success or partial success]

**Final Solution:**
[What ultimately worked?]

**Lesson Learned:**
[What would you do differently next time?]

---

[REPEAT FOR EACH CHALLENGE]

### Challenge X: [...]

**Summary:**

These challenges taught us [KEY LESSONS]. Future implementations should [RECOMMENDATIONS].
```

**Example:**

```markdown
## 5.6 Implementation Challenges

During implementation, we encountered several significant challenges:

### Challenge 1: GPU Memory Overflow with Large Coalitions

**Problem Description:**
When evaluating K=100 coalitions for M=20 features, GPU memory usage exceeded 16GB (V100 limit), causing CUDA out-of-memory errors. This occurred during training when batch size > 1.

**Root Cause:**
The hierarchical SHAP explainer stores attention weights for all coalitions simultaneously: 100 coalitions × 12 layers × 12 heads × 197×197 patches = 5.6 billion float32 values (22.4GB). We underestimated memory usage during design.

**Solutions Attempted:**
1. **Reduce K to 50:** → Approximation error increased from 0.08 to 0.15 (unacceptable for faithfulness target >0.7)
2. **Use float16 for attention:** → Numerical instability in Shapley aggregation (values became NaN)
3. **Sequential coalition evaluation:** → Latency increased from 58ms to 850ms (violates <50ms requirement)

**Final Solution:**
Implemented **attention checkpointing**: Store attention for only the last layer during forward pass. Recompute earlier layers' attention on-demand when needed. This reduces memory from 22.4GB to 1.9GB while adding only 12ms latency (trade-off: 58ms → 70ms, still under 100ms stretch goal).

**Lesson Learned:**
Profile memory usage early, not just latency. Use `torch.cuda.max_memory_allocated()` after each forward pass during development. Checkpointing is effective for memory-latency trade-offs.

---

### Challenge 2: Attention Weights Not Matching Feature Regions

**Problem Description:**
Attention-guided coalition sampling was biased toward central patches (nose region) regardless of actual feature importance. This caused 60% of samples to include the nose, leading to poor Shapley estimates for other features.

**Root Cause:**
ViT attention is computed over patches (197×197 patch pairs), but our features are semantic regions (eyes, nose, mouth). We naively averaged attention weights within each region, but this ignored the CLS token's role. The CLS token attends strongly to central patches due to training on ImageNet (center bias).

**Solutions Attempted:**
1. **Exclude CLS token attention:** → Improved slightly (nose = 50%) but still biased
2. **Use gradient-based importance instead:** → Slow (adds 30ms) and noisy (high variance)
3. **Learned sampling weights (train separate network):** → Requires additional training data (impractical)

**Final Solution:**
Implemented **CLS-agnostic attention aggregation**: For each region, compute `attention = mean(patch→patch attention within region)`, excluding CLS→patch and patch→CLS attention. Additionally, apply **softmax temperature scaling** (T=0.5) to sharpen attention differences. This reduced nose bias to 28% (close to uniform 1/8 = 12.5% for 8 features).

**Lesson Learned:**
Attention weights are task-specific (ImageNet training creates biases). Always analyze attention distributions before using them for downstream tasks. Temperature scaling is a simple fix for overconfident distributions.

---

### Challenge 3: Numerical Instability in Geodesic Distance Computation

**Problem Description:**
Computing geodesic distance on the hypersphere via `arccos(⟨u, v⟩)` produced NaN values for ~2% of coalitions. This corrupted Shapley value estimates.

**Root Cause:**
Floating point errors caused `⟨u, v⟩` to slightly exceed 1.0 (e.g., 1.0000001) due to L2 normalization imperfections. The domain of `arccos` is [-1, 1], so values outside cause NaN.

**Solutions Attempted:**
1. **Clip to [-1, 1]:** → `arccos(clip(⟨u, v⟩, -1, 1))` → Fixed NaNs but introduced bias (clipped values → 0° distance)
2. **Use float64 for inner products:** → Reduced NaN rate from 2% to 0.5% (still present)
3. **Re-normalize after every operation:** → Slow (adds 15ms) and still 0.1% NaNs

**Final Solution:**
Implemented **numerically stable geodesic formula** using `atan2`:
```python
# Instead of: d = arccos(⟨u, v⟩)
# Use: d = atan2(||u × v||, ⟨u, v⟩)
cross_prod = torch.cross(u, v)
d = torch.atan2(torch.norm(cross_prod, dim=-1), torch.dot(u, v))
```
This avoids domain issues (atan2 is defined for all inputs) and is numerically stable. NaN rate: 0%.

**Lesson Learned:**
Never use `arccos` for angle computation in production code. Always prefer `atan2`-based formulations for numerical stability. Test with edge cases (u ≈ v, u ≈ -v).

---

### Challenge 4: Test Coverage for Rare Edge Cases

**Problem Description:**
Initial unit tests achieved 85% code coverage but missed several critical edge cases (M=1 feature, empty coalition, etc.). These caused production bugs when users provided unusual inputs.

**Root Cause:**
Test cases focused on "happy path" scenarios (standard inputs). We didn't systematically enumerate edge cases during test design.

**Solutions Attempted:**
1. **Add more random tests:** → Caught some bugs but not all edge cases (random sampling unlikely to hit M=1)
2. **Manual code review for edge cases:** → Time-consuming and error-prone

**Final Solution:**
Implemented **property-based testing** using Hypothesis library:
```python
@given(
    M=st.integers(min_value=1, max_value=100),
    K=st.integers(min_value=10, max_value=1000),
)
def test_hierarchical_shap_axioms(M, K):
    # Hypothesis generates random M, K values
    # Test that Shapley axioms hold for all inputs
    shapley = hierarchical_shap(..., M=M, K=K)
    assert_efficiency(shapley)
    assert_symmetry(shapley)
    ...
```
This automatically discovered edge cases we hadn't considered (M=1, M=2, K<M, etc.). Coverage increased from 85% to 97%.

**Lesson Learned:**
Property-based testing is highly effective for mathematical code. Define invariants (Shapley axioms) and let the test framework find edge cases. Integrate Hypothesis into CI/CD pipeline.

---

### Summary

These challenges taught us:
1. **Profile early:** Memory and latency issues are easier to fix during development than in production
2. **Question assumptions:** Attention weights, numerical stability—always validate underlying assumptions
3. **Automate edge case testing:** Property-based testing finds bugs manual tests miss
4. **Document trade-offs:** Checkpointing (memory ↓, latency ↑) is a principled engineering choice

Future implementations should:
- Allocate 20% of development time for optimization and edge case handling
- Use property-based testing from day one
- Validate third-party library assumptions (e.g., ViT attention behavior)
```

**Word Count:** 1,000-1,500 words

---

## 5.Y Code Organization

**Purpose:** Describe how your code is structured so others can navigate it.

**What to Include:**
- Directory structure
- Key modules and their purposes
- Dependencies and version requirements
- Documentation approach

---

### 5.Y.1 Directory Structure

**Template:**

```markdown
### 5.Y.1 Directory Structure

The codebase is organized as follows:

```
project_name/
├── src/                    # Source code
│   ├── models/            # Model definitions
│   │   ├── evit.py       # [Description]
│   │   ├── emha.py       # [Description]
│   │   └── ...
│   ├── explainers/        # Explanation methods
│   │   ├── hierarchical_shap.py  # [Description]
│   │   ├── kernel_shap.py        # [Description]
│   │   └── ...
│   ├── fairness/          # Demographic calibration
│   ├── utils/             # Utilities (GPU, metrics, viz)
│   └── data/              # Data loading and preprocessing
├── tests/                  # Unit and integration tests
│   ├── test_models.py
│   ├── test_explainers.py
│   └── ...
├── configs/                # Configuration files (YAML)
├── scripts/                # Training and evaluation scripts
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
├── setup.py                # Package installation
├── README.md               # Quick start guide
└── LICENSE                 # License information
```

**Key Directories:**

- **`src/`:** Core implementation ([X] lines). Organized by functionality (models, explainers, fairness, utils).
- **`tests/`:** [Y] unit tests ([Z]% coverage) and [A] integration tests. Use pytest.
- **`configs/`:** YAML configuration files for experiments (hyperparameters, paths).
- **`scripts/`:** Command-line scripts for training (`train.py`), evaluation (`evaluate.py`), and inference (`explain.py`).
- **`docs/`:** Sphinx documentation with API reference and tutorials.
```

**Example:**

```markdown
### 5.7.1 Directory Structure

The FastSHAP-ViT codebase is organized as follows:

```
fastshap-vit/
├── src/fastshap_vit/           # Source code (5,927 lines)
│   ├── models/                # Model definitions (1,240 lines)
│   │   ├── evit.py           # ExplainableViT (535 lines)
│   │   ├── emha.py           # Explainable Multi-Head Attention (312 lines)
│   │   ├── arcface.py        # ArcFace loss and head (178 lines)
│   │   └── factory.py        # Model factory (215 lines)
│   ├── explainers/            # Explanation methods (1,687 lines)
│   │   ├── hierarchical_shap.py  # Hierarchical SHAP (645 lines)
│   │   ├── fast_explainer.py     # Neural network approximator (335 lines)
│   │   ├── kernel_shap.py        # Baseline KernelSHAP (287 lines)
│   │   └── gradcam.py            # Baseline Grad-CAM (178 lines)
│   ├── fairness/              # Demographic calibration (578 lines)
│   │   ├── calibrator.py     # Statistical calibrator (390 lines)
│   │   └── metrics.py        # Fairness metrics (188 lines)
│   ├── utils/                 # Utilities (1,047 lines)
│   │   ├── gpu.py            # GPU acceleration (312 lines)
│   │   ├── metrics.py        # Faithfulness metrics (235 lines)
│   │   ├── visualization.py  # Heatmap generation (298 lines)
│   │   └── config.py         # Configuration management (202 lines)
│   └── data/                  # Data loading (1,375 lines)
│       ├── preprocessing.py  # Face detection, landmarks (487 lines)
│       ├── datasets.py       # LFW, FairFace loaders (523 lines)
│       └── augmentation.py   # Data augmentation (365 lines)
├── tests/                     # Tests (2,134 lines, 87% coverage)
│   ├── test_models.py        # E-ViT, E-MHA tests (387 lines)
│   ├── test_explainers.py    # SHAP tests (512 lines)
│   ├── test_fairness.py      # Calibration tests (298 lines)
│   ├── test_utils.py         # Utility tests (234 lines)
│   └── integration/          # End-to-end tests (703 lines)
│       ├── test_pipeline.py  # Full pipeline test
│       └── test_axioms.py    # Shapley axiom verification
├── configs/                   # Configuration files (YAML)
│   ├── train_evit.yaml       # E-ViT training config
│   ├── train_fast_explainer.yaml  # Fast explainer training
│   └── evaluate.yaml         # Evaluation config
├── scripts/                   # Command-line scripts
│   ├── train.py              # Training entry point
│   ├── evaluate.py           # Evaluation script
│   └── explain.py            # Single-image explanation script
├── docs/                      # Sphinx documentation
│   ├── api/                  # API reference (auto-generated)
│   ├── tutorials/            # Usage tutorials
│   └── index.md              # Documentation homepage
├── requirements.txt           # Python dependencies (pinned versions)
├── setup.py                   # Package installation (pip install -e .)
├── README.md                  # Quick start guide
├── LICENSE                    # MIT License
└── .github/workflows/         # CI/CD (pytest, linting, docker build)
```

**Key Directories:**

- **`src/fastshap_vit/`:** Core implementation (5,927 lines). Organized by functionality: models (ViT), explainers (SHAP), fairness (calibration), utils (GPU, metrics, viz), data (loading).
- **`tests/`:** 142 unit tests (2,134 lines, 87% coverage) using pytest. Integration tests verify end-to-end pipeline and Shapley axioms.
- **`configs/`:** YAML configuration files separating hyperparameters from code (enables reproducibility).
- **`scripts/`:** Command-line interface for training, evaluation, and inference.
- **`docs/`:** Sphinx documentation with API reference and tutorials (hosted at Read the Docs).
```

**Word Count:** 200-400 words

---

### 5.Y.2 Key Modules

**Template:**

```markdown
### 5.Y.2 Key Modules

| Module | Purpose | Key Classes/Functions | LOC |
|--------|---------|----------------------|-----|
| `models/evit.py` | [Description] | `ExplainableViT`, `forward_with_attn()` | [X] |
| `explainers/hierarchical_shap.py` | [Description] | `HierarchicalSHAP`, `build_tree()` | [Y] |
| [...] | [...] | [...] | [...] |

**Module Dependencies:**

```
models/evit.py
    ↓ depends on
timm, torch
    ↑ used by
explainers/hierarchical_shap.py
    ↓ depends on
utils/gpu.py
```

**Detailed Descriptions:**

**`models/evit.py`:**
- **Purpose:** [Description]
- **Key Classes:**
  - `ExplainableViT`: [Description with key methods]
- **Dependencies:** [List]
- **Documentation:** [Link to docs or docstrings]

**`explainers/hierarchical_shap.py`:**
- **Purpose:** [...]
- [...]
```

**Word Count:** 300-500 words

---

### 5.Y.3 Dependencies

**Template:**

```markdown
### 5.Y.3 Dependencies

The implementation requires the following dependencies:

| Library | Version | Purpose |
|---------|---------|---------|
| Python | 3.11.2 | Programming language |
| PyTorch | 2.0.1 | Deep learning framework |
| [Library] | [Version] | [Purpose] |
| [...] | [...] | [...] |

**Dependency Management:**

- **`requirements.txt`:** Pinned versions for reproducibility
  ```
  torch==2.0.1
  torchvision==0.15.2
  numpy==1.24.3
  ...
  ```

- **Installation:**
  ```bash
  pip install -r requirements.txt
  pip install -e .  # Editable install for development
  ```

**Version Compatibility:**

- **PyTorch:** Requires 2.0+ for `torch.compile()` JIT compilation
- **Python:** Requires 3.9+ for type hints (3.11 recommended for performance)
- **CUDA:** Tested with CUDA 11.8 and 12.1 (requires GPU with compute capability 7.0+)

**Optional Dependencies:**

- **Sphinx:** For building documentation (`pip install -e .[docs]`)
- **Pytest:** For running tests (`pip install -e .[dev]`)
```

**Word Count:** 200-400 words

---

## 5.Z Testing and Validation

**Purpose:** Describe your testing strategy to establish correctness and reliability.

**What to Include:**
- Unit tests (individual functions)
- Integration tests (end-to-end pipelines)
- Validation against theory (does implementation match theorems?)

---

### 5.Z.1 Unit Tests

**Template:**

```markdown
### 5.Z.1 Unit Tests

**Coverage:** [X]% code coverage ([Y] tests)

**Test Structure:**

Each module has corresponding tests in `tests/test_<module>.py` following the AAA pattern:
- **Arrange:** Set up test inputs and expected outputs
- **Act:** Execute the function under test
- **Assert:** Verify results match expectations

**Example Test:**

```python
def test_hierarchical_shap_efficiency_axiom():
    """Test that Shapley values satisfy efficiency axiom."""
    # Arrange: Create mock model and inputs
    model = MockModel(output=1.0)
    input = torch.randn(1, 3, 224, 224)
    features = create_feature_masks(M=8)

    # Act: Compute Shapley values
    shapley = hierarchical_shap(model, input, features, K=100)

    # Assert: Efficiency axiom (sum = v(M) - v(∅))
    assert torch.allclose(
        shapley.sum(),
        torch.tensor(1.0 - 0.0),
        atol=1e-2  # Allow 0.01 tolerance for approximation
    )
```

**Critical Tests:**

1. **Correctness Tests:** Verify core algorithm behavior
   - Shapley axioms (efficiency, symmetry, dummy, additivity)
   - Geodesic distance computation (compare with scipy)
   - Tree structure (balanced, parent-child relationships)

2. **Edge Case Tests:** Verify handling of unusual inputs
   - M = 1 feature (single feature)
   - M = 2^k exactly (power-of-two features)
   - Empty coalition (S = ∅)
   - Full coalition (S = M)
   - Identical features (symmetry test)

3. **Regression Tests:** Prevent previously fixed bugs from reoccurring
   - NaN in geodesic distance (Challenge 3 from Section 5.X)
   - GPU memory overflow (Challenge 1)
   - Attention bias (Challenge 2)

**Test Execution:**

```bash
pytest tests/ --cov=src --cov-report=html
```

**Coverage Report:** See `htmlcov/index.html` for line-by-line coverage
```

**Word Count:** 400-600 words

---

### 5.Z.2 Integration Tests

**Template:**

```markdown
### 5.Z.2 Integration Tests

**Purpose:** Verify end-to-end pipeline behavior (input → output).

**Test Cases:**

1. **Full Pipeline Test:**
   - **Input:** Sample image from LFW dataset
   - **Expected Output:** Explanation heatmap + Shapley values summing to target value
   - **Assertions:**
     - No errors during execution
     - Output shapes correct (heatmap is 224×224×3)
     - Shapley values satisfy efficiency (sum = v(M) - v(∅))
   - **Runtime:** < 100ms (real-time requirement)

2. **Calibration Pipeline Test:**
   - **Input:** Batch of images from FairFace (7 demographic groups)
   - **Expected Output:** Calibrated Shapley values with <10% variance across groups
   - **Assertions:**
     - Variance ratio < 10% (fairness metric)
     - Rank correlation > 0.95 (faithfulness preserved)

3. **Multi-Model Test:**
   - **Input:** Same image, different models (E-ViT, baseline ViT)
   - **Expected Output:** Different explanations (E-ViT should have lower latency)
   - **Assertions:**
     - E-ViT latency < baseline latency
     - Both satisfy Shapley axioms

**Example Integration Test:**

```python
def test_full_pipeline():
    """Test end-to-end pipeline from image to explanation."""
    # Arrange
    image_path = 'tests/data/sample_face.jpg'
    config = load_config('configs/evaluate.yaml')

    # Act
    model = ModelFactory.create(config['model'])
    explainer = HierarchicalSHAP(model, **config['explainer'])
    calibrator = StatisticalCalibrator(**config['calibrator'])

    image = load_image(image_path)
    features = extract_features(image)

    shapley = explainer.explain(model, image, features)
    calibrated = calibrator.calibrate(shapley, demographic='asian')
    heatmap = visualize(calibrated, image, features)

    # Assert
    assert heatmap.shape == (224, 224, 3)
    assert torch.allclose(shapley.sum(), 1.0, atol=0.05)
    assert calibrated.shape == (8,)

    # Runtime check
    start = time.time()
    _ = explainer.explain(model, image, features)
    latency = (time.time() - start) * 1000  # ms
    assert latency < 100, f"Latency {latency}ms exceeds 100ms requirement"
```
```

**Word Count:** 400-600 words

---

### 5.Z.3 Validation Against Theory

**Template:**

```markdown
### 5.Z.3 Validation Against Theory

**Purpose:** Verify implementation matches theoretical results from Chapter 3.

**Theoretical Predictions:**

| Property | Theoretical Result (Chapter 3) | Implementation | Match? |
|----------|-------------------------------|----------------|--------|
| Complexity | O(M log M + K·D) | [Measured] | ✅/❌ |
| Approximation Error | O(R/√K) | [Measured] | ✅/❌ |
| Shapley Axioms | All 4 satisfied | [Tested] | ✅/❌ |

**Validation Tests:**

1. **Complexity Verification:**
   - **Theory:** Theorem 3.3 predicts O(M log M + K·D) time complexity
   - **Test:** Run explainer with varying M (4, 8, 16, 32) and K (50, 100, 200), measure runtime
   - **Result:** [Plot showing log-linear relationship]
   - **Conclusion:** Implementation matches theoretical complexity

2. **Approximation Error Verification:**
   - **Theory:** Theorem 3.5 predicts error ε = O(R/√K)
   - **Test:** Compare hierarchical SHAP with exact SHAP (brute force for M=4), vary K
   - **Result:** Error decreases as 1/√K (slope = -0.5 on log-log plot)
   - **Conclusion:** Implementation matches theoretical bound

3. **Axiom Verification:**
   - **Theory:** Theorem 3.2 proves all 4 Shapley axioms hold
   - **Test:** Property-based testing with Hypothesis (1000 random inputs)
   - **Result:** All axioms satisfied within numerical tolerance (ε=1e-6)
   - **Conclusion:** Implementation is a valid Shapley value

**Validation Results:**

**Figure 5.X: Complexity Verification**
[Plot: M on x-axis (log scale), runtime on y-axis (log scale), showing log-linear relationship]

**Figure 5.Y: Approximation Error Verification**
[Plot: K on x-axis (log scale), error on y-axis (log scale), showing -0.5 slope]
```

**Word Count:** 400-700 words

---

## 5.W Summary

**Purpose:** Recap the implementation and transition to results (Chapter 6).

**Template:**

```markdown
## 5.W Summary

This chapter described the implementation of [SYSTEM NAME], the [DESCRIPTION] presented in Chapter 4. We developed a [TECHNOLOGIES] system consisting of [N] major components:

1. **[Component 1]:** [Brief recap]
2. **[Component 2]:** [Brief recap]
3. **[Component 3]:** [Brief recap]
...

**Key Highlights:**

- **Architecture:** [Modular/Scalable/Extensible] design with [X] lines of code
- **Performance:** [Y ms latency, Z fps throughput]
- **Testing:** [A]% code coverage with [B] unit tests and [C] integration tests
- **Challenges:** Overcame [key challenges] through [solutions]
- **Validation:** Implementation matches theoretical predictions (Chapter 3)

**Code Availability:**

The complete implementation is open-source and available at [REPOSITORY URL] under the [LICENSE] license. See Appendix [X] for installation instructions and usage examples.

**Connection to Chapter 6:**

In the next chapter, we evaluate the system's performance on [DATASETS] to answer our research questions:
- **RQ1:** [Brief statement]
- **RQ2:** [Brief statement]
- **RQ3:** [Brief statement]

We report [METRICS] and compare against [BASELINES].
```

**Example:**

```markdown
## 5.8 Summary

This chapter described the implementation of FastSHAP-ViT, the real-time explainability framework for vision transformers presented in Chapter 4. We developed a GPU-accelerated PyTorch system consisting of 5 major components:

1. **Input Processor:** Preprocesses images with face detection and landmark extraction
2. **E-ViT Model:** Vision transformer with explainable multi-head attention (E-MHA)
3. **Hierarchical SHAP Explainer:** Computes Shapley values using hierarchical approximation
4. **Demographic Calibrator:** Reduces explanation bias across demographic groups
5. **Visualization Generator:** Creates heatmaps and attribution overlays

**Key Highlights:**

- **Architecture:** Modular design with 5,927 lines of Python code organized into 8 modules
- **Performance:** 58ms latency per explanation (17 fps throughput) with 8.2GB GPU memory
- **Testing:** 87% code coverage with 142 unit tests and 12 integration tests
- **Challenges:** Overcame GPU memory overflow (checkpointing), attention bias (CLS-agnostic aggregation), and numerical instability (atan2-based geodesic distance)
- **Validation:** Complexity matches O(M log M) prediction, approximation error follows O(1/√K) bound, all Shapley axioms verified

**Code Availability:**

The complete implementation is open-source and available at https://github.com/username/fastshap-vit under the MIT license. See Appendix A for installation instructions and usage examples.

**Connection to Chapter 6:**

In the next chapter, we evaluate FastSHAP-ViT's performance on LFW and FairFace datasets to answer our research questions:
- **RQ1 (Computational Optimization):** Can we achieve <50ms latency while maintaining >0.7 insertion AUC?
- **RQ2 (Architectural Integration):** Does E-ViT with E-MHA preserve >99% accuracy on LFW?
- **RQ3 (Demographic Fairness):** Can calibration reduce explanation variance to <10% across demographics?

We report faithfulness (insertion/deletion AUC), accuracy (LFW), fairness (variance ratio), and latency (ms). We compare against KernelSHAP, Grad-CAM, LIME, and vanilla ViT baselines.
```

**Word Count:** 300-500 words

---

## CODE SNIPPETS GUIDELINES

### When to Include Code

**✅ Include Code For:**
- Core algorithms (the "brain" of your system)
- Novel techniques or clever optimizations
- Tricky implementation details not obvious from pseudocode
- Critical functions referenced in multiple places
- Code that illustrates a key design pattern

**❌ Don't Include Code For:**
- Boilerplate (imports, argument parsing, logging setup)
- Standard library usage ("we use `numpy.array` to store data")
- Trivial getters/setters
- Entire classes (just show key methods)
- Code that's longer than 30 lines (link to repo instead)

### How to Present Code

**1. Syntax Highlighting:**
Use markdown code blocks with language specification:

````markdown
```python
def function_name(arg1, arg2):
    """Docstring here."""
    return result
```
````

**2. Commenting Key Lines:**
```python
def hierarchical_shap(model, input, features, K=100):
    M = len(features)
    L = int(np.ceil(np.log2(M)))  # Number of tree levels

    # Core loop: sample and evaluate coalitions at each level
    for level in range(L):
        coalitions = sample_coalitions(...)  # ← Novel sampling strategy
        values = evaluate_coalitions(...)     # ← GPU-accelerated batch
        marginal_contributions[:, level] = ...

    return marginal_contributions.sum(dim=1)  # ← Aggregate across levels
```

**3. Snippet Length:**
- Aim for < 20 lines per snippet
- If longer, show only the key parts:
  ```python
  def long_function(...):
      # ... [setup code omitted] ...

      # Key part: hierarchical sampling
      for level in range(L):
          coalitions = sample_coalitions(tree, level, K)
          # ... [details in repository] ...

      return result
  ```

**4. Repository References:**
```markdown
The complete implementation (235 lines) is available at:
`src/explainers/hierarchical_shap.py:45-280`

See repository: https://github.com/username/project
```

### Pseudocode vs. Real Code

**Use Pseudocode When:**
- Explaining conceptual flow (high-level algorithm)
- Comparing with methodology chapter (Algorithm 4.X)
- Avoiding language-specific details

**Use Real Code When:**
- Showing actual implementation details
- Demonstrating language-specific techniques (e.g., PyTorch JIT)
- Proving reproducibility

**Example of Both:**

**Pseudocode (Conceptual):**
```
Algorithm: Hierarchical SHAP
1. Build tree over features
2. For each level:
   a. Sample coalitions
   b. Evaluate model
   c. Estimate marginal contributions
3. Aggregate and return
```

**Real Code (Implementation):**
```python
def hierarchical_shap(model, input, features, K=100):
    tree = build_feature_tree(features)
    marginal = torch.zeros(len(features), int(np.ceil(np.log2(len(features)))))

    for level in range(tree.depth):
        coalitions = sample_coalitions(tree, level, K)
        values = model(apply_coalitions(input, coalitions, features))
        marginal[:, level] = estimate_marginal(coalitions, values)

    return marginal.sum(dim=1)
```

---

## QUALITY CHECKLIST

### Implementation Quality
- [ ] All major components are implemented (Section 5.2)
- [ ] Core algorithms match pseudocode from Chapter 4
- [ ] Edge cases are handled (Section 5.X.2)
- [ ] Performance is optimized (Section 5.X.3)
- [ ] Code is modular and follows design patterns (Section 5.2.4)

### Documentation
- [ ] Code availability statement is clear (Section 5.1)
- [ ] Repository URL and license are provided
- [ ] Directory structure is explained (Section 5.Y.1)
- [ ] Key modules are documented (Section 5.Y.2)
- [ ] Dependencies are listed with versions (Section 5.Y.3)
- [ ] Code snippets are concise (< 30 lines) and well-commented

### Testing
- [ ] Unit tests achieve > 80% coverage (Section 5.Z.1)
- [ ] Integration tests verify end-to-end pipeline (Section 5.Z.2)
- [ ] Implementation matches theoretical predictions (Section 5.Z.3)
- [ ] Shapley axioms (or equivalent properties) are verified
- [ ] Edge cases are covered by tests

### Reproducibility
- [ ] Installation instructions are provided (README or Appendix)
- [ ] Configuration files are included (configs/)
- [ ] Random seeds are documented
- [ ] Hardware requirements are specified
- [ ] Dependencies are pinned (requirements.txt)

### Clarity
- [ ] Architecture diagram is included (Figure 5.1)
- [ ] Data flow is explained step-by-step (Section 5.2.3)
- [ ] Implementation challenges are honestly discussed (Section 5.X)
- [ ] Performance results are quantified (latency, throughput, memory)
- [ ] Transitions to Chapter 6 are clear (Section 5.W)

---

## FIGURE RECOMMENDATIONS

### Figure 5.1: System Architecture Diagram

**Purpose:** High-level view of components and their interactions

**What to Include:**
- Major components (boxes)
- Data flow (arrows)
- Technologies used (labels)
- Input and output

**Tools:**
- Draw.io (web-based, free)
- PowerPoint/Keynote (easy for simple diagrams)
- PlantUML (code-based UML diagrams)

---

### Figure 5.2: Component Interaction Flowchart

**Purpose:** Detailed view of how components call each other

**What to Include:**
- Sequence of operations (vertical timeline)
- Function calls between components
- Data passed at each step

**Example:** UML sequence diagram

---

### Figure 5.3: Class Diagram (UML)

**Purpose:** Object-oriented design structure

**What to Include:**
- Key classes
- Inheritance relationships
- Key methods and attributes

**Tools:** PlantUML, Lucidchart

---

### Figure 5.4: Performance Profiling Results

**Purpose:** Show bottlenecks and optimization impact

**What to Include:**
- Bar chart: time breakdown by component (before/after optimization)
- Speedup numbers labeled on bars

---

### Figure 5.5: Test Coverage Visualization

**Purpose:** Show which parts of code are tested

**What to Include:**
- Bar chart: coverage % by module
- Overall coverage number

**Tool:** pytest-cov generates HTML reports

---

## REVISION ITERATION PROCESS

### Iteration 1: Completeness (Week 1)
**Goal:** Ensure all major components are described

**Checklist:**
- [ ] All components from Section 5.2 have detailed sections (5.3, 5.4, ...)
- [ ] Architecture diagram is included (Figure 5.1)
- [ ] Code availability statement is present (Section 5.1)
- [ ] Directory structure is documented (Section 5.Y.1)
- [ ] Testing strategy is explained (Section 5.Z)

**Output:** Complete draft covering all major components

---

### Iteration 2: Code Quality (Week 2)
**Goal:** Verify implementation follows best practices

**Checklist:**
- [ ] Design patterns are documented (Section 5.2.4)
- [ ] Code snippets are concise (< 30 lines) and well-commented
- [ ] Edge cases are handled (Section 5.X.2)
- [ ] Error handling is documented
- [ ] Performance optimizations are explained (Section 5.X.3)

**Output:** Chapter demonstrates high-quality engineering

---

### Iteration 3: Testing (Week 3)
**Goal:** Ensure testing coverage is adequate

**Checklist:**
- [ ] Unit tests achieve > 80% coverage
- [ ] Integration tests verify end-to-end pipeline
- [ ] Validation against theory is provided (Section 5.Z.3)
- [ ] Critical tests are identified and explained
- [ ] Test execution instructions are clear

**Output:** Convincing evidence of correctness

---

### Iteration 4: Documentation (Week 4)
**Goal:** Make implementation accessible to others

**Checklist:**
- [ ] README exists with quick start guide
- [ ] Installation instructions are clear
- [ ] Dependencies are documented with versions
- [ ] API documentation exists (Sphinx or similar)
- [ ] Usage examples are provided
- [ ] Repository is public (if claimed)

**Output:** Others can reproduce your work

---

### Iteration 5: Reproducibility (Week 5)
**Goal:** Ensure independent researchers can replicate results

**Checklist:**
- [ ] Configuration files separate code from hyperparameters
- [ ] Random seeds are documented
- [ ] Hardware requirements are specified
- [ ] Docker image or environment.yml provided (optional but recommended)
- [ ] Repository includes sample data or download scripts
- [ ] README includes expected outputs

**Output:** Reproducible research artifact

---

## WHEN TO STOP ITERATING

**Stop when:**
✅ All major components are described
✅ Code is available at stated repository URL
✅ Tests achieve > 80% coverage (or justify why not)
✅ Implementation matches theoretical predictions
✅ Performance results are quantified
✅ Challenges are honestly documented
✅ Others can install and run your code

**Don't stop if:**
❌ Code availability statement is missing or vague
❌ Repository is private (if you claimed open-source)
❌ No tests are mentioned
❌ Implementation differs from methodology (Chapter 4) without explanation
❌ Performance claims are unsupported
❌ Code doesn't compile/run

---

## ESTIMATED TIME INVESTMENT

| Task | Time Estimate |
|------|---------------|
| Section 5.1 (Introduction) | 2-4 hours |
| Section 5.2 (Architecture) | 6-10 hours |
| Sections 5.3-5.X (Components) | 5-10 hours each × N components |
| Section 5.Y (Challenges) | 4-8 hours |
| Section 5.Z (Code Organization) | 3-6 hours |
| Section 5.W (Testing) | 6-12 hours |
| Section 5.V (Summary) | 2-4 hours |
| Figures (5-6 figures) | 6-12 hours |
| Revision Iterations 1-5 | 20-30 hours |
| **Total** | **80-150 hours** |

**Note:** Time varies based on:
- Complexity of implementation (simple script vs. large system)
- Whether code is already written (documenting vs. implementing)
- Testing completeness (minimal vs. comprehensive)
- Figure quality (ASCII art vs. professional diagrams)

---

## RESOURCES

### Software Documentation Guides

1. **"Documentation Guide"** by Write the Docs Community
   - Comprehensive guide to technical documentation
   - URL: https://www.writethedocs.org/guide/

2. **"The Best API Documentation"** by Tom Johnson
   - Though focused on APIs, principles apply to implementation chapters

3. **"Clean Code"** by Robert C. Martin (2008)
   - Best practices for writing maintainable code

4. **"The Pragmatic Programmer"** by Hunt & Thomas (2019)
   - Software engineering wisdom

### Testing Resources

- **Pytest Documentation:** https://docs.pytest.org/
- **Hypothesis (Property-Based Testing):** https://hypothesis.readthedocs.io/
- **Coverage.py:** https://coverage.readthedocs.io/

### Diagram Tools

- **Draw.io:** https://www.drawio.com/ (free, web-based)
- **PlantUML:** https://plantuml.com/ (code-based UML)
- **Mermaid:** https://mermaid-js.github.io/ (markdown-based diagrams)

---

## WORD COUNT TARGET

**Overall Target:** 7,000-10,000 words

**Breakdown by Section:**
- Section 5.1 (Introduction): 500-800 words
- Section 5.2 (Architecture): 1,200-2,000 words
- Sections 5.3-5.X (Components): 1,000-2,000 words each × N components
- Section 5.Y (Challenges): 1,000-1,500 words
- Section 5.Z (Code Organization): 800-1,200 words
- Section 5.W (Testing): 1,200-2,000 words
- Section 5.V (Summary): 300-500 words

**Current Word Count:** [TRACK HERE]

**Note:** Word counts include code snippets and captions, but not full code listings.

---

## NOTES TO SELF

**[YOUR NOTES]**

Use this space to track:
- Components to describe:
- Challenges to document:
- Figures to create:
- Tests to write/document:
- TODOs:

---

## 📚 UNIVERSAL CITATION REMINDER

**RULE 1: SCIENTIFIC TRUTH COMES FIRST**

⚠️ **CRITICAL:** Before submitting ANY section of this chapter:

- [ ] All libraries/frameworks used are cited (PyTorch, timm, NumPy, etc.)
- [ ] Design patterns are cited if borrowed from literature
- [ ] Algorithms implemented from papers are cited
- [ ] Baseline implementations are cited (e.g., KernelSHAP from Lundberg et al.)
- [ ] Testing methodologies are cited if following established practices
- [ ] Code availability statement includes repository URL and license

**Software Citations:**

Use this format:
> We implement the system in PyTorch 2.0 (Paszke et al., 2019) using the timm library for ViT backbones (Wightman, 2021).

**See:** [citation_guidelines.md](../../tools/bibliography/citation_guidelines.md) for detailed guidance.

---

**END OF TEMPLATE**

---

**STATUS:** ✅ Enhanced from 30% → 95% (October 10, 2025)
**Improvements:** Complete rewrite with comprehensive guidance, templates, examples, code presentation guidelines, testing strategies, challenge documentation framework, quality checklists, figure recommendations, and 5-iteration revision process
