# List All Available Tutorials

Display all 11 interactive tutorials with learning paths, duration, and prerequisites.

## Instructions

1. List all tutorial directories in `tutorials/` (sorted numerically 01-11)
2. For each tutorial, read the first 10 lines of `README.md`
3. Extract title (from `# Tutorial X:` header), **Duration**, **Prerequisites**, and **What you'll learn**
4. Group tutorials by learning track (Foundation, Specialized, Advanced)
5. Format output with clear progression and time estimates
6. Add learning path recommendations

## Tutorial Learning Tracks

**FOUNDATION TUTORIALS** (1-5):
- 01_getting_started, 02_literature_review, 03_experimental_design, 04_ai_check, 05_complete_workflow

**SPECIALIZED RESEARCH** (6-8):
- 06_multisite_trials, 07_mixed_methods, 08_grant_proposals

**ADVANCED METHODS** (9-11):
- 09_qualitative_research, 10_meta_analysis, 11_implementation_science

## Output Format

Present as a well-formatted list with learning tracks:

```
📚 Research Assistant - Available Tutorials (11 total, 8 hours content)

FOUNDATION TUTORIALS (Start Here)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Getting Started (15 min)
   Learn: Installation, basic plugin usage, invoking agents, using skills
   Prerequisites: Claude Code installed

2. Literature Review (45 min)
   Learn: Complete PRISMA 2020 workflow, multi-database searching, screening
   Prerequisites: Tutorial 1 completed

3. Experimental Design (40 min)
   Learn: NIH rigor standards, power analysis, randomization, CONSORT compliance
   Prerequisites: Tutorial 1 completed

[Continue for all tutorials...]

SPECIALIZED RESEARCH (Choose Based on Your Work)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. Multi-Site Trials (50 min)
   Learn: [What you'll learn from README]
   Prerequisites: [Prerequisites from README]

[Continue...]

ADVANCED METHODS (For Specific Methodologies)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. Qualitative Research (50 min)
   Learn: [What you'll learn from README]
   Prerequisites: [Prerequisites from README]

[Continue...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📖 Recommended Learning Paths:

🎯 Quick Start (1 hour):
   Tutorials 1 → 2 (abridged) → 5 (overview)

📊 Quantitative Research (3 hours):
   Tutorials 1 → 2 → 3 → 5 → 10

📝 Qualitative Research (2.5 hours):
   Tutorials 1 → 2 → 9 → 7

🔬 Complete Researcher (8 hours):
   All tutorials in order (1-11)

💡 Access: Read tutorials/[number]_[name]/README.md
🎯 Interactive: Follow along with real examples in each tutorial
```

## Implementation Notes

- Read from: `/home/aaron/github/astoreyai/ai_scientist/tutorials/`
- Parse README.md headers carefully (lines 1-6)
- Extract duration from "**Duration**: X minutes"
- Extract prerequisites from "**Prerequisites**: ..."
- Extract learning objectives from "**What you'll learn**: ..."
- Total content: 280KB, approximately 8 hours
- Present learning paths for different research types
