# Production Research Assistant System

A production-grade research automation system built on **Claude Code** architecture, implementing the complete scientific research workflow from problem formulation through publication. Designed for both **autonomous research generation** and **PhD dissertation assistance**.

> **Status:** Phase 8 COMPLETE ✅ - Production-ready with 86.15% test coverage (exceeds 85% target)
> **Architecture:** Pure Claude Code with MCP servers, hooks, and specialized agents
> **Test Coverage:** 86.15% (183/183 tests passing, zero mocking, real logic validation)
> **Production Ready:** Full test suite, comprehensive documentation, all critical modules >85% tested
> **See:** `docs/PHASE8_FINAL_REPORT.md` for details | `htmlcov/index.html` for coverage | `PROJECT_STATUS.md` for status

---

## 🚀 Quick Start

**Get started in 10 minutes:**

1. **[QUICK_START.md](QUICK_START.md)** - Fast setup guide
2. **[INSTALLATION.md](INSTALLATION.md)** - Complete installation instructions
3. **[docs/API_SETUP.md](docs/API_SETUP.md)** - API configuration (all free)

**Already installed?** Just run: `claude` in this directory

---

## 🎯 Overview

This system transforms Claude Code into a complete research assistant capable of:

- **Autonomous Research Mode**: Full ReAct-style hypothesis generation, literature review, experimental design, and paper writing
- **Research Assistant Mode**: Human-guided PhD dissertation completion with systematic workflows
- **PRISMA 2020 Compliant**: Systematic literature reviews following reporting guidelines
- **NIH Rigor Standards**: Experimental designs meeting reproducibility requirements
- **Production Quality**: Real API integrations, version control, quality gates, and reproducibility

### Key Differentiators

- ✅ **Real Implementations**: No mocks - all APIs integrated (Semantic Scholar, arXiv, PubMed, Zotero)
- ✅ **Claude Code Native**: Built specifically for Claude Code architecture (hooks, agents, MCP servers)
- ✅ **Dual Mode**: Seamlessly switch between autonomous and assistant modes
- ✅ **Research Standards**: PRISMA 2020, CONSORT, NIH rigor compliance built-in
- ✅ **Reproducibility**: Git + DVC + MLflow artifact management
- ✅ **Quality Gates**: Decision gates at every workflow phase

---

## 🏗️ Architecture

### Four-Layer System

```
┌─────────────────────────────────────────────────────────────┐
│               Claude Code Primary Agent                      │
│  Hooks: SessionStart, PreToolUse, PostToolUse, Stop, etc.  │
└───────────────────┬─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
┌───────▼──────┐       ┌───────▼──────────┐
│  Subagents   │       │   MCP Servers    │
│              │       │                  │
│ • Literature │       │ • Filesystem     │
│ • Analysis   │       │ • Git            │
│ • Design     │       │ • Zotero         │
│ • Citation   │       │ • PostgreSQL     │
│ • Hypothesis │       │ • Memory Keeper  │
└──────┬───────┘       └────────┬─────────┘
       │                        │
       └────────┬───────────────┘
                │
     ┌──────────▼──────────┐
     │  Artifact Storage   │
     │                     │
     │ • MLflow (tracking) │
     │ • DVC (data)        │
     │ • Git (code/docs)   │
     └─────────────────────┘
```

### Components

**Layer 1: Orchestration**
- Claude Code CLI with 8 event hooks
- Mode switching (autonomous/assistant)
- State machine workflow management

**Layer 2: Data Access (MCP Servers)**
- Literature Search (Semantic Scholar, arXiv, PubMed)
- Citation Management (Zotero, BibTeX, OpenCitations)
- Research Database (PostgreSQL)
- Memory Keeper (persistent context)
- Standard servers (Filesystem, Git, Fetch)

**Layer 3: Specialized Agents**
- 10 research agents (literature reviewer, experiment designer, data analyst, etc.)
- 22 progressive-disclosure skills
- Mode-specific behaviors

**Layer 4: Artifact Management**
- Git for code and documentation
- DVC for data versioning
- MLflow for experiment tracking
- DOI generation for publication

---

## 🔄 Research Workflow

### 11-Phase State Machine

1. **Problem Formulation** → FINER criteria validation
2. **Literature Review** → PRISMA 2020 systematic review
3. **Gap Analysis** → Pattern identification and prioritization
4. **Hypothesis Formation** → Tree-of-Thought generation
5. **Experimental Design** → Power analysis, randomization (NIH standards)
6. **IRB Approval** → Human-guided ethics review
7. **Data Collection** → Real-time validation hooks
8. **Analysis** → Reproducible statistical analysis
9. **Interpretation** → Effect sizes, confidence intervals
10. **Writing** → CONSORT/PRISMA compliant manuscripts
11. **Publication** → DOI generation, archival

Each phase includes:
- Decision gates with validation criteria
- Agent assignment
- MCP server integration
- Deliverable specifications

---

## 🚀 Quick Start

### Prerequisites

```bash
# Ensure Claude Code CLI is installed
# https://docs.claude.com/en/docs/claude-code/overview

# System requirements
- Python 3.11+
- Node.js 20+
- PostgreSQL (for literature database)
- Docker (for reproducibility)
- Git
```

### Installation

```bash
# Clone repository
git clone <repository-url>
cd ai_scientist

# Install Python dependencies
pip install -r requirements.txt

# Install MCP servers
npx @modelcontextprotocol/server-filesystem
uvx mcp-server-git
uv tool run zotero-mcp
npx mcp-memory-keeper

# Configure MCP servers (see docs/setup.md)
# Edit ~/.claude/claude_desktop_config.json

# Initialize DVC for data versioning
dvc init
dvc remote add -d storage s3://your-bucket/dvcstore

# Start MLflow tracking server
mlflow server --backend-store-uri postgresql://localhost/mlflow \
              --default-artifact-root s3://your-bucket/mlflow \
              --host 0.0.0.0 --port 5000
```

### Basic Usage

#### Autonomous Research Mode

```bash
# Start Claude Code in autonomous mode
claude-code

# In chat:
"Conduct autonomous research on [topic]. Use autonomous mode."
```

The system will:
1. Generate hypotheses using Tree-of-Thought
2. Conduct systematic literature review (PRISMA)
3. Design experiments with power analysis
4. Execute and validate results
5. Generate publication-ready manuscript

#### Research Assistant Mode

```bash
# Start Claude Code in assistant mode
claude-code

# In chat:
"Help me with my dissertation literature review on [topic]."
```

The system will:
1. Guide you through PRISMA workflow
2. Assist with database searches
3. Help with screening and extraction
4. Generate PRISMA flow diagram
5. Synthesize findings

---

## 📁 Project Structure

```
ai_scientist/
├── .claude/                      # Claude Code configuration
│   ├── settings.json            # Hook configurations
│   ├── CLAUDE.md                # Project instructions (mode config)
│   ├── agents/                  # 10 specialized agents
│   │   ├── literature-reviewer.md
│   │   ├── experiment-designer.md
│   │   ├── data-analyst.md
│   │   └── ... (7 more)
│   ├── skills/                  # 22 progressive-disclosure skills
│   │   ├── systematic-review/
│   │   ├── hypothesis-generation/
│   │   └── ...
│   └── hooks/                   # Validation, logging, security
│       ├── session-start.sh
│       ├── pre-tool-security.py
│       ├── post-tool-log.py
│       └── pre-compact-backup.py
│
├── mcp-servers/                 # Custom MCP server implementations
│   ├── literature-search.py     # Semantic Scholar, arXiv, PubMed
│   ├── citation-management.py   # Zotero, BibTeX integration
│   └── research-database.py     # PostgreSQL for research data
│
├── workflows/                   # 8 workflow guides
│   ├── chapter_writing_workflow.md
│   ├── defense_preparation_workflow.md
│   └── ...
│
├── templates/                   # LaTeX, communication templates
│   ├── latex/
│   └── communication/
│
├── docs/                        # Documentation
│   ├── setup.md                # Setup instructions
│   ├── agents.md               # Agent documentation
│   ├── workflows.md            # Workflow guides
│   └── api-reference.md        # API reference
│
├── tests/                       # Test suite
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── PROJECT_STATUS.md           # Single source of truth for status
├── README.md                   # This file
└── .gitignore                  # Git ignore patterns
```

---

## 🧠 Dual-Mode Operation

### Mode Configuration

Modes are configured in `.claude/CLAUDE.md`:

```markdown
# Current Mode: AUTONOMOUS

## Autonomous Mode Behaviors
- Auto-progress through workflow phases
- Generate hypotheses without human approval
- Automated literature screening with inter-rater simulation
- Self-reflection loops for hypothesis refinement
- Automatic experiment execution and validation
```

OR

```markdown
# Current Mode: ASSISTANT

## Assistant Mode Behaviors
- Wait for human approval at decision gates
- Interactive hypothesis refinement
- Human-guided literature screening
- Collaborative experimental design
- Explanation of all decisions
```

### Switching Modes

```bash
# Edit .claude/CLAUDE.md and change mode header
# OR use slash command:
/switch-mode autonomous
/switch-mode assistant
```

---

## 🎨 Agent System

### 10 Specialized Agents

| Agent | Purpose | Model | Key Features |
|-------|---------|-------|--------------|
| **literature-reviewer** | PRISMA 2020 systematic reviews | Opus | Multi-database search, inter-rater reliability, risk of bias assessment |
| **experiment-designer** | NIH-compliant experimental design | Opus | Power analysis, randomization, pre-registration |
| **data-analyst** | Reproducible statistical analysis | Sonnet | Assumption testing, effect sizes, sensitivity analyses |
| **hypothesis-generator** | Tree-of-Thought hypothesis generation | Opus | Multi-candidate generation, falsifiability checks |
| **citation-manager** | Citation management and verification | Sonnet | BibTeX, Zotero, retraction checking |
| **gap-analyst** | Literature gap identification | Sonnet | Pattern recognition, prioritization |
| **manuscript-writer** | Reporting guideline-compliant writing | Opus | CONSORT/PRISMA checklists, chain-of-drafts |
| **meta-reviewer** | Cross-phase synthesis | Opus | Pattern analysis, feedback generation |
| **quality-assurance** | Reproducibility validation | Sonnet | Docker testing, citation verification |
| **code-reviewer** | Code quality and security | Sonnet | Linting, security checks, best practices |

---

## 🛠️ MCP Server Ecosystem

### Custom Research Servers

**Literature Search MCP**
```python
# Real API integrations - NO MOCKS
@mcp.tool()
def search_literature(query: str, databases: list[str]) -> list[dict]:
    """Search Semantic Scholar, arXiv, PubMed in parallel"""
    # Returns deduplicated results with metadata
```

**Citation Management MCP**
```python
@mcp.tool()
def verify_citations(doi_list: list[str]) -> dict:
    """Verify citations via OpenCitations, check retractions"""
    # Returns validation status and warnings
```

**Research Database MCP**
```python
@mcp.tool()
def store_extraction(study_id: str, data: dict) -> str:
    """Store systematic review extracted data"""
    # PostgreSQL storage with full-text search
```

### Configuration

See `~/.claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "literature": {
      "command": "python",
      "args": ["mcp-servers/literature-search.py"]
    },
    "citations": {
      "command": "python",
      "args": ["mcp-servers/citation-management.py"]
    },
    "research_db": {
      "command": "python",
      "args": ["mcp-servers/research-database.py"],
      "env": {"DB_HOST": "localhost", "DB_NAME": "research"}
    }
  }
}
```

---

## 🔌 Hook System

### 8 Event Hooks

| Hook | Purpose | Example Use |
|------|---------|-------------|
| **SessionStart** | Load research protocols, mode config | Load PRISMA checklist, NIH guidelines |
| **UserPromptSubmit** | Validate scope, check mode | Ensure query matches mode capabilities |
| **PreToolUse** | Security checks, rate limiting | Block unsafe bash commands, rate limit APIs |
| **PostToolUse** | Logging, DVC tracking | Auto-track large files, log all tool calls |
| **PreCompact** | State backup, memory preservation | Backup research state before context compression |
| **PostCompact** | Restore critical context | Reload current hypothesis, phase state |
| **Error** | Error recovery, fallback | Retry with exponential backoff |
| **Stop** | Completion validation, archiving | Validate all deliverables, create DOIs |

### Example Hook Implementation

```python
# .claude/hooks/post-tool-log.py
def log_tool_use(tool_name, tool_input, tool_output):
    # Log to SQLite
    conn.execute("INSERT INTO tool_log VALUES (?,?,?,?)",
                 (timestamp, tool_name, input_json, output_preview))

    # Auto-track with DVC if file is large
    if tool_name == "Write" and file_size > 10MB:
        os.system(f"dvc add {path} && git add {path}.dvc")
```

---

## 📊 Research Standards Compliance

### PRISMA 2020 (Systematic Reviews)
- ✅ 27-item checklist automated
- ✅ Flow diagram generation
- ✅ Inter-rater reliability (Cohen's Kappa > 0.6)
- ✅ Risk of bias assessment (Cochrane RoB 2, ROBINS-I)
- ✅ GRADE evidence quality

### CONSORT (RCTs)
- ✅ 30-item checklist
- ✅ Power analysis (≥80% power)
- ✅ Randomization with seed documentation
- ✅ Blinding protocols
- ✅ CONSORT flow diagram

### NIH Rigor & Reproducibility
- ✅ Biological variables (SABV)
- ✅ Pre-registration (OSF, ClinicalTrials.gov)
- ✅ FAIR data management plans
- ✅ Statistical analysis pre-specification
- ✅ Code and data availability

---

## 🔬 Example Workflows

### Autonomous Research: Novel Hypothesis Generation

```bash
claude-code

# In chat:
"Generate novel hypotheses for quantum error correction using
machine learning approaches. Use autonomous mode. Conduct full
research cycle including literature review, experimental design,
and manuscript preparation."
```

**What happens:**
1. FINER criteria validation
2. PRISMA systematic review (auto-screening)
3. Gap analysis → ML approaches underexplored
4. Tree-of-Thought hypothesis generation (5 candidates)
5. Hypothesis tournament → select top 3
6. Experimental design with power analysis
7. Reproducible analysis (Docker)
8. CONSORT-compliant manuscript
9. Pre-registration and DOI generation

**Time:** 4-6 hours (mostly LLM calls)
**Cost:** ~$50-100 in API costs
**Output:** Full research paper, pre-registered, reproducible

### Research Assistant: PhD Dissertation Chapter

```bash
claude-code

# In chat:
"Help me complete my dissertation literature review chapter on
the effectiveness of mindfulness interventions for anxiety.
I need PRISMA-compliant systematic review."
```

**What happens:**
1. Guide you through search strategy development
2. Execute searches across PubMed, PsycINFO, Scopus
3. Collaborative screening (you decide, AI tracks)
4. Data extraction with standardized forms
5. Risk of bias assessment
6. Meta-analysis (if appropriate)
7. GRADE evidence quality
8. Generate PRISMA flow diagram
9. Write synthesis with citations
10. Verify all citations (retraction check)

**Time:** 2-4 weeks (human-guided)
**Deliverables:** Complete chapter, PRISMA checklist, all data files

---

## 📈 Quality Assurance

### Pre-commit Hooks
- Code formatting (black, mypy)
- Security scanning (detect-private-key)
- Data validation
- Citation verification

### Reproducibility Testing
```bash
# Automated Docker-based validation
docker run -v $(pwd):/work python:3.11 bash -c "
    pip install -r requirements.txt
    python analysis/primary_analysis.py
"
# Compare results with original
diff results/primary_results.json results/primary_results_original.json
```

### Decision Gates
Every phase requires passing validation before proceeding:
```python
def validate_literature_review() -> dict:
    return {
        "prisma_compliant": sum(checklist.values()) >= 24/27,
        "search_reproducible": search_strategy_documented(),
        "inter_rater_reliable": cohens_kappa() > 0.6,
        "pass": all_checks_true()
    }
```

---

## 🚦 Current Status

**See `PROJECT_STATUS.md` for detailed status**

### Phase 1: Foundation & Cleanup ✅ COMPLETE
- [x] Documentation consolidated
- [x] Python code deleted
- [x] Backup created
- [x] `.claude/` structure created
- [x] Git initialized

### Phase 2: Core Integration ✅ COMPLETE
- [x] 5 priority agents implemented
- [x] 3 MCP servers implemented
- [x] 6 hook scripts implemented
- [x] Skills organized as reference docs
- [x] System tested and validated

### Phase 3: Documentation & Testing ✅ IN PROGRESS
- [x] Installation guide created
- [x] Quick start guide created
- [x] API setup guide created
- [x] MCP server logic tested
- [ ] Real API integration testing

**Estimated Completion:** 69-91 hours total (~9-11 days)
**Progress:** ~20% complete (17 hours)

---

## 📖 Documentation

### Getting Started
- **[QUICK_START.md](QUICK_START.md)** - 10-minute setup guide
- **[INSTALLATION.md](INSTALLATION.md)** - Complete installation instructions (15-30 minutes)
- **[docs/API_SETUP.md](docs/API_SETUP.md)** - Free API configuration guide

### System Documentation
- **[PROJECT_STATUS.md](PROJECT_STATUS.md)** - Current implementation status and roadmap
- **[TEST_RESULTS.md](TEST_RESULTS.md)** - System validation and testing results
- **[mcp-servers/README.md](mcp-servers/README.md)** - MCP server details and setup

### Research References
- **[docs/skills/](docs/skills/)** - 22 research methodology specifications (404KB)
  - Power analysis, PRISMA diagrams, experiment design, etc.
- **[.claude/agents/](/.claude/agents/)** - 5 specialized agent implementations
  - literature-reviewer, experiment-designer, data-analyst, etc.

### Configuration
- **[.claude/CLAUDE.md](.claude/CLAUDE.md)** - Project instructions and mode configuration
- **[.claude/settings.json](.claude/settings.json)** - Hook system configuration
- **[requirements.txt](requirements.txt)** - Python dependencies (pinned versions)

---

## 🤝 Contributing

We welcome contributions in:
- Agent implementations
- MCP server development
- Workflow improvements
- Domain-specific templates
- Quality assurance tools

See `CONTRIBUTING.md` (coming soon)

---

## 📄 License

MIT License - See LICENSE file

---

## 🙏 Acknowledgments

This system builds on specifications from:
- Anthropic's Claude Code architecture
- Model Context Protocol (MCP)
- PRISMA 2020 guidelines
- NIH rigor and reproducibility standards
- Multi-agent research system patterns (Anthropic Engineering)
- Tree-of-Thought reasoning (Princeton NLP)

---

## 📚 Key References

- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code/overview
- **MCP Specification**: https://spec.modelcontextprotocol.io/
- **PRISMA 2020**: https://www.prisma-statement.org/
- **NIH Rigor**: https://grants.nih.gov/policy-and-compliance/policy-topics/reproducibility
- **MLflow**: https://mlflow.org/docs/latest/
- **DVC**: https://dvc.org/doc/start

---

## 💡 Vision

**Goal:** Enable researchers to conduct rigorous, reproducible research with AI assistance while maintaining full transparency, quality, and adherence to scientific standards.

**Philosophy:** Real implementations, real standards, real science.

---

**Last Updated:** January 5, 2025
**Project Status:** Phase 2 Complete - Tested and Functional
**Contact:** See PROJECT_STATUS.md for details
