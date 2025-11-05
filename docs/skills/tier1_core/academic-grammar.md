# @academic-grammar - Academic Writing Quality Check

Check and improve academic writing quality, grammar, style, and clarity.

## Skill Type
**Category:** Writing / Quality Assurance
**Tier:** Core (Tier 1)
**Reusability:** Very High - every draft needs review

## What This Skill Does

1. Checks grammar, punctuation, spelling
2. Identifies weak/vague language
3. Improves clarity and conciseness
4. Ensures academic tone and style
5. Detects common dissertation writing errors
6. Suggests stronger alternatives

## Invocation

```
@academic-grammar [text] [level]
```

## Check Levels

### Level 1: Basic (Grammar & Spelling)
- Spelling errors
- Basic grammar (subject-verb agreement)
- Punctuation
- **Time:** 30 seconds per paragraph

### Level 2: Style (Academic Writing)
- Passive vs active voice
- Wordiness
- Paragraph structure
- Transitions
- **Time:** 2 minutes per paragraph

### Level 3: Comprehensive (Deep Review)
- All Level 1 + Level 2 checks
- Argument clarity
- Citation integration
- Claim-evidence alignment
- Technical precision
- **Time:** 5 minutes per paragraph

## Input Format

### Quick Check
```
@academic-grammar

"The results shows that our method performs better than baseline.
It can be seen that the accuracy is higher."
```

### With Context
```
@academic-grammar level:comprehensive

Chapter 6 (Results) - First draft
[paste 2-3 paragraphs]

Check for:
- Passive voice overuse
- Vague language
- Missing citations
- Weak claims
```

### Specific Focus
```
@academic-grammar focus:passive-voice

[paste text]

I tend to overuse passive voice. Help me fix this.
```

## Output Examples

### Example 1: Grammar & Clarity

**Input:**
```
@academic-grammar

"The results clearly shows that our method performs significantly
better than the baseline method. It can be seen that the accuracy
is obviously higher and the consistency is much more better."
```

**Output:**

```markdown
## Grammar & Style Review

### Issues Found: 5

---

**Issue 1: Subject-Verb Agreement** ⚠️
> "The results clearly shows..."

**Problem:** "results" (plural) with "shows" (singular)

**Fix:**
> "The results clearly **show**..."

---

**Issue 2: Vague Adverb ("clearly")** ⚠️
> "The results clearly shows..."

**Problem:** "Clearly" is subjective and vague. If it's clear, show the data.

**Fix:**
> "The results **demonstrate** that..." OR
> "The results show that... (see Table 6.1)"

---

**Issue 3: Passive Voice + Vague** ⚠️
> "It can be seen that the accuracy is obviously higher..."

**Problem:** Passive voice ("can be seen") + vague ("obviously")

**Fix:**
> "Our method achieves **15% higher accuracy** (p < 0.001, see Table 6.1)"

---

**Issue 4: Double Comparative** ❌
> "...much more better"

**Problem:** Can't use "more" with "better" (already comparative)

**Fix:**
> "...much **better**" OR "...significantly higher"

---

**Issue 5: Lack of Specificity** ⚠️
> "performs significantly better"

**Problem:** No numbers, no statistics, no evidence

**Fix:**
> "achieves 15% higher localization accuracy (M=0.87, SD=0.04)
> compared to baseline (M=0.72, SD=0.06), t(198)=14.2, p<0.001"

---

### Revised Paragraph

**Before:**
> "The results clearly shows that our method performs significantly
> better than the baseline method. It can be seen that the accuracy
> is obviously higher and the consistency is much more better."

**After:**
> "BiometricGradCAM achieves 15% higher localization accuracy
> (M=0.87, SD=0.04) compared to GradCAM baseline (M=0.72, SD=0.06),
> t(198)=14.2, p<0.001 (see Table 6.1). Consistency scores also
> improve significantly from 0.65 to 0.92 (42% increase, p<0.001)."

**Improvements:**
- ✅ Fixed subject-verb agreement
- ✅ Removed vague language ("clearly", "obviously")
- ✅ Added specific numbers and statistics
- ✅ Changed passive to active voice
- ✅ Fixed grammar error ("more better")
- ✅ Added citation to table

**Word count:** 36 words → 50 words (+39%, but much clearer)
```

### Example 2: Passive Voice Overuse

**Input:**
```
@academic-grammar focus:passive-voice

"Experiments were conducted on two datasets. The VGGFace2 dataset
was used for training and the LFW dataset was used for testing.
200 verification pairs were selected from each dataset. The
BiometricGradCAM method was compared to four baseline methods."
```

**Output:**

```markdown
## Passive Voice Analysis

**Passive voice detected:** 5 instances in 4 sentences (100% passive!)

**Recommended:** Aim for <20% passive voice in academic writing.

---

### Sentence-by-Sentence Fixes

**Sentence 1:** ❌ Passive
> "Experiments **were conducted** on two datasets."

**Fix:** ✅ Active
> "**We conducted** experiments on two datasets."

OR (if emphasizing datasets):
> "Two datasets served as testbeds for our experiments."

---

**Sentence 2-3:** ❌ Passive (compound)
> "The VGGFace2 dataset **was used** for training and the LFW
> dataset **was used** for testing."

**Fix:** ✅ Active
> "**We used** VGGFace2 for training and LFW for testing."

OR (more concise):
> "Training used VGGFace2; testing used LFW."

---

**Sentence 4:** ❌ Passive
> "200 verification pairs **were selected** from each dataset."

**Fix:** ✅ Active
> "**We selected** 200 verification pairs from each dataset."

OR (emphasizing randomness):
> "**Random sampling produced** 200 verification pairs per dataset."

---

**Sentence 5:** ❌ Passive
> "The BiometricGradCAM method **was compared** to four baseline methods."

**Fix:** ✅ Active
> "**We compared** BiometricGradCAM to four baseline methods."

OR (emphasizing evaluation):
> "**Comparative evaluation contrasted** BiometricGradCAM with four baselines."

---

### Fully Revised Paragraph

**Before (100% passive):**
> "Experiments were conducted on two datasets. The VGGFace2 dataset
> was used for training and the LFW dataset was used for testing.
> 200 verification pairs were selected from each dataset. The
> BiometricGradCAM method was compared to four baseline methods."

**After (0% passive):**
> "We conducted experiments on two datasets. VGGFace2 provided
> training data while LFW served as the test set. Random sampling
> produced 200 verification pairs per dataset. We compared
> BiometricGradCAM against four baseline methods."

**Improvements:**
- ✅ Changed 5 passive constructions to active
- ✅ More direct and engaging
- ✅ Clearer agent (who did what)
- ✅ More concise (52 words → 41 words)

---

### When Passive Voice is OK

**Acceptable uses:**
1. **Unknown agent:** "The dataset was released in 2018." (don't know by whom)
2. **Emphasis on object:** "200 faces were incorrectly classified."
3. **Methods section convention:** "Samples were preprocessed..." (focus on procedure)
4. **Avoiding "we" overuse:** Mix active and passive for variety

**Rule of thumb:** <20% passive voice overall
```

### Example 3: Vague Language & Weak Claims

**Input:**
```
@academic-grammar focus:claims

"Our novel method significantly improves results. The proposed
approach effectively enhances performance. This innovative
technique successfully addresses the problem."
```

**Output:**

```markdown
## Vague Language & Weak Claims Analysis

**Problems identified:** 9 weak/vague terms

---

### Issue 1: "Novel" / "Innovative" Without Evidence

❌ **Vague:**
> "Our **novel** method..."
> "This **innovative** technique..."

**Problem:** Claiming novelty without specifying what's new.

✅ **Specific:**
> "Our method is the first to incorporate biometric verification
> constraints into gradient-based attribution."

OR:
> "Unlike prior work (Smith et al., 2023; Jones et al., 2022),
> our method accounts for pairwise similarity metrics."

---

### Issue 2: "Significantly" Without Statistics

❌ **Vague:**
> "...significantly improves results."

**Problem:** "Significantly" has statistical meaning. Show the stats.

✅ **Specific:**
> "...improves localization accuracy by 15% (Cohen's d=0.8,
> t(198)=14.2, p<0.001)"

---

### Issue 3: "Effectively" / "Successfully" (Redundant)

❌ **Vague:**
> "...effectively enhances performance."
> "...successfully addresses the problem."

**Problem:** If it enhances performance, it's already effective. Redundant.

✅ **Specific:**
> "...increases consistency from 0.65 to 0.92 (42% improvement)"
> "...reduces false positive rate by 23% (from 0.13 to 0.10)"

---

### Issue 4: Vague Nouns ("results", "performance", "problem")

❌ **Vague:**
> "...improves **results**"
> "...enhances **performance**"
> "...addresses the **problem**"

**Problem:** What results? Which aspect of performance? What problem?

✅ **Specific:**
> "...improves **localization accuracy** from 0.72 to 0.87"
> "...enhances **explanation faithfulness** by 28%"
> "...addresses the **lack of biometric consistency** in standard XAI"

---

### Revised Paragraph

**Before (vague):**
> "Our novel method significantly improves results. The proposed
> approach effectively enhances performance. This innovative
> technique successfully addresses the problem."

**After (specific):**
> "BiometricGradCAM is the first XAI method to incorporate
> verification constraints into gradient-based attribution.
> Compared to standard GradCAM, our method improves localization
> accuracy by 15% (from 0.72 to 0.87, Cohen's d=0.8, p<0.001)
> and increases explanation consistency by 42% (from 0.65 to 0.92,
> p<0.001). These improvements address the critical gap in
> biometric-aware explainability identified in Chapter 2."

**Improvements:**
- ✅ Removed vague adjectives ("novel", "innovative")
- ✅ Specified exact improvements with numbers
- ✅ Added statistical significance
- ✅ Named the specific problem addressed
- ✅ Referenced prior chapters for context

**Credibility:** Low → High
```

## Common Issues Checked

### Grammar Issues
- [ ] Subject-verb agreement
- [ ] Pronoun-antecedent agreement
- [ ] Verb tense consistency
- [ ] Comma splices
- [ ] Run-on sentences
- [ ] Sentence fragments

### Style Issues
- [ ] Passive voice overuse (>20%)
- [ ] Wordiness
- [ ] Weak verbs ("is", "are", "seems")
- [ ] Nominalizations ("utilization" → "use")
- [ ] Hedging overuse ("might", "could", "possibly")

### Academic Writing Issues
- [ ] Vague language ("clearly", "obviously")
- [ ] Unsupported claims
- [ ] Missing citations
- [ ] Informal tone ("really", "very", "a lot")
- [ ] Contractions ("don't", "can't")
- [ ] First person overuse

### Technical Issues
- [ ] Undefined acronyms
- [ ] Inconsistent terminology
- [ ] Ambiguous pronouns ("this", "it")
- [ ] Missing definitions
- [ ] Jargon without explanation

## RULE 1 Enforcement

**Special check:** Aspirational language

❌ **Avoid:**
- "This work will enable..."
- "Our method will allow..."
- "This can be used for..."
- "This has implications for..."

✅ **Use:**
- "This work enables..." (if you demonstrated it)
- "Our experiments show..." (what you actually did)
- "We validated on..." (what you tested)

## Academic Tone Guidelines

### Too Informal → Academic

| Too Informal | Academic |
|--------------|----------|
| "We got 87% accuracy" | "Our method achieved 87% accuracy" |
| "The results are really good" | "The results demonstrate substantial improvement" |
| "This is a big problem" | "This represents a significant challenge" |
| "It's obvious that..." | "The evidence indicates that..." |

### Conversational → Formal

| Conversational | Formal |
|----------------|--------|
| "Let's look at..." | "Consider..." / "Examine..." |
| "We can see..." | "The data show..." |
| "A lot of studies" | "Numerous studies" / "15 studies" |
| "Nowadays" | "Currently" / "In recent years" |

## Time Savings

**Manual proofreading:** 3-4 hours per chapter (20-30 pages)
**Using @academic-grammar:** 30-60 minutes per chapter
**Saved:** ~3 hours per chapter 🎉

## Best Practices

### 1. Multiple Passes
- Pass 1: Grammar/spelling
- Pass 2: Style/clarity
- Pass 3: Claims/evidence

### 2. Read Aloud
Catches awkward phrasing you miss when reading silently.

### 3. Use Tools
- Grammarly (grammar)
- Hemingway Editor (readability)
- @academic-grammar (academic style)

### 4. Get Peer Review
Fresh eyes catch different issues.

### 5. Wait 24 Hours
Review with fresh perspective.

## Common Mistakes by Chapter

### Chapter 1 (Introduction)
- Vague research questions
- Overstating significance
- Missing clear structure

### Chapter 2 (Literature Review)
- Too many quotes (paraphrase instead)
- Missing synthesis (just listing papers)
- Citation format inconsistencies

### Chapter 3-4 (Methodology)
- Passive voice overuse
- Insufficient detail for replication
- Undefined variables/terms

### Chapter 6 (Results)
- Interpreting instead of reporting
- Missing descriptive statistics
- No reference to tables/figures

### Chapter 7 (Discussion)
- Overgeneralizing results
- Not acknowledging limitations
- Weak connection to literature

## Integration with Dissertation

### Workflow
```
1. Write rough draft (don't self-edit yet)
2. Use @academic-grammar for first cleanup
3. Address all grammar/style issues
4. Get advisor feedback
5. Use @academic-grammar again post-revision
6. Final proofread before submission
```

### Target Metrics
- **Passive voice:** <20%
- **Average sentence length:** 15-25 words
- **Readability:** Grade 12-16 (academic audience)
- **Paragraph length:** 4-8 sentences

## Related Skills

- `@contribution-writer` - Articulate contributions clearly
- `@limitation-writer` - Write limitations section
- `@abstract-writer` - Polish abstract
- `/quality-check` - Overall quality assurance

## Software Integration

### Grammarly
- Catches basic grammar
- Suggests improvements
- Plagiarism check (premium)

**Limitation:** Not discipline-specific

### Hemingway Editor
- Readability score
- Highlights complex sentences
- Identifies passive voice

**Limitation:** Sometimes overly simplistic

### LaTeX Spellcheck
```bash
aspell -t -c chapter1.tex
```

### VS Code / Overleaf
- Built-in spell check
- Grammar extensions available

## Field-Specific Notes

### STEM Fields
- Precision critical (exact terms)
- Passive voice more common in Methods
- Figures/tables heavily integrated

### Social Sciences
- Active voice strongly preferred
- Theoretical framing important
- Qualitative data integration

### Humanities
- Longer, more complex sentences acceptable
- Rhetorical style varies by subfield
- Citation density high

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 30-60 minutes per chapter
**Time saved:** ~3 hours per chapter
**Reusability:** Very High (every draft, every chapter)
**Critical for:** All chapters, especially final revision
