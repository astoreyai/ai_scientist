# List All Research Templates

Display all 10 research templates with their purpose and reporting standards.

## Instructions

1. List all template directories in `templates/`
2. For each template, read the first 10 lines of `README.md`
3. Extract the **Purpose** and **Reporting Standard** information
4. Group templates by category
5. Format output with clear categorization
6. Add usage instructions showing how to copy templates

## Template Categories

**EVIDENCE SYNTHESIS** (3 templates):
- network_meta_analysis, scoping_review, systematic_review

**EXPERIMENTAL DESIGN** (3 templates):
- observational_study, pragmatic_trial, rct_study

**SPECIALIZED METHODS** (2 templates):
- computational_methods, quality_improvement

**ACADEMIC DEVELOPMENT** (2 templates):
- advisor_communication, phd_dissertation

## Output Format

Present as a well-formatted list:

```
📋 Research Assistant - Available Templates (10 total)

EVIDENCE SYNTHESIS
1. systematic-review
   Purpose: PRISMA 2020-compliant systematic review and meta-analysis
   Standard: PRISMA 2020 (27-item checklist)

2. scoping-review
   Purpose: [Purpose from README]
   Standard: [Standard from README]

3. network-meta-analysis
   Purpose: [Purpose from README]
   Standard: [Standard from README]

EXPERIMENTAL DESIGN
4. rct-study
   Purpose: Complete template for Randomized Controlled Trial research projects
   Standard: CONSORT 2010

[Continue for all categories]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Usage: Copy a template to your project directory
   Example: cp -r templates/systematic_review/ my_project/

📖 Details: Each template includes complete workflow, checklists, and examples
🎯 Quick Start: /quick-start for guided template selection
📚 Learn More: /tutorials for step-by-step guides using templates
```

## Implementation Notes

- Read from: `/home/aaron/github/astoreyai/ai_scientist/templates/`
- Extract Purpose from line starting with "**Purpose**:"
- Extract Reporting Standard from line starting with "**Reporting Standard**:"
- Use directory names with underscores replaced by hyphens for display
- Keep output concise and scannable
