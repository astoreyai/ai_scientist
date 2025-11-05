# Automated Scopus Pipeline - Integration Guide

**How to use the automated pipeline with existing PhD dissertation workflow**

---

## Overview

The automated Scopus pipeline **replaces manual search execution** but **integrates seamlessly** with the existing literature review workflow.

### What Changes

**BEFORE (Manual):**
- Manually execute searches in Scopus web interface (20-30 min)
- Manually export results from each database (10-15 min)
- Manually import to reference manager (5-10 min)
- Manually deduplicate (30-60 min)
- Manually document everything (20-30 min)
- **Total: 1.5-2.5 hours** per search session

**AFTER (Automated):**
- Define queries in YAML (5 min, one-time)
- Run `python scopus_search.py` (30 sec)
- Run `python result_exporter.py` (automatic)
- Run `python deduplication.py` (2 min)
- Import to reference manager (5 min)
- **Total: 5-10 minutes** per search session

### What Stays the Same

✅ You still define inclusion/exclusion criteria (REQUIRED for objectivity)
✅ You still screen titles/abstracts manually (REQUIRED for quality)
✅ You still read full-text papers (REQUIRED for understanding)
✅ You still extract data manually (REQUIRED for depth)
✅ You still synthesize findings (REQUIRED for insight)

**Automation saves 90% of time on mechanical tasks, lets you focus on intellectual work.**

---

## Integration with Workflow 02

### Original Workflow Mapping

| **Original Prompt** | **Automated Equivalent** | **Status** |
|---------------------|--------------------------|------------|
| **2.1: Define Inclusion/Exclusion Criteria** | Same (no change) | ✅ Manual (required) |
| **2.2: Develop Search Strategy** | Edit `config/search_queries.yaml` | ✅ Automated |
| **2.3: Execute Systematic Search** | Run `scopus_search.py` | ✅ Automated |
| **2.3: Export Results** | Run `result_exporter.py` | ✅ Automated |
| **2.3: Deduplicate** | Run `deduplication.py` | ✅ Automated |
| **2.4: Screen and Select Papers** | Same (no change) | ✅ Manual (required) |
| **2.5: Extract Data and Synthesize** | Same (no change) | ✅ Manual (required) |
| **2.6: Structure Literature Review** | Same (no change) | ✅ Manual (required) |
| **2.7: Write Literature Review Sections** | Same (no change) | ✅ Manual (required) |
| **2.8: Write Gap Analysis and Finalize** | Same (no change) | ✅ Manual (required) |

### Modified Workflow Timeline

| **Week** | **Phase** | **Automated Steps** | **Manual Steps** | **Time** |
|----------|-----------|---------------------|------------------|----------|
| **1** | **Planning** | None | Define criteria (2.1) | 5-10 hours |
| | | Edit `search_queries.yaml` | Validate queries | |
| **2** | **Search Execution** | Run scripts (5-10 min) | Review results | 5-10 hours |
| | | `scopus_search.py` | Import to ref manager | |
| | | `result_exporter.py` | | |
| | | `deduplication.py` | | |
| **3** | **Title Screening** | None | Screen titles (2.4) | 10-20 hours |
| **4** | **Abstract Screening** | None | Screen abstracts (2.4) | 10-20 hours |
| **5** | **Full-Text Screening** | None | Retrieve & screen (2.4) | 10-20 hours |
| **6-7** | **Data Extraction** | None | Extract data (2.5) | 15-25 hours |
| **8-9** | **Synthesis** | None | Synthesize findings (2.5-2.6) | 15-25 hours |
| **10-12** | **Writing** | None | Write chapters (2.7-2.8) | 25-35 hours |
| **13-14** | **Revision** | None | Revise & polish | 10-15 hours |

**Total Timeline:** 13-14 weeks (same as before)
**Total Work:** 105-180 hours (same as before)
**Time Saved:** 1-2 hours per week on mechanical tasks = **More time for thinking!**

---

## Step-by-Step Integration

### Phase 1: Setup (One-Time, 15 minutes)

1. **Install dependencies**
   ```bash
   cd /home/aaron/projects/xai/PHD_PIPELINE/tools/literature_review/automated_scopus
   pip install -r requirements.txt
   ```

2. **Get Scopus API key**
   - Go to https://dev.elsevier.com/
   - Register with your institution email
   - Create application
   - Copy API key

3. **Configure credentials**
   ```bash
   cd config/
   nano scopus_config.yaml
   # Add your API key
   ```

4. **Read documentation**
   - `README.md` - Quick start
   - `AUTOMATED_SCOPUS_PIPELINE.md` - Full architecture

### Phase 2: Define Search Strategy (Week 1)

**Follows Prompt 2.1-2.2 from original workflow**

1. **Define inclusion/exclusion criteria** (REQUIRED)
   - Use `tools/literature_review/inclusion_exclusion_criteria_template.md`
   - This step is NOT automated - you must define criteria BEFORE searching

2. **Define search queries**
   - Edit `config/search_queries.yaml`
   - Start with 1-2 queries, test, then expand

   ```yaml
   searches:
     - id: "search_001"
       name: "Your Research Topic"
       query: >
         TITLE-ABS-KEY("keyword1" OR "keyword2")
         AND TITLE-ABS-KEY("keyword3")
       date_range:
         start: 2015
         end: 2025
       research_questions:
         - "RQ1: What are we investigating?"
       enabled: true
   ```

3. **Validate queries**
   ```bash
   cd scripts/
   python scopus_search.py --dry-run
   ```

### Phase 3: Execute Searches (Week 2, 10 minutes)

**Replaces Prompt 2.3 (manual execution)**

```bash
cd scripts/

# 1. Execute searches (30 seconds)
python scopus_search.py

# 2. Export results (automatic)
python result_exporter.py

# 3. Deduplicate (2 minutes)
python deduplication.py

# 4. Update PRISMA (1 minute)
python prisma_updater.py
```

**Outputs:**
- `exports/deduplicated/all_results_*.ris` - Import this to reference manager
- `exports/deduplicated/screening_*.csv` - Use this for screening
- `prisma_flow_diagram.md` - Include in dissertation
- `logs/search_log_*.md` - Document in methodology

### Phase 4: Import to Reference Manager (5 minutes)

**Zotero:**
1. File → Import → Choose `exports/deduplicated/all_results_*.ris`
2. Select collection: "Literature Review - [Your Topic]"
3. Verify count matches (should be "Unique papers" count from deduplication)

**Mendeley:**
1. File → Import → RIS → Choose `exports/deduplicated/all_results_*.ris`
2. Create folder: "Literature Review - [Your Topic]"

**EndNote:**
1. File → Import → File → Choose `exports/deduplicated/all_results_*.ris`
2. Import Option: RefMan RIS

### Phase 5: Manual Screening (Weeks 3-5)

**Follows Prompt 2.4 from original workflow**

Use `exports/deduplicated/screening_*.csv`:

1. **Title screening**
   - Open CSV in Excel/Google Sheets
   - Mark `Title_Screen` column: Include / Exclude / Uncertain
   - Fill `Exclusion_Reason` for excluded papers

2. **Abstract screening**
   - For "Include" and "Uncertain" from title screening
   - Mark `Abstract_Screen` column
   - Update `Exclusion_Reason` if excluded

3. **Full-text screening**
   - Retrieve full texts for included papers
   - Mark `Full_Text_Screen` column
   - Final inclusion decision

**Tip:** Use reference manager's tagging/groups feature to track screening decisions

### Phase 6: Data Extraction (Weeks 6-7)

**Follows Prompt 2.5 from original workflow**

Use `tools/literature_review/synthesis_matrix_template.csv`:

1. Create one row per included paper
2. Extract key information systematically
3. Rate quality
4. Note relevance to each research question

### Phase 7: Synthesis & Writing (Weeks 8-14)

**Follows Prompts 2.5-2.8 from original workflow**

1. **Synthesize** findings from synthesis matrix (Prompt 2.5)
2. **Structure** literature review (Prompt 2.6)
3. **Write** sections 2.1-2.6 (Prompts 2.7-2.8)
4. **Include** PRISMA diagram from `prisma_flow_diagram.md`
5. **Reference** search log from `logs/search_log_*.md` in methodology

---

## Reproducibility Documentation

### In Your Methodology Chapter

Include the following to document reproducibility:

```markdown
### 2.X.X Systematic Literature Search

A systematic literature search was conducted using the Scopus database
via the Scopus Search API (Elsevier, 2025) on [DATE]. The search was
fully automated using a reproducible pipeline to ensure transparency
and replicability.

**Search Strategy:**
Three search queries were executed (see Appendix A for complete query
syntax):
1. Search 001: [Name] - Retrieved 146 papers
2. Search 002: [Name] - Retrieved 12 papers
3. Total: 158 papers identified

**Deduplication:**
Automated deduplication was performed using three strategies:
- Exact DOI matching
- Title and first author matching
- Fuzzy title matching (threshold: 85%)

A total of 13 duplicates (8.2%) were identified and removed,
resulting in 145 unique papers for screening.

**PRISMA Flow:**
The systematic search and screening process followed PRISMA guidelines
(Page et al., 2021). See Figure X for the complete PRISMA flow diagram.

**Reproducibility:**
All search queries, API parameters, and execution logs are available
in the project repository. The search can be reproduced by executing
the provided scripts with the archived configuration files.
```

### In Your Appendix

Include:

1. **Appendix A: Complete Search Queries**
   - Copy from `logs/search_log_*.md`
   - Shows exact query syntax for each search

2. **Appendix B: PRISMA Flow Diagram**
   - Insert `prisma_flow_diagram.md` content
   - Visual diagram (generate at http://prisma.thetacollaborative.ca/)

3. **Appendix C: Deduplication Report** (optional)
   - Copy from `reports/deduplication_report_*.md`
   - Shows transparency in duplicate handling

### In Your References

Cite the tools:

```
Elsevier. (2025). Scopus Search API. https://dev.elsevier.com/

Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021).
The PRISMA 2020 statement: an updated guideline for reporting
systematic reviews. BMJ, 372, n71.
```

---

## Benefits of Automation

### 1. Time Savings
- **90% less time** on mechanical tasks
- More time for reading and thinking
- Faster iteration on search strategies

### 2. Reproducibility
- **Exact reproduction** of searches possible
- All parameters documented automatically
- Version-controlled query definitions

### 3. Transparency
- **Complete audit trail** for peer review
- Timestamps on all operations
- No black-box processing

### 4. Quality
- **Consistent application** of criteria
- No manual transcription errors
- Automatic duplicate detection

### 5. Iteration
- **Easy to re-run** searches as your topic evolves
- Test different search strategies quickly
- Combine results from multiple iterations

---

## Common Questions

### Q: Do I still need to manually screen papers?

**A: Yes!** Automation handles **mechanical** tasks (searching, exporting, deduplicating).
You still do all **intellectual** tasks (screening, reading, synthesizing).

**Why?**
- Only a human can judge paper relevance to your specific research questions
- Automated screening would introduce bias
- PhD-level synthesis requires human expertise

### Q: Is automated search acceptable for my dissertation?

**A: Yes!** As long as you:
- Document the process completely (which the pipeline does automatically)
- Use objective, pre-defined criteria (which you still define manually)
- Follow PRISMA guidelines (which the pipeline enforces)

**In fact, automation IMPROVES quality:**
- More reproducible than manual searching
- Better documentation
- Eliminates human error in mechanical steps

### Q: Can I add non-Scopus sources?

**A: Yes!** The pipeline is designed for Scopus, but you can:
- Manually add papers from other sources to your reference manager
- Document non-Scopus sources in PRISMA diagram (there's a section for this)
- Combine automated + manual searches

**Recommended:** Use automated pipeline for primary search, then manually add:
- Citation network papers (backward/forward search)
- Hand-searched journals
- Gray literature (if needed)

### Q: What if Scopus doesn't have full coverage of my field?

**A: Add complementary searches:**
- Use automated pipeline for Scopus
- Manually search Web of Science, PubMed, IEEE Xplore, etc.
- Document all sources in PRISMA
- Combine results

**Future:** The pipeline architecture supports extending to other databases
(see `AUTOMATED_SCOPUS_PIPELINE.md` - Advanced Features)

### Q: How do I cite the automated pipeline in my dissertation?

**A: Two options:**

**Option 1 (Recommended):** Cite the API and method
```
Searches were executed using the Scopus Search API (Elsevier, 2025)
with an automated reproducible pipeline following PRISMA guidelines
(Page et al., 2021).
```

**Option 2:** Cite as software (if publishing the pipeline)
```
Searches were executed using the Automated Scopus Literature Review
Pipeline (Smith, 2025), which implements the Scopus Search API
(Elsevier, 2025) following PRISMA guidelines (Page et al., 2021).
```

---

## Troubleshooting Integration

### Issue: Results seem incomplete compared to web interface

**Explanation:** The API and web interface may have slight differences. This is normal.

**Solution:**
- Document the exact API version and date
- Note in methodology that API was used (not web interface)
- This is actually MORE reproducible than web interface

### Issue: Reference manager import shows different count than deduplication

**Check:**
- Did all papers import successfully?
- Are there import errors in reference manager?
- Check reference manager duplicate detection (may find additional duplicates)

**Solution:** Document both counts in methodology if different

### Issue: Advisor wants me to search other databases too

**Solution:** Use automated pipeline for Scopus, manual searches for others

**Document:**
```
Primary search: Scopus (automated, N=145 unique papers)
Supplementary searches:
  - Web of Science (manual, N=87 unique papers)
  - Citation network (manual, N=12 unique papers)
Combined after cross-database deduplication: N=198 unique papers
```

---

## Next Steps

1. **Setup** the pipeline (15 minutes, one-time)
2. **Define** your search queries following Prompt 2.1-2.2
3. **Execute** the automated pipeline (10 minutes)
4. **Continue** with manual workflow from Prompt 2.4 (screening)
5. **Document** using automatically generated logs and PRISMA diagram

---

**This integration transforms literature review from tedious manual work to systematic, reproducible science while preserving the intellectual rigor required for a PhD dissertation. ✅**

**Questions? See:**
- `automated_scopus/README.md` - Quick start
- `AUTOMATED_SCOPUS_PIPELINE.md` - Full architecture
- `workflows/02_literature_review.md` - Original workflow
