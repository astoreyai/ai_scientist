# PRISMA Flow Diagram Template

**Based on:** PRISMA 2020 Statement (http://prisma-statement.org/)

---

## How to Use This Template

1. Complete your literature search following `search_protocol_template.md`
2. Fill in the numbers below at each stage
3. Copy this text-based flowchart to your dissertation
4. For final dissertation, convert to a visual diagram using:
   - draw.io (free, open-source)
   - Microsoft PowerPoint/Visio
   - LaTeX TikZ
   - PRISMA Flow Diagram Generator: http://prisma.thetacollaborative.ca/

---

## PRISMA 2020 Flow Diagram (Text Version)

```
┌─────────────────────────────────────────────────────────────────┐
│                        IDENTIFICATION                             │
└─────────────────────────────────────────────────────────────────┘

Records identified from:
├─ Database 1 (e.g., Scopus): n = [___]
├─ Database 2 (e.g., Web of Science): n = [___]
├─ Database 3 (e.g., [field-specific]): n = [___]
├─ Other sources (e.g., Google Scholar): n = [___]
└─ TOTAL: n = [___]

Records removed before screening:
├─ Duplicate records removed: n = [___]
├─ Records marked as ineligible by automation tools: n = [___]
└─ Records removed for other reasons: n = [___]

                              ↓

┌─────────────────────────────────────────────────────────────────┐
│                         SCREENING                                 │
└─────────────────────────────────────────────────────────────────┘

Records screened (title/abstract): n = [___]

Records excluded (title/abstract): n = [___]
├─ Reason 1 [e.g., wrong topic]: n = [___]
├─ Reason 2 [e.g., wrong methodology]: n = [___]
├─ Reason 3 [e.g., wrong publication type]: n = [___]
└─ Other reasons: n = [___]

                              ↓

Reports sought for retrieval: n = [___]

Reports not retrieved: n = [___]
├─ Reason [e.g., paywall, no access]: n = [___]

                              ↓

┌─────────────────────────────────────────────────────────────────┐
│                         ELIGIBILITY                               │
└─────────────────────────────────────────────────────────────────┘

Reports assessed for eligibility (full-text): n = [___]

Reports excluded (full-text): n = [___]
├─ Reason 1 [e.g., did not meet inclusion criterion X]: n = [___]
├─ Reason 2 [e.g., insufficient data]: n = [___]
├─ Reason 3 [e.g., low quality]: n = [___]
└─ Other reasons: n = [___]

                              ↓

┌─────────────────────────────────────────────────────────────────┐
│                         INCLUDED                                  │
└─────────────────────────────────────────────────────────────────┘

Studies included in review: n = [___]

Studies included from:
├─ Database searches: n = [___]
├─ Backward citation search: n = [___]
├─ Forward citation search: n = [___]
└─ Other sources: n = [___]

```

---

## Fill-in-the-Blank Summary

**Total records identified:** [___]

**Records after duplicates removed:** [___]

**Records screened (title/abstract):** [___]

**Records excluded at title/abstract stage:** [___]

**Full-text articles assessed:** [___]

**Full-text articles excluded:** [___]

**Studies included in final review:** [___]

**Inclusion rate:** [___]% (studies included / total screened)

---

## Detailed Exclusion Reasons (Full-Text Stage)

Document each excluded paper and reason:

| Citation | Exclusion Reason | Specific Criterion Violated |
|----------|------------------|------------------------------|
| Author (Year) | [e.g., Wrong population] | [e.g., Inclusion criterion 2.4] |
| Author (Year) | [e.g., Insufficient data] | [e.g., Quality criterion] |
| Author (Year) | [e.g., Not peer-reviewed] | [e.g., Inclusion criterion 2.2] |
| ... | ... | ... |

**Note:** Keep this detailed table for your methods section appendix. The PRISMA diagram shows summary counts only.

---

## Search Date Information

| Database | Search Date | Results | After Deduplication |
|----------|-------------|---------|---------------------|
| Scopus | [YYYY-MM-DD] | [N] | [N] |
| Web of Science | [YYYY-MM-DD] | [N] | [N] |
| [Other DB] | [YYYY-MM-DD] | [N] | [N] |
| Google Scholar | [YYYY-MM-DD] | [N] | [N] |
| **TOTAL** | - | **[N]** | **[N]** |

---

## Citation Network Analysis

**Backward citation search:**
- Papers selected for reference mining: [N] (typically 5-10 key papers)
- Additional relevant papers found: [N]
- Papers meeting inclusion criteria: [N]

**Forward citation search:**
- Papers selected for citation tracking: [N]
- Papers citing these works: [N]
- Papers meeting inclusion criteria: [N]

**Hand search:**
- Journals hand-searched: [List journals]
- Additional papers found: [N]

---

## Timeline of Search Process

| Activity | Date | Notes |
|----------|------|-------|
| Search protocol finalized | [YYYY-MM-DD] | |
| Database searches conducted | [YYYY-MM-DD] to [YYYY-MM-DD] | |
| Duplicates removed | [YYYY-MM-DD] | Tool used: [e.g., Zotero] |
| Title/abstract screening | [YYYY-MM-DD] to [YYYY-MM-DD] | |
| Full-text retrieval | [YYYY-MM-DD] to [YYYY-MM-DD] | |
| Full-text screening | [YYYY-MM-DD] to [YYYY-MM-DD] | |
| Data extraction | [YYYY-MM-DD] to [YYYY-MM-DD] | |
| Final review complete | [YYYY-MM-DD] | |

---

## Inter-Rater Reliability (if applicable)

**For solo PhD:**
- Screening performed by: [Your name]
- Quality check: [Re-screened random sample of N papers]
- Consistency check: [X% agreement on re-screening]

**For multi-reviewer process:**
- Screeners: [Names]
- Independent screening: [% of total]
- Disagreements resolved by: [Process]
- Cohen's kappa: [value] (if calculated)
- Interpretation: [Excellent/Good/Moderate/Fair/Poor agreement]

---

## How to Report in Dissertation

### Method Section Text (Template):

> We conducted a systematic literature review following PRISMA guidelines (Page et al., 2021). We searched [list databases] on [dates] using the search strategy detailed in Appendix X. Our search yielded [N] records. After removing [N] duplicates, we screened [N] records by title and abstract, excluding [N] records that did not meet our inclusion criteria. We retrieved [N] full-text articles for detailed assessment. Of these, [N] were excluded for the following reasons: [list main reasons with counts]. We supplemented our database searches with backward citation analysis of [N] key papers and forward citation tracking, which yielded an additional [N] papers. Our final review included [N] studies. Figure X presents the PRISMA flow diagram.

### Figure Caption:

> **Figure X:** PRISMA 2020 flow diagram showing the systematic literature search and screening process. From [N] initial records, [N] studies met inclusion criteria and were included in the final review.

---

## LaTeX Code for Visual Diagram

For a publication-ready diagram, use this LaTeX TikZ template:

```latex
% Add to preamble:
% \usepackage{tikz}
% \usetikzlibrary{shapes,arrows,positioning}

\begin{figure}[h]
\centering
\begin{tikzpicture}[
    node distance=1.5cm,
    box/.style={rectangle, draw, minimum width=8cm, minimum height=1cm, align=center},
    arrow/.style={->, thick}
]

% Identification
\node[box] (id) {Records identified from databases\\n = [N]};
\node[box, right=of id] (removed) {Records removed before screening\\Duplicates: n = [N]\\Other: n = [N]};

% Screening
\node[box, below=of id] (screen) {Records screened\\n = [N]};
\node[box, right=of screen] (excluded1) {Records excluded\\n = [N]};

% Eligibility
\node[box, below=of screen] (assess) {Full-text articles assessed\\n = [N]};
\node[box, right=of assess] (excluded2) {Full-text articles excluded\\Reason 1: n = [N]\\Reason 2: n = [N]};

% Included
\node[box, below=of assess] (included) {Studies included in review\\n = [N]};

% Arrows
\draw[arrow] (id) -- (screen);
\draw[arrow] (screen) -- (assess);
\draw[arrow] (assess) -- (included);

\end{tikzpicture}
\caption{PRISMA 2020 flow diagram of the systematic literature review process.}
\label{fig:prisma}
\end{figure}
```

---

## PRISMA Checklist Compliance

Ensure your literature review chapter includes:

- [ ] PRISMA flow diagram (this document)
- [ ] Full search strings (in appendix)
- [ ] Inclusion/exclusion criteria (in methods)
- [ ] Search dates and databases (in methods)
- [ ] Number of reviewers and reliability (in methods)
- [ ] Reasons for exclusion with counts
- [ ] List of included studies (appendix or table)
- [ ] Data extraction fields (methods)
- [ ] Quality assessment criteria (methods)
- [ ] Synthesis approach (methods)

---

## References

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, 372.

**Full PRISMA website:** http://prisma-statement.org/

**PRISMA Explanation and Elaboration:** http://prisma-statement.org/documents/PRISMA_2020_explanation_elaboration.pdf

---

**RULE 1 Compliance:**
✅ PRISMA ensures transparency and reproducibility
✅ Every number must be truthful (actual count, not estimate)
✅ If you estimate (e.g., Google Scholar results), explicitly state it
✅ Deviations from planned protocol must be documented
