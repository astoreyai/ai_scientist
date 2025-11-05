# Stage 1: Topic Development & Research Questions
## Detailed Prompt Chain

---

## 🎯 SUBCOMPONENTS

1. Topic Selection & Refinement
2. Research Gap Identification
3. Research Questions Formulation
4. Theoretical Framework Selection
5. Scope Definition

---

## 📥 REQUIRED INFORMATION (INPUTS)

- General area of interest
- Academic background/discipline
- Available resources (time, data access, funding)
- Career goals/motivations
- Preliminary reading done
- Advisor preferences/requirements

---

## 📤 DELIVERABLES (OUTPUTS)

1. Refined topic statement (1-2 paragraphs)
2. 3-5 specific research questions
3. Theoretical framework outline
4. Scope boundaries document
5. Preliminary research plan

---

## 🤖 AI PROMPT CHAINS

### Prompt 1.1: Topic Brainstorming & Refinement

**USER INPUT REQUIRED:**
- Broad field of interest
- 2-3 areas within that field you find compelling
- Any constraints (access, time, resources)

**PROMPT:**
\`\`\`
I'm developing a dissertation topic in [FIELD]. I'm particularly interested in [AREA 1], [AREA 2], and [AREA 3].

My constraints are:
- Timeline: [X months/years]
- Data access: [describe what you can access]
- Resources: [funding, software, equipment available]

Please help me:
1. Identify 5 specific, researchable topics within these areas
2. For each topic, explain:
   - Current relevance and importance
   - Feasibility given my constraints
   - Potential research gaps
   - Expected contribution to the field
3. Rank them by combination of impact and feasibility
4. Highlight any emerging trends that might make certain topics more valuable

Format the output as a comparison table.
\`\`\`

**EXPECTED OUTPUT:** Comparison table of 5 topics with feasibility scores

---

### Prompt 1.2: Research Gap Analysis

**USER INPUT REQUIRED:**
- Selected topic from Prompt 1.1
- 3-5 key papers you've already read (titles and authors)

**PROMPT:**
\`\`\`
My selected dissertation topic is: [TOPIC FROM 1.1]

I've read these key papers:
1. [Author, Year, Title]
2. [Author, Year, Title]
3. [Author, Year, Title]

Based on this topic, help me:
1. Identify what is already well-researched in this area
2. Identify 5-7 potential research gaps, including:
   - Methodological gaps (approaches not yet tried)
   - Theoretical gaps (frameworks not applied)
   - Contextual gaps (populations/settings not studied)
   - Temporal gaps (outdated studies needing updates)
3. For each gap, explain:
   - Why it matters
   - Who would care about filling this gap
   - Preliminary thoughts on how to address it
4. Recommend which gaps are most suitable for a dissertation

Prioritize gaps that are:
- Significant but manageable in scope
- Feasible with available methods
- Likely to lead to publications
\`\`\`

**EXPECTED OUTPUT:** Prioritized list of research gaps with justification

---

### Prompt 1.3: Research Questions Formulation

**USER INPUT REQUIRED:**
- Selected research gap from Prompt 1.2
- Preferred research approach (qualitative/quantitative/mixed)

**PROMPT:**
\`\`\`
Research Gap: [SELECTED GAP FROM 1.2]
Research Approach: [qualitative/quantitative/mixed methods]

Help me formulate research questions that:
1. Create one overarching research question that addresses this gap
2. Develop 3-5 specific sub-questions that:
   - Are answerable with my chosen approach
   - Build logically toward answering the main question
   - Have clear, measurable outcomes
   - Are neither too broad nor too narrow for a dissertation

For each question, specify:
- What type of data would be needed to answer it
- What methods could address it
- Potential challenges in answering it
- How it contributes to the overall research goal

Ensure questions follow these criteria:
- SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- Aligned with dissertation-level expectations
- Original contribution to knowledge
- Feasible within typical dissertation constraints
\`\`\`

**EXPECTED OUTPUT:** Structured research questions with implementation notes

---

### Prompt 1.4: Theoretical Framework Selection

**USER INPUT REQUIRED:**
- Research questions from Prompt 1.3
- Discipline/field

**PROMPT:**
\`\`\`
My research questions are:
[PASTE QUESTIONS FROM 1.3]

My discipline is: [FIELD/DISCIPLINE]

Help me select an appropriate theoretical framework:

1. Suggest 4-5 theoretical frameworks commonly used in my field that could inform this research
2. For each framework, explain:
   - Core concepts and assumptions
   - How it relates to my research questions
   - Strengths for my particular study
   - Limitations or criticisms I should be aware of
   - Key scholars/foundational texts
3. Recommend whether I should:
   - Use a single framework
   - Combine multiple frameworks
   - Develop a new integrated framework
4. Provide a preliminary outline of how to apply the chosen framework to my study

Include examples of how other researchers have successfully used these frameworks in similar contexts.
\`\`\`

**EXPECTED OUTPUT:** Framework comparison and recommendation with application outline

---

### Prompt 1.5: Scope Definition & Boundaries

**USER INPUT REQUIRED:**
- Research questions from 1.3
- Theoretical framework from 1.4
- Practical constraints

**PROMPT:**
\`\`\`
Research Questions: [FROM 1.3]
Theoretical Framework: [FROM 1.4]
Constraints: [timeline, resources, access]

Help me define clear scope boundaries:

1. Define what IS included in this dissertation:
   - Specific populations/subjects
   - Geographic/contextual boundaries
   - Time period
   - Specific variables or phenomena
   - Methodological approaches

2. Define what is explicitly EXCLUDED and why:
   - Related topics that are out of scope
   - Populations not being studied
   - Alternative approaches not being used

3. Create inclusion/exclusion criteria for:
   - Literature review
   - Data collection
   - Analysis

4. Identify potential scope creep risks and how to avoid them

5. Provide a one-paragraph "scope statement" that clearly defines the boundaries of this research

This scope should be:
- Defendable and logical
- Achievable within dissertation constraints
- Sufficient to make a meaningful contribution
- Clear enough to guide all subsequent research decisions
\`\`\`

**EXPECTED OUTPUT:** Comprehensive scope definition document with inclusion/exclusion criteria

---

## ✅ QUALITY CHECKS FOR STAGE 1

Before moving to Stage 2 (Literature Review), verify:

- [ ] Topic is specific enough to be manageable but broad enough to be significant
- [ ] Research gap is clearly identified and justified
- [ ] Research questions are SMART and answerable
- [ ] Theoretical framework is appropriate and well-understood
- [ ] Scope is clearly defined with explicit boundaries
- [ ] All deliverables are documented and saved
- [ ] Advisor/committee has reviewed and approved topic

---

## 🔄 ITERATION GUIDANCE

If any quality check fails:
- Return to relevant prompt
- Refine inputs based on feedback
- Re-run prompt with updated information
- Document why changes were made

---

## 📁 SAVE YOUR OUTPUTS

Create a folder structure:
\`\`\`
/Dissertation_Project/
  /01_Topic_Development/
    - topic_comparison_table.md
    - research_gaps_analysis.md
    - research_questions_final.md
    - theoretical_framework_notes.md
    - scope_definition.md
    - advisor_feedback.md
\`\`\`

Feed these outputs into Stage 2: Literature Review
