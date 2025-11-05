# Stage 3: Methodology Design
## Detailed Prompt Chain

---

## 🎯 SUBCOMPONENTS

1. Research Paradigm & Philosophy
2. Research Design Selection
3. Sampling Strategy
4. Data Collection Instruments
5. Data Analysis Plan
6. Validity & Reliability
7. Ethical Considerations
8. Writing the Methodology Chapter

---

## 📥 REQUIRED INFORMATION (INPUTS)

- Research questions (from Stage 1)
- Literature review findings (from Stage 2)
- Resource constraints (time, budget, access)
- Institutional IRB/ethics requirements
- Available tools/software

---

## 📤 DELIVERABLES (OUTPUTS)

1. Methodological framework document
2. Research design diagram
3. Sampling plan
4. Data collection protocols/instruments
5. Analysis codebook or statistical plan
6. Validity/reliability strategy
7. Ethics approval application
8. Complete methodology chapter (6,000-8,000 words)

---

## 🤖 AI PROMPT CHAINS

### Prompt 3.1: Establish Research Paradigm

**USER INPUT REQUIRED:**
- Research questions
- Nature of research (exploratory, explanatory, descriptive)
- Disciplinary norms

**PROMPT:**
```
My research questions are:
[PASTE RESEARCH QUESTIONS]

The nature of my research is: [exploratory/explanatory/descriptive/evaluative]

My discipline is: [FIELD]

Help me articulate my research paradigm:

1. PARADIGM IDENTIFICATION:
   Explain which paradigm best fits my research:
   - Positivist (objective reality, quantitative)
   - Interpretivist/Constructivist (subjective meanings, qualitative)
   - Critical (power structures, emancipatory)
   - Pragmatic (what works, mixed methods)

2. ONTOLOGICAL POSITION:
   - What is the nature of reality in my study?
   - Is there one truth to discover or multiple perspectives?

3. EPISTEMOLOGICAL POSITION:
   - How can knowledge be gained in my study?
   - What counts as valid evidence?
   - What is the researcher's relationship to what's being studied?

4. METHODOLOGICAL IMPLICATIONS:
   - What methods are most aligned?
   - What assumptions am I making?
   - How will this affect data collection and analysis?

5. DRAFT STATEMENT:
   Write a 1-2 paragraph "methodological positioning" statement for my Chapter 4

Example for CS/Engineering: "This research adopts a positivist paradigm, assuming an objective reality that can be measured and analyzed. We employ computational experiments to test hypotheses about system performance."

Example for Social Sciences: "This study is grounded in an interpretivist paradigm, recognizing that participants' experiences are socially constructed. We use qualitative interviews to understand subjective meanings."
```

**EXPECTED OUTPUT:** Paradigm statement + justification (300-500 words)

**SAVE AS:** `/03_Methodology/research_paradigm.md`

---

### Prompt 3.2: Select Research Design

**USER INPUT REQUIRED:**
- Research questions
- Paradigm from 3.1
- Resources/constraints

**PROMPT:**
```
Research Questions: [PASTE]

Research Paradigm: [FROM 3.1]

Constraints: [time, budget, access, etc.]

Help me select the optimal research design:

1. DESIGN OPTIONS - Evaluate these designs for my questions:

   QUANTITATIVE:
   - Experimental (randomized controlled trial)
   - Quasi-experimental (no random assignment)
   - Survey/correlational
   - Longitudinal
   - Meta-analysis

   QUALITATIVE:
   - Phenomenological (lived experiences)
   - Grounded theory (theory from data)
   - Ethnographic (cultural immersion)
   - Narrative (stories/biographies)
   - Case study (in-depth single case)

   MIXED METHODS:
   - Convergent parallel (qual + quant simultaneously)
   - Explanatory sequential (quant → qual)
   - Exploratory sequential (qual → quant)

   COMPUTATIONAL:
   - Algorithm development & evaluation
   - Simulation study
   - Benchmark comparison
   - Ablation study
   - Theoretical analysis with empirical validation

2. COMPARISON:
   For each viable option, explain:
   - Strengths for answering my specific questions
   - Weaknesses or limitations
   - Resource requirements (time, money, access)
   - Timeline implications
   - What I'll be able to claim/conclude

3. RECOMMENDATION:
   - Recommend the best design for my study
   - Justify why it's optimal
   - Explain trade-offs

4. DESIGN DETAILS:
   - Describe specific procedures/steps
   - Create text-based diagram showing the design flow
   - Explain the logic connecting design to RQs
   - Identify potential confounds and how to address them

5. ALIGNMENT CHECK:
   - RQ1 → [How this design answers it]
   - RQ2 → [How this design answers it]
   - RQ3 → [How this design answers it]
```

**EXPECTED OUTPUT:** Research design justification + diagram (800-1,200 words)

**SAVE AS:** `/03_Methodology/research_design.md` and `/03_Methodology/design_diagram.pdf`

---

### Prompt 3.3: Develop Sampling Strategy

**USER INPUT REQUIRED:**
- Research design from 3.2
- Population of interest
- Resource constraints

**PROMPT:**
```
My research design is: [FROM 3.2]

My population of interest is: [DESCRIBE]

My resources/constraints are: [time, budget, access]

Help me develop a rigorous sampling strategy:

1. SAMPLING FRAME:
   - Define the target population precisely
   - Identify sampling frame (list/database of potential participants)
   - Discuss any limitations of the frame (e.g., who's missing?)

2. SAMPLING METHOD:

   PROBABILITY SAMPLING (for quantitative, generalizable):
   - Simple random
   - Stratified random
   - Cluster sampling
   - Systematic sampling

   NON-PROBABILITY SAMPLING (for qualitative, theoretical):
   - Purposive/theoretical sampling
   - Snowball/chain referral
   - Convenience sampling
   - Maximum variation sampling

   COMPUTATIONAL:
   - Dataset selection (which benchmarks?)
   - Train/validation/test splits (what ratios?)
   - Cross-validation strategy
   - Synthetic data generation (if needed)

   Recommend the most appropriate method and explain why.

3. SAMPLE SIZE:

   QUANTITATIVE:
   - Conduct power analysis (α = 0.05, power = 0.80, expected effect size = ?)
   - Calculate minimum N needed
   - Account for attrition (add 10-20%)
   - Software: G*Power, pwr package in R

   QUALITATIVE:
   - Estimate N based on saturation principle (typically 12-30 interviews)
   - Justify estimate based on similar studies
   - Plan for flexibility (stop when saturation reached)

   COMPUTATIONAL:
   - Justify dataset sizes (cite standard benchmarks)
   - If collecting new data, justify N (statistical power? representative?)
   - Cross-validation folds (typically 5 or 10)

4. INCLUSION/EXCLUSION CRITERIA:
   - Who is eligible? (specific, objective criteria)
   - Who is excluded? (and why?)
   - How will you verify eligibility?

5. RECRUITMENT STRATEGY:
   - How will you identify potential participants?
   - How will you contact them? (email, flyers, gatekeepers?)
   - What incentives will you offer? (money, gift cards, results?)
   - Timeline for recruitment

6. SAMPLING BIAS MITIGATION:
   - What biases might occur? (selection, non-response, volunteer)
   - How will you minimize them?
   - How will you assess representativeness?

Generate:
1. Detailed sampling plan
2. Recruitment email/script templates
3. Inclusion/exclusion checklist
4. Timeline for recruitment
```

**EXPECTED OUTPUT:** Complete sampling plan (1,000-1,500 words)

**SAVE AS:** `/03_Methodology/sampling_plan.md`

---

### Prompt 3.4: Design Data Collection Instruments

**USER INPUT REQUIRED:**
- Research questions
- Research design from 3.2
- Type of data needed (quantitative, qualitative, computational)

**PROMPT:**
```
Research Questions: [PASTE]

Research Design: [FROM 3.2]

Type of data needed: [quantitative/qualitative/computational/mixed]

Help me design data collection instruments:

1. INSTRUMENT SELECTION:

   QUANTITATIVE INSTRUMENTS:
   - Survey/questionnaire (new or existing scale?)
   - Observational checklist (structured observation)
   - Physiological measures (sensors, biometrics)
   - Archival data extraction form
   - Performance tests

   QUALITATIVE INSTRUMENTS:
   - Interview protocol (structured, semi-structured, unstructured)
   - Focus group guide
   - Observation protocol (ethnographic field notes)
   - Document analysis framework
   - Diary/journal prompts

   COMPUTATIONAL INSTRUMENTS:
   - Experiment script (code to run experiments)
   - Logging framework (what to record?)
   - Metrics calculation code
   - Simulation parameters
   - Benchmark evaluation protocols

2. FOR SURVEYS/QUESTIONNAIRES:

   - Decide: Existing validated scale or new instrument?
   - If existing: Which scale? Cite the original validation study
   - If new: Justify why existing scales are inadequate

   Design principles:
   - Question types: Likert scales, multiple choice, open-ended
   - Number of items per construct (minimum 3-5)
   - Response options (5-point or 7-point scale?)
   - Wording: Clear, unambiguous, no double-barreled questions
   - Order: Demographics at end, sensitive topics later
   - Length: Target 10-15 minutes to complete

   Create draft survey with:
   - Informed consent intro
   - Instructions
   - All questions
   - Thank you message

3. FOR INTERVIEWS:

   Create interview protocol:

   **Opening:**
   - Introduce yourself and study
   - Explain confidentiality
   - Get verbal consent
   - Ask permission to record

   **Main Questions (5-10 questions):**
   - Start with easy, descriptive questions
   - Move to more complex, analytical questions
   - Use open-ended questions (how, what, tell me about...)
   - Include probes: "Can you give an example?" "Tell me more."

   **Closing:**
   - Is there anything else you'd like to add?
   - Thank them
   - Explain next steps

   Example: "Tell me about your experience with [topic]. How did you feel about [aspect]? Can you give me a specific example?"

4. FOR COMPUTATIONAL EXPERIMENTS:

   Design experiment framework:

   **Configuration:**
   - Hyperparameters to test
   - Datasets to use (cite and justify)
   - Baselines to compare (cite original papers)
   - Metrics to calculate (cite definitions)
   - Hardware setup (GPU, CPU, memory)
   - Random seeds (for reproducibility)

   **Procedure:**
   - Data preprocessing steps
   - Model training procedure
   - Evaluation protocol
   - What to log (losses, accuracies, timings)

   **Reproducibility:**
   - Code structure
   - Documentation
   - Environment specifications (requirements.txt)

5. PILOT TESTING:
   - Test instrument with 3-5 people
   - Identify confusing questions
   - Check timing
   - Revise based on feedback
   - Document pilot results

Generate complete instruments ready for use or IRB submission.
```

**EXPECTED OUTPUT:**
- Survey/questionnaire (if applicable)
- Interview protocol (if applicable)
- Experiment code specifications (if computational)

**SAVE AS:** `/03_Methodology/data_collection_instruments/`

---

### Prompt 3.5: Develop Data Analysis Plan

**USER INPUT REQUIRED:**
- Research questions
- Type of data (quantitative, qualitative, computational)
- Specific hypotheses (if applicable)

**PROMPT:**
```
Research Questions: [PASTE]

Type of data: [quantitative/qualitative/computational/mixed]

Hypotheses (if applicable): [PASTE or "exploratory research, no hypotheses"]

Help me create a detailed data analysis plan:

1. DATA PREPARATION:

   QUANTITATIVE:
   - Data cleaning (missing data? outliers?)
   - Coding (how to code responses?)
   - Data transformation (log, standardize?)
   - Assumption checking (normality, homogeneity)

   QUALITATIVE:
   - Transcription (verbatim or intelligent?)
   - Anonymization (remove identifying info)
   - Data organization (by participant, by theme?)
   - Memo-writing plan

   COMPUTATIONAL:
   - Data preprocessing (normalization, augmentation?)
   - Feature engineering (if applicable)
   - Train/val/test splits (ratios)
   - Handling class imbalance

2. ANALYSIS STRATEGY:

   QUANTITATIVE - Recommend specific statistical tests:

   For RQ1 [PASTE RQ1]:
   - Appropriate test: [t-test, ANOVA, regression, chi-square, etc.]
   - Justification: [why this test?]
   - Assumptions to check: [normality, homoscedasticity, etc.]
   - Software: [SPSS, R, Python (scipy.stats)]
   - Alpha level: 0.05
   - Effect size measure: [Cohen's d, r², eta²]

   For RQ2 [PASTE RQ2]:
   - [Repeat]

   For RQ3 [PASTE RQ3]:
   - [Repeat]

   QUALITATIVE - Recommend coding approach:

   Approach: [Thematic analysis, grounded theory, IPA, content analysis]

   Phase 1: Initial coding (open coding)
   - Read transcripts multiple times
   - Apply line-by-line coding
   - Create initial code list

   Phase 2: Focused coding (axial coding)
   - Group related codes
   - Identify patterns
   - Develop themes

   Phase 3: Theoretical coding (selective coding)
   - Connect themes
   - Build theoretical framework
   - Test against data

   Software: NVivo, MAXQDA, Atlas.ti, or manual

   COMPUTATIONAL - Evaluation metrics:

   For RQ1 [PASTE RQ1]:
   - Metrics: [accuracy, F1, AUC, latency, throughput, etc.]
   - Statistical significance testing: [paired t-test between methods]
   - Effect sizes: [Cohen's d]
   - Baselines: [which methods to compare]

   For RQ2 [PASTE RQ2]:
   - [Repeat]

3. DEALING WITH COMPLEXITY:

   - Multiple comparisons: [Bonferroni correction, FDR]
   - Missing data: [listwise deletion, imputation, mixed models]
   - Outliers: [criteria for exclusion]
   - Subgroup analysis: [if planned]
   - Sensitivity analysis: [test robustness]

4. ANALYSIS TIMELINE:

   Week 1-2: Data cleaning and preparation
   Week 3-4: Preliminary analysis
   Week 5-6: Full analysis
   Week 7: Robustness checks
   Week 8: Write-up

5. CREATE ANALYSIS CODEBOOK (if quantitative):

   Variable | Type | Values | Notes
   ---------|------|--------|------
   Age | Continuous | 18-99 | Check for outliers
   Gender | Categorical | 1=M, 2=F, 3=Other |
   Satisfaction | Likert | 1-5 | Reverse code items 3,7

   OR CREATE CODING MANUAL (if qualitative):

   Theme | Definition | When to apply | Example
   ------|------------|---------------|--------
   Frustration | Expressions of dissatisfaction | When P mentions difficulty | "I couldn't figure out..."

6. SOFTWARE & SYNTAX:
   - Which software will you use?
   - Draft analysis syntax/code
   - Document assumptions and decisions
```

**EXPECTED OUTPUT:** Complete analysis plan (1,500-2,000 words) + codebook/manual

**SAVE AS:** `/03_Methodology/analysis_plan.md` and `/03_Methodology/codebook.xlsx`

---

### Prompt 3.6: Ensure Validity & Reliability

**USER INPUT REQUIRED:**
- Research design from 3.2
- Data collection instruments from 3.4
- Analysis plan from 3.5

**PROMPT:**
```
Research Design: [FROM 3.2]

Instruments: [BRIEF DESCRIPTION]

Analysis Plan: [BRIEF DESCRIPTION]

Help me establish validity and reliability:

1. VALIDITY (Are you measuring what you intend to measure?):

   A. INTERNAL VALIDITY (for causal claims):

   Threats:
   - History (external events during study)
   - Maturation (participants change over time)
   - Testing (taking test affects later performance)
   - Instrumentation (instrument changes)
   - Selection bias (groups differ at baseline)
   - Attrition (differential dropout)

   For my study, which threats apply?
   How will I address each threat?

   Example: "Selection bias is a concern. We address it by random assignment and checking baseline equivalence."

   B. EXTERNAL VALIDITY (generalizability):

   Questions:
   - To whom can I generalize? (population validity)
   - To what settings? (ecological validity)
   - To what times? (temporal validity)
   - What limits generalizability?

   Example: "Findings generalize to undergraduate students at large public universities in the US, but may not apply to community college students."

   C. CONSTRUCT VALIDITY (are concepts well-defined?):

   - Face validity: Does instrument appear to measure what it claims?
   - Content validity: Does instrument cover all aspects of construct?
   - Convergent validity: Correlates with measures of same construct
   - Discriminant validity: Doesn't correlate with measures of different constructs

   For my instruments:
   - Which validity types apply?
   - How will I establish/demonstrate validity?

2. RELIABILITY (consistency and repeatability):

   A. FOR QUANTITATIVE INSTRUMENTS:

   - Internal consistency: Cronbach's alpha (target ≥ 0.70)
     * If using existing scale, cite reliability from original study
     * If new scale, plan pilot test to assess alpha

   - Test-retest reliability: Correlation over time
     * If assessing, specify timeline (e.g., 2 weeks apart)

   - Inter-rater reliability: Agreement between coders
     * Cohen's kappa (for categorical) or ICC (for continuous)
     * Target ≥ 0.70
     * Plan: Two coders independently code 20% of data

   B. FOR QUALITATIVE DATA:

   - Credibility (internal validity):
     * Member checking: Share findings with participants
     * Triangulation: Multiple data sources
     * Prolonged engagement: Sufficient time in field
     * Peer debriefing: Discuss with colleagues

   - Transferability (external validity):
     * Thick description: Rich, detailed context
     * Maximum variation sampling

   - Dependability (reliability):
     * Audit trail: Document all decisions
     * Inter-coder agreement: Two coders, calculate kappa

   - Confirmability (objectivity):
     * Reflexivity: Acknowledge researcher bias
     * Negative case analysis: Look for disconfirming evidence

   C. FOR COMPUTATIONAL EXPERIMENTS:

   - Reproducibility:
     * Fixed random seeds
     * Version control
     * Environment documentation
     * Code availability

   - Reliability across runs:
     * Report mean ± std over multiple runs (≥3)
     * Check variance - if high, investigate why

   - Validity of metrics:
     * Cite metrics from literature
     * Ensure metrics align with research questions

3. ADDRESSING THREATS:

   Create a table:

   | Threat | How It Applies to My Study | Mitigation Strategy |
   |--------|----------------------------|---------------------|
   | Selection bias | Non-random assignment | Statistical controls, propensity score matching |
   | Attrition | 20% dropout expected | Intention-to-treat analysis, compare dropouts vs. completers |
   | [etc.] | | |

4. VALIDATION PLAN:

   Quantitative:
   - Run pilot with n=30 to assess Cronbach's alpha
   - Conduct factor analysis to confirm structure
   - Check convergent/discriminant validity

   Qualitative:
   - Member checking with 5 participants
   - Peer debriefing after every 5 interviews
   - Maintain reflexive journal throughout

Generate a comprehensive validity/reliability section for my methodology chapter.
```

**EXPECTED OUTPUT:** Validity & reliability strategy (1,000-1,500 words)

**SAVE AS:** `/03_Methodology/validity_reliability.md`

---

### Prompt 3.7: Address Ethical Considerations

**USER INPUT REQUIRED:**
- Research design from 3.2
- Participants/data sources
- Potential risks

**PROMPT:**
```
Research Design: [FROM 3.2]

Participants: [WHO? HOW MANY?]

Data: [WHAT DATA WILL YOU COLLECT?]

Potential Risks: [PHYSICAL? PSYCHOLOGICAL? PRIVACY? NONE?]

Help me address all ethical considerations:

1. IRB DETERMINATION:

   Does your study require IRB review?

   YES if:
   - Human subjects research (living individuals)
   - Interaction or intervention with people
   - Collection of identifiable private information
   - Experimental manipulation

   NO if:
   - Publicly available datasets only
   - No human subjects involvement
   - Quality improvement (not research)

   My study: [DOES/DOES NOT] require IRB.

   If YES: Determine review type:
   - Exempt (minimal risk, no intervention)
   - Expedited (minimal risk, standard procedures)
   - Full board (more than minimal risk)

2. INFORMED CONSENT:

   If human subjects, create informed consent document:

   Must include:
   - Purpose of study
   - Procedures (what will participants do?)
   - Duration (how long will it take?)
   - Risks (what could go wrong?)
   - Benefits (what do they gain?)
   - Confidentiality (how will data be protected?)
   - Voluntary participation (can withdraw anytime)
   - Contact information (researcher, IRB)
   - Statement: "I agree to participate" + signature

   Special populations (need extra protection):
   - Children (<18): Parental consent + child assent
   - Prisoners: Restricted research types
   - Pregnant women: Extra risk assessment
   - Cognitive impairment: Assess capacity to consent

   Generate a draft informed consent document.

3. CONFIDENTIALITY & PRIVACY:

   Data Protection Plan:

   - Identifiers to collect: [Name? Email? ID number?]
   - How to de-identify: [Assign participant IDs, remove names]
   - Where to store data: [Encrypted drive, locked cabinet]
   - Who has access: [Only research team]
   - How long to retain: [Typically 3-7 years per regulations]
   - Data destruction plan: [Shred paper, delete files after X years]

   For sensitive data (health, financial, illegal behavior):
   - Extra protections: [Encryption, secure servers]
   - Legal protections: [Certificate of Confidentiality?]
   - Reporting obligations: [Mandatory reporting if harm disclosed?]

4. RISKS & BENEFITS:

   Risks:
   - Physical: [Pain? Fatigue? Injury?]
   - Psychological: [Stress? Emotional distress? Stigma?]
   - Social: [Reputation? Relationships?]
   - Economic: [Loss of employability?]
   - Legal: [Disclosure of illegal activity?]
   - Privacy: [Breach of confidential information?]

   My study risks: [LIST or "Minimal risk - no greater than everyday life"]

   How to minimize risks: [STRATEGIES]

   Benefits:
   - To participants: [Incentives? Learning? Access to results?]
   - To society: [Advancing knowledge in X area]

   Risk-benefit ratio: [Benefits must outweigh risks]

5. SPECIAL ETHICAL CONSIDERATIONS:

   For my field:

   - Deception: [Am I deceiving participants? If yes, justify and plan debriefing]
   - Dual roles: [Am I researching my own students/employees? Conflicts?]
   - Community consent: [If researching communities, need community approval?]
   - Power imbalances: [Am I in authority over participants?]
   - Cultural sensitivity: [Are there cultural considerations?]
   - Environmental impact: [If computational, acknowledge carbon footprint?]

6. IRB APPLICATION PREPARATION:

   Documents needed:
   - [ ] IRB application form
   - [ ] Research protocol summary
   - [ ] Informed consent document(s)
   - [ ] Recruitment materials (emails, flyers)
   - [ ] Data collection instruments (surveys, interview guides)
   - [ ] Data management plan
   - [ ] CITI training certificate (human subjects research training)

   Timeline:
   - Submit application: [DATE]
   - Expected approval: [6-8 weeks for full review, 2-4 for expedited]
   - **DO NOT START DATA COLLECTION UNTIL APPROVED**

7. ETHICAL STATEMENT FOR CHAPTER 4:

   Draft ethics section:

   "This study was approved by the [INSTITUTION] Institutional Review Board (Protocol #XXXXX, approved [DATE]). All participants provided informed consent before participating. Data were stored securely on encrypted servers with access limited to the research team. Participants could withdraw at any time without penalty. [If applicable: Participants were compensated $XX for their time.]"

   OR if no IRB required:

   "This study does not involve human subjects. All analyses use publicly available datasets ([CITE]). No IRB approval was required."

Generate:
1. IRB application materials
2. Informed consent document
3. Data management plan
4. Ethics statement for methodology chapter
```

**EXPECTED OUTPUT:** Complete ethics package (2,000-3,000 words)

**SAVE AS:** `/03_Methodology/ethics/` directory with all documents

**⚠️ CRITICAL:** DO NOT collect data without IRB approval (if required)!

---

### Prompt 3.8: Write Methodology Chapter

**USER INPUT REQUIRED:**
- All previous prompts (3.1-3.7)
- Chapter 4 template from `/templates/dissertation/chapter_04_methodology.md`

**PROMPT:**
```
I've completed all methodology planning (Prompts 3.1-3.7).

Help me write a comprehensive Chapter 4: Methodology.

Use this structure:

**Section 4.1: Overview**
- Brief roadmap of chapter
- Restate research questions
- Preview methodology

Draft: [3-4 paragraphs, 300-400 words]

---

**Section 4.2: Research Approach**
- State paradigm (from Prompt 3.1)
- Justify research design (from Prompt 3.2)
- Explain alignment with RQs

Include:
- Paradigm statement
- Research design rationale
- Connection: RQ1 → [Method], RQ2 → [Method], RQ3 → [Method]

Draft: [600-800 words]

---

**Section 4.3-4.5: Components of My Method**

For each major component (algorithm, system, procedure):

**4.X.1 Problem Formulation**
- Mathematical formulation (if applicable)
- Variables and notation
- Assumptions

**4.X.2 Proposed Approach**
- Describe the method in detail
- Use pseudocode or diagrams
- Explain design choices

**4.X.3 Theoretical Analysis** (if applicable)
- Complexity analysis
- Proofs or guarantees

Draft each section: [800-1,200 words per component]

---

**Section 4.6: Experimental Design**

**4.6.1 Datasets/Participants**
From Prompt 3.3 (Sampling):
- Describe population
- Sampling method
- Sample size (with power analysis or justification)
- Inclusion/exclusion criteria
- Recruitment strategy

For computational: Describe datasets, cite sources, justify selection

Draft: [600-800 words]

**4.6.2 Data Collection Instruments**
From Prompt 3.4:
- Describe instruments (surveys, interviews, experimental protocol)
- If existing, cite validation studies
- If new, describe development and pilot testing

Draft: [500-700 words]

**4.6.3 Evaluation Metrics**
- Define each metric precisely
- Cite sources for metrics
- Explain why appropriate for RQs

Draft: [300-500 words]

**4.6.4 Baselines** (if applicable)
- Describe comparison methods
- Cite original papers
- Justify selection

Draft: [300-500 words]

**4.6.5 Experimental Protocol**
- Step-by-step procedure
- Conditions or configurations
- Hardware/software specifications

Draft: [400-600 words]

---

**Section 4.7: Data Analysis Plan**
From Prompt 3.5:
- Describe analysis approach for each RQ
- Specify statistical tests or coding approach
- Explain how analysis answers RQs

Draft: [600-800 words]

---

**Section 4.8: Validity & Reliability**
From Prompt 3.6:
- Discuss threats to validity and mitigation
- Describe reliability measures
- Justify rigor of approach

Draft: [600-800 words]

---

**Section 4.9: Ethical Considerations**
From Prompt 3.7:
- State IRB approval (number and date) or "Not applicable"
- Describe informed consent process
- Explain confidentiality protections
- Discuss any risks and mitigation

Draft: [300-500 words]

---

**Section 4.10: Reproducibility**
- Code availability
- Data availability
- Environment specifications
- Random seeds

Draft: [300-500 words]

---

WRITING GUIDELINES:
- Use past tense for completed work, future tense for planned work
- Be specific and detailed (someone should be able to replicate)
- Justify all choices (why this method? why this N?)
- Cite all sources (instruments, metrics, baselines, statistical tests)
- Include figures (research design diagram, analysis flowchart)

Generate section drafts, then I'll revise and polish.
```

**EXPECTED OUTPUT:** Complete Chapter 4 draft (6,000-8,000 words)

**SAVE AS:** `/03_Methodology/chapter_04_methodology_DRAFT.md`

**NEXT STEPS:**
1. Share draft with advisor for feedback
2. Revise based on feedback
3. Finalize IRB application (if needed)
4. **Get IRB approval before data collection**
5. **Get committee approval of methodology**

---

## ✅ QUALITY CHECKS FOR STAGE 3

Before moving to Stage 4 (Data Collection), verify:

### Content
- [ ] Research design clearly justified and appropriate for RQs
- [ ] Paradigm explicitly stated and aligned with methods
- [ ] Sampling strategy rigorous and feasible
- [ ] Sample size justified (power analysis or saturation)
- [ ] Data collection instruments valid and reliable
- [ ] Analysis plan detailed and defensible
- [ ] All ethical considerations addressed
- [ ] Reproducibility information complete

### IRB & Ethics
- [ ] **IRB APPROVAL OBTAINED** (if required) ← **CRITICAL**
- [ ] Informed consent documents finalized
- [ ] Data management plan in place
- [ ] CITI training completed (if required)

### Committee Approval
- [ ] **METHODOLOGY APPROVED BY COMMITTEE** ← **CRITICAL**
- [ ] Committee feedback incorporated
- [ ] Any concerns addressed

### Reproducibility
- [ ] Methodology is detailed enough for replication
- [ ] All instruments are documented
- [ ] Analysis plan is complete
- [ ] Code/protocols are organized

### Citations
- [ ] All existing instruments cited
- [ ] All metrics cited
- [ ] All statistical tests cited or explained
- [ ] All baselines/comparison methods cited

---

## 🔄 ITERATION & REVISION

Methodology chapters often require multiple revisions:

### Iteration 1: First Draft (Weeks 1-2)
- Use Prompts 3.1-3.8 to generate content
- Focus on completeness, not perfection
- Get all sections written

### Iteration 2: Advisor Review (Week 3)
- Share with advisor
- Get feedback on design appropriateness
- Identify gaps or weaknesses

### Iteration 3: Revise & Strengthen (Week 4)
- Address advisor feedback
- Strengthen justifications
- Add missing details
- Improve clarity

### Iteration 4: IRB Preparation (Week 5)
- Finalize all ethics materials
- Ensure reproducibility
- Prepare IRB application

### Iteration 5: Final Polish (Week 6)
- Proofread
- Check all citations
- Verify consistency
- Format figures/tables

**CRITICAL CHECKPOINT:** Do not move to data collection until:
1. Committee approves methodology
2. IRB approves ethics (if required)
3. Advisor signs off on plan

---

## 📁 SAVE YOUR OUTPUTS

```
/Dissertation_Project/
  /03_Methodology/
    - research_paradigm.md
    - research_design.md
    - design_diagram.pdf
    - sampling_plan.md
    - data_collection_instruments/
      * survey.pdf
      * interview_protocol.md
      * experiment_script.py
    - analysis_plan.md
    - codebook.xlsx
    - validity_reliability.md
    - ethics/
      * IRB_application.pdf
      * informed_consent.pdf
      * data_management_plan.md
      * IRB_approval.pdf (after approval)
    - chapter_04_methodology_DRAFT.md
    - chapter_04_methodology_FINAL.md
```

---

## 📚 RESOURCES

### Research Design:
- Creswell & Creswell (2018). *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*
- Shadish, Cook & Campbell (2002). *Experimental and Quasi-Experimental Designs*

### Sampling:
- Patton (2015). *Qualitative Research & Evaluation Methods* (for qualitative sampling)
- Cohen (1988). *Statistical Power Analysis* (for quantitative power analysis)
- Software: G*Power (free), pwr package in R

### Ethics:
- Belmont Report: https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/
- CITI Training: https://about.citiprogram.org/
- Your institution's IRB website

### Validity:
- Shadish, Cook & Campbell (2002). *Experimental and Quasi-Experimental Designs*
- Lincoln & Guba (1985). *Naturalistic Inquiry* (for qualitative trustworthiness)

---

## ⏱️ EXPECTED TIMELINE FOR STAGE 3

**Total Time:** 6-8 weeks (can overlap with Stage 2)

| Week | Task | Prompts | Hours |
|------|------|---------|-------|
| 1 | Establish paradigm, select design | 3.1, 3.2 | 10-15 |
| 2 | Sampling, instruments | 3.3, 3.4 | 15-20 |
| 3 | Analysis plan, validity | 3.5, 3.6 | 10-15 |
| 4 | Ethics, IRB prep | 3.7 | 10-15 |
| 5 | Write methodology chapter | 3.8 | 20-25 |
| 6 | Advisor review, revision | N/A | 10-15 |
| 7-8 | IRB submission & approval | N/A | waiting |

**Total Estimated Hours:** 75-105 hours of active work

**Note:** IRB approval timeline varies (2-12 weeks). Start early!

---

**⚠️ CRITICAL REMINDER:** Do NOT collect data without:
1. Committee approval of methodology
2. IRB approval (if human subjects)
3. Informed consent materials ready
4. Data management plan in place

Collecting data without approval is research misconduct and can invalidate your entire dissertation.

---

**Feed outputs from Stage 3 into Stage 4: Data Collection & Analysis**

---

**END OF STAGE 3: METHODOLOGY DESIGN**
