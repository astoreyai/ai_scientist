# Tutorial 1: Getting Started with Research Assistant

**Duration**: 15 minutes  
**Prerequisites**: Claude Code installed, Research Assistant plugin installed  
**What you'll learn**: Basic plugin usage, invoking agents, using skills

---

## Overview

This tutorial introduces the Research Assistant plugin for Claude Code. You'll learn how to:

1. Verify installation
2. Invoke your first agent
3. Use a research skill
4. Understand outputs

By the end, you'll be comfortable with the basic workflow.

---

## Step 1: Verify Installation

First, let's confirm the plugin is properly installed.

**Action**: In Claude Code, run:

```
/skill list
```

**Expected Output**: You should see 22+ skills including:
- ai-check
- citation-format
- power-analysis
- effect-size
- prisma-diagram
- ... and 17 more

**✓ Checkpoint**: If you see the skill list, the plugin is installed correctly.

**Troubleshooting**: If skills don't appear:
1. Check plugin installation: `/plugin list`
2. Reinstall if needed: `/plugin install research-assistant@research-assistant-marketplace`
3. Restart Claude Code

---

## Step 2: Invoke Your First Agent

Let's use the `literature-reviewer` agent to understand how agents work.

**Action**: Type the following:

```
/agent literature-reviewer

I'm a PhD student studying mindfulness interventions for anxiety. 
I need to conduct a systematic literature review.
Can you help me get started?
```

**What Happens**:
1. The agent loads with specialized knowledge of PRISMA 2020 guidelines
2. It asks clarifying questions about your review scope
3. It helps develop a search strategy
4. It explains the systematic review workflow

**Expected Questions from Agent**:
- What is your specific research question?
- What population are you studying?
- What intervention/exposure?
- What comparison group?
- What outcomes?
- What study designs to include?

**✓ Checkpoint**: The agent should respond with PRISMA-specific guidance.

**Example Agent Response**:
```
I'll help you conduct a PRISMA 2020 compliant systematic review. Let's start by 
defining your research question using the PICOS framework:

Population: Adults (18+) with anxiety disorders?
Intervention: Mindfulness-based interventions (MBSR, MBCT)?
Comparison: Usual care, waitlist control?
Outcome: Anxiety symptom reduction (measured how)?
Study design: RCTs only, or include observational studies?

Please clarify each component so we can develop a precise search strategy.
```

---

## Step 3: Use a Research Skill

Now let's use the `power-analysis` skill to calculate sample size.

**Action**: Type:

```
I need to calculate required sample size for an RCT:
- Design: Independent groups t-test
- Expected effect size: Cohen's d = 0.5 (medium effect)
- Alpha: 0.05
- Power: 0.80
- Two-tailed test
```

**What Happens**:
The power-analysis skill activates automatically (Claude recognizes the request matches skill description).

**Expected Output**:
```
Sample Size Calculation:

Design: Independent samples t-test (two-tailed)
Effect size: d = 0.50
Alpha: 0.05
Power: 0.80

Required N: 64 per group (128 total)

Accounting for 20% attrition:
Recruit: 160 participants (80 per group)

Sensitivity Analysis:
- Power to detect d = 0.40: 55%
- Power to detect d = 0.60: 95%

NIH-Formatted Justification:
Sample size was determined using G*Power 3.1 for an independent samples t-test. 
To detect a medium effect (d = 0.50) with 80% power and alpha = 0.05, we require 
64 participants per group (128 total). Accounting for anticipated 20% attrition, 
we will recruit 160 participants.
```

**✓ Checkpoint**: You should receive a complete sample size calculation with justification.

---

## Step 4: Understand Agent vs Skill

**Key Difference**:

| Feature | Agents | Skills |
|---------|--------|--------|
| **Invocation** | `/agent agent-name` | Automatic or explicit request |
| **Purpose** | Complex, multi-step workflows | Specific calculations/tasks |
| **Tools** | Full access (Read, Write, Bash, etc.) | Usually computation-only |
| **Examples** | Systematic reviews, experimental design | Power analysis, citation formatting |

**When to Use Agents**:
- Conducting a complete systematic review
- Designing an entire experiment
- Analyzing collected data
- Writing a manuscript

**When to Use Skills**:
- Calculating a specific statistic
- Formatting citations
- Checking for AI-generated text
- Creating a PRISMA diagram

---

## Step 5: Try the AI-Check Skill

Let's test the centerpiece feature: AI-generated text detection.

**Action**: Create a test file:

```bash
echo "This comprehensive study leverages robust methodologies to delve into the 
relationship between stress and health. Furthermore, the analysis demonstrates 
significant findings utilizing state-of-the-art techniques. Moreover, these 
results facilitate our understanding of this important phenomenon." > test_ai.txt
```

Then run:

```
Please run ai-check on test_ai.txt
```

**Expected Output**:
```
AI-Check Results for test_ai.txt

Overall Confidence: 75% (HIGH)
Verdict: Likely AI-generated

Issues Detected:
- Grammar perfection score: 95% (no natural errors)
- Sentence uniformity: 85% (all sentences 15-20 words)
- AI-typical words found (8 instances):
  • "comprehensive" (1)
  • "leverages" (1)
  • "robust" (1)
  • "delve" (1)
  • "utilizing" (1)
  • "facilitate" (1)
  • "furthermore" (1)
  • "moreover" (1)

Suggestions:
1. Replace AI-typical words:
   - "delve" → "examine", "investigate"
   - "leverage" → "use", "apply"
   - "utilizing" → "using"
   
2. Vary sentence length (currently all 15-20 words)
   
3. Remove excessive transition words:
   - "Furthermore" → consider omitting
   - "Moreover" → use simpler transitions
```

**✓ Checkpoint**: The ai-check should flag the obviously AI-generated text.

**Try with Human Text**: Create a file with natural writing and compare results.

---

## Step 6: Explore Documentation

Now that you understand the basics, explore the full documentation:

**Available Guides**:
- `docs/USER_GUIDE.md` - Complete user manual
- `docs/AGENT_REFERENCE.md` - All 10 agents documented
- `docs/SKILL_REFERENCE.md` - All 22 skills documented
- `docs/INSTALLATION.md` - Installation and configuration

**Action**: Read the relevant guide for your current needs.

---

## Next Steps

You've completed the Getting Started tutorial! You now know how to:
- ✅ Verify plugin installation
- ✅ Invoke agents
- ✅ Use research skills
- ✅ Run AI-check
- ✅ Access documentation

**Continue Learning**:
- [Tutorial 2: Literature Review](../02_literature_review/README.md) - Complete PRISMA workflow
- [Tutorial 3: Experimental Design](../03_experimental_design/README.md) - Design rigorous studies
- [Tutorial 4: AI-Check Deep Dive](../04_ai_check/README.md) - Master AI-detection
- [Tutorial 5: Complete Workflow](../05_complete_workflow/README.md) - End-to-end research

---

## Quick Reference

**Common Commands**:
```bash
/agent literature-reviewer    # Start systematic review
/agent experiment-designer     # Design study
/agent data-analyst           # Analyze data
/agent manuscript-writer      # Write paper
/skill list                   # See all skills
```

**Key Skills** (invoked automatically or explicitly):
- ai-check - Detect AI-generated text
- power-analysis - Calculate sample size
- effect-size - Calculate Cohen's d, etc.
- citation-format - Format references
- prisma-diagram - Create PRISMA flow diagram

---

*Tutorial created: 2025-11-10*  
*Version: 1.1.0*
