# Installation Guide - Research Assistant Plugin

Complete installation instructions for the Research Assistant plugin for Claude Code.

## Prerequisites

- **Claude Code CLI** installed and configured
- **Python 3.11+** for AI-check and MCP servers
- **Git** for version control
- **PostgreSQL** (optional, for research-database MCP server)

---

## Quick Installation

### Step 1: Install Plugin

```bash
# Add the marketplace
/plugin marketplace add astoreyai/ai_scientist

# Install the plugin
/plugin install research-assistant@research-assistant-marketplace
```

That's it! The plugin is now installed with:
- ✅ 10 specialized agents
- ✅ 22 research skills  
- ✅ 7 workflow hooks
- ✅ AI-check system

---

## Verify Installation

### Check Installed Components

```bash
# List all skills
/skill list

# Should show:
# - ai-check
# - citation-format
# - power-analysis
# - effect-size
# - prisma-diagram
# - hypothesis-test
# ... and 16 more

# List all agents
/agent list

# Should show:
# - literature-reviewer
# - experiment-designer
# - data-analyst
# ... and 7 more
```

### Test AI-Check

Create a test file and commit:
```bash
cd your-research-project
echo "This study leverages robust methodologies to delve into comprehensive analysis." > test.md
git add test.md
git commit -m "test"

# Should see AI-check warning/block if configured
```

---

## Optional: MCP Server Installation

MCP servers provide additional capabilities for literature search, citation management, and data storage.

### Literature Search MCP

**Install:**
```bash
cd ~/.claude/plugins/research-assistant/mcp-servers/literature-search
pip install -e .
```

**Configure:**
Edit Claude Desktop config: `Claude > Settings > Developers > Edit Config`

```json
{
  "mcpServers": {
    "literature": {
      "command": "python",
      "args": ["-m", "research_lit_search.server"],
      "env": {
        "OPENALEX_EMAIL": "your-email@example.com"
      }
    }
  }
}
```

**Test:**
Restart Claude Desktop and verify the `literature` MCP server appears in settings.

### Citation Management MCP

**Install:**
```bash
cd ~/.claude/plugins/research-assistant/mcp-servers/citation-management
pip install -e .
```

**Configure:**
```json
{
  "mcpServers": {
    "citations": {
      "command": "python",
      "args": ["-m", "research_citations.server"]
    }
  }
}
```

### Research Database MCP

**Prerequisites:**
```bash
# Install PostgreSQL
sudo apt-get install postgresql postgresql-contrib  # Linux
brew install postgresql  # macOS

# Create database
createdb research_db
```

**Install:**
```bash
cd ~/.claude/plugins/research-assistant/mcp-servers/research-database
pip install -e .
```

**Configure:**
```json
{
  "mcpServers": {
    "research-db": {
      "command": "python",
      "args": ["-m", "research_db.server"],
      "env": {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "research_db",
        "DB_USER": "your_username",
        "DB_PASSWORD": "your_password"
      }
    }
  }
}
```

---

## Configuration

### AI-Check Configuration

The plugin includes a default `.ai-check-config.yaml` template. Customize as needed:

```yaml
pre_commit:
  enabled: true
  block_threshold: 0.70  # Block commits >= 70% AI confidence
  warn_threshold: 0.30   # Warn for >= 30% confidence

detection:
  ai_words_per_1000_threshold: 3.0  # Flag if >3 AI words per 1000 words
```

### Hook Configuration

Hooks are pre-configured in `.claude/settings.json`. To disable AI-check pre-commit hook:

```json
{
  "hooks": {
    "gitPreCommit": {
      "enabled": false
    }
  }
}
```

---

## Troubleshooting

### Plugin Not Loading

**Issue:** Plugin doesn't appear after installation

**Solution:**
```bash
# Check plugin list
/plugin list

# Reinstall if needed
/plugin uninstall research-assistant
/plugin install research-assistant@research-assistant-marketplace
```

### AI-Check Not Working

**Issue:** Pre-commit hook not blocking AI text

**Solution:**
1. Check hook is enabled in `.claude/settings.json`
2. Verify Python 3.11+ is installed
3. Check the hook script is executable:
   ```bash
   chmod +x ~/.claude/plugins/research-assistant/hooks/pre-commit-ai-check.py
   ```

### MCP Server Connection Fails

**Issue:** MCP server not connecting in Claude Desktop

**Solution:**
1. Verify installation: `pip list | grep research-`
2. Check configuration syntax in Claude Desktop config
3. Restart Claude Desktop
4. Check logs: `Claude > Settings > Developers > View Logs`

### Import Errors

**Issue:** `ModuleNotFoundError` when running AI-check

**Solution:**
```bash
# Install required dependencies
pip install pyyaml

# For MCP servers, reinstall
cd ~/.claude/plugins/research-assistant/mcp-servers/literature-search
pip install -e .
```

---

## Uninstallation

### Remove Plugin

```bash
/plugin uninstall research-assistant
```

### Remove MCP Servers

```bash
pip uninstall research-literature-search
pip uninstall research-citation-management
pip uninstall research-database
```

### Clean Up Configuration

Remove MCP server entries from Claude Desktop config.

---

## Platform-Specific Notes

### macOS

- Use `~/.claude/` for configuration files
- Claude Desktop config: `~/Library/Application Support/Claude/claude_desktop_config.json`

### Linux

- Use `~/.claude/` for configuration files
- Claude Desktop config: `~/.config/Claude/claude_desktop_config.json`

### Windows

- Use `%USERPROFILE%\.claude\` for configuration files
- Claude Desktop config: `%APPDATA%\Claude\claude_desktop_config.json`

---

## Next Steps

1. **Read the User Guide:** `docs/USER_GUIDE.md`
2. **Try the AI-check skill:** Test on your manuscript
3. **Invoke an agent:** Start with `/agent literature-reviewer`
4. **Configure for your workflow:** Customize thresholds and settings

---

## Support

- **Issues:** https://github.com/astoreyai/ai_scientist/issues
- **Documentation:** https://github.com/astoreyai/ai_scientist/tree/main/docs
- **Email:** aaron@astoreyai.com

---

*Installation guide last updated: 2025-11-09*
