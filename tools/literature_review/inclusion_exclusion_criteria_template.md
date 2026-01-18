# Inclusion/Exclusion Criteria

**Project:** [Your Dissertation Title]
**Date:** [YYYY-MM-DD]
**Version:** 1.0

---

## Purpose

These criteria define which studies are eligible for inclusion in your systematic literature review. They must be:
- **Specific:** Clear enough that two independent reviewers would make the same decision
- **Objective:** Minimize subjective judgment
- **Defensible:** You can justify each criterion in your methodology chapter
- **Reproducible:** Another researcher could apply these criteria and get similar results

---

## Inclusion Criteria

Studies **MUST** meet **ALL** of the following criteria to be included:

### IC1: Time Period
- **Criterion:** Published between [YYYY] and [YYYY]
- **Rationale:** [Why this timeframe? E.g., "2015-2025 captures the era of deep learning breakthroughs"]
- **Edge case handling:**
  - Papers "in press" or "early access" with confirmed publication year: **Include**
  - Preprints without formal publication: **[Include/Exclude - specify]**

### IC2: Publication Type
- **Criterion:** Must be one of:
  - [ ] Peer-reviewed journal article
  - [ ] Peer-reviewed conference proceedings
  - [ ] PhD dissertation
  - [ ] Master's thesis
  - [ ] Technical report from recognized institution
  - [ ] Book chapter (if peer-reviewed)
  - [ ] Preprint (if meeting quality standards)

- **Rationale:** [Why these types? E.g., "Ensure academic rigor through peer review"]
- **Edge case handling:**
  - Workshop papers: **[Include/Exclude - specify]**
  - arXiv preprints with high citations: **[Include/Exclude - specify]**
  - Industry white papers: **[Include/Exclude - specify]**

### IC3: Language
- **Criterion:** Written in [English / list multiple languages]
- **Rationale:** [E.g., "Researcher fluency; most CS literature is in English"]
- **Edge case handling:**
  - Papers with English abstract but non-English full text: **[Include/Exclude - specify]**

### IC4: Subject/Topic Relevance
- **Criterion:** Paper must address at least one of:
  1. [Topic 1: e.g., "Explainable AI methods"]
  2. [Topic 2: e.g., "Facial recognition systems"]
  3. [Topic 3: e.g., "Fairness in machine learning"]

- **Rationale:** [How do these topics connect to your research questions?]
- **Edge case handling:**
  - Paper mentions topic briefly but focuses elsewhere: **Exclude**
  - Paper addresses topic implicitly without using exact keywords: **Include if clearly relevant**

### IC5: Methodological Relevance
- **Criterion:** Paper must include at least one of:
  - [ ] Empirical evaluation (experiments, user studies, case studies)
  - [ ] Theoretical contribution (proofs, formal models)
  - [ ] Novel algorithm/method
  - [ ] Systematic review/meta-analysis
  - [ ] Implementation/system description

- **Rationale:** [E.g., "Need evidence-based or theoretically grounded work"]
- **Edge case handling:**
  - Position papers without evaluation: **[Include/Exclude - specify]**
  - Purely tutorial/survey papers: **[Include/Exclude - specify]**

### IC6: Domain/Application
- **Criterion:** Paper must be in domain: [Specify domains, e.g., "Computer vision, machine learning, or biometric systems"]
- **Rationale:** [E.g., "Constrain scope to relevant application areas"]
- **Edge case handling:**
  - Cross-domain papers (e.g., medical imaging using facial recognition): **[Include/Exclude - specify]**

### IC7: Accessibility
- **Criterion:** Full text must be accessible
- **Rationale:** Cannot assess eligibility or extract data without full text
- **Edge case handling:**
  - Paywall but accessible via university: **Include**
  - Unable to obtain via interlibrary loan: **Exclude (document separately)**

### IC8: Quality Threshold (if applicable)
- **Criterion:** [Define minimum quality standards]
  - E.g., "Conference: CORE rank A or above"
  - E.g., "Journal: JCR Q1 or Q2"
  - E.g., "Minimum sample size N ≥ X for empirical studies"

- **Rationale:** [E.g., "Ensure methodological rigor"]
- **Edge case handling:**
  - High-quality paper in lower-ranked venue: **[Include/Exclude - specify]**

---

## Exclusion Criteria

Studies will be **AUTOMATICALLY EXCLUDED** if they meet **ANY** of the following:

### EC1: Publication Type
- **Exclude:**
  - Editorials
  - Opinion pieces
  - News articles
  - Blog posts
  - Advertisements
  - Letters to the editor (unless substantial empirical content)
  - Book reviews

- **Rationale:** Lack academic rigor or original contribution

### EC2: Language
- **Exclude:** Not in [specified language(s)]
- **Exception:** Papers with English translations available may be included if translation is official

### EC3: Duplicate Publications
- **Exclude:**
  - Same study published in multiple venues (keep most complete version)
  - Extended abstracts of full papers (keep full paper)

- **How to identify:** Check author lists, methods, results
- **Tiebreaker:** Keep journal version over conference, or more recent version

### EC4: Topic Out of Scope
- **Exclude papers focusing on:**
  - [Off-topic area 1: e.g., "Medical diagnosis unrelated to biometrics"]
  - [Off-topic area 2: e.g., "Natural language processing without vision component"]
  - [Off-topic area 3: e.g., "Hardware-only papers without algorithmic contribution"]

### EC5: Insufficient Detail
- **Exclude:**
  - Papers lacking methodological detail (cannot assess validity)
  - Results without statistical information (for empirical papers)
  - Claims without evidence or citations (for theoretical papers)

### EC6: Retracted or Withdrawn
- **Exclude:** Any paper that has been retracted or withdrawn
- **Check:** CrossRef, Retraction Watch database

### EC7: Inaccessible
- **Exclude:** Full text not available after exhausting:
  - University library access
  - Interlibrary loan
  - Author contact (request preprint)
  - ResearchGate/Academia.edu

- **Document:** Keep list of excluded papers due to access (report in appendix)

### EC8: Low Quality (if quality threshold defined)
- **Exclude:**
  - Papers with critical methodological flaws (e.g., no control group when needed)
  - Papers with statistical errors (e.g., p-hacking, HARKing)
  - Papers lacking reproducibility information

---

## Screening Decision Tree

Use this decision tree during screening:

```
START
  |
  v
Is publication type eligible (IC2)?
  ├─ NO → EXCLUDE (EC1)
  └─ YES → Continue
          |
          v
      Is language eligible (IC3)?
          ├─ NO → EXCLUDE (EC2)
          └─ YES → Continue
                  |
                  v
              Is it a duplicate (EC3)?
                  ├─ YES → EXCLUDE (keep best version)
                  └─ NO → Continue
                          |
                          v
                      Is time period eligible (IC1)?
                          ├─ NO → EXCLUDE
                          └─ YES → Continue
                                  |
                                  v
                              Is topic relevant (IC4)?
                                  ├─ NO → EXCLUDE (EC4)
                                  └─ YES → Continue
                                          |
                                          v
                                      Is methodology relevant (IC5)?
                                          ├─ NO → EXCLUDE
                                          └─ YES → Continue
                                                  |
                                                  v
                                              Is full text accessible (IC7)?
                                                  ├─ NO → EXCLUDE (EC7)
                                                  └─ YES → Continue
                                                          |
                                                          v
                                                      Does it meet quality threshold (IC8)?
                                                          ├─ NO → EXCLUDE (EC8)
                                                          └─ YES → **INCLUDE**
```

---

## Edge Cases and How to Handle Them

### Edge Case 1: Borderline Relevance
**Scenario:** Paper mentions your topic but isn't primarily about it
**Decision:** If topic appears in < 25% of paper (rough heuristic), **exclude**
**Rationale:** Need substantive treatment of topic

### Edge Case 2: Mixed Methods
**Scenario:** Paper uses both qualitative and quantitative methods
**Decision:** **Include** if at least one method is rigorous
**Rationale:** Mixed methods can provide richer insights

### Edge Case 3: Negative Results
**Scenario:** Paper reports "no significant effect" or failed replication
**Decision:** **Include** - negative results are valuable
**Rationale:** Publication bias avoidance, complete picture of field

### Edge Case 4: Preprints
**Scenario:** arXiv/bioRxiv paper not yet peer-reviewed
**Decision:** [Define your approach]
- Option A: Include if highly cited (>X citations) and methodologically sound
- Option B: Exclude all preprints
- Option C: Include but flag as "not peer-reviewed" in synthesis
**Rationale:** [Balance timeliness vs. quality control]

### Edge Case 5: Industry White Papers
**Scenario:** High-quality technical report from company (e.g., Google, Microsoft)
**Decision:** [Define your approach]
- Option A: Include if rigorous methodology, even without formal peer review
- Option B: Exclude (not peer-reviewed)
**Rationale:** [Your field's norms]

### Edge Case 6: Outdated But Seminal Papers
**Scenario:** Highly influential paper from before your time window
**Decision:** **Include as exception** if paper is foundational (cite >1000 times)
**Document:** Note exception in methods section
**Rationale:** Some papers are too important to exclude

### Edge Case 7: Non-English Abstract Available
**Scenario:** Paper in [other language] with English abstract only
**Decision:** **Exclude** - cannot assess full text
**Alternative:** If abstract suggests high relevance, seek translation
**Rationale:** Need full methodological detail

### Edge Case 8: Conference Extended to Journal
**Scenario:** Same authors, same study, published in both conference and journal
**Decision:** **Include journal version only** (typically more complete)
**Check:** Compare methods and results to confirm they're the same study
**Rationale:** Avoid double-counting

---

## Applying Criteria: Examples

### Example 1: ✅ INCLUDE

**Citation:** Smith, J., & Doe, A. (2023). Explainable AI for facial recognition using SHAP. *Journal of Machine Learning Research*, 24(1), 1-30.

**Assessment:**
- IC1 (Time): 2023 ✅
- IC2 (Type): Peer-reviewed journal ✅
- IC3 (Language): English ✅
- IC4 (Topic): Explainable AI + facial recognition ✅
- IC5 (Method): Empirical evaluation ✅
- IC6 (Domain): Machine learning ✅
- IC7 (Access): Available via university ✅
- IC8 (Quality): JMLR is top-tier journal ✅

**Decision:** **INCLUDE**

---

### Example 2: ❌ EXCLUDE (EC4 - Topic)

**Citation:** Jones, K. (2022). Natural language processing for sentiment analysis. *ACL Conference*, pp. 100-110.

**Assessment:**
- IC1 (Time): 2022 ✅
- IC2 (Type): Peer-reviewed conference ✅
- IC3 (Language): English ✅
- IC4 (Topic): NLP, not related to facial recognition or explainability in vision ❌

**Decision:** **EXCLUDE** - Topic out of scope (EC4)

---

### Example 3: ❌ EXCLUDE (EC1 - Publication Type)

**Citation:** Tech Blog. (2024). "Why XAI is the future." Retrieved from techblog.com

**Assessment:**
- IC2 (Type): Blog post ❌

**Decision:** **EXCLUDE** - Not a scholarly publication (EC1)

---

### Example 4: ⚠️ UNCERTAIN → Full-Text Screening

**Citation:** Brown, L. (2021). Interpretable models for computer vision. *IEEE Transactions on Pattern Analysis*, 43(5), 200-215.

**Assessment from abstract:**
- IC1 (Time): 2021 ✅
- IC2 (Type): Peer-reviewed journal ✅
- IC4 (Topic): "Computer vision" mentioned, but unclear if facial recognition is addressed

**Decision:** **UNCERTAIN** - Move to full-text screening to assess IC4

---

## Documentation During Screening

For **each excluded paper**, record:

| Citation | Exclusion Reason | Specific Criterion | Notes |
|----------|------------------|-------------------|-------|
| Author (Year) | Topic out of scope | EC4 | Focused on medical imaging only |
| Author (Year) | Not accessible | EC7 | Paywall, not in university database |
| Author (Year) | Duplicate | EC3 | Conference version; kept journal version |

---

## Inter-Rater Reliability

**For solo screening:**
1. Screen a random 10% sample twice (separated by ≥1 week)
2. Calculate self-agreement rate
3. If <90%, revisit criteria for clarity

**For dual screening:**
1. Both reviewers independently screen all (or subset)
2. Calculate Cohen's kappa
3. Resolve disagreements through discussion
4. If kappa <0.6, revisit criteria

---

## Reporting in Dissertation

### Methods Section Text:

> We applied the following inclusion criteria: (1) published between [years], (2) peer-reviewed scholarly publications, (3) written in English, (4) addressing [topics], and (5) including empirical evaluation or theoretical contribution. Exclusion criteria were: (1) editorials or opinion pieces, (2) duplicate publications, (3) studies lacking methodological detail, and (4) retracted papers. Full inclusion and exclusion criteria are detailed in Appendix X. [If solo:] Screening was performed by a single reviewer (the author), with 10% of records re-screened for consistency (agreement rate: X%). [If dual:] Two reviewers independently screened all records, with disagreements resolved through discussion (Cohen's kappa = X.XX, indicating [excellent/good] agreement).

---

## Version Control

| Version | Date | Changes | Reason |
|---------|------|---------|--------|
| 1.0 | [YYYY-MM-DD] | Initial criteria | Protocol development |
| 1.1 | [YYYY-MM-DD] | [Change made] | [Rationale] |

**IMPORTANT:** If you modify criteria after starting screening, document here and justify in your methods section.

---

**RULE 1 Compliance:**
✅ Criteria must be defined BEFORE screening (no post-hoc changes)
✅ Any deviations from protocol must be transparently reported
✅ Cannot exclude papers simply because they contradict your hypothesis
✅ Must report number excluded for each criterion (PRISMA requirement)
