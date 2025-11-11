# Research Assistant for Claude Code

**Professional research workflow automation for PhD students and academics**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://claude.com/code)
[![Version](https://img.shields.io/badge/version-1.2.0--beta3-green)](CHANGELOG.md)

---

## Overview

A comprehensive Claude Code plugin that transforms academic research workflows with **11 interactive tutorials**, **10 research templates**, specialized agents, and AI-detection capabilities. Designed for PhD students, researchers, and academics conducting systematic reviews, experimental studies, meta-analyses, and writing rigorous manuscripts.

**Total Learning Content**: 280KB, 8 hours of comprehensive research training

---

## What's New in v1.2.0-beta3

- **3 New Advanced Tutorials**: Qualitative Research, Meta-Analysis, Implementation Science (105KB)
- **4 New Specialized Templates**: Scoping Review, Network Meta-Analysis, Pragmatic Trial, Quality Improvement
- **Comprehensive Research Coverage**: Quantitative, qualitative, mixed methods, evidence synthesis, and implementation science
- **Real-World Examples**: Every tutorial includes complete worked examples with data

---

## Quick Start

\`\`\`bash
# Clone the repository
git clone https://github.com/astoreyai/ai_scientist.git
cd ai_scientist

# Start with Tutorial 1
cat tutorials/01_getting_started/README.md

# Use a specialized agent
/agent literature-reviewer

# Use a research template
cp -r templates/systematic_review/ my_project/
\`\`\`

---

## Tutorials (11 Total, 280KB)

### Foundation Tutorials (1-5)
**Tutorial 1: Getting Started** (8.5KB, 15 minutes)
- Plugin basics and workflow overview
- Understanding research protocols
- Quick start examples

**Tutorial 2: Literature Review** (28KB, 45 minutes)
- PRISMA 2020 systematic review workflow
- Multi-database search strategies
- Screening and data extraction
- Risk of bias assessment
- Complete workflow from protocol to PRISMA diagram

**Tutorial 3: Experimental Design** (29KB, 40 minutes)
- NIH rigor and reproducibility standards
- Power analysis and sample size calculation
- Randomization protocols
- CONSORT compliance
- Pre-registration with OSF

**Tutorial 4: AI-Check Deep Dive** (18KB, 30 minutes)
- Detecting AI-generated text patterns
- Integration modes (standalone, pre-commit, QA, manuscript)
- Interpretation and improvement strategies

**Tutorial 5: Complete Workflow** (32KB, 60 minutes)
- End-to-end research project: idea → publication
- Decision gates and quality checkpoints
- Real example: RCT on meditation for anxiety

### Specialized Research Tutorials (6-8)
**Tutorial 6: Multi-Site Trials** (27KB, 50 minutes)
- Consortium coordination and governance
- Central vs. local IRB considerations
- Data harmonization across sites
- Statistical approaches (fixed vs. random effects)

**Tutorial 7: Mixed Methods Research** (28KB, 55 minutes)
- Convergent, sequential, and embedded designs
- Qualitative + quantitative integration
- Joint display tables and visual integration
- GRAM checklist compliance

**Tutorial 8: Grant Proposals** (31KB, 60 minutes)
- NIH R01 proposal structure
- Specific Aims development
- Significance, Innovation, Approach sections
- Budget justification and human subjects

### Advanced Methods Tutorials (9-11) - NEW in beta3
**Tutorial 9: Qualitative Research** (26KB, 50 minutes)
- Grounded theory, phenomenology, ethnography
- Charmaz constructivist grounded theory
- Purposive and theoretical sampling
- In-depth interview development
- Constant comparison analysis (NVivo workflow)
- Trustworthiness criteria (Lincoln & Guba)
- COREQ 32-item checklist compliance

**Tutorial 10: Meta-Analysis Deep Dive** (24KB, 55 minutes)
- Fixed vs. random effects model selection
- Effect size calculation (SMD, MD, RR, OR)
- Forest plot creation and interpretation
- Heterogeneity assessment (Q, I², τ²)
- Subgroup analysis and meta-regression
- Publication bias detection (funnel plots, Egger's test)
- R metafor package with complete code
- PRISMA-MA checklist

**Tutorial 11: Implementation Science** (55KB, 55 minutes)
- RE-AIM framework (Reach, Effectiveness, Adoption, Implementation, Maintenance)
- CFIR assessment (5 domains, 39 constructs)
- ERIC implementation strategies (73 strategies)
- Hybrid effectiveness-implementation designs
- Proctor's 8 implementation outcomes
- Adaptation vs. fidelity tension
- Real example: TF-CBT in community clinics

---

## Research Templates (10 Total)

### Evidence Synthesis Templates
**Systematic Review Template**
- PRISMA 2020 compliance (27-item checklist)
- Complete protocol template
- Search strategy documentation
- Risk of bias assessment tools
- Data extraction forms

**Scoping Review Template** - NEW in beta3
- Arksey & O'Malley framework
- PRISMA-ScR compliance (22-item checklist)
- PCC framework (Population, Concept, Context)
- 5-stage iterative methodology
- Evidence mapping and gap analysis

**Network Meta-Analysis Template** - NEW in beta3
- Mixed treatment comparisons with ranking
- Network geometry visualization
- Consistency assessment (node-splitting)
- R netmeta package code
- PRISMA-NMA checklist (32 items)
- SUCRA/P-scores for treatment ranking
- League tables for all comparisons

### Experimental Design Templates
**RCT Study Template**
- CONSORT 2010 compliance
- Randomization sequence generation
- Allocation concealment
- Complete trial protocol
- Analysis plan template

**Observational Study Template**
- STROBE checklist compliance
- Exposure and outcome definitions
- Confounder identification
- Statistical analysis plan

**Pragmatic Trial Template** - NEW in beta3
- PRECIS-2 tool (9-domain scoring)
- Real-world effectiveness focus
- CONSORT extension for pragmatic trials
- Strict intention-to-treat analysis
- Patient-important outcomes

### Specialized Methods Templates
**Computational Methods Template**
- Algorithm development and validation
- Reproducibility standards
- Performance evaluation metrics
- Code documentation standards

**Quality Improvement Template** - NEW in beta3
- Model for Improvement (PDSA cycles)
- SMART aim statement development
- Key driver diagram creation
- Statistical process control (SPC) charts
- R qicharts2 package code
- SQUIRE 2.0 reporting (18 items)
- Real example: Pressure injury reduction

### Academic Development Templates
**PhD Dissertation Template**
- Chapter structure and organization
- Dissertation planning timeline
- Committee meeting agendas
- Defense preparation checklist

**Advisor Communication Template**
- Meeting agenda templates
- Progress report formats
- Milestone tracking
- Publication planning

---

## Specialized Agents (10)

### Literature & Evidence Synthesis
- **literature-reviewer** - PRISMA 2020 systematic reviews, multi-database searches
- **meta-reviewer** - Quality assessment of reviews (AMSTAR 2)
- **gap-analyst** - Systematic gap identification and prioritization

### Experimental Design & Analysis
- **experiment-designer** - NIH-rigorous experimental design, power analysis
- **data-analyst** - Reproducible statistical analysis with effect sizes
- **hypothesis-generator** - Tree-of-Thought hypothesis generation

### Writing & Documentation
- **manuscript-writer** - CONSORT/PRISMA-compliant manuscripts
- **citation-manager** - BibTeX/Zotero, retraction checking

### Quality & Review
- **quality-assurance** - Protocol adherence, reproducibility validation
- **code-reviewer** - Statistical code review for correctness

---

## Key Features

### Research Protocols & Standards
- **PRISMA 2020** - Systematic review reporting
- **CONSORT** - RCT reporting standard
- **STROBE** - Observational study reporting
- **SQUIRE 2.0** - Quality improvement reporting
- **COREQ** - Qualitative research reporting
- **NIH Rigor Standards** - Reproducibility requirements
- **PRECIS-2** - Pragmatic trial assessment

### AI-Check System
Detect AI-generated text patterns to ensure authentic academic writing:

**Detection Methods:**
- Grammar perfection patterns
- Sentence uniformity analysis (15-25 word uniformity)
- AI-typical vocabulary ("delve", "leverage", "robust", etc.)
- Style consistency flags

**Integration Modes:**
- Standalone analysis: \`python tools/ai_check.py manuscript.tex\`
- Pre-commit hook: Automatically blocks high-AI commits
- QA integration: Part of quality assurance workflow
- Manuscript review: Section-by-section analysis

**Confidence Levels:**
- 0-30%: Likely human
- 30-70%: Possible AI assistance
- 70-100%: Likely AI-generated

### Reproducibility Tools
- **Git Integration** - Version control for research
- **DVC (Data Version Control)** - Large dataset tracking
- **MLflow** - Experiment tracking and logging
- **Docker** - Containerized analysis environments
- **Pre-registration** - OSF integration templates

---

## Research Coverage

**Quantitative Methods**
- RCTs, observational studies, meta-analysis, network meta-analysis

**Qualitative Methods**
- Grounded theory, phenomenology, ethnography, qualitative synthesis

**Mixed Methods**
- Convergent, sequential, embedded designs with integration

**Evidence Synthesis**
- Systematic reviews, scoping reviews, meta-analysis, network meta-analysis

**Implementation Science**
- RE-AIM, CFIR, ERIC strategies, hybrid designs

**Quality Improvement**
- PDSA cycles, statistical process control, sustainability

**Real-World Effectiveness**
- Pragmatic trials, PRECIS-2 assessment

**Grant Writing**
- NIH R01 proposals, specific aims, significance/innovation/approach

**Multi-Site Research**
- Consortium coordination, data harmonization

---

## Installation

### From GitHub
\`\`\`bash
# Clone repository
git clone https://github.com/astoreyai/ai_scientist.git
cd ai_scientist

# Optional: Set up Python environment for MCP servers
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

### MCP Servers
Three MCP servers are included for enhanced functionality:
- **literature-search** - Multi-database literature searches
- **citation-manager** - BibTeX/Zotero integration, retraction checking
- **research-db** - Structured data storage for systematic reviews

See \`mcp-servers/README.md\` for installation instructions.

---

## Usage

### Tutorial Learning Path
1. Start with **Tutorial 1** (Getting Started) - Understand plugin basics
2. Follow **Tutorial 2** (Literature Review) - Learn PRISMA workflow
3. Try **Tutorial 3** (Experimental Design) - Master NIH standards
4. Complete **Tutorial 5** (Complete Workflow) - End-to-end example
5. Explore specialized tutorials based on your research needs

### Using Templates
\`\`\`bash
# Copy a template to your project
cp -r templates/systematic_review/ my_systematic_review/
cd my_systematic_review/

# Follow the template README
cat README.md

# Use the provided checklists and forms
ls *.md *.csv
\`\`\`

### Working with Agents
\`\`\`bash
# Launch specialized agent
/agent literature-reviewer

# Or use via Claude Code task delegation
# Claude Code will automatically delegate complex multi-step tasks
# to specialized agents when appropriate
\`\`\`

### AI-Check Integration
\`\`\`bash
# Standalone check
python tools/ai_check.py manuscript.tex

# Enable pre-commit hook
cp hooks/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit

# Check specific sections
python tools/ai_check.py manuscript.tex --section introduction
\`\`\`

---

## Documentation

- **Tutorials**: See \`tutorials/\` directory (11 comprehensive tutorials)
- **Templates**: See \`templates/\` directory (10 research templates)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md) - Complete version history
- **License**: [LICENSE](LICENSE) - MIT License
- **Installation Guide**: \`docs/INSTALLATION.md\`
- **User Guide**: \`docs/USER_GUIDE.md\`

---

## Requirements

- **Claude Code** - Latest version recommended
- **Python 3.8+** - For MCP servers and tools (optional)
- **R 4.0+** - For meta-analysis templates (optional)
- **Git** - For version control
- **LaTeX** - For PDF generation (optional)

---

## Project Structure

\`\`\`
ai_scientist/
├── tutorials/           # 11 interactive tutorials (280KB)
│   ├── 01_getting_started/
│   ├── 02_literature_review/
│   ├── 03_experimental_design/
│   ├── 04_ai_check/
│   ├── 05_complete_workflow/
│   ├── 06_multisite_trials/
│   ├── 07_mixed_methods/
│   ├── 08_grant_proposals/
│   ├── 09_qualitative_research/
│   ├── 10_meta_analysis/
│   └── 11_implementation_science/
│
├── templates/           # 10 research templates
│   ├── systematic_review/
│   ├── scoping_review/
│   ├── network_meta_analysis/
│   ├── rct_study/
│   ├── observational_study/
│   ├── pragmatic_trial/
│   ├── computational_methods/
│   ├── quality_improvement/
│   ├── phd_dissertation/
│   └── advisor_communication/
│
├── code/                # Core plugin code
│   ├── orchestrator.py
│   ├── research_workflow.py
│   ├── quality_assurance/
│   └── validators/
│
├── mcp-servers/         # MCP server implementations
│   ├── literature/
│   ├── citations/
│   └── research_db/
│
├── tests/               # Comprehensive test suite (116 tests, 57% coverage)
├── automation/          # Setup and build scripts
├── hooks/               # Pre-commit hooks (AI-check)
└── .claude/             # Claude Code configuration
\`\`\`

---

## Testing

\`\`\`bash
# Run full test suite
pytest

# Run with coverage
pytest --cov=code --cov-report=html

# View coverage report
open htmlcov/index.html
\`\`\`

**Current Test Coverage**: 57% (116 tests passing)

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (\`git checkout -b feature/amazing-feature\`)
3. Write tests for new functionality
4. Ensure all tests pass (\`pytest\`)
5. Commit changes with clear messages
6. Push to your fork
7. Open a Pull Request

See \`CONTRIBUTING.md\` for detailed guidelines (coming soon).

---

## Roadmap

### v1.2.0 Final Release
- Complete documentation review
- External user testing
- Security audit
- PyPI package distribution (optional)

### v1.3.0 (Planned)
- Additional tutorials (12-15): Machine learning, causal inference, Bayesian methods
- Template expansions: Case-control studies, cross-sectional surveys
- Enhanced MCP server capabilities
- Continuous integration workflows

### v2.0.0 (Future)
- Full autonomous research mode
- Interactive web dashboard
- Collaborative multi-user workflows
- Integration with additional reference managers

---

## Citation

If you use this plugin in your research, please cite:

\`\`\`bibtex
@software{research_assistant_2024,
  author = {Storey, Aaron},
  title = {Research Assistant for Claude Code},
  year = {2024},
  version = {1.2.0-beta3},
  url = {https://github.com/astoreyai/ai_scientist}
}
\`\`\`

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/astoreyai/ai_scientist/issues)
- **Email**: aaron@astoreyai.com
- **Discussions**: [GitHub Discussions](https://github.com/astoreyai/ai_scientist/discussions)

---

## Acknowledgments

This plugin implements research standards and reporting guidelines from:
- PRISMA 2020 (Page et al., 2021)
- CONSORT (Schulz et al., 2010)
- NIH Rigor and Reproducibility Guidelines
- RE-AIM Framework (Glasgow et al., 1999)
- CFIR (Damschroder et al., 2009)
- PRECIS-2 (Loudon et al., 2015)
- SQUIRE 2.0 (Ogrinc et al., 2016)
- COREQ (Tong et al., 2007)

Special thanks to the research methods community for developing these invaluable standards.

---

**Professional research workflow automation for academics**

**Version**: 1.2.0-beta3 | **Last Updated**: 2024-11-10 | **Total Content**: 280KB tutorials + 10 templates
