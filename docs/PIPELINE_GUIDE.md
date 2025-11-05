# PhD Pipeline Comprehensive Guide

**Complete instructions for using the autonomous dissertation pipeline**

---

## Table of Contents

1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Workflow System](#workflow-system)
4. [Template System](#template-system)
5. [Autonomous Agents](#autonomous-agents)
6. [Quality Assurance](#quality-assurance)
7. [LaTeX Compilation](#latex-compilation)
8. [Troubleshooting](#troubleshooting)
9. [Customization](#customization)
10. [Best Practices](#best-practices)

---

## Overview

### Pipeline Architecture

The pipeline follows a **phased approach** with clear deliverables:

```
Phase 1: Planning (Weeks 1-4)
  ├── Topic Development
  ├── Literature Review
  └── Research Framework

Phase 2: Methodology (Weeks 5-8)
  ├── Theoretical Foundation
  ├── Experimental Design
  └── Implementation Planning

Phase 3: Execution (Weeks 9-24)
  ├── Data Collection/Experiments
  ├── Implementation
  └── Analysis

Phase 4: Writing (Weeks 25-36)
  ├── Draft All Chapters
  ├── Revisions
  └── Integration

Phase 5: Finalization (Weeks 37-40)
  ├── LaTeX Conversion
  ├── Bibliography
  └── Defense Preparation
```

### Core Principles

1. **Work Sequentially**: Complete each phase before moving on
2. **Use Templates**: Don't start from scratch
3. **Track Progress**: Update todo lists daily
4. **Quality Check**: Use checklists at each milestone
5. **Be Honest**: Only claim what you can prove

---

## Setup Instructions

### Initial Setup

```bash
# 1. Navigate to your project directory
cd /path/to/your/dissertation/project

# 2. Copy the pipeline
cp -r PHD_PIPELINE .

# 3. Run setup script
cd PHD_PIPELINE
./automation/scripts/setup.sh
```

### What Setup Creates

```
MY_DISSERTATION/
├── config.yaml              # Your dissertation configuration
├── chapters/                # Markdown chapter files
│   ├── chapter_01_introduction.md
│   ├── chapter_02_literature_review.md
│   ├── chapter_03_theory.md
│   ├── chapter_04_methodology.md
│   ├── chapter_05_implementation.md
│   ├── chapter_06_results.md
│   ├── chapter_07_discussion.md
│   └── chapter_08_conclusion.md
├── latex/                   # LaTeX compilation files
│   ├── dissertation.tex
│   └── chapters/
├── bibliography/            # References
│   └── references.bib
├── figures/                 # Figures and diagrams
├── code/                    # Implementation code
├── data/                    # Datasets and results
└── progress/                # Progress tracking
    ├── todo.md
    └── timeline.md
```

### Configuration

Edit `MY_DISSERTATION/config.yaml`:

```yaml
# Dissertation Metadata
title: "Your Full Dissertation Title"
subtitle: "Optional Subtitle"
author: "Your Full Name"
email: "your.email@university.edu"

# Academic Information
degree: "Doctor of Philosophy (PhD)"
field: "Computer Science"  # Adjust for your field
university: "Your University Name"
department: "Department of Computer Science"
advisor: "Dr. Advisor Name"
committee:
  - "Dr. Committee Member 1"
  - "Dr. Committee Member 2"
  - "Dr. Committee Member 3"

# Research Information
topic_area: "Brief 1-2 sentence description of your research area"
keywords:
  - "Keyword 1"
  - "Keyword 2"
  - "Keyword 3"
  - "Keyword 4"
  - "Keyword 5"

# Timeline (adjust based on your needs)
timeline_months: 12
target_defense_date: "2026-10-01"

# Research Characteristics
research_type: "computational"  # computational | experimental | theoretical | mixed
datasets: "public"  # public | private | none
irb_required: false
industry_partners: false
```

---

## Workflow System

### Phase 1: Planning

#### 1.1 Topic Development (`workflows/01_topic_development.md`)

**Goal:** Define your research problem and contributions

**Tasks:**
1. Identify research gap
2. Formulate research questions (3-5)
3. List expected contributions (5-8)
4. Define success criteria

**Deliverable:** `planning/research_framework.md`

**Time:** 1-2 weeks

#### 1.2 Literature Review (`workflows/02_literature_review.md`)

**Goal:** Survey related work and position your research

**Tasks:**
1. Identify key papers (50-100)
2. Create literature matrix
3. Identify gaps your work addresses
4. Draft initial bibliography

**Deliverable:** `planning/literature_matrix.md`, `chapters/chapter_02_literature_review.md` (draft)

**Time:** 2-4 weeks

### Phase 2: Methodology

#### 2.1 Theoretical Foundation (`workflows/03_methodology.md`)

**Goal:** Establish theoretical basis for your work

**Tasks:**
1. Define core concepts
2. Present mathematical framework
3. Prove key theorems (if applicable)
4. Establish notation

**Deliverable:** `chapters/chapter_03_theory.md`

**Time:** 2-4 weeks

#### 2.2 Experimental Design (`workflows/03_methodology.md`)

**Goal:** Design experiments to validate your contributions

**Tasks:**
1. Select datasets/benchmarks
2. Define evaluation metrics
3. Choose baselines for comparison
4. Design ablation studies

**Deliverable:** `planning/experimental_protocol.md`, `chapters/chapter_04_methodology.md`

**Time:** 2-3 weeks

### Phase 3: Execution

#### 3.1 Implementation (`workflows/04_data_analysis.md`)

**Goal:** Build your system/algorithm

**Tasks:**
1. Implement core components
2. Write unit tests
3. Document code
4. Create usage examples

**Deliverable:** `code/` directory, `chapters/chapter_05_implementation.md`

**Time:** 8-16 weeks (varies widely)

#### 3.2 Experiments (`workflows/04_data_analysis.md`)

**Goal:** Run evaluations and collect results

**Tasks:**
1. Run experiments on all datasets
2. Compare against baselines
3. Perform ablation studies
4. Collect statistical significance

**Deliverable:** `data/results/`, figures, `chapters/chapter_06_results.md`

**Time:** 4-8 weeks

### Phase 4: Writing

#### 4.1 Chapter Drafting (`workflows/05_writing.md`)

**Goal:** Write all 8 chapters

**Tasks:**
1. Expand chapter outlines to full drafts
2. Create figures and tables
3. Write honest claims based on actual results
4. Cross-reference between chapters

**Deliverable:** All chapters completed (Markdown)

**Time:** 8-12 weeks

#### 4.2 Revision (`workflows/05_writing.md`)

**Goal:** Polish writing quality

**Tasks:**
1. Self-review all chapters
2. Check for consistency
3. Fix grammar/spelling
4. Verify all claims have evidence

**Deliverable:** Revised chapters

**Time:** 2-4 weeks

### Phase 5: Finalization

#### 5.1 LaTeX Conversion (`workflows/06_finalization.md`)

**Goal:** Convert to final PDF format

**Tasks:**
1. Convert Markdown to LaTeX
2. Format equations and algorithms
3. Insert figures/tables
4. Compile to PDF

**Deliverable:** `latex/dissertation.pdf`

**Time:** 2-3 weeks

#### 5.2 Bibliography (`workflows/06_finalization.md`)

**Goal:** Complete references

**Tasks:**
1. Convert all citations to BibTeX
2. Verify citation accuracy
3. Check formatting consistency

**Deliverable:** `bibliography/references.bib`

**Time:** 1 week

#### 5.3 Defense Preparation (`workflows/06_finalization.md`)

**Goal:** Prepare for defense

**Tasks:**
1. Create presentation slides
2. Prepare answers to anticipated questions
3. Practice talk
4. Submit dissertation to committee

**Deliverable:** Defense presentation, final PDF

**Time:** 2-3 weeks

---

## Template System

### Chapter Templates

All templates are in `templates/dissertation/` with the following structure:

```markdown
# Chapter [N]: [Title]

## Overview
[Brief chapter summary - 2-3 sentences]

## Key Contributions
- Contribution 1
- Contribution 2
- ...

## Chapter Outline

### [Section 1]
[Placeholder text with guidance on what to write]

### [Section 2]
[Placeholder text with guidance on what to write]

...

## Figures/Tables
[List of figures needed]

## Word Count Target
[X,000 - Y,000 words]

## Quality Checklist
- [ ] All claims have evidence
- [ ] Figures are clear and labeled
- [ ] References are cited
- [ ] Transitions are smooth
```

### Customizing Templates

**For Your Field:**

1. **Computer Science/Engineering**: Keep implementation chapter (Ch 5)
2. **Pure Math/Theory**: Remove implementation, expand theory chapter (Ch 3)
3. **Experimental Science**: Add experimental setup details to methodology (Ch 4)
4. **Humanities**: Adjust to fit your dissertation structure

**Example Customization:**

```bash
# Rename theory chapter for your field
mv chapter_03_theory.md chapter_03_historical_analysis.md

# Add field-specific chapter
cp chapter_template.md chapter_05_case_studies.md
```

---

## Autonomous Agents

### Overview

The pipeline includes AI agent workflows for systematic execution. These are designed to work with Claude Code or similar AI assistants.

### Agent System (`automation/agents/autonomous_system.md`)

**Purpose:** AI-assisted systematic completion of dissertation tasks

**How It Works:**

1. **Phase-by-Phase Execution**: Agent follows workflow in sequence
2. **Quality Checks**: Built-in verification at each step
3. **Progress Tracking**: Updates todo lists automatically
4. **Error Recovery**: Detects and handles blockers

### Orchestrator (`automation/agents/orchestrator.md`)

**Purpose:** High-level coordination of all phases

**Features:**

- **Timeline Management**: Tracks deadlines and milestones
- **Dependency Tracking**: Ensures prerequisites are met
- **Resource Allocation**: Estimates time/effort for tasks
- **Status Reporting**: Generates progress reports

### Using Agents

```bash
# Option 1: Run full autonomous pipeline
./automation/scripts/run_autonomous.sh

# Option 2: Run single phase
./automation/scripts/run_phase.sh 1  # Phase 1: Planning

# Option 3: Manual execution with agent assistance
# Copy workflows to CLAUDE.md and let AI assistant guide you
```

---

## Quality Assurance

### Chapter Quality Checklist

Use `tools/quality_assurance/chapter_checklist.md` for each chapter:

**Content Quality:**
- [ ] All claims are supported by evidence
- [ ] No aspirational claims (only what was actually done)
- [ ] Clear logical flow between sections
- [ ] Sufficient detail without being verbose

**Technical Quality:**
- [ ] All equations are correctly formatted
- [ ] All figures are referenced in text
- [ ] All citations are accurate
- [ ] Code examples (if any) are correct

**Writing Quality:**
- [ ] No grammar/spelling errors
- [ ] Consistent terminology throughout
- [ ] Appropriate academic tone
- [ ] Smooth transitions between sections

### Dissertation Quality Checklist

Use `tools/quality_assurance/dissertation_checklist.md` before submission:

**Overall Structure:**
- [ ] All 8 chapters present and complete
- [ ] Total word count: 80,000-100,000
- [ ] Chapter lengths are balanced
- [ ] Consistent formatting throughout

**Research Integrity:**
- [ ] All research questions are answered
- [ ] Contributions match what was claimed
- [ ] Experimental results are reproducible
- [ ] No plagiarism (use plagiarism checker)

**Defense Readiness:**
- [ ] Can explain all technical details
- [ ] Can defend all design choices
- [ ] Can answer "why not X?" questions
- [ ] Presentation is ready

---

## LaTeX Compilation

### Build Process

```bash
# From MY_DISSERTATION/latex/ directory

# Option 1: Use provided script
../automation/scripts/build_latex.sh

# Option 2: Manual compilation
pdflatex dissertation.tex
bibtex dissertation
pdflatex dissertation.tex
pdflatex dissertation.tex
```

### Customizing LaTeX

**Modify Preamble** (`latex/preamble.tex`):

```latex
% University-specific formatting
\usepackage[margin=1in]{geometry}  % Adjust margins
\usepackage{setspace}
\doublespacing  % or \onehalfspacing

% Custom packages for your field
\usepackage{algorithm2e}  % For algorithms
\usepackage{listings}     % For code
\usepackage{tikz}         % For diagrams
```

**Chapter Formatting** (`latex/chapters/`):

- Each chapter is a separate `.tex` file
- Included in main `dissertation.tex`
- Easy to compile individual chapters for review

---

## Troubleshooting

### Common Issues

**Issue 1: LaTeX won't compile**

```bash
# Check for missing packages
tlmgr list --installed

# Install missing packages
tlmgr install <package-name>

# Clear auxiliary files
rm *.aux *.log *.out *.toc
```

**Issue 2: Bibliography not showing**

```bash
# Ensure BibTeX is run
bibtex dissertation

# Check .bib file syntax
bibtex-tidy references.bib
```

**Issue 3: Figures not appearing**

```latex
% Check figure path in LaTeX
\graphicspath{{../figures/}}

% Ensure figure files exist
ls ../figures/
```

### Getting Help

1. **Check Documentation**: Read relevant workflow guide
2. **Review Examples**: See `examples/` directory
3. **Search Issues**: Common problems have solutions in docs
4. **Ask AI Assistant**: Use Claude Code with CLAUDE.md instructions

---

## Customization

### Adapting for Your Field

#### Pure Mathematics

```yaml
# config.yaml adjustments
research_type: "theoretical"
chapters:
  - "Chapter 3: Theoretical Foundation" (expand to 15,000 words)
  - "Chapter 5: Proofs and Lemmas" (instead of implementation)
  - "Chapter 6: Examples and Applications" (instead of experiments)
```

#### Experimental Physics

```yaml
# config.yaml adjustments
research_type: "experimental"
chapters:
  - "Chapter 4: Experimental Setup" (expand with apparatus details)
  - "Chapter 5: Measurement Protocol"
  - "Chapter 6: Results and Error Analysis"
```

#### Social Sciences

```yaml
# config.yaml adjustments
research_type: "mixed"
irb_required: true
chapters:
  - "Chapter 4: Research Design" (qualitative/quantitative methods)
  - "Chapter 5: Data Collection"
  - "Chapter 6: Analysis and Findings"
```

### Adding Custom Workflows

```bash
# Create new workflow file
cp workflows/template_workflow.md workflows/08_my_custom_step.md

# Edit to add your specific tasks
nano workflows/08_my_custom_step.md

# Reference in orchestrator
# Edit automation/agents/orchestrator.md to include your workflow
```

---

## Best Practices

### 1. Version Control

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial dissertation setup"

# Commit frequently
git commit -m "Completed literature review draft"

# Use branches for major revisions
git checkout -b revision-1
```

### 2. Backup Strategy

```bash
# Daily backups
cp -r MY_DISSERTATION ~/Dropbox/dissertation_backup_$(date +%F)

# Use cloud storage (Dropbox, Google Drive, OneDrive)
# Use university-provided backup systems
```

### 3. Time Management

- **Work in focused blocks**: 2-4 hour sessions
- **Set weekly goals**: Complete 1 section per week
- **Use todo lists**: Track daily tasks
- **Take breaks**: Avoid burnout

### 4. Writing Discipline

- **Write daily**: Even 500 words per day adds up
- **Don't edit while drafting**: Finish draft first, then revise
- **Use placeholders**: [TODO: Add figure] - come back later
- **Be honest**: Only claim what you can prove

### 5. Quality Over Speed

- **Better to finish slowly with quality than rush and fail defense**
- **Get feedback early**: Share drafts with advisor
- **Revise iteratively**: Multiple passes improve quality
- **Don't cut corners on experiments**: Weak results won't pass defense

---

## Conclusion

This pipeline provides structure, but **you must do the work**. Use it as a guide, adapt it to your needs, and stay disciplined. Completing a PhD dissertation is a marathon, not a sprint.

**You can do this. 🎓**

---

**For further assistance:**
- See individual workflow files in `workflows/`
- Check template files in `templates/`
- Review example dissertation in `examples/`
- Consult with your advisor regularly
