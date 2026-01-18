# Agent Reference - Research Assistant Plugin

Complete reference for all 10 specialized research agents.

---

## Agent Overview

| Agent | Primary Use | Model | Tools |
|-------|-------------|-------|-------|
| literature-reviewer | Systematic reviews (PRISMA 2020) | Opus | Read, Write, Grep, Glob, Bash, WebFetch |
| experiment-designer | Experimental design (NIH rigor) | Sonnet | Read, Write, Bash, Edit |
| data-analyst | Statistical analysis | Sonnet | Read, Write, Bash, Edit |
| hypothesis-generator | Hypothesis generation | Sonnet | Read, Write |
| manuscript-writer | Academic writing | Sonnet | Read, Write, Edit |
| citation-manager | Reference management | Haiku | Read, Write |
| gap-analyst | Literature gap identification | Sonnet | Read, Write, Edit |
| quality-assurance | QA validation | Sonnet | Read, Write, Bash, Edit |
| meta-reviewer | Cross-phase synthesis | Sonnet | Read, Write, Edit |
| code-reviewer | Code quality review | Sonnet | Read, Write, Bash, Edit |

---

## 1. literature-reviewer

**Purpose:** Conduct PRISMA 2020 compliant systematic literature reviews.

**Invoke:** `/agent literature-reviewer`

**Capabilities:**
- Multi-database literature search (OpenAlex, arXiv, PubMed)
- PRISMA 2020 workflow (identification, screening, eligibility)
- Title/abstract and full-text screening
- Structured data extraction
- Inter-rater reliability tracking
- Risk of bias assessment
- PRISMA flow diagram generation

**When to Use:**
- Starting a systematic review
- Conducting meta-analysis
- Comprehensive literature synthesis
- Dissertation literature chapter
- Grant proposal background

**Example:**
```
/agent literature-reviewer

Research question: Does cognitive behavioral therapy reduce depression in adults compared to usual care?

Population: Adults (18+) with major depressive disorder
Intervention: Cognitive behavioral therapy (CBT)
Comparison: Usual care, waitlist, or attention control
Outcome: Depression scores (validated measures)
Design: RCTs only
```

**Outputs:**
- Search strategy documentation
- PRISMA flow diagram data
- Screening decisions log
- Extracted data tables
- Risk of bias assessments
- Synthesis matrices

---

## 2. experiment-designer

**Purpose:** Design rigorous experiments following NIH rigor standards.

**Invoke:** `/agent experiment-designer`

**Capabilities:**
- Power analysis and sample size calculation
- Randomization protocol development
- Blinding procedures
- Control group selection
- Variable operationalization
- Timeline and resource planning
- Pre-registration document creation
- NIH rigor compliance checking

**When to Use:**
- Planning new studies
- Grant proposal development
- Pre-registration
- Dissertation study design
- IRB protocol development

**Example:**
```
/agent experiment-designer

I need to design an RCT testing a mindfulness intervention for anxiety in college students.

Requirements:
- Adequate power (80%)
- Proper randomization
- Appropriate control group
- Pre-registration ready
- Budget: $50,000
- Timeline: 12 months
```

**Outputs:**
- Complete experimental protocol
- Power analysis with justification
- Randomization procedure (with seed)
- Timeline and milestones
- Budget allocation
- Pre-registration document
- IRB application materials

---

## 3. data-analyst

**Purpose:** Perform reproducible statistical analyses.

**Invoke:** `/agent data-analyst`

**Capabilities:**
- Assumption testing (normality, homogeneity)
- Effect size calculation with confidence intervals
- Primary and secondary outcome analysis
- Sensitivity analyses
- Multiple comparison corrections
- Missing data handling
- Reproducibility validation

**When to Use:**
- Analyzing collected data
- Results chapter writing
- Responding to reviewer comments
- Sensitivity analyses
- Statistical consultation needed

**Example:**
```
/agent data-analyst

I have data from an RCT (N=120, 60 per group) comparing intervention to control on anxiety scores (GAD-7).

Data: anxiety_data.csv
Columns: participant_id, group (intervention/control), pre_score, post_score, age, sex

Analysis needed:
- Check assumptions
- Primary analysis (group difference in post scores, controlling for pre)
- Effect size with 95% CI
- Sensitivity analysis excluding outliers
```

**Outputs:**
- Assumption test results
- Primary analysis with effect sizes
- Formatted results tables
- Statistical reporting text
- R or Python analysis scripts
- Reproducibility documentation

---

## 4. hypothesis-generator

**Purpose:** Generate testable research hypotheses using Tree-of-Thought reasoning.

**Invoke:** `/agent hypothesis-generator`

**Capabilities:**
- Tree-of-Thought hypothesis generation
- Falsifiability checking
- Testability assessment
- Novelty evaluation
- Hypothesis refinement
- Variable operationalization

**When to Use:**
- Formulating research questions
- Generating multiple hypothesis candidates
- Refining vague ideas
- Grant proposal development
- Dissertation planning

**Example:**
```
/agent hypothesis-generator

Research area: The relationship between social media use and mental health in adolescents.

Literature suggests correlation but mechanisms unclear. Generate 5 testable hypotheses about potential mediating or moderating factors.
```

**Outputs:**
- 5+ hypothesis candidates
- Falsifiability assessment for each
- Testability ratings
- Recommended approach for each
- Ranked by feasibility and novelty

---

## 5. manuscript-writer

**Purpose:** Write reporting guideline-compliant manuscripts.

**Invoke:** `/agent manuscript-writer`

**Capabilities:**
- CONSORT-compliant RCT manuscripts
- PRISMA-compliant systematic reviews
- STROBE-compliant observational studies
- APA-style formatting
- Section-by-section drafting
- AI-check integration (automatic)
- Reference management

**When to Use:**
- Writing journal articles
- Dissertation chapters
- Conference papers
- Grant proposals
- Research reports

**Example:**
```
/agent manuscript-writer

I need to write an RCT manuscript for submission to JAMA Psychiatry.

Study: RCT of CBT vs usual care for depression (N=200)
Results: CBT group improved significantly (d=0.65, p<.001)
Follow-up: 6 months
Format: CONSORT checklist compliance required
```

**Outputs:**
- Complete manuscript draft
- Structured abstract
- CONSORT checklist completed
- Figure and table shells
- Reference list (formatted)
- Cover letter draft
- AI-check reports for each section

---

## 6. citation-manager

**Purpose:** Manage, verify, and format citations.

**Invoke:** `/agent citation-manager`

**Capabilities:**
- Citation verification via Crossref
- Retraction checking
- BibTeX management and cleaning
- Citation formatting (multiple styles)
- Duplicate detection
- Reference completeness checking

**When to Use:**
- Managing large bibliographies
- Checking for retractions
- Formatting references
- Cleaning BibTeX files
- Pre-submission verification

**Example:**
```
/agent citation-manager

I have a BibTeX file with 200 references. Please:
1. Check all DOIs are valid
2. Check for any retractions
3. Remove duplicates
4. Format consistently
5. Identify any incomplete entries
```

**Outputs:**
- Cleaned BibTeX file
- Verification report
- Retraction alerts (if any)
- Duplicate removal log
- Incomplete entry list

---

## 7. gap-analyst

**Purpose:** Identify research gaps from literature synthesis.

**Invoke:** `/agent gap-analyst`

**Capabilities:**
- Pattern identification across studies
- Knowledge gap identification
- Methodological gap detection
- Theoretical gap analysis
- Gap prioritization by impact
- Research direction recommendations

**When to Use:**
- After completing literature review
- Grant proposal justification
- Dissertation proposal
- Research agenda development

**Example:**
```
/agent gap-analyst

I've completed a systematic review of 45 studies on exercise interventions for anxiety.

Synthesis matrix: synthesis_matrix.csv

Please identify:
1. What populations are understudied?
2. What methodological weaknesses exist?
3. What mechanisms remain unclear?
4. Which gaps should I prioritize for my dissertation?
```

**Outputs:**
- Comprehensive gap analysis
- Gap categories (knowledge, methodological, theoretical)
- Prioritized gap recommendations
- Justification for each gap
- Suggested research directions

---

## 8. quality-assurance

**Purpose:** Comprehensive quality validation of research artifacts.

**Invoke:** `/agent quality-assurance`

**Capabilities:**
- Reproducibility checking
- Citation verification
- Statistical validation
- AI-check integration
- Reporting guideline compliance
- Code review
- Data integrity checks

**When to Use:**
- Before manuscript submission
- Pre-defense review
- Grant proposal review
- After major revisions
- Periodic quality checks

**Example:**
```
/agent quality-assurance

Please perform comprehensive QA on my dissertation Chapter 4 (Results).

Files:
- manuscript/chapter_04_results.tex
- data/analysis_results.csv
- code/primary_analysis.R

Check:
- All results reproducible
- Statistics reported correctly
- All figures referenced
- No AI-generated text
- CONSORT compliance
```

**Outputs:**
- Comprehensive QA report
- Issues found with severity
- Reproducibility assessment
- AI-check results
- Compliance checklist
- Recommendations for fixes

---

## 9. meta-reviewer

**Purpose:** Cross-phase synthesis and comprehensive feedback.

**Invoke:** `/agent meta-reviewer`

**Capabilities:**
- Cross-chapter coherence checking
- Argument flow evaluation
- Gap and redundancy identification
- Overall narrative assessment
- Integration recommendations

**When to Use:**
- Reviewing complete dissertation
- Mid-project assessment
- Before defense
- Comprehensive manuscript review
- After major revisions

**Example:**
```
/agent meta-reviewer

Please review my complete dissertation for coherence and flow.

Chapters: 1 (intro), 2 (literature), 3 (methods), 4 (results), 5 (discussion)

Focus on:
- Do the research questions flow from literature?
- Do methods address research questions?
- Do results answer research questions?
- Does discussion integrate findings?
- Any contradictions across chapters?
```

**Outputs:**
- Cross-chapter coherence report
- Identified gaps or redundancies
- Flow and narrative assessment
- Integration recommendations
- Prioritized revision suggestions

---

## 10. code-reviewer

**Purpose:** Review research code for quality and reproducibility.

**Invoke:** `/agent code-reviewer`

**Capabilities:**
- Code quality assessment
- Security vulnerability detection
- Best practices checking
- Documentation review
- Reproducibility validation
- Statistical implementation verification

**When to Use:**
- Before sharing code
- Pre-submission review
- Reproducibility validation
- Collaboration preparation
- Code cleanup

**Example:**
```
/agent code-reviewer

Review my analysis scripts for reproducibility and quality.

Files:
- analysis/primary_analysis.R
- analysis/sensitivity_analysis.R
- analysis/figure_generation.R

Check for:
- Reproducibility (seeds, file paths)
- Code quality (readable, documented)
- Statistical correctness
- Security issues
- Best practices
```

**Outputs:**
- Code review report
- Issues by severity
- Best practice recommendations
- Reproducibility assessment
- Refactoring suggestions

---

## Agent Best Practices

### Invoking Agents

**Good:**
```
/agent literature-reviewer

I need to conduct a systematic review on [specific topic] following PRISMA 2020.
Population: [specific]
Intervention: [specific]
Comparison: [specific]
Outcome: [specific]
```

**Less Effective:**
```
Help me with literature
```

### Chaining Agents

Agents work well in sequence:
```
1. /agent literature-reviewer  # Complete review
2. /agent gap-analyst          # Identify gaps
3. /agent hypothesis-generator # Develop hypotheses  
4. /agent experiment-designer  # Design study
5. /agent manuscript-writer    # Write up
6. /agent quality-assurance    # Final QA
```

### Agent Outputs

- Agents generate structured outputs
- Save outputs for reference
- Version control agent-generated files
- Review and edit agent outputs

---

*Agent reference last updated: 2025-11-09*
