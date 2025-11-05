# @timeline-generator - Generate Realistic PhD Timelines

Generate realistic, achievable timelines for dissertation milestones and tasks.

## Skill Type
**Category:** Project Management / Planning
**Tier:** Specialized (Tier 2)
**Reusability:** Very High - every PhD student needs realistic timelines

## What This Skill Does

1. Creates phased dissertation timelines
2. Estimates task durations realistically
3. Identifies dependencies between tasks
4. Plans buffer time for setbacks
5. Generates Gantt charts and milestone schedules
6. Provides weekly/monthly breakdowns

## Invocation

```
@timeline-generator [start-date] [target-completion] [current-status]
```

## Timeline Phases

### Phase 1: Literature Review (2-4 months)
- Initial reading and note-taking
- PRISMA systematic review
- Gap identification
- Research question refinement

### Phase 2: Methodology Design (1-2 months)
- Experimental design
- Power analysis
- IRB approval (if needed)
- Pilot studies

### Phase 3: Data Collection / Experiments (2-6 months)
- Dataset preparation
- Running experiments
- Quality checks
- Preliminary analysis

### Phase 4: Analysis and Writing (3-6 months)
- Statistical analysis
- Results interpretation
- Chapter drafting (Chapters 4-6)
- Iterative advisor feedback

### Phase 5: Finalization (1-2 months)
- Complete all chapters
- LaTeX compilation
- Proofreading and revision
- Defense preparation

## Typical Task Durations

### Writing Tasks
- **Abstract:** 2-3 hours
- **Chapter 1 (Introduction):** 2-3 weeks
- **Chapter 2 (Literature Review):** 4-6 weeks
- **Chapter 3 (Theory/Framework):** 3-4 weeks
- **Chapter 4 (Methodology):** 2-3 weeks
- **Chapter 5 (Implementation):** 2-3 weeks
- **Chapter 6 (Results):** 3-4 weeks
- **Chapter 7 (Discussion):** 2-3 weeks
- **Chapter 8 (Conclusion):** 1-2 weeks

### Research Tasks
- **Literature search:** 1-2 weeks
- **PRISMA review:** 3-4 weeks
- **Experiment design:** 1-2 weeks
- **Pilot study:** 2-3 weeks
- **Full experiments:** 1-3 months (depends on compute)
- **Data analysis:** 2-4 weeks

### Administrative Tasks
- **IRB approval:** 1-3 months (if required)
- **Advisor meetings:** Weekly (1 hour/week)
- **Committee formation:** 1-2 weeks
- **Defense scheduling:** 2-4 weeks lead time

## Input Format

### Simple Timeline Request
```
@timeline-generator

Start: January 1, 2025
Target defense: December 15, 2025
Current status: Literature review complete, starting methodology

Generate full timeline with milestones.
```

### Detailed Status
```
@timeline-generator

Start: October 15, 2024
Target: June 1, 2025 (7.5 months remaining)

Completed:
- Literature review (Chapter 2) ✅
- Theoretical framework (Chapter 3) ✅
- Methodology designed (Chapter 4 drafted)

In progress:
- Running experiments (VGGFace2: 60% complete)

Not started:
- LFW experiments
- Results analysis (Chapter 6)
- Discussion (Chapter 7)
- Finalization

Constraints:
- Need 2 weeks for defense prep
- Advisor feedback: ~1 week turnaround
```

## Output Examples

### Example 1: Full Dissertation Timeline (12 months)

**Input:**
```
@timeline-generator

Start: January 1, 2025
Target defense: December 15, 2025
Starting from scratch (no chapters written yet)

Generate realistic 12-month timeline.
```

**Output:**

```markdown
# PhD Dissertation Timeline: 12-Month Plan

**Student:** [Your Name]
**Start Date:** January 1, 2025
**Target Defense:** December 15, 2025
**Total Duration:** 11.5 months

---

## Overview: 5 Phases

| Phase | Duration | Start | End | Key Deliverable |
|-------|----------|-------|-----|-----------------|
| **1. Literature Review** | 3 months | Jan 1 | Mar 31 | Chapter 2 complete |
| **2. Methodology Design** | 1.5 months | Apr 1 | May 15 | Chapter 4 complete |
| **3. Experiments & Data** | 3 months | May 16 | Aug 15 | Results data ready |
| **4. Analysis & Writing** | 3 months | Aug 16 | Nov 15 | Chapters 1, 5-7 complete |
| **5. Finalization** | 1 month | Nov 16 | Dec 15 | Defense-ready |

---

## Phase 1: Literature Review (Jan 1 - Mar 31)

### Month 1 (January)
**Weeks 1-2 (Jan 1-14):**
- Initial reading (20-30 papers)
- Identify key themes
- Set up Zotero/reference manager
- Draft research questions

**Weeks 3-4 (Jan 15-31):**
- PRISMA search protocol
- Database searches (OpenAlex, Google Scholar)
- Screen abstracts (n ≈ 200-300)
- Begin full-text review

### Month 2 (February)
**Weeks 5-6 (Feb 1-14):**
- Full-text review (include n ≈ 50-80)
- Data extraction
- Synthesis matrix creation

**Weeks 7-8 (Feb 15-28):**
- Draft Chapter 2 (Literature Review)
- Identify gaps
- Refine research questions
- **Advisor meeting:** Review draft

### Month 3 (March)
**Weeks 9-10 (Mar 1-14):**
- Revise Chapter 2 based on feedback
- Create PRISMA flowchart
- Finalize research questions

**Weeks 11-12 (Mar 15-31):**
- Draft Chapter 1 (Introduction)
- Write problem statement
- Outline contributions
- **Milestone:** Chapter 1 & 2 complete ✅

---

## Phase 2: Methodology Design (Apr 1 - May 15)

### Month 4 (April)
**Weeks 13-14 (Apr 1-14):**
- Design experiments (variables, conditions)
- Power analysis (determine n)
- Select datasets (VGGFace2, LFW)

**Weeks 15-16 (Apr 15-30):**
- Draft Chapter 4 (Methodology)
- Specify hypotheses
- Preregister study (OSF)
- **Advisor meeting:** Review design

### Month 5 (May 1-15)
**Weeks 17-18 (May 1-15):**
- Revise methodology based on feedback
- Pilot study (n = 20 pairs)
- Validate pipeline
- **Milestone:** Chapter 4 complete, ready for experiments ✅

---

## Phase 3: Experiments & Data (May 16 - Aug 15)

### Month 5-6 (May 16 - Jun 30)
**Weeks 19-22:**
- Data preparation (clean, preprocess)
- Run VGGFace2 experiments (n = 200)
- Monitor progress daily
- **Compute time:** ~2-3 weeks

### Month 7 (July)
**Weeks 23-26:**
- Run LFW experiments (n = 200)
- Quality checks (visual inspection)
- Outlier analysis
- **Milestone:** All experiments complete ✅

### Month 8 (Aug 1-15)
**Weeks 27-28:**
- Preliminary data analysis
- Descriptive statistics
- Check assumptions
- **Advisor meeting:** Review preliminary results

---

## Phase 4: Analysis & Writing (Aug 16 - Nov 15)

### Month 8-9 (Aug 16 - Sep 30)
**Weeks 29-30 (Aug 16-31):**
- Hypothesis testing (t-tests, ANOVA)
- Effect size calculations
- Create figures and tables

**Weeks 31-32 (Sep 1-15):**
- Draft Chapter 6 (Results)
- Report all statistical tests
- Generate visualizations

**Weeks 33-34 (Sep 16-30):**
- Draft Chapter 3 (Theoretical Framework)
- Formalize propositions/theorems
- **Advisor meeting:** Review Chapters 3 & 6

### Month 10 (October)
**Weeks 35-36 (Oct 1-15):**
- Revise Chapters 3 & 6
- Draft Chapter 5 (Implementation)
- Document code and methods

**Weeks 37-38 (Oct 16-31):**
- Draft Chapter 7 (Discussion)
- Interpret findings
- Compare to literature
- Address limitations
- **Advisor meeting:** Review Chapters 5 & 7

### Month 11 (November 1-15)
**Weeks 39-40 (Nov 1-15):**
- Revise all chapters based on feedback
- Finalize Chapter 1 (Introduction)
- Finalize Chapter 8 (Conclusion)
- **Milestone:** All 8 chapters drafted ✅

---

## Phase 5: Finalization (Nov 16 - Dec 15)

### Month 11-12 (Nov 16 - Dec 15)
**Weeks 41-42 (Nov 16-30):**
- LaTeX compilation
- Format figures, tables, references
- Proofread entire dissertation
- Fix all TODOs and placeholders
- **Advisor meeting:** Final review

**Weeks 43-44 (Dec 1-15):**
- Committee review (2 weeks)
- Prepare defense presentation
- Rehearse defense (3× minimum)
- Anticipate questions
- **Defense date:** December 15, 2025 🎓

---

## Weekly Time Allocation

**Full-time PhD student (40 hours/week):**
- **Dissertation work:** 30 hours/week
- **Advisor meetings:** 1 hour/week
- **Reading/learning:** 5 hours/week
- **Administrative:** 2 hours/week
- **Buffer:** 2 hours/week

**Part-time PhD student (20 hours/week):**
- Double all durations (24-month timeline instead of 12)

---

## Critical Milestones & Checkpoints

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| ✅ Research questions finalized | Jan 31, 2025 | |
| ✅ Chapter 2 (Literature) complete | Mar 31, 2025 | |
| ✅ Chapter 4 (Methodology) complete | May 15, 2025 | |
| ✅ Experiments complete | Jul 31, 2025 | |
| ✅ Chapters 3, 5, 6 complete | Oct 15, 2025 | |
| ✅ All chapters drafted | Nov 15, 2025 | |
| ✅ LaTeX compiled, defense-ready | Dec 1, 2025 | |
| 🎓 **Defense** | **Dec 15, 2025** | |

---

## Buffer Time & Risk Mitigation

### Built-in Buffers
- **1 week** between each phase (catch-up time)
- **2 weeks** for advisor feedback delays
- **1 week** for unexpected setbacks

### Contingency Plans
**If experiments take longer (e.g., 4 months instead of 3):**
- Reduce writing time by working in parallel (draft while experiments run)
- Extend timeline by 1 month (defense in January 2026)

**If major revisions required:**
- Use November buffer time
- Prioritize critical chapters (4, 6, 7)

**If advisor unavailable:**
- Get feedback from committee members or peers
- Schedule meetings 2-3 weeks in advance

---

## Tracking Progress

### Weekly Review (Every Friday)
- [ ] What did I complete this week?
- [ ] Am I on schedule?
- [ ] What blockers did I encounter?
- [ ] What's the plan for next week?

### Monthly Review (Last Day of Month)
- [ ] Did I hit this month's milestones?
- [ ] Do I need to adjust the timeline?
- [ ] What help do I need?

### Tools
- **Gantt chart:** Visual timeline (use Excel, Notion, or Trello)
- **TODO list:** Daily tasks (use TodoWrite skill)
- **Progress log:** Weekly summaries

---

## Advisor Communication Schedule

| Frequency | Purpose | Duration |
|-----------|---------|----------|
| **Weekly meetings** | Progress update, quick questions | 30-60 min |
| **Monthly review** | Chapter drafts, major decisions | 1-2 hours |
| **Critical checkpoints** | Methodology, results, final draft | 1-2 hours |

**Total advisor time:** ~50-60 hours over 12 months

---

## Defense Preparation Timeline (Last 2 Weeks)

### Week 1 (Dec 1-7)
- [ ] Create presentation slides (30-45 min talk)
- [ ] Rehearse presentation (alone)
- [ ] Anticipate 20-30 questions
- [ ] Prepare backup slides (extra analyses)

### Week 2 (Dec 8-14)
- [ ] Rehearse with advisor (get feedback)
- [ ] Rehearse with peers (practice Q&A)
- [ ] Rehearse with family (timing)
- [ ] Final polish of slides
- [ ] Rest day before defense (Dec 14)

### Defense Day (Dec 15)
- **Arrive 30 min early**
- **Test technology (slides, video, etc.)**
- **Deep breaths** 🧘
- **Defend!** 🎓
```

---

### Example 2: Accelerated Timeline (6 months, some work done)

**Input:**
```
@timeline-generator

Start: June 1, 2025
Target defense: December 1, 2025 (6 months)

Already complete:
- Chapters 1-4 (Introduction, Literature, Theory, Methodology)
- Experiments 80% done (should finish by June 15)

Need to complete:
- Finish experiments
- Analyze results
- Write Chapters 5-8
- Finalize and defend
```

**Output:**

```markdown
# Accelerated Timeline: 6 Months to Defense

**Start:** June 1, 2025
**Target Defense:** December 1, 2025
**Duration:** 6 months

**Current Status:**
✅ Chapters 1-4 complete
✅ Experiments 80% complete (finish by Jun 15)

---

## Phase Breakdown

| Phase | Duration | Dates | Deliverable |
|-------|----------|-------|-------------|
| **1. Finish Experiments** | 2 weeks | Jun 1-15 | All data collected |
| **2. Analysis** | 3 weeks | Jun 16 - Jul 6 | Chapter 6 drafted |
| **3. Writing (Ch 5, 7, 8)** | 6 weeks | Jul 7 - Aug 17 | All chapters drafted |
| **4. Revision** | 4 weeks | Aug 18 - Sep 14 | Polished chapters |
| **5. Finalization** | 6 weeks | Sep 15 - Nov 1 | Defense-ready |
| **6. Defense Prep** | 4 weeks | Nov 1 - Dec 1 | Presentation ready |

---

## Month-by-Month Plan

### June (Weeks 1-4)
**Jun 1-15:** Finish remaining experiments
**Jun 16-30:**
- Preliminary data analysis
- Descriptive statistics
- Check assumptions
- **Milestone:** Data ready for Chapter 6 ✅

### July (Weeks 5-8)
**Jul 1-15:**
- Draft Chapter 6 (Results)
- All statistical tests
- Create figures/tables
- **Advisor meeting:** Review Chapter 6

**Jul 16-31:**
- Draft Chapter 5 (Implementation)
- Revise Chapter 6 based on feedback
- **Milestone:** Chapters 5 & 6 complete ✅

### August (Weeks 9-12)
**Aug 1-15:**
- Draft Chapter 7 (Discussion)
- Draft Chapter 8 (Conclusion)

**Aug 16-31:**
- Revise all chapters (1-8)
- Integrate feedback
- **Advisor meeting:** Full draft review
- **Milestone:** All chapters drafted ✅

### September (Weeks 13-16)
**Sep 1-15:**
- Major revisions based on feedback
- Fill in any missing sections
- Polish writing

**Sep 16-30:**
- LaTeX compilation
- Format figures, tables, references
- Committee distribution (2-week review period)
- **Milestone:** Defense-ready draft ✅

### October (Weeks 17-20)
**Oct 1-15:**
- Committee review period
- Address any major concerns
- Finalize presentation outline

**Oct 16-31:**
- Create presentation slides
- Prepare backup slides
- Rehearse (3× minimum)

### November (Weeks 21-22)
**Nov 1-7:**
- Final rehearsals
- Anticipate questions

**Nov 8-Dec 1:**
- Committee feedback integration
- Final polish
- **Defense:** December 1, 2025 🎓
```

---

### Example 3: Gantt Chart (Visual Timeline)

```
## Gantt Chart: 12-Month Dissertation Timeline

Task                          Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
──────────────────────────────────────────────────────────────────────────────────────────
Literature Review             ███████████
  ├─ Initial reading          ████
  ├─ PRISMA search                 ████
  └─ Chapter 2 writing                  ████

Methodology Design                            ██████
  ├─ Experiment design                        ███
  └─ Chapter 4 writing                           ███

Experiments                                         ███████████
  ├─ VGGFace2                                     █████
  └─ LFW                                               ██████

Analysis & Writing                                              ███████████████
  ├─ Chapter 6 (Results)                                        █████
  ├─ Chapter 3 (Theory)                                            ████
  ├─ Chapter 5 (Implementation)                                       ████
  └─ Chapter 7 (Discussion)                                               ████

Finalization                                                                    ██████
  ├─ LaTeX compilation                                                          ███
  ├─ Defense prep                                                                  ███
  └─ Defense                                                                          🎓
```

---

## Time Savings

**Manual timeline creation:** 2-3 hours (estimating, adjusting, formatting)
**Using @timeline-generator:** 15-20 minutes (review, customize)
**Saved:** ~2.5 hours 🎉

## Best Practices

### 1. Be Realistic
Don't plan 80-hour weeks. Plan sustainable 40-50 hours.

### 2. Build in Buffers
Add 20% buffer time for unexpected delays.

### 3. Track Progress Weekly
Review timeline every Friday.

### 4. Adjust as Needed
Timeline is a living document, not set in stone.

### 5. Communicate with Advisor
Share timeline, get feedback early.

## Related Skills

- `@experiment-design` - Estimate experiment duration
- `@methodology-writer` - Plan methodology chapter timeline
- `@defense-prep` - Defense preparation timeline
- `@contribution-writer` - Plan writing phase

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 15-20 minutes
**Time saved:** ~2.5 hours
**Reusability:** Very High (every PhD student needs a timeline)
**Critical for:** Project management, staying on track, graduation planning
