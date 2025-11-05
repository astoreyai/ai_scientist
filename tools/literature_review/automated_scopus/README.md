# Automated Scopus Literature Review Pipeline

**Quick Start Guide**

---

## Overview

This pipeline automates systematic literature searches using the Scopus API, producing reproducible, peer-review-ready documentation.

### What It Does

✅ **Automates** Scopus searches with full documentation
✅ **Exports** to BibTeX (.bib), RIS (.ris), CSV (.csv), JSON
✅ **Deduplicates** papers automatically with confidence scores
✅ **Updates** PRISMA flow diagram with provenance
✅ **Saves** complete execution logs for reproducibility

### What You Still Do Manually

📝 Title/abstract screening
📝 Full-text screening
📝 Data extraction
📝 Synthesis and writing

---

## 📚 Complete Example

**Want to see a full end-to-end example?**

See **[`COMPLETE_EXAMPLE.md`](COMPLETE_EXAMPLE.md)** for a comprehensive walkthrough showing:

- ✅ **Complete search execution** from research question to final papers
- ✅ **All generated files** (logs, reports, exports, PRISMA diagram)
- ✅ **Inclusion/exclusion criteria** with decision tree
- ✅ **Keyword development** for 3 searches with full documentation
- ✅ **Screening workflow** with example data
- ✅ **Dissertation methodology section** (annotated for Chapter 2)
- ✅ **Appendices** ready for dissertation
- ✅ **Timeline and statistics** for 10-week literature review

**Example Topic:** "Explainable AI Methods for Face Recognition Systems"
**From:** Research question → **To:** 38 included papers with complete documentation

---

## Quick Start (5 Minutes)

### 1. Setup

```bash
# Install dependencies
pip install requests pyyaml

# Get Scopus API key
# Go to: https://dev.elsevier.com/
# Register, create app, copy API key

# Configure credentials
cd config/
cp scopus_config.yaml.template scopus_config.yaml
# Edit scopus_config.yaml and add your API key
```

### 2. Define Queries

Edit `config/search_queries.yaml`:

```yaml
searches:
  - id: "search_001"
    name: "Your Research Topic"

    # Specify keywords by concept (documented, organized)
    keywords:
      concept_1_main_topic:
        - "keyword1"
        - "synonym1"
        - "related_term1"
      concept_2_application:
        - "keyword2"
        - "synonym2"

    # Build query from keywords
    query: >
      TITLE-ABS-KEY("keyword1" OR "synonym1" OR "related_term1")
      AND TITLE-ABS-KEY("keyword2" OR "synonym2")

    date_range:
      start: 2015
      end: 2025
    enabled: true
```

**📖 Keyword Development:** See [`KEYWORD_DEVELOPMENT_GUIDE.md`](KEYWORD_DEVELOPMENT_GUIDE.md) for comprehensive guidance on developing effective keywords.

### 3. Execute Pipeline

```bash
cd scripts/

# Run searches
python scopus_search.py

# Export results
python result_exporter.py

# Deduplicate
python deduplication.py

# Update PRISMA
python prisma_updater.py
```

### 4. Import to Reference Manager

```bash
# Zotero: File → Import → exports/deduplicated/all_results_*.ris
# Mendeley: File → Import → RIS → all_results_*.ris
# EndNote: File → Import → File → all_results_*.ris
```

---

## File Structure

```
automated_scopus/
├── README.md                    # This file
├── config/
│   ├── scopus_config.yaml       # API credentials and settings
│   └── search_queries.yaml      # Define your searches
├── scripts/
│   ├── scopus_search.py         # Execute searches
│   ├── result_exporter.py       # Export to formats
│   ├── deduplication.py         # Find duplicates
│   └── prisma_updater.py        # Update PRISMA diagram
├── results/                     # Raw API responses (JSON)
├── exports/                     # Formatted exports
│   └── deduplicated/            # Deduplicated exports
├── logs/                        # Execution logs
└── reports/                     # Generated reports
```

---

## Scripts

### `scopus_search.py` - Execute Searches

```bash
# Execute all enabled queries
python scopus_search.py

# Execute specific query
python scopus_search.py --query search_001

# Validate without executing
python scopus_search.py --dry-run
```

**Outputs:**
- `results/search_*.json` - Raw API responses
- `logs/scopus_search_*.log` - Execution log
- `logs/search_log_*.md` - Comprehensive search documentation

### `result_exporter.py` - Export Results

```bash
# Export to all formats
python result_exporter.py

# Export specific search
python result_exporter.py --search search_001

# Export specific format
python result_exporter.py --format bibtex
```

**Outputs:**
- `exports/*.bib` - BibTeX for LaTeX
- `exports/*.ris` - RIS for reference managers
- `exports/screening_*.csv` - CSV for screening
- `exports/all_results_*.json` - Combined JSON
- `reports/export_report_*.md` - Export summary

### `deduplication.py` - Find Duplicates

```bash
# Run deduplication
python deduplication.py
```

**Outputs:**
- `reports/deduplication_report_*.md` - Deduplication summary
- `reports/duplicates_*.csv` - Detailed duplicate list
- `exports/deduplicated/*.csv` - Deduplicated exports

**Strategies:**
1. **Exact DOI match** (highest confidence)
2. **Title + First author match** (high confidence)
3. **Fuzzy title match** (medium confidence - review recommended)

### `prisma_updater.py` - Update PRISMA

```bash
# Update PRISMA diagram
python prisma_updater.py

# Generate PRISMA report
python prisma_updater.py --report
```

**Outputs:**
- `prisma_flow_diagram.md` - Updated PRISMA diagram
- `reports/prisma_report_*.md` - PRISMA status report

---

## Workflow

### Phase 1: Search Execution (15 minutes)

1. **Define queries** in `config/search_queries.yaml`
2. **Validate**: `python scopus_search.py --dry-run`
3. **Execute**: `python scopus_search.py`

**Result:** Raw search results in `results/`

### Phase 2: Export & Deduplicate (5 minutes)

4. **Export**: `python result_exporter.py`
5. **Deduplicate**: `python deduplication.py`
6. **Update PRISMA**: `python prisma_updater.py`

**Result:** Deduplicated exports in `exports/deduplicated/`

### Phase 3: Import to Reference Manager (5 minutes)

7. Import `exports/deduplicated/all_results_*.ris` to Zotero/Mendeley/EndNote
8. Verify import success

**Result:** Papers in reference manager

### Phase 4: Manual Screening (hours to weeks)

9. **Title screening**: Use `exports/deduplicated/screening_*.csv`
10. **Abstract screening**: Mark Include/Exclude
11. **Full-text screening**: Retrieve and assess full texts

**Result:** Final included papers

### Phase 5: Data Extraction & Synthesis (weeks)

12. Extract data using `tools/literature_review/synthesis_matrix_template.csv`
13. Synthesize findings
14. Write literature review chapter

**Result:** Complete literature review

---

## Keyword Development (Important!)

**High-quality searches require well-developed keywords.**

### Quick Start

1. **Break research question into 2-4 concepts**
2. **List 5-10 keywords per concept** (main terms, synonyms, acronyms)
3. **Build query** connecting concepts with AND, synonyms with OR
4. **Test in Scopus web** interface first
5. **Add to** `config/search_queries.yaml`

### Example

**Research Question:** "How is SHAP used in medical diagnosis?"

**Keywords:**
```yaml
concept_1_shap:
  - "SHAP"
  - "Shapley"
  - "Shapley values"
concept_2_medical:
  - "medical diagnosis"
  - "clinical diagnosis"
  - "disease detection"
```

**Query:**
```
TITLE-ABS-KEY("SHAP" OR "Shapley" OR "Shapley values")
AND TITLE-ABS-KEY("medical diagnosis" OR "clinical diagnosis" OR "disease detection")
```

**📖 Full Guide:** [`KEYWORD_DEVELOPMENT_GUIDE.md`](KEYWORD_DEVELOPMENT_GUIDE.md) - Step-by-step keyword development process

---

## Configuration

### API Credentials (`config/scopus_config.yaml`)

```yaml
scopus:
  api_key: "YOUR_API_KEY_HERE"  # Required
  inst_token: null               # Optional

  # Adjust these based on your quota
  quota_limit: 20000             # Weekly quota
  max_results_per_request: 25    # Default: 25

output:
  formats:
    - bibtex
    - ris
    - csv
    - json
```

### Search Queries (`config/search_queries.yaml`)

```yaml
searches:
  - id: "search_001"
    name: "Descriptive Name"
    description: "What this search covers"
    enabled: true  # Set false to skip

    # Scopus query syntax
    query: >
      TITLE-ABS-KEY("term1" OR "term2")
      AND TITLE-ABS-KEY("term3")

    # Filters
    date_range:
      start: 2015
      end: 2025

    subject_areas:  # Optional
      - COMP  # Computer Science
      - ENGI  # Engineering

    document_types:  # Optional
      - "ar"  # Article
      - "cp"  # Conference Paper
      - "re"  # Review

    # Metadata for documentation
    research_questions:
      - "RQ1: What are we looking for?"

    expected_results: "50-200 papers"
    notes: "Any notes about this search"
```

**Scopus Query Syntax:**
- `TITLE-ABS-KEY("term")` - Search title, abstract, keywords
- `TITLE("term")` - Search title only
- `AUTH("Smith")` - Search author
- `PUBYEAR > 2020` - Publication year
- Boolean: `AND`, `OR`, `AND NOT`
- Wildcards: `comput*` matches "computer", "computing", etc.

**See:** https://dev.elsevier.com/sc_search_tips.html

---

## Reproducibility

### What Gets Saved

Every execution creates:

1. **Raw API responses** (`results/`)
   - Complete JSON with all metadata
   - Never modified, permanent record

2. **Execution logs** (`logs/`)
   - Exact timestamp
   - API parameters used
   - Number of results
   - Any errors

3. **Query snapshots** (`logs/`)
   - Copy of queries at execution time
   - Version control with git

### Reproducing a Search

```bash
# Use archived query file
cp logs/search_queries_2025-10-16.yaml config/search_queries.yaml

# Re-run
python scopus_search.py

# Results should match exactly*
# *Unless papers were added/removed from Scopus
```

**Recommendation:** Version control `config/` directory with git

---

## Troubleshooting

### Error: "API Key Invalid"

**Fix:**
- Verify API key in `config/scopus_config.yaml`
- Check key hasn't expired at https://dev.elsevier.com/

### Error: "Quota Exceeded"

**Fix:**
- Wait for quota to reset (typically weekly)
- Reduce `max_results_per_request` to conserve quota
- Contact Elsevier to increase quota

### Error: "No Results Found"

**Fix:**
- Test query in Scopus web interface first
- Check date range isn't too restrictive
- Try broader keywords
- Run `scopus_search.py --dry-run` to validate syntax

### Results Don't Match Web Interface

**Explanation:**
- Scopus database is constantly updated
- Results may vary by hours/days
- This is expected and should be documented with timestamps

### Deduplication Missing Obvious Duplicates

**Fix:**
- Check `reports/duplicates_*.csv` manually
- Review fuzzy matches flagged for manual review
- Some duplicates (different editions, etc.) require human judgment

---

## Advanced Usage

### Custom Export Formats

Edit `scripts/result_exporter.py` to add custom export formats.

### Multi-Database Extension

The pipeline can be extended to support:
- Web of Science
- PubMed
- IEEE Xplore
- ACM Digital Library

See `AUTOMATED_SCOPUS_PIPELINE.md` for architecture.

### Scheduled Searches

Set up cron job to re-run searches weekly:

```bash
# Monday 9 AM
0 9 * * 1 cd /path/to/automated_scopus/scripts && python scopus_search.py
```

### Citation Network Search

After initial screening, identify key papers and search for:
- Papers **citing** them (forward search)
- Papers they **reference** (backward search)

Use Scopus "Cited by" feature or Google Scholar.

---

## Integration with PhD Pipeline

This automated pipeline integrates with:

1. **`workflows/02_literature_review.md`**
   - Replaces Prompts 2.2-2.3 (search execution)
   - Follow remaining prompts for synthesis

2. **`tools/literature_review/`**
   - Use `synthesis_matrix_template.csv` for data extraction
   - Use `inclusion_exclusion_criteria_template.md` for screening

3. **`templates/dissertation/chapter_02_literature_review.md`**
   - Write synthesis using extracted data
   - Reference PRISMA diagram from `prisma_flow_diagram.md`

---

## Time Savings

| Task | Manual | Automated | Savings |
|------|--------|-----------|---------|
| Execute searches | 5-10 min/database | 30 sec | 95% |
| Export results | 5 min/database | Automatic | 100% |
| Document searches | 15-30 min | Automatic | 100% |
| Deduplicate | 30-60 min | 2 min | 95% |
| Update PRISMA | 10-20 min | 1 min | 95% |
| Generate reports | 20-30 min | Automatic | 100% |
| **Total** | **1.5-2.5 hours** | **5-10 min** | **90%+** |

---

## Support

**Documentation:**
- `AUTOMATED_SCOPUS_PIPELINE.md` - Full architecture
- `config/search_queries.yaml` - Query examples
- Scopus API Docs: https://dev.elsevier.com/

**Common Issues:**
- Check `logs/` for detailed error messages
- Review `reports/` for execution summaries

**Questions:**
- Contact your library for Scopus API access
- Elsevier Developer Portal for API support

---

## Examples

### Example 1: Single Topic Search

```yaml
searches:
  - id: "ml_healthcare"
    name: "Machine Learning in Healthcare"
    query: >
      TITLE-ABS-KEY("machine learning" OR "deep learning")
      AND TITLE-ABS-KEY("healthcare" OR "medical")
    date_range:
      start: 2018
      end: 2025
    enabled: true
```

### Example 2: Multiple Related Searches

```yaml
searches:
  - id: "xai_methods"
    name: "XAI Methods"
    query: >
      TITLE-ABS-KEY("SHAP" OR "LIME" OR "Grad-CAM")
    date_range:
      start: 2017
      end: 2025

  - id: "xai_applications"
    name: "XAI Applications"
    query: >
      TITLE-ABS-KEY("explainable AI")
      AND TITLE-ABS-KEY("application" OR "case study")
    date_range:
      start: 2017
      end: 2025
```

### Example 3: Gap Analysis Search

```yaml
searches:
  - id: "gap_analysis"
    name: "Falsifiability in XAI (Gap)"
    query: >
      TITLE-ABS-KEY("falsifiability" OR "falsifiable")
      AND TITLE-ABS-KEY("explainable AI" OR "XAI")
    date_range:
      start: 2010
      end: 2025
    expected_results: "5-20 papers"
    notes: "Expected to find few papers - establishes novelty"
```

---

**Ready to start? Edit `config/search_queries.yaml` and run `python scopus_search.py`! 🚀**
