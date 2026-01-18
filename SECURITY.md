# Security Policy

## Supported Versions

We release security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.2.x   | :white_check_mark: |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

We take security seriously. If you discover a security vulnerability in the Research Assistant plugin, please report it privately.

### How to Report

**Email:** aaron@astoreyai.com

**Subject Line:** `[SECURITY] Research Assistant - [Brief Description]`

**Information to Include:**

1. **Type of vulnerability** (e.g., command injection, path traversal, XSS, etc.)
2. **Affected component** (e.g., hook script, MCP server, skill, etc.)
3. **Steps to reproduce** the vulnerability
4. **Potential impact** (what an attacker could accomplish)
5. **Suggested fix** (if you have one)
6. **Your contact information** (for follow-up questions)

### What to Expect

- **Acknowledgment:** Within 48 hours of your report
- **Initial Assessment:** Within 5 business days
- **Status Updates:** Every 7 days until resolved
- **Resolution:** Security fixes will be released as soon as possible
- **Credit:** You will be credited in the security advisory (unless you prefer to remain anonymous)

### Security Updates

Security updates will be:
- Released as patch versions (e.g., 1.2.1)
- Announced in CHANGELOG.md
- Tagged in GitHub releases
- Mentioned in README.md if critical

### Our Commitment

We commit to:
- Respond promptly to security reports
- Keep you informed throughout the process
- Credit reporters appropriately
- Disclose vulnerabilities responsibly after patching

## Security Best Practices for Users

### API Keys and Credentials

**Never commit API keys or credentials to version control:**

```bash
# Store in environment variables
export SCOPUS_API_KEY="your-key-here"
export SEMANTIC_SCHOLAR_API_KEY="your-key-here"

# Or use .env files (already in .gitignore)
echo "SCOPUS_API_KEY=your-key-here" > .env
```

### Hook Security

The `.claude/hooks/pre-tool-security.py` hook validates commands before execution:

**Blocked Operations:**
- Destructive commands (`rm -rf /`, `dd`, `mkfs`)
- System path modifications (`/etc`, `/sys`, `/boot`)
- Privilege escalation (`sudo`, `su`)
- Network exploits (reverse shells, pipe-to-bash)

**Allowed Operations:**
- File operations within project directory
- Safe bash commands for research tasks
- Read operations on non-sensitive paths

### File Operations

The plugin restricts file operations to:
- Project directory
- User home directory (`.cache`, `.config`)
- Temporary directories (`/tmp`, `/var/tmp`)

System directories are protected by the security hook.

### Network Access

MCP servers and tools that access external APIs:

**Literature Search (Scopus, Semantic Scholar, PubMed):**
- Use official APIs with rate limiting
- API keys stored in configuration files (not in code)
- Requests are logged for audit trails

**Citation Verification (OpenCitations, Crossref):**
- Read-only API access
- No authentication required for these services
- Rate limits respected

### Python Code Execution

When running analysis scripts:

```bash
# Use virtual environment to isolate dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run scripts in sandboxed environment
python code/analysis/your_script.py
```

### Docker Isolation

For maximum security, run analysis in Docker:

```dockerfile
FROM python:3.11-slim
WORKDIR /research
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY code/ ./code/
COPY data/ ./data/
CMD ["python", "code/analysis/primary_analysis.py"]
```

## Known Security Considerations

### 1. Bash Command Execution

The plugin can execute bash commands through Claude Code's Bash tool. These are:
- Validated by the pre-tool-security hook
- Logged to `.claude/security.log`
- Blocked if they match dangerous patterns

**User Responsibility:** Review the security hook configuration in `.claude/hooks/pre-tool-security.py`

### 2. File System Access

The plugin can read and write files within allowed directories. Users should:
- Keep sensitive data outside the project directory
- Review `.gitignore` to prevent accidental commits
- Use encryption for sensitive research data

### 3. API Keys in Configuration

Configuration files may contain API keys:
- `tools/literature_review/automated_scopus/config/scopus_config.yaml`
- Other configuration files

**Mitigation:**
- These files are in `.gitignore`
- Use environment variables instead when possible
- Rotate keys regularly
- Use read-only or limited-scope API keys

### 4. Python Code Execution

The plugin includes Python code for analysis and data management:
- All code is open-source and auditable
- No code is downloaded from external sources at runtime
- Virtual environments isolate dependencies

**User Responsibility:** Review code before execution, especially in `code/` and `tools/` directories.

### 5. MCP Server Security

MCP servers run as local services and can:
- Access the file system (within project scope)
- Make network requests (to literature databases)
- Execute database queries (SQLite for research data)

**Mitigation:**
- Servers use read-only credentials where possible
- All requests are logged
- No sensitive data is transmitted to external services without user initiation

## Third-Party Dependencies

We minimize third-party dependencies and regularly audit:

**Python Dependencies:**
- `mlflow` - Experiment tracking (Apache 2.0 license)
- `requests` - HTTP library (Apache 2.0 license)
- `pyyaml` - YAML parsing (MIT license)
- `pydantic` - Data validation (MIT license)

**Dependency Management:**
```bash
# Check for known vulnerabilities
pip install pip-audit
pip-audit

# Or using safety
pip install safety
safety check
```

## Security Audit History

| Date | Auditor | Scope | Findings |
|------|---------|-------|----------|
| 2025-11-11 | Internal | Full codebase review | 1 TODO comment (non-critical) |
| 2025-11-10 | Internal | Pre-distribution security review | API keys properly handled |

## Disclosure Policy

We follow responsible disclosure:

1. **Private Report** → Security researcher reports vulnerability privately
2. **Confirmation** → We confirm and assess the vulnerability
3. **Fix Development** → We develop and test a fix
4. **Patch Release** → We release a patched version
5. **Public Disclosure** → We publicly disclose after users have had time to update (typically 7-14 days)

## Security Hall of Fame

We recognize security researchers who help improve the project:

*No vulnerabilities reported yet*

## Contact

For security concerns: **aaron@astoreyai.com**

For general issues: [GitHub Issues](https://github.com/astoreyai/ai_scientist/issues)

---

**Last Updated:** 2025-11-11
**Version:** 1.2.0-beta3
