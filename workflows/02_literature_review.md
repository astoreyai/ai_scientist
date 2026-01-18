# Stage 2: Literature Review
## Detailed Prompt Chain (Based on Systematic Search Methodology)

---

## 🎯 SUBCOMPONENTS

1. Scoping (Inclusion/Exclusion Criteria)
2. Systematic Keyword Search
3. Execute Systematic Search
4. Screen and Select Papers
5. Extract Data and Synthesize
6. Structure Literature Review
7. Write Literature Review Sections
8. Write Gap Analysis and Finalize

---

## 📥 REQUIRED INFORMATION (INPUTS)

- Research questions (from Stage 1)
- Theoretical framework (from Stage 1)
- Scope boundaries (from Stage 1)
- Database access credentials (Scopus, Web of Science, PubMed, etc.)
- Reference management software setup (Zotero, Mendeley, EndNote)

---

## 📤 DELIVERABLES (OUTPUTS)

1. Search protocol document (detailed methodology)
2. Inclusion/exclusion criteria document
3. Search strings for multiple databases
4. PRISMA flow diagram with numbers
5. Annotated bibliography (50-150+ sources)
6. Literature synthesis matrix (spreadsheet)
7. Gap analysis document
8. Theoretical foundation outline
9. Complete literature review chapter (8,000-15,000 words)
10. References in .bib or .ris format

---

## 🤖 AI PROMPT CHAINS

### Prompt 2.1: Define Inclusion & Exclusion Criteria (Scoping)

**USER INPUT REQUIRED:**
- Research questions from Stage 1
- Scope definition from Stage 1

**PROMPT:**
```
My research questions are:
[PASTE RESEARCH QUESTIONS]

My defined scope is:
[PASTE SCOPE DEFINITION]

Help me create rigorous inclusion and exclusion criteria for my literature search:

1. INCLUSION CRITERIA - Define what studies MUST have:
   - Time period (e.g., last 10 years, or all time if seminal)
   - Publication types (peer-reviewed, books, dissertations, gray literature?)
   - Language(s)
   - Geographic scope
   - Population/subject characteristics
   - Study types (empirical, theoretical, reviews?)
   - Relevance thresholds

2. EXCLUSION CRITERIA - Define what to automatically exclude:
   - Specific topics that are too tangential
   - Methodological approaches not relevant
   - Publication types (editorials, news articles?)
   - Quality thresholds

3. SCREENING CRITERIA:
   - Title screening rules
   - Abstract screening rules
   - Full-text screening rules

4. Create a decision tree flowchart in text format showing how to apply these criteria

5. Provide 5 edge case examples with how to classify them

Make criteria:
- Specific and objective (minimize subjective judgment)
- Aligned with research questions
- Defendable in methodology section
- Reproducible by another researcher
```

**EXPECTED OUTPUT:** Detailed inclusion/exclusion criteria document with decision tree

**SAVE AS:** `/02_Literature_Review/inclusion_exclusion_criteria.md`

---

### Prompt 2.2: Develop Search Strategy & Keywords

**USER INPUT REQUIRED:**
- Research questions
- Inclusion/exclusion criteria from 2.1
- List of 5-10 key papers you already know are relevant

**PROMPT:**
```
Research Questions: [PASTE]

Key Known Papers:
1. [Title, Author, Year]
2. [Title, Author, Year]
3. [...]

Help me develop a comprehensive search strategy:

1. KEYWORD DEVELOPMENT:
   - Extract key concepts from my research questions
   - For each concept, provide:
     * Main keywords
     * Synonyms
     * Related terms
     * Variant spellings
     * Acronyms
   - Suggest Boolean operators to combine them (AND, OR, NOT)

2. SEARCH STRING CONSTRUCTION:
   - Create 3-5 different search strings with varying specificity
   - Show how to use:
     * Quotation marks for exact phrases
     * Wildcards (* or ?) for variations
     * Parentheses for grouping
   - Adapt for different database syntax

3. DATABASE SELECTION:
   - Recommend ≥2 databases for my field (e.g., Scopus, Web of Science, PubMed, PsycINFO, ERIC, etc.)
   - Explain unique coverage of each
   - Suggest field-specific databases I might be missing

4. SEARCH VALIDATION:
   - Test if search strings retrieve the known relevant papers I listed
   - If not, suggest modifications
   - Estimate expected number of results (too many? too few?)

5. DOCUMENTATION TEMPLATE:
   - Create a template to record:
     * Database name
     * Date of search
     * Search string used
     * Number of results
     * Notes/observations

Provide search strings I can copy-paste directly into databases.
```

**EXPECTED OUTPUT:** Complete search strategy with ready-to-use search strings for multiple databases

**SAVE AS:** `/02_Literature_Review/search_protocol.md` and `/02_Literature_Review/search_strings.md`

---

### Prompt 2.3: Execute Systematic Search

**USER INPUT REQUIRED:**
- Search strings from Prompt 2.2
- Database access (Scopus, Web of Science, PubMed, etc.)
- Reference manager setup (Zotero, Mendeley, EndNote)

**INSTRUCTIONS (Primarily Manual, AI-Assisted Documentation):**

This step is primarily **manual work** but AI can help with documentation and troubleshooting.

#### Step 1: Execute Searches

For **each database** in your search protocol:

1. Log into the database
2. Navigate to advanced search
3. Copy-paste your search string (adjust syntax if needed)
4. Apply filters (date range, publication type, etc.)
5. Note the number of results
6. Export results in standard format:
   - Scopus: `.ris` or `.bib`
   - Web of Science: `.ciw` or `.txt`
   - PubMed: `.nbib` or `.xml`
   - Google Scholar: Use Publish or Perish or manual export

#### Step 2: Document Each Search

**PROMPT (For Each Database Search):**
```
I just completed a search in [DATABASE NAME] on [DATE].

Search string: [PASTE SEARCH STRING]
Filters applied: [e.g., 2013-2023, peer-reviewed only, English]
Results: [NUMBER] papers

Help me:
1. Create a formatted log entry for my search protocol document
2. Assess if this number of results is reasonable
3. If results seem too high (>1000) or too low (<20), suggest search string adjustments

Format the log entry like this:
---
**Database:** [Name]
**Date:** YYYY-MM-DD
**Search String:** [exact string]
**Filters:** [list]
**Results:** [number]
**Notes:** [observations]
**Export File:** [filename.ris]
---
```

**SAVE AS:** Append to `/02_Literature_Review/search_protocol.md` under "Search Execution Log"

#### Step 3: Import to Reference Manager

1. Open your reference manager (Zotero/Mendeley/EndNote)
2. Create a new collection/folder: "Systematic Review - [Your Topic]"
3. Import all exported files
4. Verify import success (check total count matches sum of searches)

#### Step 4: Deduplicate

**Within your reference manager:**
- Zotero: Select all → Right-click → "Merge Duplicate Items"
- Mendeley: Tools → Check for Duplicates
- EndNote: References → Find Duplicates

Document how many duplicates you removed.

**PROMPT (After Deduplication):**
```
Initial total papers: [NUMBER]
After deduplication: [NUMBER]
Duplicates removed: [NUMBER]

Help me:
1. Create a PRISMA flow diagram entry for this
2. Verify this deduplication rate is typical (usually 10-30%)
3. Suggest if I should manually check for missed duplicates

Format:
---
**Initial search results (all databases):** [n]
**Duplicates removed:** [n]
**Records after deduplication:** [n]
---
```

**SAVE AS:** Append to `/02_Literature_Review/search_protocol.md` under "Deduplication Results"

#### Step 5: Prepare for Screening

1. Export deduplicated library to spreadsheet format (.csv)
2. Create screening spreadsheet with columns:
   - ID
   - Title
   - Authors
   - Year
   - Abstract
   - Title_Screen (Include/Exclude/Uncertain)
   - Abstract_Screen (Include/Exclude/Uncertain)
   - Full_Text_Screen (Include/Exclude/Uncertain)
   - Exclusion_Reason
   - Notes

**PROMPT:**
```
I have [NUMBER] papers after deduplication.

Help me:
1. Create a screening spreadsheet template with proper columns
2. Suggest efficient screening workflow (title → abstract → full-text)
3. Recommend screening tools if available (Rayyan, Covidence, or manual Excel/Sheets)
4. Estimate time needed (title: ~5 sec/paper, abstract: ~30 sec/paper, full-text: ~10 min/paper)
```

**SAVE AS:** `/02_Literature_Review/screening_tracker.xlsx` (or Google Sheets)

#### Step 6: Backup Everything

Create backups of:
- Reference manager library file
- Exported .bib/.ris files
- Screening spreadsheet
- Search protocol document

**VERIFICATION CHECKLIST:**
- [ ] All database searches documented in search protocol
- [ ] All export files saved with clear naming (e.g., `scopus_2025-10-10.ris`)
- [ ] Reference manager library contains all papers
- [ ] Deduplication completed and documented
- [ ] Screening spreadsheet created and ready
- [ ] Backups created in at least 2 locations

**EXPECTED OUTPUT:**
- Complete search protocol with execution log
- Deduplicated reference library
- Screening spreadsheet ready for Prompt 2.4

---

### Prompt 2.4: Screen and Select Papers

**USER INPUT REQUIRED:**
- Inclusion/exclusion criteria from Prompt 2.1
- Deduplicated papers from Prompt 2.3
- Screening spreadsheet from Prompt 2.3

**INSTRUCTIONS:**

This is **manual screening work**, but AI can assist with decision-making for borderline cases.

#### Phase 1: Title Screening

**Manual Work:**
1. Open your screening spreadsheet
2. Read only the title of each paper
3. Apply inclusion/exclusion criteria
4. Mark as:
   - **Include:** Clearly relevant
   - **Exclude:** Clearly irrelevant (note reason)
   - **Uncertain:** Cannot decide from title alone

**PROMPT (For Borderline Cases):**
```
I'm title screening and unsure about this paper:

Title: [PASTE TITLE]
My inclusion criteria: [PASTE KEY CRITERIA]

Should I include this for abstract screening, or exclude now?

Provide:
1. Reasoning for Include or Exclude
2. Which specific criterion it meets or fails
3. Suggestion for handling similar cases
```

**GUIDANCE:**
- When uncertain, err on the side of inclusion (will filter in abstract screening)
- Common exclusion reasons:
  - Wrong topic
  - Wrong population
  - Editorial/opinion piece
  - Non-English (if excluded)
  - Wrong time period

**EXPECTED TIME:** ~5-10 seconds per title

**CHECKPOINT:**
After title screening, you should exclude ~30-50% of papers.

**PROMPT (After Title Screening):**
```
Title screening results:
- Total papers: [NUMBER]
- Included: [NUMBER]
- Excluded: [NUMBER]
- Uncertain: [NUMBER]

Top exclusion reasons:
1. [REASON]: [COUNT]
2. [REASON]: [COUNT]
3. [REASON]: [COUNT]

Help me:
1. Verify these exclusion rates are reasonable
2. Create PRISMA flow diagram entry
3. Decide how to handle "Uncertain" papers (typically: move to abstract screening)

Format PRISMA entry:
---
**Records after title screening:** [n included + n uncertain]
**Records excluded at title screening:** [n], because:
  - [Reason 1]: [n]
  - [Reason 2]: [n]
  - [Reason 3]: [n]
---
```

**SAVE AS:** Update `/02_Literature_Review/screening_tracker.xlsx` and append to `search_protocol.md`

---

#### Phase 2: Abstract Screening

**Manual Work:**
1. For all papers marked "Include" or "Uncertain" from title screening
2. Read the abstract carefully
3. Apply full inclusion/exclusion criteria
4. Mark as:
   - **Include:** Proceed to full-text screening
   - **Exclude:** Does not meet criteria (note specific reason)

**PROMPT (For Borderline Cases):**
```
I'm abstract screening and unsure about this paper:

Title: [PASTE TITLE]
Abstract: [PASTE ABSTRACT]

My inclusion criteria:
[PASTE CRITERIA]

Should I include this for full-text screening?

Provide:
1. Detailed reasoning (which criteria it meets/fails)
2. If it's a borderline case, suggest what to look for in full-text
3. Classification: Include or Exclude
```

**GUIDANCE:**
- Read abstract completely before deciding
- Apply all inclusion/exclusion criteria
- Common exclusion reasons at abstract level:
  - Wrong methodology
  - Wrong outcome variables
  - Insufficient detail (indicates low quality)
  - Not empirical (if empirical required)
  - Wrong intervention/exposure

**EXPECTED TIME:** ~30-60 seconds per abstract

**CHECKPOINT:**
After abstract screening, you should exclude another ~40-60% of remaining papers.

**PROMPT (After Abstract Screening):**
```
Abstract screening results:
- Papers from title screening: [NUMBER]
- Included for full-text: [NUMBER]
- Excluded at abstract: [NUMBER]

Top exclusion reasons:
1. [REASON]: [COUNT]
2. [REASON]: [COUNT]
3. [REASON]: [COUNT]

Help me:
1. Verify these exclusion rates are reasonable
2. Create PRISMA flow diagram entry
3. Estimate full-text screening workload ([NUMBER] papers × ~10 min = [X] hours)

Format PRISMA entry:
---
**Records after abstract screening:** [n]
**Records excluded at abstract screening:** [n], because:
  - [Reason 1]: [n]
  - [Reason 2]: [n]
  - [Reason 3]: [n]
---
```

**SAVE AS:** Update `/02_Literature_Review/screening_tracker.xlsx` and append to `search_protocol.md`

---

#### Phase 3: Full-Text Screening

**Manual Work:**
1. Retrieve full-text PDFs for all included papers
   - Use university library access
   - Try Google Scholar for open access
   - Use interlibrary loan for hard-to-get papers
   - Contact authors if necessary (ResearchGate, email)
2. Read each paper (or at minimum: intro, methods, results, discussion)
3. Apply inclusion/exclusion criteria rigorously
4. Mark as:
   - **Include:** Final set for data extraction
   - **Exclude:** Does not meet criteria (note detailed reason)

**PROMPT (For PDF Retrieval Issues):**
```
I cannot access the full-text for this paper:

Title: [TITLE]
Authors: [AUTHORS]
Journal: [JOURNAL], Year: [YEAR], DOI: [DOI]

Help me:
1. Suggest alternative access methods
2. Decide if I should exclude it (due to inaccessibility) or keep trying
3. Draft author contact email if needed
```

**PROMPT (For Borderline Full-Text Papers):**
```
I've read the full-text of this paper and am unsure if it meets my criteria:

Title: [TITLE]
Key details: [BRIEFLY SUMMARIZE METHOD, SAMPLE, FINDINGS]

My inclusion criteria:
[PASTE CRITERIA]

Specific concern: [e.g., "Sample size is only n=10, my criteria says n≥20"]

Should I include or exclude?

Provide:
1. Detailed reasoning
2. Whether to treat this as an exception or strict exclusion
3. How to document this decision
```

**GUIDANCE:**
- Full-text screening is the most rigorous stage
- Common exclusion reasons at full-text level:
  - Insufficient methodological detail
  - Sample does not match inclusion criteria
  - Data quality concerns
  - Duplicate publication (same data as another paper)
  - Full-text reveals abstract was misleading
  - Cannot extract required data

**EXPECTED TIME:** ~10-15 minutes per paper (varies by paper length and complexity)

**CHECKPOINT:**
After full-text screening, you should exclude another ~20-40% of remaining papers.

**PROMPT (After Full-Text Screening):**
```
Full-text screening results:
- Papers retrieved for full-text: [NUMBER]
- Papers included in final set: [NUMBER]
- Papers excluded at full-text: [NUMBER]
- Papers inaccessible: [NUMBER] (document separately)

Top exclusion reasons:
1. [REASON]: [COUNT]
2. [REASON]: [COUNT]
3. [REASON]: [COUNT]

Help me:
1. Verify these exclusion rates are reasonable
2. Create complete PRISMA flow diagram entry
3. Assess if final number ([NUMBER] papers) is sufficient for my review

Format PRISMA entry:
---
**Full-text articles assessed for eligibility:** [n]
**Full-text articles excluded:** [n], because:
  - [Reason 1]: [n]
  - [Reason 2]: [n]
  - [Reason 3]: [n]
**Articles included in synthesis:** [n]
---
```

**SAVE AS:** Update `/02_Literature_Review/screening_tracker.xlsx` and append to `search_protocol.md`

---

#### Phase 4: Citation Network Search (Backward and Forward)

**Now that you have a final set of included papers, expand via citation searching:**

**Backward Citation Search (References):**
1. For each included paper, review its reference list
2. Identify papers that appear highly relevant but were missed in database search
3. Screen these papers using same criteria (title → abstract → full-text)

**Forward Citation Search (Citations to the paper):**
1. Use Google Scholar or Scopus "Cited by" feature
2. Identify papers that cited your included papers
3. Screen these papers using same criteria

**PROMPT:**
```
I have [NUMBER] included papers after full-text screening.

Help me plan citation network search:

1. Should I do backward/forward search on ALL papers, or just key papers?
2. How to identify "key papers" (e.g., highly cited, seminal, most relevant)?
3. Estimate time needed for citation search
4. Create documentation template for citation search results

My final paper count: [NUMBER]
Estimated citations per paper: [estimate, e.g., 50 backward, 20 forward]
```

**Manual Work:**
1. For each key paper, export its references (backward) and citing papers (forward)
2. Deduplicate against your existing library
3. Screen new papers using same process (title → abstract → full-text)
4. Document how many papers were added via citation search

**PROMPT (After Citation Search):**
```
Citation search results:
- Backward search added: [NUMBER] papers
- Forward search added: [NUMBER] papers
- Total papers after citation search: [NUMBER]

Help me:
1. Create PRISMA flow diagram entry for citation search
2. Verify completeness (did I miss obvious sources?)
3. Decide if citation search was saturated (i.e., no new highly relevant papers found)

Format PRISMA entry:
---
**Additional records identified through citation searching:** [n]
**Records screened:** [n]
**Records excluded:** [n]
**Full-text articles assessed:** [n]
**Articles added to synthesis:** [n]
---
**TOTAL ARTICLES IN FINAL REVIEW:** [n]
---
```

**SAVE AS:** Update `/02_Literature_Review/screening_tracker.xlsx` and append to `search_protocol.md`

---

#### Phase 5: Finalize PRISMA Diagram

**PROMPT:**
```
Help me create a complete PRISMA flow diagram with all my numbers:

**Identification:**
- Scopus: [n]
- Web of Science: [n]
- PubMed: [n]
- Other databases: [n]
- **Total records identified:** [n]

**Screening:**
- **Duplicates removed:** [n]
- **Records after deduplication:** [n]
- **Records excluded at title screening:** [n]
- **Records after title screening:** [n]
- **Records excluded at abstract screening:** [n]
- **Records after abstract screening:** [n]

**Eligibility:**
- **Full-text articles assessed:** [n]
- **Full-text articles excluded:** [n], because:
  - [Reason 1]: [n]
  - [Reason 2]: [n]
  - [Reason 3]: [n]

**Citation Searching:**
- **Additional records from citation search:** [n]
- **Records screened:** [n]
- **Records added after citation search:** [n]

**Included:**
- **Total articles included in synthesis:** [n]

Generate:
1. Text-based PRISMA diagram (boxes and arrows)
2. Verification that all numbers add up correctly
3. LaTeX/TikZ code for PRISMA diagram (optional)
4. Markdown table format for PRISMA
```

**EXPECTED OUTPUT:**
- Complete PRISMA flow diagram with all numbers
- Verification that search process was systematic and reproducible

**SAVE AS:** `/02_Literature_Review/PRISMA_diagram.md` (and optionally `.tex` or `.png`)

---

**VERIFICATION CHECKLIST FOR PROMPT 2.4:**
- [ ] Title screening completed and documented
- [ ] Abstract screening completed and documented
- [ ] Full-text screening completed and documented
- [ ] All exclusion reasons documented
- [ ] Citation search completed (backward and forward)
- [ ] PRISMA diagram complete with accurate numbers
- [ ] Final included papers list created
- [ ] Screening decisions are reproducible (criteria applied consistently)

**EXPECTED OUTPUT:**
- Final set of included papers (typically 30-150 papers, field-dependent)
- Complete PRISMA flow diagram
- Detailed documentation of screening process

---

### Prompt 2.5: Extract Data and Synthesize

**USER INPUT REQUIRED:**
- Final set of included papers from Prompt 2.4
- Research questions from Stage 1
- Synthesis matrix template (see `tools/literature_review/synthesis_matrix_template.csv`)

**INSTRUCTIONS:**

This prompt guides you through **data extraction** (pulling key info from each paper) and **synthesis** (finding patterns across papers).

---

#### Phase 1: Set Up Data Extraction

**PROMPT:**
```
I have [NUMBER] papers in my final literature review set.

My research questions are:
[PASTE RESEARCH QUESTIONS]

Help me design a data extraction strategy:

1. BIBLIOGRAPHIC DATA (extract for all papers):
   - Author(s)
   - Year
   - Title
   - Journal/Source
   - DOI
   - Citation count (as of [DATE])

2. METHODOLOGICAL DATA (customize for my field):
   - Study design (e.g., experimental, survey, qualitative, review)
   - Sample size
   - Population/participants
   - Data collection method
   - Analysis approach
   - Key variables measured

3. FINDINGS DATA (aligned with my RQs):
   - Main findings relevant to RQ1
   - Main findings relevant to RQ2
   - Main findings relevant to RQ3
   - Effect sizes (if applicable)
   - Statistical significance
   - Limitations noted by authors

4. QUALITY ASSESSMENT:
   - Methodological rigor (High/Medium/Low)
   - Sample quality
   - Reporting quality
   - Relevance to my research (High/Medium/Low)

5. ADDITIONAL FIELDS:
   - Theoretical framework used
   - Key concepts/constructs
   - Geographic context
   - Time period of study
   - Gaps identified by authors
   - Future work suggested

Create a spreadsheet template with these columns that I can use for data extraction.
```

**EXPECTED OUTPUT:** Customized data extraction spreadsheet template

**SAVE AS:** `/02_Literature_Review/data_extraction_template.xlsx` (or use `synthesis_matrix_template.csv` from tools/)

---

#### Phase 2: Extract Data from Each Paper

**Manual Work (per paper):**
1. Open the paper PDF
2. Open your data extraction spreadsheet
3. Read the paper carefully (intro, methods, results, discussion)
4. Fill in all columns in the spreadsheet for this paper
5. Add notes on anything particularly interesting or confusing

**PROMPT (For Complex or Confusing Papers):**
```
I'm extracting data from this paper and need help understanding it:

Citation: [AUTHOR YEAR]
Title: [TITLE]

Specific questions:
1. [e.g., "What does 'hierarchical moderation' mean in their methodology?"]
2. [e.g., "They report β=0.34, p<.05 - is this a strong or weak effect?"]
3. [e.g., "How does their theoretical framework relate to mine?"]

Help me:
1. Clarify confusing concepts
2. Interpret their findings
3. Decide what to record in my data extraction spreadsheet
```

**EXPECTED TIME:** ~15-30 minutes per paper (varies by paper complexity)

**TIPS:**
- Extract data consistently across all papers
- If a paper doesn't report something (e.g., effect size), note "Not reported"
- Use direct quotes for key definitions or findings
- Note page numbers for important information (for later citation)

**CHECKPOINT:**
After extracting data from ~25% of papers, review your spreadsheet. Are you being consistent? Do you need to add/remove columns?

**PROMPT (Mid-Extraction Check):**
```
I've extracted data from [NUMBER] out of [TOTAL] papers so far.

I'm noticing:
1. [e.g., "Many papers don't report effect sizes"]
2. [e.g., "Lots of variation in how they define 'X'"]
3. [e.g., "Some papers are reviews, not empirical - should I extract differently?"]

Help me:
1. Decide if I need to modify my extraction template
2. Ensure consistency across papers
3. Address emerging issues
```

**SAVE AS:** `/02_Literature_Review/synthesis_matrix.xlsx` (updated continuously)

---

#### Phase 3: Synthesize by Theme

**Once all data is extracted, begin synthesis:**

**PROMPT:**
```
I've completed data extraction for all [NUMBER] papers.

My synthesis matrix is here: [ATTACH OR DESCRIBE]

Help me synthesize the literature by theme:

1. IDENTIFY THEMES:
   - Group papers by research focus
   - Common themes might be:
     * Theoretical approaches
     * Methodological approaches
     * Populations studied
     * Contexts studied
     * Types of interventions/variables
   - Suggest 4-6 major themes for organizing my review

2. FOR EACH THEME:
   - Which papers fall under this theme? (list by Author Year)
   - What are the common findings?
   - What are the disagreements or contradictions?
   - What patterns emerge?
   - How has this area evolved over time?

3. CREATE SYNTHESIS TABLES:
   - Design comparison tables showing key papers side-by-side
   - Organize by theme
   - Highlight agreements, disagreements, gaps

4. CROSS-CUTTING PATTERNS:
   - What patterns appear across all themes?
   - Are there methodological trends (e.g., shift from surveys to experiments)?
   - Are there geographic or temporal patterns?
   - What theoretical frameworks dominate?

Generate:
1. List of themes with paper assignments
2. For each theme: summary of key findings + contradictions
3. Synthesis table templates
```

**EXPECTED OUTPUT:**
- 4-6 thematic groupings
- Summary of findings for each theme
- Comparison tables

**SAVE AS:** `/02_Literature_Review/synthesis_by_theme.md`

---

#### Phase 4: Identify Gaps

**This is CRITICAL for justifying your research.**

**PROMPT:**
```
Based on my synthesis, help me identify research gaps:

1. METHODOLOGICAL GAPS:
   - Are there methods not yet applied?
   - Are there limitations in existing methods?
   - Are there populations not yet studied?
   - Are there contexts missing?

2. CONTEXTUAL GAPS:
   - Geographic gaps (e.g., most studies in Western countries)
   - Temporal gaps (e.g., pre-2020 vs. post-2020)
   - Population gaps (e.g., mostly students, not professionals)
   - Setting gaps (e.g., lab studies, not field studies)

3. THEORETICAL GAPS:
   - Are there unexplained phenomena?
   - Are there contradictions in findings that need theoretical resolution?
   - Are there theoretical frameworks not yet applied?
   - Are there integration opportunities (e.g., combining two theories)?

4. EMPIRICAL GAPS:
   - Research questions not yet answered
   - Variables not yet studied
   - Relationships not yet tested
   - Mechanisms not yet explored

5. INTEGRATION GAPS:
   - Are there fragmented research streams that need integration?
   - Are there interdisciplinary connections not made?

For each gap:
1. Describe the gap clearly
2. Explain why it matters (significance)
3. Explain how my research addresses this gap

Generate:
1. Comprehensive list of gaps (organized by type)
2. For each gap: description + significance + how I address it
3. Positioning diagram (2x2 matrix or Venn diagram showing where my research fits)
```

**EXPECTED OUTPUT:**
- Detailed gap analysis (3-5 major gaps)
- Justification for each gap
- Positioning of your research relative to existing literature

**SAVE AS:** `/02_Literature_Review/gap_analysis.md`

---

#### Phase 5: Create Comparison Tables

**PROMPT:**
```
Create comparison tables for my literature review.

For Theme 1: [THEME NAME]
Papers: [List Author Year citations]

Create a table with columns:
| Author (Year) | Sample | Method | Key Findings | Limitations |

For Theme 2: [THEME NAME]
Papers: [List Author Year citations]

Create a table with columns:
| Author (Year) | Theoretical Framework | Population | Main Result | Effect Size |

Customize tables for each theme to highlight the most relevant comparisons.

Also create:
1. Methodology comparison table (across all papers)
2. Findings summary table (organized by RQ)
3. Quality assessment table
```

**EXPECTED OUTPUT:**
- 3-6 comparison tables (one per theme, plus cross-cutting tables)
- Tables are clear, concise, and highlight key information

**SAVE AS:** `/02_Literature_Review/comparison_tables.md`

---

**VERIFICATION CHECKLIST FOR PROMPT 2.5:**
- [ ] Data extraction completed for all papers
- [ ] Synthesis matrix filled completely
- [ ] Papers grouped by theme (4-6 themes)
- [ ] Key findings summarized for each theme
- [ ] Contradictions and agreements noted
- [ ] Research gaps identified (3-5 major gaps)
- [ ] Gap analysis justifies your research
- [ ] Comparison tables created

**EXPECTED OUTPUT:**
- Complete synthesis matrix (spreadsheet)
- Synthesis by theme document
- Gap analysis document
- Comparison tables

---

### Prompt 2.6: Structure Literature Review

**USER INPUT REQUIRED:**
- Synthesis by theme from Prompt 2.5
- Gap analysis from Prompt 2.5
- Research questions from Stage 1

**GOAL:** Organize your synthesized literature into a clear chapter structure.

---

**PROMPT:**
```
I've synthesized my literature into the following themes:

Theme 1: [NAME] - [NUMBER] papers
Theme 2: [NAME] - [NUMBER] papers
Theme 3: [NAME] - [NUMBER] papers
Theme 4: [NAME] - [NUMBER] papers
[etc.]

My research questions are:
[PASTE RQs]

My identified gaps are:
1. [GAP 1]
2. [GAP 2]
3. [GAP 3]

Help me structure my literature review chapter:

1. ORGANIZATIONAL APPROACH:
   - Should I organize by theme, chronologically, methodologically, or theoretically?
   - Provide rationale for recommended approach
   - Show alternative structures if applicable

2. CHAPTER OUTLINE:
   - Section 2.1: Introduction
     * Purpose of literature review
     * Organization preview
     * Search methodology summary

   - Section 2.2: [First Major Section]
     * What to cover
     * Which papers to discuss
     * How to organize subsections

   - Section 2.3: [Second Major Section]
     * What to cover
     * Which papers to discuss
     * How to organize subsections

   - [Additional sections 2.4, 2.5 as needed]

   - Section 2.6: Summary and Research Gaps
     * How to synthesize across sections
     * How to present gaps
     * How to position my research

3. SECTION ALLOCATION:
   - Suggested word count for each section
   - Priority sections (where to spend most time)
   - Balance between breadth and depth

4. PAPER PLACEMENT:
   - Which papers should be discussed in detail? (5-10 key papers)
   - Which papers should be cited together in groups?
   - Which papers are tangential (minimal mention)?

5. WRITING STRATEGY:
   - For each major section (2.2-2.5), provide:
     * Opening paragraph template
     * Survey/Analysis/Connection/Transition structure
     * How to integrate critical analysis (not just summary)
     * How to build toward gaps

Generate:
1. Detailed chapter outline with subsections
2. Word count targets per section
3. Paper placement guide (which papers in which sections)
4. Writing templates for each section type
```

**EXPECTED OUTPUT:**
- Complete chapter outline (Sections 2.1-2.6 with subsections)
- Word count allocation
- Paper placement strategy
- Writing templates

**SAVE AS:** `/02_Literature_Review/lit_review_outline.md`

---

**EXAMPLE STRUCTURE (Adapt for Your Field):**

**Thematic Organization (Most Common):**
```
2.1 Introduction (500-700 words)
2.2 [Theme 1: Theoretical Foundations] (2,000-3,000 words)
    2.2.1 Early theories (1990s-2000s)
    2.2.2 Contemporary frameworks (2010s-present)
    2.2.3 Critical evaluation
2.3 [Theme 2: Methodological Approaches] (2,000-3,000 words)
    2.3.1 Experimental studies
    2.3.2 Survey-based research
    2.3.3 Qualitative approaches
    2.3.4 Methodological critiques
2.4 [Theme 3: Empirical Findings in Context A] (2,500-3,500 words)
    2.4.1 Findings on variable X
    2.4.2 Findings on variable Y
    2.4.3 Contradictions and unresolved questions
2.5 [Theme 4: Empirical Findings in Context B] (2,000-3,000 words)
    2.5.1 Findings on population P
    2.5.2 Findings on setting S
    2.5.3 Emerging trends
2.6 Summary and Research Gaps (1,500-2,000 words)
    2.6.1 Key findings from literature
    2.6.2 Identified gaps
    2.6.3 Positioning of current research

Total: 10,500-15,200 words
```

**Chronological Organization (Less Common, for Historical Fields):**
```
2.1 Introduction
2.2 Foundational Period (1950s-1980s)
2.3 Expansion Period (1990s-2000s)
2.4 Contemporary Period (2010s-present)
2.5 Summary and Research Gaps
```

**Methodological Organization (For Methods-Focused Research):**
```
2.1 Introduction
2.2 Qualitative Studies
2.3 Quantitative Studies
2.4 Mixed Methods Studies
2.5 Summary and Research Gaps
```

---

**WRITING STRATEGY TEMPLATE (For Each Major Section 2.2-2.5):**

```
[SECTION TITLE]

**Opening Paragraph (3-5 sentences):**
- Introduce the theme
- Explain why this area matters for your research
- Preview subsections

**Subsection 2.X.1: [Subtopic A]**
- Survey: What have researchers found? (cite 5-10 papers)
- Analyze: What do these findings mean? Critical evaluation
- Compare: Where do researchers agree? Disagree?
- Connect: How does this relate to your research?

**Subsection 2.X.2: [Subtopic B]**
- [Repeat structure]

**Subsection 2.X.3: Critical Evaluation**
- What are the strengths of this research stream?
- What are the limitations?
- What remains unresolved?

**Closing Paragraph (2-3 sentences):**
- Summarize key takeaways from this section
- Transition to next section
```

---

**CRITICAL ANALYSIS GUIDELINES:**

**Don't just summarize** ("Smith (2020) found X, Jones (2021) found Y, Brown (2022) found Z").

**Instead, synthesize and analyze:**
- "Research consistently shows X (Smith, 2020; Jones, 2021; Brown, 2022). However, these findings are limited to context A, leaving context B unexplored."
- "While early studies suggested X (Smith, 2020), more recent research challenges this view (Jones, 2021; Brown, 2022), suggesting instead that Y."
- "Three theoretical frameworks dominate this area: Framework A (Smith, 2020), Framework B (Jones, 2021), and Framework C (Brown, 2022). However, none adequately explain phenomenon Z, which is central to my research."

---

**CITATION STRATEGY:**

**Group related papers:**
- "Multiple studies have shown X (Author1, Year; Author2, Year; Author3, Year)."

**Highlight key papers:**
- "Smith's (2020) seminal work established..."
- "In a comprehensive review, Jones (2021) demonstrated..."

**Show evolution:**
- "Early research suggested X (Author1, Year), but subsequent studies found Y (Author2, Year; Author3, Year), leading to the current consensus that Z (Author4, Year)."

**Acknowledge disagreement:**
- "While some researchers argue X (Author1, Year; Author2, Year), others contend that Y (Author3, Year; Author4, Year). This disagreement likely stems from differences in [methodology/context/definition]."

---

**VERIFICATION CHECKLIST FOR PROMPT 2.6:**
- [ ] Chapter outline is complete (all sections and subsections)
- [ ] Organization approach is clear and justified
- [ ] Word count targets are reasonable (total 8,000-15,000 words)
- [ ] Paper placement is strategic (key papers highlighted, others grouped)
- [ ] Writing templates are actionable
- [ ] Critical analysis strategy is defined (not just summary)
- [ ] Structure aligns with research questions

**EXPECTED OUTPUT:**
- Detailed literature review outline
- Writing strategy for each section
- Paper placement guide

---

### Prompt 2.7: Write Literature Review Sections

**USER INPUT REQUIRED:**
- Chapter outline from Prompt 2.6
- Synthesis matrix from Prompt 2.5
- All papers (PDFs) from Prompt 2.4

**GOAL:** Write each section of your literature review chapter, one at a time.

---

#### Section 2.1: Introduction

**PROMPT:**
```
Help me write Section 2.1: Introduction to my literature review.

My research questions are:
[PASTE RQs]

My chapter outline is:
[PASTE OUTLINE - sections 2.2, 2.3, 2.4, etc.]

Write Section 2.1 following this structure:

**Paragraph 1: Purpose of Literature Review (2-3 sentences)**
- State what this chapter accomplishes
- Explain how it supports the research

**Paragraph 2: Scope and Search Strategy (3-4 sentences)**
- Summarize search approach (databases, keywords, criteria)
- State number of papers reviewed
- Reference PRISMA diagram or search protocol (if applicable)

**Paragraph 3: Theoretical Foundation (2-3 sentences)**
- Introduce the main theoretical framework(s)
- Explain why this theory is relevant

**Paragraph 4: Organization of Chapter (3-4 sentences)**
- Preview sections 2.2, 2.3, 2.4, etc.
- Explain the logic of organization (thematic, chronological, etc.)
- State how chapter builds toward identifying research gaps

**Target Length:** 500-700 words

**Tone:** Formal, objective, clear

Generate a draft of Section 2.1.
```

**EXPECTED OUTPUT:** Draft of Section 2.1 (500-700 words)

**SAVE AS:** `/02_Literature_Review/section_2.1_introduction.md`

**MANUAL WORK:**
- Review draft
- Edit for clarity and accuracy
- Add citations as needed
- Refine transitions

---

#### Sections 2.2-2.5: Thematic Sections (Repeat for Each)

**PROMPT (Customize for Each Section):**
```
Help me write Section 2.X: [SECTION TITLE]

**Section Details:**
- Theme: [e.g., "Theoretical Frameworks for Explainable AI"]
- Papers to discuss: [List 10-20 key papers by Author Year]
- Subsections:
  - 2.X.1: [Subsection title]
  - 2.X.2: [Subsection title]
  - 2.X.3: [Subsection title]

**Key Points to Cover:**
1. [e.g., "Early SHAP theory (Lundberg & Lee, 2017)"]
2. [e.g., "Extensions to deep learning (Author, Year)"]
3. [e.g., "Criticisms of SHAP (Author, Year)"]
4. [e.g., "Alternative approaches: LIME, Grad-CAM"]

**Structure for Section 2.X:**

**Opening Paragraph (3-5 sentences):**
- Introduce the theme
- Explain why it matters for my research
- Preview subsections

**Subsection 2.X.1: [Subtopic A]**
- Survey existing research (cite 5-10 papers)
- Analyze key findings
- Identify patterns and trends
- Critical evaluation (strengths, limitations)

**Subsection 2.X.2: [Subtopic B]**
- Survey existing research (cite 5-10 papers)
- Compare and contrast findings
- Discuss contradictions or disagreements
- Connect to my research questions

**Subsection 2.X.3: [Subtopic C or Critical Evaluation]**
- Synthesize findings from 2.X.1 and 2.X.2
- Identify what remains unresolved
- Build toward research gaps

**Closing Paragraph (2-3 sentences):**
- Summarize key takeaways
- Transition to next section

**Target Length:** 2,000-3,500 words

**Tone:** Analytical, critical (not just descriptive), formal

**Citation Strategy:**
- Group related papers: "Several studies have shown X (Author1, Year; Author2, Year; Author3, Year)."
- Highlight seminal papers: "Smith's (2020) groundbreaking work..."
- Show evolution: "Early research suggested X (Author, Year), but recent studies find Y (Author, Year)."
- Acknowledge disagreement: "While some argue X (Author, Year), others contend Y (Author, Year)."

Generate a draft of Section 2.X.
```

**EXPECTED OUTPUT:** Draft of Section 2.X (2,000-3,500 words per section)

**SAVE AS:** `/02_Literature_Review/section_2.X_[theme_name].md`

**MANUAL WORK:**
- Review draft for accuracy (check that AI didn't make up citations!)
- Add specific quotes or data from papers
- Refine critical analysis
- Ensure transitions between subsections are smooth
- Verify all citations are correct

**REPEAT FOR ALL THEMATIC SECTIONS (2.2, 2.3, 2.4, 2.5, etc.)**

---

#### Writing Tips for Sections 2.2-2.5

**1. Don't just list papers:**
❌ **Bad:** "Smith (2020) studied X. Jones (2021) studied Y. Brown (2022) studied Z."

✅ **Good:** "Researchers have consistently found that X improves outcomes (Smith, 2020; Jones, 2021; Brown, 2022). However, these studies are limited to population A, and it remains unclear whether X applies to population B."

**2. Show patterns, not just individual studies:**
❌ **Bad:** Describing each paper individually in separate paragraphs

✅ **Good:** Grouping papers by theme, showing agreements/disagreements, identifying trends

**3. Be critical, not just descriptive:**
❌ **Bad:** "Smith (2020) found X using method Y with sample Z."

✅ **Good:** "Smith's (2020) findings are compelling, but the small sample size (n=30) and reliance on self-report measures limit generalizability. Subsequent studies with larger samples (Jones, 2021; Brown, 2022) have partially replicated these findings, but inconsistencies remain."

**4. Connect to your research:**
End each subsection with: "These findings suggest [takeaway], but [gap] remains unexplored. My research addresses this gap by..."

**5. Use transitions:**
- "Building on this foundation, researchers have explored..."
- "In contrast to the quantitative studies reviewed above, qualitative research suggests..."
- "While theoretical work has established X, empirical validation remains limited..."

**6. Use synthesis phrases:**
- "A growing body of evidence suggests..."
- "Research consistently shows..."
- "Scholars disagree on..."
- "While early studies found X, more recent work indicates Y..."
- "A critical limitation across these studies is..."

---

#### Citation Format Guidance

**Single author:**
- "Smith (2020) found that X..."
- "Recent research shows X (Smith, 2020)."

**Two authors:**
- "Smith and Jones (2020) demonstrated..."
- "X has been shown (Smith & Jones, 2020)."

**Three or more authors (APA 7th):**
- "Smith et al. (2020) reported..."
- "X is well-established (Smith et al., 2020)."

**Multiple papers:**
- "Several studies support X (Smith, 2020; Jones, 2021; Brown, 2022)."
- Order by year, or by relevance

**Citing reviews:**
- "For a comprehensive review, see Smith (2020)."
- "As detailed in meta-analyses (Smith, 2020; Jones, 2021)..."

---

**VERIFICATION CHECKLIST FOR EACH SECTION:**
- [ ] Opening paragraph clearly introduces theme
- [ ] All subsections are covered
- [ ] 5-10 papers cited per subsection (minimum)
- [ ] Analysis is critical, not just descriptive
- [ ] Papers are synthesized, not just listed
- [ ] Contradictions/disagreements are discussed
- [ ] Connections to research questions are explicit
- [ ] Closing paragraph summarizes and transitions
- [ ] All citations are accurate (no made-up citations!)
- [ ] Word count target met (2,000-3,500 words per section)

---

#### Common Mistakes to Avoid

**Mistake 1: "Listing" papers**
- Each paper gets its own paragraph
- No synthesis or comparison
- Reads like an annotated bibliography

**Fix:** Group papers by theme, compare findings, identify patterns

**Mistake 2: Over-reliance on quotes**
- Long block quotes from papers
- Minimal paraphrasing

**Fix:** Paraphrase in your own words, use quotes sparingly for key definitions or striking findings

**Mistake 3: No critical analysis**
- Just describes what papers found
- Doesn't evaluate methodology, limitations, or significance

**Fix:** Add evaluation: "This finding is significant because...", "However, this study is limited by...", "These contradictions suggest..."

**Mistake 4: Missing connections to your research**
- Literature review feels disconnected from your RQs
- Doesn't build toward identifying gaps

**Fix:** End each subsection with: "These findings inform my research by...", "However, [gap] remains, which my study addresses..."

**Mistake 5: Inconsistent organization**
- Sections overlap or don't follow a clear logic
- Subsections within a section don't connect

**Fix:** Follow your outline strictly, use transitions, ensure each subsection builds on the previous

---

**EXPECTED OUTPUT FOR PROMPT 2.7:**
- Drafted Section 2.1 (Introduction)
- Drafted Sections 2.2-2.5 (all thematic sections)
- Total word count: ~8,000-12,000 words so far (before Section 2.6)

---

### Prompt 2.8: Write Gap Analysis and Finalize

**USER INPUT REQUIRED:**
- Drafted sections 2.1-2.5 from Prompt 2.7
- Gap analysis document from Prompt 2.5
- Research questions from Stage 1

**GOAL:** Write Section 2.6 (Summary and Research Gaps) and finalize the entire literature review chapter.

---

#### Step 1: Write Section 2.6.1 - Key Findings from Literature

**PROMPT:**
```
Help me write Section 2.6.1: Key Findings from Literature

I've completed sections 2.2-2.5, covering:
- Section 2.2: [THEME 1]
- Section 2.3: [THEME 2]
- Section 2.4: [THEME 3]
- Section 2.5: [THEME 4]

Synthesize the key findings across all sections:

**Structure for Section 2.6.1:**

**Paragraph 1: Overall Synthesis (3-4 sentences)**
- What is the state of knowledge in this area?
- What are the major themes that emerged?

**Finding 1: [Key Finding from across literature] (1 paragraph)**
- Summarize the finding
- Which sections/papers support this? (cite)
- Why is this important?

**Finding 2: [Key Finding from across literature] (1 paragraph)**
- Summarize the finding
- Which sections/papers support this? (cite)
- Why is this important?

**Finding 3: [Key Finding from across literature] (1 paragraph)**
- Summarize the finding
- Which sections/papers support this? (cite)
- Why is this important?

[Continue for 3-5 key findings total]

**Final Paragraph: State of the Field (2-3 sentences)**
- Where does the field currently stand?
- What has been accomplished?
- What remains to be done? (transition to 2.6.2)

**Target Length:** 800-1,200 words

Generate a draft of Section 2.6.1.
```

**EXPECTED OUTPUT:** Draft of Section 2.6.1 (800-1,200 words)

**SAVE AS:** `/02_Literature_Review/section_2.6.1_key_findings.md`

---

#### Step 2: Write Section 2.6.2 - Identified Gaps

**PROMPT:**
```
Help me write Section 2.6.2: Identified Research Gaps

My gap analysis identified these gaps:

Gap 1: [METHODOLOGICAL GAP]
- Description: [e.g., "No studies have applied SHAP to Vision Transformers"]
- Why it matters: [significance]

Gap 2: [THEORETICAL GAP]
- Description: [e.g., "No theory explains X in context Y"]
- Why it matters: [significance]

Gap 3: [EMPIRICAL GAP]
- Description: [e.g., "No studies have examined Z in population P"]
- Why it matters: [significance]

[Add more gaps as needed]

**Structure for Section 2.6.2:**

**Opening Paragraph (2-3 sentences):**
- Transition from 2.6.1 (what we know) to gaps (what we don't know)
- State that several important gaps remain

**For Each Gap: (1 paragraph each)**

**Gap 1: [NAME]**
- Describe the gap clearly and specifically
- Explain why this gap exists (methodological difficulty? lack of attention? recent development?)
- Explain why filling this gap matters (theoretical contribution? practical application? methodological advancement?)
- Cite any authors who have called for this research (if applicable)

**Gap 2: [NAME]**
- [Repeat structure]

**Gap 3: [NAME]**
- [Repeat structure]

[Continue for 3-5 gaps]

**Closing Paragraph (2-3 sentences):**
- Summarize the gaps collectively
- State that your research addresses these gaps
- Transition to Section 2.6.3

**Target Length:** 800-1,200 words

**Tone:** Objective, not defensive ("gaps" not "failures" of prior research)

Generate a draft of Section 2.6.2.
```

**EXPECTED OUTPUT:** Draft of Section 2.6.2 (800-1,200 words)

**SAVE AS:** `/02_Literature_Review/section_2.6.2_gaps.md`

---

#### Step 3: Write Section 2.6.3 - Positioning of Current Research

**PROMPT:**
```
Help me write Section 2.6.3: Positioning of Current Research

My research:
- Title: [YOUR DISSERTATION TITLE]
- Research Questions:
  - RQ1: [PASTE]
  - RQ2: [PASTE]
  - RQ3: [PASTE]

The gaps I identified:
1. [GAP 1]
2. [GAP 2]
3. [GAP 3]

**Structure for Section 2.6.3:**

**Paragraph 1: Overview of Current Research (3-4 sentences)**
- State the purpose of your research
- Briefly describe your approach
- Position it relative to the literature reviewed

**Paragraph 2: How RQ1 Addresses Gap(s) (2-3 sentences)**
- Connect RQ1 to specific gap(s)
- Explain how your approach fills this gap
- State the contribution

**Paragraph 3: How RQ2 Addresses Gap(s) (2-3 sentences)**
- [Repeat structure]

**Paragraph 4: How RQ3 Addresses Gap(s) (2-3 sentences)**
- [Repeat structure]

**Paragraph 5: Differentiation from Existing Work (3-4 sentences)**
- How is your work different from the closest existing research?
- What unique contribution do you make?
- Build on (not just criticize) prior work

**Optional: Positioning Diagram**
- Create a 2x2 matrix or Venn diagram showing where your research fits
- Axes could be: Theoretical vs. Applied, Quantitative vs. Qualitative, etc.
- Show your research in relation to key prior works

**Closing Paragraph (2-3 sentences):**
- Restate the significance of your research
- Transition to Chapter 3 (Methodology or Theory)

**Target Length:** 600-900 words

Generate a draft of Section 2.6.3.
```

**EXPECTED OUTPUT:** Draft of Section 2.6.3 (600-900 words)

**SAVE AS:** `/02_Literature_Review/section_2.6.3_positioning.md`

---

#### Step 4: Integration and Flow Check

**PROMPT:**
```
I've drafted all sections of my literature review (2.1-2.6).

Help me check for integration and flow:

1. TERMINOLOGY CONSISTENCY:
   - Are key terms defined consistently across all sections?
   - Do I use the same terminology throughout? (e.g., not switching between "explainability" and "interpretability" without clarifying)

2. CROSS-CHAPTER REFERENCES:
   - Are there places where I should add cross-references? (e.g., "As discussed in Section 2.3...")
   - Are transitions between sections smooth?

3. NARRATIVE FLOW:
   - Does the chapter tell a coherent story?
   - Does it build logically toward identifying gaps?
   - Does Section 2.6 effectively synthesize and conclude?

4. REDUNDANCY CHECK:
   - Are there repeated ideas that should be consolidated?
   - Are there papers cited multiple times in different sections (is this intentional and necessary)?

5. ALIGNMENT WITH RESEARCH QUESTIONS:
   - Does the literature review clearly connect to my RQs?
   - Will readers understand how this review sets up my research?

Provide:
1. List of terminology inconsistencies to fix
2. Suggested cross-references to add
3. Transition improvements
4. Redundancy to eliminate
5. Overall coherence assessment
```

**MANUAL WORK:**
- Read the entire chapter from start to finish
- Make edits based on AI suggestions
- Ensure smooth flow between sections

---

#### Step 5: Add Figures and Tables

**PROMPT:**
```
Help me decide what figures and tables to include in my literature review:

1. **Table 2.1: Comparison of Key Studies**
   - Which studies should be compared?
   - What columns should the table have? (Author, Year, Sample, Method, Key Findings, Limitations)

2. **Figure 2.1: PRISMA Flow Diagram**
   - Already created in Prompt 2.4
   - Where to place? (usually in Section 2.1 or as early as possible)

3. **Figure 2.2: Theoretical Framework Diagram**
   - Visualize the main theoretical framework
   - Show relationships between key concepts

4. **Figure 2.3: Timeline of Research Evolution** (optional)
   - If chronological trends are important
   - Show how the field has evolved over time

5. **Figure 2.4: Positioning Diagram**
   - 2x2 matrix or Venn diagram
   - Show where your research fits relative to existing work

For each figure/table:
1. Suggest where to place it (which section)
2. Provide caption template
3. Ensure it's referenced in text ("as shown in Figure 2.X...")

Generate:
1. List of recommended figures/tables
2. Caption templates
3. Placement suggestions
```

**EXPECTED OUTPUT:**
- List of figures and tables to create
- Caption templates
- Placement guidance

**MANUAL WORK:**
- Create figures using draw.io, PowerPoint, TikZ, or other tools
- Format tables in Markdown or LaTeX
- Insert into appropriate sections
- Ensure all figures/tables are referenced in text

---

#### Step 6: Final Polish

**PROMPT:**
```
Help me perform final polish on my literature review chapter:

1. CITATION COUNT:
   - I've cited [NUMBER] unique sources
   - Is this sufficient for my field?
   - Target: 50-150 sources (field-dependent)
   - Are there key papers I'm missing?

2. BALANCE OF SOURCES:
   - Seminal papers (≥10 years old): [COUNT]
   - Recent papers (≤5 years): [COUNT]
   - Is this balance appropriate? (should have both foundational and recent)

3. VERB TENSE:
   - Use past tense for specific studies: "Smith (2020) found..."
   - Use present tense for established knowledge: "Research shows..."
   - Check consistency

4. VOICE:
   - Minimize passive voice
   - Use active voice where possible: "Researchers have demonstrated X" (not "X has been demonstrated")

5. CLARITY:
   - Are there overly long sentences? (>30 words)
   - Are there paragraphs that are too long? (>200 words)
   - Are there jargon terms that need definition?

6. CITATION FORMAT:
   - Are all in-text citations formatted correctly? (APA, Chicago, IEEE, etc.)
   - Are all cited papers in the reference list?
   - Are all references cited in text?

Provide:
1. Citation count assessment
2. List of verb tense errors to fix
3. List of overly long/complex sentences to simplify
4. Citation format issues to correct

Also generate a checklist for final review before submitting to advisor.
```

**EXPECTED OUTPUT:**
- Final polish checklist
- List of specific fixes needed

**MANUAL WORK:**
- Read aloud (catches awkward phrasing)
- Run spell/grammar check (Grammarly, Word, etc.)
- Verify all citations are accurate
- Format consistently
- Check figure/table numbering

---

#### Step 7: Prepare for Advisor Review

**PROMPT:**
```
I'm ready to submit my literature review chapter to my advisor.

Help me prepare:

1. SELF-REVIEW CHECKLIST:
   - [ ] All sections complete (2.1-2.6)
   - [ ] Word count appropriate (8,000-15,000 words)
   - [ ] All citations accurate (no made-up sources)
   - [ ] Figures/tables included and referenced
   - [ ] PRISMA diagram included (if systematic review)
   - [ ] Gaps clearly articulated
   - [ ] Positioning of my research is clear
   - [ ] Smooth transitions between sections
   - [ ] Critical analysis (not just summary)
   - [ ] No typos or grammatical errors

2. ADVISOR MEETING PREPARATION:
   - What specific feedback should I request?
   - What questions should I ask?
   - What are likely areas of concern?

3. FEEDBACK TRACKING:
   - Create a template to track advisor feedback
   - Columns: Date, Section, Feedback, Action Taken, Status

Generate:
1. Complete self-review checklist
2. List of questions for advisor
3. Feedback tracking template
```

**EXPECTED OUTPUT:**
- Self-review checklist
- Advisor meeting preparation guide
- Feedback tracking template

**SAVE AS:** `/02_Literature_Review/review_checklist.md` and `/02_Literature_Review/advisor_feedback_tracker.md`

---

**VERIFICATION CHECKLIST FOR PROMPT 2.8:**
- [ ] Section 2.6.1 (Key Findings) drafted
- [ ] Section 2.6.2 (Gaps) drafted
- [ ] Section 2.6.3 (Positioning) drafted
- [ ] Integration check completed
- [ ] Terminology consistent throughout
- [ ] Transitions smooth
- [ ] Figures and tables added
- [ ] All figures/tables referenced in text
- [ ] Citation count appropriate (50-150 unique sources)
- [ ] Citation format consistent
- [ ] Final polish completed (grammar, clarity, verb tense)
- [ ] Self-review checklist completed
- [ ] Ready for advisor review

**EXPECTED OUTPUT:**
- **Complete Chapter 2: Literature Review (8,000-15,000 words)**
- All sections (2.1-2.6) fully drafted
- Figures and tables included
- Citations formatted and accurate
- Ready for advisor feedback

**SAVE AS:** `/02_Literature_Review/chapter_02_literature_review_COMPLETE.md`

---

## ✅ ENHANCED QUALITY CHECKS FOR STAGE 2

Before moving to Stage 3 (Methodology), verify:

### Content Quality
- [ ] Systematic search process is documented and reproducible
- [ ] PRISMA diagram accurately represents the process (if applicable)
- [ ] Inclusion/exclusion criteria are clear and consistently applied
- [ ] 50-150 unique sources cited (field-dependent)
- [ ] Balance of seminal (≥10 years) and recent (≤5 years) papers
- [ ] Literature synthesis matrix is complete
- [ ] Research gaps are clearly articulated and justified (3-5 major gaps)
- [ ] Literature review is analytical/critical, not just descriptive
- [ ] All claims are supported by citations (no unsupported assertions)

### Structure and Organization
- [ ] Review connects back to research questions throughout
- [ ] Theoretical foundation is established
- [ ] Papers are synthesized (grouped by theme), not just listed
- [ ] Contradictions and disagreements are discussed
- [ ] Each major section (2.2-2.5) has critical evaluation
- [ ] Section 2.6 effectively synthesizes and identifies gaps
- [ ] Positioning of current research is clear (Section 2.6.3)

### Writing Quality
- [ ] Word count is appropriate (typically 8,000-15,000 words)
- [ ] Transitions between sections are smooth
- [ ] Terminology is consistent throughout
- [ ] Verb tense is consistent (past for studies, present for knowledge)
- [ ] No overly long sentences (>30 words) or paragraphs (>200 words)
- [ ] Minimal passive voice
- [ ] No typos or grammatical errors

### Citations and References
- [ ] References are properly formatted (APA, Chicago, IEEE, etc.)
- [ ] All in-text citations appear in reference list
- [ ] All references are cited in text
- [ ] No over-reliance on secondary sources
- [ ] No made-up citations (all sources verified)

### Figures and Tables
- [ ] PRISMA diagram included (if systematic review)
- [ ] Comparison tables included (Table 2.1 minimum)
- [ ] Positioning diagram included (Figure 2.X)
- [ ] All figures/tables are referenced in text
- [ ] All figures/tables have clear captions

### Advisor Approval
- [ ] Chapter reviewed by advisor
- [ ] Feedback incorporated
- [ ] Scope approved (not too broad, not too narrow)
- [ ] Gaps justified and defensible
- [ ] Positioning of research is clear

### Reproducibility
- [ ] Search protocol is documented (databases, keywords, dates)
- [ ] Screening decisions are documented
- [ ] Another researcher could reproduce the search
- [ ] Data extraction process is clear

---

## 🔄 REVISION ITERATION PROCESS

**Literature reviews require multiple drafts. Follow this 5-iteration process:**

### Iteration 1: First Draft (Weeks 1-3)
**Goal:** Get ideas down, complete all sections

**Tasks:**
- [ ] Complete Prompts 2.1-2.8
- [ ] Draft all sections (2.1-2.6)
- [ ] Cite papers (even if citations incomplete)
- [ ] Create basic structure

**Advisor Review:** Optional (for very rough feedback)

**Deliverable:** Rough draft with all sections present

---

### Iteration 2: Critical Analysis (Week 4)
**Goal:** Add evaluation, not just summary

**Tasks:**
- [ ] Review each section: Are you analyzing or just describing?
- [ ] Add critical evaluation to each subsection
- [ ] Identify strengths and limitations of papers
- [ ] Discuss contradictions and disagreements
- [ ] Connect findings to your research questions

**Self-Check:**
- Does each paragraph contain analysis, or just summary?
- Have you identified patterns across papers?
- Have you evaluated methodological quality?

**Deliverable:** Draft with critical analysis added

---

### Iteration 3: Gap Refinement (Week 5)
**Goal:** Ensure gaps are real and defensible

**Tasks:**
- [ ] Review Section 2.6.2 (Gaps)
- [ ] Are gaps truly gaps, or just understudied areas?
- [ ] Are gaps significant? (why do they matter?)
- [ ] Are gaps addressable by your research?
- [ ] Are gaps defensible if challenged?

**Advisor Review:** **CRITICAL CHECKPOINT**
- Submit Sections 2.6.1-2.6.3 (gap analysis and positioning)
- Ask: "Are these gaps real? Are they significant? Does my research address them?"

**Deliverable:** Draft with refined gap analysis, approved by advisor

---

### Iteration 4: Writing Quality (Week 6)
**Goal:** Clarity, flow, transitions, readability

**Tasks:**
- [ ] Read entire chapter start to finish
- [ ] Fix awkward phrasing
- [ ] Improve transitions between sections
- [ ] Check terminology consistency
- [ ] Simplify complex sentences
- [ ] Eliminate redundancy
- [ ] Ensure logical flow

**Self-Check:**
- Can someone unfamiliar with your topic understand it?
- Does the chapter tell a coherent story?
- Are there smooth transitions between sections?

**Deliverable:** Draft with improved writing quality

---

### Iteration 5: Citations & Formatting (Week 7)
**Goal:** Perfect citations, formatting, polish

**Tasks:**
- [ ] Verify all citations are accurate (no made-up sources)
- [ ] Check citation format consistency (APA, Chicago, IEEE)
- [ ] Ensure all in-text citations are in reference list
- [ ] Ensure all references are cited in text
- [ ] Format figures and tables correctly
- [ ] Add figure/table captions
- [ ] Proofread for typos and grammar
- [ ] Check word count (8,000-15,000 words)

**Tools:**
- Zotero/Mendeley for citation management
- Grammarly or similar for grammar check
- University style guide for formatting

**Advisor Review:** Submit complete chapter for final review

**Deliverable:** Final polished draft, ready for dissertation

---

### When to Stop Iterating

**You're done when:**
- [ ] Advisor approves the chapter
- [ ] All quality checks pass
- [ ] You can defend every claim and gap
- [ ] The chapter clearly sets up your research
- [ ] Writing is clear and professional
- [ ] Citations are accurate and complete

**Estimated Time:** 6-8 weeks for complete literature review (including research, synthesis, writing, revisions)

---

## 🔧 ITERATION GUIDANCE: TROUBLESHOOTING

### Problem: Too Many Papers (>200)
**Return to:** Prompt 2.1 (Tighten inclusion criteria)
**Solution:**
- Narrow time period (e.g., last 5 years instead of 10)
- Focus on higher-quality journals
- Exclude gray literature
- Apply stricter relevance criteria

### Problem: Too Few Papers (<30)
**Return to:** Prompt 2.2 (Broaden search terms)
**Solution:**
- Add more databases
- Use broader keywords
- Extend time period
- Include gray literature (dissertations, conference papers)
- Check for variant terms you missed

### Problem: Gaps Unclear or Weak
**Return to:** Prompt 2.5-2.6 (Deepen synthesis)
**Solution:**
- Re-examine contradictions in literature (these are often gaps)
- Look for methodological limitations across papers
- Identify populations, contexts, or variables not yet studied
- Consult with advisor on what constitutes a "real" gap

### Problem: Writing Too Descriptive (No Analysis)
**Return to:** Prompt 2.7 (Add critical analysis)
**Solution:**
- Don't just summarize papers; evaluate them
- Ask: What are the strengths? Limitations? Implications?
- Compare and contrast findings across papers
- Identify patterns and trends
- Connect findings to your research questions

### Problem: Review Feels Disconnected from Research
**Return to:** Prompt 2.8 (Improve positioning)
**Solution:**
- Add explicit connections to RQs in each section
- Ensure Section 2.6.3 clearly positions your research
- End each major section with: "These findings inform my research by..."
- Make sure gaps directly relate to your RQs

### Problem: Advisor Says "Too Broad" or "Too Narrow"
**Return to:** Prompt 2.1 (Adjust scope)
**Solution:**
- Too broad: Tighten inclusion criteria, focus on most relevant papers
- Too narrow: Broaden search terms, expand time period, include adjacent areas

### Problem: Citations Are Inconsistent or Incomplete
**Return to:** Use reference manager (Zotero, Mendeley, EndNote)
**Solution:**
- Import all papers into reference manager
- Use auto-cite features
- Export bibliography in required format
- Verify all in-text citations match reference list

---

## 📁 COMPLETE FILE STRUCTURE FOR STAGE 2

```
/Dissertation_Project/
  /02_Literature_Review/

    ## Planning Documents
    - inclusion_exclusion_criteria.md
    - search_protocol.md
    - search_strings.md

    ## Search Execution
    - search_log.md (dates, databases, results)
    - [database_name]_export.ris (exported references)
    - screening_tracker.xlsx (title/abstract/full-text screening)

    ## Synthesis
    - PRISMA_diagram.md (and .png/.pdf)
    - synthesis_matrix.xlsx (data extraction spreadsheet)
    - synthesis_by_theme.md
    - gap_analysis.md
    - comparison_tables.md

    ## Writing
    - lit_review_outline.md
    - section_2.1_introduction.md
    - section_2.2_[theme1].md
    - section_2.3_[theme2].md
    - section_2.4_[theme3].md
    - section_2.5_[theme4].md
    - section_2.6.1_key_findings.md
    - section_2.6.2_gaps.md
    - section_2.6.3_positioning.md

    ## Final Output
    - chapter_02_literature_review_COMPLETE.md
    - references.bib (or .ris)

    ## Review
    - review_checklist.md
    - advisor_feedback_tracker.md
```

---

## 📚 RESOURCES

### Reference Managers
- **Zotero** (free, open-source): https://www.zotero.org/
- **Mendeley** (free): https://www.mendeley.com/
- **EndNote** (paid, institutional license): https://endnote.com/

### Systematic Review Tools
- **Rayyan** (free, web-based screening): https://www.rayyan.ai/
- **Covidence** (paid, comprehensive): https://www.covidence.org/
- **PRISMA** (guidelines): http://www.prisma-statement.org/

### Databases (Field-Dependent)
- **Multidisciplinary:** Scopus, Web of Science, Google Scholar
- **Computer Science:** IEEE Xplore, ACM Digital Library
- **Health/Medicine:** PubMed, Embase, CINAHL
- **Psychology:** PsycINFO, PsycARTICLES
- **Education:** ERIC
- **Business:** ABI/INFORM, Business Source Complete
- **Social Sciences:** JSTOR, ProQuest

### Citation Formats
- **APA 7th Edition:** https://apastyle.apa.org/
- **Chicago Manual of Style:** https://www.chicagomanualofstyle.org/
- **IEEE:** https://ieeeauthorcenter.ieee.org/

---

## 🎯 EXPECTED TIMELINE FOR STAGE 2

**Total Time:** 6-10 weeks (field-dependent, can vary significantly)

| Week | Task | Prompts | Time |
|------|------|---------|------|
| 1 | Define criteria, develop search strategy | 2.1, 2.2 | 5-10 hours |
| 2 | Execute searches, screen titles/abstracts | 2.3, 2.4 (partial) | 10-20 hours |
| 3 | Full-text screening, citation search | 2.4 (complete) | 10-20 hours |
| 4 | Data extraction, synthesis | 2.5 | 15-25 hours |
| 5 | Structure review, write Sections 2.1-2.3 | 2.6, 2.7 (partial) | 15-20 hours |
| 6 | Write Sections 2.4-2.5 | 2.7 (continued) | 15-20 hours |
| 7 | Write Section 2.6, finalize | 2.8 | 10-15 hours |
| 8 | Revise (Iteration 2-3) | N/A | 10-15 hours |
| 9 | Revise (Iteration 4-5) | N/A | 10-15 hours |
| 10 | Final polish, advisor review | N/A | 5-10 hours |

**Total Estimated Hours:** 105-180 hours

**Note:** Timeline varies significantly by:
- Number of papers (30 vs. 150)
- Field (some fields require more extensive reviews)
- Your reading speed
- Whether you're doing systematic review (longer) vs. narrative review (shorter)

---

**Feed outputs from Stage 2 into Stage 3: Methodology Design**

---

**END OF WORKFLOW 02: LITERATURE REVIEW**
