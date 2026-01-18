# QUICK START GUIDE
## How to Use the Dissertation AI Prompt Chain System

---

## 🎯 WHAT IS THIS SYSTEM?

This is a **reproducible, systematic pipeline** of AI prompts designed to assist you through every stage of your dissertation, from topic selection to defense preparation.

Each stage contains:
- **Detailed prompts** you can copy and use with AI (like Claude)
- **Clear inputs** you need to provide
- **Specific outputs** you should receive
- **Quality checks** to verify you're ready to move forward
- **Iteration guidance** for when things need refinement

---

## 📚 THE FILES EXPLAINED

### 01_SYSTEM_OVERVIEW.md
**PURPOSE:** Your roadmap - shows how all pieces fit together
**WHEN TO USE:** Start here! Read this first to understand the system
**KEY INFO:**
- Overall structure of 6 stages
- Pipeline workflow
- How files connect to each other

### 02_TOPIC_DEVELOPMENT.md
**PURPOSE:** Develop and refine your dissertation topic
**WHEN TO USE:** At the very beginning of your dissertation journey
**CONTAINS:**
- 5 prompts for topic development, gap analysis, RQ formulation, theoretical framework, and scope
- Quality checks before moving to literature review

### 03_LITERATURE_REVIEW.md
**PURPOSE:** Conduct systematic literature search and write literature review
**WHEN TO USE:** After topic is approved
**CONTAINS:**
- 8 prompts covering scoping, search strategy, citation analysis, PRISMA, synthesis, and writing
- Based on systematic review methodology

### 04_METHODOLOGY.md
**PURPOSE:** Design your research methodology
**WHEN TO USE:** After literature review is substantially complete
**CONTAINS:**
- 8 prompts for paradigm, design, sampling, instruments, analysis plan, validity, ethics, and writing
- Critical: Get committee and IRB approval before data collection

### 05_DATA_ANALYSIS.md
**PURPOSE:** Collect and analyze your data
**WHEN TO USE:** After methodology approved and IRB obtained
**CONTAINS:**
- 8 prompts for data management, quality monitoring, cleaning, quant analysis, qual analysis, mixed methods, interpretation, and visualization

### 06_WRITING.md
**PURPOSE:** Write all major dissertation chapters
**WHEN TO USE:** After data analysis is complete
**CONTAINS:**
- 11 prompts for Results, Discussion, Introduction, Conclusion chapters and integration

### 07_FINALIZATION.md
**PURPOSE:** Finalize dissertation and prepare for defense
**WHEN TO USE:** After all chapters are drafted
**CONTAINS:**
- 7 prompts for abstract, references, front matter, formatting, appendices, proofreading, and defense prep

### 08_QUALITY_CHECKLIST.md
**PURPOSE:** Track your progress and verify quality at each stage
**WHEN TO USE:** Throughout your entire dissertation - refer to it constantly
**CONTAINS:**
- Comprehensive checklists for every stage
- Progress trackers
- Red flags to watch for
- Risk management strategies

### 09_AUTONOMOUS_AGENT_SYSTEM.md
**PURPOSE:** Understand how to use LLMs as autonomous agents
**WHEN TO USE:** If you want to automate the entire pipeline
**CONTAINS:**
- Architecture for self-executing AI systems
- How to build iterative loops
- Complete example: autonomous systematic review

### 10_READY_TO_USE_ORCHESTRATOR.md
**PURPOSE:** Copy-paste autonomous agent prompt
**WHEN TO USE:** When you want AI to execute a complete systematic review autonomously
**CONTAINS:**
- Ready-to-use orchestrator prompt
- Instructions for autonomous execution
- Example outputs

---

## 🚀 HOW TO GET STARTED

### Step 1: Understand Where You Are

Ask yourself:
- Do I have a dissertation topic? → **Start at File 02**
- Is my topic approved but I need to do lit review? → **Start at File 03**
- Is my lit review done, need methodology? → **Start at File 04**
- Is my methodology approved, ready for data? → **Start at File 05**
- Do I have data analyzed, ready to write? → **Start at File 06**
- Are chapters drafted, need to finalize? → **Start at File 07**

**In general:** Start from the beginning unless you've already completed earlier stages.

### Step 2: Read the Relevant File

Open the file for your current stage and:
1. Read the subcomponents to understand what's involved
2. Check the "Required Information" to see what you need to provide
3. Review the "Deliverables" to know what outputs you'll create
4. Read through all prompts to understand the workflow

### Step 3: Use the Prompts

For each prompt in the file:

1. **Copy the prompt text** from the file
2. **Fill in the placeholders** with your specific information
   - Replace `[PASTE RESEARCH QUESTIONS]` with your actual research questions
   - Replace `[YOUR FIELD]` with your discipline
   - Replace `[SOFTWARE]` with the tools you're using
   - Etc.
3. **Paste into AI assistant** (like Claude, ChatGPT, etc.)
4. **Provide any additional context** requested in "USER INPUT REQUIRED"
5. **Review the output** you receive
6. **Refine and iterate** if needed by asking follow-up questions
7. **Save the output** in your organized folder structure
8. **Move to next prompt**

### Step 4: Check Quality Before Moving On

Before advancing to the next stage:
1. Open **File 08** (Quality Checklist)
2. Find the section for your current stage
3. Go through **every checkbox** in the Quality Checks section
4. If something isn't checked, return to relevant prompt and address it
5. Review "Red Flags" section to identify potential issues
6. Only proceed when ALL quality checks pass

### Step 5: Repeat for Each Stage

Work through the files sequentially:
- Complete all prompts in File 02
- Check quality in File 08
- Committee approval
- Move to File 03
- Complete all prompts in File 03
- Check quality in File 08
- Committee approval
- Move to File 04
- And so on...

---

## 💡 EXAMPLE WORKFLOW: Using a Single Prompt

Let's walk through **Prompt 2.1** (Define Inclusion & Exclusion Criteria) as an example:

### STEP 1: Locate the Prompt
Open `03_LITERATURE_REVIEW.md`, find Prompt 2.1

### STEP 2: Check Required Inputs
The prompt requires:
- Research questions from Stage 1
- Scope definition from Stage 1

*Make sure you have these ready!*

### STEP 3: Read the Full Prompt
The prompt says:
```
My research questions are:
[PASTE RESEARCH QUESTIONS]

My defined scope is:
[PASTE SCOPE DEFINITION]

Help me create rigorous inclusion and exclusion criteria for my literature search:
[rest of prompt...]
```

### STEP 4: Customize with Your Info
Replace the placeholders:
```
My research questions are:
RQ1: How does social media use affect adolescent mental health?
RQ2: What moderating factors influence this relationship?
RQ3: What interventions show promise for mitigating negative effects?

My defined scope is:
This study focuses on adolescents ages 13-18 in Western countries, examining Instagram, TikTok, and Snapchat use over the past 5 years (2019-2024). It excludes Facebook and X/Twitter use, focuses on mental health outcomes (anxiety, depression, self-esteem), and does not examine academic or physical health outcomes.

Help me create rigorous inclusion and exclusion criteria for my literature search:
[rest of prompt...]
```

### STEP 5: Paste to AI
Copy your customized prompt and paste it to Claude (or your AI assistant of choice)

### STEP 6: Review Output
Claude will provide:
- Detailed inclusion criteria
- Exclusion criteria
- Screening criteria
- Decision tree
- Edge case examples

### STEP 7: Save Output
Save Claude's response to:
`/Dissertation_Project/02_Literature_Review/inclusion_exclusion_criteria.md`

### STEP 8: Move to Next Prompt
Continue to Prompt 2.2 (Develop Search Strategy)

---

## 🎯 PRO TIPS FOR SUCCESS

### 1. Don't Skip Steps
- Each prompt builds on previous ones
- Skipping creates gaps that cause problems later
- If you're tempted to skip, ask: "Why do I want to skip this?"

### 2. Keep Everything Organized
Recommended folder structure (from File 01):
```
/Dissertation_Project/
  /01_Topic_Development/
  /02_Literature_Review/
  /03_Methodology/
  /04_Data_Analysis/
  /05_Writing/
  /06_Finalization/
  /AI_Outputs/ (save all AI responses here)
  /Committee_Feedback/
  /Drafts_Archive/
```

### 3. Customize Prompts to Your Field
- These prompts are templates - adapt them!
- Add field-specific terminology
- Adjust for qualitative vs quantitative emphasis
- Include discipline-specific methods or requirements

### 4. Iterate When Needed
If AI output isn't quite right:
- Ask follow-up questions
- Provide more context
- Be more specific about what you need
- Try rephrasing the prompt
- Use the "🔄 Iteration Guidance" in each file

### 5. Use Quality Checks Religiously
- Quality checks prevent:
  * Wasted time on wrong directions
  * Major revisions later
  * Committee rejection
  * Redoing work
- Better to catch issues early!

### 6. Save AI Conversations
- Copy and save all AI outputs
- Date stamp them
- Note which prompt was used
- Document your iterations and refinements

### 7. Committee Check-ins
Schedule committee reviews at these critical points:
- ✅ After File 02 (Topic approved)
- ✅ After File 03 (Lit review approved)
- ✅ After File 04 (Methodology approved) **CRITICAL**
- ✅ After File 06 (Full draft reviewed)

### 8. Adapt Timeline to Your Situation
General timeline (full-time student):
- Stage 1 (Topic): 1-2 months
- Stage 2 (Lit Review): 2-4 months
- Stage 3 (Methodology): 1-2 months
- Stage 4 (Data): 3-6 months (highly variable)
- Stage 5 (Writing): 2-4 months
- Stage 6 (Finalization): 1-2 months

**Total: 10-20 months** (but can vary widely!)

### 9. Use Multiple AI Tools
Consider using:
- Claude for analytical tasks and writing
- ChatGPT for brainstorming and drafting
- Perplexity for literature searches
- Consensus.ai for research synthesis

### 10. Remember the Human Element
AI is a tool to:
- ✅ Structure your thinking
- ✅ Generate drafts and ideas
- ✅ Provide frameworks
- ✅ Organize your work

AI does NOT:
- ❌ Replace your expertise
- ❌ Replace your advisor
- ❌ Replace your critical thinking
- ❌ Guarantee acceptance (you still need to review and refine!)

---

## 🚨 COMMON MISTAKES TO AVOID

### Mistake #1: Using Prompts Without Customization
**Problem:** Generic outputs that don't fit your specific research
**Solution:** Always fill in ALL placeholders with your specific information

### Mistake #2: Not Saving Outputs
**Problem:** Lose valuable AI-generated content, can't track your progress
**Solution:** Immediately save every AI output to organized folders

### Mistake #3: Skipping Quality Checks
**Problem:** Advance with flawed work, causes bigger problems later
**Solution:** Complete ALL quality checks before moving to next stage

### Mistake #4: Working in Isolation
**Problem:** No feedback, potential wrong directions, burnout
**Solution:** Regular advisor meetings, peer support, committee check-ins

### Mistake #5: Treating AI Output as Final
**Problem:** Unrefined, generic, or incorrect content in dissertation
**Solution:** Always review, refine, and customize AI outputs

### Mistake #6: Changing Direction Mid-Stream
**Problem:** Wasted work, confusion, delays
**Solution:** Commit to decisions at each stage, only change with advisor approval

### Mistake #7: Not Backing Up Work
**Problem:** Lost work due to technical failure
**Solution:** Save everything in multiple locations (cloud + local)

---

## 🔧 TROUBLESHOOTING

### "The AI output doesn't make sense for my field"
→ Provide more field-specific context in your prompt
→ Include examples from your field
→ Explicitly state your field's norms and expectations

### "I'm getting generic responses"
→ Be more specific in your inputs
→ Provide more context and details
→ Show examples of what you're looking for
→ Ask follow-up questions to refine

### "I don't know how to answer a prompt's required inputs"
→ Return to previous stage - you may have skipped something
→ Consult with advisor
→ Review related prompts for guidance

### "My committee disagrees with AI suggestions"
→ Committee trumps AI always
→ Document committee's feedback
→ Modify prompts to align with committee expectations
→ Use AI to help implement committee's direction

### "I'm overwhelmed by the number of prompts"
→ Remember: you don't do all 50+ prompts at once!
→ Focus on current stage only
→ One prompt at a time
→ Break down large prompts into smaller pieces
→ Take breaks between prompts

### "My results don't match what the prompt expected"
→ Research findings are unpredictable - this is normal!
→ Use iteration prompts to adapt
→ Adjust subsequent prompts based on your actual results
→ This is okay - the system is flexible!

---

## 📋 QUICK REFERENCE: When to Use Each File

| Your Situation | Start With | Complete | Before Moving On |
|----------------|-----------|----------|------------------|
| Just starting dissertation | File 02 | All 5 prompts | Committee approval of topic |
| Have topic, need lit review | File 03 | All 8 prompts | Lit review draft + gap clear |
| Have lit review, need methods | File 04 | All 8 prompts | Committee + IRB approval |
| Have IRB approval, ready for data | File 05 | Prompts 4.1-4.3 | Data collection started |
| Data collected, need to analyze | File 05 | Prompts 4.4-4.8 | All findings documented |
| Have findings, need to write | File 06 | All 11 prompts | Full draft complete |
| Have draft, need to finalize | File 07 | All 7 prompts | Defense + submission |

---

## ✅ SUCCESS CHECKLIST

You're using this system correctly if you:
- [ ] Read File 01 (Overview) first
- [ ] Working through files sequentially
- [ ] Customizing every prompt with your specific information
- [ ] Saving all AI outputs in organized folders
- [ ] Using File 08 quality checks at every stage
- [ ] Getting committee approval at key milestones
- [ ] Iterating on outputs until they're truly useful
- [ ] Treating AI as a tool, not the final answer
- [ ] Maintaining backup copies of everything
- [ ] Tracking your progress systematically

---

## 🎓 FINAL THOUGHTS

This system is designed to:
- **Remove ambiguity** about what to do next
- **Provide structure** when the process feels overwhelming
- **Ensure quality** at every stage
- **Save time** through systematic approaches
- **Reduce anxiety** by breaking the huge task into manageable pieces

**Remember:**
- You don't have to be perfect
- Progress is better than perfection
- One step at a time
- This is a marathon, not a sprint
- Thousands have done this before you - and you can too!

---

## 🆘 NEED HELP?

If stuck:
1. Check the "Iteration Guidance" in the relevant file
2. Review "Troubleshooting" section above
3. Consult File 08 for red flags and solutions
4. Talk to your advisor (they're there to help!)
5. Connect with fellow dissertation students
6. Take a break and come back fresh

---

## 🚀 READY TO BEGIN?

1. **Read** this Quick Start Guide ✓
2. **Read** File 01 (Overview) to understand the system
3. **Assess** where you are in the process
4. **Open** the relevant stage file
5. **Begin** with Prompt X.1
6. **Use** the AI to work through each prompt
7. **Check** quality before advancing
8. **Move forward** one step at a time

**You've got this!**

Now go start with the appropriate file for your current stage. The system will guide you from there.

*Good luck, future Doctor!* 🎓
