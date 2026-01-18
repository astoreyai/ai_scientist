# Quick Start Guide

Interactive getting started guide for the Research Assistant plugin.

## Instructions

1. Greet the user and assess their research needs
2. Guide them through initial setup verification
3. Recommend appropriate starting point based on their project type
4. Provide specific next steps with commands

## Quick Start Workflow

### Step 1: Verify Installation

Ask Claude to verify the installation by checking for key resources:
- Confirm 22 skills are available (`/skills`)
- Confirm 10 agents are available (`/agents`)
- Confirm 10 templates are available (`/templates`)
- Confirm 11 tutorials are available (`/tutorials`)

### Step 2: Identify Research Type

Ask the user what type of research they're conducting:

**A. Systematic Review / Evidence Synthesis**
- Start with: `/tutorials` → Tutorial 2 (Literature Review)
- Use template: `cp -r templates/systematic_review/ my_project/`
- Launch agent: Use Task tool with subagent_type="literature-reviewer"

**B. Experimental Study (RCT)**
- Start with: `/tutorials` → Tutorial 3 (Experimental Design)
- Use template: `cp -r templates/rct_study/ my_project/`
- Launch agent: Use Task tool with subagent_type="experiment-designer"

**C. Observational Study**
- Use template: `cp -r templates/observational_study/ my_project/`
- Check protocol: `/protocols` for STROBE checklist
- Launch agent: Use Task tool with subagent_type="experiment-designer"

**D. Meta-Analysis**
- Start with: `/tutorials` → Tutorial 10 (Meta-Analysis)
- Use template: `cp -r templates/network_meta_analysis/ my_project/` (if comparing treatments)
- Use skill: Skill tool with skill="meta-analysis"

**E. Qualitative Research**
- Start with: `/tutorials` → Tutorial 9 (Qualitative Research)
- Check protocol: `/protocols` for COREQ checklist
- Use skills: Skill tool with skill="research-questions"

**F. Grant Proposal (NIH R01)**
- Start with: `/tutorials` → Tutorial 8 (Grant Proposals)
- Use template: `cp -r templates/phd_dissertation/ my_project/` (adapt for grant)
- Check protocol: `/protocols` for NIH rigor standards

**G. PhD Dissertation**
- Use template: `cp -r templates/phd_dissertation/ my_project/`
- Use template: `cp -r templates/advisor_communication/ my_communication/`
- Start with: `/tutorials` → Tutorial 1, then Tutorial 5 (Complete Workflow)

**H. Quality Improvement Project**
- Use template: `cp -r templates/quality_improvement/ my_project/`
- Check protocol: `/protocols` for SQUIRE 2.0
- Start with tutorials on experimental design

**I. Not Sure / Exploring**
- Start with: `/tutorials` → Tutorial 1 (Getting Started)
- Browse: `/skills` to see what's available
- Browse: `/agents` to understand capabilities

### Step 3: First Action Checklist

Provide a personalized checklist based on their research type:

```
🚀 Your Quick Start Checklist

[ ] Read Tutorial [X] ([topic]) - [estimated time]
[ ] Copy template: cp -r templates/[template-name]/ my_project/
[ ] Review protocol: /protocols and check [PROTOCOL NAME]
[ ] Set up project structure (create folders for data, analysis, docs)
[ ] Launch first agent: [agent name] or use first skill: [skill name]
[ ] (Optional) Review relevant additional tutorials

Next Steps:
1. [Specific action based on research type]
2. [Specific action based on research type]
3. Use /agent [agent-name] when ready for complex tasks
```

## Output Format

Present as an interactive guide:

```
🎯 Research Assistant - Quick Start Guide

Welcome! Let's get you started with the right resources for your research.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: Verify Installation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ 22 Skills available (/skills to browse)
✓ 10 Agents ready (/agents to see specialists)
✓ 10 Templates ready (/templates to browse)
✓ 11 Tutorials available (/tutorials for learning paths)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: What Type of Research Are You Doing?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Select your research type for personalized guidance:

📊 A. Systematic Review / Meta-Analysis
   → Tutorial 2, literature-reviewer agent, PRISMA 2020

🔬 B. Randomized Controlled Trial (RCT)
   → Tutorial 3, experiment-designer agent, CONSORT

📈 C. Observational Study
   → Templates, experiment-designer agent, STROBE

📉 D. Meta-Analysis (Statistical)
   → Tutorial 10, meta-analysis skill, R/Python code

💬 E. Qualitative Research
   → Tutorial 9, research-questions skill, COREQ

💰 F. Grant Proposal (NIH R01)
   → Tutorial 8, NIH rigor protocol

🎓 G. PhD Dissertation
   → Tutorial 5, phd_dissertation template

📋 H. Quality Improvement
   → quality_improvement template, SQUIRE 2.0

❓ I. Not Sure / Exploring
   → Tutorial 1 (15 min), then browse /skills and /agents

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👉 Tell me your research type (A-I) and I'll provide your personalized
   quick start checklist with specific commands and next steps!

💡 Or ask: "I'm doing [describe your research]" for guidance
```

## Implementation Notes

- Interactive and conversational approach
- Provide specific, actionable commands
- Estimate time commitments (tutorials are 15-60 min each)
- Cross-reference protocols, templates, tutorials, skills, agents
- Personalize based on user's specific research needs
- Keep checklist concrete and achievable
