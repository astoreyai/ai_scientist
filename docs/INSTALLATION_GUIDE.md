# Research Assistant - Installation Guide

**Version:** 1.2.0-beta3
**Platform Support:** Linux, macOS, Windows (WSL)
**Installation Time:** 5-30 minutes depending on setup

---

## Table of Contents

1. [Quick Installation](#quick-installation)
2. [Full Installation](#full-installation)
3. [Verification](#verification)
4. [Configuration](#configuration)
5. [Optional Components](#optional-components)
6. [Troubleshooting](#troubleshooting)

---

## Quick Installation

### Prerequisites
- Claude Code installed
- Git (for cloning from GitHub)

### Install from GitHub Marketplace

**Step 1: Add Marketplace**
```bash
# In Claude Code
/plugin marketplace add https://github.com/astoreyai/ai_scientist
```

**Step 2: Install Plugin**
```bash
# In Claude Code
/plugin install research-assistant
```

**Step 3: Verify**
```bash
# Check skills loaded
/skill list
# Expected: 22 skills displayed

# Check agents loaded
/agent list
# Expected: 10 agents displayed
```

**Installation Complete!** You can now use all 22 skills and 10 agents.

---

## Full Installation

For users who want MCP servers, Python tools, and full functionality.

### Step 1: Clone Repository

```bash
# Clone to a permanent location
git clone https://github.com/astoreyai/ai_scientist.git
cd ai_scientist
```

### Step 2: Create Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows WSL)
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Expected packages:
# - pyyaml (for YAML parsing)
# - sqlalchemy (for database operations)
# - requests (for API calls)
# - semanticscholar (for literature search)
# - biopython (for PubMed searches)
# - pandas (for data analysis)
# - pytest (for testing)
```

**Note:** Installation takes 2-5 minutes depending on internet speed.

### Step 4: Configure Environment Variables

```bash
# Copy template
cp .env.template .env

# Edit with your API keys (optional)
nano .env  # or vim .env, or your preferred editor
```

**Required for MCP Servers:**
- `PUBMED_EMAIL` - Your email for PubMed searches (free, no API key needed)
- `OPENALEX_EMAIL` - Your email for OpenAlex searches (free)

**Optional API Keys:**
- `PUBMED_API_KEY` - Higher rate limits (free from NCBI)
- `OPENCITATIONS_TOKEN` - Citation verification (free from OpenCitations)

**Getting API Keys:**

1. **PubMed API Key** (Optional, but recommended):
   - Visit: https://www.ncbi.nlm.nih.gov/account/settings/
   - Create account → Settings → API Key Management → Create API Key
   - Add to `.env`: `PUBMED_API_KEY=your_key_here`

2. **OpenCitations Token** (Optional):
   - Visit: https://opencitations.net/
   - Sign up for free account
   - Generate token in dashboard
   - Add to `.env`: `OPENCITATIONS_TOKEN=your_token_here`

### Step 5: Open in Claude Code

```bash
# From the ai_scientist directory
claude-code .
```

Plugin will auto-load from `.claude/settings.json` configuration.

### Step 6: Verify Installation

Run the verification script:

```bash
./automation/pre_distribution_checks.sh
```

**Expected Output:**
```
✅ ALL CHECKS PASSED - READY FOR DISTRIBUTION

Skills: 22/22
Agents: 10/10
Tutorials: 11
Templates: 10
MCP Servers: 6
Hooks: 7/7
```

---

## Verification

### Basic Verification

**1. Check Skills**
```bash
# In Claude Code
/skill list
```

**Expected:** 22 skills including:
- ai-check
- power-analysis
- effect-size
- prisma-diagram
- citation-format
- hypothesis-test
- research-questions
- literature-gap
- synthesis-matrix
- inclusion-criteria
- experiment-design
- data-visualization
- results-interpretation
- irb-protocol
- pre-registration
- randomization
- blinding
- risk-of-bias
- meta-analysis
- sensitivity-analysis
- subgroup-analysis
- publication-prep

**2. Check Agents**
```bash
# In Claude Code
/agent list
```

**Expected:** 10 agents:
- literature-reviewer
- experiment-designer
- data-analyst
- manuscript-writer
- citation-manager
- hypothesis-generator
- gap-analyst
- quality-assurance
- meta-reviewer
- code-reviewer

**3. Test a Skill**
```bash
# Try the AI-check skill
"Run ai-check on this text: This comprehensive study leverages robust methodologies to delve into the relationship between stress and health."
```

**Expected:** AI-detection analysis with confidence score.

**4. Test an Agent**
```bash
# Invoke literature reviewer
/agent literature-reviewer

"I need help starting a systematic review on mindfulness interventions."
```

**Expected:** Agent loads with PRISMA 2020 guidance.

### Advanced Verification

**5. Test Hooks**

Hooks run automatically at lifecycle events:

- **SessionStart**: Runs when you open Claude Code
- **PreToolUse**: Validates bash commands before execution
- **PostToolUse**: Logs tool usage after execution
- **PreCompact**: Backs up state before context compression
- **Stop**: Validates completion when closing
- **gitPreCommit**: Checks for AI text before commits

**To test PreToolUse security hook:**
```bash
# Try a blocked command (should be prevented)
rm -rf /
```

**Expected:** Hook blocks the command with security warning.

**6. Test MCP Servers** (if Python dependencies installed)

```bash
# Test literature search server
cd mcp-servers
python test_mcp_servers_integration.py
```

**Expected:** All MCP server tests pass.

---

## Configuration

### Plugin Configuration

Location: `.claude/settings.json`

**Auto-loading configuration:**
```json
{
  "plugins": [
    {
      "source": "./",
      "name": "research-assistant"
    }
  ]
}
```

This makes the plugin auto-load when Claude Code opens in the `ai_scientist` directory.

### Hook Configuration

Location: `.claude/settings.json`

Pre-configured hooks:
- `SessionStart`: Load research protocols
- `UserPromptSubmit`: Validate research scope
- `PreToolUse`: Security validation for bash commands
- `PostToolUse`: Tool logging and DVC auto-tracking
- `PreCompact`: Backup research state
- `Stop`: Validate completion and archive
- `gitPreCommit`: AI-check validation

**No configuration changes needed** - hooks work out of the box.

### MCP Server Configuration

Location: `mcp-servers/claude_desktop_config.json.template`

**Copy template:**
```bash
cp mcp-servers/claude_desktop_config.json.template ~/.config/claude/claude_desktop_config.json
```

**Edit paths** to match your installation:
```json
{
  "mcpServers": {
    "literature-search": {
      "command": "python",
      "args": ["/path/to/ai_scientist/mcp-servers/literature-search.py"]
    }
  }
}
```

### Environment Variables

Location: `.env` (copy from `.env.template`)

**Basic setup (no API keys):**
```bash
# Minimum required for literature search
PUBMED_EMAIL=your_email@example.com
OPENALEX_EMAIL=your_email@example.com
```

**Full setup (with API keys):**
```bash
# Literature Search APIs
PUBMED_API_KEY=your_pubmed_api_key
PUBMED_EMAIL=your_email@example.com
OPENALEX_EMAIL=your_email@example.com
OPENCITATIONS_TOKEN=your_opencitations_token

# Database (optional, defaults to SQLite)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=research_assistant
DB_USER=research_user
DB_PASSWORD=your_password

# MCP Servers (optional)
MCP_LITERATURE_SEARCH_ENABLED=true
MCP_CITATION_MANAGEMENT_ENABLED=true
MCP_RESEARCH_DATABASE_ENABLED=true
```

---

## Optional Components

### R Installation (for Meta-Analysis Tutorial)

**Ubuntu/Debian:**
```bash
sudo apt-get install r-base
```

**macOS:**
```bash
brew install r
```

**R Packages:**
```r
# In R console
install.packages(c("meta", "metafor", "dmetar"))
```

### LaTeX (for Manuscript Compilation)

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows (WSL):**
```bash
sudo apt-get install texlive-latex-extra
```

### PostgreSQL (for Large Research Databases)

**Ubuntu/Debian:**
```bash
sudo apt-get install postgresql postgresql-contrib
```

**Create database:**
```bash
sudo -u postgres psql
CREATE DATABASE research_assistant;
CREATE USER research_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE research_assistant TO research_user;
```

**Update `.env`:**
```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=research_assistant
DB_USER=research_user
DB_PASSWORD=your_password
```

---

## Troubleshooting

### Plugin Not Loading

**Symptom:** `/skill list` returns empty or error

**Solution 1:** Verify you're in the correct directory
```bash
pwd
# Expected: /path/to/ai_scientist
```

**Solution 2:** Check `.claude/settings.json` exists
```bash
cat .claude/settings.json
```

**Solution 3:** Restart Claude Code
```bash
# Close Claude Code completely
# Reopen in the ai_scientist directory
claude-code .
```

**Solution 4:** Enable debug mode
```bash
claude --debug
# Look for "research-assistant" in startup messages
```

### Skills Not Appearing

**Symptom:** Only some skills load, or none appear

**Check skill count:**
```bash
find skills -name "SKILL.md" | wc -l
# Expected: 22
```

**Validate YAML frontmatter:**
```bash
# Check a sample skill
head -10 skills/ai-check/SKILL.md
# Should show:
# ---
# name: ai-check
# description: "..."
# allowed-tools: ...
# version: 1.0.0
# ---
```

**Re-validate plugin configuration:**
```bash
cat .claude/settings.json | python3 -m json.tool
```

### MCP Servers Not Working

**Symptom:** Literature search fails or MCP errors

**Check Python version:**
```bash
python3 --version
# Expected: 3.8 or higher
```

**Check dependencies:**
```bash
pip list | grep -E '(semanticscholar|biopython|sqlalchemy|pyyaml)'
```

**Install missing dependencies:**
```bash
pip install -r requirements.txt
```

**Test MCP servers directly:**
```bash
cd mcp-servers
python literature-search.py --test
```

### Permission Errors

**Symptom:** "Permission denied" when running hooks

**Fix hook permissions:**
```bash
chmod +x .claude/hooks/*.sh
chmod +x hooks/*.sh
```

**Fix directory permissions:**
```bash
chmod -R u+rw .
```

### API Rate Limit Errors

**Symptom:** "Rate limit exceeded" during literature search

**Solutions:**

1. **Add API keys** (increases limits):
   - Get PubMed API key: https://www.ncbi.nlm.nih.gov/account/settings/
   - Add to `.env`: `PUBMED_API_KEY=your_key_here`

2. **Wait between searches:**
   - PubMed without key: 3 requests/second
   - PubMed with key: 10 requests/second
   - OpenAlex polite (with email): 100k/day

3. **Use cached results:**
   - Results automatically cached in `data/literature/search_results.csv`
   - Reuse cached data when possible

### Windows (WSL) Specific Issues

**Line ending problems:**
```bash
# Convert scripts to Unix line endings
sudo apt-get install dos2unix
find .claude/hooks -name "*.sh" -exec dos2unix {} \;
find .claude/hooks -name "*.py" -exec dos2unix {} \;
```

**Python interpreter path:**
```bash
# Update shebang lines if needed
sed -i 's|/usr/bin/python|/usr/bin/python3|' .claude/hooks/*.py
```

---

## Getting Help

If you encounter issues not covered here:

1. **Check TROUBLESHOOTING.md**: Comprehensive guide with 50+ solutions
2. **Search GitHub Issues**: https://github.com/astoreyai/ai_scientist/issues
3. **Ask on Discussions**: https://github.com/astoreyai/ai_scientist/discussions
4. **Email Support**: aaron@astoreyai.com

**When reporting issues, include:**
- Operating system and version
- Claude Code version (`claude --version`)
- Plugin installation method (marketplace, local, GitHub)
- Output from `./automation/pre_distribution_checks.sh`
- Full error messages

---

## Next Steps

After installation:

1. **Quick Start**: Read `QUICK_START.md` (5 minutes)
2. **Tutorial 1**: Complete "Getting Started" tutorial (15 minutes)
3. **Try AI-Check**: Test on a sample document
4. **Explore Skills**: Browse all 22 skills with `/skill list`
5. **Invoke an Agent**: Try `/agent literature-reviewer`

---

**Installation Guide Version:** 1.0
**Plugin Version:** 1.2.0-beta3
**Last Updated:** 2025-11-11
