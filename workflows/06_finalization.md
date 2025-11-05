# Stage 6: Finalization & Defense Preparation
## Detailed Prompt Chain

**Purpose:** Transform complete dissertation draft into final, polished document and prepare for successful defense

**Timeline:** 4-8 weeks (depending on committee feedback turnaround)

**Effort Level:** HIGH (requires attention to detail, multiple iterations, presentation preparation)

---

## 🎯 SUBCOMPONENTS

1. Abstract Writing
2. References & Citations
3. Front Matter
4. Formatting & Style
5. Appendices
6. Final Proofreading
7. Defense Preparation
8. Post-Defense Revisions

---

## 📥 REQUIRED INFORMATION (INPUTS)

**Before starting this workflow, you MUST have:**

- ✅ Complete drafts of all 8 chapters (Chapters 1-8)
- ✅ All figures and tables finalized
- ✅ Reference list compiled (in reference manager)
- ✅ Institutional formatting requirements (from Graduate School website)
- ✅ Defense presentation requirements (time limit, format)
- ✅ Committee availability for defense scheduling

**If any of these are missing, complete them first before proceeding.**

---

## 📤 DELIVERABLES (OUTPUTS)

By the end of this workflow, you will have:

1. ✅ Final abstract (250-350 words)
2. ✅ Complete, formatted reference list
3. ✅ All front matter (title page, acknowledgments, dedication, TOC, lists)
4. ✅ Appendices (organized and referenced)
5. ✅ Fully formatted dissertation (per institutional requirements)
6. ✅ Defense presentation (15-20 slides, 25-30 minutes)
7. ✅ Defense talking points and anticipated Q&A
8. ✅ Final dissertation PDF submitted to committee
9. ✅ Post-defense revisions completed

---

## 🤖 AI PROMPT CHAINS

### Prompt 6.1: Write the Abstract

**USER INPUT REQUIRED:**
- Word limit (check your university requirements, usually 250-350 words)
- All 8 chapters (for extracting key information)
- Research questions (from Chapter 1)
- Key findings (from Chapter 6)

**PROMPT:**
```
I need to write a dissertation abstract with the following constraints:

REQUIREMENTS:
- Word limit: [250 words for some institutions, 350 for others - CHECK YOUR REQUIREMENTS]
- Must be self-contained (understandable without reading dissertation)
- Must follow this structure:

STRUCTURE (allocate words carefully):
1. Background/Context (20-30 words, 1-2 sentences)
   - What is the broad area?
   - Why does this area matter?

2. Problem/Gap (30-40 words, 2 sentences)
   - What specific problem exists?
   - What gap in knowledge/practice?

3. Purpose Statement (15-25 words, 1 sentence)
   - "This dissertation [verb: investigates/develops/evaluates]..."
   - State clear objective

4. Research Questions (20-30 words, 1-2 sentences)
   - List 2-3 main RQs (brief versions)
   - OR state overarching RQ

5. Methodology (40-60 words, 2-3 sentences)
   - Research approach (quantitative/qualitative/mixed)
   - Data collection method
   - Sample/dataset
   - Analysis method

6. Key Findings (80-100 words, 3-5 sentences)
   - Answer to RQ1: [finding + metric if quantitative]
   - Answer to RQ2: [finding + metric if quantitative]
   - Answer to RQ3: [finding + metric if quantitative]
   - **This is the MOST IMPORTANT section - allocate most words here**

7. Conclusions/Implications (40-60 words, 2-3 sentences)
   - Theoretical contribution
   - Practical implication
   - Significance statement

MY DISSERTATION DETAILS:
- Title: [paste full title]
- Field: [e.g., Computer Science, Education, Psychology]
- Research Questions: [paste RQs from Chapter 1]
- Methodology: [brief: e.g., "Mixed methods with n=250 survey + 30 interviews"]
- Key Findings:
  - RQ1: [paste key finding with metrics]
  - RQ2: [paste key finding with metrics]
  - RQ3: [paste key finding with metrics]
- Main Contribution: [paste 1-sentence contribution statement from Chapter 1]

Please help me draft an abstract that:
1. Stays within [X] word limit
2. Follows the structure above
3. Is clear and jargon-free
4. Highlights quantitative results (specific numbers)
5. Is suitable for interdisciplinary readers
```

**EXPECTED OUTPUT:**
- First draft of abstract (250-350 words)
- Word count breakdown by section
- Suggestions for cutting/expanding if over/under limit

**ITERATION TIPS:**
- **Iteration 1:** Get all content in (likely over word limit)
- **Iteration 2:** Cut ruthlessly to meet word limit
  - Remove: "This dissertation", "The results show that"
  - Use active voice: "We found" not "It was found that"
  - Combine sentences
- **Iteration 3:** Ensure clarity and flow
- **Iteration 4:** Check keywords are present (for searchability)
- **Iteration 5:** Proofread

**SAVE AS:** `/06_Finalization/abstract_v1.md`, `/06_Finalization/abstract_v2.md`, ... `/06_Finalization/abstract_FINAL.md`

**⚠️ COMMON MISTAKES:**
- ❌ Using jargon without definition
- ❌ Being too vague ("Results were positive")
- ❌ Omitting quantitative results (always include metrics!)
- ❌ Going over word limit (will be rejected by Graduate School)
- ❌ Including citations (abstracts typically have no citations)

---

### Prompt 6.2: Finalize References

**USER INPUT REQUIRED:**
- Citation style (APA 7th, Chicago, MLA, IEEE, etc. - CHECK YOUR REQUIREMENTS)
- Reference manager software (Zotero, Mendeley, EndNote, or manual)
- Access to all chapters (to check in-text citations)

**PROMPT:**
```
I need to create a perfect reference list for my dissertation.

REQUIREMENTS:
- Citation style: [APA 7th / Chicago / MLA / IEEE - specify]
- Current reference count: [e.g., 187 references]
- Reference manager: [Zotero / Mendeley / EndNote / Manual]

TASK 1: REFERENCE LIST FORMATTING
Help me ensure my reference list is formatted correctly:

1. ALPHABETICAL ORDER:
   - Last name, First initial format (APA)
   - Alphabetical by first author's last name
   - Multiple works by same author: chronological order

2. HANGING INDENT:
   - First line flush left
   - Subsequent lines indented 0.5 inches

3. SPACING:
   - Double-spaced throughout (APA)
   - No extra space between entries

4. COMMON REFERENCE TYPES (provide format for each):
   - Journal article (with DOI)
   - Journal article (without DOI)
   - Book
   - Book chapter
   - Dissertation/Thesis
   - Conference paper
   - Website/Online source
   - Software/Code repository
   - Dataset

TASK 2: IN-TEXT CITATION CHECK
Help me verify citation consistency:

1. ORPHAN CITATIONS (in-text citation but no reference entry):
   - How to find: Search for (Author, Year) patterns in text
   - How to fix: Add reference entry OR remove citation

2. ORPHAN REFERENCES (reference entry but never cited):
   - How to find: Use reference manager's "unused references" feature
   - How to fix: Remove from reference list OR add citation to text

3. INCONSISTENT AUTHOR NAMES:
   - Check: "Smith, J." in text vs. "Smith, John" in references
   - Standardize to one format

TASK 3: COMMON ERRORS TO CHECK

For APA 7th specifically:
- [ ] DOIs formatted as https://doi.org/10.xxxx (not doi: or dx.doi.org)
- [ ] Article titles in sentence case (not title case)
- [ ] Journal names in title case and italicized
- [ ] Book titles in sentence case and italicized
- [ ] Volume numbers italicized, issue numbers not italicized
- [ ] "Retrieved from" only for unstable URLs (not for journal articles)
- [ ] Author names: Last, F. M. (not Last, First Middle)
- [ ] "et al." for 21+ authors in reference list, all authors for <21
- [ ] Year in parentheses: (2023). not 2023. or (2023)
- [ ] No period after DOI

TASK 4: REFERENCE MANAGER EXPORT
If using reference manager:
1. Select all references in library
2. Check for duplicates (remove)
3. Verify all fields complete (especially DOIs, page numbers)
4. Export as [APA 7th / Chicago / etc.] formatted bibliography
5. Copy into Word/LaTeX dissertation document
6. Manually check formatting (managers sometimes make errors)

TASK 5: MANUAL FORMATTING (if not using reference manager)
1. List all references alphabetically in spreadsheet
2. Format each reference according to style guide
3. Double-check against official examples
4. Copy into dissertation document
5. Apply hanging indent formatting
```

**EXPECTED OUTPUT:**
- Formatted reference list (100-200 references typical)
- Citation consistency report (orphan citations/references identified)
- Corrected reference formatting

**TOOLS:**
- **APA 7th:** https://apastyle.apa.org/style-grammar-guidelines/references
- **Chicago:** https://www.chicagomanualofstyle.org/tools_citationguide.html
- **Zotero:** Free, open-source reference manager
- **Citation Checker:** Many universities have citation formatting tools

**SAVE AS:** `/06_Finalization/references_formatted.docx`

**⚠️ CRITICAL:**
- Incomplete references (missing DOI, page numbers) may cause Graduate School rejection
- Inconsistent formatting throughout will require revision before final submission
- Budget 4-6 hours for thorough reference checking

---

### Prompt 6.3: Write Front Matter

**USER INPUT REQUIRED:**
- University/department formatting requirements (margins, fonts, spacing)
- Dissertation title (finalized)
- Committee member names and titles
- Degree information (PhD in X, Department of Y, University of Z)
- Defense date
- People to acknowledge (advisor, committee, funders, family, friends)
- Dedication (optional)

**INSTRUCTIONS:**

Front matter appears **before Chapter 1** and includes (in order):

1. **Title Page**
2. **Copyright Page** (optional, check requirements)
3. **Approval/Signature Page** (if required)
4. **Dedication** (optional, 1 page max)
5. **Acknowledgments** (1-2 pages)
6. **Abstract** (from Prompt 6.1)
7. **Table of Contents**
8. **List of Figures**
9. **List of Tables**
10. **List of Abbreviations** (if applicable)

#### Component 1: Title Page

**PROMPT:**
```
Help me create a properly formatted title page:

REQUIRED INFORMATION:
- Dissertation title: [paste full title]
- Your name: [full legal name as appears on university records]
- Degree: [e.g., Doctor of Philosophy]
- Major/Field: [e.g., Computer Science]
- University: [full official name]
- Year: [year of defense]

FORMATTING (check your university's requirements - this is common format):
- All text centered
- Specific spacing between elements
- Specific font size for title vs. other text

TYPICAL FORMAT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[3-4 blank lines from top]

[DISSERTATION TITLE IN ALL CAPS]
[14pt font, bold, centered]

[2 blank lines]

by

[1 blank line]

[Your Full Legal Name]
[12pt font, centered]

[2 blank lines]

A Dissertation Submitted in Partial Fulfillment
of the Requirements for the Degree of
[Degree Name]
in the Department of [Department]
at [University Name]

[2 blank lines]

[City, State]
[Month Year]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CHECK YOUR UNIVERSITY'S REQUIREMENTS - format varies by institution!
```

**SAVE AS:** `/06_Finalization/front_matter/01_title_page.docx`

---

#### Component 2: Copyright Page (if required)

**FORMAT:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Centered, middle of page]

© [Year] [Your Full Name]
ALL RIGHTS RESERVED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**ALTERNATIVE (if releasing under open license):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Centered, middle of page]

© [Year] [Your Full Name]

This work is licensed under a Creative Commons
Attribution 4.0 International License.
(or other license as appropriate)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**SAVE AS:** `/06_Finalization/front_matter/02_copyright_page.docx`

---

#### Component 3: Approval/Signature Page (if required)

**FORMAT:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The dissertation of [Your Name] is approved:

[2 blank lines]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Committee Member 1 Name], [Title]     Date

[2 blank lines]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Committee Member 2 Name], [Title]     Date

[2 blank lines]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Committee Member 3 Name], [Title]     Date

[2 blank lines]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Advisor Name], [Title]               Date
Dissertation Committee Chair

[University Name]
[Year]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**NOTE:** Some universities require **actual signatures** (printed and signed), others accept digital. Check requirements.

**SAVE AS:** `/06_Finalization/front_matter/03_approval_page.docx`

---

#### Component 4: Dedication (OPTIONAL)

**PROMPT:**
```
Help me write a brief dedication (1 page max).

GUIDELINES:
- Personal and heartfelt
- Brief (1-3 sentences typical)
- Centered on page
- No quotation marks needed
- Can be to family, mentor, cause, etc.

EXAMPLES:

Example 1 (Simple):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Centered, middle of page]

To my parents,
whose unwavering support made this journey possible.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 2 (With quote):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Centered, middle of page]

To all who dare to ask "why?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 3 (Multiple):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Centered, middle of page]

To my wife, Sarah, for her endless patience,
to my advisor, Dr. Smith, for his wisdom,
and to my late grandmother, who believed in me
before I believed in myself.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**SAVE AS:** `/06_Finalization/front_matter/04_dedication.docx`

---

#### Component 5: Acknowledgments

**PROMPT:**
```
Help me write acknowledgments (1-2 pages).

WHO TO ACKNOWLEDGE (in this order):
1. Advisor (primary mentor)
2. Committee members (each by name)
3. Funding sources (NSF grant #, fellowship name, etc.)
4. Research assistants/collaborators
5. Department/university support
6. Family and friends
7. Anyone else who contributed

TONE:
- Professional but warm
- Specific (mention what each person contributed)
- Humble and grateful
- First person is acceptable here ("I would like to thank...")

STRUCTURE TEMPLATE:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACKNOWLEDGMENTS

I would like to express my deepest gratitude to the many people who made this
dissertation possible.

First and foremost, I thank my advisor, [Name], for [specific contribution:
guidance, patience, insight, etc.]. [Brief anecdote or specific example of
their mentorship]. Without [his/her/their] support, this work would not have
been possible.

I am grateful to my committee members, [Name 1], [Name 2], and [Name 3], for
their invaluable feedback and perspectives. [Specific contribution from each,
if possible: e.g., "Dr. Jones's expertise in X strengthened Chapter 3
considerably."]

This research was supported by [funding source with grant number]. I acknowledge
[Institution/Lab/Center] for providing [resources/facilities/data].

I thank my fellow graduate students in the [Department] for [intellectual
community/feedback/support], particularly [Name] for [specific help].

Finally, I thank my family, especially [names], for their unconditional love
and support throughout this journey. [Personal note: e.g., "My wife's patience
during late nights and weekend work cannot be overstated."]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LENGTH: 1-2 pages (don't exceed 2 pages)

⚠️ DO NOT FORGET:
- Funding sources (required by many grants)
- Committee members (each deserves recognition)
- Anyone who provided data, code, or resources
```

**SAVE AS:** `/06_Finalization/front_matter/05_acknowledgments.docx`

---

#### Component 6: Abstract (already written in Prompt 6.1)

**SAVE AS:** `/06_Finalization/front_matter/06_abstract.docx`

---

#### Component 7: Table of Contents

**AUTOMATIC GENERATION (Word):**
1. Ensure all chapter/section headings use Heading styles (Heading 1, 2, 3)
2. Place cursor where TOC should appear
3. References → Table of Contents → Automatic Table 1
4. Update TOC before final submission: Right-click → Update Field → Update entire table

**AUTOMATIC GENERATION (LaTeX):**
```latex
\tableofcontents
% LaTeX auto-generates from \chapter, \section, \subsection commands
```

**MANUAL (if required):**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TABLE OF CONTENTS

CHAPTER                                                    PAGE

1. INTRODUCTION ......................................... 1
   1.1 Motivation ........................................ 2
   1.2 Problem Statement ................................. 5
   1.3 Research Questions ................................ 8
   1.4 Contributions .................................... 10
   ...

2. LITERATURE REVIEW ................................... 15
   2.1 Introduction ..................................... 16
   2.2 Explainable AI ................................... 18
   ...

[Continue for all 8 chapters]

REFERENCES ............................................. 250

APPENDICES ............................................. 275
   Appendix A: Survey Instrument ........................ 276
   Appendix B: Interview Protocol ....................... 280
   ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**FORMATTING:**
- Leaders (dots) connecting chapter titles to page numbers
- Indentation for subsections
- Page numbers right-aligned

**SAVE AS:** `/06_Finalization/front_matter/07_table_of_contents.docx`

---

#### Component 8: List of Figures

**AUTOMATIC GENERATION (Word):**
1. Ensure all figures have captions (Insert Caption)
2. References → Insert Table of Figures

**FORMAT:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LIST OF FIGURES

FIGURE                                                     PAGE

1.1  Problem visualization diagram ...................... 12
1.2  Scope boundary diagram ............................. 15
1.3  Methodology overview flowchart ..................... 20

2.1  Literature review positioning matrix ............... 45
2.2  Chronological evolution of XAI methods ............. 52

3.1  Conceptual framework diagram ....................... 68
3.2  Visualization of key theorem ....................... 75
...

[Continue for all figures, typically 20-30 total]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**SAVE AS:** `/06_Finalization/front_matter/08_list_of_figures.docx`

---

#### Component 9: List of Tables

**AUTOMATIC GENERATION (Word):**
1. Ensure all tables have captions (Insert Caption → Table)
2. References → Insert Table of Tables

**FORMAT:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LIST OF TABLES

TABLE                                                      PAGE

2.1  Comparison of XAI methods .......................... 48
2.2  Summary of surveyed papers ......................... 56

4.1  Experimental design matrix ......................... 95
4.2  Hyperparameter settings ........................... 102

6.1  Accuracy results on LFW dataset ................... 145
6.2  Latency benchmarks ................................ 150
6.3  Fairness metrics .................................. 158
...

[Continue for all tables, typically 10-20 total]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**SAVE AS:** `/06_Finalization/front_matter/09_list_of_tables.docx`

---

#### Component 10: List of Abbreviations (if applicable)

**WHEN TO INCLUDE:**
- If you use 10+ abbreviations/acronyms throughout dissertation
- If field-specific terms need definition

**FORMAT:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LIST OF ABBREVIATIONS

AI       Artificial Intelligence
AUC      Area Under the Curve
CNN      Convolutional Neural Network
DNN      Deep Neural Network
EMA      Exponential Moving Average
GMMA     Guppy Multiple Moving Average
GPU      Graphics Processing Unit
LIME     Local Interpretable Model-agnostic Explanations
ML       Machine Learning
SHAP     SHapley Additive exPlanations
ViT      Vision Transformer
XAI      Explainable Artificial Intelligence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**ALPHABETICAL ORDER, left-aligned**

**SAVE AS:** `/06_Finalization/front_matter/10_list_of_abbreviations.docx`

---

### ASSEMBLING FRONT MATTER

**ORDER (from front to back):**
1. Title Page (page i - lowercase Roman numerals)
2. Copyright Page (page ii)
3. Approval Page (page iii)
4. Dedication (page iv - if included)
5. Acknowledgments (pages v-vi)
6. Abstract (pages vii-viii)
7. Table of Contents (pages ix-xi)
8. List of Figures (page xii)
9. List of Tables (page xiii)
10. List of Abbreviations (page xiv - if included)

**[Chapter 1 begins on page 1 - switch to Arabic numerals]**

**PAGE NUMBERING:**
- Front matter: lowercase Roman numerals (i, ii, iii, iv, ...)
- Main text (Chapter 1 onward): Arabic numerals (1, 2, 3, ...)
- Page numbers typically: bottom center or top right (check requirements)

**EXPECTED OUTPUT:**
- All 10 front matter components completed
- Properly numbered
- Formatted per institutional requirements

**SAVE AS:** `/06_Finalization/front_matter/FRONT_MATTER_COMPLETE.docx` (all components combined)

---

### Prompt 6.4: Format Dissertation

**USER INPUT REQUIRED:**
- University formatting guide (download from Graduate School website)
- Word processor (Microsoft Word or LaTeX)
- Complete dissertation draft (all chapters + front matter + references)

**INSTRUCTIONS:**

This prompt helps you apply institutional formatting requirements. **CHECK YOUR UNIVERSITY'S GUIDE** - requirements vary significantly.

**COMMON FORMATTING REQUIREMENTS:**

#### 1. MARGINS
**Typical requirements:**
- Top: 1 inch
- Bottom: 1 inch
- Left: 1.5 inches (for binding)
- Right: 1 inch

**Word:** Page Layout → Margins → Custom Margins
**LaTeX:** `\usepackage[top=1in, bottom=1in, left=1.5in, right=1in]{geometry}`

---

#### 2. FONT
**Typical requirements:**
- Font: Times New Roman, Arial, or similar
- Size: 12pt for body text
- Size: 10-11pt acceptable for footnotes, captions

**Word:** Home → Font → [Select font and size]
**LaTeX:** `\usepackage{times}` or `\usepackage{mathptmx}`

---

#### 3. SPACING
**Typical requirements:**
- Body text: Double-spaced
- Block quotes: Single-spaced, indented
- Footnotes: Single-spaced
- References: Single or double-spaced (varies - check requirements)

**Word:** Home → Paragraph → Line Spacing → 2.0
**LaTeX:** `\doublespacing` (requires `\usepackage{setspace}`)

---

#### 4. HEADING HIERARCHY
**Typical structure:**

**LEVEL 1 (CHAPTER):**
- All caps, bold, centered
- New page for each chapter
- Example: CHAPTER 1: INTRODUCTION

**Level 2 (Major Section):**
- Title case, bold, left-aligned
- Example: 1.1 Motivation

**Level 3 (Subsection):**
- Title case, bold, left-aligned
- Example: 1.1.1 Background

**Level 4 (if needed):**
- Sentence case, italicized, left-aligned
- Example: 1.1.1.1 Historical context

**Word:** Use Heading 1, Heading 2, Heading 3 styles (modify to match requirements)
**LaTeX:** `\chapter{}`, `\section{}`, `\subsection{}`, `\subsubsection{}`

---

#### 5. PAGE NUMBERING
**Typical requirements:**

**Front Matter:**
- Lowercase Roman numerals (i, ii, iii, ...)
- Bottom center OR top right
- Title page counted but not numbered (page i, but number not shown)

**Main Text:**
- Arabic numerals (1, 2, 3, ...)
- Chapter 1 starts on page 1
- Top right OR bottom center

**Word:**
1. Section breaks between front matter and Chapter 1
2. Insert → Page Number → Format → Number format (i, ii, iii vs. 1, 2, 3)
3. Different first page (to hide number on title page)

**LaTeX:**
```latex
\frontmatter % Roman numerals
\mainmatter  % Arabic numerals, reset to 1
```

---

#### 6. CITATION FORMAT
**Typical requirements:**
- In-text: (Author, Year) for APA; (Author Year) for Chicago; [1] for IEEE
- Reference list: Alphabetical (APA, Chicago) or numbered (IEEE)
- Hanging indent for reference list

**Covered in Prompt 6.2**

---

#### 7. FIGURE AND TABLE FORMATTING
**Typical requirements:**

**Figures:**
- Caption below figure
- Format: "Figure X.Y: [Caption text in sentence case]"
- Numbered consecutively within each chapter (or continuously)
- Example: Figure 3.2: Conceptual framework diagram

**Tables:**
- Caption above table
- Format: "Table X.Y: [Caption text in sentence case]"
- Numbered same as figures
- Example: Table 6.1: Accuracy results on LFW dataset

**Placement:**
- Figures/tables should appear AFTER first mention in text
- Can be on same page or next page
- Should not break across pages (keep together)

**Word:**
- Insert Caption (right-click figure/table)
- Modify caption style for formatting

**LaTeX:**
```latex
\begin{figure}[h]
  \centering
  \includegraphics[width=0.8\textwidth]{figure.pdf}
  \caption{Caption text here}
  \label{fig:conceptual}
\end{figure}
```

---

#### 8. EQUATION FORMATTING
**For STEM dissertations:**

**Display equations:**
- Centered
- Numbered on right (if referenced)
- Example:
  ```
                E = mc²                    (3.1)
  ```

**Word:** Insert → Equation → Design → Professional
**LaTeX:**
```latex
\begin{equation}
  E = mc^2
  \label{eq:einstein}
\end{equation}
```

---

### FORMATTING CHECKLIST

**Before submitting to committee:**

**Margins & Spacing:**
- [ ] All margins correct (top: 1", bottom: 1", left: 1.5", right: 1")
- [ ] Body text double-spaced
- [ ] Block quotes single-spaced and indented
- [ ] No extra space between paragraphs (unless required)

**Font & Typography:**
- [ ] Consistent font throughout (Times New Roman 12pt or equivalent)
- [ ] Footnotes/captions 10-11pt
- [ ] No orphan headings (heading at bottom of page with text on next)
- [ ] No widows (single line of paragraph at top/bottom of page)

**Page Numbering:**
- [ ] Front matter: Roman numerals (i, ii, iii, ...)
- [ ] Title page counted but not numbered
- [ ] Main text: Arabic numerals starting at 1
- [ ] Page numbers in correct location (top right or bottom center)
- [ ] Consistent throughout

**Headings:**
- [ ] Chapter headings: All caps, bold, centered
- [ ] Section headings: Title case, bold, left-aligned
- [ ] Consistent numbering (1.1, 1.2, ... OR 1.1.1, 1.1.2, ...)
- [ ] New page for each chapter

**Figures & Tables:**
- [ ] All figures have captions below
- [ ] All tables have captions above
- [ ] All numbered correctly (Figure X.Y, Table X.Y)
- [ ] All referenced in text before appearing
- [ ] List of Figures accurate
- [ ] List of Tables accurate

**References:**
- [ ] Formatted per style guide (APA, Chicago, IEEE)
- [ ] Alphabetical order (or numbered for IEEE)
- [ ] Hanging indent applied
- [ ] Consistent throughout
- [ ] All in-text citations have reference entries
- [ ] All reference entries are cited in text

**Table of Contents:**
- [ ] All chapters listed
- [ ] All major sections listed (1.1, 1.2, etc.)
- [ ] Page numbers accurate
- [ ] Leaders (dots) connecting titles to page numbers

**Overall:**
- [ ] No formatting inconsistencies
- [ ] Checked against university formatting guide
- [ ] Used formatting checklist from Graduate School (if provided)

---

### TOOLS FOR FORMATTING

**Microsoft Word:**
- **Styles:** Use built-in styles (Heading 1, 2, 3; Normal) - easier to modify consistently
- **Section Breaks:** Insert → Break → Section Break (Next Page) - for different page numbering
- **Table of Contents:** References → Table of Contents (auto-generates from headings)
- **Captions:** Right-click figure/table → Insert Caption

**LaTeX:**
- **Template:** Many universities provide official LaTeX templates
- **Packages:** `geometry` (margins), `setspace` (spacing), `hyperref` (clickable TOC)
- **Compile:** Compile multiple times for TOC/references to update

**PDF Submission:**
- Export to PDF (File → Save As → PDF)
- Check PDF matches formatting (sometimes fonts/spacing change)
- Ensure all hyperlinks work (TOC, citations)
- Check file size (<20MB typical requirement)

---

**EXPECTED OUTPUT:**
- Fully formatted dissertation meeting all institutional requirements
- Formatting checklist completed

**SAVE AS:** `/06_Finalization/DISSERTATION_FORMATTED.docx` (or .tex → .pdf)

**⏱️ TIME ESTIMATE:** 6-10 hours for thorough formatting

---

### Prompt 6.5: Organize Appendices

**USER INPUT REQUIRED:**
- Supplementary materials that don't fit in main chapters
- Institutional requirements for appendices (some have limits on length)

**INSTRUCTIONS:**

Appendices contain supplementary material that supports the dissertation but would disrupt the flow if included in main chapters.

#### WHAT GOES IN APPENDICES?

**INCLUDE in Appendices:**
- ✅ Full survey instruments (if you only showed excerpt in Chapter 4)
- ✅ Interview protocols (full questions, not just summary)
- ✅ Raw data tables (if summarized in Chapter 6)
- ✅ Extended statistical output (full ANOVA tables, regression output)
- ✅ Code listings (key algorithms, not entire codebase)
- ✅ Additional figures/tables referenced but not critical
- ✅ Supplementary proofs (if main proofs are in Chapter 3)
- ✅ IRB approval letter (if required by university)
- ✅ Informed consent forms
- ✅ Supplementary analyses (robustness checks, sensitivity analyses)

**DO NOT INCLUDE in Appendices:**
- ❌ Entire codebase (link to GitHub instead)
- ❌ Full datasets (provide data availability statement instead)
- ❌ Irrelevant materials
- ❌ Low-quality figures
- ❌ Duplicate information (already fully presented in chapters)

---

#### APPENDIX ORGANIZATION

**Lettering:**
- Appendix A, Appendix B, Appendix C, ... (capital letters)
- Each appendix starts on new page

**Numbering:**
- Figures in appendices: Figure A.1, Figure A.2, ... (for Appendix A)
- Tables in appendices: Table B.1, Table B.2, ... (for Appendix B)

**Order:**
- Order of appearance in dissertation
- If Appendix A is referenced in Chapter 3, and Appendix B in Chapter 5, then A comes before B

---

#### EXAMPLE APPENDIX STRUCTURE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDICES

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDIX A: SURVEY INSTRUMENT

[Full survey with all questions, response options, instructions]

This appendix contains the complete survey instrument used in the study
described in Chapter 4. The survey was administered via Qualtrics and
consisted of 45 questions across 5 sections:

Section 1: Demographics (5 questions)
1. What is your age? [Open-ended]
2. What is your gender? [Multiple choice: Male, Female, Non-binary, Prefer not to say]
...

[Continue with all 45 questions]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDIX B: INTERVIEW PROTOCOL

[Full interview protocol]

This appendix contains the semi-structured interview protocol used in Phase 2
of the study (Chapter 4, Section 4.3.2). Interviews lasted 45-60 minutes.

INTRODUCTION SCRIPT:
"Thank you for agreeing to participate in this interview. As outlined in the
consent form, this interview will take approximately 45-60 minutes..."

MAIN QUESTIONS:
1. Can you describe your experience with [topic]?
   - Probe: When did you first encounter [topic]?
   - Probe: What challenges did you face?

[Continue with all interview questions and probes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDIX C: FULL STATISTICAL OUTPUT

[Extended statistical tables]

This appendix contains complete statistical output referenced in Chapter 6.

Table C.1: Full ANOVA Table for RQ1
┌─────────────────┬────────┬──────┬────────┬─────────┬─────────┐
│ Source          │ df     │ SS   │ MS     │ F       │ p       │
├─────────────────┼────────┼──────┼────────┼─────────┼─────────┤
│ Between Groups  │ 2      │ 45.3 │ 22.65  │ 12.45   │ <.001   │
│ Within Groups   │ 247    │ 450.2│ 1.82   │         │         │
│ Total           │ 249    │ 495.5│        │         │         │
└─────────────────┴────────┴──────┴────────┴─────────┴─────────┘

Post-hoc tests (Tukey HSD):
- Group A vs. Group B: p = .002, d = 0.65
- Group A vs. Group C: p = .001, d = 0.78
- Group B vs. Group C: p = .456, d = 0.18 (ns)

[Continue with all extended statistical output]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDIX D: KEY ALGORITHM IMPLEMENTATIONS

[Code listings]

This appendix contains pseudocode and implementation details for key algorithms
described in Chapter 5.

Algorithm D.1: Hierarchical SHAP (Python)

```python
def hierarchical_shap(model, x, M):
    """
    Compute hierarchical SHAP values

    Args:
        model: Trained model
        x: Input sample
        M: Number of features

    Returns:
        phi: SHAP values (M-dimensional)
    """
    # Level 1: Coarse approximation
    phi_coarse = approximate_shap(model, x, M//4)

    # Level 2: Refinement
    phi_fine = refine_shap(model, x, phi_coarse, M)

    return phi_fine
```

[Continue with other key algorithms]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPENDIX E: IRB APPROVAL LETTER

[Scanned IRB approval letter]

[Include if required by university]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### REFERENCING APPENDICES IN TEXT

**In main chapters, reference appendices like this:**

> "The complete survey instrument is provided in Appendix A."

> "Full statistical output, including post-hoc tests, is available in Appendix C."

> "See Appendix D for implementation details of the hierarchical SHAP algorithm."

**Every appendix MUST be referenced at least once in the main text.**

---

#### FORMATTING APPENDICES

**Headings:**
- APPENDIX A: [TITLE IN ALL CAPS]
- Each appendix starts on new page

**Page Numbering:**
- Continue from main text (Arabic numerals)
- Example: If Chapter 8 ends on page 248, Appendix A starts on page 249

**In Table of Contents:**
```
APPENDICES .............................................. 249
  Appendix A: Survey Instrument ......................... 250
  Appendix B: Interview Protocol ........................ 255
  Appendix C: Full Statistical Output ................... 260
  Appendix D: Key Algorithm Implementations ............. 265
  Appendix E: IRB Approval Letter ....................... 270
```

---

**PROMPT FOR ORGANIZING:**
```
Help me organize my appendices:

I have the following supplementary materials:
1. [List item 1: e.g., "Full survey - 45 questions"]
2. [List item 2: e.g., "Interview protocol"]
3. [List item 3: e.g., "Extended statistical tables"]
4. [...]

TASKS:
1. Determine what should be included in appendices (vs. main chapters or omitted)
2. Assign appendix letters (A, B, C, ...) in order of reference in dissertation
3. Create title for each appendix
4. Format each appendix consistently
5. Ensure each appendix is referenced in main text

FORMATTING:
- Each appendix starts new page
- Heading: APPENDIX A: [TITLE]
- Include brief intro paragraph explaining content
- Number figures/tables within appendix (Figure A.1, Table B.2, etc.)
```

**EXPECTED OUTPUT:**
- Organized appendices (lettered A, B, C, ...)
- Each appendix properly formatted
- All appendices referenced in main text
- Appendices listed in Table of Contents

**SAVE AS:** `/06_Finalization/appendices/APPENDIX_A.docx`, `/06_Finalization/appendices/APPENDIX_B.docx`, etc.

**⏱️ TIME ESTIMATE:** 2-4 hours

---

### Prompt 6.6: Proofread Dissertation

**USER INPUT REQUIRED:**
- Complete, formatted dissertation (all chapters + front matter + references + appendices)
- Time (ideally 1-2 weeks AFTER finishing writing - fresh eyes)
- Proofreading tools (Grammarly, university writing center, peer readers)

**INSTRUCTIONS:**

Proofreading is the **final check** before submitting to committee. This is NOT editing for content - that should be done already. This is checking for:
- Typos and spelling errors
- Grammar and punctuation
- Formatting consistency
- Citation accuracy
- Overall polish

#### MULTI-PASS PROOFREADING STRATEGY

**⚠️ CRITICAL:** Do NOT try to proofread everything at once. Use multiple passes, each with a specific focus.

---

**PASS 1: CONTENT ACCURACY (Focus: Facts and Figures)**

**What to check:**
- [ ] All numbers are correct (check against raw data/analysis output)
- [ ] All figure/table numbers referenced correctly in text
  - Example: "as shown in Figure 3.2" → verify Figure 3.2 exists and shows what you claim
- [ ] All chapter cross-references correct
  - Example: "as discussed in Chapter 2" → verify discussion exists in Chapter 2
- [ ] All equations numbered correctly
- [ ] All appendix references correct

**How:**
- Open dissertation and original data/analysis files side-by-side
- Verify every number, statistic, figure reference

**⏱️ Time:** 4-6 hours

---

**PASS 2: CITATIONS AND REFERENCES (Focus: Academic Integrity)**

**What to check:**
- [ ] Every in-text citation has a reference entry
- [ ] Every reference entry is cited in text (no orphan references)
- [ ] Citation format consistent throughout
  - (Author, Year) vs. (Author Year) vs. [1]
- [ ] Reference list formatted correctly (see Prompt 6.2)
- [ ] DOIs included and formatted correctly
- [ ] Page numbers included where required

**How:**
- Use reference manager's "unused references" feature
- Search for common citation patterns: (Author, or [1] or Author (Year)
- Check random sample of 20-30 references against style guide

**Tools:**
- Zotero: Tools → Check for Orphaned Citations
- Mendeley: Similar feature
- Manual: Ctrl+F search for (Author, patterns

**⏱️ Time:** 3-4 hours

---

**PASS 3: GRAMMAR AND SPELLING (Focus: Language)**

**What to check:**
- [ ] Spelling errors (typos, homophone errors like "their" vs. "there")
- [ ] Grammar errors (subject-verb agreement, tense consistency)
- [ ] Punctuation errors (commas, semicolons, dashes)
- [ ] Capitalization consistency
- [ ] Commonly confused words (affect/effect, its/it's, principle/principal)

**How:**
- Run spell check (Word: F7, or Review → Spelling & Grammar)
- Use Grammarly (free or premium)
- Read aloud (forces you to slow down and catch errors)

**Tools:**
- **Microsoft Word Spell Check:** Basic but essential
- **Grammarly:** https://www.grammarly.com (free version sufficient)
- **ProWritingAid:** Alternative to Grammarly
- **Read Aloud:** Natural Reader, or Word's built-in Read Aloud

**Common Errors to Watch For:**
- ❌ "The data shows" → ✅ "The data show" (data is plural)
- ❌ "affect" (verb) vs. "effect" (noun) - commonly confused
- ❌ "its" (possessive) vs. "it's" (it is) - commonly confused
- ❌ Inconsistent tense: "We found that X was... and Y is..." → pick one tense

**⏱️ Time:** 6-8 hours (for 300+ page dissertation)

---

**PASS 4: FORMATTING CONSISTENCY (Focus: Visual Polish)**

**What to check:**
- [ ] Heading hierarchy consistent (all Level 1 headings same format, all Level 2 same, etc.)
- [ ] Font consistent throughout (no random Times New Roman → Arial switches)
- [ ] Spacing consistent (no random single-spaced paragraphs in double-spaced text)
- [ ] Figure/table captions formatted consistently
  - All Figure X.Y: Caption below
  - All Table X.Y: Caption above
- [ ] Page numbers correct and consistent
- [ ] No orphan headings (heading at bottom of page with no text)
- [ ] No widows (single line of paragraph at top/bottom of page)

**How:**
- Scroll through entire dissertation looking only at formatting
- Check first page of each chapter (consistency in chapter heading format)
- Check all figures (consistency in caption format)
- Check all tables (consistency in caption format)

**⏱️ Time:** 2-3 hours

---

**PASS 5: FINAL POLISH (Focus: Overall Quality)**

**What to check:**
- [ ] Read abstract - does it accurately represent dissertation?
- [ ] Read each chapter's first and last paragraph - do they flow?
- [ ] Check all hyperlinks work (in PDF: TOC links, citation links)
- [ ] Check figure quality (resolution, readability)
- [ ] Check table formatting (aligned, readable)
- [ ] Verify acknowledgments include everyone
- [ ] Verify all required front matter included

**How:**
- Print dissertation (or read on different device for fresh perspective)
- Read straight through (not editing, just reading for flow)
- Click all hyperlinks in PDF to verify

**⏱️ Time:** 4-6 hours

---

#### TOOLS AND STRATEGIES

**Tool 1: Grammarly**
```
1. Install Grammarly (browser extension or desktop app)
2. Upload dissertation to Grammarly
3. Review all suggestions
4. Accept/reject based on context
5. Note: Grammarly sometimes suggests incorrect changes for technical writing - use judgment
```

**Tool 2: Text-to-Speech (Read Aloud)**
```
1. Word: Review → Read Aloud
2. Or: Natural Reader (free online tool)
3. Listen while following along
4. Catches errors you'd miss reading silently
5. Particularly good for awkward phrasing
```

**Tool 3: Print Reading**
```
1. Print dissertation (or at least key chapters)
2. Read with pen in hand
3. Mark errors directly on paper
4. Studies show: people catch more errors on paper than screen
```

**Tool 4: Peer Proofreading**
```
1. Ask colleague/friend to proofread 1-2 chapters (not entire dissertation - too much)
2. Focus on Introduction and Conclusion (most visible chapters)
3. Provide specific guidance: "Check for typos and awkward phrasing, not content"
4. Reciprocate (offer to proofread their work)
```

**Tool 5: University Writing Center**
```
1. Many universities offer dissertation proofreading services
2. Book appointment 2-3 weeks in advance (they're busy near deadlines)
3. They can catch errors you've become blind to
4. Note: They may only review excerpt (e.g., 30 pages) - choose Introduction, Conclusion, 1 other chapter
```

**Tool 6: Plagiarism Check**
```
1. Run through Turnitin or similar (your university may provide access)
2. Should be <10% similarity (excluding references)
3. High similarity in specific sections may indicate insufficient paraphrasing
4. Note: Some similarity is expected (common phrases, your own published papers)
```

---

#### PROOFREADING CHECKLIST

**Before submitting to committee:**

**Content:**
- [ ] All numbers verified against source data
- [ ] All figure/table references correct
- [ ] All chapter cross-references correct
- [ ] All equations correct and numbered

**Citations:**
- [ ] Every citation has reference entry
- [ ] No orphan references
- [ ] Citation format consistent
- [ ] Reference list formatted correctly

**Language:**
- [ ] Spell check run (and errors corrected)
- [ ] Grammar check run (Grammarly or equivalent)
- [ ] Read aloud (by you or text-to-speech)
- [ ] No commonly confused words (affect/effect, its/it's)

**Formatting:**
- [ ] Heading hierarchy consistent
- [ ] Font consistent
- [ ] Spacing consistent
- [ ] Figure/table captions consistent
- [ ] Page numbers correct
- [ ] No orphan headings or widows

**Final Checks:**
- [ ] Abstract accurate
- [ ] Hyperlinks work (in PDF)
- [ ] Figures high quality
- [ ] Tables readable
- [ ] Acknowledgments complete
- [ ] Front matter complete

**Final Review:**
- [ ] Printed and read (or read on different device)
- [ ] Peer proofread (at least 1-2 chapters)
- [ ] University writing center review (if available)

---

#### COMMON ERRORS TO AVOID

**Error 1: Inconsistent Terminology**
- ❌ Chapter 1: "machine learning model", Chapter 3: "ML model", Chapter 5: "learning model"
- ✅ Pick one term and use consistently: "machine learning (ML) model" first mention, then "ML model"

**Error 2: Tense Shifts**
- ❌ "We found that X was significant. Y is also important."
- ✅ "We found that X was significant. Y was also important." (consistent past tense)

**Error 3: Number/Word Inconsistency**
- ❌ "three datasets... 5 experiments... twelve participants"
- ✅ Spell out 0-9, use numerals for 10+ (or follow your style guide)

**Error 4: Missing Hyphenation**
- ❌ "Well known algorithm" (as adjective)
- ✅ "Well-known algorithm" (hyphenate compound adjectives before nouns)

**Error 5: Incorrect Citation Placement**
- ❌ "Smith (2020) found that X. (Smith, 2020)"
- ✅ "Smith (2020) found that X." (don't double-cite)

---

**EXPECTED OUTPUT:**
- Polished, error-free dissertation
- Proofreading checklist completed
- List of corrections made (for your records)

**SAVE AS:** `/06_Finalization/DISSERTATION_PROOFREAD_FINAL.docx` (or .pdf)

**⏱️ TIME ESTIMATE:** 20-30 hours total (across all 5 passes)

**⏰ SCHEDULE:** Spread over 1-2 weeks (don't try to do it all in one day - you'll miss errors)

---

### Prompt 6.7: Prepare Defense Presentation

**USER INPUT REQUIRED:**
- Defense format (in-person, virtual, hybrid)
- Presentation time limit (typically 20-30 minutes)
- Committee members (names and areas of expertise)
- Complete dissertation (to extract key content)
- Department/university defense norms (ask advisor)

**INSTRUCTIONS:**

Your defense presentation is **NOT a summary of your entire dissertation**. It's a **strategic highlight of your contributions and findings**.

**Key Principle:** The committee has (theoretically) read your dissertation. The presentation is to:
1. Highlight your main contributions
2. Show your mastery of the material
3. Set up discussion/Q&A

---

#### PRESENTATION STRUCTURE (for 25-30 minute talk)

**Slide Count:** 15-20 slides (rough guide: 1-2 minutes per slide)

**Timing Breakdown:**

| Section | Time | Slides | Purpose |
|---------|------|--------|---------|
| **1. Introduction** | 2-3 min | 2-3 | Hook, context, your name/title |
| **2. Motivation/Problem** | 3-4 min | 2-3 | Why this matters, what's the gap |
| **3. Research Questions** | 1-2 min | 1 | Clear RQs (brief versions) |
| **4. Theoretical Framework** | 2-3 min | 1-2 | Key theory (if applicable) |
| **5. Methodology** | 3-4 min | 2-3 | How you studied this |
| **6. Results** | 10-12 min | 6-8 | **HEART OF PRESENTATION** |
| **7. Discussion/Implications** | 3-4 min | 2-3 | What it means, who benefits |
| **8. Conclusion** | 1-2 min | 1-2 | Contributions, future work |
| **9. Acknowledgments** | 30 sec | 1 | Thank advisor, committee, funders |
| **Total** | **25-30 min** | **18-25** | |

---

#### SLIDE-BY-SLIDE TEMPLATE

**SLIDE 1: TITLE SLIDE**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Centered]

[DISSERTATION TITLE]
[Not all caps - Title Case for slides]

[Your Name]
Advisor: [Advisor Name]

PhD Dissertation Defense
[Department], [University]
[Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Good afternoon. My name is [Name], and today I'll be presenting my dissertation titled '[Title]', completed under the supervision of Dr. [Advisor Name]."

**Time:** 30 seconds

---

**SLIDE 2: MOTIVATION (Part 1 - The Big Picture)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS WORK MATTERS

[One compelling image or statistic]

Example:
• "AI systems make 1 billion+ decisions daily"
• [Image: AI in healthcare, finance, law enforcement]

Problem: These systems are often BLACK BOXES
→ Lack of transparency
→ Inability to trust or debug

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Artificial intelligence systems are increasingly used in high-stakes domains like healthcare, finance, and law enforcement. However, these systems are often black boxes - we can't understand why they make the decisions they do. This lack of transparency creates serious problems for trust, accountability, and debugging."

**Time:** 1 minute

---

**SLIDE 3: MOTIVATION (Part 2 - The Specific Problem)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE PROBLEM: Current XAI Methods Are Too Slow

[Bar chart comparing methods]

Method          | Latency
----------------|----------
Grad-CAM        | 18 ms     ✓ Fast
LIME            | 890 ms    ✗ Slow
SHAP            | 2,300 ms  ✗ Very Slow

❌ Existing methods: either fast but unfaithful, or faithful but slow
❌ No method achieves real-time + high-quality explanations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Existing explainability methods face a critical trade-off. Fast methods like Grad-CAM take only 18 milliseconds but are often unfaithful to the model. High-quality methods like SHAP are faithful but take over 2 seconds - far too slow for real-time applications. No method achieves both real-time performance and high-quality explanations."

**Time:** 1-1.5 minutes

---

**SLIDE 4: RESEARCH QUESTIONS**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH QUESTIONS

RQ1: Can we achieve <50ms latency while maintaining
     >0.7 faithfulness (insertion AUC)?

RQ2: Can we integrate explainability into the model
     architecture with <1% accuracy degradation?

RQ3: Can we ensure demographic fairness with <10%
     variance across groups?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "This dissertation addresses three research questions. First, can we achieve real-time explanations - under 50 milliseconds - while maintaining high faithfulness? Second, can we integrate explainability directly into the model architecture without sacrificing accuracy? And third, can we ensure explanations are fair across demographic groups?"

**Time:** 1 minute

---

**SLIDE 5: THEORETICAL CONTRIBUTION**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY THEORETICAL CONTRIBUTION

Novel SHAP Formulation for Hypersphere Embeddings

Standard SHAP:     φᵢ = Σ [v(S ∪ {i}) - v(S)]
                        (for Euclidean spaces)

Our Formulation:   φᵢ = Σ [dₐ(S ∪ {i}) - dₐ(S)]
                        (for hypersphere spaces)

✓ Preserves all 4 Shapley axioms
✓ Reduces complexity: O(2^M) → O(M log M)

[Simple diagram showing Euclidean vs. hypersphere geometry]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Our key theoretical contribution is a novel SHAP formulation for hypersphere embeddings, which are used in facial recognition systems. Standard SHAP assumes Euclidean geometry, but facial embeddings lie on a hypersphere. Our formulation adapts SHAP to this geometry while preserving all Shapley axioms and reducing computational complexity from exponential to logarithmic."

**Time:** 1.5 minutes

---

**SLIDE 6: METHODOLOGY OVERVIEW**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

METHODOLOGY OVERVIEW

Approach: Three-stage pipeline

Stage 1: E-ViT Training
→ Vision Transformer with explanation capability
→ Trained on LFW dataset (13K images)

Stage 2: Fast Explainer Training
→ Neural network to approximate SHAP
→ Trained with hierarchical SHAP labels

Stage 3: Joint Fine-Tuning
→ End-to-end optimization
→ Accuracy + explanation quality

[Flowchart: Data → E-ViT → Fast Explainer → Explanations]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Our methodology consists of three stages. First, we train an Explainable Vision Transformer, or E-ViT, on the Labeled Faces in the Wild dataset. Second, we train a fast explainer network to approximate SHAP values using our hierarchical framework. Third, we jointly fine-tune both components end-to-end to optimize for both accuracy and explanation quality."

**Time:** 1.5 minutes

---

**SLIDE 7-14: RESULTS** (**MOST IMPORTANT SLIDES**)

**SLIDE 7: RQ1 Results (Latency)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RQ1: LATENCY RESULTS ✓

[Bar chart: Latency comparison]

Method          | Latency  | Target: <50ms
----------------|----------|--------------
Grad-CAM        | 18 ms    | ✓
RISE            | 1,200 ms | ✗
LIME            | 890 ms   | ✗
Vanilla SHAP    | 2,300 ms | ✗
FastSHAP (Ours) | 42 ms    | ✓ ACHIEVED

✓ 55× faster than vanilla SHAP
✓ Within real-time requirement

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "For Research Question 1, we achieved 42 milliseconds latency - well within our 50 millisecond target and 55 times faster than vanilla SHAP. This makes our method suitable for real-time applications."

**Time:** 1 minute

---

**SLIDE 8: RQ1 Results (Faithfulness)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RQ1: FAITHFULNESS RESULTS ✓

[Line plot: Insertion AUC curves]

Method          | Insertion AUC | Target: >0.7
----------------|---------------|-------------
Grad-CAM        | 0.52          | ✗
RISE            | 0.68          | ✗ (close)
Vanilla SHAP    | 0.78          | ✓
FastSHAP (Ours) | 0.73          | ✓ ACHIEVED

✓ Maintains high faithfulness (0.73 > 0.7)
✓ Comparable to vanilla SHAP (0.73 vs. 0.78)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Critically, we also maintain high faithfulness. Our insertion AUC is 0.73, exceeding our 0.7 target and comparable to vanilla SHAP at 0.78. This shows we didn't sacrifice explanation quality for speed."

**Time:** 1 minute

---

**SLIDE 9: RQ2 Results (Accuracy)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RQ2: ACCURACY RESULTS ✓

[Table: Accuracy on LFW]

Model               | Accuracy | Change
--------------------|----------|--------
Baseline ViT        | 98.7%    | -
E-ViT (Ours)        | 99.2%    | +0.5%

✓ No accuracy degradation (target: <1% loss)
✓ Actually IMPROVED accuracy (+0.5%)
✓ Explainability came "for free"

[Optional: Show example image with explanation overlay]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "For Research Question 2, we found that integrating explainability into the architecture did not degrade accuracy. In fact, our E-ViT achieved 99.2% accuracy on LFW, a 0.5% improvement over the baseline. This suggests that learning to explain actually regularizes the model and improves performance."

**Time:** 1 minute

---

**SLIDE 10: RQ3 Results (Fairness - Before Calibration)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RQ3: FAIRNESS CHALLENGE

[Bar chart: Explanation variance by demographic]

Before Calibration:

Group           | Explanation Variance
----------------|---------------------
White           | 12.3
Black           | 18.7
Asian           | 14.1
Latino          | 19.2
Variance Ratio  | 18.3% (White vs. Latino)

❌ Exceeds 10% target
❌ Explanations are demographically biased

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "For Research Question 3, we initially observed demographic bias in explanations. The variance ratio between demographic groups was 18.3%, well above our 10% target. This meant explanations were not equally faithful across groups."

**Time:** 1 minute

---

**SLIDE 11: RQ3 Results (Fairness - After Calibration)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RQ3: FAIRNESS RESULTS ✓

[Bar chart: After calibration]

After Calibration:

Group           | Explanation Variance
----------------|---------------------
White           | 13.1
Black           | 14.2
Asian           | 13.8
Latino          | 14.0
Variance Ratio  | 7.2% ✓ (White vs. Black)

✓ Reduced from 18.3% to 7.2%
✓ Below 10% target
✓ Maintains faithfulness (rank correlation: 0.96)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Our demographic calibration method reduced the variance ratio from 18.3% to 7.2%, well below our 10% target. Critically, this was achieved while maintaining faithfulness, with a rank correlation of 0.96 with uncalibrated explanations. This shows we can ensure fairness without sacrificing explanation quality."

**Time:** 1 minute

---

**SLIDE 12: Key Result - Visual Example**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXAMPLE: REAL-TIME EXPLANATION

[Side-by-side images]

Input Image          FastSHAP Explanation (42ms)
[Face photo]      →  [Face with heatmap overlay]

Key attributes highlighted:
• Eyes (25% contribution)
• Nose (18% contribution)
• Mouth (15% contribution)

✓ Real-time (<50ms)
✓ Interpretable (highlights key features)
✓ Faithful (insertion AUC: 0.73)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Here's a concrete example. Given this input image, FastSHAP generates this explanation in 42 milliseconds, highlighting the eyes, nose, and mouth as key features. This is fast enough for real-time applications while being both interpretable and faithful to the model."

**Time:** 1-1.5 minutes

---

**SLIDE 13: Ablation Study**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ABLATION STUDY: What Matters?

[Table: Component contribution]

Component                    | Insertion AUC | Latency
-----------------------------|---------------|----------
Full FastSHAP                | 0.73          | 42 ms
- Hierarchical approximation | 0.71 (-0.02)  | 65 ms (+23ms)
- Attention-guided sampling  | 0.68 (-0.05)  | 48 ms (+6ms)
- GPU acceleration           | 0.73 (same)   | 125 ms (+83ms)

Key Takeaways:
• Hierarchical approximation: Crucial for speed
• Attention sampling: Crucial for faithfulness
• GPU acceleration: Essential for real-time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Our ablation study shows that all three components are essential. Removing hierarchical approximation increases latency by 23 milliseconds. Removing attention sampling decreases faithfulness by 0.05. And removing GPU acceleration makes the method 3 times slower. Each component plays a critical role."

**Time:** 1-1.5 minutes

---

**SLIDE 14: Summary of Results**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY: ALL RESEARCH QUESTIONS ANSWERED ✓

Research Question              | Target    | Achieved  | ✓/✗
-------------------------------|-----------|-----------|----
RQ1: Latency                   | <50ms     | 42ms      | ✓
RQ1: Faithfulness              | >0.7 AUC  | 0.73 AUC  | ✓
RQ2: Accuracy degradation      | <1%       | +0.5%     | ✓
RQ3: Demographic fairness      | <10% var  | 7.2% var  | ✓

✓ All targets met or exceeded
✓ First method to achieve real-time + faithful + fair explanations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "To summarize the results: all three research questions were answered affirmatively. We achieved 42 millisecond latency, 0.73 insertion AUC, no accuracy degradation, and 7.2% demographic variance. To our knowledge, this is the first method to achieve real-time, faithful, and fair explanations simultaneously."

**Time:** 1 minute

---

**SLIDE 15: DISCUSSION - Theoretical Implications**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THEORETICAL IMPLICATIONS

1. SHAP can be adapted to non-Euclidean spaces
   → Opens door for SHAP on graphs, manifolds, etc.

2. Explainability and accuracy are not mutually exclusive
   → E-ViT achieved BOTH (+0.5% accuracy)
   → Explanation as regularization

3. Fairness requires explicit calibration
   → Uncalibrated methods exhibit demographic bias
   → Calibration is necessary, not optional

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "This work has three main theoretical implications. First, SHAP can be successfully adapted to non-Euclidean spaces like hyperspheres, opening the door for SHAP on graphs and manifolds. Second, explainability and accuracy are not mutually exclusive - our E-ViT achieved both. And third, fairness requires explicit calibration - it doesn't emerge automatically from faithful explanations."

**Time:** 1.5 minutes

---

**SLIDE 16: DISCUSSION - Practical Implications**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRACTICAL IMPLICATIONS

Who Benefits:
• Practitioners: Real-time explanations for production systems
• Regulators: Auditable AI (EU AI Act compliance)
• End users: Transparent decisions in high-stakes domains

Applications:
• Healthcare: Explain diagnostic predictions
• Finance: Explain loan decisions
• Law enforcement: Explain facial recognition matches

[Image showing example applications]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "Practically, this work benefits three groups. Practitioners can now deploy real-time explanations in production systems. Regulators can audit AI systems for compliance with regulations like the EU AI Act. And end users receive transparent explanations for high-stakes decisions in healthcare, finance, and law enforcement."

**Time:** 1 minute

---

**SLIDE 17: LIMITATIONS**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LIMITATIONS

1. Generalization
   → Tested only on facial recognition
   → May not transfer to other vision tasks

2. Approximation Error
   → 0.73 AUC vs. 0.78 for vanilla SHAP
   → 0.05 trade-off for 55× speedup

3. Calibration Overhead
   → Requires demographic labels for fairness
   → May not be available in all domains

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "This work has three main limitations. First, we tested only on facial recognition - generalization to other vision tasks remains to be demonstrated. Second, there's a small approximation error compared to vanilla SHAP - a 0.05 AUC trade-off for 55 times speedup. And third, fairness calibration requires demographic labels, which may not be available in all domains."

**Time:** 1 minute

**⚠️ IMPORTANT:** Be honest about limitations. Committee WILL ask about them. Better to bring them up yourself.

---

**SLIDE 18: FUTURE WORK**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FUTURE WORK

Short-term (1-2 years):
• Extend to other vision tasks (object detection, segmentation)
• Improve approximation error (target: 0.75+ AUC)
• Test on larger datasets (VGGFace2, IJB-C)

Long-term (5-10 years):
• SHAP for other non-Euclidean spaces (graphs, time series)
• Explainability for multimodal models (vision + language)
• Theoretical bounds on approximation error

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "For future work, short-term extensions include applying this to other vision tasks, improving approximation error, and testing on larger datasets. Long-term directions include SHAP for other non-Euclidean spaces like graphs and time series, explainability for multimodal models, and deriving theoretical bounds on approximation error."

**Time:** 1 minute

---

**SLIDE 19: CONCLUSION**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONCLUSION

Contributions:
1. Novel SHAP formulation for hypersphere embeddings
2. Hierarchical approximation reducing complexity O(2^M) → O(M log M)
3. E-ViT architecture for real-time explainability
4. Demographic calibration for fair explanations

Impact:
✓ First method to achieve real-time + faithful + fair explanations
✓ Enables explainable AI in production systems
✓ Advances toward transparent and accountable AI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "In conclusion, this dissertation makes four main contributions: a novel SHAP formulation for hypersphere embeddings, hierarchical approximation reducing computational complexity, the E-ViT architecture for real-time explainability, and demographic calibration for fair explanations. The impact is threefold: this is the first method to achieve real-time, faithful, and fair explanations; it enables explainable AI in production systems; and it advances us toward transparent and accountable AI."

**Time:** 1 minute

---

**SLIDE 20: ACKNOWLEDGMENTS**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACKNOWLEDGMENTS

• Dr. [Advisor Name] - for guidance and mentorship
• Committee members - for invaluable feedback
• [Funding source] - for financial support
• Fellow graduate students - for intellectual community
• Family and friends - for unwavering support

Thank you!

Questions?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**What to say:**
> "I'd like to thank my advisor, Dr. [Name], for his guidance and mentorship throughout this journey. I also thank my committee members for their invaluable feedback, [Funding source] for financial support, my fellow graduate students for intellectual community, and my family and friends for their unwavering support. Thank you, and I'm happy to take questions."

**Time:** 30 seconds

**[END OF PRESENTATION - Begin Q&A]**

---

#### SLIDE DESIGN PRINCIPLES

**1. MINIMAL TEXT**
- **Rule:** Max 6 bullet points per slide, max 6 words per bullet ("6x6 rule")
- **Why:** You're speaking, not reading slides to committee
- **Example:**
  - ❌ "The results of our experiments demonstrated that the proposed method achieved 42 milliseconds latency"
  - ✅ "FastSHAP: 42 ms latency" (you say the rest)

**2. LARGE FONTS**
- **Minimum:** 20pt for body text, 28pt for headings
- **Why:** Readability in large room or via Zoom
- **Check:** Can you read slide from 10 feet away?

**3. HIGH-QUALITY FIGURES**
- **Resolution:** 300+ DPI for images
- **Clarity:** Simple, clear, not cluttered
- **Labels:** All axes labeled, legends present
- **Colors:** Colorblind-friendly (avoid red/green)

**4. CONSISTENT STYLE**
- **Template:** Use university template or professional template (Beamer, PowerPoint built-ins)
- **Colors:** Max 3-4 colors throughout
- **Fonts:** One font family (e.g., Arial throughout, or Times throughout)

**5. VISUAL HIERARCHY**
- **Headings:** Largest, bold
- **Subheadings:** Medium, bold
- **Body:** Smallest
- **Emphasis:** Use color or bold, not underline

---

#### ANTICIPATED QUESTIONS & PREPARATION

**Common Question Types:**

**1. CLARIFICATION QUESTIONS**
> "Can you explain how you calculated X?"
> "What exactly do you mean by Y?"

**Preparation:**
- Know your methods inside-out
- Have backup slides with technical details
- Be ready to draw on whiteboard/paper

**2. CHALLENGE QUESTIONS**
> "Why didn't you use method Z instead?"
> "Isn't your sample size too small?"

**Preparation:**
- For every design choice, know: why you made it, what alternatives exist, why alternatives were inferior
- Have references ready: "Smith (2020) also used n=250 for similar study"

**3. EXTENSION QUESTIONS**
> "How would this apply to domain X?"
> "What if you relaxed assumption Y?"

**Preparation:**
- Think through extensions (what you put in "Future Work")
- It's OK to say "I haven't studied that, but I speculate..."

**4. PHILOSOPHICAL QUESTIONS**
> "What is the broader impact of this work?"
> "What are the ethical implications?"

**Preparation:**
- Connect to big picture (EU AI Act, algorithmic accountability)
- Be thoughtful, not dismissive

---

#### Q&A STRATEGIES

**Strategy 1: The Pause**
- Don't rush to answer
- Pause 2-3 seconds to think
- It's OK to say "That's a good question, let me think..."

**Strategy 2: Clarify If Needed**
- If question is unclear: "Just to make sure I understand, are you asking about X or Y?"
- Rephrasing shows you're listening

**Strategy 3: Bridge Back to Your Work**
- Answer question, then connect to your contribution
- Example: "That's an interesting point about generalization. In our work, we focused on facial recognition, but the hierarchical framework could potentially extend to [domain]."

**Strategy 4: "I Don't Know" is OK**
- If you truly don't know: admit it
- Then: "But here's how I would approach finding out..." (shows problem-solving)

**Strategy 5: Redirect Hostile Questions**
- If question seems hostile: stay calm, reframe neutrally
- Example: "I hear your concern about sample size. Let me explain the power analysis that justified n=250..."

---

#### PRACTICE REGIMEN

**3-4 Weeks Before:**
- Create slides (allow time for revision)
- Practice alone (record yourself)
- Time yourself (must fit within limit)

**2 Weeks Before:**
- Practice with lab group (friendly audience)
- Get feedback on clarity
- Revise slides based on feedback

**1 Week Before:**
- Mock defense with advisor (or lab)
- Simulate Q&A (have people ask hard questions)
- Finalize slides (no more changes after this)

**2-3 Days Before:**
- Practice 3-5 more times
- Focus on smooth delivery, not memorization
- Practice transitions between slides

**Day Before:**
- One final run-through
- Check technology (laptop, adapters, remote)
- Get good sleep (more important than extra practice)

---

**EXPECTED OUTPUT:**
- Defense presentation (15-20 slides)
- Anticipated questions list (15-20 questions)
- Backup slides (5-10 technical details)
- Talking points for each slide

**SAVE AS:**
- `/06_Finalization/defense/defense_presentation_final.pptx` (or .pdf)
- `/06_Finalization/defense/anticipated_questions.md`
- `/06_Finalization/defense/talking_points.md`

**⏱️ TIME ESTIMATE:**
- Slide creation: 10-15 hours
- Practice: 15-20 hours
- **Total: 25-35 hours**

---

## ✅ FINAL QUALITY CHECKS

**Before submitting to committee:**

- [ ] **Abstract:** Within word limit, accurate, self-contained
- [ ] **References:** All formatted correctly, no orphans, no errors
- [ ] **Front Matter:** All components complete (title page → abbreviations)
- [ ] **Formatting:** Per institutional requirements (margins, fonts, spacing, headings)
- [ ] **Appendices:** Organized, lettered, referenced in text
- [ ] **Proofreading:** 5-pass proofread complete, no typos/grammar errors
- [ ] **Defense Presentation:** 15-20 slides, 25-30 minutes, practiced
- [ ] **Committee Approval:** Advisor has approved final draft before distribution
- [ ] **Distribution:** Sent to committee 6-8 weeks before defense (check university requirements)

---

## 🎓 POST-DEFENSE

**After successful defense:**

1. **Celebrate!** 🎉 (You've earned it)

2. **Incorporate Required Revisions** (1-2 weeks)
   - Committee will provide list of revisions
   - Make changes carefully
   - Document all changes for advisor review

3. **Get Final Advisor Approval**
   - Advisor reviews revised version
   - Signs off on final submission

4. **Submit Final Version to Graduate School**
   - Upload to ProQuest or university repository
   - Pay any submission fees
   - Submit embargo request (if applicable - to delay public release)

5. **Format Check by Graduate School** (1-2 weeks)
   - They will check formatting compliance
   - May request minor corrections
   - Be responsive (quick turnaround expected)

6. **Final Acceptance**
   - You're now officially Dr. [Your Name]!
   - Degree conferred at next graduation ceremony

7. **Celebrate Again!** 🏆

---

## 📁 SAVE YOUR OUTPUTS

**Recommended folder structure:**

```
/Dissertation_Project/
  /06_Finalization/
    - abstract_FINAL.md
    - DISSERTATION_FORMATTED_FINAL.docx (or .pdf)

    /front_matter/
      - 01_title_page.docx
      - 02_copyright_page.docx
      - 03_approval_page.docx
      - 04_dedication.docx
      - 05_acknowledgments.docx
      - 06_abstract.docx
      - 07_table_of_contents.docx
      - 08_list_of_figures.docx
      - 09_list_of_tables.docx
      - 10_list_of_abbreviations.docx
      - FRONT_MATTER_COMPLETE.docx

    /appendices/
      - APPENDIX_A_survey.docx
      - APPENDIX_B_interview_protocol.docx
      - APPENDIX_C_statistical_output.docx
      - APPENDIX_D_code.docx
      - APPENDIX_E_IRB.pdf

    /defense/
      - defense_presentation_final.pptx
      - anticipated_questions.md
      - talking_points.md
      - backup_slides.pptx

    /submitted_versions/
      - DISSERTATION_SUBMITTED_TO_COMMITTEE_2025-11-15.pdf
      - DISSERTATION_FINAL_SUBMITTED_TO_GRAD_SCHOOL_2025-12-20.pdf
```

**⚠️ CRITICAL:**
- Keep multiple backups (cloud + external drive)
- Version control all files (Git recommended)
- Save submitted versions with dates (for your records)

---

## 📊 TIMELINE ESTIMATE

| Task | Time Estimate |
|------|---------------|
| **6.1 Abstract** | 2-4 hours |
| **6.2 References** | 4-6 hours |
| **6.3 Front Matter** | 6-8 hours |
| **6.4 Formatting** | 6-10 hours |
| **6.5 Appendices** | 2-4 hours |
| **6.6 Proofreading** | 20-30 hours (across 1-2 weeks) |
| **6.7 Defense Prep** | 25-35 hours |
| **Total** | **65-97 hours** |

**Calendar Time:** 4-8 weeks (depending on committee feedback turnaround)

---

**CONGRATULATIONS, DOCTOR!** 🏆🎓

You've completed one of the most challenging intellectual endeavors. This workflow has guided you from idea to defense.

**Remember:** The dissertation is not the end - it's the beginning of your career as an independent scholar.

**Now go forth and make your contribution to knowledge!** 🚀
