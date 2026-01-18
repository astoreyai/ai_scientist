# Keyword Development Guide for Scopus Searches

**Quick reference for developing comprehensive search queries**

---

## Overview

Effective literature searches require **well-developed keywords** organized by concept. This guide shows you how to:

1. ✅ Break research questions into concepts
2. ✅ Generate comprehensive keyword lists
3. ✅ Build Boolean search queries
4. ✅ Test and refine searches

---

## Step-by-Step Process

### Step 1: Identify Core Concepts (2-4 per search)

Break your research question into **independent concepts** that must ALL appear in results.

**Example Research Question:**
> "How are SHAP explanations used in medical diagnosis?"

**Concepts:**
- Concept 1: SHAP explanations
- Concept 2: Medical diagnosis

**Rule:** Each concept = one group of synonyms connected with OR

---

### Step 2: Brainstorm Keywords per Concept

For each concept, list:
- ✅ **Main terms** - Primary vocabulary
- ✅ **Synonyms** - Alternative terms with same meaning
- ✅ **Acronyms** - Common abbreviations
- ✅ **Related terms** - Closely associated concepts
- ✅ **Variant spellings** - UK/US differences, hyphenation

**Example for Concept 1 (SHAP explanations):**

```yaml
concept_1_shap:
  - "SHAP"                              # Acronym
  - "Shapley"                           # Full name
  - "Shapley values"                    # Technical term
  - "SHapley Additive exPlanations"    # Full expansion
  - "game-theoretic explanation"        # Related concept
  - "cooperative game theory"           # Theoretical basis
```

**Example for Concept 2 (Medical diagnosis):**

```yaml
concept_2_medical:
  - "medical diagnosis"                 # Main term
  - "clinical diagnosis"                # Synonym
  - "disease detection"                 # Related term
  - "diagnostic imaging"                # Specific application
  - "radiology"                         # Specific domain
  - "pathology"                         # Specific domain
  - "healthcare"                        # Broader term
  - "biomedical"                        # Related
```

**Tips:**
- Start with 5-10 keywords per concept
- Add more if searches return too few results
- Remove overly broad terms if too many irrelevant results

---

### Step 3: Build Boolean Query

Connect keywords using Boolean operators:

**Within concepts: Use OR**
```
"SHAP" OR "Shapley" OR "Shapley values" OR "game-theoretic explanation"
```

**Between concepts: Use AND**
```
(Concept 1 terms) AND (Concept 2 terms)
```

**Full Query Example:**
```
TITLE-ABS-KEY("SHAP" OR "Shapley" OR "Shapley values" OR "game-theoretic explanation")
AND TITLE-ABS-KEY("medical diagnosis" OR "clinical diagnosis" OR "disease detection" OR "diagnostic imaging" OR "radiology")
```

---

## Boolean Operator Reference

### OR - Any term matches (within concept)
```
"machine learning" OR "deep learning" OR "neural network"
```
**Result:** Papers with ANY of these terms

### AND - All concepts must appear (between concepts)
```
("machine learning" OR "deep learning") AND ("healthcare" OR "medical")
```
**Result:** Papers with BOTH a ML term AND a healthcare term

### AND NOT - Exclude terms
```
"machine learning" AND NOT "hardware"
```
**Result:** ML papers, excluding hardware implementations
**Warning:** Use sparingly - may exclude relevant papers

### W/n - Words within n words of each other
```
"neural" W/3 "network"
```
**Result:** "neural network", "neural convolutional network", etc.

### PRE/n - Words in order within n words
```
"machine" PRE/2 "learning"
```
**Result:** "machine learning" but NOT "learning machine"

---

## Scopus Field Codes

### TITLE-ABS-KEY() - Recommended for most searches
Search in title, abstract, and author keywords
```
TITLE-ABS-KEY("explainable AI")
```

### TITLE() - Title only (more precise)
```
TITLE("systematic review")
```

### ABS() - Abstract only
```
ABS("method")
```

### KEY() - Author keywords only
```
KEY("deep learning")
```

### AUTH() - Author name
```
AUTH("Smith")
```

### AFFIL() - Author affiliation
```
AFFIL("Stanford")
```

---

## Wildcards

### * - Multiple characters
```
"comput*" matches: computer, computing, computation, computational
"neural network*" matches: neural network, neural networks
```

### ? - Single character
```
"wom?n" matches: woman, women
"analy?e" matches: analyze, analyse
```

**Warning:** Overly broad wildcards retrieve irrelevant papers
- ❌ "data*" - Too broad (database, datasheet, etc.)
- ✅ "interpret*" - Good (interpretable, interpretation, interpreted)

---

## Practical Examples

### Example 1: Narrow and Focused

**Research Question:** "Grad-CAM applications in chest X-ray diagnosis"

**Keywords:**
```yaml
concept_1_method:
  - "Grad-CAM"
  - "Gradient-weighted Class Activation Mapping"
  - "GradCAM"

concept_2_application:
  - "chest X-ray"
  - "chest radiograph"
  - "thoracic imaging"
  - "pulmonary imaging"
```

**Query:**
```
TITLE-ABS-KEY("Grad-CAM" OR "Gradient-weighted Class Activation Mapping" OR "GradCAM")
AND TITLE-ABS-KEY("chest X-ray" OR "chest radiograph" OR "thoracic imaging")
```

**Expected:** 20-50 papers (narrow, specific)

---

### Example 2: Broad Survey

**Research Question:** "Explainable AI methods in computer vision"

**Keywords:**
```yaml
concept_1_xai:
  - "explainable AI"
  - "XAI"
  - "interpretable"
  - "interpretability"
  - "transparent"
  - "explainability"
  - "attribution method"
  - "saliency map"

concept_2_cv:
  - "computer vision"
  - "image recognition"
  - "image classification"
  - "object detection"
  - "visual recognition"
```

**Query:**
```
TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretable" OR "interpretability" OR "attribution method" OR "saliency map")
AND TITLE-ABS-KEY("computer vision" OR "image recognition" OR "image classification" OR "object detection")
```

**Expected:** 200-500 papers (broad survey)

---

### Example 3: Gap Analysis

**Research Question:** "Is falsifiability applied to XAI evaluation?" (expecting few papers)

**Keywords:**
```yaml
concept_1_falsifiability:
  - "falsifiability"
  - "falsifiable"
  - "Popper"
  - "demarcation criterion"
  - "testability"
  - "refutability"

concept_2_xai:
  - "explainable AI"
  - "XAI"
  - "interpretability"
  - "machine learning explanation"
```

**Query:**
```
TITLE-ABS-KEY("falsifiability" OR "falsifiable" OR "Popper" OR "demarcation criterion")
AND TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretability")
```

**Expected:** 5-20 papers (gap identification - few papers proves novelty)

---

## Testing Your Query

### 1. Test in Scopus Web Interface First

Before automating, test manually:

1. Go to https://www.scopus.com/
2. Click "Advanced search"
3. Paste your query
4. Review results

**Check:**
- ✅ Result count reasonable (20-500 papers)
- ✅ First 20 papers are relevant
- ✅ No obvious errors in query syntax

### 2. Refine Based on Results

**Too many results (>500)?**
- Add more specific terms
- Use narrower date range
- Add subject area filter
- Use TITLE() instead of TITLE-ABS-KEY() for key terms

**Too few results (<20)?**
- Add synonyms
- Remove overly specific terms
- Expand date range
- Check for typos

**Irrelevant papers appearing?**
- Add more specific terms to make concepts clearer
- Use AND NOT to exclude common false positives
- Consider using W/n proximity operators

### 3. Validate with Dry Run

```bash
python scopus_search.py --dry-run
```

This checks:
- Query syntax is valid
- API key is configured
- No execution (safe test)

---

## Common Keyword Patterns

### Medical/Clinical Research
```yaml
# Disease names
- Official name (e.g., "myocardial infarction")
- Common name (e.g., "heart attack")
- Abbreviation (e.g., "MI")

# Populations
- "patient" OR "clinical" OR "healthcare"

# Outcomes
- "diagnosis" OR "prognosis" OR "treatment" OR "outcome"
```

### Machine Learning
```yaml
# Methods
- Full name (e.g., "Support Vector Machine")
- Abbreviation (e.g., "SVM")
- Variants (e.g., "support vector classifier")

# Tasks
- "classification" OR "regression" OR "clustering" OR "prediction"

# Evaluation
- "accuracy" OR "performance" OR "validation" OR "benchmark"
```

### Computer Vision
```yaml
# Modalities
- "image" OR "visual" OR "video" OR "frame"

# Tasks
- "recognition" OR "detection" OR "segmentation" OR "tracking"

# Domains
- "face" OR "object" OR "scene" OR "action"
```

---

## Keyword Development Worksheet

Use this template for your searches:

```yaml
# Search ID: [unique_id]
# Research Question: [your question here]

searches:
  - id: "[unique_id]"
    name: "[descriptive name]"
    description: "[what this search covers]"

    # Step 1: Identify concepts
    # Concept 1: [name]
    # Concept 2: [name]

    keywords:
      concept_1_[name]:
        - "[main term]"
        - "[synonym 1]"
        - "[synonym 2]"
        - "[acronym]"
        - "[related term]"
        # Add more...

      concept_2_[name]:
        - "[main term]"
        - "[synonym 1]"
        - "[synonym 2]"
        # Add more...

    # Step 2: Build query
    query: >
      TITLE-ABS-KEY("[term]" OR "[term]" OR "[term]")
      AND TITLE-ABS-KEY("[term]" OR "[term]")

    # Step 3: Add filters
    date_range:
      start: 2015
      end: 2025

    subject_areas:
      - COMP  # Adjust for your field

    document_types:
      - "ar"  # Article
      - "cp"  # Conference paper

    research_questions:
      - "RQ1: [your research question]"

    expected_results: "[50-200 papers]"
    notes: "[any notes about this search]"
    enabled: true
```

---

## Quick Reference Card

| **Task** | **Syntax** | **Example** |
|----------|------------|-------------|
| Exact phrase | `"phrase"` | `"machine learning"` |
| Multiple terms (OR) | `term1 OR term2` | `"XAI" OR "explainable AI"` |
| All terms (AND) | `term1 AND term2` | `("XAI") AND ("face")` |
| Exclude term | `AND NOT term` | `"AI" AND NOT "hardware"` |
| Wildcard (multiple) | `term*` | `"comput*"` |
| Wildcard (single) | `term?` | `"wom?n"` |
| Title/abstract/keywords | `TITLE-ABS-KEY()` | `TITLE-ABS-KEY("XAI")` |
| Title only | `TITLE()` | `TITLE("review")` |
| Proximity | `W/n` | `"neural" W/3 "network"` |
| Date range | `date_range:` | `start: 2015, end: 2025` |

---

## Tips for High-Quality Searches

### ✅ DO:
- Start with 2-4 core concepts
- List 5-10 keywords per concept
- Test in Scopus web interface first
- Use quotes for exact phrases
- Combine broad and narrow terms with OR
- Document all keywords in YAML
- Version control your query file

### ❌ DON'T:
- Use too many wildcards (*)
- Create overly complex queries (>4 concepts)
- Forget to test before automating
- Modify queries after execution (create new ID instead)
- Use only acronyms (add full terms too)
- Ignore false positives in test results

---

## Next Steps

1. **Define your research question** clearly
2. **Break into 2-4 concepts**
3. **Brainstorm 5-10 keywords** per concept
4. **Build query** using Boolean operators
5. **Test in Scopus web** interface
6. **Refine** based on results
7. **Add to** `config/search_queries.yaml`
8. **Execute** with `python scopus_search.py`

---

## Need Help?

**Scopus Query Syntax:**
- Official docs: https://dev.elsevier.com/sc_search_tips.html
- Example queries in `config/search_queries.yaml`

**Query Building:**
- See examples in this document
- Test in Scopus web interface
- Ask your librarian for help

**Pipeline Issues:**
- Check `automated_scopus/README.md`
- See `AUTOMATED_SCOPUS_PIPELINE.md`

---

**Well-developed keywords = High-quality literature review. Take time to get this right! ✅**
