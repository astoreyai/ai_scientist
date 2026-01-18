# @keywords-develop - Generate Research Keywords

Develop effective keywords for literature searches, abstracts, and article indexing.

## Skill Type
**Category:** Literature Review / Writing
**Tier:** Core (Tier 1)
**Reusability:** Very High - needed for searches, abstracts, submissions

## What This Skill Does

1. Generates keyword lists for literature searches
2. Creates keywords for article abstracts (3-7 words/phrases)
3. Maps to controlled vocabularies (MeSH, ACM, IEEE)
4. Optimizes for discoverability and search engines
5. Validates keyword effectiveness

## Invocation

```
@keywords-develop [topic] [purpose]
```

## Keyword Types

### 1. Search Keywords (Literature Review)
**Purpose:** Find relevant papers in databases

**Characteristics:**
- Broad and narrow terms
- Synonyms and variants
- Boolean operators (AND, OR, NOT)
- Wildcards (*, ?)

**Example:**
```
("explainable AI" OR XAI OR "interpretable machine learning")
AND
("face recognition" OR "facial recognition" OR "face verification")
```

### 2. Index Keywords (For Your Paper)
**Purpose:** Help readers find your published work

**Characteristics:**
- 3-7 specific terms/phrases
- Mix of broad and specific
- From controlled vocabulary if required
- Appear in title/abstract

**Example:**
```
Keywords: explainable AI, biometric verification, face recognition,
GradCAM, attribution methods, deep learning, interpretability
```

### 3. MeSH Terms (Medical/Health)
**Purpose:** Index in PubMed/MEDLINE

**Characteristics:**
- Controlled vocabulary
- Hierarchical structure
- Major vs minor descriptors

### 4. ACM/IEEE Keywords (Computer Science)
**Purpose:** Index in CS databases

**Characteristics:**
- ACM Computing Classification System
- IEEE Thesaurus terms

## Input Format

### Simple Topic
```
@keywords-develop

Topic: Explainable AI for face recognition
Purpose: Literature search
```

### Detailed Context
```
@keywords-develop

Topic: Falsifiable attribution for biometric face recognition
Audience: Computer science, security, machine learning
Goals:
  1. Find existing work on XAI + biometrics
  2. Keywords for my dissertation abstract
  3. Search terms for OpenAlex/Web of Science
```

### From Abstract
```
@keywords-develop

Here's my abstract:
[paste 200-word abstract]

Generate 5-7 keywords for journal submission.
```

## Output Examples

### Example 1: Literature Search Keywords

**Input:**
```
@keywords-develop

I need to search for papers on XAI methods for biometric systems.
Databases: OpenAlex, Google Scholar, IEEE Xplore
```

**Output:**

```markdown
## Literature Search Keywords: XAI for Biometrics

### Core Concept Clusters

**Cluster 1: Explainability/Interpretability**
```
"explainable AI" OR "explainable artificial intelligence" OR XAI OR
"interpretable machine learning" OR interpretability OR
"model explanation" OR "black box explanation" OR transparency OR
"attribution methods" OR saliency OR "attention mechanisms"
```

**Cluster 2: Biometric Modality**
```
biometric* OR "face recognition" OR "facial recognition" OR
"face verification" OR "face identification" OR
"facial biometric*" OR "face matching" OR
"identity verification" OR authentication
```

**Cluster 3: XAI Methods**
```
GradCAM OR "Grad-CAM" OR LIME OR "Local Interpretable" OR
SHAP OR "Shapley" OR "Integrated Gradients" OR
"Layer-wise Relevance" OR LRP OR "attention map*" OR
"saliency map*" OR heatmap* OR attribution
```

**Cluster 4: Evaluation/Quality**
```
faithfulness OR fidelity OR consistency OR
"explanation quality" OR "attribution quality" OR
"localization accuracy" OR "explainability evaluation"
```

---

### Boolean Search Strings

**Option 1 (Broad - use for initial search):**
```
("explainable AI" OR XAI OR interpretab*)
AND
(biometric* OR "face recognition" OR "face verification")
```

**Expected results:** 500-2000 papers

---

**Option 2 (Medium specificity):**
```
("explainable AI" OR XAI OR "attribution method*")
AND
("face recognition" OR "face verification")
AND
(GradCAM OR LIME OR SHAP OR "saliency map*")
```

**Expected results:** 100-500 papers

---

**Option 3 (Narrow - for very specific search):**
```
("explainable AI" OR XAI)
AND
("face verification" OR "biometric verification")
AND
(GradCAM OR "Grad-CAM")
AND
("faithfulness" OR "explanation quality")
```

**Expected results:** 20-100 papers

---

### Recommended Search Strategy

1. **Start broad (Option 1)** - get overview
2. **Refine to medium (Option 2)** - find relevant clusters
3. **Go narrow (Option 3)** - find directly comparable work

### Database-Specific Syntax

**OpenAlex:**
```
display_name.search:"explainable AI" AND
display_name.search:"face recognition"
```

**Google Scholar:**
```
allintitle: "explainable AI" "face recognition"
```

**IEEE Xplore:**
```
("Document Title":"explainable AI" OR "Abstract":"XAI")
AND "Index Terms":"face recognition"
```

---

### Related Terms to Add

**Synonyms for "Explainable AI":**
- Interpretable AI
- Transparent AI
- Understandable AI
- Model explanation
- AI transparency

**Synonyms for "Face Recognition":**
- Facial recognition
- Face verification
- Face identification
- Facial biometrics
- Face matching

**Domain terms:**
- Deep learning
- Convolutional neural networks
- Transfer learning
- Verification accuracy
```

### Example 2: Keywords for Journal Submission

**Input:**
```
@keywords-develop

Generate keywords for my paper:

Title: "Falsifiable Attribution: A Framework for Explainable Biometric Face Verification"

Abstract: [250-word abstract about theoretical framework, BiometricGradCAM, experiments on VGGFace2/LFW]

Journal: IEEE Transactions on Biometrics, Behavior, and Identity Science
Required: 5-7 keywords from IEEE Thesaurus
```

**Output:**

```markdown
## Keywords for Journal Submission

### Recommended Keywords (5-7)

**Option A (Balanced - Recommended):**
1. Explainable artificial intelligence
2. Biometric verification
3. Face recognition
4. Attribution methods
5. Deep learning
6. Image analysis
7. Trustworthy AI

**Why these work:**
- ✅ Mix of broad (XAI, deep learning) and specific (biometric verification)
- ✅ All appear in IEEE Thesaurus
- ✅ Cover theory (XAI), application (biometrics), method (attribution)
- ✅ Appear in your title/abstract

---

**Option B (More Technical):**
1. Explainable artificial intelligence
2. Face verification
3. Gradient-based attribution
4. Convolutional neural networks
5. Biometric faithfulness
6. Saliency mapping

**When to use:** If journal prefers technical specificity

---

**Option C (More Applied):**
1. Biometric authentication
2. Explainable AI
3. Face recognition systems
4. Interpretability
5. Security applications
6. Deep neural networks

**When to use:** If emphasizing practical applications

---

### Keyword Analysis

| Keyword | Specificity | Search Volume | Appears in Title? | Appears in Abstract? | IEEE Thesaurus? |
|---------|-------------|---------------|-------------------|----------------------|-----------------|
| Explainable AI | Medium | High (10K+) | ✅ Yes | ✅ Yes | ✅ Yes |
| Biometric verification | Medium | Medium (2K+) | ✅ Yes | ✅ Yes | ✅ Yes |
| Face recognition | Broad | Very High (50K+) | ✅ Yes | ✅ Yes | ✅ Yes |
| Attribution methods | Specific | Low (500+) | ✅ Yes | ✅ Yes | ✅ Yes |
| Deep learning | Broad | Very High (100K+) | ❌ No | ✅ Yes | ✅ Yes |
| GradCAM | Very Specific | Very Low (100+) | ❌ No | ✅ Yes | ❌ No |

**Recommendation:** Use Option A (includes 5 high/medium volume terms + 2 specific terms)

---

### Discoverability Optimization

**High-impact keywords (include at least 2):**
- Explainable AI (emerging field, high interest)
- Face recognition (established field, high search volume)
- Biometric verification (specific domain)

**Niche keywords (include 1-2):**
- Attribution methods (specialists will search)
- Falsifiable (unique to your framework)

**Broad keywords (include 1):**
- Deep learning (connects to larger community)

---

### Final Recommendation

**Keywords:**
```
explainable artificial intelligence, biometric verification,
face recognition, attribution methods, deep learning,
interpretability, trustworthy AI
```

**Rationale:**
- ✅ 7 keywords (within journal range 5-7)
- ✅ All IEEE Thesaurus terms
- ✅ Mix of broad and specific
- ✅ High discoverability (>15K combined searches/month)
- ✅ Covers theory, method, application
```

### Example 3: From Dissertation Title to Keywords

**Input:**
```
@keywords-develop

Dissertation title: "Falsifiable Attribution for Biometric Face Recognition: A Theoretical Framework and Empirical Validation"

Generate:
1. Keywords for dissertation abstract (ProQuest)
2. Keywords for Chapter 1
3. Search terms to find related dissertations
```

**Output:**

```markdown
## Keywords for PhD Dissertation

### 1. Dissertation Abstract Keywords (ProQuest)

**Primary Keywords (Required - 5):**
1. Explainable artificial intelligence
2. Biometric face recognition
3. Attribution methods
4. Theoretical frameworks
5. Deep learning

**Rationale:**
- Cover all major components (XAI, biometrics, theory, methods)
- Broad enough for discoverability
- Specific enough to filter relevant searches

---

### 2. Chapter-Specific Keywords

**Chapter 1 (Introduction):**
- Explainable AI, face recognition, biometric security, deep learning, interpretability

**Chapter 2 (Literature Review):**
- XAI methods, GradCAM, LIME, SHAP, saliency maps, attribution

**Chapter 3 (Theoretical Framework):**
- Falsifiable attribution, theoretical properties, biometric faithfulness, verification constraints

**Chapter 4 (Methodology):**
- BiometricGradCAM, gradient-based attribution, experimental design, VGGFace2

**Chapter 5 (Implementation):**
- PyTorch, ArcFace, ResNet, implementation, software engineering

**Chapter 6 (Results):**
- Localization accuracy, consistency metrics, cross-dataset validation, LFW

**Chapter 7 (Discussion):**
- Trustworthy AI, deployment implications, limitations, future work

---

### 3. Search Terms for Related Dissertations

**Search ProQuest Dissertations & Theses:**

```
noft(explainable AI OR XAI) AND
noft(face recognition OR biometric* OR facial recognition) AND
noft(deep learning OR neural network*)
```

**Expected:** 50-200 dissertations

**Narrow down:**
```
ti(explainable) AND ti(biometric* OR face)
```

**Expected:** 5-20 directly related dissertations

---

**Search Google Scholar (for recent PhD work):**
```
allintitle: PhD "explainable AI" biometric*
```

---

### Keyword Hierarchy

```
Level 1 (Broadest):
  ├─ Artificial Intelligence
  └─ Biometrics

Level 2:
  ├─ Explainable AI
  ├─ Deep Learning
  └─ Face Recognition

Level 3:
  ├─ Attribution Methods
  ├─ Interpretability
  └─ Verification

Level 4 (Most Specific):
  ├─ GradCAM
  ├─ BiometricGradCAM
  ├─ Falsifiable Attribution
  └─ Localization Accuracy
```

**Usage:**
- Abstract: Include 2-3 from each level
- Chapter keywords: Focus on Level 3-4
- Search: Start Level 1-2, refine to 3-4
```

## Keyword Development Strategy

### Step 1: Brainstorm Core Concepts
List main ideas from your research (5-10 concepts)

### Step 2: Find Synonyms
For each core concept, list 3-5 synonyms/variants

### Step 3: Check Controlled Vocabularies
- ACM Computing Classification
- IEEE Thesaurus
- MeSH (if medical)
- Library of Congress Subject Headings

### Step 4: Validate Search Volume
Use Google Scholar to check:
- Too broad: >50,000 results
- Good: 1,000-50,000 results
- Too narrow: <100 results

### Step 5: Test and Refine
Run searches, adjust based on results

## Validation Checks

The skill validates:
- ✅ Keywords appear in title or abstract
- ✅ Mix of broad and specific terms
- ✅ Controlled vocabulary compliance (if required)
- ✅ 3-7 keywords for abstracts
- ✅ No redundancy (e.g., "XAI" and "explainable AI" both included)
- ✅ Search volume reasonable

## Common Mistakes Fixed

### Mistake 1: Too Generic
❌ "Machine learning, AI, computer science, algorithms"

✅ "Explainable AI, biometric verification, face recognition, attribution methods"

### Mistake 2: Too Specific
❌ "BiometricGradCAM, VGGFace2, ArcFace-ResNet100"

✅ Mix broad ("face recognition") with specific ("BiometricGradCAM")

### Mistake 3: Not in Controlled Vocabulary
❌ "Black-box AI" (not in IEEE Thesaurus)

✅ "Explainable artificial intelligence" (IEEE term)

### Mistake 4: Redundant
❌ "XAI, explainable AI, explainable artificial intelligence"

✅ Pick one: "explainable artificial intelligence"

## Time Savings

**Manual keyword development:** 2-3 hours (searching thesauri, testing, refining)
**Using @keywords-develop:** 15-20 minutes
**Saved:** ~2 hours 🎉

## Best Practices

### 1. Align with Title/Abstract
Keywords should appear in title or abstract.

### 2. Think Like a Searcher
What would someone search to find your work?

### 3. Balance Broad and Narrow
2-3 broad terms (discoverability) + 2-3 narrow terms (precision)

### 4. Check Journal Requirements
Some journals require specific controlled vocabularies.

### 5. Update as Field Evolves
"Neural networks" (1990s) → "deep learning" (2010s) → "foundation models" (2020s)

## Integration with Dissertation

### Abstract (End)
```
Keywords: explainable artificial intelligence, biometric verification,
face recognition, attribution methods, deep learning
```

### ProQuest Submission
Required fields:
- Subject categories (choose 2-3)
- Keywords (5-7)
- Abstract (350 words max)

### Journal Submission
Varies by journal:
- IEEE: 5-7 from IEEE Thesaurus
- ACM: ACM CCS categories
- Springer: Free-text keywords (3-6)

## Field-Specific Notes

### Computer Science
**Common terms:**
- Algorithms, machine learning, deep learning
- Computer vision, natural language processing
- Software engineering, systems

**Controlled vocabulary:** ACM Computing Classification System

### Medical/Health
**Common terms:**
- Clinical trials, diagnosis, treatment
- Epidemiology, public health
- Patient outcomes

**Controlled vocabulary:** MeSH (Medical Subject Headings)

### Social Sciences
**Common terms:**
- Qualitative research, quantitative methods
- Theory development, empirical studies
- Human behavior, social systems

**Controlled vocabulary:** APA Thesaurus

## Related Skills

- `/run-literature-search` - Use keywords to search databases
- `@abstract-writer` - Keywords appear at end of abstract
- `@lit-gap` - Keywords help scope literature review
- `@inclusion-criteria` - Keywords define search scope

---

**Status:** Documented
**Complexity:** Low-Medium
**Time to use:** 15-20 minutes
**Time saved:** ~2 hours
**Reusability:** Very High (every paper, search, abstract)
**Critical for:** Literature search, paper submission, discoverability
