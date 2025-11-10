# User Guide - Research Assistant Plugin

Comprehensive guide to using the Research Assistant plugin for academic research workflows.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Using Agents](#using-agents)
3. [Using Skills](#using-skills)
4. [AI-Check System](#ai-check-system)
5. [Research Workflows](#research-workflows)
6. [Best Practices](#best-practices)

---

## Getting Started

### First Steps

After installation, familiarize yourself with available components:

```bash
# See all available agents
/agent list

# See all available skills
/skill list

# View current configuration
cat .claude/settings.json
```

### Your First Research Task

Let's start a systematic literature review:

```
/agent literature-reviewer

I need to conduct a systematic review on mindfulness interventions for anxiety in adolescents. 
Please help me develop a search strategy following PRISMA 2020 guidelines.
```

The agent will guide you through:
1. Defining inclusion/exclusion criteria
2. Developing search strings
3. Selecting databases
4. Planning screening workflow

---

## Using Agents

### Available Agents

| Agent | When to Use | Example Command |
|-------|-------------|-----------------|
| literature-reviewer | Systematic reviews | `/agent literature-reviewer` |
| experiment-designer | Study design | `/agent experiment-designer` |
| data-analyst | Statistical analysis | `/agent data-analyst` |
| hypothesis-generator | Generate hypotheses | `/agent hypothesis-generator` |
| manuscript-writer | Write papers | `/agent manuscript-writer` |
| citation-manager | Manage references | `/agent citation-manager` |
| gap-analyst | Find research gaps | `/agent gap-analyst` |
| quality-assurance | QA validation | `/agent quality-assurance` |
| meta-reviewer | Review work | `/agent meta-reviewer` |
| code-reviewer | Review code | `/agent code-reviewer` |

### Example: Literature Review Workflow

**Step 1: Start the agent**
```
/agent literature-reviewer
```

**Step 2: Define your review**
```
Research Question: Does mindfulness-based stress reduction (MBSR) reduce anxiety in adolescents?

Population: Adolescents aged 12-18
Intervention: MBSR programs
Comparison: Waitlist control or active control
Outcome: Anxiety scores (standardized measures)
Study Design: RCTs only
```

**Step 3: Search strategy**
The agent helps develop search strings:
```
Database: PubMed
Search String: (mindfulness OR "mindfulness-based stress reduction" OR MBSR) 
AND (anxiety OR "anxiety disorder") 
AND (adolescent* OR teen* OR youth)
AND ("randomized controlled trial" OR RCT)
```

**Step 4: Screening**
Agent guides through title/abstract and full-text screening with PRISMA documentation.

**Step 5: Data extraction**
Agent provides structured extraction templates for study characteristics, outcomes, and risk of bias.

### Example: Experimental Design

```
/agent experiment-designer

I need to design an RCT comparing CBT to usual care for depression in adults. 
Need help with power analysis, randomization, and protocol development.
```

Agent provides:
- Power analysis calculations
- Randomization procedures
- Blinding strategies
- Timeline development
- Pre-registration template

---

## Using Skills

Skills are invoked naturally during conversation or explicitly requested.

### AI-Check Skill

**Manual invocation:**
```
Please run ai-check on docs/manuscript/discussion.tex and provide detailed feedback.
```

**Automatic via pre-commit:**
```bash
git add manuscript.tex
git commit -m "Add discussion section"
# AI-check runs automatically
```

**Output:**
```
Overall Confidence: 65% (MEDIUM)

Issues Detected:
- 8 AI-typical words found: "delve", "leverage", "robust"
- Sentence uniformity score: 72%
- AI words per 1000: 4.2 (baseline: 1.5)

Suggestions:
1. Replace "delve" with "examine" or "explore"
2. Vary sentence lengths (currently 15-20 words consistently)
3. Remove excessive transition words ("furthermore", "moreover")
```

### Citation-Format Skill

**Example:**
```
Please convert these citations to APA 7th edition:

Smith, J., Jones, M. (2023). Deep learning. AI Journal, 15(2), 123-145.
```

**Output:**
```
APA 7th Edition:

Smith, J., & Jones, M. (2023). Deep learning. AI Journal, 15(2), 123-145. https://doi.org/10.xxxx/yyyy
```

### Power-Analysis Skill

**Example:**
```
I need to calculate required sample size for an independent samples t-test.
Expected effect size: d = 0.5 (medium)
Alpha: 0.05
Power: 0.80
```

**Output:**
```
Sample Size Calculation:
- Design: Independent samples t-test (two-tailed)
- Effect size: d = 0.50
- Alpha: 0.05
- Power: 0.80
- Required N: 64 per group (128 total)

With 20% anticipated attrition:
- Recruit: 160 participants (80 per group)

Sensitivity Analysis:
- Power to detect d = 0.40: 55%
- Power to detect d = 0.60: 95%
```

### Effect-Size Skill

**Example:**
```
Calculate Cohen's d for these results:
Group 1: M = 45.2, SD = 8.3, N = 50
Group 2: M = 37.8, SD = 9.1, N = 50
```

**Output:**
```
Cohen's d = 0.85 (Large effect)
95% CI: [0.43, 1.27]

Interpretation:
The intervention group scored 0.85 standard deviations higher than control, 
representing a large and practically meaningful effect.
```

### PRISMA-Diagram Skill

**Example:**
```
Generate a PRISMA flow diagram with these counts:

Identification:
- Database records: 1,250
- Other sources: 15
- Duplicates removed: 320

Screening:
- Records screened: 945
- Records excluded: 820

Eligibility:
- Full-text assessed: 125
- Full-text excluded: 98 (reasons: wrong outcome: 45, wrong population: 30, not RCT: 23)

Included:
- Studies included: 27
```

**Output:** Properly formatted PRISMA 2020 flow diagram in markdown.

---

## AI-Check System

### Understanding Confidence Scores

**0-30% (Low): Appears Human** ✅
- Natural variation in writing
- Authentic voice
- No action needed

**30-70% (Medium): Possible AI Assistance** ⚠️
- Some uniformity detected
- Review flagged sections
- Apply suggestions selectively

**70-100% (High): Likely AI-Generated** 🚫
- Excessive uniformity
- Multiple AI-typical words
- Significant revision needed

### AI-Typical Words to Avoid

**High-Risk Words** (rarely used by humans):
- "delve" → use "examine", "explore"
- "leverage" → use "use", "apply"
- "utilize" → use "use"

**Medium-Risk Words** (overused by AI):
- "robust" → use "strong", "reliable"
- "comprehensive" → use "complete", "thorough"
- "facilitate" → use "enable", "help"

**Transition Overuse:**
- "furthermore" → use "also", "next"
- "moreover" → use dash or simpler transitions
- "additionally" → often unnecessary

### Improving Flagged Text

**Original (78% confidence):**
```
Furthermore, this comprehensive study delves into the robust methodologies 
utilized to facilitate the implementation of innovative approaches. Moreover, 
the analysis demonstrates significant findings that leverage state-of-the-art 
techniques.
```

**Revised (18% confidence):**
```
We examined the methods used in this approach. The analysis shows clear 
improvements across metrics using current techniques. These findings suggest 
practical applications for future research.
```

**What Changed:**
- Removed all AI-typical words
- Simplified transitions
- Varied sentence lengths (6, 13, 10 words vs uniform 15-18)
- More direct, active voice

---

## Research Workflows

### Complete Dissertation Chapter Workflow

**1. Literature Review (PRISMA)**
```
/agent literature-reviewer
# Develop search strategy, screen studies, extract data
```

**2. Identify Gaps**
```
/agent gap-analyst
# Analyze synthesis matrix, identify knowledge gaps
```

**3. Generate Hypotheses**
```
/agent hypothesis-generator
# Develop testable hypotheses addressing gaps
```

**4. Design Study**
```
/agent experiment-designer
# Power analysis, randomization, protocol development
```

**5. Write Manuscript**
```
/agent manuscript-writer
# Draft following reporting guidelines (CONSORT, PRISMA)
```

**6. Quality Assurance**
```
/agent quality-assurance
# Validate reproducibility, check citations, run AI-check
```

### Grant Proposal Development

**1. Scientific Premise**
```
/agent literature-reviewer
# Demonstrate gap in knowledge
```

**2. Research Strategy**
```
/agent experiment-designer
# Rigorous design with NIH rigor standards
```

**3. Sample Size Justification**
```
Please calculate required sample size with power analysis for this RCT...
# Uses power-analysis skill
```

**4. Statistical Analysis Plan**
```
Please help develop a detailed statistical analysis plan...
# Uses hypothesis-test and data-analyst skills
```

**5. References**
```
Please format all references in NIH style...
# Uses citation-format skill
```

**6. Final Review**
```
/agent quality-assurance
# Comprehensive QA before submission
```

---

## Best Practices

### For PhD Students

**1. Start Each Chapter with Literature Review**
```
/agent literature-reviewer
# Systematic approach ensures comprehensive coverage
```

**2. Pre-Register Studies**
```
/agent experiment-designer
# Agent helps create pre-registration documents
```

**3. Check Writing Authenticity**
```
python tools/ai_check.py chapter_draft.tex
# Run before sending to advisor
```

**4. Track Everything**
```
# Git for code, DVC for data, MLflow for experiments
# Hooks automate tracking
```

### For Grant Writing

**1. Use Power Analysis Skill**
```
# Justify sample sizes with calculations
# Show sensitivity analyses
```

**2. Follow NIH Rigor Standards**
```
/agent experiment-designer
# Agent ensures all rigor elements addressed
```

**3. Validate All Citations**
```
/agent citation-manager
# Check for retractions, verify DOIs
```

### For Journal Submissions

**1. Check Reporting Guidelines**
```
/agent manuscript-writer
# CONSORT for RCTs, PRISMA for reviews, STROBE for observational
```

**2. Run Complete QA**
```
/agent quality-assurance
# Reproducibility, citations, statistics, AI-check
```

**3. Format Citations Correctly**
```
Please convert all references to APA 7th edition...
```

---

## Tips and Tricks

### Efficient Agent Use

**Chain agents together:**
```
/agent literature-reviewer
# After completion:
/agent gap-analyst
# Then:
/agent hypothesis-generator
```

**Save agent outputs:**
- Agents generate markdown files automatically
- Stored in `.claude/agent-outputs/`
- Version control these with git

### Skill Combinations

**Comprehensive power analysis:**
```
1. Calculate sample size (power-analysis skill)
2. Calculate expected effect size (effect-size skill)
3. Plan statistical tests (hypothesis-test skill)
4. All feed into pre-registration
```

### AI-Check Workflow

**During writing:**
1. Draft section naturally
2. Run AI-check
3. Review suggestions
4. Revise
5. Re-check until <30% confidence
6. Commit with confidence

**Track progress:**
```bash
python tools/ai_check.py manuscript.tex --track
# Builds history database
# See improvements over time
```

---

## Troubleshooting

### Agent Not Responding as Expected

**Issue:** Agent gives generic responses

**Solution:** Be more specific in your request:

❌ "Help with my research"
✅ "I need to conduct a PRISMA 2020 systematic review on [specific topic]. Help me develop a search strategy for PubMed, Embase, and PsycINFO targeting [specific population, intervention, outcome]."

### AI-Check False Positives

**Issue:** Human writing flagged as AI

**Solution:**
- Check if writing is overly formal
- Review specific patterns flagged
- Adjust thresholds in `.ai-check-config.yaml`
- Document authentic writing process for committee

### Skill Not Working

**Issue:** Skill not being invoked

**Solution:**
- Use explicit language: "Please use the power-analysis skill to..."
- Check skill is enabled: `/skill list`
- Restart Claude Code if needed

---

## Support Resources

- **Documentation:** `docs/` directory
- **Agent Reference:** `docs/AGENT_REFERENCE.md`
- **Skill Reference:** `docs/SKILL_REFERENCE.md`
- **Issues:** https://github.com/astoreyai/ai_scientist/issues
- **Email:** aaron@astoreyai.com

---

*User guide last updated: 2025-11-09*
