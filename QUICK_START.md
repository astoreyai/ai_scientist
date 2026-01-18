# Quick Start Guide - Research Assistant System

**Get started in 10 minutes**

---

## 1. Install Dependencies (2 minutes)

```bash
cd /path/to/ai_scientist

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install minimal dependencies
pip install mcp psycopg2-binary
```

---

## 2. Test System (1 minute)

```bash
# Test hooks work
echo '{}' | bash .claude/hooks/session-start.sh
```

Expected output:
```
Research Assistant System ready.
Mode: ASSISTANT
```

✅ **System ready!**

---

## 3. Start Claude Code

```bash
claude
```

---

## 4. Try Your First Agent

```
You: "Use the literature-reviewer agent to explain PRISMA 2020 systematic review guidelines"
```

The agent will:
- Load PRISMA 2020 specifications
- Explain the 27-item checklist
- Guide you through systematic review process

---

## 5. Common Tasks

### Literature Review

```
You: "Help me conduct a systematic literature review on [your topic]"
```

Agent will guide you through:
1. Defining research question (FINER criteria)
2. Creating search strategy
3. Screening papers (PRISMA)
4. Data extraction
5. Quality assessment

### Power Analysis

```
You: "I need to calculate sample size for an experiment with 80% power to detect a medium effect"
```

Agent consults power-analysis specifications and calculates required sample size.

### Experiment Design

```
You: "Help me design a rigorous experiment following NIH standards"
```

Agent will:
1. Conduct power analysis
2. Address SABV (Sex as Biological Variable)
3. Create randomization protocol
4. Plan for reproducibility

---

## 6. Switch Modes

**ASSISTANT Mode (default):** Human-guided, interactive
**AUTONOMOUS Mode:** Fully automated, minimal intervention

To switch, edit `.claude/CLAUDE.md`:

```bash
nano .claude/CLAUDE.md
```

Change:
```markdown
## Current Mode: ASSISTANT
```

to:
```markdown
## Current Mode: AUTONOMOUS
```

---

## 7. Check Your Progress

View session log:
```bash
tail -f .claude/session.log
```

View tool usage:
```bash
sqlite3 .claude/tool_log.db "SELECT tool_name, COUNT(*) FROM tool_log GROUP BY tool_name;"
```

---

## Next Steps

### Want MCP Servers? (Optional)

Full installation guide: `INSTALLATION.md`

MCP servers add:
- Multi-database literature search (OpenAlex, arXiv, PubMed)
- Citation verification
- Research database storage

### Learn More

- **README.md** - System overview
- **docs/skills/** - Research methodology guides
- **.claude/agents/** - Agent specifications
- **PROJECT_STATUS.md** - Implementation status

---

## Need Help?

**Check logs:**
```bash
# Session initialization
cat .claude/session.log

# Security validations
cat .claude/security.log

# Tool executions
cat .claude/post-tool.log
```

**Common Issues:**
- "Module not found" → Run `pip install -r requirements.txt`
- "Permission denied" → Run `chmod +x .claude/hooks/*.py .claude/hooks/*.sh`
- "Database error" → PostgreSQL not needed for basic use, ignore warning

---

**You're ready to start!** 🚀

Try: *"Use the experiment-designer agent to help me plan a study"*
