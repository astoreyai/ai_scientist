# Research Assistant - Claude Code Marketplace Listing

**Plugin Name:** Research Assistant
**Version:** 1.2.0-beta3
**Category:** Productivity / Academic Research
**License:** MIT
**Author:** Aaron Storey (aaron@astoreyai.com)

---

## Short Description (1-2 sentences)

Professional research workflow automation for PhD students and academics. Complete PRISMA 2020 systematic reviews, NIH-compliant experimental design, reproducible statistical analysis, and AI-generated text detection in one integrated Claude Code plugin.

---

## Long Description

The Research Assistant plugin transforms Claude Code into a comprehensive research workflow platform designed specifically for PhD students, postdocs, and academic researchers. Whether you're conducting systematic literature reviews, designing rigorous experiments, analyzing data, or writing manuscripts, this plugin provides specialized tools, agents, and workflows that follow gold-standard methodologies.

### What Makes This Plugin Unique

**Compliance-First Design:**
- PRISMA 2020 systematic review standards
- NIH rigor and reproducibility requirements
- CONSORT/STROBE reporting guidelines
- Pre-registration and open science practices

**Complete Research Lifecycle:**
From literature search to publication, every phase is supported with specialized tools and templates.

**AI-Detection Innovation:**
Built-in AI-generated text detection helps maintain authentic academic writing and catch inadvertent LLM artifacts before submission.

**Production-Ready Quality:**
116 tests, comprehensive documentation, security-validated hooks, and professional-grade code quality.

---

## Key Features

### 22 Specialized Skills
- **AI-Check**: Detect AI-generated text patterns in manuscripts
- **Power Analysis**: Calculate sample sizes with NIH justifications
- **Effect Size**: Compute Cohen's d, eta-squared, odds ratios with confidence intervals
- **PRISMA Diagram**: Generate PRISMA 2020 flow diagrams with counts
- **Citation Format**: Format references in APA, IEEE, Chicago, Vancouver
- **Risk of Bias**: Assess study quality using ROB2/ROBINS-I
- **Meta-Analysis**: Random/fixed effects models with forest plots
- **Pre-Registration**: Generate OSF/ClinicalTrials.gov registration protocols
- **Literature Gap Analysis**: Identify research gaps systematically
- **Hypothesis Testing**: Statistical test selection and interpretation
- ...and 12 more research-specific skills

### 10 Autonomous Agents
- **Literature Reviewer**: PRISMA 2020 compliant systematic reviews
- **Experiment Designer**: NIH-standard experimental protocols
- **Data Analyst**: Reproducible statistical analysis with assumption testing
- **Manuscript Writer**: CONSORT/PRISMA compliant paper drafting
- **Citation Manager**: BibTeX/Zotero integration and retraction checking
- **Hypothesis Generator**: Tree-of-Thought research question formation
- **Gap Analyst**: Systematic gap identification and prioritization
- **Quality Assurance**: Protocol adherence and reproducibility validation
- **Meta-Reviewer**: AMSTAR 2 quality assessment for systematic reviews
- **Code Reviewer**: Reproducibility and correctness validation for research code

### 11 Comprehensive Tutorials (280KB Content)
1. Getting Started (15 min)
2. Systematic Literature Review with PRISMA 2020 (60 min)
3. Experimental Design with NIH Rigor Standards (90 min)
4. Statistical Analysis and Reproducibility (120 min)
5. Manuscript Writing and Publication (90 min)
6. Multi-Site Clinical Trials (180 min)
7. Mixed Methods Research (150 min)
8. Grant Proposal Writing (NIH R01) (120 min)
9. Qualitative Research Methods (120 min)
10. Meta-Analysis and Evidence Synthesis (150 min)
11. Implementation Science (240 min)

### 10 Ready-to-Use Templates
- Systematic Review (PRISMA 2020)
- Randomized Controlled Trial (CONSORT)
- Observational Study (STROBE)
- PhD Dissertation (8 chapters)
- Scoping Review (PRISMA-ScR)
- Network Meta-Analysis
- Pragmatic Clinical Trial
- Quality Improvement Study
- Computational Methods Paper
- Advisor Communication Templates

### 3 MCP Servers
- **Literature Search**: Multi-database search (Semantic Scholar, arXiv, PubMed, OpenAlex)
- **Citation Management**: BibTeX/Zotero integration, retraction checking via Crossref
- **Research Database**: Structured storage for systematic review data with SQLite/PostgreSQL

### 6 Lifecycle Hooks + Git Pre-Commit
- **SessionStart**: Load research protocols and mode configuration
- **UserPromptSubmit**: Validate research scope
- **PreToolUse**: Security validation (blocks dangerous bash commands)
- **PostToolUse**: Tool usage logging and DVC auto-tracking for large files
- **PreCompact**: Backup research state before context compression
- **Stop**: Validate phase completion and archive artifacts
- **gitPreCommit**: AI-check validation before commits

---

## Who Should Use This Plugin

### Perfect For:
- **PhD Students**: Complete dissertation workflows from proposal to defense
- **Postdoctoral Researchers**: Systematic reviews and meta-analyses
- **Clinical Researchers**: RCT design and CONSORT-compliant reporting
- **Academic PIs**: Grant writing (NIH R01/R21) and study oversight
- **Systematic Reviewers**: PRISMA 2020 compliant reviews with automation
- **Implementation Scientists**: RE-AIM/CFIR frameworks and mixed methods

### Use Cases:
- Conducting PRISMA 2020 systematic literature reviews
- Designing experiments with NIH rigor standards
- Performing reproducible statistical analyses
- Writing manuscripts following reporting guidelines
- Developing NIH grant proposals (R01, R21, K awards)
- Meta-analysis and evidence synthesis
- Qualitative research and thematic analysis
- Mixed methods research integration
- Multi-site clinical trial management
- AI-detection in academic writing

---

## Requirements

### Minimum Requirements:
- Claude Code installed
- No additional dependencies for basic functionality

### Recommended:
- Python 3.8+ (for MCP servers and advanced features)
- Git (for version control features)
- LaTeX (for manuscript compilation, optional)
- R 4.0+ (for meta-analysis tutorials, optional)

### Optional API Keys:
- PubMed API key (for literature searches, free)
- OpenAlex/Semantic Scholar (for cross-disciplinary searches, free)
- OpenCitations token (for citation verification, free)

**Note:** All API keys are optional. Plugin works without them using local tools.

---

## Installation

### Quick Start (Recommended)

**Option 1: GitHub Marketplace (Current)**
```bash
# In Claude Code
/plugin marketplace add https://github.com/astoreyai/ai_scientist
/plugin install research-assistant
```

**Option 2: Local Development**
```bash
# Clone and open in Claude Code
git clone https://github.com/astoreyai/ai_scientist.git
cd ai_scientist
claude-code .
```

**Verification:**
```bash
# In Claude Code, check installation
/skill list        # Should show 22 skills
/agent list        # Should show 10 agents
```

### Full Installation Guide

See `INSTALLATION.md` for complete setup including:
- Python dependency installation
- MCP server configuration
- API key setup (.env.template provided)
- Troubleshooting common issues

**Time Required:** 5 minutes (quick) to 30 minutes (full setup with MCP servers)

---

## Quick Start Guide

### 1. Verify Installation
```bash
/skill list    # See all 22 skills
/agent list    # See all 10 agents
```

### 2. Run AI-Check on a Document
```bash
# In Claude Code
"Please run ai-check on my_manuscript.tex"
```

### 3. Start a Systematic Review
```bash
/agent literature-reviewer

"I need to conduct a systematic review on mindfulness interventions
for anxiety in adults. Help me get started."
```

### 4. Calculate Sample Size
```bash
"I need sample size for an RCT:
- Design: Independent groups t-test
- Effect size: d = 0.5
- Power: 0.80, Alpha: 0.05"
```

### 5. Design an Experiment
```bash
/agent experiment-designer

"Help me design a randomized controlled trial testing a new
cognitive intervention for memory improvement."
```

---

## Documentation

### Included Documentation (7 files):
- **README.md**: Comprehensive overview (543 lines)
- **INSTALLATION.md**: Detailed setup guide (15-30 min)
- **TROUBLESHOOTING.md**: Diagnostics and solutions (712 lines)
- **CONTRIBUTING.md**: Developer guidelines (267 lines)
- **SECURITY.md**: Vulnerability reporting
- **CHANGELOG.md**: Complete version history (720 lines)
- **QUICK_START.md**: 5-minute quickstart

### Online Resources:
- GitHub: https://github.com/astoreyai/ai_scientist
- Issues: https://github.com/astoreyai/ai_scientist/issues
- Discussions: https://github.com/astoreyai/ai_scientist/discussions

---

## Support

### Getting Help:
1. **TROUBLESHOOTING.md**: Check the comprehensive troubleshooting guide first
2. **GitHub Issues**: Report bugs or request features
3. **GitHub Discussions**: Ask questions and share experiences
4. **Email**: aaron@astoreyai.com

### Response Time:
- Critical bugs: 24-48 hours
- General issues: 2-5 business days
- Feature requests: Triaged weekly

---

## Quality Standards

### Testing:
- 116 automated tests
- 57% code coverage
- Security-validated hooks
- JSON schema validation
- YAML frontmatter validation

### Security:
- No hardcoded secrets
- Environment variables for API keys
- Dangerous command blocking
- Path traversal prevention
- File operations restricted to project scope

### Compliance:
- PRISMA 2020 reporting standards
- NIH rigor and reproducibility requirements
- CONSORT/STROBE guidelines
- OSF pre-registration standards
- FAIR data principles

---

## Roadmap

### v1.3.0 (Planned - Q1 2025)
- Enhanced literature search (PubMed Central full-text)
- Automated citation extraction from PDFs
- Grant budget calculator
- Expanded qualitative analysis tools
- GRADE evidence assessment

### v1.4.0 (Planned - Q2 2025)
- Interactive PRISMA diagram builder
- REDCap integration for data collection
- Automated systematic review screening
- Enhanced meta-analysis visualizations
- Protocol deviation tracking

### v2.0.0 (Planned - Q3 2025)
- Web dashboard for team collaboration
- Real-time inter-rater reliability calculation
- Automated manuscript submission workflows
- Integration with institutional repositories
- Publication impact tracking

---

## License

MIT License - Free for academic, commercial, and personal use.

See LICENSE file for full terms.

---

## Contributing

Contributions welcome! See CONTRIBUTING.md for:
- Development setup
- Code style guidelines
- Pull request process
- Testing requirements
- Documentation standards

---

## Citation

If you use this plugin in your research, please cite:

```bibtex
@software{storey2024research_assistant,
  author = {Storey, Aaron},
  title = {Research Assistant: Claude Code Plugin for Academic Research Workflows},
  year = {2024},
  version = {1.2.0-beta3},
  url = {https://github.com/astoreyai/ai_scientist},
  license = {MIT}
}
```

---

## Acknowledgments

Built with Claude Code by Anthropic.

Follows standards from:
- PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)
- NIH (National Institutes of Health rigor and reproducibility guidelines)
- CONSORT (Consolidated Standards of Reporting Trials)
- Cochrane Collaboration
- EQUATOR Network

---

**Plugin Version:** 1.2.0-beta3
**Last Updated:** 2025-11-11
**Marketplace Status:** ✅ Ready for Distribution (100/100)
