# Changelog

All notable changes to the Research Assistant plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-09

### Added
- Initial release of Research Assistant plugin for Claude Code
- 10 specialized research agents:
  - literature-reviewer - PRISMA 2020 systematic reviews
  - experiment-designer - NIH-compliant experimental design
  - data-analyst - Reproducible statistical analysis
  - hypothesis-generator - Tree-of-Thought hypothesis generation
  - manuscript-writer - Reporting guideline-compliant writing
  - citation-manager - Citation management and verification
  - gap-analyst - Literature gap identification
  - quality-assurance - Comprehensive QA validation
  - meta-reviewer - Cross-phase synthesis
  - code-reviewer - Code quality and security review
  
- 6 core research skills:
  - ai-check - Comprehensive AI-generated text detection
  - citation-format - Multi-style citation formatting
  - power-analysis - Statistical power calculations
  - effect-size - Effect size calculations and interpretation
  - prisma-diagram - PRISMA 2020 flow diagram generation
  - hypothesis-test - Statistical test selection and interpretation
  
- AI-check feature with 4-way integration:
  - Standalone skill for manual checking
  - Pre-commit hook to block AI-generated text
  - Quality assurance integration
  - Manuscript writer agent integration
  
- Complete AI-detection library:
  - Grammar pattern analysis
  - Sentence uniformity detection
  - Paragraph structure analysis
  - AI-typical word frequency checking
  - Punctuation pattern detection
  - Suggestion generation
  - Historical tracking database
  
- Pre-commit hook for AI-detection
- CLI tool for AI-detection (tools/ai_check.py)
- Configuration system (.ai-check-config.yaml)
- Research workflow hooks:
  - Session start hook
  - Pre-tool security validation
  - Post-tool logging
  - Pre-compact backup
  - Stop validation
  
- Comprehensive documentation
- MIT License
- Plugin marketplace distribution support

### Changed
- N/A (initial release)

### Deprecated
- N/A (initial release)

### Removed
- N/A (initial release)

### Fixed
- N/A (initial release)

### Security
- Pre-tool security validation for bash commands
- Path traversal prevention
- AI-detection to ensure authentic academic writing

---

## Future Releases

### [1.1.0] - Planned
- Additional 16 specialized skills
- MCP server packages (literature-search, citation-management, research-database)
- Enhanced documentation
- Example research project templates
- Interactive tutorials

### [1.2.0] - Planned
- Integration with Zotero and Mendeley
- Advanced statistical analysis workflows
- Automated PRISMA checklist validation
- LaTeX template library
