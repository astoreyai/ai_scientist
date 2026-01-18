# Installation Guide - Production Research Assistant System

**Complete setup instructions for Claude Code Research Assistant**

**Time Required:** 15-30 minutes
**Difficulty:** Intermediate
**System:** Linux/macOS (Windows WSL supported)

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start (5 minutes)](#quick-start)
3. [Full Installation](#full-installation)
4. [Configuration](#configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)
7. [Uninstallation](#uninstallation)

---

## Prerequisites

### Required

✅ **Python 3.11+**
```bash
python3 --version  # Should be 3.11 or higher
```

✅ **Git**
```bash
git --version
```

✅ **Claude Code CLI**
- Install from: https://claude.com/code
- Verify: `claude --version`

### Recommended

⭐ **PostgreSQL 14+** (for research database)
```bash
psql --version
```

⭐ **jq** (for JSON processing in hooks)
```bash
jq --version
```

### Optional (for enhanced features)

- **DVC** - Data version control
- **MLflow** - Experiment tracking
- **Docker** - Reproducibility

---

## Quick Start

**Get started in 5 minutes with core features:**

### 1. Clone or navigate to project

```bash
cd /path/to/ai_scientist
```

### 2. Install Python dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core dependencies
pip install mcp psycopg2-binary
```

### 3. Test hooks system

```bash
# Test session start hook
echo '{}' | bash .claude/hooks/session-start.sh
```

Expected output:
```
Research Assistant System ready.
Mode: ASSISTANT
Protocols: PRISMA 2020, NIH Rigor
```

✅ **Core system ready!** You can now use agents without MCP servers.

---

## Full Installation

**Complete setup with all features (MCP servers, database, APIs):**

### Step 1: Install Python Dependencies

```bash
# Navigate to project
cd /path/to/ai_scientist

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

This installs:
- MCP framework
- Literature search APIs (pyalex, arxiv, biopython)
- Citation tools (habanero, bibtexparser)
- Database drivers (psycopg2)
- Data science tools (pandas, numpy, scipy)
- Experiment tracking (mlflow, dvc)

**Verification:**
```bash
python3 -c "from mcp.server.fastmcp import FastMCP; print('✅ MCP installed')"
python3 -c "import pyalex; print('✅ PyAlex installed')"
python3 -c "import psycopg2; print('✅ PostgreSQL driver installed')"
```

---

### Step 2: PostgreSQL Setup (Optional but Recommended)

The research database server requires PostgreSQL for systematic review data storage.

#### Install PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
Download from: https://www.postgresql.org/download/windows/

#### Create Database

```bash
# Create database
createdb research_db

# Or with specific user
createdb -U postgres research_db

# Verify
psql -d research_db -c "SELECT version();"
```

#### Set Environment Variables

Add to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="research_db"
export DB_USER="postgres"
export DB_PASSWORD="your_password"
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

---

### Step 3: Configure MCP Servers

MCP servers connect Claude Code to external data sources.

#### Create Configuration File

Edit `~/.claude/claude_desktop_config.json`:

```bash
mkdir -p ~/.claude
nano ~/.claude/claude_desktop_config.json
```

#### Add Server Configuration

Use absolute paths (replace `/path/to/ai_scientist` with actual path):

```json
{
  "mcpServers": {
    "literature": {
      "command": "python",
      "args": ["/absolute/path/to/ai_scientist/mcp-servers/literature-search.py"],
      "env": {
        "OPENALEX_EMAIL": "your-email@example.com",
        "PUBMED_EMAIL": "your-email@example.com",
        "PUBMED_API_KEY": ""
      }
    },
    "citations": {
      "command": "python",
      "args": ["/absolute/path/to/ai_scientist/mcp-servers/citation-management.py"],
      "env": {
        "OPENCITATIONS_TOKEN": ""
      }
    },
    "research_db": {
      "command": "python",
      "args": ["/absolute/path/to/ai_scientist/mcp-servers/research-database.py"],
      "env": {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "research_db",
        "DB_USER": "postgres",
        "DB_PASSWORD": "your_password"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/absolute/path/to/ai_scientist"]
    },
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "/absolute/path/to/ai_scientist"]
    }
  }
}
```

**Get Absolute Path:**
```bash
cd /path/to/ai_scientist
pwd  # Copy this output
```

#### Optional: API Keys (for higher rate limits)

**PubMed API Key:**
1. Create NCBI account: https://www.ncbi.nlm.nih.gov/account/
2. Go to: https://www.ncbi.nlm.nih.gov/account/settings/
3. Create API key
4. Add to config: `"PUBMED_API_KEY": "your-key"`

**OpenCitations Token:**
1. Visit: https://opencitations.net/
2. Request access token (optional)
3. Add to config: `"OPENCITATIONS_TOKEN": "your-token"`

---

### Step 4: Set Up Hooks System

Hooks are already configured in `.claude/settings.json`. Verify they're executable:

```bash
chmod +x .claude/hooks/*.py
chmod +x .claude/hooks/*.sh

# Verify
ls -la .claude/hooks/
```

All scripts should show `x` permission (executable).

---

## Configuration

### Mode Selection (ASSISTANT vs AUTONOMOUS)

Edit `.claude/CLAUDE.md` to change operating mode:

**ASSISTANT Mode** (default - human-guided):
```markdown
## Current Mode: ASSISTANT
```

**AUTONOMOUS Mode** (fully automated):
```markdown
## Current Mode: AUTONOMOUS
```

Save file and restart session for changes to take effect.

---

### Customizing Research Protocols

Protocols are auto-generated in `.claude/protocols/` on first run. Customize if needed:

**PRISMA 2020 Checklist:**
```bash
nano .claude/protocols/prisma_2020_checklist.md
```

**NIH Rigor Checklist:**
```bash
nano .claude/protocols/nih_rigor_checklist.md
```

---

## Verification

### Test 1: Core Hooks System

```bash
# Test session start
echo '{}' | bash .claude/hooks/session-start.sh
```

**Expected output:**
```
Research Assistant System ready.
Mode: ASSISTANT
Protocols: PRISMA 2020, NIH Rigor
Session log: .claude/session.log
```

✅ **Pass:** System initialized

---

### Test 2: Security Validation

```bash
# Test dangerous command blocking
echo '{"name": "Bash", "input": {"command": "rm -rf /"}}' | \
  python3 .claude/hooks/pre-tool-security.py
```

**Expected:** Exit code 2 (blocked), JSON with `"decision": "block"`

✅ **Pass:** Security system working

---

### Test 3: Tool Logging

```bash
# Test logging hook
echo '{"name": "Read", "status": "success", "input": {}, "output": {}}' | \
  python3 .claude/hooks/post-tool-log.py
```

**Expected:** JSON with `"status": "success", "logged": true`

Check database created:
```bash
ls -la .claude/tool_log.db
```

✅ **Pass:** Logging system working

---

### Test 4: MCP Servers (if installed)

**Test Literature Search Server:**
```bash
cd mcp-servers
python literature-search.py &
PID=$!

# Server should start without errors
# Kill after test
kill $PID
```

**Test Citation Management Server:**
```bash
python citation-management.py &
PID=$!
kill $PID
```

**Test Research Database Server:**
```bash
# Requires PostgreSQL running
python research-database.py &
PID=$!
kill $PID
```

✅ **Pass:** MCP servers start without errors

---

### Test 5: Claude Code Integration

Start Claude Code in project directory:

```bash
cd /path/to/ai_scientist
claude
```

In Claude Code, test an agent:

```
User: "Use the literature-reviewer agent to explain PRISMA 2020 guidelines"

Expected: Agent loads and provides detailed PRISMA explanation
```

✅ **Pass:** Agents accessible in Claude Code

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'mcp'"

**Problem:** MCP framework not installed

**Solution:**
```bash
pip install mcp
# Or
pip install -r requirements.txt
```

---

### Issue: "Database connection failed"

**Problem:** PostgreSQL not running or incorrect credentials

**Solution:**
```bash
# Check if PostgreSQL is running
pg_isready

# If not running, start it
# Ubuntu/Debian:
sudo service postgresql start

# macOS:
brew services start postgresql

# Test connection manually
psql -h localhost -U postgres -d research_db

# Verify environment variables
echo $DB_HOST $DB_NAME $DB_USER
```

---

### Issue: "Session start hook fails"

**Problem:** Missing dependencies or permissions

**Solution:**
```bash
# Check dependencies
which python3
which git
which jq

# Install jq if missing
# Ubuntu/Debian:
sudo apt-get install jq

# macOS:
brew install jq

# Check permissions
ls -la .claude/hooks/session-start.sh
# Should show: -rwxr-xr-x (executable)

# Fix if needed
chmod +x .claude/hooks/session-start.sh
```

---

### Issue: "Permission denied" when running hooks

**Problem:** Hooks not executable

**Solution:**
```bash
chmod +x .claude/hooks/*.py
chmod +x .claude/hooks/*.sh
```

---

### Issue: MCP servers not showing in Claude Code

**Problem:** Configuration file incorrect or servers not starting

**Solution:**

1. **Verify config file location:**
```bash
ls -la ~/.claude/claude_desktop_config.json
```

2. **Check absolute paths in config:**
```bash
cd /path/to/ai_scientist
pwd  # Use this exact path in config
```

3. **Test server manually:**
```bash
cd /path/to/ai_scientist
python mcp-servers/literature-search.py
# Should start without errors
```

4. **Check logs:**
```bash
# Claude Code logs location varies by system
# Check Claude Code documentation for log location
```

---

### Issue: "Rate limit exceeded" when using APIs

**Problem:** Making too many requests without API keys

**Solution:**

1. **Add email to increase OpenAlex rate limit:**
```json
"OPENALEX_EMAIL": "your-email@example.com"
```

2. **Get PubMed API key:**
- https://www.ncbi.nlm.nih.gov/account/settings/
- Increases rate limit from 3 req/sec to 10 req/sec

3. **Add delays between requests:**
- APIs automatically implement rate limiting
- Consider batch operations

---

### Issue: Hooks execute but show warnings

**Problem:** Non-critical dependency missing

**Solution:**

Check `.claude/session.log` for details:
```bash
tail -20 .claude/session.log
```

Most warnings can be safely ignored. Common ones:
- "DVC not installed" - Only needed for large data files
- "Missing optional dependency" - Doesn't affect core functionality

---

## Uninstallation

### Remove Virtual Environment

```bash
cd /path/to/ai_scientist
rm -rf venv
```

### Remove MCP Server Configuration

```bash
# Backup first
cp ~/.claude/claude_desktop_config.json ~/.claude/claude_desktop_config.json.backup

# Remove MCP server entries
nano ~/.claude/claude_desktop_config.json
# Delete the mcpServers section or specific entries
```

### Remove PostgreSQL Database

```bash
# Drop database
dropdb research_db

# Or with specific user
dropdb -U postgres research_db
```

### Remove Generated Files

```bash
cd /path/to/ai_scientist

# Remove generated protocol files
rm -rf .claude/protocols/

# Remove session state
rm .claude/session_state.json

# Remove logs
rm .claude/*.log

# Remove database
rm .claude/tool_log.db
```

---

## Next Steps

### After Installation

1. **Read the Quick Start Guide** - `QUICK_START.md`
2. **Try example workflows** - Start with literature review
3. **Customize modes** - Switch between ASSISTANT and AUTONOMOUS
4. **Explore agents** - Use specialized research agents
5. **Set up version control** - Configure Git + DVC for data

### Recommended Workflow

1. **Start session** - Claude Code initializes with hooks
2. **Use agents** - Invoke literature-reviewer, experiment-designer, etc.
3. **Review outputs** - Check generated files and results
4. **Iterate** - Refine research based on agent suggestions
5. **Track progress** - Use tool logging and session state

---

## Support

### Documentation

- **README.md** - System overview
- **PROJECT_STATUS.md** - Current implementation status
- **TEST_RESULTS.md** - System validation and testing
- **mcp-servers/README.md** - MCP server details
- **docs/skills/** - Research methodology references

### Getting Help

1. **Check logs:**
   - `.claude/session.log` - Session initialization
   - `.claude/security.log` - Security validations
   - `.claude/post-tool.log` - Tool execution history

2. **Review test results:**
   - `TEST_RESULTS.md` - Known issues and fixes

3. **Verify installation:**
   - Run verification tests in this guide
   - Check all dependencies installed

---

## System Requirements

### Minimum Requirements

- **CPU:** 2 cores
- **RAM:** 4 GB
- **Disk:** 2 GB free space
- **OS:** Linux, macOS, Windows WSL
- **Python:** 3.11+

### Recommended Requirements

- **CPU:** 4+ cores
- **RAM:** 8+ GB
- **Disk:** 10+ GB free space (for literature database)
- **Network:** Stable internet (for API calls)

---

## FAQ

### Q: Do I need all MCP servers?

**A:** No. The core system (hooks + agents) works without MCP servers. MCP servers add:
- **literature:** Multi-database literature search
- **citations:** Citation verification and retraction checking
- **research_db:** Systematic review data storage

Start with core system, add servers as needed.

---

### Q: Can I use this offline?

**A:** Partially. The hooks and agents work offline, but MCP servers require internet for:
- Literature searches (OpenAlex, arXiv, PubMed)
- Citation verification (Crossref, OpenCitations)

The research database works offline after initial setup.

---

### Q: How do I update the system?

**A:**
```bash
cd /path/to/ai_scientist
git pull  # If using git
pip install -r requirements.txt --upgrade
```

---

### Q: Is my data private?

**A:** Yes:
- Hooks run locally
- Database is local (PostgreSQL)
- MCP servers make API calls but don't share your research data
- No telemetry or tracking

API calls to external services (OpenAlex, etc.) follow their privacy policies.

---

### Q: Can I customize the agents?

**A:** Yes. Edit agent files in `.claude/agents/`:
```bash
nano .claude/agents/literature-reviewer.md
```

Agents are markdown files with prompts and tool specifications.

---

## Version

**Installation Guide Version:** 1.0
**System Version:** Phase 2 Complete
**Last Updated:** January 5, 2025

---

**Installation complete!** 🎉

Start using the system:
```bash
cd /path/to/ai_scientist
claude  # Start Claude Code
```

Then try: *"Use the literature-reviewer agent to help me with a systematic review"*
