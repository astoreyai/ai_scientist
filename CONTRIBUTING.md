# Contributing to Research Assistant

Thank you for your interest in contributing to the Research Assistant plugin for Claude Code!

## Ways to Contribute

### Reporting Issues
- Use the GitHub issue tracker
- Provide clear reproduction steps
- Include your environment details (OS, Claude Code version)
- Attach relevant error messages or logs

### Suggesting Enhancements
- Check existing issues to avoid duplicates
- Clearly describe the use case and expected benefit
- Consider if it fits the project's research-focused scope

### Contributing Code

#### Before You Start
1. Fork the repository
2. Create a feature branch from `main`
3. Review the codebase structure (see README.md)
4. Ensure you have Python 3.11+ and required dependencies

#### Development Guidelines

**Code Quality:**
- Follow PEP 8 style guide for Python code
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Keep functions focused and under 50 lines when possible

**Testing:**
- Add tests for new features in `tests/`
- Maintain test coverage above 80%
- Run full test suite before submitting: `pytest`
- Ensure all tests pass

**Documentation:**
- Update README.md if adding user-facing features
- Update CHANGELOG.md with your changes
- Add docstrings and inline comments for complex logic
- Update relevant tutorial or template documentation

**Research Standards:**
- Follow PRISMA 2020 guidelines for literature review features
- Follow NIH rigor standards for experimental design features
- Cite sources for statistical methods or research protocols
- Ensure reproducibility of any analysis code

#### Pull Request Process

1. **Update Documentation**
   - README.md for feature changes
   - CHANGELOG.md under "Unreleased" section
   - Relevant tutorials or templates

2. **Run Quality Checks**
   ```bash
   # Run tests
   pytest tests/ --cov=code --cov-report=html

   # Check code style
   ruff check .
   black --check .

   # Validate hooks (if modified)
   python .claude/hooks/pre-tool-security.py --test
   ```

3. **Commit Message Format**
   Use conventional commits:
   - `feat:` new feature
   - `fix:` bug fix
   - `docs:` documentation only
   - `test:` adding/updating tests
   - `refactor:` code refactoring
   - `chore:` maintenance tasks

   Example: `feat: add power analysis calculator to experiment-design skill`

4. **Submit PR**
   - Provide clear description of changes
   - Reference any related issues
   - Explain design decisions if non-obvious
   - Add screenshots for UI changes (if applicable)

5. **Code Review**
   - Address reviewer feedback promptly
   - Keep commits atomic and well-described
   - Squash commits if requested

### Contributing Tutorials

We welcome new research methodology tutorials!

**Tutorial Guidelines:**
- Follow existing tutorial structure (see `tutorials/` directory)
- Include real examples with data
- Provide code snippets users can adapt
- Cover both theory and practical application
- Include troubleshooting section
- Cite academic sources
- Target 8,000-15,000 words (20-40 pages)

**Tutorial Template:**
```markdown
# [Tutorial Number]. [Topic]

## Overview
[Research area, who should use this, time to complete]

## Learning Objectives
[What users will be able to do]

## Prerequisites
[Required knowledge, software, data]

## Core Concepts
[Theoretical foundation]

## Step-by-Step Guide
[Practical implementation]

## Real Example
[Complete worked example with data]

## Common Issues
[Troubleshooting guide]

## Additional Resources
[Citations, further reading]
```

### Contributing Templates

Research project templates must be:
- Generic (no personal research content)
- Well-documented with README.md
- Include folder structure guidance
- Provide example files where helpful
- Follow research best practices

### Contributing Skills

Skills extend Claude Code's capabilities for specific tasks.

**Skill Requirements:**
- Clear, focused purpose (one task done well)
- Proper frontmatter in SKILL.md:
  ```yaml
  ---
  name: skill-name
  description: "Clear one-line description"
  ---
  ```
- Detailed usage instructions
- Examples of input/output
- Error handling guidance

**Skills Directory:**
Place skills in `skills/[skill-name]/SKILL.md`

### Code of Conduct

**Be Respectful:**
- Treat all contributors with respect
- Provide constructive feedback
- Focus on ideas, not individuals
- Welcome diverse perspectives

**Academic Integrity:**
- Properly cite sources
- Don't plagiarize code or documentation
- Respect licensing of dependencies
- Maintain scientific rigor

**Privacy & Security:**
- Never commit API keys or credentials
- Don't include personal research data
- Follow data protection best practices
- Report security issues privately (see SECURITY.md)

## Development Setup

### Prerequisites
- Python 3.11 or higher
- Git
- Claude Code (latest version)
- Virtual environment tool (venv)

### Setup Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/astoreyai/ai_scientist.git
   cd ai_scientist
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Run Tests**
   ```bash
   pytest tests/
   ```

5. **Install Plugin in Claude Code**
   ```bash
   # Add to .claude/settings.json in your test project:
   {
     "plugins": [
       {
         "source": "/path/to/ai_scientist",
         "name": "research-assistant"
       }
     ]
   }
   ```

## Project Structure

```
research-assistant/
├── .claude/                    # Claude Code configuration
│   ├── agents/                 # Specialized agents
│   ├── hooks/                  # Workflow hooks
│   └── settings.json           # Plugin settings
├── .claude-plugin/             # Plugin metadata
│   ├── plugin.json             # Plugin definition
│   └── marketplace.json        # Marketplace listing
├── code/                       # Core Python modules
│   ├── data_management/        # DVC, MLflow, git workflows
│   └── quality_assurance/      # QA validators
├── docs/                       # Technical documentation
├── mcp-servers/                # MCP server implementations
├── skills/                     # Claude Code skills (22 total)
├── templates/                  # Research project templates (10)
├── tests/                      # Test suite
├── tools/                      # Standalone research tools
└── tutorials/                  # Research methodology guides (11)
```

## Getting Help

- **Documentation**: See `/docs` directory
- **Examples**: Check `/tutorials` for guided examples
- **Issues**: Search existing issues on GitHub
- **Discussions**: Use GitHub Discussions for questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License (see LICENSE file).

---

**Thank you for helping improve research workflows for PhD students and academics worldwide!**
