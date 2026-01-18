# List All Available Skills

Display all 22 research skills with descriptions and categorization.

## Instructions

1. Read skill metadata from all files matching `skills/*/SKILL.md`
2. Extract the `name` and `description` from YAML frontmatter (lines 2-3)
3. Group skills by the following categories and display them
4. Format output with clear categorization and numbering
5. Add usage instructions at the end

## Skill Categories

**ANALYSIS & STATISTICS** (6 skills):
- data-visualization, effect-size, hypothesis-test, power-analysis, sensitivity-analysis, subgroup-analysis

**EXPERIMENTAL DESIGN** (6 skills):
- blinding, experiment-design, inclusion-criteria, irb-protocol, pre-registration, randomization

**LITERATURE SYNTHESIS** (5 skills):
- literature-gap, meta-analysis, prisma-diagram, risk-of-bias, synthesis-matrix

**WRITING & PUBLICATION** (4 skills):
- citation-format, publication-prep, research-questions, results-interpretation

**QUALITY ASSURANCE** (1 skill):
- ai-check

## Output Format

Present as a well-formatted list with categories as headers, numbered sequentially across all categories:

```
🔬 Research Assistant - Available Skills (22 total)

ANALYSIS & STATISTICS
1. [skill-name] - [description from YAML]
...

EXPERIMENTAL DESIGN
7. [skill-name] - [description from YAML]
...

[Continue for all categories]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Usage: Invoke skills using the Skill tool
   Example: Use the Skill tool with skill="power-analysis"

📚 Learn more: /tutorials for step-by-step guides
🎯 Quick start: /quick-start for getting started
```

## Implementation Notes

- Read files from project root: `/home/aaron/github/astoreyai/ai_scientist/skills/`
- Parse YAML frontmatter carefully (between `---` markers)
- Preserve order within categories for consistency
- Keep descriptions concise (truncate if > 150 chars)
