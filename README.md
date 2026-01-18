# Research Assistant for Claude Code

**PRISMA 2020 systematic reviews and NIH-compliant research workflows in Claude Code**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Compatible](https://img.shields.io/badge/Claude%20Code-Compatible-blue)](https://claude.ai/code)

Transform academic research workflows with 22 specialized skills, 10 intelligent agents, and professional-grade quality assurance. Built for PhD students, postdocs, and academics conducting systematic reviews, experimental studies, and rigorous manuscript preparation.

***

## Installation

```bash
# Step 1: Add to marketplace
/plugin marketplace add https://github.com/astoreyai/ai_scientist

# Step 2: Install plugin
/plugin install research-assistant

# Step 3: Verify installation
/skill list  # Should show 22 skills
/agent list  # Should show 10 agents
```

***

## Quick Start

### Approach 0: Run an AI-Check

```bash
# Detect AI-generated text in manuscripts
/skill ai-check manuscript.tex
# Returns confidence score: 0-30% (human), 30-70% (mixed), 70-100% (AI)
```

### Approach 1: Invoke a Specialized Agent

```bash
# Launch PRISMA 2020 systematic review agent
/agent literature-reviewer

# Agent guides you through:
# 1. Multi-database search strategy
# 2. Abstract screening workflow
# 3. Risk of bias assessment
# 4. PRISMA flow diagram generation
```

### Approach 2: Complete Research Workflow

```flow
# Power user: Full systematic review
/skill problem-formulation -> /agent literature-reviewer -> /skill gap-analysis -> /agent manuscript-writer
# Validates FINER criteria → PRISMA 2020 review → Gap prioritization → Publication-ready manuscript
```

***

## Slash Commands

Quick discovery and navigation commands for all resources:

```bash
/skills      # List all 22 research skills (categorized)
/agents      # List all 10 specialized agents (by type)
/templates   # List all 10 research templates (with standards)
/tutorials   # List all 11 tutorials (with learning paths)
```

**What slash commands do:**
- Provide instant access to available resources
- Show categorized lists with descriptions
- Include usage examples and recommendations
- No need to read documentation first

**Example workflow:**
```bash
# Discover what's available
/skills          # Browse 22 research skills

# See specialized agents
/agents          # 10 agents for complex tasks

# Find a template for your project
/templates       # 10 templates with reporting standards

# Learn step-by-step
/tutorials       # 11 tutorials, 8 hours of content
```

***

## Core Features

| Category | Skills | Capabilities |
|----------|--------|--------------|
| **Evidence Synthesis** | `systematic-review`, `scoping-review`, `meta-analysis`, `network-meta-analysis` | PRISMA 2020/PRISMA-ScR/PRISMA-MA compliance, forest plots, heterogeneity assessment |
| **Experimental Design** | `rct-design`, `observational-study`, `pragmatic-trial`, `power-analysis` | CONSORT/STROBE reporting, NIH rigor standards, randomization protocols |
| **Quality Improvement** | `pdsa-cycles`, `spc-charts`, `improvement-science` | SQUIRE 2.0 reporting, Model for Improvement, control charts |
| **Qualitative Research** | `grounded-theory`, `phenomenology`, `qualitative-synthesis` | COREQ checklist, constant comparison, trustworthiness criteria |
| **Implementation Science** | `reaim-framework`, `cfir-assessment`, `hybrid-designs` | RE-AIM, CFIR 39 constructs, ERIC strategies |
| **Statistical Analysis** | `effect-sizes`, `assumption-testing`, `sensitivity-analysis` | Reproducible R/Python code, confidence intervals, power calculations |
| **Writing Support** | `manuscript-drafting`, `grant-proposals`, `dissertation-structure` | NIH R01 proposals, CONSORT/PRISMA manuscripts, LaTeX formatting |
| **Quality Assurance** | `ai-check`, `reproducibility-validation`, `protocol-adherence` | AI-text detection, git/DVC integration, pre-registration |

***

## Specialized Agents

### Evidence Synthesis Agents
- **literature-reviewer** - PRISMA 2020 systematic reviews with inter-rater reliability
- **meta-reviewer** - Quality assessment using AMSTAR 2 criteria
- **gap-analyst** - Systematic gap identification and research prioritization

### Design & Analysis Agents
- **experiment-designer** - NIH-rigorous protocols with pre-registration
- **data-analyst** - Reproducible statistical analysis with effect sizes
- **hypothesis-generator** - Tree-of-Thought hypothesis evolution

### Writing & Quality Agents
- **manuscript-writer** - CONSORT/PRISMA-compliant publication drafts
- **citation-manager** - BibTeX/Zotero integration, retraction checking
- **quality-assurance** - Protocol validation and reproducibility audits
- **code-reviewer** - Statistical code correctness verification

***

## Interactive Tutorials

**11 comprehensive tutorials, 280KB total, 8 hours of training**

| Tutorial | Focus | Duration | Key Outputs |
|----------|-------|----------|-------------|
| **Getting Started** | Plugin basics, workflow overview | 25 min | First systematic review setup |
| **Literature Review** | PRISMA 2020 end-to-end | 45 min | Complete PRISMA flow diagram |
| **Experimental Design** | NIH rigor standards | 40 min | Pre-registered RCT protocol |
| **AI-Check Deep Dive** | AI-text detection | 30 min | Pre-commit hook integration |
| **Complete Workflow** | Idea → publication | 60 min | Full RCT manuscript (meditation study) |
| **Multi-Site Trials** | Consortium coordination | 50 min | Data harmonization protocol |
| **Mixed Methods** | Integration strategies | 55 min | Joint display tables, GRAM compliance |
| **Grant Proposals** | NIH R01 writing | 60 min | Complete Specific Aims + approach |
| **Qualitative Research** | Grounded theory | 50 min | COREQ-compliant analysis (NVivo) |
| **Meta-Analysis** | Random effects models | 55 min | Forest plots, publication bias tests |
| **Implementation Science** | RE-AIM/CFIR | 55 min | TF-CBT implementation evaluation |

***

## Research Templates

**10 production-ready templates with checklists and protocols**

### Evidence Synthesis
- **Systematic Review** - PRISMA 2020 27-item checklist, risk of bias tools
- **Scoping Review** - PRISMA-ScR 22-item, PCC framework, Arksey & O'Malley
- **Network Meta-Analysis** - PRISMA-NMA 32-item, SUCRA rankings, league tables

### Experimental Studies
- **RCT Study** - CONSORT 2010, allocation concealment, analysis plan
- **Observational Study** - STROBE checklist, confounder identification
- **Pragmatic Trial** - PRECIS-2 9-domain scoring, real-world effectiveness

### Specialized Methods
- **Computational Methods** - Algorithm validation, reproducibility standards
- **Quality Improvement** - SQUIRE 2.0 18-item, PDSA cycles, SPC charts

### Academic Development
- **PhD Dissertation** - Chapter structure, timeline, committee agendas
- **Advisor Communication** - Meeting templates, milestone tracking

***

## AI-Check System

Detect AI-generated text patterns to ensure authentic academic writing.

**Detection Methods:**
- Grammar perfection analysis (>95% correctness flags)
- Sentence uniformity detection (15-25 word consistency patterns)
- AI-typical vocabulary ("delve", "leverage", "robust", "comprehensive")
- Style consistency scoring

**Integration Modes:**

```bash
# Standalone manuscript analysis
python tools/ai_check.py manuscript.tex

# Pre-commit hook (blocks high-AI commits)
cp hooks/pre-commit .git/hooks/ && chmod +x .git/hooks/pre-commit

# Section-specific checking
python tools/ai_check.py manuscript.tex --section methods
```

**Confidence Scoring:**
- **0-30%**: Likely human-written
- **30-70%**: Possible AI assistance, review flagged sections
- **70-100%**: Likely AI-generated, manual rewrite recommended

***

## Real-World Examples

### Example 1: PRISMA Systematic Review

```flow
# Complete systematic review workflow
/skill problem-formulation FINER
  -> /agent literature-reviewer
    # Multi-database search: PubMed, Embase, PsycINFO
    # 2,847 records identified → 124 full-text reviewed → 23 included
  -> /skill risk-of-bias
    # Cochrane RoB 2 assessment
  -> /skill meta-analysis
    # Random effects model, I² = 68%
  -> /agent manuscript-writer PRISMA
    # Publication-ready manuscript with flow diagram
```

### Example 2: NIH-Rigorous RCT

```flow
# Pre-registered randomized controlled trial
/skill rct-design
  -> /skill power-analysis effect_size=0.5
    # 80% power, alpha=0.05 → N=128 required
  -> /skill randomization seed=42
    # Permuted block randomization (block size 4)
  -> /skill preregistration OSF
    # Timestamped protocol registration
  -> /agent data-analyst
    # Intention-to-treat analysis with effect sizes
```

### Example 3: Grant Proposal Development

```flow
# NIH R01 proposal from concept to submission
/skill specific-aims
  -> /skill significance-innovation
  -> /skill approach-section
    # Experimental design, power analysis, timeline
  -> /skill human-subjects
    # Inclusion/exclusion, recruitment, protection plans
  -> /agent quality-assurance NIH-checklist
    # Validates all required components
```

***

## Research Coverage

**Quantitative Methods**: RCTs, observational studies, meta-analysis, network meta-analysis

**Qualitative Methods**: Grounded theory, phenomenology, ethnography, qualitative synthesis

**Mixed Methods**: Convergent, sequential, embedded designs with integration strategies

**Evidence Synthesis**: Systematic reviews, scoping reviews, meta-analyses (fixed/random effects)

**Implementation Science**: RE-AIM, CFIR, ERIC strategies, hybrid effectiveness-implementation designs

**Quality Improvement**: PDSA cycles, statistical process control, SQUIRE 2.0 reporting

**Grant Writing**: NIH R01/R03/R21 proposals, specific aims, significance/innovation/approach

***

## Quality Standards

| Standard | Application | Validation |
|----------|-------------|------------|
| **PRISMA 2020** | Systematic reviews | 27-item checklist (24/27 minimum) |
| **CONSORT** | RCTs | 30-item checklist, flow diagram |
| **STROBE** | Observational studies | 22-item checklist |
| **SQUIRE 2.0** | Quality improvement | 18-item checklist |
| **COREQ** | Qualitative research | 32-item checklist |
| **NIH Rigor** | All experimental | Power ≥80%, pre-registration, SABV |
| **PRECIS-2** | Pragmatic trials | 9-domain scoring (0-5 each) |
| **PRISMA-MA** | Meta-analyses | 32-item checklist, heterogeneity tests |

***

## Reproducibility Tools

**Version Control Integration:**
- Git tracking for code, protocols, manuscripts
- DVC (Data Version Control) for large datasets (>10MB auto-tracked)
- Pre-commit hooks for quality gates (AI-check, linting)

**Experiment Tracking:**
- MLflow integration for statistical analyses
- Random seed documentation
- Complete dependency pinning (requirements.txt)

**Containerization:**
- Docker environments for reproducible analysis
- All code executable in clean containers

**Pre-Registration:**
- OSF integration templates
- Timestamped protocol submission
- Analysis plan versioning

***

## Requirements

- **Claude Code** (latest version)
- **Python 3.8+** (for MCP servers, optional)
- **R 4.0+** (for meta-analysis templates, optional)
- **Git** (for version control)

***

## Project Structure

```
research-assistant/
├── skills/              # 22 specialized research skills
├── .claude/agents/      # 10 intelligent research agents
├── tutorials/           # 11 interactive tutorials (280KB)
├── templates/           # 10 production-ready research templates
├── mcp-servers/         # Literature search, citations, research DB
├── tools/               # AI-check, validators, quality assurance
├── hooks/               # Pre-commit hooks for quality gates
└── tests/               # 116 tests, 57% coverage
```

***

## Support

**GitHub Issues**: [Report bugs or request features](https://github.com/astoreyai/ai_scientist/issues)

**Email**: astoreyai@gmail.com

**Documentation**: See `tutorials/` directory for 11 comprehensive guides

***

## Citation

If you use this plugin in your research:

```bibtex
@software{research_assistant_2025,
  author = {Storey, Aaron},
  title = {Research Assistant for Claude Code},
  year = {2025},
  version = {1.2.0-beta3},
  url = {https://github.com/astoreyai/ai_scientist}
}
```

***

## License

MIT License - see [LICENSE](LICENSE) for details.

***

**Professional research workflow automation for academics**

**22 Skills** | **10 Agents** | **11 Tutorials** | **10 Templates** | **PRISMA 2020 + NIH Compliant**
