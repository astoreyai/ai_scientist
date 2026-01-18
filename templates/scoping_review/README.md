# Scoping Review Template

**Template Type:** Scoping Review
**Framework:** Arksey & O'Malley (2005), updated by Levac et al. (2010) and JBI (2020)
**Reporting Standard:** PRISMA-ScR (PRISMA Extension for Scoping Reviews)
**Use Case:** Map breadth of literature on a topic, identify research gaps, clarify concepts

---

## What is a Scoping Review?

A **scoping review** is a type of knowledge synthesis that systematically maps the literature on a topic, identifying key concepts, theories, evidence, and research gaps.

**When to use a scoping review:**
- The topic is emerging or heterogeneous
- You want to map breadth of literature (not depth)
- Research question is exploratory
- You need to identify gaps for future research
- You want to clarify concepts and definitions

**Scoping Review vs. Systematic Review:**

```
Characteristic        Scoping Review              Systematic Review
──────────────────────────────────────────────────────────────────────
Purpose               Map literature breadth      Synthesize evidence depth
Research Question     Broad, exploratory          Focused, specific (PICO)
Search Strategy       Comprehensive, iterative    Comprehensive, exhaustive
Study Selection       Broad inclusion             Narrow inclusion
Quality Assessment    Usually NOT done            Always done (RoB)
Synthesis             Narrative, descriptive      Statistical (meta-analysis)
                                                  or narrative
Outcome               Evidence map, gaps          Pooled effect estimate,
                                                  recommendations
──────────────────────────────────────────────────────────────────────
```

---

## Arksey & O'Malley Framework (5 Stages)

### Stage 1: Identify the Research Question

Use the **PCC framework** (not PICO):
- **P**opulation: Who? (patients, providers, settings)
- **C**oncept: What? (interventions, phenomena, experiences)
- **C**ontext: Where? (setting, culture, geography)

**Example:**
```
Research Question: "What is known about mobile health interventions 
                    for chronic disease self-management in low- and 
                    middle-income countries?"

P = Patients with chronic diseases (diabetes, hypertension, COPD, etc.)
C = Mobile health (mHealth) interventions (apps, SMS, wearables)
C = Low- and middle-income countries (LMICs)
```

### Stage 2: Identify Relevant Studies

**Search Strategy:**
- **Databases:** 3-6 databases minimum (e.g., PubMed, Embase, CINAHL, PsycINFO, Web of Science, Scopus)
- **Grey literature:** Google Scholar, conference proceedings, dissertations
- **Hand-searching:** Reference lists of included studies and key journals
- **Iterative:** Refine search terms based on initial results

**Inclusion/Exclusion Criteria:**
- **Broad** - cast a wide net
- **Iterative** - may evolve as you learn about the topic

**Example:**
```
INCLUSION:
✓ Any study design (RCT, observational, qualitative, mixed methods)
✓ mHealth interventions for chronic disease self-management
✓ Conducted in LMICs (World Bank classification)
✓ Adults ≥18 years
✓ Published 2010-present (past 15 years)
✓ English, Spanish, French languages

EXCLUSION:
✗ mHealth for acute conditions (e.g., trauma, infections)
✗ mHealth for diagnosis only (not self-management)
✗ Studies conducted in high-income countries
✗ Pediatric populations (<18 years)
```

### Stage 3: Study Selection

**Two-Stage Screening:**
1. **Title/Abstract Screening:** Two independent reviewers, liberal inclusion threshold
2. **Full-Text Screening:** Two independent reviewers, apply eligibility criteria

**Inter-Rater Reliability:**
- Calculate κ (kappa) for 10% sample
- Target: κ > 0.6 (substantial agreement)
- Resolve conflicts through discussion or third reviewer

**PRISMA-ScR Flow Diagram:**
```
Records identified through database searching: [n=X]
Additional records identified through other sources: [n=Y]
                        ↓
Records after duplicates removed: [n=Z]
                        ↓
Records screened (title/abstract): [n=Z]
    → Records excluded: [n=A]
                        ↓
Full-text articles assessed for eligibility: [n=B]
    → Full-text articles excluded, with reasons: [n=C]
      Reason 1 (e.g., wrong population): [n]
      Reason 2 (e.g., wrong intervention): [n]
                        ↓
Studies included in scoping review: [n=D]
```

### Stage 4: Chart the Data

**Data Charting** (NOT "data extraction" - broader, more iterative)

Use a **charting form** (spreadsheet or database) to extract:

**Standard Fields:**
- Author, year, country
- Study design/methodology
- Population characteristics
- Concept (intervention, phenomenon)
- Context (setting)
- Key findings relevant to research question

**Iterative Process:**
- Pilot chart 5-10 studies
- Refine charting form
- Two reviewers independently chart data
- Discuss discrepancies

**Example Charting Form Excerpt:**
```
Study | Design    | Population  | mHealth Type | Chronic Disease | Setting | Key Findings
──────────────────────────────────────────────────────────────────────────────────────────
Chen  | RCT       | Adults with | SMS text     | Type 2 diabetes | Urban   | Improved
2019  |           | T2DM, n=120 | reminders    |                 | India   | HbA1c by
      |           |             |              |                 |         | 0.8%
──────────────────────────────────────────────────────────────────────────────────────────
```

### Stage 5: Collate, Summarize, and Report Results

**Descriptive Analysis:**
- Frequency counts (e.g., # studies by year, country, design)
- Tables and figures (bar charts, evidence maps, bubble plots)
- Narrative summary organized by themes or characteristics

**Common Organizational Schemes:**
1. **By study characteristic:** Publication year, geography, design
2. **By concept:** Type of intervention, outcome domain
3. **By context:** Setting, population characteristics
4. **Thematic:** Identified themes from synthesis

**Example Summary:**
```
RESULTS

Study Characteristics:
  - 127 studies included
  - Publication years: 2010-2025 (peak 2020-2023 with 58 studies)
  - Countries: India (32), Kenya (18), South Africa (15), Brazil (12), others (50)
  - Designs: RCT (45), Quasi-experimental (28), Observational (31), Qualitative (23)

Population:
  - Chronic diseases: T2DM (52), hypertension (34), COPD (18), mixed (23)
  - Mean age: 45-65 years (predominantly middle-aged adults)
  - Gender: 58% female across studies

Concept (mHealth Interventions):
  - SMS text reminders (48 studies) - most common
  - Mobile apps (38 studies)
  - Wearables (15 studies)
  - Voice calls (12 studies)
  - Multi-modal (14 studies)

Context:
  - Settings: Urban (72), Rural (34), Mixed (21)
  - Infrastructure: Variable mobile network access (reported in 67 studies)

Key Findings:
  1. Most studies focused on medication adherence (89/127)
  2. Majority reported positive effects on self-management behaviors
  3. Few studies addressed sustainability beyond pilot phase
  4. Limited reporting of implementation challenges
  5. Health literacy and digital literacy identified as barriers

Research Gaps:
  - Limited evidence from rural settings
  - Few studies on multi-morbidity management
  - Lack of cost-effectiveness analyses
  - Need for longer follow-up periods (>12 months)
  - Implementation science frameworks rarely applied
```

---

## PRISMA-ScR Checklist (20 Items + 2 Optional)

| Section          | Item | Checklist Item | Location |
|------------------|------|----------------|----------|
| **TITLE**        | 1    | Identify the report as a scoping review | Title page |
| **ABSTRACT**     | 2    | Structured summary (background, objectives, methods, results, conclusions) | Abstract |
| **INTRODUCTION** |      |                |          |
| Rationale        | 3    | Describe the rationale | Intro, ¶1-2 |
| Objectives       | 4    | Provide explicit research question and objectives (PCC) | Intro, ¶3 |
| **METHODS**      |      |                |          |
| Protocol & reg   | 5    | Indicate if protocol exists, where accessed, registration info | Methods, ¶1 |
| Eligibility      | 6    | Specify inclusion/exclusion criteria | Methods, p.3 |
| Info sources     | 7    | Describe all sources (databases, registers, websites, dates) | Methods, p.3 |
| Search           | 8    | Present full search strategy for ≥1 database | Appendix A |
| Selection        | 9    | State process for study selection | Methods, p.4 |
| Data charting    | 10a  | Describe methods for charting data | Methods, p.4 |
| Data items       | 10b  | List and define all variables charted | Methods, p.4 |
| Critical appraisal| 11  | If done, describe methods (OPTIONAL for scoping reviews) | N/A |
| Synthesis        | 12   | Describe methods of synthesis | Methods, p.5 |
| **RESULTS**      |      |                |          |
| Selection        | 13   | Give numbers at each stage (PRISMA-ScR flow diagram) | Results, Fig 1 |
| Study characteristics | 14 | Present characteristics of included sources | Results, Table 1 |
| Critical appraisal| 15  | If done, present results (OPTIONAL) | N/A |
| Results synthesis| 16   | Present results of synthesis | Results, p.8-15 |
| **DISCUSSION**   |      |                |          |
| Summary          | 17   | Summarize main results, link to research question | Discussion, ¶1 |
| Limitations      | 18   | Discuss limitations of scoping review process | Discussion, p.3 |
| Conclusions      | 19   | General interpretation, implications for future research | Discussion, ¶final |
| **FUNDING**      |      |                |          |
| Funding          | 20   | Describe funding sources and role | Funding section |

**Note:** Critical appraisal of individual sources (#11, #15) is OPTIONAL for scoping reviews. Most scoping reviews do NOT assess study quality/risk of bias.

---

## Template Files Included

This template includes:

1. **README.md** (this file) - Overview and instructions
2. **protocol_template.md** - Complete protocol template
3. **search_strategy.md** - Database search strategy template
4. **screening_forms/** - Title/abstract and full-text screening forms
5. **data_charting_template.xlsx** - Excel template for data charting
6. **prisma_scr_checklist.md** - PRISMA-ScR checklist for reporting
7. **manuscript_template.md** - Manuscript structure template

---

## Getting Started

### Step 1: Define Your Research Question (Stage 1)

1. Open `protocol_template.md`
2. Complete the PCC framework section
3. Write 1-2 broad research questions
4. Define objectives

### Step 2: Develop Search Strategy (Stage 2)

1. Open `search_strategy.md`
2. Identify 3-6 databases to search
3. Develop search string with key concepts
4. Test search in pilot database (e.g., PubMed)
5. Refine based on results
6. Finalize search for all databases

### Step 3: Screen Studies (Stage 3)

1. Export search results to reference manager (Zotero, EndNote, Covidence)
2. Remove duplicates
3. Use `screening_forms/title_abstract_form.md` for Stage 1 screening
4. Two reviewers independently screen 10% to calculate κ
5. Complete title/abstract screening
6. Use `screening_forms/full_text_form.md` for Stage 2 screening
7. Track exclusions with reasons
8. Generate PRISMA-ScR flow diagram

### Step 4: Chart Data (Stage 4)

1. Open `data_charting_template.xlsx`
2. Pilot chart 5-10 studies
3. Refine charting form (add/remove fields)
4. Two reviewers independently chart data
5. Resolve discrepancies through discussion

### Step 5: Synthesize and Report (Stage 5)

1. Open `manuscript_template.md`
2. Conduct descriptive analysis (frequencies, tables, figures)
3. Organize results by theme, characteristic, or concept
4. Create evidence map or visual summary
5. Identify research gaps
6. Complete PRISMA-ScR checklist (`prisma_scr_checklist.md`)
7. Write discussion and conclusions

---

## Common Mistakes to Avoid

1. **Making scoping review too narrow** - Scoping reviews should be broad; if question is narrow, do a systematic review instead
2. **Conducting quality appraisal** - Usually not done in scoping reviews (exceptions exist)
3. **Synthesizing effect estimates** - Scoping reviews are descriptive, not meta-analytic
4. **Using PRISMA instead of PRISMA-ScR** - Use the scoping review extension
5. **Not iterating** - Scoping reviews are iterative; search strategy and charting form should evolve
6. **Ignoring grey literature** - Important for scoping reviews to capture breadth

---

## Key References

**Methodology:**
- Arksey H, O'Malley L. Scoping studies: towards a methodological framework. *Int J Soc Res Methodol*. 2005;8(1):19-32.
- Levac D, Colquhoun H, O'Brien KK. Scoping studies: advancing the methodology. *Implement Sci*. 2010;5:69.
- Peters MDJ, Godfrey C, McInerney P, et al. Chapter 11: Scoping Reviews (2020 version). *JBI Manual for Evidence Synthesis*. 2020.

**Reporting:**
- Tricco AC, Lillie E, Zarin W, et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation. *Ann Intern Med*. 2018;169(7):467-473. [Link](https://www.acpjournals.org/doi/10.7326/M18-0850)

**PCC Framework:**
- Joanna Briggs Institute. *The Joanna Briggs Institute Reviewers' Manual 2015: Methodology for JBI Scoping Reviews*. 2015.

---

## Support Tools

**Reference Management:**
- [Covidence](https://www.covidence.org) - Systematic review platform (supports scoping reviews)
- [DistillerSR](https://www.evidencepartners.com/products/distillersr-systematic-review-software/) - Systematic review software
- [Zotero](https://www.zotero.org) - Free reference manager

**PRISMA-ScR Tools:**
- [PRISMA-ScR Flow Diagram Template](http://www.prisma-statement.org/Extensions/ScopingReviews)
- [PRISMA-ScR Checklist](http://www.prisma-statement.org/Extensions/ScopingReviews)

**Data Charting:**
- Excel or Google Sheets (simple, accessible)
- REDCap (structured, auditable, multi-user)
- Tableau or R for visualizations (evidence maps)

---

## Example Scoping Reviews

**High-Quality Published Examples:**

1. **Implementation science example:**
   Colquhoun HL, et al. Scoping reviews: time for clarity in definition, methods, and reporting. *J Clin Epidemiol*. 2014;67(12):1291-1294.

2. **mHealth example:**
   Peiris D, et al. Behaviour change strategies for mobile health. *Cochrane Database Syst Rev*. 2019.

3. **Chronic disease example:**
   Morton K, et al. Using digital interventions for self-management of chronic physical health conditions: A meta-ethnography review. *Patient Educ Couns*. 2017;100(4):616-635.

---

**Need Help?** See Tutorial 2 (Literature Review) for more details on systematic search strategies and screening processes.

---

*This template follows Arksey & O'Malley (2005) methodology and PRISMA-ScR (2018) reporting guidelines.*
