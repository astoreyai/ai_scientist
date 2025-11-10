# Tutorial 4: Mastering AI-Check for Academic Writing

**Duration**: 30 minutes  
**Prerequisites**: Tutorial 1 completed, basic understanding of academic writing  
**What you'll learn**: AI-detection methods, interpreting results, improving flagged text, pre-commit hooks

---

## Overview

The AI-check system is the centerpiece of the Research Assistant plugin. This tutorial teaches you how to:

1. Understand the 5 detection methods (v1.0) + 4 enhanced methods (v1.1)
2. Run AI-check standalone
3. Interpret results correctly
4. Apply suggestions to improve writing
5. Use pre-commit hooks
6. Track improvements over time
7. Build a personalized writing profile

---

## Part 1: Understanding Detection Methods

### Original Methods (v1.0)

**1. Grammar Perfection Detection**
- AI rarely makes grammatical errors
- Humans make natural mistakes
- Flags: Perfect grammar, no typos, no awkward phrasing

**2. Sentence Uniformity Detection**
- AI favors 15-25 word sentences
- Humans vary more naturally
- Flags: 80%+ sentences in 15-25 word range

**3. Paragraph Structure Detection**
- AI tends toward 4-6 sentence paragraphs
- Mechanical structure (intro, 2-3 support, conclusion)
- Flags: Excessive structural uniformity

**4. AI-Word Frequency Detection**
- AI overuses certain words: "delve", "leverage", "robust"
- Also transition words: "furthermore", "moreover"
- Flags: >3 AI-words per 1000 words

**5. Punctuation Pattern Detection**
- AI uses perfect punctuation (semicolons, colons, em-dashes)
- Humans more inconsistent
- Flags: Suspiciously perfect punctuation

### Enhanced Methods (v1.1)

**6. N-Gram Language Modeling**
- Analyzes bigram and trigram probabilities
- Detects statistical anomalies in word transitions
- Flags: Unusual word sequences, repetitive phrases

**7. Sentence Complexity Analysis**
- Calculates Flesch-Kincaid, Gunning-Fog readability scores
- Measures complexity variance across sentences
- Flags: Excessive uniformity in complexity (AI-typical)

**8. Citation Pattern Analysis**
- Detects AI citation patterns:
  - Front-loading (more citations in first 1/3 of text)
  - Generic frames ("as noted by", "according to")
  - Citation clustering
- Flags: Non-human citation distribution

**9. Adaptive Thresholding**
- Builds personalized baseline from your writing
- Adjusts thresholds to your individual style
- Reduces false positives over time

---

## Part 2: Running AI-Check

### Method 1: Standalone Command

**Create a test file** with obviously AI-generated text:

```bash
cat > manuscript_draft.txt << 'DRAFT'
Furthermore, this comprehensive study leverages robust methodologies to delve 
into the intricate relationship between cognitive behavioral therapy and anxiety 
reduction. Moreover, the analysis demonstrates significant findings that utilize 
state-of-the-art statistical techniques. Additionally, these results facilitate 
our understanding of this important therapeutic intervention. The research 
methodology employed in this investigation is particularly noteworthy, as it 
incorporates multiple validated assessment instruments.
DRAFT
```

**Run AI-check**:

```bash
python tools/ai_check.py manuscript_draft.txt
```

**Expected Output**:

```
═══════════════════════════════════════════════════════════════
                    AI-CHECK REPORT
═══════════════════════════════════════════════════════════════

File: manuscript_draft.txt
Analyzed: 2025-11-10 14:30:22
Total Words: 73
Total Sentences: 4

───────────────────────────────────────────────────────────────
OVERALL ASSESSMENT
───────────────────────────────────────────────────────────────

Confidence: 82% (HIGH) 🚫
Verdict: LIKELY AI-GENERATED

This text exhibits multiple AI-typical patterns and should be 
revised before submission.

───────────────────────────────────────────────────────────────
DETECTION BREAKDOWN
───────────────────────────────────────────────────────────────

Grammar Perfection:        95% ⚠️
Sentence Uniformity:       88% ⚠️
Paragraph Structure:       75% ⚠️
AI-Word Frequency:         92% 🚫
Punctuation Patterns:      70% ⚠️

Language Model:            78% 🚫
  ├─ Bigram anomalies:     65%
  ├─ Trigram anomalies:    72%
  ├─ Transition score:     85%
  └─ Repetition score:     68%

Complexity Analysis:       81% 🚫
  ├─ Flesch-Kincaid:       12.4 (college level)
  ├─ Gunning-Fog:          12.6 (college level)
  ├─ Uniformity score:     89%
  └─ Complexity variance:  1.8 (very low)

Citation Patterns:         N/A (no citations found)

───────────────────────────────────────────────────────────────
ISSUES DETECTED
───────────────────────────────────────────────────────────────

❌ CRITICAL ISSUES (must fix):

1. Excessive AI-typical words (12 instances):
   • "Furthermore" (1)
   • "comprehensive" (1)
   • "leverages" (1)
   • "robust" (1)
   • "delve" (1)
   • "Moreover" (1)
   • "utilize" (1)
   • "Additionally" (1)
   • "facilitate" (1)
   • "particularly noteworthy" (1)
   • "incorporates" (1)
   • "validated" (1)

   AI words per 1000: 164.4 (threshold: 3.0)

2. Extreme sentence uniformity:
   All sentences are 17-19 words (AI sweet spot: 15-25)

3. Very low complexity variance (1.8):
   Human writing typically shows variance of 3-8

⚠️  WARNINGS:

4. Perfect grammar throughout (no natural errors)

5. Mechanical paragraph structure (4 sentences, uniform pattern)

6. Repetitive phrase patterns:
   • "this [adjective] study" (appears 2x)
   • "the [verb]" constructions (appears 5x)

───────────────────────────────────────────────────────────────
SUGGESTIONS FOR IMPROVEMENT
───────────────────────────────────────────────────────────────

✏️  WORD REPLACEMENTS:

Replace AI-typical words with natural alternatives:

Line 1: "Furthermore" → Delete or use "First" / "To begin"
Line 1: "comprehensive" → "complete" / "thorough" / delete
Line 1: "leverages" → "uses" / "applies"
Line 1: "robust" → "strong" / "reliable"
Line 1: "delve into" → "examine" / "investigate" / "explore"
Line 2: "Moreover" → Delete or use "Second" / "Also"
Line 2: "utilize" → "use"
Line 3: "Additionally" → Delete or combine with previous sentence
Line 3: "facilitate" → "help" / "improve" / "enable"

✏️  SENTENCE STRUCTURE:

Vary sentence length:
- Current: All 17-19 words
- Target: Mix of short (5-10), medium (12-18), long (20-30)

Example revision:
"This study examines CBT for anxiety reduction. [8 words]
We used validated assessment instruments and advanced 
statistical techniques. [10 words]
Our analysis shows significant therapeutic benefits. [7 words]"

✏️  COMPLEXITY:

Introduce natural complexity variation:
- Some simple, direct sentences
- Some complex sentences with subclauses
- Avoid mechanical uniformity

Example revision:
"CBT shows promise for anxiety treatment. [6 words - simple]
While previous studies focused on adults, our investigation 
examined adolescents aged 12-18 using multiple validated 
measures. [18 words - complex]
Results were significant. [3 words - very simple]"

───────────────────────────────────────────────────────────────
RECOMMENDED NEXT STEPS
───────────────────────────────────────────────────────────────

1. Apply word replacements (removes ~50 AI confidence points)
2. Vary sentence lengths (removes ~20 points)
3. Re-run ai-check to verify improvements
4. Build writing profile by committing authentic work

───────────────────────────────────────────────────────────────

Legend: 🚫 Critical (>70%)  |  ⚠️ Warning (30-70%)  |  ✅ Good (<30%)
```

---

## Part 3: Before/After Example

### BEFORE (AI-Generated - 82% Confidence)

```
Furthermore, this comprehensive study leverages robust methodologies to delve 
into the intricate relationship between cognitive behavioral therapy and anxiety 
reduction. Moreover, the analysis demonstrates significant findings that utilize 
state-of-the-art statistical techniques. Additionally, these results facilitate 
our understanding of this important therapeutic intervention.
```

**Problems**:
- 9 AI-typical words
- All sentences 17-19 words
- Perfect grammar
- Mechanical transitions (Furthermore, Moreover, Additionally)
- Complexity variance: 1.8

### AFTER (Human-Revised - 18% Confidence)

```
We examined CBT for anxiety treatment in adolescents. The study used three 
validated assessment tools: the GAD-7, SCARED, and RCMAS. Statistical analysis 
showed significant improvements in the CBT group compared to waitlist control 
(d = 0.68, p < .001). These findings add to evidence supporting CBT as an 
effective intervention, though long-term outcomes need further study.
```

**Improvements**:
- 0 AI-typical words
- Varied sentence lengths: 8, 17, 21, 19 words
- Some minor imperfections (natural)
- Natural flow without forced transitions
- Complexity variance: 6.2

**Result**: AI-check confidence dropped from 82% → 18%

---

## Part 4: Using Pre-Commit Hooks

The AI-check can automatically run before each git commit.

### Setup

**1. Check hook is enabled**:

```bash
cat .claude/settings.json | grep -A 5 gitPreCommit
```

Should show:
```json
"gitPreCommit": {
  "command": "python3 hooks/pre-commit-ai-check.py",
  "enabled": true,
  "description": "Check for AI-generated text patterns before commit"
}
```

**2. Configure thresholds** in `.ai-check-config.yaml`:

```yaml
pre_commit:
  enabled: true
  block_threshold: 0.70   # Block commits >= 70% confidence
  warn_threshold: 0.30    # Warn for >= 30% confidence
  
  # Which files to check
  file_patterns:
    - "*.tex"
    - "*.md"
    - "*.txt"
    - "*.rst"
  
  # Which to ignore
  exclude_patterns:
    - "node_modules/**"
    - "*.min.*"
    - ".git/**"
```

### Testing the Hook

**1. Create AI-generated file**:

```bash
echo "This comprehensive study leverages robust methodologies." > test.md
```

**2. Try to commit**:

```bash
git add test.md
git commit -m "Add methodology section"
```

**Expected**: Hook blocks commit

```
🚫 AI-GENERATED TEXT DETECTED

The following files exceeded AI confidence threshold (70%):

  test.md: 85% confidence

Detected issues:
  • Excessive AI-typical words (3 instances)
  • Mechanical sentence structure
  • Perfect grammar without natural variation

RECOMMENDATION:
Revise flagged sections before committing. Run 'python tools/ai_check.py test.md' 
for detailed suggestions.

To bypass this check (NOT RECOMMENDED):
git commit --no-verify -m "message"

Commit BLOCKED. Please revise and try again.
```

**3. Revise the file**:

```bash
echo "We used rigorous research methods for this study." > test.md
```

**4. Try again**:

```bash
git add test.md
git commit -m "Add methodology section"
```

**Expected**: Hook allows commit (or warns if 30-70%)

```
✅ AI-check passed (confidence: 22%)

[main abc1234] Add methodology section
 1 file changed, 1 insertion(+)
```

---

## Part 5: Building Your Writing Profile (v1.1 Feature)

The enhanced AI-check can build a personalized profile of YOUR writing style, reducing false positives.

### How It Works

1. **Initial Phase** (First 10 commits):
   - AI-check uses default thresholds
   - Saves metrics from each commit to `~/.claude/ai-check-profile.json`
   
2. **Learning Phase** (Commits 11-30):
   - Builds baseline metrics:
     - Your average complexity variance
     - Your typical sentence length distribution
     - Your natural word choices
   
3. **Adaptive Phase** (Commit 30+):
   - Personalizes thresholds to YOUR style
   - Reduces false positives significantly

### Example Profile

After 30 commits of authentic writing, your profile might look like:

```json
{
  "samples": 30,
  "avg_complexity_variance": 6.8,
  "avg_sentence_length": 16.2,
  "sentence_length_std_dev": 5.4,
  "common_words": {
    "however": 15,
    "therefore": 12,
    "although": 10
  },
  "ai_word_baseline": 0.8,
  "created": "2025-11-10",
  "last_updated": "2025-12-05"
}
```

**Personalized Thresholds**:
- Default block threshold: 70%
- YOUR adjusted threshold: 75% (allows 5% more variance)
- Reduces false positive rate from 15% → 3%

### Viewing Your Profile

```bash
python tools/ai_check.py --show-profile
```

Output:
```
═══════════════════════════════════════════════════════════════
                   YOUR WRITING PROFILE
═══════════════════════════════════════════════════════════════

Samples analyzed: 30 commits
Profile created: 2025-11-10
Last updated: 2025-12-05

Your Baseline Metrics:
  Complexity variance:     6.8 (human range: 3-8)
  Sentence length (avg):   16.2 words
  Sentence length (std):   5.4 words
  AI-word frequency:       0.8 per 1000 words

Personalized Thresholds:
  Block threshold:  75% (default: 70%)
  Warn threshold:   35% (default: 30%)

Profile Status: ✅ ACTIVE (30+ samples)
Estimated false positive rate: 3% (vs 15% default)
```

---

## Part 6: Advanced Configuration

### Customize Detection Weights

Edit `.ai-check-config.yaml` to adjust detection method weights:

```yaml
detection:
  # Weight each detection method (must sum to 1.0)
  weights:
    grammar_perfection: 0.15      # Less weight (can vary naturally)
    sentence_uniformity: 0.20     # Moderate weight
    paragraph_structure: 0.15     # Less weight (field-dependent)
    ai_word_frequency: 0.30       # High weight (strong signal)
    punctuation_patterns: 0.05    # Low weight (can vary)
    language_model: 0.10          # Moderate weight
    complexity: 0.15              # Moderate weight
    citations: 0.05               # Low weight (not always applicable)
  
  # AI-word thresholds
  ai_words_per_1000_threshold: 3.0
  
  # Complexity thresholds
  low_variance_threshold: 2.0
  ideal_variance_range: [3.0, 8.0]
```

### Domain-Specific Profiles

Create field-specific AI-word lists:

```yaml
ai_words:
  # Universal AI words
  universal:
    high_risk: ["delve", "leverage", "utilize"]
    medium_risk: ["robust", "comprehensive"]
  
  # STEM-specific (these might be legitimate in STEM writing)
  stem:
    high_risk: ["delve"]  # Still suspicious
    medium_risk: []       # "robust" is acceptable in STEM
  
  # Humanities-specific
  humanities:
    high_risk: ["delve", "leverage", "utilize", "robust"]
    medium_risk: ["comprehensive", "facilitate"]
```

---

## Part 7: Troubleshooting

### False Positives

**Problem**: Your authentic writing is flagged as AI

**Solutions**:

1. **Build a profile**: Commit 30+ authentic documents to train adaptive thresholds

2. **Adjust weights**: If you naturally use "robust" in STEM writing, reduce ai_word weight

3. **Check specific methods**: Run with `--verbose` to see which methods trigger

```bash
python tools/ai_check.py --verbose manuscript.tex
```

4. **Document your style**: Add `--update-profile` flag to save as authentic

```bash
python tools/ai_check.py --update-profile manuscript.tex
```

### False Negatives

**Problem**: AI-generated text passes detection

**Solutions**:

1. **Lower thresholds**: Change block_threshold from 0.70 → 0.60

2. **Enable enhanced detection**: Ensure v1.1 methods are active

3. **Report the miss**: Help improve detection by reporting false negatives

---

## Part 8: Best Practices

### DO:

✅ Run AI-check on all manuscript drafts before sharing  
✅ Build your writing profile with authentic work  
✅ Apply suggested improvements iteratively  
✅ Use pre-commit hooks for automatic checking  
✅ Review flagged sections carefully (AI-check isn't perfect)

### DON'T:

❌ Bypass the hook with `--no-verify` unless absolutely necessary  
❌ Ignore warnings (30-70% confidence still needs review)  
❌ Submit flagged text to journals without revision  
❌ Use AI-check as the sole authenticity measure  
❌ Forget that AI-check is a tool, not a judge

---

## Part 9: Integration with Research Workflow

### PhD Dissertation Use Case

**Setup**:
1. Enable pre-commit hook
2. Set conservative thresholds (block: 60%, warn: 25%)
3. Run on all chapter drafts before advisor review

**Workflow**:
```bash
# Draft chapter
vim chapters/chapter_03_methods.tex

# Check before committing
python tools/ai_check.py chapters/chapter_03_methods.tex

# Apply suggestions, iterate

# Commit when clean
git add chapters/chapter_03_methods.tex
git commit -m "Complete methods chapter"
# Hook runs automatically, blocks if issues found

# Track progress
python tools/ai_check.py --show-history
```

### Journal Submission Use Case

**Pre-submission checklist**:
1. Run AI-check on final manuscript
2. Ensure all sections < 30% confidence
3. Generate AI-check report for records
4. Include in submission materials (optional)

```bash
# Generate formal report
python tools/ai_check.py manuscript.tex --format=pdf --output=ai-check-report.pdf

# Archive for records
cp ai-check-report.pdf submission_records/
```

---

## Summary

You've mastered the AI-check system! You can now:

✅ Understand all 9 detection methods  
✅ Run standalone AI-checks  
✅ Interpret complex results  
✅ Apply suggestions effectively  
✅ Use pre-commit hooks  
✅ Build personalized writing profiles  
✅ Configure advanced settings  
✅ Integrate into your research workflow

**Next Tutorial**: [Complete Workflow](../05_complete_workflow/README.md) - Put everything together

---

## Quick Reference Card

```bash
# Basic usage
python tools/ai_check.py file.tex

# With profile update (mark as authentic)
python tools/ai_check.py --update-profile file.tex

# Verbose output
python tools/ai_check.py --verbose file.tex

# Show your writing profile
python tools/ai_check.py --show-profile

# Show improvement history
python tools/ai_check.py --show-history

# Generate PDF report
python tools/ai_check.py file.tex --format=pdf

# Check multiple files
python tools/ai_check.py chapter_*.tex
```

**Configuration Files**:
- `.ai-check-config.yaml` - Detection settings
- `~/.claude/ai-check-profile.json` - Your writing profile
- `.claude/hooks/pre-commit-ai-check.py` - Pre-commit hook

**Key Metrics**:
- < 30%: Likely human ✅
- 30-70%: Possible AI ⚠️
- > 70%: Likely AI 🚫

---

*Tutorial created: 2025-11-10*  
*Version: 1.1.0*  
*Enhanced detection methods included*
