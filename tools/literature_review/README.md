# Literature Review Tools

**Purpose:** Support systematic, reproducible literature reviews following PRISMA guidelines

---

## 🚀 NEW: Automated Scopus Pipeline

**Want to save 90% of time on literature searches?**

We now provide a **fully automated Scopus search pipeline** that:
- ✅ Executes searches via Scopus API with full documentation
- ✅ Exports to BibTeX, RIS, CSV automatically
- ✅ Deduplicates papers with confidence scores
- ✅ Updates PRISMA diagram automatically
- ✅ Generates complete execution logs for reproducibility

**📖 Quick Start:** See [`automated_scopus/README.md`](automated_scopus/README.md)

**📖 Integration Guide:** See [`AUTOMATED_INTEGRATION_GUIDE.md`](AUTOMATED_INTEGRATION_GUIDE.md)

**Time Saved:** Manual = 1.5-2.5 hours per search session → Automated = 5-10 minutes

**Note:** You still manually screen papers (title/abstract/full-text), extract data, and synthesize findings. Automation handles mechanical tasks only.

---

## Tools in This Directory

### 1. [search_protocol_template.md](search_protocol_template.md)
**Complete protocol for systematic literature search**

Use this to:
- Define research questions
- Set inclusion/exclusion criteria
- Develop keyword search strategy
- Document database searches
- Track screening process
- Ensure reproducibility

**When to use:** At the START of your literature review (before searching)

**Output:** A completed protocol you can reference in your methodology chapter

---

### 2. [inclusion_exclusion_criteria_template.md](inclusion_exclusion_criteria_template.md)
**Detailed criteria for selecting papers**

Use this to:
- Define objective, reproducible selection criteria
- Create decision trees for screening
- Handle edge cases systematically
- Document reasons for exclusion
- Ensure inter-rater reliability

**When to use:** During protocol development (fills into search_protocol_template.md)

**Output:** Clear, defensible criteria for your methodology

---

### 3. [prisma_flow_diagram_template.md](prisma_flow_diagram_template.md)
**PRISMA 2020 compliant flow diagram**

Use this to:
- Track papers through screening stages
- Document numbers at each stage
- Report exclusion reasons with counts
- Create publication-ready diagram
- Meet PRISMA reporting standards

**When to use:** THROUGHOUT the review process (update as you screen)

**Output:** Flow diagram for your methods section (required for systematic reviews)

---

### 4. [synthesis_matrix_template.csv](synthesis_matrix_template.csv)
**Structured data extraction spreadsheet**

Use this to:
- Extract key information from each paper
- Compare studies systematically
- Identify patterns and gaps
- Support synthesis and analysis
- Track quality ratings

**When to use:** During data extraction phase (after selecting papers)

**Output:** Spreadsheet feeding into your literature review chapter

**How to use:**
1. Open in Excel, Google Sheets, or LibreOffice
2. Add one row per included paper
3. Fill in all columns
4. Sort/filter to identify themes
5. Use for writing synthesis sections

**Columns:**
- Citation, Year, Title, Authors, Venue
- Study_Type (empirical/theoretical/review)
- Research_Questions, Methodology, Sample_Size
- Key_Findings, Limitations
- Relevance_to_RQ1/RQ2/RQ3 (adapt to your RQs)
- Quality_Rating, Notes

---

## Workflow: Using These Tools Together

### Phase 1: Planning (Week 1)

1. **Define Research Questions** (from [01_topic_development.md](../../workflows/01_topic_development.md))
2. **Complete `search_protocol_template.md`**
   - Fill in research questions
   - Use `inclusion_exclusion_criteria_template.md` to define criteria
   - Develop keyword strategy (Section 4-5)
   - List databases to search (Section 6)
3. **Finalize protocol BEFORE searching** (avoid bias)

### Phase 2: Searching (Week 1-2)

1. **Execute searches in each database**
2. **Document in `search_protocol_template.md` Section 5**
   - Record exact search strings
   - Record dates
   - Record result counts
3. **Export results to reference manager** (Zotero, Mendeley, EndNote)
4. **Remove duplicates**
5. **Update `prisma_flow_diagram_template.md`** (Identification section)

### Phase 3: Screening (Week 2-4)

1. **Title/Abstract Screening**
   - Apply inclusion/exclusion criteria
   - Use decision tree from `inclusion_exclusion_criteria_template.md`
   - Track excluded papers with reasons
   - Update `prisma_flow_diagram_template.md` (Screening section)

2. **Full-Text Screening**
   - Retrieve full-text articles
   - Apply full criteria
   - Document exclusions in detail
   - Update `prisma_flow_diagram_template.md` (Eligibility section)

3. **Citation Network Analysis**
   - Backward search (check references of key papers)
   - Forward search (check papers citing key papers)
   - Update `prisma_flow_diagram_template.md` (Additional sources)

### Phase 4: Data Extraction (Week 4-6)

1. **Open `synthesis_matrix_template.csv`**
2. **Create one row per included paper**
3. **Extract key information systematically**
4. **Rate quality using criteria from `search_protocol_template.md` Section 9**
5. **Add notes on relevance to each research question**

### Phase 5: Synthesis (Week 6-8)

1. **Analyze `synthesis_matrix_template.csv`**
   - Sort by theme/topic
   - Group similar methodologies
   - Identify patterns
   - Find contradictions
   - Locate gaps

2. **Write Literature Review Chapter**
   - Use [chapter_02_literature_review.md](../../templates/dissertation/chapter_02_literature_review.md) template
   - Organize by themes (not chronologically)
   - Synthesize (don't just summarize)
   - Connect to your research questions
   - Highlight gaps your work addresses

### Phase 6: Reporting (Ongoing)

1. **In Methods Section:**
   - Include PRISMA diagram (from `prisma_flow_diagram_template.md`)
   - Summarize search strategy
   - Reference full protocol in appendix

2. **In Appendix:**
   - Complete search protocol (from `search_protocol_template.md`)
   - Full search strings for each database
   - Inclusion/exclusion criteria (from `inclusion_exclusion_criteria_template.md`)
   - List of included studies (optional)
   - List of excluded studies with reasons (optional, if manageable)

---

## Expected Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| **1. Planning** | 1 week | Completed search protocol |
| **2. Searching** | 1-2 weeks | Database results exported |
| **3. Screening** | 2-4 weeks | Final set of included papers |
| **4. Data Extraction** | 2-4 weeks | Completed synthesis matrix |
| **5. Synthesis** | 2-4 weeks | Written literature review chapter |
| **6. Revision** | 1-2 weeks | Polished chapter |
| **TOTAL** | **8-15 weeks** | Complete Chapter 2 |

*Timeline varies based on:*
- Breadth of research topic (narrow vs. broad)
- Number of papers to screen (100 vs. 1000+)
- Solo vs. team screening
- Availability of database access

---

## Quality Checks

Before considering your literature review complete, verify:

### Systematic Search:
- [ ] Search protocol documented before searching
- [ ] ≥2 databases searched
- [ ] Search strings recorded with dates
- [ ] Backward/forward citation analysis done
- [ ] PRISMA diagram complete with actual numbers

### Reproducibility:
- [ ] Inclusion/exclusion criteria are objective
- [ ] Another researcher could replicate your search
- [ ] All decisions documented with rationale
- [ ] Deviations from protocol explained

### Synthesis Quality:
- [ ] Organized by themes (not chronologically)
- [ ] Critical analysis (not just summary)
- [ ] Gaps clearly identified
- [ ] Connects to your research questions
- [ ] All claims cited

### Reporting:
- [ ] PRISMA checklist complete
- [ ] Flow diagram in methods
- [ ] Search strategy in methods/appendix
- [ ] Synthesis matrix supports claims
- [ ] 50-150+ sources (field-dependent)

---

## Common Pitfalls to Avoid

### ❌ **Don't:** Start searching without a protocol
**Why:** Risk of bias - you might unconsciously search for papers confirming your hypothesis
**Fix:** Complete search_protocol_template.md FIRST

### ❌ **Don't:** Define criteria after screening
**Why:** Post-hoc criteria are not objective
**Fix:** Finalize inclusion/exclusion criteria before seeing search results

### ❌ **Don't:** Only search one database
**Why:** Incomplete coverage, not systematic
**Fix:** Search ≥2 databases + citation networks

### ❌ **Don't:** Forget to document excluded papers
**Why:** PRISMA requires counts and reasons
**Fix:** Track exclusions in prisma_flow_diagram_template.md

### ❌ **Don't:** Only cite papers that agree with you
**Why:** Confirmation bias, cherry-picking
**Fix:** Include contradictory findings, discuss disagreements

### ❌ **Don't:** Write descriptive summaries
**Why:** Literature review should synthesize and analyze
**Fix:** Organize by themes, identify patterns, critique methods

### ❌ **Don't:** Skip quality assessment
**Why:** Low-quality papers can mislead
**Fix:** Rate quality in synthesis matrix, consider excluding very low quality

### ❌ **Don't:** Ignore negative results
**Why:** Publication bias - field may overestimate effect sizes
**Fix:** Actively search for failed replications and null results

---

## Field-Specific Adaptations

### Computer Science:
- **Databases:** Scopus, Web of Science, IEEE Xplore, ACM Digital Library, arXiv, DBLP
- **Quality:** Conference rank (CORE), journal impact factor
- **Typical count:** 50-150 papers

### Engineering:
- **Databases:** Scopus, Web of Science, Compendex, IEEE Xplore
- **Quality:** Journal quartile (JCR), patent citations
- **Typical count:** 60-200 papers

### Natural Sciences:
- **Databases:** PubMed, Web of Science, Scopus, PubMed Central
- **Quality:** Journal impact factor, study design rigor
- **Typical count:** 100-300 papers (more for medical reviews)

### Social Sciences:
- **Databases:** PsycINFO, ERIC, Sociological Abstracts, Web of Science
- **Quality:** Study design, sample size, statistical power
- **Typical count:** 75-200 papers

### Mathematics:
- **Databases:** MathSciNet, zbMATH, arXiv
- **Quality:** Journal prestige, citation count
- **Typical count:** 40-100 papers (more selective, theory-focused)

---

## Additional Resources

### PRISMA Guidelines:
- **Website:** http://prisma-statement.org/
- **2020 Statement:** http://prisma-statement.org/PRISMAStatement/
- **Explanation & Elaboration:** http://prisma-statement.org/documents/PRISMA_2020_explanation_elaboration.pdf

### Reference Managers:
- **Zotero** (free, open-source): https://www.zotero.org/
- **Mendeley** (free): https://www.mendeley.com/
- **EndNote** (paid, often via university): https://endnote.com/

### Systematic Review Tools:
- **Covidence:** https://www.covidence.org/ (systematic review platform)
- **Rayyan:** https://www.rayyan.ai/ (free for academics)
- **PRISMA Flow Diagram Generator:** http://prisma.thetacollaborative.ca/

### Database Access:
- Contact your university library for access to:
  - Scopus, Web of Science, IEEE Xplore, etc.
  - Interlibrary loan for inaccessible papers
  - Systematic review support services

---

## Integration with PhD Pipeline

These tools integrate with:

1. **[workflows/02_literature_review.md](../../workflows/02_literature_review.md)**
   - Follow that workflow for step-by-step prompts
   - Use these templates to capture outputs

2. **[templates/dissertation/chapter_02_literature_review.md](../../templates/dissertation/chapter_02_literature_review.md)**
   - Write your synthesis here
   - Reference data from synthesis matrix

3. **[tools/bibliography/](../bibliography/)**
   - Use citation_guidelines.md for citing papers
   - Export references.bib from reference manager

4. **[tools/quality_assurance/scientific_validity_checklist.md](../quality_assurance/scientific_validity_checklist.md)**
   - Verify all literature review claims are cited
   - Ensure RULE 1 compliance (no unsupported claims)

---

## RULE 1: Scientific Truth Compliance

**✅ These tools enforce RULE 1 by:**

1. **Reproducibility:** Systematic search protocol ensures another researcher can replicate your review
2. **Transparency:** PRISMA diagram shows exactly what papers were included/excluded and why
3. **Objectivity:** Predefined inclusion/exclusion criteria minimize bias
4. **Traceability:** Synthesis matrix links every claim to specific papers
5. **Completeness:** Cannot cherry-pick papers - must report all papers meeting criteria

**✅ When writing literature review, you CAN claim:**
- "Our systematic search identified N papers meeting inclusion criteria"
- "X papers reported positive effects, Y papers found null results"
- "The literature shows inconsistent findings (cite, cite, cite)"

**❌ When writing literature review, you CANNOT claim:**
- "Most studies agree..." (without systematic count)
- "It is well known..." (without citation)
- "Obviously..." or "Clearly..." (without evidence)
- Selectively cite only papers supporting your hypothesis

---

**Need help?** See [PHD_PIPELINE/README.md](../../README.md) or [PIPELINE_GUIDE.md](../../PIPELINE_GUIDE.md)
