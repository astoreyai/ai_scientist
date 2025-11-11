# Troubleshooting Guide

**Research Assistant for Claude Code v1.2.0-beta3**

This guide helps diagnose and resolve common issues with the Research Assistant plugin.

---

## Quick Diagnostics

Run these commands to check your installation:

```bash
# Check plugin files exist
ls -la .claude-plugin/  # Should show plugin.json, marketplace.json

# Count skills
find skills/ -name "SKILL.md" | wc -l  # Should show 22

# Count agents
ls -1 .claude/agents/*.md | wc -l  # Should show 10

# Check Python version (for MCP servers)
python3 --version  # Should be 3.8+

# Validate JSON syntax
cat .claude-plugin/plugin.json | python3 -m json.tool > /dev/null && echo "Valid" || echo "Invalid"
```

---

## Installation Issues

### Plugin Not Loading

**Symptoms:**
- `/skill list` returns empty or error
- `/agent list` returns empty or error
- Plugin doesn't appear in Claude Code

**Diagnosis:**

1. **Enable debug mode:**
   ```bash
   claude --debug
   ```
   Look for messages about "research-assistant" during startup.

2. **Check Claude Code logs:**
   ```bash
   tail -f ~/.claude/logs/$(date +%Y-%m-%d).log
   ```
   Watch for error messages during plugin loading.

3. **Verify directory structure:**
   ```bash
   pwd  # Make sure you're in the ai_scientist directory
   ls .claude-plugin/  # Should show plugin.json, marketplace.json
   ```

**Solutions:**

1. **Verify you're in the correct directory:**
   ```bash
   cd /path/to/ai_scientist
   claude-code .
   ```

2. **Check .claude/settings.json exists and is valid:**
   ```bash
   cat .claude/settings.json | python3 -m json.tool
   ```

3. **Restart Claude Code:**
   Close and reopen Claude Code in the ai_scientist directory.

4. **Reinstall (if using marketplace):**
   ```bash
   /plugin uninstall research-assistant
   /plugin install research-assistant
   ```

---

### Skills Not Appearing

**Symptoms:**
- `/skill list` shows 0 skills or incomplete list
- Claude doesn't recognize skill names
- Skills worked before but stopped working

**Diagnosis:**

```bash
# Check skill directories exist
ls skills/  # Should show 22 directories

# Verify SKILL.md files
find skills/ -name "SKILL.md" | wc -l  # Should show 22

# Check a sample skill's frontmatter
head -6 skills/ai-check/SKILL.md  # Should show valid YAML
```

**Solutions:**

1. **Verify plugin configuration in .claude/settings.json:**
   ```bash
   cat .claude/settings.json | grep -A 5 "plugins"
   ```

   Should show:
   ```json
   "plugins": [
     {
       "source": "./",
       "name": "research-assistant"
     }
   ]
   ```

2. **If missing, add plugin configuration:**
   Edit `.claude/settings.json` to include the plugins array.

3. **Check SKILL.md frontmatter syntax:**
   ```bash
   # Each skill should start with:
   # ---
   # name: skill-name
   # description: "..."
   # allowed-tools: Tool1, Tool2
   # version: 1.0.0
   # ---
   ```

4. **Validate YAML syntax:**
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('skills/ai-check/SKILL.md').read().split('---')[1])"
   ```

5. **Restart Claude Code:**
   ```bash
   # Close Claude Code completely, then reopen in the directory
   claude-code /path/to/ai_scientist
   ```

---

### Agents Not Available

**Symptoms:**
- `/agent agent-name` fails with "not found"
- Agents don't appear in suggestions
- Agent invocations return errors

**Diagnosis:**

```bash
# Check agents directory
ls .claude/agents/  # Should show 10 .md files

# Count agent files
ls -1 .claude/agents/*.md | wc -l  # Should show 10

# Check frontmatter of a sample agent
head -10 .claude/agents/literature-reviewer.md
```

**Solutions:**

1. **Verify agent frontmatter format:**
   ```bash
   head -10 .claude/agents/literature-reviewer.md
   ```

   Should show:
   ```yaml
   ---
   name: literature-reviewer
   description: Brief purpose
   tools: Read, Write, Grep, Glob, Bash, WebFetch
   model: opus
   color: Blue
   ---
   ```

2. **Check agents directory location:**
   Agents must be in `.claude/agents/` (note the dot prefix).

3. **Validate agent YAML:**
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('.claude/agents/literature-reviewer.md').read().split('---')[1])"
   ```

4. **Restart Claude Code:**
   Agent configurations are loaded at startup.

---

### Permission Errors

**Symptoms:**
- "Permission denied" errors
- Hooks don't execute
- Can't read/write files

**Solutions:**

```bash
# Fix directory permissions
chmod -R u+rw .

# Make hooks executable
chmod +x .claude/hooks/*.sh .claude/hooks/*.py

# Fix specific skill directories
chmod -R u+rw skills/

# Fix agent permissions
chmod -R u+rw .claude/agents/
```

---

## Runtime Issues

### MCP Server Connection Failures

**Symptoms:**
- Literature searches fail
- Citation verification errors
- "MCP server not available" messages

**Diagnosis:**

```bash
# Check Python version
python3 --version  # Should be 3.8+

# Check if dependencies installed
pip list | grep -E '(semanticscholar|biopython|sqlalchemy|pyyaml)'

# Test MCP server directly
cd mcp-servers/literature
python server.py --test
```

**Solutions:**

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify individual MCP servers:**
   ```bash
   # Test literature search
   cd mcp-servers/literature
   python server.py --test

   # Test citations
   cd mcp-servers/citations
   python server.py --test

   # Test research database
   cd mcp-servers/research_db
   python server.py --test
   ```

3. **Check MCP configuration:**
   See `mcp-servers/README.md` for detailed setup instructions.

4. **API key issues (for literature search):**
   ```bash
   # Check if API keys configured
   cat tools/literature_review/automated_scopus/config/scopus_config.yaml
   ```

---

### Hook Execution Failures

**Symptoms:**
- AI-check doesn't run on commit
- Pre-commit hooks don't trigger
- Session start hook fails

**Diagnosis:**

```bash
# Check hook files exist
ls -la .claude/hooks/

# Verify executable permissions
ls -l .claude/hooks/*.py .claude/hooks/*.sh

# Test hook manually
python3 .claude/hooks/pre-commit-ai-check.py test_file.md
```

**Solutions:**

1. **Make hooks executable:**
   ```bash
   chmod +x .claude/hooks/*.sh .claude/hooks/*.py
   ```

2. **Check Python dependencies for hooks:**
   ```bash
   pip install pyyaml sqlalchemy
   ```

3. **Verify settings.json hook configuration:**
   ```bash
   cat .claude/settings.json | jq '.hooks'
   ```

4. **Test hook directly:**
   ```bash
   python3 .claude/hooks/pre-commit-ai-check.py manuscript.tex
   ```

---

### AI-Check False Positives

**Symptoms:**
- Authentic writing flagged as AI-generated
- High confidence scores for human text
- Too many AI-typical words detected

**Solutions:**

1. **Review flagged words:**
   The tool may be overly sensitive. Common academic words like "furthermore" and "moreover" can trigger false positives.

2. **Adjust thresholds in .ai-check-config.yaml:**
   ```yaml
   detection:
     ai_words_per_1000_threshold: 4.0  # Increase from default 3.0

   pre_commit:
     block_threshold: 0.80  # Increase from default 0.70
   ```

3. **Exclude specific patterns:**
   ```yaml
   pre_commit:
     exclude_patterns:
       - "*/drafts/*"
       - "*/notes/*"
       - "*/examples/*"
   ```

4. **Whitelist domain-specific terms:**
   ```yaml
   detection:
     whitelist_words:
       - "methodology"  # Your field-specific terms
       - "heterogeneity"
   ```

---

## Performance Issues

### Slow Literature Searches

**Symptoms:**
- Searches take >2 minutes
- Timeout errors
- API rate limit messages

**Solutions:**

1. **Narrow search scope:**
   - Reduce date range (e.g., last 5 years instead of 10)
   - Use more specific keywords
   - Limit to fewer databases

2. **Respect API rate limits:**
   - Wait 60 seconds between searches
   - Use smaller result batches (100 instead of 500)
   - Cache results for reuse

3. **Check network connection:**
   ```bash
   ping pubmed.ncbi.nlm.nih.gov
   ping api.semanticscholar.org
   ```

4. **Use cached results:**
   Results are automatically cached in `data/literature/search_results.csv`.

---

### Large File Handling

**Symptoms:**
- Claude Code freezes
- Memory errors
- Very slow processing

**Solutions:**

1. **Use DVC for large files:**
   ```bash
   # Track large files with DVC
   dvc add data/large_dataset.csv
   git add data/large_dataset.csv.dvc .gitignore
   ```

2. **Process in chunks:**
   Split large datasets into smaller files for processing.

3. **Increase Node memory (if applicable):**
   ```bash
   export NODE_OPTIONS="--max-old-space-size=8192"
   claude-code .
   ```

4. **Use streaming for large analyses:**
   Process data row-by-row instead of loading entire file.

---

### Slow Agent Responses

**Symptoms:**
- Agents take >1 minute to respond
- Timeout messages
- Incomplete agent outputs

**Solutions:**

1. **Check agent model setting:**
   Some agents use `opus` which is more thorough but slower. Edit agent frontmatter to use `sonnet`:
   ```yaml
   model: sonnet  # Instead of opus
   ```

2. **Break down complex requests:**
   Instead of "conduct full systematic review", request:
   - "help me define PICOS framework"
   - "develop search strategy"
   - "screen first 50 abstracts"

3. **Reduce scope:**
   Start with smaller datasets or simpler analyses.

---

## Integration Issues

### Git Integration Problems

**Symptoms:**
- Git hooks don't trigger
- Commits blocked unexpectedly
- Hook errors on commit

**Solutions:**

1. **Verify git hooks directory:**
   ```bash
   ls .git/hooks/
   # Should show pre-commit hook
   ```

2. **Link hooks if needed:**
   ```bash
   ln -s ../../hooks/pre-commit .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

3. **Test hook manually:**
   ```bash
   .git/hooks/pre-commit
   ```

4. **Bypass hook temporarily (if needed):**
   ```bash
   git commit --no-verify -m "message"
   ```

---

### LaTeX Compilation Errors

**Symptoms:**
- PDF generation fails
- Missing packages
- Compilation timeout

**Solutions:**

1. **Check LaTeX installation:**
   ```bash
   which pdflatex
   pdflatex --version
   ```

2. **Install missing packages:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full

   # macOS
   brew install --cask mactex
   ```

3. **Use manual compilation:**
   ```bash
   cd outputs/manuscript
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```

---

## Platform-Specific Issues

### Windows (WSL)

**Common issues:**
- Line ending problems (CRLF vs LF)
- Path separators (backslash vs forward slash)
- Permission issues

**Solutions:**

```bash
# Fix line endings
dos2unix .claude/hooks/*.py .claude/hooks/*.sh

# Convert all scripts
find . -name "*.sh" -exec dos2unix {} \;
find . -name "*.py" -exec dos2unix {} \;

# Ensure correct Python interpreter
sed -i 's|/usr/bin/python|/usr/bin/python3|' .claude/hooks/*.py
```

### macOS

**Common issues:**
- .DS_Store files
- Gatekeeper blocking executables
- Homebrew Python paths

**Solutions:**

```bash
# Remove .DS_Store files
find . -name ".DS_Store" -delete

# Add to .gitignore
echo ".DS_Store" >> .gitignore

# Use system Python if Homebrew causes issues
/usr/bin/python3 -m pip install -r requirements.txt
```

### Linux

**Common issues:**
- SELinux blocking execution
- Missing system libraries
- Python version conflicts

**Solutions:**

```bash
# Check SELinux status
sestatus

# Install system dependencies (Ubuntu/Debian)
sudo apt-get install python3-dev python3-pip git

# Install system dependencies (Fedora/RHEL)
sudo dnf install python3-devel python3-pip git
```

---

## Data Issues

### Missing Data Files

**Symptoms:**
- "File not found" errors
- Empty search results
- Data loading failures

**Solutions:**

1. **Check data directory structure:**
   ```bash
   ls -la data/
   # Should show: raw/, processed/, literature/, results/
   ```

2. **Restore tracked files with DVC:**
   ```bash
   dvc pull
   ```

3. **Regenerate data:**
   Run literature search or analysis scripts to recreate missing data.

---

### Corrupted or Invalid Data

**Symptoms:**
- Parse errors
- Encoding issues
- Malformed CSV/JSON

**Solutions:**

1. **Validate file format:**
   ```bash
   # Check CSV
   head data/literature/search_results.csv

   # Check JSON
   cat results/primary_results.json | python3 -m json.tool
   ```

2. **Fix encoding issues:**
   ```bash
   # Convert to UTF-8
   iconv -f ISO-8859-1 -t UTF-8 file.csv > file_utf8.csv
   ```

3. **Regenerate from source:**
   If data is corrupted, rerun the analysis or search that created it.

---

## Reporting Issues

If you can't resolve the issue, please report it on GitHub with the following information:

### Required Information

```bash
# System information
uname -a
python3 --version
claude --version

# Plugin state
ls -la .claude-plugin/
find skills/ -name "SKILL.md" | wc -l
ls -1 .claude/agents/*.md | wc -l

# Configuration
cat .claude/settings.json | python3 -m json.tool

# Recent logs
tail -50 ~/.claude/logs/$(date +%Y-%m-%d).log
```

### Issue Template

When opening an issue, include:

1. **Operating System**: (e.g., Ubuntu 22.04, macOS 13.5, Windows 11 WSL)
2. **Claude Code Version**: Output of `claude --version`
3. **Plugin Version**: 1.2.0-beta3
4. **Error Message**: Full error text
5. **Steps to Reproduce**: What you did before the error
6. **Expected Behavior**: What should have happened
7. **Actual Behavior**: What actually happened
8. **Debug Output**: Output from `claude --debug`
9. **Configuration**: Contents of `.claude/settings.json` (remove API keys)

### Submit Issue

[Create GitHub Issue](https://github.com/astoreyai/ai_scientist/issues/new)

---

## Getting Help

- **GitHub Issues**: https://github.com/astoreyai/ai_scientist/issues
- **Discussions**: https://github.com/astoreyai/ai_scientist/discussions
- **Email**: aaron@astoreyai.com

---

## Common Solutions Summary

| Problem | Quick Fix |
|---------|-----------|
| Skills not loading | Check `.claude/settings.json` has plugins config |
| Agents not available | Verify `.claude/agents/` directory exists |
| Permission errors | Run `chmod -R u+rw . && chmod +x .claude/hooks/*` |
| MCP server fails | Install dependencies: `pip install -r requirements.txt` |
| Plugin not recognized | Restart Claude Code in the ai_scientist directory |
| JSON syntax error | Validate with `cat file.json \| python3 -m json.tool` |
| Hook doesn't execute | Make executable: `chmod +x .claude/hooks/*.py` |
| Slow performance | Use `sonnet` model instead of `opus` in agents |

---

**Last Updated**: 2025-11-11
**Plugin Version**: 1.2.0-beta3
