# List All Available Agents

Display all 10 specialized agents with their capabilities and recommended use cases.

## Instructions

1. Read agent metadata from all files matching `.claude/agents/*.md`
2. Extract the `name` and `description` from YAML frontmatter (lines 2-3)
3. Group agents by the following categories
4. Format output with clear categorization and numbering
5. Add usage instructions at the end

## Agent Categories

**LITERATURE & EVIDENCE SYNTHESIS** (3 agents):
- gap-analyst, literature-reviewer, meta-reviewer

**EXPERIMENTAL DESIGN & ANALYSIS** (3 agents):
- data-analyst, experiment-designer, hypothesis-generator

**WRITING & DOCUMENTATION** (2 agents):
- citation-manager, manuscript-writer

**QUALITY & REVIEW** (2 agents):
- code-reviewer, quality-assurance

## Output Format

Present as a well-formatted list with categories as headers:

```
🤖 Research Assistant - Available Agents (10 total)

LITERATURE & EVIDENCE SYNTHESIS
1. [agent-name] - [description from YAML]
2. [agent-name] - [description from YAML]
3. [agent-name] - [description from YAML]

EXPERIMENTAL DESIGN & ANALYSIS
4. [agent-name] - [description from YAML]
...

[Continue for all categories]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Usage: Launch agents using the Task tool with subagent_type parameter
   Example: Use Task tool with subagent_type="literature-reviewer"

📖 Agent Descriptions: Read .claude/agents/[agent-name].md for full details
🎯 When to Use: Agents handle complex, multi-step autonomous tasks
⚡ Delegation: Claude Code automatically delegates to agents when appropriate
```

## Implementation Notes

- Read files from: `/home/aaron/github/astoreyai/ai_scientist/.claude/agents/`
- Parse YAML frontmatter between `---` markers
- List agents alphabetically within each category
- Keep descriptions concise (full description from YAML)
- Explain that agents are for complex, multi-step research tasks
