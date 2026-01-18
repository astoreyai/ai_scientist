# Implementation Approaches: Skills vs. Agents vs. Slash Commands vs. Workflows

**Date:** October 18, 2025
**Purpose:** Analyze which PhD Pipeline processes should be implemented as Skills, Agents, Slash Commands, or Workflows

---

## FRAMEWORK COMPARISON

| Feature | **Skills** | **Agents** | **Slash Commands** | **Workflows** |
|---------|-----------|-----------|-------------------|---------------|
| **When to Use** | Reusable capabilities across projects | Complex, autonomous multi-step tasks | Simple, project-specific commands | Multi-stage processes with human decisions |
| **Complexity** | Low-High | High-Very High | Low-Medium | Medium-Very High |
| **Autonomy** | Interactive | Autonomous | Interactive | Mix of both |
| **Context** | General-purpose | Task-specific | Project-specific | Process-specific |
| **State** | Stateless | Stateful (during execution) | Stateless | Persistent across sessions |
| **Human Interaction** | Frequent | Minimal | Frequent | Frequent |
| **Examples** | @pdf, @xlsx | Task tool with autonomous execution | /build-latex, /setup | Multi-day research processes |

---

## DECISION MATRIX: WHEN TO USE WHAT

### ✅ USE SKILLS WHEN:
- Process is **reusable across ANY PhD dissertation**
- Needs to work in **multiple project contexts**
- Should be **available marketplace-wide**
- Low-to-medium complexity
- Requires interactive guidance
- **Example:** Citation formatting, figure generation, quality checks

### ✅ USE AGENTS WHEN:
- Task is **complex and multi-step**
- Can run **autonomously without human intervention**
- Has **clear success criteria**
- Needs to coordinate multiple tools/actions
- User wants to **"set and forget"**
- **Example:** Running 100-paper literature search, experiment execution, data analysis pipeline

### ✅ USE SLASH COMMANDS WHEN:
- Process is **specific to this PhD pipeline project**
- Simple automation or wrapper
- Invokes existing scripts/tools
- Project-specific configuration
- **Example:** /setup-dissertation, /build-latex, /check-progress

### ✅ USE WORKFLOWS WHEN:
- Process spans **multiple sessions/days/weeks**
- Requires **human decisions at each stage**
- Has **deliverables at each checkpoint**
- Needs **state persistence** across time
- Multiple tools/agents coordinated
- **Example:** Complete literature review (scoping → searching → screening → synthesis), dissertation writing (outlining → drafting → revising → finalizing)

---

## MAPPING PHD PIPELINE PROCESSES

### Category 1: SIMPLE AUTOMATION
**Best as:** Slash Commands

| Process | Implementation | Rationale |
|---------|---------------|-----------|
| Setup dissertation structure | `/setup-dissertation` | Project-specific, runs setup.sh script |
| Build LaTeX to PDF | `/build-latex` | Project-specific, wraps build_latex.sh |
| Check experiment status | `/check-experiments` | Project-specific monitoring |
| Update progress tracker | `/update-progress` | Project-specific TODO management |
| Run citation validation | `/validate-citations` | Project-specific bibliography check |

**Why Slash Commands?**
- These are wrappers around existing bash scripts
- Specific to the PhD pipeline project structure
- Don't need to be marketplace skills
- Simple, single-purpose automation

**Implementation:**
```bash
# .claude/commands/setup-dissertation.md
Run the setup script to initialize dissertation:
- Execute: PHD_PIPELINE/automation/scripts/setup.sh
- Create directory structure
- Copy templates
- Initialize config
```

---

### Category 2: REUSABLE TOOLS
**Best as:** Skills

| Process | Implementation | Rationale |
|---------|---------------|-----------|
| Citation formatter | `@citation-format` | Useful across ANY academic project |
| Figure/table generator | `@figure-table` | General academic need |
| Abstract writer | `@abstract-writer` | Any research paper |
| Quality grammar check | `@academic-grammar` | Any academic writing |
| Statistical power analysis | `@power-analysis` | Any quantitative research |
| Create PRISMA diagram | `@prisma-diagram` | Any systematic review |

**Why Skills?**
- Useful beyond this specific PhD pipeline
- Other students/researchers could use them
- General academic capabilities
- Should be discoverable in marketplace

**Implementation:**
```markdown
# anthropic-skills/citation-format/skill.md
Format citations according to academic style guides.

Supports:
- APA 7th edition
- Chicago
- IEEE
- MLA

Usage: @citation-format [style] [references]
```

---

### Category 3: AUTONOMOUS COMPLEX TASKS
**Best as:** Agents (Task tool)

| Process | Implementation | Rationale |
|---------|---------------|-----------|
| Automated Scopus search | Agent: `scopus-researcher` | Autonomous, complex, multi-API |
| Data cleaning pipeline | Agent: `data-cleaner` | Systematic, rule-based, autonomous |
| Citation deduplication | Agent: `citation-deduplicator` | Algorithmic, no human needed |
| Experiment monitoring | Agent: `experiment-monitor` | Long-running, autonomous checking |
| LaTeX error diagnostics | Agent: `latex-debugger` | Complex troubleshooting |

**Why Agents?**
- Can run autonomously for hours
- Complex multi-step logic
- No human decisions needed
- Clear success/failure criteria
- Background execution

**Implementation:**
```python
# Current implementation exists:
# PHD_PIPELINE/automation/agents/orchestrator.md

# Example invocation:
task = Task(
    subagent_type="general-purpose",
    description="Automated Scopus literature search",
    prompt="""
    Execute a comprehensive Scopus search:
    1. Load keywords from config
    2. Run API queries for each database
    3. Deduplicate results
    4. Export to BibTeX
    5. Update PRISMA diagram
    6. Return summary report

    Run autonomously until complete.
    """
)
```

---

### Category 4: MULTI-STAGE PROCESSES
**Best as:** Workflows (potentially using all of the above)

| Process | Implementation | Components |
|---------|---------------|------------|
| **Systematic Literature Review** | Workflow | Slash commands + Agents + Skills |
| **Write Chapter** | Workflow | Skills + human revision cycles |
| **Design Methodology** | Workflow | Interactive prompts + human decisions |
| **Data Analysis** | Workflow | Agents for processing + Skills for visualization |
| **Dissertation Finalization** | Workflow | Mix of automation + quality checks |

**Systematic Literature Review Workflow Example:**

```
STAGE 1: Planning (Interactive - Human Decisions)
├─ Skill: @keywords-develop
├─ Skill: @inclusion-criteria
└─ Human: Review and approve

STAGE 2: Searching (Autonomous - Agent)
├─ Agent: scopus-researcher
│   ├─ Run queries
│   ├─ Deduplicate
│   └─ Export results
└─ Output: BibTeX file with 500 papers

STAGE 3: Screening (Interactive - Human Decisions)
├─ /command: /screen-papers
├─ Human: Title screening (500 → 200)
├─ Human: Abstract screening (200 → 80)
└─ Human: Full-text screening (80 → 50)

STAGE 4: Synthesis (Agent + Skills)
├─ Skill: @synthesis-matrix
├─ Skill: @prisma-diagram
├─ Agent: gap-analyzer
└─ Output: Literature synthesis

STAGE 5: Writing (Skills + Human)
├─ Skill: @write-lit-review-outline
├─ Human: Draft sections
├─ Skill: @citation-format
├─ Skill: @academic-grammar
└─ Output: Chapter 2
```

**Why Workflow?**
- Spans multiple days/weeks
- Requires human judgment at key points
- Mix of autonomous and interactive steps
- State must persist across sessions
- Multiple deliverables

**Implementation:**
Could be implemented as a **guiding skill** that tracks state:

```markdown
# anthropic-skills/systematic-lit-review/skill.md
Multi-stage systematic literature review workflow.

State tracking:
- [x] Stage 1: Planning
- [ ] Stage 2: Searching  ← You are here
- [ ] Stage 3: Screening
- [ ] Stage 4: Synthesis
- [ ] Stage 5: Writing

Current step: Running Scopus search agent
Next step: Screen 500 papers (title screening)
```

---

## RECOMMENDED ARCHITECTURE FOR PHD PIPELINE

### Layer 1: Project-Specific Commands (Slash Commands)
**Location:** `.claude/commands/` in dissertation project

```
.claude/commands/
├── setup.md              # /setup - Initialize dissertation
├── build.md              # /build - Compile LaTeX
├── progress.md           # /progress - Show status
├── quality-check.md      # /quality-check - Run all checks
└── experiments.md        # /experiments - Run experiments
```

**Purpose:** Project-specific automation, wraps bash scripts

---

### Layer 2: Reusable Skills (Marketplace)
**Location:** `anthropic-skills/` marketplace

```
anthropic-skills/phd-tools/
├── citation-format/
├── figure-table/
├── abstract-writer/
├── prisma-diagram/
├── academic-grammar/
├── power-analysis/
└── synthesis-matrix/
```

**Purpose:** General academic tools useful across any research project

---

### Layer 3: Specialized Agents
**Location:** Invoked via Task tool, configs in project

```
agents/
├── scopus-researcher.md     # Autonomous literature search
├── data-cleaner.md          # Autonomous data pipeline
├── experiment-monitor.md    # Long-running monitoring
├── latex-debugger.md        # Error troubleshooting
└── gap-analyzer.md          # Literature gap analysis
```

**Purpose:** Complex, autonomous, long-running tasks

---

### Layer 4: Workflow Orchestration
**Location:** Workflow guides (markdown) + state tracking

```
workflows/
├── 01_topic_development.md    # Interactive workflow
├── 02_literature_review.md    # Calls agents + skills
├── 03_methodology.md          # Interactive + agents
├── 04_data_analysis.md        # Agents + skills
├── 05_writing.md              # Skills + human
└── 06_finalization.md         # Commands + skills
```

**Purpose:** Multi-stage processes with human decisions

---

## CONCRETE IMPLEMENTATION RECOMMENDATIONS

### Immediate: Slash Commands (Week 1)
Create `.claude/commands/` for this project:

1. ✅ `/setup` - Run setup.sh
2. ✅ `/build` - Run build_latex.sh
3. ✅ `/progress` - Show TODO status
4. ✅ `/quality-check` - Run quality checklists
5. ✅ `/experiments` - Monitor running experiments

**Why first?** Easiest to implement, immediate productivity boost

---

### Phase 2: Core Skills (Weeks 2-4)
Develop marketplace skills:

1. ✅ `@citation-format` - Universal need
2. ✅ `@figure-table` - Publication quality visuals
3. ✅ `@prisma-diagram` - Systematic reviews
4. ✅ `@academic-grammar` - Writing quality
5. ✅ `@abstract-writer` - Paper abstracts

**Why second?** High-value, reusable across projects

---

### Phase 3: Specialized Agents (Weeks 5-6)
Implement complex agents:

1. ✅ `scopus-researcher` - Autonomous search
2. ✅ `data-cleaner` - Data pipeline
3. ✅ `gap-analyzer` - Literature synthesis
4. ✅ `experiment-monitor` - Long-running tasks
5. ✅ `latex-debugger` - Error resolution

**Why third?** Most complex, highest development time

---

### Phase 4: Workflow Guides (Weeks 7-8)
Create workflow orchestration:

1. ✅ Systematic Literature Review workflow
2. ✅ Chapter Writing workflow
3. ✅ Methodology Design workflow
4. ✅ Data Analysis workflow
5. ✅ Finalization workflow

**Why last?** Ties everything together, requires other layers

---

## HYBRID EXAMPLE: LITERATURE REVIEW

Here's how ALL FOUR approaches work together:

### User Journey:

```bash
# Week 1: Planning (Interactive)
User: "I need to do a systematic literature review on face recognition security"

Skill: @keywords-develop
→ Generates: Keywords list

Skill: @inclusion-criteria
→ Generates: Screening criteria

Slash Command: /save-search-protocol
→ Saves to project

# Week 2-3: Searching (Autonomous)
User: "/run-scopus-search"

Slash Command: /run-scopus-search
  ↓
  Launches Agent: scopus-researcher
    ↓
    Agent runs autonomously:
    - Queries Scopus API
    - Deduplicates 500 papers
    - Exports BibTeX
    - Updates PRISMA diagram
  ↓
  Returns: search_results.bib

# Week 4-5: Screening (Interactive + Tools)
User: "/screen-papers"

Slash Command: /screen-papers
  ↓
  Skill: @prisma-tracker
  → Tracks screening progress

  Human: Reviews papers

  Skill: @prisma-diagram
  → Updates flow diagram

# Week 6-7: Synthesis (Agent + Skills)
User: "Synthesize the literature"

Skill: @synthesis-matrix
→ Creates comparison table

Agent: gap-analyzer
→ Analyzes gaps autonomously

Skill: @write-lit-review-outline
→ Generates structure

# Week 8-9: Writing (Skills + Human)
User: "/write-chapter 2"

Workflow guides human through:
  1. Outline (Skill: @outliner)
  2. Draft sections (Human)
  3. Citations (Skill: @citation-format)
  4. Polish (Skill: @academic-grammar)
  5. Quality check (Skill: @chapter-quality-check)

Final: /build-latex
→ Generates PDF
```

### Architecture Benefits:

1. **Slash Commands** = Project-specific glue
2. **Skills** = Reusable capabilities
3. **Agents** = Autonomous heavy-lifting
4. **Workflows** = Human-guided process

Each layer does what it does best!

---

## SUMMARY: WHAT SHOULD BE WHAT?

### Slash Commands (13 processes)
**Project-specific automation:**
- /setup-dissertation
- /build-latex
- /update-progress
- /validate-citations
- /check-experiments
- /quality-check
- /run-scopus-search
- /screen-papers
- /save-protocol
- /backup-data
- /timeline-update
- /advisor-email
- /final-check

---

### Skills (22 processes)
**Reusable academic tools:**
- @citation-format
- @figure-table
- @prisma-diagram
- @synthesis-matrix
- @abstract-writer
- @keywords-develop
- @inclusion-criteria
- @academic-grammar
- @power-analysis
- @statistical-test-selector
- @visualize-results
- @gap-analyzer
- @chapter-quality-check
- @scientific-validity-check
- @write-acknowledgments
- @latex-humanizer
- @equation-formatter
- @table-generator
- @outliner
- @topic-developer
- @research-questions-generator
- @theoretical-framework-builder

---

### Agents (10 processes)
**Autonomous complex tasks:**
- scopus-researcher (literature search)
- citation-deduplicator
- data-cleaner
- experiment-monitor
- latex-debugger
- gap-analyzer (deep analysis)
- statistical-analyzer
- search-optimizer
- paper-screener (ML-assisted)
- reference-validator

---

### Workflows (5 major processes)
**Multi-stage processes:**
1. **Systematic Literature Review** (8-12 weeks)
   - Planning → Searching → Screening → Synthesis → Writing

2. **Chapter Writing** (2-4 weeks per chapter)
   - Outlining → Drafting → Citation → Revision → Quality

3. **Methodology Design** (3-6 weeks)
   - Paradigm → Design → Sampling → Ethics → Validation

4. **Data Analysis** (4-8 weeks)
   - Cleaning → Exploration → Testing → Visualization → Interpretation

5. **Dissertation Finalization** (6-8 weeks)
   - LaTeX → Proofreading → Citations → Abstract → Defense Prep

---

## KEY INSIGHT

**Don't make everything a skill!**

The PhD Pipeline benefits from ALL FOUR approaches:
- **Slash commands** for project-specific quick actions
- **Skills** for reusable academic tools
- **Agents** for autonomous heavy lifting
- **Workflows** for human-guided processes

**Best Practice:**
- Start with slash commands (easiest)
- Develop high-value skills (reusable)
- Add agents for autonomy (complex)
- Tie together with workflows (orchestration)

This creates a **layered architecture** where each component does what it's best at.
