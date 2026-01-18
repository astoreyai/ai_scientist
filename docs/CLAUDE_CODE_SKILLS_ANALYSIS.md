# Claude Code Skills Analysis for PhD Pipeline
## Comprehensive Repository Review

**Date:** October 18, 2025
**Purpose:** Identify all processes in the PhD Pipeline that could be converted to Claude Code skills
**Total Skill Candidates Identified:** 35+

---

## EXECUTIVE SUMMARY

The PhD Pipeline contains **35+ distinct, repeatable processes** that are excellent candidates for Claude Code skills. These range from simple automation (setup scripts) to complex multi-step workflows (literature reviews, LaTeX compilation).

**Skill Categories:**
- 🔄 **Automation Skills** (7): One-command processes
- 📝 **Workflow Skills** (7): Multi-step guided processes
- ✅ **Quality Check Skills** (6): Validation and review processes
- 🔬 **Research Skills** (8): Academic research-specific tasks
- 📊 **Writing Skills** (7): Document generation and formatting

---

## TIER 1: HIGHEST PRIORITY SKILLS (13)
*Most frequently used, highest impact*

### 1. **setup-dissertation** ⭐⭐⭐⭐⭐
**File:** `automation/scripts/setup.sh`
**Type:** Automation
**Complexity:** Low (single script)
**Frequency:** Once per dissertation
**Impact:** Critical - first step for any user

**What it does:**
- Creates dissertation directory structure
- Copies all templates
- Initializes config.yaml
- Sets up bibliography, figures, chapters directories

**Skill invocation:** `@setup-dissertation [dissertation-name]`

**Why it's perfect for a skill:**
- ✅ Self-contained
- ✅ Clear inputs (dissertation name)
- ✅ Predictable outputs (directory structure)
- ✅ Zero ambiguity
- ✅ Already fully automated

---

### 2. **build-latex** ⭐⭐⭐⭐⭐
**File:** `automation/scripts/build_latex.sh`
**Type:** Automation
**Complexity:** Medium (handles errors, multiple passes)
**Frequency:** 10-50 times per dissertation
**Impact:** High - needed for every PDF generation

**What it does:**
- Runs pdflatex multiple times
- Handles bibtex compilation
- Manages auxiliary files
- Reports errors clearly
- Generates final PDF

**Skill invocation:** `@build-latex`

**Why it's perfect for a skill:**
- ✅ Frequently used
- ✅ Consistent process
- ✅ Already scripted
- ✅ Error handling built-in

---

### 3. **systematic-lit-review** ⭐⭐⭐⭐⭐
**File:** `workflows/02_literature_review.md`
**Type:** Multi-step workflow
**Complexity:** High (8 prompts, multiple tools)
**Frequency:** 1-3 times per dissertation
**Impact:** Critical - foundation of research

**What it does:**
1. Define inclusion/exclusion criteria
2. Develop search keywords
3. Create search strings for databases
4. Execute searches (Scopus integration)
5. Screen papers (PRISMA methodology)
6. Extract data to synthesis matrix
7. Structure literature review
8. Write and finalize chapter

**Skill invocation:** `@systematic-lit-review`

**Why it's perfect for a skill:**
- ✅ Highly structured process
- ✅ Clear deliverables at each step
- ✅ Includes Python automation scripts
- ✅ PRISMA-compliant methodology
- ✅ Reduces 100+ hours to guided workflow

**Sub-skills:**
- `@scopus-search` - Run automated Scopus queries
- `@prisma-diagram` - Generate PRISMA flow diagram
- `@synthesis-matrix` - Create literature synthesis matrix

---

### 4. **chapter-quality-check** ⭐⭐⭐⭐⭐
**File:** `tools/quality_assurance/chapter_quality_checklist.md`
**Type:** Quality validation
**Complexity:** Medium
**Frequency:** 8+ times (once per chapter)
**Impact:** High - ensures quality

**What it does:**
- Checks chapter structure
- Validates all citations
- Verifies figures/tables referenced
- Checks writing quality
- Ensures logical flow
- Validates academic tone

**Skill invocation:** `@chapter-quality-check [chapter-file]`

**Why it's perfect for a skill:**
- ✅ Systematic checklist
- ✅ Can be automated with AI
- ✅ Clear pass/fail criteria
- ✅ Prevents submission of incomplete work

---

### 5. **scientific-validity-check** ⭐⭐⭐⭐⭐
**File:** `tools/quality_assurance/scientific_validity_checklist.md`
**Type:** Quality validation
**Complexity:** High (requires deep analysis)
**Frequency:** Continuous throughout dissertation
**Impact:** Critical - ensures honest science

**What it does:**
- Validates every claim has evidence
- Checks for overgeneralization
- Identifies aspirational vs. actual claims
- Verifies reproducibility
- Ensures limitations acknowledged
- Validates statistical rigor

**Skill invocation:** `@scientific-validity-check [chapter-file]`

**Why it's perfect for a skill:**
- ✅ Enforces RULE 1 (scientific truth)
- ✅ Prevents common PhD mistakes
- ✅ AI can identify unsupported claims
- ✅ Critical for publication

---

### 6. **citation-formatter** ⭐⭐⭐⭐
**File:** `tools/bibliography/citation_guidelines.md`
**Type:** Formatting automation
**Complexity:** Medium
**Frequency:** Continuous
**Impact:** High - prevents rejection

**What it does:**
- Converts citations to correct format
- Validates BibTeX entries
- Checks citation completeness
- Ensures consistency
- Generates bibliography

**Skill invocation:** `@citation-formatter [style]`

---

### 7. **defense-prep** ⭐⭐⭐⭐
**File:** `tools/defense_prep/defense_preparation_complete.md`
**Type:** Multi-step workflow
**Complexity:** High (40KB guide)
**Frequency:** Once per dissertation
**Impact:** Critical - final hurdle

**What it does:**
- Creates 6-month defense timeline
- Generates presentation outline
- Prepares anticipated questions
- Rehearsal schedule
- Committee communication plan

**Skill invocation:** `@defense-prep`

---

### 8. **figure-table-generator** ⭐⭐⭐⭐
**File:** `tools/writing_aids/figure_table_equation_guidelines.md`
**Type:** Content generation
**Complexity:** Medium (33KB guide)
**Frequency:** 20-50 times per dissertation
**Impact:** High - visual quality matters

**What it does:**
- Creates publication-quality figures
- Generates LaTeX tables
- Formats equations
- Ensures proper captioning
- Cross-references correctly

**Skill invocation:** `@figure-table [type] [data]`

---

### 9. **data-backup-protocol** ⭐⭐⭐⭐
**File:** `tools/data_management/data_management_protocol.md`
**Type:** Automation + checklist
**Complexity:** Medium (46KB protocol)
**Frequency:** Daily/weekly
**Impact:** Critical - prevents data loss

**What it does:**
- Implements 3-2-1 backup rule
- Automated backup scripts
- Version control setup
- Data integrity checks
- Recovery procedures

**Skill invocation:** `@data-backup-setup`

---

### 10. **write-chapter** ⭐⭐⭐⭐
**File:** `workflows/05_writing.md`
**Type:** Multi-step workflow
**Complexity:** Very High (91KB - largest workflow)
**Frequency:** 8 times (one per chapter)
**Impact:** High - core work

**What it does:**
- Multi-pass writing process
- Structural outlining
- Content generation
- Citation integration
- Revision cycles
- Academic tone refinement

**Skill invocation:** `@write-chapter [chapter-number]`

---

### 11. **methodology-designer** ⭐⭐⭐⭐
**File:** `workflows/03_methodology.md`
**Type:** Multi-step workflow
**Complexity:** High (32KB)
**Frequency:** 1-2 times per dissertation
**Impact:** Critical - research design

**What it does:**
1. Select research paradigm
2. Design study methodology
3. Define sampling strategy
4. Create instruments
5. Plan data analysis
6. Ensure validity/reliability
7. Address ethical considerations

**Skill invocation:** `@methodology-designer`

---

### 12. **data-analysis-workflow** ⭐⭐⭐⭐
**File:** `workflows/04_data_analysis.md`
**Type:** Multi-step workflow
**Complexity:** High (47KB)
**Frequency:** 1-3 times per dissertation
**Impact:** High - results chapter

**What it does:**
1. Data cleaning pipeline
2. Exploratory analysis
3. Statistical testing
4. Visualization creation
5. Results interpretation
6. Findings documentation

**Skill invocation:** `@data-analysis`

---

### 13. **topic-developer** ⭐⭐⭐⭐
**File:** `workflows/01_topic_development.md`
**Type:** Multi-step workflow
**Complexity:** Medium
**Frequency:** 1 time per dissertation (but critical)
**Impact:** Critical - everything depends on this

**What it does:**
1. Brainstorm research topics
2. Gap analysis in literature
3. Formulate research questions
4. Develop theoretical framework
5. Define scope and boundaries

**Skill invocation:** `@topic-developer`

---

## TIER 2: HIGH VALUE SKILLS (12)

### 14. **progress-tracker** ⭐⭐⭐
**File:** `tools/progress_tracking/todo_template.md`
**Type:** Project management
**Complexity:** Low
**Frequency:** Daily/weekly
**Impact:** Medium - keeps on track

**What it does:**
- Creates TODO lists per chapter
- Tracks milestones
- Updates progress metrics
- Identifies blockers

**Skill invocation:** `@progress-update`

---

### 15. **timeline-generator** ⭐⭐⭐
**File:** `tools/progress_tracking/timeline_template.md`
**Type:** Planning
**Complexity:** Low
**Frequency:** 1-3 times per dissertation
**Impact:** Medium - planning

**What it does:**
- Creates realistic timeline
- Identifies dependencies
- Accounts for advisor feedback cycles
- Generates Gantt chart

**Skill invocation:** `@timeline-create`

---

### 16. **advisor-emailer** ⭐⭐⭐
**File:** `templates/advisor_communication/`
**Type:** Content generation
**Complexity:** Low
**Frequency:** 10-50 times per dissertation
**Impact:** Medium - communication

**What it does:**
- Drafts progress update emails
- Requests feedback professionally
- Summarizes meetings
- Proposes next steps

**Skill invocation:** `@advisor-email [type]`

---

### 17. **scopus-automated-search** ⭐⭐⭐
**File:** `tools/literature_review/automated_scopus/`
**Type:** Automation (Python scripts)
**Complexity:** High (multiple Python files)
**Frequency:** 1-5 times per dissertation
**Impact:** High - saves 20+ hours

**What it does:**
- Runs Scopus API queries
- Deduplicates results
- Exports to CSV/BibTeX
- Updates PRISMA diagram
- Generates search logs

**Files:**
- `scopus_search.py`
- `deduplication.py`
- `result_exporter.py`
- `prisma_updater.py`

**Skill invocation:** `@scopus-search [keywords]`

---

### 18. **prisma-flow-diagram** ⭐⭐⭐
**File:** `tools/literature_review/prisma_flow_diagram_template.md`
**Type:** Content generation
**Complexity:** Medium
**Frequency:** 1-2 times per dissertation
**Impact:** High - required for systematic reviews

**What it does:**
- Creates PRISMA 2020 compliant diagram
- Tracks screening numbers
- Documents exclusion reasons
- Generates LaTeX/TikZ diagram

**Skill invocation:** `@prisma-diagram [numbers]`

---

### 19. **synthesis-matrix** ⭐⭐⭐
**File:** `tools/literature_review/synthesis_matrix_template.csv`
**Type:** Data organization
**Complexity:** Medium
**Frequency:** 1 time per dissertation
**Impact:** High - organizes literature

**What it does:**
- Creates structured comparison table
- Extracts key findings from papers
- Identifies themes
- Supports gap analysis

**Skill invocation:** `@synthesis-matrix`

---

### 20. **gap-analyzer** ⭐⭐⭐
**File:** Part of `workflows/02_literature_review.md`
**Type:** Analysis
**Complexity:** High (requires AI reasoning)
**Frequency:** 1-2 times per dissertation
**Impact:** Critical - justifies research

**What it does:**
- Analyzes synthesis matrix
- Identifies research gaps
- Justifies contribution
- Positions research in field

**Skill invocation:** `@gap-analysis`

---

### 21. **latex-humanizer** ⭐⭐⭐
**File:** Referenced in LATEX_HUMANIZATION_COMPLETE.md
**Type:** Text transformation
**Complexity:** Medium
**Frequency:** Final pass (1 time)
**Impact:** Medium - improves readability

**What it does:**
- Converts overly formal academic prose
- Maintains scholarly tone
- Improves readability
- Removes AI-like patterns

**Skill invocation:** `@humanize-latex [chapter]`

---

### 22. **chapter-template-filler** ⭐⭐⭐
**File:** `templates/dissertation/chapter_*.md`
**Type:** Content generation
**Complexity:** Medium
**Frequency:** 8 times (one per chapter)
**Impact:** High - scaffolding

**What it does:**
- Takes chapter template
- Fills in placeholders
- Maintains structure
- Ensures completeness

**Skill invocation:** `@fill-chapter [chapter-number]`

---

### 23. **finalization-workflow** ⭐⭐⭐
**File:** `workflows/06_finalization.md`
**Type:** Multi-step workflow
**Complexity:** Very High (78KB)
**Frequency:** 1 time per dissertation
**Impact:** Critical - final polish

**What it does:**
1. LaTeX conversion/refinement
2. Final proofreading
3. Citation verification
4. Abstract writing
5. Acknowledgments
6. Formatting compliance
7. PDF generation
8. Submission preparation

**Skill invocation:** `@finalization`

---

### 24. **quality-checklist-runner** ⭐⭐⭐
**File:** `workflows/07_quality_checklist.md`
**Type:** Validation
**Complexity:** Medium
**Frequency:** Before submission
**Impact:** High - final check

**What it does:**
- Runs all quality checks
- Validates completeness
- Ensures formatting
- Checks references
- Final approval gate

**Skill invocation:** `@final-quality-check`

---

### 25. **keyword-developer** ⭐⭐⭐
**File:** `tools/literature_review/KEYWORD_DEVELOPMENT_GUIDE.md`
**Type:** Content generation
**Complexity:** Medium
**Frequency:** 1-2 times
**Impact:** High - search quality

**What it does:**
- Brainstorms search keywords
- Creates Boolean queries
- Develops synonyms
- Tests search strings

**Skill invocation:** `@keywords-develop [topic]`

---

## TIER 3: SPECIALIZED SKILLS (10)

### 26. **autonomous-orchestrator** ⭐⭐
**File:** `automation/agents/orchestrator.md`
**Type:** Meta-automation
**Complexity:** Very High
**Frequency:** Optional - advanced users
**Impact:** High for power users

**What it does:**
- Coordinates multiple skills
- Manages workflow dependencies
- Tracks overall progress
- Makes intelligent decisions

**Skill invocation:** `@orchestrate [phase]`

---

### 27. **article-extractor** ⭐⭐
**File:** Related to `article_A_theory_method`, etc.
**Type:** Content transformation
**Complexity:** High
**Frequency:** 1-3 times (for publications)
**Impact:** High for publishing

**What it does:**
- Extracts chapters as standalone articles
- Reformats for journal submission
- Generates separate bibliographies
- Adjusts formatting

**Skill invocation:** `@extract-article [chapters]`

---

### 28. **search-strategy-builder** ⭐⭐
**File:** `tools/literature_review/search_protocol_template.md`
**Type:** Planning
**Complexity:** Medium
**Frequency:** 1 time
**Impact:** High - systematic reviews

**What it does:**
- Creates search protocol
- Documents methodology
- Ensures reproducibility
- PRISMA compliant

**Skill invocation:** `@search-protocol`

---

### 29. **inclusion-exclusion-criteria** ⭐⭐
**File:** `tools/literature_review/inclusion_exclusion_criteria_template.md`
**Type:** Planning
**Complexity:** Medium
**Frequency:** 1 time
**Impact:** High - systematic reviews

**What it does:**
- Defines paper selection criteria
- Creates decision tree
- Ensures objectivity
- Documents rationale

**Skill invocation:** `@inclusion-criteria`

---

### 30. **ethics-reviewer** ⭐⭐
**File:** Part of `workflows/03_methodology.md`
**Type:** Compliance check
**Complexity:** High
**Frequency:** 1 time
**Impact:** Critical for human subjects

**What it does:**
- Identifies ethical considerations
- IRB preparation guidance
- Informed consent templates
- Risk assessment

**Skill invocation:** `@ethics-review`

---

### 31. **statistical-power-analyzer** ⭐⭐
**File:** Part of `workflows/04_data_analysis.md`
**Type:** Statistical analysis
**Complexity:** High
**Frequency:** During planning phase
**Impact:** High - study design

**What it does:**
- Calculates required sample size
- Power analysis
- Effect size estimation
- Statistical test selection

**Skill invocation:** `@power-analysis`

---

### 32. **results-visualizer** ⭐⭐
**File:** Part of `workflows/04_data_analysis.md`
**Type:** Data visualization
**Complexity:** Medium
**Frequency:** 10-30 times
**Impact:** High - visual communication

**What it does:**
- Creates publication-quality plots
- Generates LaTeX-compatible figures
- Ensures accessibility
- Follows field conventions

**Skill invocation:** `@visualize-results [data]`

---

### 33. **abstract-writer** ⭐⭐
**File:** Part of `workflows/06_finalization.md`
**Type:** Content generation
**Complexity:** Medium
**Frequency:** 1 time (but critical)
**Impact:** High - first impression

**What it does:**
- Extracts key contributions
- Writes structured abstract
- Meets word limits
- Includes keywords

**Skill invocation:** `@write-abstract`

---

### 34. **acknowledgments-generator** ⭐⭐
**File:** Part of `workflows/06_finalization.md`
**Type:** Content generation
**Complexity:** Low
**Frequency:** 1 time
**Impact:** Low - but required

**What it does:**
- Structures acknowledgments
- Thanks advisors, funders
- Professional tone
- Follows conventions

**Skill invocation:** `@write-acknowledgments`

---

### 35. **search-query-optimizer** ⭐⭐
**File:** `tools/literature_review/SCOPUS_QUERIES_QUICK_REFERENCE.md`
**Type:** Content generation
**Complexity:** Medium
**Frequency:** 2-5 times
**Impact:** Medium - search quality

**What it does:**
- Optimizes Scopus queries
- Tests different formulations
- Balances precision/recall
- Database-specific syntax

**Skill invocation:** `@optimize-query [keywords]`

---

## IMPLEMENTATION PRIORITY MATRIX

### Immediate (Weeks 1-2): Core Automation
1. ✅ `@setup-dissertation`
2. ✅ `@build-latex`
3. ✅ `@chapter-quality-check`
4. ✅ `@scientific-validity-check`
5. ✅ `@citation-formatter`

**Rationale:** Most frequently used, highest ROI, already have scripts

---

### Phase 2 (Weeks 3-4): Workflow Skills
6. ✅ `@systematic-lit-review`
7. ✅ `@topic-developer`
8. ✅ `@methodology-designer`
9. ✅ `@data-analysis-workflow`
10. ✅ `@write-chapter`

**Rationale:** Core PhD workflows, high impact

---

### Phase 3 (Weeks 5-6): Research Tools
11. ✅ `@scopus-automated-search`
12. ✅ `@prisma-flow-diagram`
13. ✅ `@synthesis-matrix`
14. ✅ `@gap-analyzer`
15. ✅ `@figure-table-generator`

**Rationale:** Specialized but high-value tools

---

### Phase 4 (Weeks 7-8): Completion & Quality
16. ✅ `@defense-prep`
17. ✅ `@finalization-workflow`
18. ✅ `@data-backup-protocol`
19. ✅ `@progress-tracker`
20. ✅ `@timeline-generator`

**Rationale:** End-stage workflows and continuous tools

---

### Phase 5 (Weeks 9-10): Nice-to-Haves
21-35: Specialized skills based on user feedback

---

## SKILL ARCHITECTURE RECOMMENDATIONS

### Skill Types

1. **Simple Command Skills** (like slash commands)
   - `@setup-dissertation`
   - `@build-latex`
   - `@citation-formatter`

2. **Interactive Workflow Skills** (multi-turn)
   - `@systematic-lit-review`
   - `@write-chapter`
   - `@methodology-designer`

3. **Validation Skills** (return pass/fail + feedback)
   - `@chapter-quality-check`
   - `@scientific-validity-check`
   - `@final-quality-check`

4. **Generation Skills** (create content)
   - `@figure-table-generator`
   - `@abstract-writer`
   - `@advisor-email`

### Skill Composability

Many skills should be composable:

```
@systematic-lit-review
  ├─ @keywords-develop
  ├─ @inclusion-criteria
  ├─ @scopus-search
  ├─ @prisma-diagram
  ├─ @synthesis-matrix
  └─ @gap-analyzer
```

### State Management

Some skills need to maintain state across sessions:
- `@progress-tracker` - persistent TODO list
- `@timeline-generator` - milestone tracking
- `@systematic-lit-review` - multi-session workflow

---

## ESTIMATED IMPACT

### Time Savings Per Dissertation

| Skill | Time Saved | Frequency | Total Saved |
|-------|-----------|-----------|-------------|
| `@systematic-lit-review` | 80 hours | 1x | 80 hours |
| `@write-chapter` | 10 hours/chapter | 8x | 80 hours |
| `@build-latex` | 15 min/use | 50x | 12.5 hours |
| `@methodology-designer` | 40 hours | 1x | 40 hours |
| `@data-analysis-workflow` | 30 hours | 1x | 30 hours |
| `@chapter-quality-check` | 2 hours/chapter | 8x | 16 hours |
| `@defense-prep` | 40 hours | 1x | 40 hours |
| `@scopus-search` | 20 hours | 1x | 20 hours |
| **TOTAL** | | | **318.5 hours** |

**That's nearly 40 full workdays saved per dissertation!**

---

## CONCLUSION

The PhD Pipeline contains **35+ processes** that are excellent candidates for Claude Code skills. The top 13 Tier 1 skills would provide immediate, dramatic value to PhD students.

**Recommended approach:**
1. Start with 5 automation skills (setup, build, quality checks)
2. Add 5 workflow skills (lit review, writing, methodology)
3. Expand based on user feedback
4. Build skill composability over time

**Key insight:** These skills enforce best practices (systematic reviews, quality checks, scientific validity) that many students skip due to time constraints. Automating these makes doing the right thing easier than doing the wrong thing.
