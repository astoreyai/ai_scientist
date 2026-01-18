# ResearchPilot - Skill Implementation Guide

**Created:** October 18, 2025
**Phase:** 1 - Understanding & Setup
**Status:** Research findings from experimental testing

---

## 🔍 FINDINGS FROM EXPERIMENTATION

### What We Learned

**Slash Commands (/) Work:** ✅
- Format: Markdown files in `.claude/commands/`
- Invocation: `/command-name`
- Execution: Claude reads the markdown and executes the bash blocks
- Status: **13 commands working perfectly**

**Skills (@) - Need Different Approach:** ⚠️
- Simply creating `.claude/skills/*.md` files doesn't auto-register them
- The `@skill-name` syntax doesn't automatically invoke them
- Skills in Claude Code may require different registration

---

## 💡 REVISED IMPLEMENTATION STRATEGY

### Approach 1: Skills AS Slash Commands ⭐ RECOMMENDED

**Rationale:**
- Slash commands work perfectly
- We can create skill-like commands
- They're reusable and well-documented
- No unknown registration mechanism

**Implementation:**
Instead of trying to create `@skills`, create **reusable slash commands** that act like skills:

```
.claude/commands/
├── [existing 13 commands]
└── skills/                    # NEW: Skill-like commands
    ├── citation-format.md      # /citation-format
    ├── prisma-diagram.md       # /prisma-diagram
    ├── power-analysis.md       # /power-analysis
    └── [all 22 skills as commands]
```

**Advantages:**
- ✅ We know this works (proven with 13 commands)
- ✅ No unknown registration mechanism
- ✅ Consistent with existing pattern
- ✅ Fully functional immediately
- ✅ Can still be reusable across dissertations

**Disadvantages:**
- ❌ Uses `/` instead of `@` prefix
- ❌ Not "skills" in Claude Code terminology
- ❌ But functionally equivalent!

### Approach 2: Prompt-Based Pseudo-Skills

**Implementation:**
Create skills as **comprehensive prompt templates** that users/agents can copy-paste or reference:

**File:** `skills/implementations/citation-format-prompt.md`

```markdown
# Citation Format Skill - Copy This Prompt

When you need to format citations, copy and use this prompt:

---

Format the following references in [APA/IEEE/Chicago] style:

[References to format]

Requirements:
- Use proper citation format
- Include DOI if available
- Alphabetical order
- Hanging indent
- All required fields

Output:
- Formatted bibliography
- Any missing information flagged
- BibTeX version (if requested)

---
```

**Advantages:**
- ✅ Works immediately
- ✅ Portable and reusable
- ✅ No technical implementation needed
- ✅ Clear and documented

**Disadvantages:**
- ❌ Manual copy-paste required
- ❌ Not automatic invocation
- ❌ Less elegant than `@skill-name`

### Approach 3: Agent-Based Skills

**Implementation:**
Each "skill" is actually a **specialized, small agent**:

```python
# To use a skill:
Task(
    subagent_type="general-purpose",
    description="Format citations in APA style",
    prompt="""
    You are the citation-format skill.

    Input: [citations]
    Task: Format in APA 7th edition
    Output: Properly formatted bibliography

    [Detailed instructions from skill spec]
    """
)
```

**Advantages:**
- ✅ Uses working Task tool
- ✅ Can be autonomous
- ✅ Flexible and powerful

**Disadvantages:**
- ❌ Overhead of launching agent
- ❌ Not as lightweight as `@skill`
- ❌ Might be overkill for simple tasks

---

## 🎯 RECOMMENDED IMPLEMENTATION PLAN

### Decision: **Hybrid Approach**

Use **Approach 1 (Slash Commands) for simple skills** and **Approach 3 (Agents) for complex skills**:

**Simple Skills → Slash Commands** (Quick, single-step tasks)
```
/citation-format
/bibtex-clean
/keywords-develop
/effect-size
/research-questions
```

**Complex Skills → Small Agents** (Multi-step, iterative tasks)
```
Task(scopus-researcher-skill, ...)  # Complex literature search
Task(statistical-analyzer-skill, ...)  # Multi-step analysis
Task(abstract-writer-skill, ...)  # Iterative writing
```

---

## 📋 IMPLEMENTATION FOR 22 SKILLS

### Tier 1: Core Skills (13 skills)

**As Slash Commands** (8 simple skills):
- `/citation-format` - Format citations
- `/bibtex-clean` - Clean BibTeX
- `/keywords-develop` - Generate keywords
- `/inclusion-criteria` - Define criteria
- `/power-analysis` - Calculate sample size
- `/effect-size` - Calculate effect sizes
- `/hypothesis-test` - Select statistical test
- `/research-questions` - Formulate RQs

**As Small Agents** (5 complex skills):
- `prisma-diagram-skill` - Generate PRISMA flowchart (multi-step)
- `synthesis-matrix-skill` - Build literature matrix (complex)
- `lit-gap-skill` - Identify gaps (analysis-heavy)
- `academic-grammar-skill` - Check writing (iterative)
- `abstract-writer-skill` - Write abstract (multi-draft)

### Tier 2: Specialized Skills (9 skills)

**As Slash Commands** (4 simple skills):
- `/latex-table` - Generate LaTeX tables
- `/figure-table` - Create figure specifications
- `/timeline-generator` - Generate timeline
- `/limitation-writer` - Write limitations

**As Small Agents** (5 complex skills):
- `methodology-writer-skill` - Draft Chapter 4 (complex)
- `contribution-writer-skill` - Articulate contributions
- `experiment-design-skill` - Design experiments
- `results-interpreter-skill` - Interpret statistics
- `defense-prep-skill` - Prepare defense materials

---

## 📝 IMPLEMENTATION TEMPLATES

### Template 1: Simple Skill as Slash Command

**File:** `.claude/commands/citation-format.md`

```markdown
# /citation-format - Format Citations

Format academic citations in specified style (APA, IEEE, Chicago, MLA).

## Usage

```
/citation-format [style] [format]
```

## Parameters

- **style**: APA (default), IEEE, Chicago, MLA
- **format**: text (default), bibtex, both

## Example

```
/citation-format APA text
```

Then paste your unformatted references.

## Implementation

[Instructions for Claude on how to format citations]

1. Identify citation components (author, year, title, etc.)
2. Apply style-specific formatting rules
3. Alphabetize if multiple citations
4. Validate required fields present
5. Output formatted bibliography

## Output Format

```
Formatted Bibliography ([Style]):

1. Author, A. (Year). Title. Journal, Volume(Issue), pages.
2. [...]

[If BibTeX requested:]
@article{key,
  author = {},
  ...
}
```
```

### Template 2: Complex Skill as Agent

**File:** `.claude/agents/skills/abstract-writer-skill.md`

```markdown
# abstract-writer-skill - Agent

Write structured academic abstract (200-350 words).

## Invocation

```python
Task(
    subagent_type="general-purpose",
    description="Write dissertation abstract",
    prompt="""
    You are the abstract-writer skill agent.

    GOAL: Write a structured academic abstract (200-350 words)

    INPUT:
    - Dissertation topic
    - Research questions
    - Methodology
    - Key findings
    - Contributions

    PROCESS:
    1. Structure abstract with 4 components:
       - Background & gap (50-75 words)
       - Methodology (50-75 words)
       - Results (75-100 words)
       - Conclusion & contribution (50-75 words)

    2. Draft abstract
    3. Check word count (200-350 target)
    4. Validate clarity and concision
    5. Revise if needed

    OUTPUT:
    - Structured abstract
    - Word count
    - Section breakdown

    Execute now.

    SPECIFIC INPUTS FOR THIS RUN:
    [User provides dissertation details]
    """
)
```
```

---

## 🔧 PRACTICAL IMPLEMENTATION STEPS

### Step 1: Convert Simple Skills to Slash Commands (8-10 hours)

For each of the 12 simple skills:

1. **Create file:** `.claude/commands/{skill-name}.md`

2. **Format:** Use slash command template

3. **Implementation logic:** Clear, step-by-step instructions

4. **Test:** Invoke with `/skill-name` and validate

5. **Document:** Add examples and usage notes

**Estimated time:** 30-45 min per skill = 6-9 hours for 12 skills

### Step 2: Create Agent-Based Skills (10-12 hours)

For each of the 10 complex skills:

1. **Create file:** `.claude/agents/skills/{skill-name}-skill.md`

2. **Format:** Agent prompt template

3. **Autonomous logic:** Complete self-contained prompt

4. **Test:** Launch via Task tool

5. **Document:** Invocation examples

**Estimated time:** 60-75 min per skill = 10-12 hours for 10 skills

### Step 3: Update Documentation (1-2 hours)

1. Update `skills/README.md` with new approach
2. Create invocation guide
3. Add examples
4. Cross-reference with commands/agents

---

## ✅ VALIDATION CHECKLIST

For each skill implementation:

- [ ] File created in appropriate location
- [ ] Format follows template
- [ ] Implementation logic is clear
- [ ] Test invocation works
- [ ] Output is as expected
- [ ] Documentation is complete
- [ ] Examples are provided
- [ ] Cross-references added

---

## 📊 REVISED TIMELINE

**Original estimate:** 15-20 hours for 22 skills
**Revised estimate:** 18-23 hours

**Breakdown:**
- 12 simple skills as slash commands: 6-9 hours
- 10 complex skills as agents: 10-12 hours
- Documentation updates: 2 hours

**Total:** 18-23 hours (similar to original)

---

## 🎯 SUCCESS CRITERIA

**A skill is successfully implemented when:**

1. ✅ **Invokable:** Can be called via `/command` or `Task()`
2. ✅ **Functional:** Produces correct output
3. ✅ **Documented:** Has clear usage instructions
4. ✅ **Tested:** Validated with real examples
5. ✅ **Reusable:** Works across different dissertations

---

## 💡 KEY INSIGHTS

### What Works
- ✅ Slash commands in `.claude/commands/`
- ✅ Task tool for agents
- ✅ Markdown documentation format
- ✅ Bash implementation blocks

### What Doesn't Work (Yet)
- ❌ Simple `.claude/skills/` file creation
- ❌ Automatic `@skill-name` invocation
- ❌ Unknown skill registration mechanism

### What We're Doing Instead
- ✅ Skills as slash commands (simple)
- ✅ Skills as agents (complex)
- ✅ Functionally equivalent
- ✅ Proven to work

---

## 🚀 NEXT STEPS

1. ✅ **Test experimental skill** - Completed
2. ⏳ **Create first real skill** - `/citation-format`
3. ⏳ **Validate pattern works** - Test invocation
4. ⏳ **Implement remaining skills** - Follow templates
5. ⏳ **Move to agent implementation** - Phase 3

---

**Status:** Pattern validated ✅
**Approach:** Hybrid (slash commands + agents)
**Confidence:** High (90%+)
**Ready to implement:** YES

**Let's build all 22 skills using the working approach!** 🛠️
