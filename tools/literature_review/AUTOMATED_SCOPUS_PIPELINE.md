# Automated Scopus Literature Review Pipeline

**Version:** 1.0.0
**Date:** October 16, 2025
**Purpose:** Fully automated, reproducible literature review using Scopus API

---

## Overview

This pipeline automates the systematic literature review process using the Scopus Search API, ensuring:

✅ **Reproducibility** - Same query always produces same results with full provenance
✅ **Automation** - Minimal manual work, maximum documentation
✅ **Quality** - Peer-review ready documentation
✅ **Integration** - Works seamlessly with existing PhD pipeline tools
✅ **RULE 1 Compliance** - Complete transparency and traceability

---

## Architecture

```
User Input:
- search_queries.yaml      # Define searches with metadata
- scopus_config.yaml       # API credentials and settings

↓ Execute Automated Pipeline

Scripts:
1. scopus_search.py        # Execute searches via Scopus API
2. result_exporter.py      # Export to .bib, .ris, .csv
3. prisma_updater.py       # Auto-update PRISMA diagram
4. deduplication.py        # Find and mark duplicates

↓ Automated Outputs

Outputs:
- results/                 # Raw API responses (JSON)
- exports/                 # Formatted exports (.bib, .ris, .csv)
- logs/                    # Complete execution logs
- prisma_updated.md        # Auto-updated PRISMA diagram
- search_log.md            # Complete search documentation
```

---

## Key Features

### 1. Query Management
- Define searches in YAML with full metadata
- Version control queries alongside code
- Execute single or batch searches
- Track query history and modifications

### 2. Automatic Documentation
- Generates search log with exact timestamps
- Updates PRISMA flow diagram automatically
- Records API responses for reproducibility
- Creates audit trail for peer review

### 3. Multi-Format Export
- **BibTeX (.bib)**: For LaTeX/Overleaf
- **RIS (.ris)**: For Zotero/Mendeley/EndNote
- **CSV (.csv)**: For screening spreadsheet
- **JSON**: Raw data for analysis

### 4. Deduplication
- Automatic detection of duplicate papers
- Multiple matching strategies (DOI, title+author, title fuzzy match)
- Generates deduplication report
- Updates PRISMA counts

### 5. Rate Limit Handling
- Respects Scopus API quotas
- Automatic retry with exponential backoff
- Progress saving (resume interrupted searches)
- Quota monitoring and warnings

---

## File Structure

```
PHD_PIPELINE/tools/literature_review/
├── AUTOMATED_SCOPUS_PIPELINE.md           # This file
├── automated_scopus/                       # New automated tools
│   ├── README.md                          # Quick start guide
│   ├── scopus_config.yaml                 # API configuration
│   ├── search_queries.yaml                # Define your searches
│   ├── scripts/
│   │   ├── scopus_search.py               # Main search script
│   │   ├── result_exporter.py             # Export to multiple formats
│   │   ├── prisma_updater.py              # Auto-update PRISMA
│   │   ├── deduplication.py               # Duplicate detection
│   │   └── query_validator.py             # Validate query syntax
│   ├── results/                           # Raw API results (JSON)
│   ├── exports/                           # Formatted exports
│   ├── logs/                              # Execution logs
│   └── reports/                           # Generated reports
└── [existing templates]                   # Integrate with existing tools
```

---

## Workflow Integration

### Original Workflow (Manual)
```
1. Define criteria → 2. Develop search strategy → 3. Execute searches MANUALLY
→ 4. Export MANUALLY → 5. Import to ref manager → 6. Deduplicate MANUALLY
→ 7. Screen → 8. Extract
```

### Automated Workflow (With Scopus API)
```
1. Define criteria → 2. Define queries in YAML → 3. RUN SCRIPT (automatic)
→ 4-6. AUTOMATED (search, export, deduplicate) → 7. Screen → 8. Extract
```

**Time Saved:** 80-90% of manual search/export/documentation work

---

## Components

### 1. `scopus_config.yaml`
**Purpose:** Store API credentials and global settings

```yaml
# Scopus API Configuration
scopus:
  api_key: "YOUR_API_KEY_HERE"  # Get from https://dev.elsevier.com/
  inst_token: null                # Optional institution token

  # API settings
  base_url: "https://api.elsevier.com/content/search/scopus"
  timeout: 30
  max_results_per_request: 25     # Scopus default
  max_retries: 3
  retry_delay: 5                  # seconds

  # Rate limiting
  quota_limit: 20000              # Weekly quota (adjust to your tier)
  quota_warning_threshold: 0.8    # Warn at 80%

# Output settings
output:
  results_dir: "results"
  exports_dir: "exports"
  logs_dir: "logs"
  reports_dir: "reports"

  # Export formats
  formats:
    - bibtex
    - ris
    - csv
    - json
```

### 2. `search_queries.yaml`
**Purpose:** Define all searches with metadata

```yaml
# Search Queries for Literature Review
# Each query is fully documented and reproducible

searches:
  - id: "search_001"
    name: "XAI Face Recognition"
    description: "Explainable AI methods for face recognition systems"

    # Scopus query syntax
    query: >
      TITLE-ABS-KEY("explainable AI" OR "interpretable" OR "XAI")
      AND TITLE-ABS-KEY("face recognition" OR "face verification" OR "facial recognition")

    # Filters
    date_range:
      start: 2015
      end: 2025

    subject_areas:
      - COMP  # Computer Science
      - ENGI  # Engineering

    document_types:
      - "ar"  # Article
      - "cp"  # Conference paper
      - "re"  # Review

    # Metadata
    research_questions:
      - "RQ1: How are XAI methods applied to face recognition?"
      - "RQ2: What metrics evaluate XAI quality in face recognition?"

    expected_results: "~50-200 papers"
    notes: "Primary search for XAI in face recognition"

  - id: "search_002"
    name: "Falsifiability XAI"
    description: "Falsifiability criterion applied to explainable AI"

    query: >
      TITLE-ABS-KEY("falsifiability" OR "falsifiable" OR "Popper")
      AND TITLE-ABS-KEY("explainable AI" OR "XAI" OR "interpretability")

    date_range:
      start: 2010
      end: 2025

    subject_areas:
      - COMP
      - MULT  # Multidisciplinary

    document_types:
      - "ar"
      - "re"

    research_questions:
      - "RQ1: Has falsifiability been applied to XAI?"

    expected_results: "~5-20 papers"
    notes: "Gap analysis - likely to find few papers"
```

### 3. `scopus_search.py`
**Purpose:** Main script to execute searches

**Key Functions:**
- Load config and queries
- Execute Scopus API calls with pagination
- Handle rate limiting and errors
- Save raw results (JSON)
- Generate search log
- Update PRISMA diagram

**Usage:**
```bash
# Execute all queries
python scopus_search.py

# Execute specific query
python scopus_search.py --query search_001

# Resume interrupted search
python scopus_search.py --resume

# Dry run (validate without executing)
python scopus_search.py --dry-run
```

### 4. `result_exporter.py`
**Purpose:** Convert API results to multiple formats

**Outputs:**
- `exports/search_001.bib` - BibTeX for LaTeX
- `exports/search_001.ris` - RIS for reference managers
- `exports/search_001.csv` - CSV for screening spreadsheet
- `exports/all_results.json` - Combined raw data

**Usage:**
```bash
# Export all results
python result_exporter.py

# Export specific search
python result_exporter.py --search search_001

# Export specific format
python result_exporter.py --format bibtex
```

### 5. `deduplication.py`
**Purpose:** Find and remove duplicate papers

**Strategies:**
1. **Exact DOI match** (highest confidence)
2. **Title + First author match** (high confidence)
3. **Fuzzy title match** (medium confidence, requires review)

**Outputs:**
- `reports/duplicates.csv` - List of duplicates with confidence scores
- `reports/deduplication_report.md` - Summary report
- `exports/deduplicated/` - Deduplicated exports

**Usage:**
```bash
# Run deduplication
python deduplication.py

# Review flagged duplicates
python deduplication.py --review
```

### 6. `prisma_updater.py`
**Purpose:** Automatically update PRISMA diagram

**Updates:**
- Identification phase (database search counts)
- Deduplication counts
- Adds timestamps and provenance

**Usage:**
```bash
# Update PRISMA diagram
python prisma_updater.py

# Generate PRISMA report
python prisma_updater.py --report
```

---

## Usage Guide

### Step 1: Setup

1. **Get Scopus API key**
   - Register at https://dev.elsevier.com/
   - Create application
   - Copy API key

2. **Configure credentials**
   ```bash
   cd PHD_PIPELINE/tools/literature_review/automated_scopus
   cp scopus_config.yaml.template scopus_config.yaml
   # Edit scopus_config.yaml and add your API key
   ```

3. **Install dependencies**
   ```bash
   pip install requests pyyaml bibtexparser rispy python-dotenv fuzzywuzzy
   ```

### Step 2: Define Queries

Edit `search_queries.yaml` to define your searches:

```yaml
searches:
  - id: "search_001"
    name: "My Research Topic"
    description: "Description of what I'm searching for"
    query: >
      TITLE-ABS-KEY("keyword1" OR "keyword2")
      AND TITLE-ABS-KEY("keyword3")
    date_range:
      start: 2015
      end: 2025
    # ... etc
```

**Tip:** Start with 1-2 queries, test, then expand.

### Step 3: Validate Queries

```bash
python scripts/query_validator.py
```

This checks:
- Query syntax is valid
- Expected results are reasonable
- No duplicate query IDs

### Step 4: Execute Searches

```bash
python scripts/scopus_search.py
```

**Output:**
```
[2025-10-16 14:23:15] Starting Scopus search pipeline
[2025-10-16 14:23:15] Loading configuration...
[2025-10-16 14:23:16] Loading queries... Found 2 queries
[2025-10-16 14:23:16] Executing search_001: XAI Face Recognition
[2025-10-16 14:23:18] Retrieved 146 results (6 API calls)
[2025-10-16 14:23:18] Saved to results/search_001_2025-10-16_14-23-15.json
[2025-10-16 14:23:20] Executing search_002: Falsifiability XAI
[2025-10-16 14:23:21] Retrieved 12 results (1 API call)
[2025-10-16 14:23:21] Saved to results/search_002_2025-10-16_14-23-15.json
[2025-10-16 14:23:21] Total results: 158 papers
[2025-10-16 14:23:21] Search log: logs/search_log_2025-10-16.md
[2025-10-16 14:23:21] PRISMA updated: prisma_updated.md
[2025-10-16 14:23:21] Complete!
```

### Step 5: Export Results

```bash
python scripts/result_exporter.py
```

**Output:**
```
Exporting results...
- exports/search_001.bib (146 entries)
- exports/search_001.ris (146 entries)
- exports/search_001.csv (146 rows)
- exports/search_002.bib (12 entries)
- exports/search_002.ris (12 entries)
- exports/search_002.csv (12 rows)
- exports/all_results.json (158 entries)
Complete!
```

### Step 6: Deduplicate

```bash
python scripts/deduplication.py
```

**Output:**
```
Analyzing 158 papers for duplicates...
Found duplicates:
- 8 exact DOI matches
- 3 title+author matches
- 2 fuzzy title matches (review recommended)
Total duplicates: 13 (8.2%)
Remaining unique papers: 145

Report saved to: reports/deduplication_report.md
Deduplicated exports saved to: exports/deduplicated/
```

### Step 7: Import to Reference Manager

**Zotero:**
1. Open Zotero
2. File → Import → Choose `exports/deduplicated/all_results.ris`
3. Select collection: "Literature Review - [Your Topic]"
4. Import

**Mendeley:**
1. Open Mendeley
2. File → Import → RIS → Choose `exports/deduplicated/all_results.ris`
3. Create folder: "Literature Review - [Your Topic]"

**EndNote:**
1. Open EndNote
2. File → Import → File → Choose `exports/deduplicated/all_results.ris`
3. Import Option: RefMan RIS
4. Create group: "Literature Review - [Your Topic]"

### Step 8: Continue Manual Workflow

Now proceed with:
- Title/Abstract screening (use `exports/deduplicated/screening.csv`)
- Full-text screening
- Data extraction (use `synthesis_matrix_template.csv`)
- Writing synthesis

---

## Reproducibility

### What Gets Saved

Every search execution creates:

1. **Raw Results** (`results/`)
   - Complete API JSON responses
   - Timestamped filenames
   - Never modified, permanent record

2. **Execution Log** (`logs/`)
   - Exact timestamp
   - API parameters used
   - Number of results per query
   - API response times
   - Any errors or warnings

3. **Query Snapshot** (`logs/`)
   - Copy of `search_queries.yaml` at execution time
   - Ensures queries are versioned

4. **Exports** (`exports/`)
   - Generated from raw results
   - Can be regenerated anytime

### Reproducing a Search

To reproduce search from October 16, 2025:

```bash
# Use archived query file
cp logs/search_queries_2025-10-16.yaml search_queries.yaml

# Re-run with same config
python scripts/scopus_search.py

# Results should match exactly (unless papers were added/removed from Scopus)
```

### Version Control

**Recommended:**
```bash
git add automated_scopus/search_queries.yaml
git add automated_scopus/scopus_config.yaml  # Remove API key first!
git add automated_scopus/logs/
git commit -m "Literature review search executed: 158 results"
```

---

## RULE 1 Compliance

This pipeline enforces **RULE 1: Scientific Truth** through:

### ✅ Transparency
- Every search is fully documented with timestamps
- Exact API parameters are recorded
- Raw data is preserved

### ✅ Reproducibility
- Queries are defined in version-controlled files
- Anyone can re-run the exact same search
- Results are deterministic (within Scopus updates)

### ✅ Completeness
- All results from query are included (no cherry-picking)
- Duplicates are detected and reported, not hidden
- Exclusions are documented with reasons

### ✅ Traceability
- Every paper can be traced to its source query
- Export formats preserve all metadata
- Screening decisions link back to original results

### ✅ Objectivity
- Queries are defined BEFORE seeing results
- No post-hoc modifications (all changes are logged)
- Automated = eliminates human selection bias

---

## Advanced Features

### Multi-Database Extension

While this pipeline focuses on Scopus, it can be extended:

```yaml
databases:
  - name: scopus
    api_key: "YOUR_SCOPUS_KEY"
    script: scopus_search.py

  - name: web_of_science
    api_key: "YOUR_WOS_KEY"
    script: wos_search.py  # To be implemented

  - name: pubmed
    api_key: "YOUR_PUBMED_KEY"
    script: pubmed_search.py  # To be implemented
```

### Scheduled Searches

Set up cron job to re-run searches weekly:

```bash
# Update literature review every Monday at 9 AM
0 9 * * 1 cd /path/to/automated_scopus && python scripts/scopus_search.py --incremental
```

### Citation Network Search

After initial screening, expand via citation search:

```yaml
searches:
  - id: "citation_forward"
    name: "Citations to Key Papers"
    query_type: "citing"
    source_papers:
      - "DOI:10.1234/example1"
      - "DOI:10.1234/example2"
    # Finds papers citing these papers

  - id: "citation_backward"
    name: "References from Key Papers"
    query_type: "references"
    source_papers:
      - "DOI:10.1234/example1"
    # Finds papers referenced by these papers
```

---

## Troubleshooting

### Error: "API Key Invalid"
**Fix:**
- Verify API key is correct in `scopus_config.yaml`
- Check key hasn't expired
- Verify key has appropriate permissions

### Error: "Quota Exceeded"
**Fix:**
- Wait for quota to reset (typically weekly)
- Reduce `max_results_per_request` to conserve quota
- Contact Elsevier to increase quota limit

### Error: "No Results Found"
**Fix:**
- Verify query syntax using Scopus web interface first
- Check date range isn't too restrictive
- Try broader keywords
- Run `query_validator.py` to check syntax

### Results Don't Match Scopus Web Interface
**Explanation:**
- Scopus database is constantly updated
- Results may vary by hours/days
- API may have slight differences from web interface
- This is expected and should be documented

### Duplicate Detection Missing Obvious Duplicates
**Fix:**
- Check `deduplication.py` settings
- Some duplicates require manual review
- Export `reports/duplicates.csv` and review manually
- Adjust fuzzy matching threshold if needed

---

## Comparison: Manual vs. Automated

| Task | Manual | Automated | Time Saved |
|------|--------|-----------|------------|
| **Execute search** | 5-10 min per database | 30 seconds | 95% |
| **Export results** | 5 min per database | Automatic | 100% |
| **Document search** | 15-30 min | Automatic | 100% |
| **Deduplicate** | 30-60 min | 2 min | 95% |
| **Update PRISMA** | 10-20 min | Automatic | 100% |
| **Generate reports** | 20-30 min | Automatic | 100% |
| **TOTAL (per search)** | **1.5-2.5 hours** | **5-10 min** | **90%+** |

**For systematic review with 3-5 databases:** Manual = 5-10 hours, Automated = 15-30 minutes

---

## Next Steps

After completing automated searches:

1. **Review** `reports/search_summary.md`
2. **Import** deduplicated results to reference manager
3. **Screen** titles/abstracts using `exports/deduplicated/screening.csv`
4. **Continue** with manual workflow (Phase 4: Data Extraction)
5. **Write** literature review chapter using synthesis matrix

---

## Support

**Documentation:**
- [README.md](automated_scopus/README.md) - Quick start
- [API Documentation](https://dev.elsevier.com/documentation/ScopusSearchAPI.wadl) - Scopus API reference

**Common Issues:**
- See "Troubleshooting" section above
- Check `logs/` for detailed error messages
- Review `reports/` for execution summaries

**Questions:**
- Consult your institution's library for Scopus API access
- Check Elsevier Developer Portal for API support

---

**This pipeline transforms literature review from tedious manual work to reproducible, automated science. ✅**
