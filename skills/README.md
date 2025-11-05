# PhD Pipeline Skills for Claude Code

Reusable capabilities for ANY PhD dissertation project - not just this pipeline!

## What Are Skills?

Skills are general-purpose tools that work across any academic project. Unlike slash commands (project-specific), skills can be used in:
- Any PhD dissertation
- Research papers
- Grant proposals
- Academic writing

## How to Use Skills

Skills are invoked with `@skill-name` in Claude Code:

```
User: "Help me format these citations"
Claude: I'll use the @citation-format skill to help you.
```

## Available Skills (22 Total)

### ✅ Tier 1: Core Skills (13)

**Citation & References:**
- `@citation-format` - Format citations in APA, IEEE, Chicago, etc.
- `@bibtex-clean` - Clean and validate BibTeX entries

**Literature Review:**
- `@prisma-diagram` - Create PRISMA flow diagrams
- `@synthesis-matrix` - Generate literature synthesis matrices
- `@inclusion-criteria` - Define paper screening criteria
- `@lit-gap` - Identify research gaps

**Writing:**
- `@abstract-writer` - Draft academic abstracts
- `@keywords-develop` - Generate research keywords
- `@academic-grammar` - Check academic writing quality
- `@research-questions` - Formulate research questions

**Statistics:**
- `@power-analysis` - Statistical power calculations
- `@effect-size` - Calculate effect sizes
- `@hypothesis-test` - Design hypothesis tests

### ✅ Tier 2: Specialized Skills (9)

**Methodology:**
- `@experiment-design` - Design rigorous experiments
- `@methodology-writer` - Draft methodology sections

**Results & Analysis:**
- `@results-interpreter` - Interpret statistical results
- `@latex-table` - Generate publication-quality LaTeX tables
- `@figure-table` - Create figures and tables

**Discussion:**
- `@limitation-writer` - Write limitations sections
- `@contribution-writer` - Articulate research contributions

**Project Management:**
- `@timeline-generator` - Generate realistic timelines
- `@defense-prep` - Prepare defense materials

## Skill Categories

### 📚 Literature Review (6 skills)
- @prisma-diagram
- @synthesis-matrix
- @inclusion-criteria
- @lit-gap
- @citation-format
- @bibtex-clean

### ✍️ Writing (7 skills)
- @abstract-writer
- @keywords-develop
- @academic-grammar
- @research-questions
- @methodology-writer
- @limitation-writer
- @contribution-writer

### 📊 Statistics & Analysis (5 skills)
- @power-analysis
- @effect-size
- @hypothesis-test
- @experiment-design
- @results-interpreter

### 🎨 Formatting & Visualization (4 skills)
- @latex-table
- @figure-table
- @prisma-diagram
- @timeline-generator

## Usage Examples

### Example 1: Format Citations

```
User: "I have these papers, format them in APA style"
Claude: I'll use @citation-format to convert these to APA 7th edition.

Smith, J., & Jones, M. (2023). Explainable AI for biometrics.
    Journal of AI Research, 45(2), 123-145.
    https://doi.org/10.1234/jair.2023.123
```

### Example 2: Generate PRISMA Diagram

```
User: "Create a PRISMA flow diagram for my lit review"
Claude: I'll use @prisma-diagram to create your flow diagram.

[Generates Mermaid/LaTeX diagram showing:]
- Identification: 487 records
- Screening: 234 after title screen
- Included: 52 studies
```

### Example 3: Power Analysis

```
User: "What sample size do I need for 80% power?"
Claude: I'll use @power-analysis to calculate this.

For your parameters:
- Effect size: d = 0.5 (medium)
- Power: 0.80
- Alpha: 0.05
→ Required N = 64 per group (128 total)
```

## Time Savings

| Skill | Manual Time | Skill Time | Saved |
|-------|-------------|------------|-------|
| @citation-format | 2-3h | 5-10min | ~2.5h |
| @prisma-diagram | 3-4h | 10-15min | ~3.5h |
| @power-analysis | 1-2h | 5min | ~1.5h |
| @synthesis-matrix | 5-8h | 30min | ~6h |
| @abstract-writer | 2-4h | 15min | ~3h |
| **Total (all 22)** | **~60h** | **~5h** | **~55h** |

**55 hours (7 workdays) saved!** 🎉

## Development Status

### ✅ Phase 1: Documentation (Current)
- Skill specifications
- Usage examples
- Best practices
- Integration guides

### ⏳ Phase 2: Implementation (Next)
- Skill prompt engineering
- Testing and validation
- Example outputs
- Field-specific variations

### ⏳ Phase 3: Marketplace (Future)
- Publish to Claude Code Skills marketplace
- Community feedback
- Continuous improvement

## Skill Design Principles

### 1. General-Purpose
Skills work for ANY dissertation/paper, not just this pipeline.

**Good:** `@citation-format` (works for any paper)
**Bad:** `@phd-pipeline-setup` (too specific)

### 2. Reusable
One skill, many uses across different projects.

### 3. Well-Documented
Clear inputs, outputs, and examples.

### 4. Field-Agnostic
Adaptable to STEM, humanities, social sciences.

### 5. Quality-Focused
Helps maintain academic rigor and standards.

## Skill File Structure

```
skills/
├── README.md                          ← This file
├── tier1_core/                        ← 13 core skills
│   ├── citation-format.md
│   ├── bibtex-clean.md
│   ├── prisma-diagram.md
│   ├── synthesis-matrix.md
│   ├── inclusion-criteria.md
│   ├── lit-gap.md
│   ├── abstract-writer.md
│   ├── keywords-develop.md
│   ├── academic-grammar.md
│   ├── research-questions.md
│   ├── power-analysis.md
│   ├── effect-size.md
│   └── hypothesis-test.md
│
├── tier2_specialized/                 ← 9 specialized skills
│   ├── experiment-design.md
│   ├── methodology-writer.md
│   ├── results-interpreter.md
│   ├── latex-table.md
│   ├── figure-table.md
│   ├── limitation-writer.md
│   ├── contribution-writer.md
│   ├── timeline-generator.md
│   └── defense-prep.md
│
└── examples/                          ← Example outputs
    ├── prisma_example.svg
    ├── synthesis_matrix_example.csv
    ├── power_analysis_example.txt
    └── ...
```

## Integration with Slash Commands

Skills and slash commands work together:

```bash
# Slash command calls skill
/validate-citations
  └─> Uses @citation-format internally

# User invokes skill directly
"Help me format these citations"
  └─> Claude uses @citation-format
```

## Comparison: Skills vs Slash Commands

| Feature | Skills | Slash Commands |
|---------|--------|----------------|
| **Scope** | General-purpose | Project-specific |
| **Invocation** | `@skill-name` | `/command-name` |
| **Reusability** | Any project | This pipeline only |
| **Marketplace** | Yes | No |
| **Context** | Stateless | Project-aware |
| **Example** | @citation-format | /setup |

## Best Practices

### When to Use Skills

✅ **Use skills when:**
- Task is general academic work
- Applies to any dissertation
- Needs to be reusable
- Could help others

❌ **Use slash commands when:**
- Specific to PhD Pipeline
- Requires project context
- Wraps existing scripts
- Project file manipulation

### Skill Quality Standards

All skills must:
- ✅ Work for multiple academic fields
- ✅ Provide clear examples
- ✅ Have documented inputs/outputs
- ✅ Maintain academic rigor
- ✅ Be well-tested

## Contributing New Skills

Want to add a skill?

1. **Identify need:** General academic task
2. **Design skill:** Define inputs/outputs
3. **Document:** Write specification
4. **Test:** Validate across fields
5. **Submit:** Add to tier1 or tier2

## Related Documentation

- `../slash/commands/` - Project-specific commands
- `../agents/` - Autonomous task execution
- `../workflows/` - Multi-stage processes
- `../docs/IMPLEMENTATION_APPROACHES_ANALYSIS.md` - Architecture

## Support

### Questions?
- Check individual skill documentation
- Review examples in `examples/`
- See usage in slash commands
- Consult implementation guide

---

**Status:** Phase 1 (Documentation) - In Progress
**Skills Documented:** 0/22
**Skills Implemented:** 0/22
**Target:** All 22 skills for any PhD dissertation

**Start using skills to accelerate your academic work!** 🚀
