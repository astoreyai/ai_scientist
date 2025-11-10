# Research Assistant for Claude Code

**Professional research workflow automation for PhD students and academics**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://claude.com/code)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](CHANGELOG.md)

---

## Overview

A comprehensive Claude Code plugin that transforms academic research workflows with specialized agents, research methodology skills, and AI-detection capabilities. Designed for PhD students, researchers, and academics conducting systematic reviews, experimental studies, and writing manuscripts.

## Key Features

- **10 Specialized Agents** for research workflows (literature review, experimental design, data analysis, manuscript writing)
- **22+ Research Skills** including AI-detection, power analysis, citation formatting, PRISMA diagrams
- **AI-Check System** with 4-way integration (standalone, pre-commit hook, QA, manuscript review)
- **PRISMA 2020 & NIH Rigor Compliance** for systematic reviews and experimental design
- **Reproducibility Standards** with Git, DVC, and MLflow integration
- **6 Workflow Hooks** for automation and validation

## Quick Start

```bash
# Install plugin
/plugin marketplace add astoreyai/ai_scientist
/plugin install research-assistant@research-assistant-marketplace

# Use an agent
/agent literature-reviewer

# Run AI-check
python tools/ai_check.py manuscript.tex
```

## AI-Check Feature

Detect AI-generated text patterns to ensure authentic academic writing:

- **Grammar perfection detection** - Identifies excessive perfection
- **Sentence uniformity analysis** - Flags uniform 15-25 word sentences  
- **AI-typical word checking** - Detects "delve", "leverage", "robust", etc.
- **Pre-commit hook** - Automatically blocks commits with high AI confidence
- **Improvement suggestions** - Provides specific recommendations

**Confidence Levels:**
- 0-30%: Likely human ✅
- 30-70%: Possible AI assistance ⚠️
- 70-100%: Likely AI-generated 🚫

## What's Included

### Agents (10)
- literature-reviewer, experiment-designer, data-analyst
- hypothesis-generator, manuscript-writer, citation-manager
- gap-analyst, quality-assurance, meta-reviewer, code-reviewer

### Skills (6 core + 16 specialized)
- ai-check, citation-format, power-analysis, effect-size
- prisma-diagram, hypothesis-test, research-questions
- literature-gap, synthesis-matrix, inclusion-criteria
- ...and 12 more

### Hooks (7)
- SessionStart, UserPromptSubmit, PreToolUse, PostToolUse
- PreCompact, Stop, gitPreCommit (AI-check)

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [User Guide](docs/USER_GUIDE.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

## License

MIT License - see [LICENSE](LICENSE) file

## Support

- Issues: https://github.com/astoreyai/ai_scientist/issues
- Email: aaron@astoreyai.com

---

**Made with ❤️ for researchers, by researchers**
