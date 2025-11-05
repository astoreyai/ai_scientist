# Quick Start Guide - PhD Dissertation Pipeline

**Time Required:** 10 minutes to setup, then follow systematic workflows

---

## 🚀 GET STARTED IN 3 STEPS

### Step 1: Setup (2 minutes)

```bash
# Navigate to the pipeline directory
cd /path/to/PHD_PIPELINE_STANDALONE

# Make scripts executable
chmod +x automation/scripts/*.sh

# Initialize your dissertation
./automation/scripts/setup.sh MY_DISSERTATION

# Navigate to your new dissertation
cd MY_DISSERTATION
```

**What just happened?**
- Created complete dissertation directory structure
- Copied all chapter templates
- Set up LaTeX compilation environment
- Created progress tracking files
- Initialized bibliography system

---

### Step 2: Configure (3 minutes)

```bash
# Edit the configuration file
nano config.yaml
```

**Fill in these fields:**
```yaml
dissertation:
  title: "Your Dissertation Title"
  author: "Your Full Name"
  university: "Your University"
  department: "Your Department"
  degree: "Doctor of Philosophy in [Field]"

advisor:
  name: "Advisor Name"
  title: "Professor/Dr."
  email: "advisor@university.edu"

research:
  field: "Your Research Area"
  keywords:
    - keyword1
    - keyword2
    - keyword3
```

---

### Step 3: Start Working (5 minutes)

```bash
# Read the orientation guide
cat ../workflows/00_quick_start.md

# Begin topic development
cat ../workflows/01_topic_development.md

# Review chapter templates
ls -la chapters/
```

**You're now ready to start!**

---

## 📅 YOUR FIRST WEEK

### Day 1: Topic Definition
```bash
# Follow topic development workflow
cat ../workflows/01_topic_development.md

# Define your research questions
# Document in: chapters/chapter_01_introduction.md
```

**Tasks:**
1. Brainstorm research topics
2. Conduct preliminary gap analysis
3. Formulate 3-5 research questions
4. Define scope boundaries

**Deliverable:** Research questions document

---

### Day 2-3: Literature Scoping
```bash
# Start literature review planning
cat ../workflows/02_literature_review.md

# Set up automated Scopus search
cd ../tools/literature_review/automated_scopus/
cat README.md
```

**Tasks:**
1. Define inclusion/exclusion criteria
2. Develop search keywords
3. Plan database searches

**Deliverable:** Search protocol document

---

### Day 4-5: Preliminary Literature Review
```bash
# Begin collecting papers
# Use Scopus automation or manual search
```

**Tasks:**
1. Run initial searches (50-100 papers)
2. Title screening
3. Create preliminary bibliography

**Deliverable:** Initial paper list

---

## 🎯 YOUR FIRST MONTH

### Week 1: Topic & Scoping (see above)
### Week 2-3: Systematic Literature Review
```bash
# Full literature review workflow
cd MY_DISSERTATION
cat ../workflows/02_literature_review.md
```

**Tasks:**
1. Complete Scopus automated search
2. Screen 200-500 papers
3. Select final 50-150 papers
4. Create synthesis matrix

### Week 4: Methodology Planning
```bash
# Design your research
cat ../workflows/03_methodology.md
```

**Tasks:**
1. Select research paradigm
2. Design study methodology
3. Plan data collection
4. Draft Chapter 4

---

## 📊 TYPICAL TIMELINE

### Months 1-3: Foundation
- ✅ Topic development
- ✅ Comprehensive literature review
- ✅ Methodology design
- ✅ Chapters 1-2 drafted

### Months 4-10: Research Execution
- ✅ Data collection/experiments
- ✅ Implementation
- ✅ Results analysis
- ✅ Chapters 4-6 drafted

### Months 11-14: Writing & Finalization
- ✅ Complete all 8 chapters
- ✅ Multi-pass revision
- ✅ LaTeX compilation
- ✅ Quality checks

### Months 15-16: Defense
- ✅ Defense preparation
- ✅ Practice presentations
- ✅ Final revisions
- ✅ **Successful defense!**

**Total Time:** 12-16 months for full-time work

---

## 🛠️ ESSENTIAL TOOLS

### 1. Build Your Dissertation PDF
```bash
cd MY_DISSERTATION/latex
bash ../../automation/scripts/build_latex.sh
```

**When to use:** After writing any chapter, before submission

---

### 2. Automated Literature Review
```bash
cd ../tools/literature_review/automated_scopus/scripts

# Configure search
nano ../config/scopus_config.yaml

# Run search
python scopus_search.py --keywords "your,keywords" --years 2015-2025
```

**When to use:** During literature review phase (Month 1-2)

---

### 3. Quality Checks
```bash
# Check chapter completeness
cat ../tools/quality_assurance/chapter_quality_checklist.md

# Validate scientific rigor
cat ../tools/quality_assurance/scientific_validity_checklist.md
```

**When to use:** Before finalizing each chapter

---

### 4. Progress Tracking
```bash
# Update TODO list
nano progress/todo.md

# Review timeline
cat ../tools/progress_tracking/timeline_template.md
```

**When to use:** Weekly review and planning

---

## 💡 PRO TIPS

### Tip 1: Start with Templates
**Don't write from scratch!**
```bash
# Use chapter templates as starting points
cp ../templates/dissertation/chapter_01_introduction.md chapters/chapter_01_introduction.md

# Fill in the placeholders systematically
```

---

### Tip 2: Use AI Assistance
**The workflows contain AI-ready prompts:**

```markdown
# Example from workflow
**PROMPT TO AI:**
Help me develop search keywords for my research on [TOPIC].
My research questions are: [PASTE QUESTIONS]
```

Copy these prompts to Claude, ChatGPT, or your preferred AI assistant.

---

### Tip 3: Systematic > Perfect
**Complete workflows systematically, even if imperfect:**
- ✅ Finish one phase before moving to next
- ✅ Use checklists to ensure completeness
- ✅ Revise in dedicated revision passes
- ❌ Don't get stuck perfecting one section

---

### Tip 4: Regular Advisor Meetings
**Use email templates:**
```bash
cat ../templates/advisor_communication/progress_update.md
```

Schedule weekly/biweekly meetings to stay on track.

---

### Tip 5: Backup Everything
**Use the 3-2-1 rule:**
```bash
# Read backup protocol
cat ../tools/data_management/data_management_protocol.md
```

- 3 copies of all data
- 2 different storage mediums
- 1 off-site backup

---

## 🚨 COMMON MISTAKES TO AVOID

### ❌ Mistake 1: Skipping Quality Checks
**Don't submit chapters without running quality checks!**
- Use `tools/quality_assurance/chapter_quality_checklist.md`
- Validate every claim has evidence

### ❌ Mistake 2: No Clear Research Questions
**Everything flows from your research questions:**
- Define them early (Week 1)
- Keep them focused and specific
- Ensure they're answerable with your methodology

### ❌ Mistake 3: Poor Literature Organization
**Use systematic approach from day 1:**
- Follow PRISMA methodology
- Use reference manager (Zotero/Mendeley)
- Create synthesis matrix as you read

### ❌ Mistake 4: Writing Too Early
**Don't write Chapter 1 until you've:**
- ✅ Completed literature review
- ✅ Designed methodology
- ✅ Know your contribution

### ❌ Mistake 5: Ignoring Your Advisor
**Stay in communication:**
- Weekly/biweekly meetings
- Share drafts early and often
- Incorporate feedback promptly

---

## 📚 NEXT STEPS

**After completing this quick start:**

1. **Read the comprehensive guide:**
   ```bash
   cat docs/PIPELINE_GUIDE.md
   ```

2. **Review your first workflow:**
   ```bash
   cat workflows/01_topic_development.md
   ```

3. **Set up your tools:**
   - Install LaTeX: `sudo apt-get install texlive-full`
   - Install reference manager: Zotero or Mendeley
   - Get Scopus API access (through your university)

4. **Create your first deliverable:**
   - Draft research questions
   - Document in `chapters/chapter_01_introduction.md`

---

## ❓ GETTING HELP

**Questions about:**
- **Setup:** See `README.md`
- **Workflows:** See `workflows/*.md`
- **Tools:** See `tools/*/README.md`
- **LaTeX:** See `templates/latex/README.md`
- **Quality:** See `tools/quality_assurance/*.md`

**Still stuck?**
- Review the comprehensive pipeline guide
- Check the workflow documentation
- Consult your advisor
- Review example dissertations in your field

---

## ✅ COMPLETION CHECKLIST

Track your progress:

### Setup Phase
- [ ] Pipeline installed
- [ ] Dissertation initialized
- [ ] Config.yaml filled
- [ ] LaTeX tested
- [ ] Tools explored

### First Week
- [ ] Research questions defined
- [ ] Literature scoping complete
- [ ] Search protocol created
- [ ] Initial papers collected
- [ ] Advisor meeting scheduled

### First Month
- [ ] Systematic literature review complete
- [ ] 50-150 papers reviewed
- [ ] Synthesis matrix created
- [ ] Methodology designed
- [ ] Chapters 1-2 drafted

### Ready to Continue
- [ ] Workflows understood
- [ ] Tools mastered
- [ ] On track with timeline
- [ ] Confident in approach

---

**🎓 You're ready to complete your PhD systematically!**

**Remember:** This is a marathon, not a sprint. Use the pipeline to maintain consistent progress over 12-16 months.

**Next:** Read `workflows/01_topic_development.md` and begin!
