# Tutorial 11: Implementation Science

**Duration:** 55 minutes
**Prerequisites:** Tutorial 3 (Experimental Design), Tutorial 5 (Complete Workflow)
**Skill Level:** Advanced
**Use Case:** Translating research findings into real-world practice

---

## What You'll Learn

Implementation science is the study of methods to promote the systematic uptake of research findings and evidence-based practices (EBPs) into routine practice. While efficacy trials test "Can it work under ideal conditions?", implementation science asks "Does it work in the real world, and how do we get it there?"

**By the end of this tutorial, you'll be able to:**

1. Apply the RE-AIM framework to evaluate implementation initiatives
2. Use CFIR to identify barriers and facilitators to implementation
3. Select and tailor implementation strategies from the ERIC compilation
4. Design hybrid effectiveness-implementation studies (Types 1-3)
5. Measure implementation outcomes (fidelity, adoption, sustainability)
6. Navigate the adaptation vs. fidelity tension
7. Develop comprehensive implementation plans

**Why This Matters:**

- **Research-Practice Gap**: 17-year average lag from discovery to practice (Balas & Boren, 2000)
- **Low Adoption Rates**: Only 14% of research findings enter routine practice (Green et al., 2009)
- **Sustainability Challenge**: 60-90% of innovations fail to sustain after initial funding (Scheirer & Dearing, 2011)
- **Health Equity**: Poor implementation disproportionately affects underserved populations

---

## Running Example: Implementing TF-CBT

**Throughout this tutorial**, we'll follow a real implementation case:

**Context**: Large urban hospital system seeks to implement Trauma-Focused Cognitive Behavioral Therapy (TF-CBT) across 12 community mental health centers serving diverse, low-income neighborhoods.

**The Evidence**: TF-CBT has strong efficacy evidence from 20+ RCTs showing large effects (d=0.80) for treating childhood PTSD and trauma.

**The Challenge**: Despite strong evidence, only 15% of eligible children in the system currently receive TF-CBT. Most clinicians use eclectic, non-evidence-based approaches.

**Our Goal**: Design and evaluate a 3-year implementation initiative to increase TF-CBT adoption, fidelity, and sustainability.

---

## Part 1: The RE-AIM Framework (10 minutes)

### What is RE-AIM?

**RE-AIM** (Glasgow et al., 1999) evaluates implementation across 5 dimensions:

```
┌────────────────────────────────────────────────────────────┐
│ R - REACH                                                  │
│   Who received the intervention?                           │
│   (Individual level)                                       │
├────────────────────────────────────────────────────────────┤
│ E - EFFECTIVENESS                                          │
│   What were the outcomes?                                  │
│   (Individual level)                                       │
├────────────────────────────────────────────────────────────┤
│ A - ADOPTION                                               │
│   Which settings/staff participated?                       │
│   (Setting/staff level)                                    │
├────────────────────────────────────────────────────────────┤
│ I - IMPLEMENTATION                                         │
│   How consistently was it delivered?                       │
│   (Setting/staff level)                                    │
├────────────────────────────────────────────────────────────┤
│ M - MAINTENANCE                                            │
│   Was it sustained over time?                              │
│   (Individual AND setting levels)                          │
└────────────────────────────────────────────────────────────┘
```

### Applying RE-AIM to TF-CBT Implementation

**REACH** (Who receives TF-CBT?)

**Numerator**: Number of eligible children who receive TF-CBT
**Denominator**: Total number of eligible children (trauma exposure + clinical need)

```
Baseline Data Collection:
- Review EHR records for past 12 months
- Identify children with trauma exposure (ACEs screen, trauma history)
- Identify children with PTSD/trauma symptoms (PTSD-RI scores ≥38)

Eligible Population: 1,847 children
Received TF-CBT: 276 children
Reach: 276/1,847 = 14.9%

Target: 60% reach by Year 3 (1,108 children)

Representativeness:
- Compare demographics of TF-CBT recipients vs. eligible non-recipients
- Hispanic children: 18% of recipients vs. 31% of eligible (underrepresented)
- Action: Target outreach to Hispanic-serving clinics
```

**EFFECTIVENESS** (Does TF-CBT work in real-world settings?)

```
Primary Outcome: PTSD symptom reduction (PTSD-RI)
Secondary Outcomes: Depression (CDI-2), behavior problems (CBCL)

Comparison Groups:
1. Children receiving TF-CBT (n=276)
2. Children receiving usual care (n=300, matched on baseline symptoms)

Results (12-week post-treatment):
PTSD-RI reduction:
  TF-CBT: -22.4 points (SE=1.8)
  Usual care: -9.1 points (SE=1.6)
  Effect size: d=0.62 (95% CI: 0.48-0.76)

Interpretation: Effectiveness (d=0.62) is lower than efficacy trials (d=0.80)
but still clinically meaningful. Represents real-world attenuation.
```

**ADOPTION** (Which settings and staff participate?)

```
Setting-Level Adoption:
- 12 eligible clinics in hospital system
- 9 clinics agreed to participate (75% adoption rate)
- Non-adopters: Smaller clinics with high staff turnover

Staff-Level Adoption:
- 127 eligible clinicians (licensed therapists serving children)
- 73 completed TF-CBT training (57% adoption rate)
- Predictors of adoption:
  * Higher baseline self-efficacy (OR=2.3)
  * Supportive supervisor (OR=3.1)
  * Previous EBP training (OR=1.8)

Representativeness:
- Compare adopting vs. non-adopting settings on size, resources, patient mix
- Adopting clinics serve more commercially insured patients (potential inequity)
```

**IMPLEMENTATION** (How consistently is TF-CBT delivered?)

```
Fidelity Assessment:
- TF-CBT adherence measured via TF-CBT BFTSC (12-item checklist)
- Expert raters code 20% of sessions (n=312 sessions across 73 clinicians)

Adherence Scores:
  Mean: 8.9/12 components delivered (74% fidelity)
  Range: 4-12 components
  Threshold: ≥9/12 for "adequate fidelity"

Fidelity Distribution:
  High fidelity (≥9/12): 43% of clinicians
  Moderate fidelity (7-8/12): 38% of clinicians
  Low fidelity (<7/12): 19% of clinicians

Most commonly omitted components:
  1. Gradual exposure (38% omission rate)
  2. Cognitive processing (29% omission rate)
  3. Parent-child conjoint sessions (24% omission rate)

Implementation Costs:
  Training: $2,400/clinician (3-day workshop + consultation)
  Ongoing supervision: $180/clinician/month
  Fidelity monitoring: $85/session coded
```

**MAINTENANCE** (Is TF-CBT sustained?)

```
Individual-Level Maintenance (6-month follow-up):
- PTSD-RI scores remain stable (-20.8 points from baseline)
- 82% of symptom gains maintained
- 18% relapse rate (PTSD-RI increase >10 points)

Setting-Level Maintenance (24 months post-funding):
- 9 clinics initially adopted TF-CBT
- 7 clinics still delivering TF-CBT at 24 months (78% sustained)
- 2 clinics discontinued (reasons: leadership turnover, competing priorities)

Sustainability Indicators (among 7 sustained clinics):
  - TF-CBT written into clinical protocols: 7/7 (100%)
  - TF-CBT included in new staff orientation: 6/7 (86%)
  - Internal TF-CBT champions identified: 7/7 (100%)
  - Ongoing fidelity monitoring: 4/7 (57%)
  - External consultation discontinued: 6/7 (86%)

Threat to Sustainability:
  - Trained clinician turnover: 31% of original cohort left by Year 2
  - Action: Develop train-the-trainer model for ongoing capacity building
```

### RE-AIM Summary Table

```
Dimension         Metric                           Result      Target
────────────────────────────────────────────────────────────────────
REACH             % eligible receiving TF-CBT      14.9%  →   60%
EFFECTIVENESS     Effect size (d)                  0.62        0.50+
ADOPTION          % clinics participating          75%         80%
                  % clinicians trained             57%         70%
IMPLEMENTATION    % with adequate fidelity         43%         70%
MAINTENANCE       % clinics sustained (24 mo)      78%         70%
────────────────────────────────────────────────────────────────────
```

**Checkpoint:** Can you identify one barrier in each RE-AIM dimension for the TF-CBT implementation?

---

## Part 2: CFIR - Identifying Barriers & Facilitators (10 minutes)

### What is CFIR?

The **Consolidated Framework for Implementation Research** (Damschroder et al., 2009) organizes factors affecting implementation into 5 domains and 39 constructs.

```
CFIR Structure:

Domain 1: INTERVENTION CHARACTERISTICS (8 constructs)
  - Relative advantage, complexity, cost, adaptability...

Domain 2: OUTER SETTING (4 constructs)
  - Patient needs, external policies, peer pressure...

Domain 3: INNER SETTING (12 constructs)
  - Culture, leadership engagement, resources, communication...

Domain 4: CHARACTERISTICS OF INDIVIDUALS (5 constructs)
  - Knowledge/beliefs, self-efficacy, motivation...

Domain 5: PROCESS (8 constructs)
  - Planning, engaging, executing, reflecting/evaluating...
```

### CFIR Assessment for TF-CBT

We conducted **semi-structured interviews** with 45 stakeholders (clinicians, supervisors, administrators) using the CFIR Interview Guide.

**Data Analysis Approach:**
1. Deductive coding using CFIR constructs as codes
2. Rate each construct: -2 (strong barrier) to +2 (strong facilitator)
3. Identify top barriers and facilitators to target with implementation strategies

**Results:**

```
DOMAIN 1: INTERVENTION CHARACTERISTICS
────────────────────────────────────────────────────────────────────
Construct              Rating  Evidence from Interviews
────────────────────────────────────────────────────────────────────
Evidence Strength        +2    "Everyone knows TF-CBT works, the data
                               is rock solid" (Clinician 12)

Relative Advantage       +1    "It's more structured than what I was
                               doing, gives me a roadmap" (Clin 7)

Complexity               -1    "The exposure component is intimidating,
                               I worry I'll make kids worse" (Clin 23)

Design Quality           +1    "The manual is really well-organized,
                               easy to follow" (Clin 18)

Cost                     -1    "3 days of training is hard to cover
                               with our staffing" (Supervisor 4)

Adaptability             -2    "I have kids who need it but don't fit
(MAJOR BARRIER)                the age range or trauma type. Can I
                               adapt?" (Clin 31) [n=19 mentioned this]

Trialability             +1    "I could try it with one case first
                               before committing fully" (Clin 9)

────────────────────────────────────────────────────────────────────

DOMAIN 2: OUTER SETTING
────────────────────────────────────────────────────────────────────
Patient Needs/Resources  +2    "We have SO many trauma cases, kids
(MAJOR FACILITATOR)            are desperate for help" (Supervisor 2)

External Policies         0    "Insurance covers it, but prior auth
                               is a pain" (Admin 3)

Peer Pressure            +1    "Other hospitals are doing this, we
                               should too" (Admin 1)

────────────────────────────────────────────────────────────────────

DOMAIN 3: INNER SETTING
────────────────────────────────────────────────────────────────────
Tension for Change       +2    "Our current approach isn't working,
(MAJOR FACILITATOR)            we need to do better" (Supervisor 5)

Compatibility             0    "It fits our mission but conflicts with
                               our open-ended therapy culture" (Clin 14)

Relative Priority        -2    "We have 5 other initiatives right now,
(MAJOR BARRIER)                this feels like one more thing" (Clin 21)
                               [n=17 mentioned competing priorities]

Leadership Engagement    +1    "Medical director is really behind this,
                               talks about it in meetings" (Clin 8)

Available Resources      -1    "We don't have protected time for the
                               training or consultation" (Supervisor 6)

Access to Knowledge      +1    "They're providing training and ongoing
                               consultation, that helps" (Clin 11)

────────────────────────────────────────────────────────────────────

DOMAIN 4: INDIVIDUAL CHARACTERISTICS
────────────────────────────────────────────────────────────────────
Knowledge & Beliefs      +1    "I believe in using EBPs, it's the right
about Intervention             thing to do for kids" (Clin 5)

Self-Efficacy            -1    "I'm worried I can't do the exposure
                               part correctly" (Clin 28)
                               [n=22 mentioned exposure concerns]

Stage of Change          +1    "I'm ready to learn this, was already
                               looking for trauma training" (Clin 13)

────────────────────────────────────────────────────────────────────

DOMAIN 5: PROCESS
────────────────────────────────────────────────────────────────────
Planning                 +1    "There's a clear implementation plan
                               with timeline and milestones" (Admin 2)

Engaging (Champions)     -1    "Would be better if we had someone on
(BARRIER)                      the inside championing this" (Clin 19)

Executing                 0    "We're early in rollout, too soon to
                               tell how execution will go" (Clin 10)

Reflecting & Evaluating  +1    "They're collecting data to track
                               progress, will adjust as needed" (Admin 4)
────────────────────────────────────────────────────────────────────
```

### CFIR Priority Barriers and Facilitators

**Top 3 Barriers (to target with implementation strategies):**

1. **Adaptability (-2)**: Clinicians unsure if/how to adapt TF-CBT for diverse client needs
2. **Relative Priority (-2)**: Competing initiatives create implementation fatigue
3. **Self-Efficacy (-1)**: Clinicians anxious about delivering exposure component

**Top 3 Facilitators (to leverage):**

1. **Patient Needs (+2)**: High prevalence of trauma creates urgency
2. **Tension for Change (+2)**: Recognition that current approaches are inadequate
3. **Evidence Strength (+2)**: Strong belief in TF-CBT's effectiveness

**Checkpoint:** How would you use this CFIR data to select implementation strategies? Which barrier would you target first?

---

## Part 3: Selecting Implementation Strategies (ERIC) (8 minutes)

### What is ERIC?

The **Expert Recommendations for Implementing Change** (Powell et al., 2015) compiled 73 discrete implementation strategies organized into 9 clusters.

```
ERIC Strategy Clusters:

1. Use Evaluative & Iterative Strategies (8 strategies)
   - Audit and feedback, stage implementation scale-up...

2. Provide Interactive Assistance (4 strategies)
   - Facilitation, technical assistance, clinical supervision...

3. Adapt & Tailor to Context (4 strategies)
   - Tailor strategies, promote adaptability...

4. Develop Stakeholder Interrelationships (13 strategies)
   - Identify champions, build coalitions, capture and share local knowledge...

5. Train & Educate Stakeholders (11 strategies)
   - Distribute educational materials, conduct training, create learning collaborative...

6. Support Clinicians (7 strategies)
   - Revise professional roles, provide ongoing consultation...

7. Engage Consumers (3 strategies)
   - Prepare patients to be active participants, involve patients/families...

8. Use Financial Strategies (6 strategies)
   - Alter incentives, place innovation on fee schedule...

9. Change Infrastructure (17 strategies)
   - Change records systems, mandate change, develop implementation glossary...
```

### Strategy Selection Process

We use CFIR barriers to select ERIC strategies using a **tailored implementation** approach:

**Step 1: Match Barriers to Strategy Clusters**

```
Barrier                Strategy Cluster            Rationale
────────────────────────────────────────────────────────────────────
Adaptability (-2)      → Adapt & Tailor           Directly addresses
                                                   adaptation concerns

Relative Priority (-2) → Develop Stakeholder      Build buy-in and
                         Interrelationships       reduce resistance

Self-Efficacy (-1)     → Train & Educate          Build skills and
                         Support Clinicians       confidence
────────────────────────────────────────────────────────────────────
```

**Step 2: Select Specific Strategies**

**FOR BARRIER 1: Adaptability (-2)**

**Selected Strategy**: *Promote Adaptability* (Cluster 3)

**Operationalization**:
```
Implementation Component: "Adaptation Guidance Protocol"

1. Develop TF-CBT Adaptation Decision Tree:
   - Core components (cannot modify): Trauma narrative, cognitive processing
   - Adaptable components (can modify): Session length, delivery format, cultural examples

2. Create "When and How to Adapt" training module (2 hours):
   - Fidelity-consistent adaptations vs. fidelity-inconsistent
   - Case examples of appropriate adaptations
   - Decision-making framework

3. Establish Adaptation Review Process:
   - Clinicians submit planned adaptations to consultation group
   - Group provides feedback within 48 hours
   - Track adaptations in registry for learning

Example Adaptation (Approved):
  Client: 7-year-old with developmental delay (IQ=68)
  Adaptation: Extend treatment from 12 to 16 sessions to allow more repetition
  Rationale: Maintains core components but adjusts pace for cognitive level
  Status: APPROVED (fidelity-consistent adaptation)

Example Adaptation (Not Approved):
  Client: 15-year-old with complex trauma
  Adaptation: Skip exposure component entirely due to clinician discomfort
  Rationale: Exposure is core component; skipping would compromise fidelity
  Status: NOT APPROVED → Refer to additional exposure training instead
```

**FOR BARRIER 2: Relative Priority (-2)**

**Selected Strategies**:
- *Identify and Prepare Champions* (Cluster 4)
- *Conduct Local Consensus Discussions* (Cluster 4)

**Operationalization**:
```
Strategy 1: Identify and Prepare Champions

Champion Selection Criteria:
  - Well-respected peer (not supervisor)
  - Early adopter with positive TF-CBT experiences
  - Strong interpersonal skills
  - Protected time (2 hours/week)

Champion Roles:
  1. Troubleshoot barriers ("What challenges are you facing?")
  2. Share success stories (in team meetings, via email)
  3. Normalize struggles ("I found exposure hard at first too")
  4. Connect clinicians with resources
  5. Advocate for TF-CBT in leadership meetings

Champion Training:
  - 4-hour workshop on change management and peer influence
  - Monthly champion community of practice calls
  - Toolkit: talking points, case study library, FAQ document

Identified Champions:
  - Clinic A: Dr. Elena Rodriguez (10 years experience, bilingual)
  - Clinic B: Sarah Johnson, LCSW (early adopter, ran 8 TF-CBT cases)
  - Clinic C: Dr. Michael Chen (respected senior clinician)
  [9 champions total across 9 clinics]

Strategy 2: Conduct Local Consensus Discussions

Format: 90-minute facilitated discussions at each clinic
Participants: All clinic staff (clinicians, admin, leadership)
Frequency: Quarterly for first year

Discussion Agenda:
  1. Review RE-AIM data for this clinic (15 min)
  2. Discuss competing priorities and trade-offs (30 min)
     - "What would we need to de-prioritize to make room for TF-CBT?"
     - "How does TF-CBT align with our clinic's mission?"
  3. Consensus building: "What's our clinic's TF-CBT goal for next quarter?" (30 min)
  4. Identify clinic-specific barriers and solutions (15 min)

Clinic A Consensus (Quarter 1):
  "We commit to having 60% of eligible trauma cases receive TF-CBT by end of Q1.
   To achieve this, we will reduce non-trauma general therapy intakes by 10%
   to create capacity. Dr. Rodriguez will champion, and supervisors will
   prioritize TF-CBT in case assignments."
```

**FOR BARRIER 3: Self-Efficacy (-1)**

**Selected Strategies**:
- *Conduct Ongoing Training* (Cluster 5)
- *Provide Ongoing Consultation* (Cluster 6)

**Operationalization**:
```
Strategy 1: Conduct Ongoing Training (Exposure-Focused)

Training Structure:
  - Initial 3-day TF-CBT workshop (existing)
  - PLUS: Advanced 1-day "Mastering Exposure" workshop (new)
  - Offered at 6 months post-initial training

Mastering Exposure Workshop Content:
  1. Rationale for exposure (extinction learning, inhibitory learning)
  2. Live demonstration with standardized patient (child actor)
  3. Supervised role-play practice (5 exposure scenarios)
  4. Managing clinician anxiety about exposure
  5. Troubleshooting difficult exposure situations

Pre-Post Assessment:
  - Exposure Self-Efficacy Scale (0-100)
  - Pre-workshop: M=52.3 (SD=18.7)
  - Post-workshop: M=78.1 (SD=12.4)
  - Change: +25.8 points, d=1.62, p<0.001

Strategy 2: Provide Ongoing Consultation

Consultation Model: "TF-CBT Learning Collaborative"

Format:
  - 90-minute group consultation calls
  - Biweekly for first 6 months, monthly thereafter
  - Led by TF-CBT expert trainer
  - Maximum 15 clinicians per call

Consultation Call Structure:
  1. Case consultation (60 min)
     - 3 clinicians present cases (20 min each)
     - Presenter shares brief summary + specific question
     - Group provides input, expert synthesizes
  2. Skill building (30 min)
     - Mini-didactic on challenging topic
     - Review of common errors from fidelity monitoring

Example Case Consultation:
  Presenter: Sarah, LCSW (6 months post-training)
  Case: 9-year-old girl, witnessed domestic violence, resists exposure
  Question: "How do I engage her in the trauma narrative when she shuts down?"

  Expert Response:
    - Normalize avoidance as PTSD symptom
    - Use gradual hierarchy (start with less distressing moments)
    - Incorporate child's strengths (loves drawing → draw narrative)
    - Involve caregiver to model coping
    - Consider shorter exposure segments (5 min vs. 15 min)

  Follow-up: Sarah successfully used drawing approach, child completed narrative

Consultation Utilization:
  - 73 trained clinicians
  - 68 participated in at least 1 call (93% engagement)
  - Mean calls attended: 8.2 (SD=3.1) over 12 months
```

### Implementation Strategy Bundle Summary

```
Barrier              Strategy                   Dose/Intensity
────────────────────────────────────────────────────────────────────
Adaptability (-2)    Promote Adaptability       Decision tree +
                                                2-hr training +
                                                ongoing review

Relative Priority    Identify Champions         9 champions,
(-2)                 Consensus Discussions      2 hrs/week +
                                                Quarterly meetings

Self-Efficacy (-1)   Ongoing Training           1-day workshop +
                     Ongoing Consultation       Biweekly calls
────────────────────────────────────────────────────────────────────

Total Implementation Cost:
  - Champion time: $156,000/year (9 × 2 hrs/week × $50/hr × 52 weeks)
  - Consultation: $78,000/year (expert time + platform)
  - Training: $32,400 (one-time, 73 clinicians × $400/person)
  - Adaptation system: $18,000/year (coordinator time)
  ────────────────────────────────────────────────────────────────
  TOTAL Year 1: $284,400
  TOTAL Year 2-3: $252,000/year (no additional training cost)
```

**Checkpoint:** Can you think of a different ERIC strategy that could address the self-efficacy barrier?

---

## Part 4: Hybrid Effectiveness-Implementation Designs (8 minutes)

### What are Hybrid Designs?

**Hybrid designs** (Curran et al., 2012) simultaneously test **clinical effectiveness** (Does the intervention work?) AND **implementation strategies** (How do we get it adopted?).

```
Traditional Research Trajectory (Slow):

Step 1: Efficacy Trials ────→ Step 2: Effectiveness Trials ────→ Step 3: Implementation Studies
        (10 years)                     (7 years)                          (5 years)

        Total: 22 years from discovery to practice

Hybrid Design (Faster):

Effectiveness + Implementation studied CONCURRENTLY
        Total: 5-8 years from discovery to practice
```

### Three Types of Hybrid Designs

```
┌────────────────────────────────────────────────────────────────────┐
│ HYBRID TYPE 1: Primarily Effectiveness, Secondarily Implementation│
│                                                                    │
│ Primary Aim:   Test intervention effectiveness                    │
│ Secondary Aim: Gather implementation data (acceptability, cost)   │
│                                                                    │
│ When to Use: Intervention has some efficacy data but limited      │
│              real-world effectiveness data. Want to prepare for   │
│              future implementation.                               │
│                                                                    │
│ Example: RCT of new digital therapy with embedded measures of     │
│          implementation feasibility and acceptability.            │
└────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│ HYBRID TYPE 2: DUAL focus on Effectiveness AND Implementation     │
│                                                                    │
│ Co-Primary Aims: (1) Test intervention effectiveness              │
│                  (2) Test implementation strategy effectiveness    │
│                                                                    │
│ When to Use: Intervention has established efficacy, need to test  │
│              both real-world effectiveness AND how to implement.   │
│                                                                    │
│ Example: Cluster RCT comparing two implementation strategies       │
│          (facilitation vs. learning collaborative) while also      │
│          measuring patient outcomes.                              │
└────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│ HYBRID TYPE 3: Primarily Implementation, Secondarily Effectiveness│
│                                                                    │
│ Primary Aim:   Test implementation strategy effectiveness         │
│ Secondary Aim: Monitor intervention effectiveness (shouldn't      │
│                decrease with implementation strategies)           │
│                                                                    │
│ When to Use: Intervention has strong efficacy AND effectiveness   │
│              evidence. Main question is HOW to implement at scale.│
│                                                                    │
│ Example: Compare three implementation strategies (training only,  │
│          training+consultation, training+consultation+champions)  │
│          while monitoring that TF-CBT still works.                │
└────────────────────────────────────────────────────────────────────┘
```

### TF-CBT Implementation: Hybrid Type 3 Design

**Rationale for Type 3**: TF-CBT has 20+ efficacy RCTs and multiple effectiveness studies. Main question is **how to implement** at scale across diverse community clinics.

**Research Question**: Which implementation strategy bundle is most effective for increasing TF-CBT adoption, fidelity, and sustainability?

**Study Design**:

```
Cluster Randomized Trial
Unit of Randomization: Clinic (n=12 clinics)
Allocation: 4 clinics per condition
Duration: 3 years (implementation + 1-year sustainability follow-up)

CONDITION 1: TRAINING ONLY (Control)
  - 3-day TF-CBT workshop
  - TF-CBT manual and materials
  - No additional support

CONDITION 2: TRAINING + CONSULTATION
  - 3-day TF-CBT workshop
  - Biweekly group consultation calls (12 months)
  - TF-CBT expert provides case-based feedback

CONDITION 3: TRAINING + CONSULTATION + CHAMPION + ADAPTATION SUPPORT (Enhanced)
  - 3-day TF-CBT workshop
  - Biweekly consultation calls (12 months)
  - Designated internal champion (2 hrs/week protected time)
  - Adaptation guidance protocol
  - Quarterly consensus discussions
```

**Primary Implementation Outcomes** (Proctor et al., 2011):

```
1. ADOPTION
   Definition: % of trained clinicians who deliver TF-CBT to at least 2 clients

   Measurement:
     - EHR data extraction quarterly
     - Binary outcome: Yes/No

   Hypothesis: Enhanced > Training+Consultation > Training Only

2. FIDELITY
   Definition: Mean TF-CBT adherence score (TF-CBT BFTSC, 0-12 scale)

   Measurement:
     - Code 20% of sessions (stratified random sample)
     - Expert raters blind to condition
     - Inter-rater reliability: ICC > 0.80

   Hypothesis: Enhanced > Training+Consultation > Training Only

3. SUSTAINABILITY
   Definition: % of clinics still delivering TF-CBT at 24 months post-funding

   Measurement:
     - EHR data at 24-month follow-up
     - Clinic interviews about barriers/facilitators

   Hypothesis: Enhanced > Training+Consultation > Training Only
```

**Secondary Clinical Outcome** (Monitor, don't deteriorate):

```
4. PTSD SYMPTOM REDUCTION
   Definition: Change in PTSD-RI scores from baseline to 12-week post-treatment

   Measurement:
     - Patient-reported outcome at baseline and 12 weeks
     - Collected on ALL children receiving TF-CBT across conditions

   Hypothesis: No significant differences across conditions (all should work)

   Safety Criterion: Mean effect size must be d ≥ 0.40 in all conditions
                     (ensures TF-CBT still effective despite implementation focus)
```

**Sample Size Calculation**:

```
Primary Outcome: Fidelity (continuous, 0-12 scale)
Design: 3-arm cluster RCT, 4 clinics per arm, 6 clinicians per clinic

Parameters:
  - Expected fidelity means:
    * Training Only: 7.2
    * Training+Consultation: 8.5
    * Enhanced: 9.3
  - SD = 2.1
  - ICC (clinician within clinic) = 0.15
  - Alpha = 0.05
  - Power = 0.80

Design Effect = 1 + (m-1) × ICC = 1 + (6-1) × 0.15 = 1.75

Effective n per arm = 4 clinics × 6 clinicians / 1.75 = 13.7 ≈ 14 per arm

Power Analysis (ANOVA):
  - 3 groups, n=14 per group, f=0.44 (large effect)
  - Power = 0.82 ✓

Total Sample:
  - 12 clinics
  - 72 clinicians (assuming 6 per clinic)
  - ~360 patients (5 per clinician over study period)
```

**Data Collection Schedule**:

```
Timeline   Implementation Data              Clinical Data
──────────────────────────────────────────────────────────────────────
Baseline   - Clinician demographics         - Patient demographics
           - Clinic characteristics         - PTSD-RI, CDI-2, CBCL
           - CFIR interviews                - Trauma history

0-12 mo    - Adoption tracking (monthly)    - Ongoing PTSD-RI at
           - Fidelity coding (20% sessions)   12 weeks post-treatment
           - Consultation attendance
           - Champion activity logs

12 mo      - RE-AIM assessment              - 6-month follow-up
           - CFIR follow-up interviews        for clinical outcomes
           - Sustainability planning

24 mo      - Sustainability assessment      - Ongoing monitoring
           - Cost analysis                    (if still delivered)
           - Clinician interviews
──────────────────────────────────────────────────────────────────────
```

**Analysis Plan**:

```r
# Primary Analysis: Fidelity outcome (mixed effects model)

library(lme4)
library(lmerTest)

# Model accounts for clustering (clinicians within clinics)
model <- lmer(fidelity_score ~ condition + (1|clinic/clinician), data = data)

# Pairwise contrasts
emmeans(model, pairwise ~ condition, adjust = "tukey")

# Expected Results:
# Enhanced vs. Training Only: diff = 2.1, 95% CI [0.8, 3.4], p = 0.002
# Training+Consultation vs. Training Only: diff = 1.3, 95% CI [0.1, 2.5], p = 0.04
# Enhanced vs. Training+Consultation: diff = 0.8, 95% CI [-0.4, 2.0], p = 0.18

# Interpretation:
# Both Training+Consultation and Enhanced improve fidelity vs. Training Only
# Enhanced is numerically higher but not significantly different from Training+Consultation
```

**Cost-Effectiveness Analysis**:

```
Implementation Cost per Clinician (3-year total):

Training Only:           $2,400 (training only)
Training+Consultation:   $10,500 (training + $675/mo consultation × 12 mo)
Enhanced:                $17,800 (above + champion time + adaptation system)

Implementation Outcome:

Training Only:           6.1 TF-CBT-completers per clinician
Training+Consultation:   9.3 TF-CBT-completers per clinician
Enhanced:                11.2 TF-CBT-completers per clinician

Cost per Additional Child Treated (vs. Training Only):

Training+Consultation:   ($10,500 - $2,400) / (9.3 - 6.1) = $2,531 per child
Enhanced:                ($17,800 - $2,400) / (11.2 - 6.1) = $3,020 per child

Interpretation:
  - Training+Consultation is most cost-effective ($2,531 per additional child)
  - Enhanced provides highest reach but at higher cost per child
  - Decision depends on budget constraints and scale-up goals
```

**Checkpoint:** Why might a hybrid design be preferable to separate effectiveness and implementation studies?

---

## Part 5: Measuring Implementation Outcomes (8 minutes)

### Proctor's Implementation Outcomes

Proctor et al. (2011) defined 8 implementation outcomes distinct from clinical outcomes:

```
┌─────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION OUTCOMES (How well did implementation go?)      │
│                                                                 │
│ 1. ACCEPTABILITY - Perception that intervention is agreeable   │
│ 2. ADOPTION - Intention/decision to use intervention           │
│ 3. APPROPRIATENESS - Perceived fit for setting/problem         │
│ 4. FEASIBILITY - Extent to which intervention can be used      │
│ 5. FIDELITY - Adherence to intervention protocol               │
│ 6. IMPLEMENTATION COST - Cost of implementation process        │
│ 7. PENETRATION - Integration within setting/service area       │
│ 8. SUSTAINABILITY - Maintenance over time after support ends   │
└─────────────────────────────────────────────────────────────────┘

vs.

┌─────────────────────────────────────────────────────────────────┐
│ SERVICE OUTCOMES (Impact on service system?)                   │
│ - Efficiency, safety, effectiveness, equity, patient-centeredness│
└─────────────────────────────────────────────────────────────────┘

vs.

┌─────────────────────────────────────────────────────────────────┐
│ CLINICAL OUTCOMES (Impact on patients?)                        │
│ - Symptom reduction, functioning, quality of life, satisfaction │
└─────────────────────────────────────────────────────────────────┘
```

### Measuring Each Implementation Outcome for TF-CBT

**1. ACCEPTABILITY** (Is TF-CBT agreeable to clinicians?)

```
Measure: Acceptability of Intervention Measure (AIM, Weiner et al., 2017)
Format: 4 items, 5-point scale (1=completely disagree, 5=completely agree)
Administration: Post-training and at 6, 12 months

Sample Items:
  1. "TF-CBT is appealing to me"
  2. "I like TF-CBT"
  3. "I welcome TF-CBT"
  4. "TF-CBT is appealing"

Scoring: Mean of 4 items (range 1-5), higher = more acceptable

Results:
  Post-training: M=4.1 (SD=0.6) - High acceptability initially
  6 months: M=3.8 (SD=0.7) - Slight decline after real-world use
  12 months: M=4.2 (SD=0.5) - Rebounds as competence increases

Interpretation: Acceptability remains high throughout, with initial dip
                during the challenging early implementation period.

Predictor Analysis:
  - Acceptability at 6 months predicts fidelity at 12 months (r=0.48, p<0.001)
  - Clinicians with acceptability <3.0 at 6 months were 4.2× more likely
    to discontinue TF-CBT by 12 months
```

**2. ADOPTION** (Do clinicians use TF-CBT?)

```
Measure: EHR-based behavioral indicator
Definition: % of trained clinicians who deliver TF-CBT to ≥2 clients

Time Points:
  3 months post-training:  31% (23/73 clinicians)
  6 months:                57% (42/73 clinicians)
  12 months:               68% (50/73 clinicians)
  24 months:               61% (41/67 remaining clinicians - 6 left)

Non-Adopter Characteristics (n=23):
  - Higher caseload (M=32 vs. M=24 for adopters, p=0.02)
  - Less supportive supervision (M=2.1 vs. M=3.8 on 5-pt scale, p<0.001)
  - Fewer trauma cases (M=3 vs. M=9 eligible cases, p=0.003)

Rapid vs. Slow Adopters:
  - Rapid (adopted within 3 months): Higher self-efficacy at baseline (OR=2.8)
  - Slow (adopted after 6 months): Needed more consultation (mean 12 vs. 6 calls)
```

**3. APPROPRIATENESS** (Is TF-CBT a good fit?)

```
Measure: Intervention Appropriateness Measure (IAM, Weiner et al., 2017)
Format: 4 items, 5-point scale
Administration: Post-training, 12 months

Sample Items:
  1. "TF-CBT seems fitting for our clients"
  2. "TF-CBT seems suitable for our clinic"
  3. "TF-CBT seems applicable to our setting"
  4. "TF-CBT seems like a good match for our needs"

Results by Clinic Type:
  Specialized trauma clinic (n=2 clinics): M=4.7 (SD=0.4) - Excellent fit
  General mental health (n=7 clinics): M=3.9 (SD=0.6) - Good fit
  Integrated primary care (n=0 clinics): [Not applicable - no PC clinics]

Appropriateness-Adoption Link:
  - Clinics with mean appropriateness >4.0 had 78% adoption rate
  - Clinics with mean appropriateness <3.5 had 43% adoption rate
  - Difference: 35 percentage points, p=0.03
```

**4. FEASIBILITY** (Can TF-CBT be delivered in routine practice?)

```
Measure: Feasibility of Intervention Measure (FIM, Weiner et al., 2017)
Format: 4 items, 5-point scale
Administration: 6 months, 12 months

Sample Items:
  1. "TF-CBT seems implementable in our clinic"
  2. "TF-CBT seems possible to use in our clinic"
  3. "TF-CBT seems doable in our clinic"
  4. "TF-CBT seems easy to use in our clinic"

Results:
  6 months: M=3.2 (SD=0.8) - Moderate feasibility
  12 months: M=3.6 (SD=0.7) - Improved feasibility

Feasibility Barriers (Open-Ended):
  1. "Not enough time for 12-16 sessions" (n=34 mentions)
  2. "Hard to engage parents in treatment" (n=28 mentions)
  3. "Documentation burden" (n=19 mentions)
  4. "Exposure component takes too long" (n=16 mentions)

Feasibility Solutions Implemented:
  - Allow flexible session length (45-90 min instead of fixed 60 min)
  - Offer parent sessions by phone when in-person not feasible
  - Create TF-CBT documentation templates in EHR
  - Break exposure across 2 sessions if needed
```

**5. FIDELITY** (See Part 1 for full details)

```
Measure: TF-CBT Brief Fidelity Training and Safety Checklist (TF-CBT BFTSC)
Range: 0-12 components
Threshold: ≥9/12 for "adequate fidelity"

Result: 43% of clinicians achieved adequate fidelity

Fidelity Improvement Strategies:
  - Fidelity feedback reports sent to clinicians quarterly
  - Consultation focused on commonly omitted components
  - Fidelity-based consultation (review coded sessions together)
```

**6. IMPLEMENTATION COST** (See Part 3 for full details)

```
Total 3-Year Implementation Cost: $788,400

Breakdown:
  Training: $175,200 (73 clinicians × $2,400)
  Consultation: $234,000 (78k/year × 3 years)
  Champions: $468,000 (156k/year × 3 years)
  Adaptation support: $54,000 (18k/year × 3 years)
  Fidelity monitoring: $157,200 (52.4k/year × 3 years)

Cost per Clinician: $10,800 over 3 years
Cost per Child Treated: $1,219 (788,400 / 647 children treated)

Return on Investment (ROI):
  - TF-CBT prevents 1 suicide attempt per 100 treated (vs. usual care)
  - Lifetime cost of suicide attempt: ~$250,000 (medical + productivity loss)
  - Expected savings: 6.47 attempts prevented × $250,000 = $1,617,500
  - ROI: ($1,617,500 - $788,400) / $788,400 = 105% return
```

**7. PENETRATION** (How deeply integrated is TF-CBT?)

```
Measure: Multi-level integration assessment

Clinic-Level Penetration:
  - 9/12 clinics delivering TF-CBT (75%)
  - Mean % of eligible clients receiving TF-CBT: 34% (range 18-62% by clinic)

Clinician-Level Penetration:
  - 50/73 trained clinicians actively using TF-CBT (68%)
  - Mean % of caseload that is TF-CBT: 22% (range 5-48%)
  - 12 clinicians using TF-CBT for >40% of caseload ("high penetrators")

System-Level Penetration Indicators:
  TF-CBT in clinical pathways (yes - added to trauma care pathway)
  TF-CBT in EHR treatment menu (yes)
  TF-CBT in quality metrics (yes - % of trauma cases receiving EBP)
  ✗ TF-CBT in payer contracts (no - not yet)
  TF-CBT in job descriptions (yes - added to new therapist postings)
  TF-CBT in orientation (yes - mentioned in new hire training)
```

**8. SUSTAINABILITY** (See Part 1 for full details)

```
24-Month Post-Funding Assessment:

Sustained Clinics: 7/9 (78%)
Sustained Clinicians: 41/67 (61% - accounting for turnover)

Sustainability Predictors (Logistic Regression):
  - Internal champion present: OR=8.2, p=0.001
  - Integrated into clinical pathways: OR=6.7, p=0.003
  - Leadership turnover: OR=0.2, p=0.02 (barrier)
  - External consultation continued: OR=0.4, p=0.08 (not significant, ns)

Interpretation: Internally-driven factors (champions, pathways) predict
                sustainability better than external support continuation.
```

**Checkpoint:** How do implementation outcomes differ from clinical outcomes? Why measure both?

---

## Part 6: Adaptation vs. Fidelity Tension (6 minutes)

### The Core Tension

```
FIDELITY                                              ADAPTATION
────────────────────────────────────────────────────────────────────
"Deliver intervention                               "Modify intervention
 exactly as designed"                               to fit local context"

Maximize effectiveness                              Maximize feasibility
                                                    and appropriateness
Minimize drift
                                                    Increase adoption
Ensure replicability                                and sustainability

Risk: Low adoption due                              Risk: Intervention
      to poor fit                                         no longer effective
────────────────────────────────────────────────────────────────────

                        THE TENSION:
            How much can we adapt without losing effectiveness?
```

### Framework for Managing Adaptation

**Core Components vs. Adaptable Periphery** (Castro et al., 2004)

```
CORE COMPONENTS (Cannot modify without compromising effectiveness)
  - Based on theory and empirical evidence
  - Essential for achieving outcomes
  - Modification would undermine mechanism of change

ADAPTABLE COMPONENTS (Can modify to fit context)
  - Format, delivery, cultural content
  - Not theorized to be essential
  - Modification may improve fit without harming effectiveness
```

### TF-CBT Core vs. Adaptable Components

```
┌────────────────────────────────────────────────────────────────────┐
│ CORE COMPONENTS (DO NOT MODIFY)                                   │
├────────────────────────────────────────────────────────────────────┤
│ 1. Trauma Narrative Development                                   │
│    - Child creates detailed account of traumatic experience       │
│    - WHY CORE: Exposure/processing is primary mechanism           │
│                                                                    │
│ 2. Cognitive Processing of Trauma Narrative                       │
│    - Identify and challenge maladaptive cognitions                │
│    - WHY CORE: Cognitive restructuring is key mechanism           │
│                                                                    │
│ 3. Gradual Exposure to Trauma Reminders                           │
│    - Systematic desensitization to triggers                       │
│    - WHY CORE: Extinction learning requires exposure              │
│                                                                    │
│ 4. Parental Treatment Component                                   │
│    - Parent skills training and processing                        │
│    - WHY CORE: Parental response mediates child outcome           │
└────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│ ADAPTABLE COMPONENTS (CAN MODIFY FOR CONTEXT)                     │
├────────────────────────────────────────────────────────────────────┤
│ 1. Session Length and Number                                      │
│    - Standard: 12-16 sessions, 60 minutes each                    │
│    - Adaptation: 20 sessions × 45 min for younger/delayed child   │
│    - Rationale: Total exposure dose maintained                    │
│                                                                    │
│ 2. Delivery Format                                                │
│    - Standard: In-person individual therapy                       │
│    - Adaptation: Telehealth delivery or group format              │
│    - Rationale: Core components still delivered                   │
│                                                                    │
│ 3. Cultural Content and Examples                                  │
│    - Standard: Examples from TF-CBT manual                        │
│    - Adaptation: Examples relevant to child's culture/context     │
│    - Rationale: Increases engagement, doesn't change mechanism    │
│                                                                    │
│ 4. Narrative Creation Method                                      │
│    - Standard: Written or verbal narrative                        │
│    - Adaptation: Drawing, song, poetry, video                     │
│    - Rationale: Narrative still created (core) via different medium│
│                                                                    │
│ 5. Sequence of Components                                         │
│    - Standard: PRACTICE acronym order                             │
│    - Adaptation: Flexible ordering based on clinical presentation │
│    - Rationale: All components delivered, order flexible          │
└────────────────────────────────────────────────────────────────────┘
```

### Real Adaptation Examples from TF-CBT Implementation

**APPROVED ADAPTATIONS** (Fidelity-Consistent)

```
CASE 1: Developmental Adaptation
  Client: 6-year-old with developmental delay (IQ=68)
  Presenting Trauma: Physical abuse by father

  Standard Protocol: 12 sessions, 60 min each

  Adaptation:
    - Extend to 18 sessions × 45 minutes
    - Use more pictures/visuals, less verbal processing
    - Create trauma narrative through drawing (child draws 6 pictures)
    - Simplify cognitive processing (good thought/bad thought)
    - Increase parent sessions (8 instead of 4)

  Core Components Maintained: ✓
    - Trauma narrative created (via drawings)
    - Exposure to narrative (reviewing drawings repeatedly)
    - Cognitive processing (simplified but present)
    - Parent treatment (enhanced)

  Outcome: PTSD-RI decreased from 42 to 18 (56% reduction)
  Classification: FIDELITY-CONSISTENT ADAPTATION ✓
```

```
CASE 2: Cultural Adaptation
  Client: 15-year-old Somali refugee, witnessed violence
  Cultural Context: Somali Muslim family, limited English

  Standard Protocol: Individual sessions, child creates written narrative

  Adaptation:
    - Involve community cultural broker in treatment (attends 2 sessions)
    - Mother wears hijab during sessions (provide female therapist)
    - Narrative includes prayers/spiritual coping (child's preference)
    - Use interpreter for parent sessions
    - Respect Ramadan fasting (flexible scheduling)

  Core Components Maintained: ✓
    - Trauma narrative created (written, included cultural elements)
    - Cognitive processing completed
    - Gradual exposure implemented
    - Parent treatment delivered (with interpreter)

  Outcome: PTSD-RI decreased from 51 to 22 (57% reduction)
  Classification: FIDELITY-CONSISTENT ADAPTATION ✓
```

```
CASE 3: Telehealth Adaptation (COVID-19)
  Client: 11-year-old, sexual abuse, lives in rural area
  Context: In-person therapy paused due to pandemic

  Standard Protocol: In-person sessions

  Adaptation:
    - Switch to HIPAA-compliant telehealth platform
    - Mail art supplies for trauma narrative creation
    - Child creates narrative at home, shares via screen
    - Parent joins last 15 min of each session from different room
    - Safety protocol: therapist has emergency contact info

  Core Components Maintained: ✓
    - Trauma narrative created (at home but therapist-guided)
    - Cognitive processing via video
    - Gradual exposure (in vivo homework, processed via video)
    - Parent treatment delivered

  Outcome: PTSD-RI decreased from 47 to 21 (55% reduction)
  Note: Telehealth TF-CBT shown to be non-inferior to in-person (Stewart et al., 2017)
  Classification: FIDELITY-CONSISTENT ADAPTATION ✓
```

**NOT APPROVED ADAPTATIONS** (Fidelity-Inconsistent)

```
CASE 4: Exposure Avoidance (REJECTED)
  Clinician Request: "Can I skip the trauma narrative for a highly avoidant teen?"
  Rationale: "She shuts down when we talk about the trauma, I don't want to re-traumatize her"

  Requested Adaptation:
    - Omit trauma narrative entirely
    - Focus only on coping skills and parenting

  Review Decision: NOT APPROVED ✗

  Reasoning:
    - Trauma narrative/exposure is CORE component
    - Avoidance is PTSD symptom, not contraindication
    - "Shutting down" is expected, requires graded exposure (not omission)
    - Without narrative, not TF-CBT (just supportive therapy)

  Alternative Recommendation:
    - Use VERY gradual exposure hierarchy
    - Start with least distressing trauma elements
    - Shorter narrative segments (5 min instead of 15 min)
    - Increase distress tolerance skills before narrative
    - Additional consultation for clinician anxiety management

  Outcome: Clinician implemented gradual approach, teen completed narrative
           by session 10. PTSD-RI decreased from 54 to 24.
```

```
CASE 5: Component Substitution (REJECTED)
  Clinician Request: "Can I substitute EMDR for the trauma narrative?"
  Rationale: "I'm trained in EMDR and the child seems more comfortable with it"

  Requested Adaptation:
    - Replace trauma narrative with EMDR bilateral stimulation
    - Keep other TF-CBT components (coping skills, parenting)

  Review Decision: NOT APPROVED ✗

  Reasoning:
    - Trauma narrative is TF-CBT core component
    - Substituting EMDR creates a different intervention (no longer TF-CBT)
    - Can't measure "TF-CBT fidelity" if core component replaced
    - If want to deliver EMDR, that's valid but it's not TF-CBT

  Alternative Recommendation:
    - Deliver EMDR if clinician prefers (valid EBP for trauma)
    - Track as "EMDR case" not "TF-CBT case" for implementation evaluation
    - Don't count toward TF-CBT fidelity metrics

  Classification: DIFFERENT INTERVENTION (EMDR), not adapted TF-CBT
```

### Systematic Adaptation Decision-Making

```
ADAPTATION DECISION TREE

Question 1: Does the adaptation modify a CORE COMPONENT?
            ├─ YES → Probably NOT APPROVED (go to Q2)
            └─ NO → Probably APPROVED (go to Q3)

Question 2: If core component modified, is it REPLACED or OMITTED?
            ├─ REPLACED → NOT APPROVED (different intervention)
            └─ OMITTED → NOT APPROVED (incomplete intervention)

            Exception: Developmental necessity (e.g., very young child
                      can't write → draw narrative instead)
                      → APPROVED if core maintained

Question 3: If adaptable component modified, does it maintain DOSE/INTENSITY?
            ├─ YES → APPROVED
            └─ NO → NEEDS REVIEW

            Example: 12 × 60min = 720min total
                     16 × 45min = 720min total (maintained)
                     8 × 60min = 480min total ✗ (reduced dose)
```

**Checkpoint:** A clinician wants to deliver TF-CBT in group format (6 kids per group) instead of individual. Use the decision tree: Approved or not?

---

## Part 7: Developing an Implementation Plan (5 minutes)

### Implementation Plan Template

```
IMPLEMENTATION PLAN: TF-CBT in Community Mental Health System
Version 1.2 | Date: October 2023

═══════════════════════════════════════════════════════════════════

SECTION 1: IMPLEMENTATION AIMS AND OUTCOMES

Primary Implementation Aim:
  Increase the percentage of eligible children receiving TF-CBT from
  15% to 60% within 36 months.

Primary Implementation Outcome: REACH (RE-AIM)
  Numerator: # children receiving TF-CBT
  Denominator: # eligible children (trauma + clinical need)
  Target: 60% by Month 36

Secondary Implementation Outcomes:
  - FIDELITY: 70% of clinicians achieve adequate fidelity (≥9/12) by Month 18
  - SUSTAINABILITY: 70% of clinics maintain TF-CBT delivery at Month 48

Clinical Outcome (Safety Monitoring):
  - PTSD symptom reduction (PTSD-RI): Effect size d ≥ 0.40 maintained

═══════════════════════════════════════════════════════════════════

SECTION 2: IMPLEMENTATION STRATEGIES (ERIC-BASED)

Strategy 1: Conduct Educational Meetings (ERIC #11)
  - 3-day TF-CBT training workshop for 73 clinicians
  - Led by certified TF-CBT trainers
  - Schedule: Cohort 1 (Jan 2024), Cohort 2 (Mar 2024), Cohort 3 (May 2024)
  - Cost: $2,400 per clinician × 73 = $175,200

Strategy 2: Provide Ongoing Consultation (ERIC #48)
  - Biweekly group consultation calls (90 min)
  - Led by TF-CBT expert
  - Case-based learning format
  - 12-month duration per cohort
  - Cost: $78,000 per year

Strategy 3: Identify and Prepare Champions (ERIC #27)
  - Identify 9 internal champions (1 per clinic)
  - 4-hour champion training workshop
  - Protected time: 2 hours/week
  - Monthly champion community of practice
  - Cost: $156,000 per year

Strategy 4: Promote Adaptability (ERIC #60)
  - Develop adaptation decision tree and guidance
  - 2-hour training on fidelity-consistent adaptation
  - Ongoing adaptation consultation available
  - Track adaptations in registry
  - Cost: $18,000 per year (coordinator time)

Strategy 5: Audit and Provide Feedback (ERIC #2)
  - Code 20% of sessions for fidelity
  - Quarterly individual feedback reports
  - Clinic-level RE-AIM dashboard
  - Cost: $52,400 per year (coder time)

═══════════════════════════════════════════════════════════════════

SECTION 3: IMPLEMENTATION TIMELINE (36 MONTHS)

PHASE 1: PREPARATION (Months 1-3)
  ☐ Form implementation team (steering committee)
  ☐ Conduct CFIR needs assessment (stakeholder interviews)
  ☐ Identify and recruit champions
  ☐ Develop implementation materials (adaptation guide, fidelity tools)
  ☐ Establish data collection systems (EHR extracts, fidelity coding)

PHASE 2: INITIAL IMPLEMENTATION (Months 4-15)
  ☐ Cohort 1 training (Jan 2024, 24 clinicians)
  ☐ Cohort 2 training (Mar 2024, 25 clinicians)
  ☐ Cohort 3 training (May 2024, 24 clinicians)
  ☐ Launch biweekly consultation calls (ongoing)
  ☐ Begin fidelity coding and feedback (Month 6)
  ☐ Quarterly consensus discussions at each clinic
  ☐ Quarterly RE-AIM monitoring

PHASE 3: FULL IMPLEMENTATION (Months 16-30)
  ☐ Continue consultation calls (reduce to monthly at Month 18)
  ☐ Ongoing fidelity monitoring and feedback
  ☐ Address emerging barriers via CFIR follow-up interviews
  ☐ Champion-led peer learning activities
  ☐ Mid-implementation review (Month 24): Assess need for strategy adjustment

PHASE 4: SUSTAINABILITY TRANSITION (Months 31-36)
  ☐ Transition consultation from external to internal experts
  ☐ Develop train-the-trainer model for new staff
  ☐ Embed TF-CBT in clinical pathways and quality metrics
  ☐ Secure ongoing funding for champion time
  ☐ Plan for post-implementation period (Months 37+)

═══════════════════════════════════════════════════════════════════

SECTION 4: EVALUATION PLAN

Data Sources:
  1. EHR data: # TF-CBT cases, client demographics, session attendance
  2. Fidelity coding: TF-CBT BFTSC scores (20% of sessions)
  3. Clinical outcomes: PTSD-RI, CDI-2, CBCL (all TF-CBT clients)
  4. CFIR interviews: Baseline, 12 months, 24 months, 36 months
  5. Implementation logs: Training attendance, consultation attendance, champion activities

Analysis Plan:
  - RE-AIM calculations at 12, 24, 36 months
  - Mixed effects models for fidelity and clinical outcomes
  - Thematic analysis of CFIR interviews
  - Cost-effectiveness analysis comparing implementation strategies

Reporting:
  - Quarterly progress reports to leadership
  - Annual reports to funders
  - Manuscript submission: Implementation outcomes paper (Month 40)

═══════════════════════════════════════════════════════════════════

SECTION 5: BUDGET (3-YEAR TOTAL)

Training:                       $175,200 (one-time, all cohorts)
Consultation:                   $234,000 ($78k × 3 years)
Champions:                      $468,000 ($156k × 3 years)
Adaptation Support:              $54,000 ($18k × 3 years)
Fidelity Monitoring:            $157,200 ($52.4k × 3 years)
Data Management:                 $90,000 ($30k × 3 years)
Evaluation Coordination:        $150,000 ($50k × 3 years)
─────────────────────────────────────────────────────────────────
TOTAL 3-YEAR IMPLEMENTATION:  $1,328,400

Cost per clinician:            $18,200 (over 3 years)
Cost per child treated:        $1,540 (assuming 862 children treated)

═══════════════════════════════════════════════════════════════════
```

**Checkpoint:** What's missing from this implementation plan that would be useful to add?

---

## Summary & Tools

### What You've Learned

1. **RE-AIM Framework**: Evaluate implementation across Reach, Effectiveness, Adoption, Implementation, and Maintenance
2. **CFIR Assessment**: Systematically identify barriers and facilitators across 5 domains
3. **ERIC Strategies**: Select and tailor 73 implementation strategies to address specific barriers
4. **Hybrid Designs**: Simultaneously test effectiveness and implementation strategies (Types 1-3)
5. **Implementation Outcomes**: Measure acceptability, adoption, fidelity, feasibility, cost, penetration, sustainability (distinct from clinical outcomes)
6. **Adaptation Guidance**: Navigate the fidelity-adaptation tension using core vs. adaptable component frameworks
7. **Implementation Planning**: Develop comprehensive plans with timelines, strategies, evaluation, and budgets

### RE-AIM vs. CFIR vs. ERIC: When to Use What

```
PURPOSE                          USE THIS FRAMEWORK
─────────────────────────────────────────────────────────────────
Evaluate implementation impact   → RE-AIM (evaluation framework)
Identify barriers/facilitators   → CFIR (determinants framework)
Select implementation strategies → ERIC (strategy compilation)
Measure implementation process   → Proctor Implementation Outcomes
Design implementation studies    → Hybrid Designs (Type 1/2/3)
```

### Essential Implementation Science Tools

**Frameworks:**
- [RE-AIM](https://www.re-aim.org) - Evaluation framework
- [CFIR](https://cfirguide.org) - Determinants framework with interview guides
- [ERIC](https://societyforimplementationresearchcollaboration.org) - 73 implementation strategies

**Measures:**
- Proctor Implementation Outcomes: [AIM, IAM, FIM](https://societyforimplementationresearchcollaboration.org/use-siscr-products/sirc-instrument-project/) (4-item scales for acceptability, appropriateness, feasibility)
- CFIR Interview Guides: [cfirguide.org/interview](https://cfirguide.org/guide/app/)
- Sustainability: [Program Sustainability Assessment Tool](https://sustaintool.org)

**Reporting:**
- [StaRI](http://www.equator-network.org/reporting-guidelines/stari-statement/) (Standards for Reporting Implementation Studies)
- [TIDieR](https://www.bmj.com/content/348/bmj.g1687) (Template for Intervention Description and Replication)

**Training Resources:**
- [Implementation Science Training Program](https://impsci.tracs.unc.edu) (UNC Chapel Hill, free online)
- [TIDIRH](https://tidirh.org) (Training Institute for Dissemination and Implementation Research in Health)
- [D&I Models](https://dissemination-implementation.org) (Comprehensive model repository)

**Software:**
- NVivo or ATLAS.ti for CFIR qualitative data analysis
- REDCap for multi-site data management
- MLflow for tracking implementation experiments

### Common Mistakes to Avoid

1. **Treating implementation as an afterthought** - Plan for implementation from the start, not after efficacy is established
2. **One-and-done training** - Training alone rarely changes practice; ongoing consultation and support are essential
3. **Ignoring context** - What works in one setting may not work in another; use CFIR to assess local context
4. **All-or-nothing fidelity** - Allow fidelity-consistent adaptations rather than rigid adherence
5. **Neglecting sustainability** - Plan for post-funding sustainability from Day 1
6. **Confusing clinical and implementation outcomes** - Measure both; implementation success ≠ clinical effectiveness

### See Also

- **Tutorial 2: Literature Review** - For systematic review of implementation science literature
- **Tutorial 3: Experimental Design** - For designing hybrid effectiveness-implementation trials
- **Tutorial 7: Mixed Methods** - CFIR qualitative interviews often paired with quantitative outcome data
- **Tutorial 10: Meta-Analysis** - Synthesizing implementation strategy effectiveness across studies
- **Quality Improvement Template** - Related but distinct from implementation science (PDSA cycles, run charts)

---

**Next Steps:**

1. Practice applying RE-AIM to an existing implementation initiative
2. Conduct a CFIR assessment with 5-10 stakeholder interviews
3. Map CFIR barriers to ERIC strategies for your context
4. Design a hybrid Type 2 or 3 study to test implementation strategies
5. Develop a comprehensive implementation plan using the template above

**Key Takeaway:** Implementation science provides rigorous methods to close the research-practice gap. By systematically assessing context (CFIR), selecting tailored strategies (ERIC), and evaluating impact (RE-AIM, Proctor outcomes), we can accelerate the translation of evidence into practice and improve population health outcomes.
