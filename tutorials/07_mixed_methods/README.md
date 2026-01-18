# Tutorial 7: Qualitative + Quantitative Mixed Methods Research

**Duration**: 55 minutes
**Prerequisites**: Tutorials 1, 2, 3, 5 completed
**What you'll learn**: Mixed methods designs, thematic analysis, integration techniques, embedding qualitative in RCTs, GRAMMS reporting guidelines

---

## Overview

This tutorial demonstrates **mixed methods research** - combining qualitative and quantitative approaches for richer insights. You'll learn:

1. Choosing appropriate mixed methods designs (convergent, explanatory, exploratory)
2. Embedding qualitative research in RCTs
3. Conducting semi-structured interviews
4. Performing thematic analysis
5. Integrating quantitative and qualitative findings
6. Joint displays and meta-inferences
7. GRAMMS reporting guidelines (Good Reporting of A Mixed Methods Study)
8. Using qualitative analysis software (NVivo, MAXQDA, ATLAS.ti)
9. Ensuring rigor in qualitative research
10. Publishing mixed methods studies

**Running Example**: We'll add qualitative components to our RCT from Tutorial 3:
*"Why does online MBCT work? A mixed methods study embedding qualitative interviews in an RCT of mindfulness-based therapy for college student depression."*

**Why Mixed Methods**:
- **Complementarity**: Qualitative explains quantitative results
- **Completeness**: Full picture (what works + why/how)
- **Context**: Understanding implementation barriers
- **Participant voice**: Beyond numbers

---

## Part 1: Choosing a Mixed Methods Design (10 minutes)

### Step 1.1: Three Core Designs

**1. Convergent Parallel Design**

```
QUANTITATIVE DATA          QUALITATIVE DATA
    (same time)                (same time)
        ↓                          ↓
    Analysis                   Analysis
        ↓                          ↓
        └──────── MERGE ──────────┘
                    ↓
              INTERPRET
              
Timeline: Simultaneous collection
Purpose: Triangulation, corroboration
Example: RCT + interviews (both at baseline)
```

**2. Explanatory Sequential Design** ← WE'LL USE THIS

```
QUANTITATIVE DATA
        ↓
    Analysis
        ↓
    Results inform...
        ↓
  QUALITATIVE DATA
        ↓
    Analysis
        ↓
  INTERPRET (explain quant results)

Timeline: Quant first, qual second
Purpose: Explain quantitative results
Example: RCT shows effect → interviews explore why/how
```

**3. Exploratory Sequential Design**

```
QUALITATIVE DATA
        ↓
    Analysis
        ↓
    Results inform...
        ↓
QUANTITATIVE DATA
        ↓
    Analysis
        ↓
  INTERPRET (generalize qual findings)

Timeline: Qual first, quant second
Purpose: Develop survey/intervention from qualitative insights
Example: Interviews identify themes → survey measures prevalence
```

**Checkpoint**: Select design based on research question.

---

### Step 1.2: Our Research Questions

**Quantitative RCT Question** (from Tutorial 3):
> "Does 8-week online MBCT reduce depressive symptoms in college students vs. wait-list control?"

**Quantitative Result** (from Tutorial 5):
> **YES** - MBCT reduced PHQ-9 by 3.2 points more than control (d=0.68, p<0.001)

**New Qualitative Questions** (explanatory):
> 1. **Why** did MBCT work? What mechanisms did participants experience?
> 2. **How** did participants use mindfulness in daily life?
> 3. What **barriers** prevented some from benefiting?
> 4. Would participants **recommend** MBCT to others? Why/why not?

**Design Choice**: **Explanatory Sequential**
- Phase 1 (complete): Quantitative RCT showing efficacy
- Phase 2 (new): Qualitative interviews explaining results

**Checkpoint**: Explanatory design chosen because quan results need explanation.

---

## Part 2: Embedding Qualitative in RCTs (10 minutes)

### Step 2.1: Sampling Strategy

**Challenge**: Cannot interview all 214 RCT participants (too resource-intensive)

**Solution**: **Purposive sampling** to capture diverse experiences

```
Qualitative Sampling Plan:
═══════════════════════════════════════════════

Total Interviews: 30 participants (from n=214 RCT completers)

Sampling Criteria (purposive):
─────────────────────────────────────────────────
1. Treatment group: MBCT only (not control)
   Rationale: Understand MBCT mechanisms

2. Response variation: Sample across outcomes
   - High responders (n=10): PHQ-9 decreased ≥50%
   - Moderate responders (n=10): PHQ-9 decreased 25-49%
   - Non-responders (n=10): PHQ-9 decreased <25%
   
   Rationale: Understand why MBCT works for some but not all

3. Demographic diversity:
   - Gender: 60% female, 40% male (match RCT sample)
   - Age: Range 18-25 (span of inclusion)
   - Race/ethnicity: Representative of sample
   
   Rationale: Ensure diverse voices

4. Engagement level:
   - High engagement (n=15): Completed ≥7 of 8 modules
   - Low engagement (n=15): Completed 4-6 modules
   
   Rationale: Explore role of engagement

Recruitment:
─────────────────────────────────────────────────
- Invite all MBCT participants (n=107) via email at 8-week endpoint
- First 30 who respond and meet sampling criteria enrolled
- $50 gift card compensation (1-hour interview)

Saturation Plan:
─────────────────────────────────────────────────
- Initial target: 30 interviews
- Assess thematic saturation after 20 interviews
- If new themes emerging, extend to 40
- Stop when saturation reached (no new themes in 3 consecutive interviews)
```

**Checkpoint**: Purposive sampling ensures rich, diverse perspectives.

---

### Step 2.2: Interview Guide Development

**Action**: Create semi-structured interview guide

```markdown
# Semi-Structured Interview Guide: MBCT RCT Participants

**Introduction** (5 minutes)

"Thank you for participating in our study on online mindfulness therapy. As you know, we're interested in understanding your experience with the MBCT program. There are no right or wrong answers - I'm interested in YOUR honest thoughts and experiences. This interview will take about 45-60 minutes. Do you have any questions before we begin?"

**Consent**: "I'm going to record this conversation so I can transcribe it later. Is that okay?" [Start recording after verbal consent]

---

## SECTION 1: Overall Experience (10 minutes)

1. **Opening**: Can you tell me about your overall experience with the MBCT program?
   - Prompt: What stands out most to you when you think back on the 8 weeks?

2. **Expectations**: What were you hoping to get out of the program when you started?
   - Prompt: Did the program meet those expectations? Why or why not?

3. **Mechanisms**: Looking back, what do you think helped the most in the program?
   - Prompt: Can you give me a specific example of when mindfulness made a difference?

---

## SECTION 2: Mindfulness Practice (15 minutes)

4. **Daily Practice**: Tell me about your daily mindfulness practice during the 8 weeks.
   - Prompt: How often did you practice? When? Where?
   - Prompt: What made it easy or hard to practice regularly?

5. **Favorite Exercises**: Which mindfulness exercises did you find most helpful?
   - Prompt: Why that one? Can you walk me through how you did it?
   - Follow-up: Were there any you didn't find helpful?

6. **Real-World Application**: Can you describe a time when you used mindfulness in your daily life?
   - Prompt: What was happening? What did you do? What was the outcome?

7. **Challenges**: What was the hardest part about learning mindfulness?
   - Prompt: How did you deal with that challenge?

---

## SECTION 3: Depression and Wellbeing (10 minutes)

8. **Symptom Changes**: How did your depression symptoms change over the 8 weeks?
   - Prompt: What felt different? What stayed the same?

9. **Mechanisms of Change**: Why do you think your symptoms [improved/didn't improve]?
   - Prompt: What role did mindfulness play?
   - Prompt: What else might have contributed?

10. **Specific Symptoms**: Were there particular symptoms that mindfulness helped with?
    - Prompt: Sleep? Concentration? Motivation? Social relationships?

---

## SECTION 4: Online Delivery (10 minutes)

11. **Technology**: What was your experience with the online platform?
    - Prompt: Easy to navigate? Technical problems?

12. **Self-Guided**: How was it doing the program on your own without a therapist?
    - Prompt: What did you like about that? What was challenging?
    - Prompt: Did you ever wish you had a live instructor?

13. **Engagement**: What kept you engaged with the program?
    - Prompt: What made you keep coming back week after week?
    - Follow-up: Were there times you thought about quitting? What kept you going?

---

## SECTION 5: Barriers and Facilitators (10 minutes)

14. **Barriers**: What got in the way of participating fully in the program?
    - Prompt: Time? Motivation? Doubts? Other commitments?

15. **Facilitators**: What helped you participate in the program?
    - Prompt: Reminders? Accountability? Personal motivation?

16. **Improvements**: If you could change anything about the program, what would it be?

---

## SECTION 6: Future Use and Recommendations (5 minutes)

17. **Continued Practice**: Are you still practicing mindfulness now (after the 8 weeks)?
    - Prompt: Why or why not?
    - If yes: How often? In what situations?

18. **Recommendation**: Would you recommend this program to a friend with depression?
    - Prompt: Why or why not? What would you tell them?

---

## Closing (5 minutes)

19. **Anything Else**: Is there anything else about your experience that you think is important for us to know?

20. **Questions**: Do you have any questions for me?

**Thank you**: "Thank you so much for sharing your experiences with me. This information is incredibly valuable for understanding how mindfulness programs work and how we can improve them. Your $50 gift card will be emailed to you within 2 business days."

[Stop recording]
```

**Checkpoint**: Interview guide balances structure (key topics) with flexibility (open-ended).

---

### Step 2.3: Conduct Pilot Interviews

**Action**: Test interview guide with 3 pilot participants

```
Pilot Interview Learnings:
═══════════════════════════════════════════════

Issue 1: Question 9 too abstract
Original: "Why do you think your symptoms improved?"
Participants struggled with causal attribution

REVISED: "When you think about what helped with your depression, 
          what comes to mind? It could be the mindfulness program, 
          something else in your life, or a combination."

Issue 2: Question 17 needs timeframe
Original: "Are you still practicing mindfulness?"
Ambiguous (daily? weekly? ever?)

REVISED: "In the past week, have you practiced any mindfulness? 
          If yes, how many times?"

Issue 3: Interviews running long (75 minutes)
Solution: Combine questions 10 and 9, reduce prompts

Issue 4: Participants wanted to see their data
Solution: Bring printed graph of their PHQ-9 scores over time
          (visual aid improved conversation about symptom changes)

Final Guide: Version 2.0 (after pilot revisions)
Average interview length: 52 minutes ✓
```

**Checkpoint**: Pilot testing refined interview guide.

---

## Part 3: Data Collection and Transcription (5 minutes)

### Step 3.1: Conduct 30 Interviews

**Timeline**: Months 20-23 (after RCT 8-week endpoint completed)

```
Interview Logistics:
─────────────────────────────────────────────────
Format: Video (Zoom) or phone (participant choice)
  - Video: 23 participants
  - Phone: 7 participants (preferred phone for privacy)

Interviewer: Doctoral student trained in qualitative methods
  (NOT involved in intervention delivery - reduces bias)

Scheduling: Flexible (evenings/weekends offered for student schedules)

Recording: Zoom cloud recording + backup audio recorder

Field Notes: Interviewer documents:
  - Non-verbal cues (if video)
  - Participant emotion/engagement
  - Interviewer reflections
  - Emerging themes
```

**Checkpoint**: All 30 interviews completed in 3 months.

---

### Step 3.2: Transcription

**Action**: Convert audio to text

```bash
# Option 1: Professional transcription service (RECOMMENDED)
# Cost: ~$1.50/min = $90/hour = $2,700 for 30 interviews
# Turnaround: 5-7 business days
# Quality: 99% accuracy, verbatim

# Option 2: Automated transcription (Rev.ai, Otter.ai)
# Cost: ~$0.25/min = $15/hour = $450 for 30 interviews
# Turnaround: <24 hours
# Quality: 85-90% accuracy (requires manual correction)
# Time: +10 hours manual correction

# Our choice: Professional service (higher quality, saves time)
```

**Transcription Specifications**:

```
Format: Verbatim (include "um," "uh," false starts, laughter)
  - Capture natural speech patterns
  - Important for qualitative analysis

Speaker Labels:
  - Interviewer: "I:"
  - Participant: "P:"

Timestamps: Every 5 minutes (helps locate quotes)

De-identification:
  - Replace names with [NAME]
  - Replace locations with [LOCATION]
  - Replace identifiable details with [DETAIL]

Quality Check:
  - Research team member reviews 10% of transcripts against audio
  - If error rate >5%, send back to transcriptionist
  - Our QC: 2.1% error rate (within acceptable range)
```

**Transcripts Received**:
- 30 transcripts (average 9,500 words each)
- Total: 285,000 words
- 950 pages of qualitative data

**Checkpoint**: High-quality transcripts ready for analysis.

---

## Part 4: Thematic Analysis (15 minutes)

### Step 4.1: Familiarization with Data

**Action**: Read all transcripts twice

```
Familiarization Process:
─────────────────────────────────────────────────
Week 1: Initial Reading
  - Read all 30 transcripts without coding
  - Take reflective notes (patterns, surprises, confusions)
  - Discuss initial impressions in research team meeting

Week 2: Active Reading
  - Re-read transcripts with attention to research questions
  - Highlight striking quotes
  - Note preliminary codes in margins

Team Discussion:
  - "I'm noticing a lot of participants talk about 'awareness'..."
  - "Several mentioned using mindfulness during arguments"
  - "Some differentiate between 'formal practice' vs 'informal mindfulness'"
```

**Checkpoint**: Immersed in data, ready for systematic coding.

---

### Step 4.2: Generate Initial Codes

**Action**: Code line-by-line using NVivo software

```
Coding Process (Inductive + Deductive):
═══════════════════════════════════════════════

Inductive Codes (data-driven):
  - Let codes emerge from participant language
  - Example: Participant says "I noticed I was spiraling"
    → Code: "Metacognitive awareness"

Deductive Codes (theory-driven):
  - Based on mindfulness literature
  - Example: Looking for "acceptance" (key MBCT concept)

Coding Example (Transcript Excerpt):

─────────────────────────────────────────────────
I: Can you describe a time when you used mindfulness?

P: "Yeah, so I was in the library studying for finals [1], and I 
started getting really anxious [2]. Normally I'd just push through
[3], but I remembered the breathing exercise [4]. So I stopped,
did like five minutes of mindful breathing [5], and noticed my
heart rate slow down [6]. I felt more focused after [7], like I
could actually retain the material instead of just panicking [8]."

Codes Applied:
[1] Context: Academic stress
[2] Symptom: Anxiety
[3] Previous coping: Avoidance/pushing through
[4] Mechanism: Remembering technique
[5] Practice: Formal breathing exercise
[6] Physical change: Autonomic regulation
[7] Outcome: Improved focus
[8] Mechanism: Cognitive clarity vs. rumination
─────────────────────────────────────────────────

After coding all 30 transcripts:
  → 487 unique codes generated
```

**Checkpoint**: All transcripts systematically coded.

---

### Step 4.3: Search for Themes

**Action**: Group codes into themes

```
Theme Development Process:
═══════════════════════════════════════════════

Step 1: Sort codes into potential themes
  - Print all 487 codes on cards
  - Physically sort into piles
  - Look for patterns and clusters

Step 2: Identify candidate themes

Example:

Codes related to "awareness":
  - Noticing thoughts without reacting
  - Catching rumination early
  - Awareness of body sensations
  - Recognition of negative thought patterns
  - Metacognitive insight
  
  → CANDIDATE THEME: "Decentering from Thoughts"

Step 3: Review and refine
  - Check if theme has enough data
  - Check if theme is coherent
  - Check if themes are distinct (minimal overlap)

Initial Themes (12):
  1. Decentering from thoughts
  2. Acceptance vs. avoidance
  3. Embodied awareness
  4. Self-compassion
  5. Attention regulation
  6. Values clarification
  7. Social connection through mindfulness
  8. Barriers to practice
  9. Integration into daily life
  10. Technology as facilitator
  11. Technology as barrier
  12. Dosage and engagement
```

**Checkpoint**: 12 candidate themes identified.

---

### Step 4.4: Review and Refine Themes

**Action**: Collapse and refine themes

```
Theme Refinement:
═══════════════════════════════════════════════

Themes 1-7: Collapse into "Mechanisms of Change" (overarching theme)
  ├─ Subtheme 1.1: Decentering from thoughts
  ├─ Subtheme 1.2: Acceptance vs. avoidance
  ├─ Subtheme 1.3: Embodied awareness
  ├─ Subtheme 1.4: Self-compassion
  └─ Subtheme 1.5: Attention regulation

Theme 8-9: Combine into "Barriers and Facilitators"
  ├─ Subtheme 2.1: Time constraints
  ├─ Subtheme 2.2: Motivation fluctuations
  ├─ Subtheme 2.3: Skepticism about mindfulness
  └─ Subtheme 2.4: Integration into routines

Theme 10-11: Combine into "Role of Online Delivery"
  ├─ Subtheme 3.1: Flexibility and accessibility
  ├─ Subtheme 3.2: Lack of human support
  └─ Subtheme 3.3: Self-directed learning

Theme 12: Standalone theme "Engagement Matters"
  ├─ Subtheme 4.1: Formal vs. informal practice
  └─ Subtheme 4.2: Dose-response relationship

FINAL THEMATIC STRUCTURE (4 main themes, 13 subthemes)
```

**Checkpoint**: Coherent, non-overlapping themes with rich data support.

---

### Step 4.5: Define and Name Themes

**Action**: Write detailed theme definitions with exemplar quotes

```
═══════════════════════════════════════════════
THEME 1: MECHANISMS OF CHANGE
═══════════════════════════════════════════════

Definition: Participants described five core mechanisms through which 
mindfulness reduced depressive symptoms, all related to changing their 
relationship with thoughts and emotions rather than changing content.

Subtheme 1.1: Decentering from Thoughts
─────────────────────────────────────────────────
Definition: Stepping back from thoughts, observing without believing or reacting.

Prevalence: 28/30 participants (93%)

Exemplar Quotes:

"Before, I'd think 'I'm worthless' and just believe it. Now I notice 
'I'm having the thought that I'm worthless.' It sounds small, but it's 
huge. It's like... the thought is there, but it's not ME." 
[Participant 12, High Responder]

"I learned to watch my thoughts like clouds passing by. They come, they 
go, I don't have to grab onto them and make them mean something." 
[Participant 7, Moderate Responder]

Subtheme 1.2: Acceptance vs. Avoidance
─────────────────────────────────────────────────
Definition: Turning toward difficult emotions rather than suppressing or avoiding.

Prevalence: 24/30 participants (80%)

Exemplar Quote:

"I used to try to push away sad feelings, which just made me feel worse. 
Now I'm like, 'okay, sadness, you're here.' I breathe with it. It sounds 
counterintuitive, but accepting it makes it less overwhelming." 
[Participant 19, High Responder]

[Additional subthemes follow same structure...]

═══════════════════════════════════════════════
THEME 2: BARRIERS AND FACILITATORS
═══════════════════════════════════════════════

[Similar detailed definition and quotes...]
```

**Checkpoint**: Themes richly defined with participant voice foregrounded.

---

## Part 5: Integration of Quantitative and Qualitative Findings (10 minutes)

### Step 5.1: Create Joint Display

**Joint Display**: Visual table integrating both data types

```
═══════════════════════════════════════════════════════════════════════
           JOINT DISPLAY: INTEGRATED FINDINGS
═══════════════════════════════════════════════════════════════════════

Research Question: Why did online MBCT reduce depression?

QUANTITATIVE RESULTS          QUALITATIVE RESULTS              META-INFERENCE
(RCT, n=214)                  (Interviews, n=30)               (Integration)
─────────────────────────────────────────────────────────────────────────────

WHAT WORKED?                  WHY IT WORKED?
─────────────────────────────────────────────────────────────────────────────
MBCT reduced PHQ-9 by         Mechanism: Decentering           CONVERGENCE
3.2 points (d=0.68, p<.001)   "I learned to observe thoughts   → Confirms 
                              without believing them"          hypothesized
                              (28/30 participants)             decentering
                                                               mechanism

Secondary: Reduced GAD-7      Mechanism: Acceptance            EXPANSION
by 2.4 points (p<.001)        "Turning toward difficult        → Explains how
                              emotions reduced their power"    MBCT affects
                              (24/30 participants)             anxiety too

FOR WHOM?                     WHY VARIATION?
─────────────────────────────────────────────────────────────────────────────
Engagement moderated          Low responders reported:         EXPLANATION
effect: High engagement       • Time barriers (n=8)            → Clarifies
showed d=0.82, Low            • Skepticism about mindfulness   moderator
showed d=0.41                   (n=6)                          mechanism
                              • Preference for medication      
                                (n=4)                          

Gender: No difference         Male participants:               COMPLEMENTARITY
(p=0.42)                      "Mindfulness felt 'soft' at      → Adds nuance
                              first, but it's actually         (initial 
                              really hard" (n=3)               resistance
                                                               overcome)

WHAT ABOUT ONLINE?            ONLINE FACILITATORS?             EXPANSION
─────────────────────────────────────────────────────────────────────────────
No in-person comparison       Facilitators:                    → Informs
in this trial                 • Flexibility: "I could do it    future 
                              at 2am when I couldn't sleep"    hybrid models
                              (n=22)                           
                              • Privacy: "No one knew I was    
                              struggling" (n=18)               
                                                               
                              Barriers:                        
                              • Lack of accountability         
                                "Easy to skip" (n=15)          
                              • No live support                
                                "Wished I could ask questions" 
                                (n=12)                         

═══════════════════════════════════════════════════════════════════════
```

**Meta-Inference Types**:
- **Convergence**: Qual confirms quan (triangulation)
- **Expansion**: Qual adds breadth to quan
- **Explanation**: Qual explains quan mechanisms
- **Complementarity**: Qual nuances quan findings
- **Discordance**: Qual contradicts quan (explore why)

**Checkpoint**: Integrated findings provide fuller understanding than either alone.

---

### Step 5.2: Develop Conceptual Model

**Action**: Create visual model integrating findings

```
═══════════════════════════════════════════════
    CONCEPTUAL MODEL: How Online MBCT Works
═══════════════════════════════════════════════

                   ONLINE MBCT PROGRAM
                    (8 weeks, self-guided)
                           │
                           ↓
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ↓                  ↓                  ↓
    FACILITATORS       MECHANISMS         BARRIERS
    (Qual Theme 2)     (Qual Theme 1)     (Qual Theme 2)
        │                  │                  │
   ┌────┴────┐        ┌────┼────┐       ┌────┴────┐
   │         │        │    │    │       │         │
 Flexibility Privacy  Decent Accept Embod Time  Skepticism
 Access              ering  ance   iment Constr
   │         │        │    │    │       │         │
   └────┬────┘        └────┼────┘       └────┬────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ↓
                   ENGAGEMENT LEVEL
                   (Quan Moderator)
                  High vs. Low (Qual Theme 4)
                           │
                           ↓
                    OUTCOMES (Quan Results)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ↓                  ↓                  ↓
   Depression         Anxiety            Functioning
   Reduction          Reduction          Improvement
   (PHQ-9 -3.2)       (GAD-7 -2.4)      (SDS -1.2)
   d=0.68             d=0.51             d=0.34

═══════════════════════════════════════════════

Key Insights from Integration:
• Mechanisms (qual) explain effect size (quan)
• Barriers (qual) explain non-responders (quan)
• Engagement (both) is key moderator
• Online features (qual) increase access but reduce accountability
```

**Checkpoint**: Conceptual model synthesizes quan + qual into coherent theory.

---

## Part 6: Reporting Mixed Methods (5 minutes)

### Step 6.1: GRAMMS Checklist

**GRAMMS**: Good Reporting of A Mixed Methods Study (6 items)

```
═══════════════════════════════════════════════
       GRAMMS REPORTING CHECKLIST
═══════════════════════════════════════════════

1. Describe justification for using mixed methods
   In manuscript: "Quantitative RCT establishes efficacy (what works), 
                   but qualitative interviews explain mechanisms (why/how). 
                   Integration provides richer understanding."

2. Describe design (convergent/explanatory/exploratory)
   In manuscript Methods: "Explanatory sequential design. Phase 1: RCT 
                           (n=214). Phase 2: Interviews with purposive 
                           sample (n=30) to explain quantitative results."

3. Describe sampling strategy for each component
   Quan: "Random allocation to MBCT vs control (n=268 randomized)"
   Qual: "Purposive sampling stratified by response level and engagement 
          (n=30 from MBCT group only)"

4. Describe data collection and analysis separately for each component
   Quan: "PHQ-9 at baseline, 8 weeks, 6 months. ANCOVA adjusted for baseline."
   Qual: "Semi-structured interviews (45-60 min). Thematic analysis per 
          Braun & Clarke (2006). NVivo 12 for coding."

5. Describe integration techniques
   In manuscript: "Joint display (Table 3) integrating quantitative results 
                   with qualitative themes. Meta-inferences identify 
                   convergence, expansion, and explanation."

6. Describe limitations of integration
   In manuscript: "Qualitative sample (n=30) may not fully represent all 
                   RCT participants (n=214). Participants self-selected 
                   into interviews (potential bias toward positive 
                   experiences)."

GRAMMS Compliance: 6/6 items ✓
```

**Checkpoint**: GRAMMS checklist ensures transparent reporting.

---

### Step 6.2: Manuscript Structure

**Mixed Methods Manuscript Sections**:

```
TITLE
"Why Does Online Mindfulness-Based Cognitive Therapy Work for College 
Student Depression? An Explanatory Sequential Mixed Methods Study"

ABSTRACT
Background: Online MBCT reduces depression, but mechanisms unclear.
Methods: Explanatory sequential design. Phase 1: RCT (n=214). 
         Phase 2: Interviews (n=30). Integration via joint display.
Results: MBCT reduced PHQ-9 by 3.2 points (quan). Mechanisms included 
         decentering, acceptance, embodied awareness (qual). Integration 
         revealed engagement as key moderator.
Conclusion: Mindfulness works through changing relationship with thoughts. 
            Online format increases access but requires engagement support.

INTRODUCTION
- Prevalence of college depression
- Evidence for MBCT (cite systematic review from Tutorial 2)
- Gap: Mechanisms unknown, especially online delivery
- Rationale for mixed methods (triangulation, explanation)

METHODS
Part 1: Quantitative Component (RCT)
- Design, participants, intervention, outcomes, analysis
- (Can refer to previously published RCT protocol)

Part 2: Qualitative Component (Interviews)
- Sampling (purposive, n=30)
- Interview guide development
- Data collection procedures
- Thematic analysis approach

Part 3: Integration
- Joint display creation
- Meta-inference development

RESULTS
Part 1: Quantitative Results
- Table 1: Demographics
- Table 2: Outcomes (MBCT vs control)
- Figure 1: CONSORT diagram

Part 2: Qualitative Results
- Table 3: Participant characteristics (interview sample)
- Theme 1: Mechanisms (with subthemes and quotes)
- Theme 2: Barriers/Facilitators
- Theme 3: Online Delivery
- Theme 4: Engagement

Part 3: Integration
- Table 4: Joint Display (convergence, expansion, explanation)
- Figure 2: Conceptual Model

DISCUSSION
- Summary of integrated findings
- Comparison to existing literature
- Theoretical implications
- Clinical implications
- Limitations (of each method and integration)
- Future research

Target Journal: Journal of Mixed Methods Research or 
                Qualitative Health Research
```

**Checkpoint**: Manuscript structure follows GRAMMS and showcases integration.

---

## Summary and Next Steps

### What You've Learned

**Mixed Methods Design**:
- Chose explanatory sequential design (quan → qual)
- Embedded qualitative component in RCT
- Used purposive sampling (n=30 stratified by response)
- Developed semi-structured interview guide
- Conducted and transcribed 30 interviews

**Qualitative Analysis**:
- Performed thematic analysis (Braun & Clarke framework)
- Generated 487 initial codes → 4 main themes
- Defined themes with rich participant quotes
- Used NVivo software for systematic coding

**Integration**:
- Created joint display linking quan and qual findings
- Developed conceptual model synthesizing results
- Identified meta-inferences (convergence, expansion, explanation)
- Reported per GRAMMS guidelines (6/6 items)

**Key Insights from Integration**:
- Quan showed **WHAT** works (MBCT reduces depression, d=0.68)
- Qual explained **WHY** (decentering, acceptance mechanisms)
- Qual explained **FOR WHOM** (barriers for low engagers)
- Qual revealed **HOW** (online flexibility increases access but reduces accountability)

**Advantages of Mixed Methods**:
- Richer understanding than quan or qual alone
- Mechanisms explain effect sizes
- Participant voice humanizes numbers
- Informs intervention refinement

---

### Tools and Resources

**Qualitative Software**:
- **NVivo**: Industry standard, powerful but expensive
- **MAXQDA**: Similar to NVivo, Windows/Mac
- **ATLAS.ti**: Good for theory-building
- **Dedoose**: Web-based, collaborative, affordable
- **RQDA** (R package): Free, open-source

**Reporting Guidelines**:
- **GRAMMS**: Good Reporting of A Mixed Methods Study
- **COREQ**: Consolidated Criteria for Reporting Qualitative Research
- **SRQR**: Standards for Reporting Qualitative Research

**Books**:
- Creswell & Plano Clark (2017): *Designing and Conducting Mixed Methods Research*
- Braun & Clarke (2021): *Thematic Analysis: A Practical Guide*

---

### Next Steps

**After This Tutorial**:
1. Consider adding qualitative to your next RCT
2. Use mixed methods for pilot studies (qual → quan → intervention)
3. Explore other designs (convergent, exploratory)

**See Also**:
- Tutorial 8: Grant Proposal Writing (budgeting for qual data collection)

---

**Tutorial Complete!** You now know how to design, conduct, and report mixed methods research that integrates quantitative and qualitative approaches for richer insights.
