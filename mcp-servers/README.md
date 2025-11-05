# MCP Servers for Research Assistant System

Three custom MCP servers providing research capabilities: literature search, citation management, and research database.

**All servers use REAL API integrations - NO MOCKS.**

---

## Servers

### 1. Literature Search (`literature-search.py`)

Unified search across academic databases with deduplication.

**Databases:**
- **OpenAlex** - Comprehensive, free, 250M+ works
- **arXiv** - Physics, CS, math preprints
- **PubMed** - Biomedical literature (35M+ citations)

**Tools:**
- `search_literature(query, databases, date_range, max_results_per_db)` - Multi-database search
- `get_paper_metadata(identifier, id_type)` - Fetch detailed metadata
- `get_citation_count(doi)` - Get citation count from OpenAlex

**Setup:**
```bash
# Install dependencies
pip install pyalex arxiv biopython requests

# Set environment variables (optional but recommended)
export OPENALEX_EMAIL="your@email.com"  # Faster rate limits
export PUBMED_EMAIL="your@email.com"    # Required
export PUBMED_API_KEY="your-key"        # Optional, increases rate limit
```

**Example Usage:**
```python
# Search multiple databases
results = search_literature(
    query="machine learning quantum computing",
    databases=["openalex", "arxiv"],
    date_range=["2020-01-01", "2024-12-31"],
    max_results_per_db=50
)

# Returns:
{
    "query": "machine learning quantum computing",
    "databases_searched": ["openalex", "arxiv"],
    "total_results": 89,
    "unique_results": 76,
    "duplicates_removed": 13,
    "papers": [...]
}
```

---

### 2. Citation Management (`citation-management.py`)

Citation verification, retraction checking, and BibTeX processing.

**APIs:**
- **Crossref** - DOI resolution, metadata, retraction checking
- **OpenCitations** - Citation data, citation counts

**Tools:**
- `verify_citations(doi_list)` - Verify DOIs and get metadata
- `check_retractions(doi_list)` - Check for retracted papers
- `format_bibliography(bibtex_string, style)` - Format citations (APA, IEEE, Chicago)
- `clean_bibtex_file(bibtex_string)` - Clean and deduplicate BibTeX
- `get_citation_metadata(doi)` - Complete metadata from all sources

**Setup:**
```bash
# Install dependencies
pip install habanero bibtexparser requests

# Optional: Set OpenCitations token for higher rate limits
export OPENCITATIONS_TOKEN="your-token"
```

**Example Usage:**
```python
# Check for retractions
result = check_retractions([
    "10.1126/science.aaa1234",
    "10.1038/nature12345"
])

# Returns:
{
    "total_checked": 2,
    "retracted_count": 1,
    "retracted_papers": [{
        "doi": "10.1126/science.aaa1234",
        "retracted": true,
        "retraction_date": [2023, 5, 15]
    }]
}
```

---

### 3. Research Database (`research-database.py`)

PostgreSQL database for systematic review data storage.

**Features:**
- Literature storage with full-text search
- PRISMA flow tracking
- Data extraction storage
- Screening decision tracking (inter-rater reliability)

**Tools:**
- `store_literature(papers)` - Store search results
- `query_literature(search_query, filters, limit)` - Full-text search
- `store_extraction(study_id, extracted_data)` - Store extracted data
- `get_prisma_counts(project_name)` - Get PRISMA flow diagram counts
- `update_study_stage(study_id, new_stage, exclusion_reason)` - Update study progress
- `get_database_stats()` - Database statistics

**Setup:**
```bash
# Install dependencies
pip install psycopg2-binary

# Create database
createdb research_db

# Set environment variables
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="research_db"
export DB_USER="postgres"
export DB_PASSWORD="your-password"

# Database schema is auto-created on first run
```

**Example Usage:**
```python
# Store literature search results
result = store_literature(papers)

# Query with full-text search
results = query_literature(
    search_query="mindfulness anxiety",
    filters={"year_min": 2015, "stage": "included"},
    limit=100
)

# Get PRISMA counts
counts = get_prisma_counts("my_review")
# Returns: {"identified": 1234, "screened": 456, "included": 89, ...}
```

---

## Installation

### Prerequisites

```bash
# Python 3.11+
python --version

# PostgreSQL (for research-database server)
psql --version

# Node.js (for standard MCP servers)
node --version
```

### Python Dependencies

```bash
# Install all dependencies at once
pip install -r ../requirements.txt

# Or install individually
pip install mcp pyalex arxiv biopython habanero bibtexparser psycopg2-binary requests
```

### Database Setup

```bash
# Create PostgreSQL database
createdb research_db

# Or with specific user
createdb -U postgres research_db

# Verify
psql -d research_db -c "SELECT version();"
```

---

## Configuration

### Claude Desktop Configuration

Edit `~/.claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "literature": {
      "command": "python",
      "args": ["/full/path/to/mcp-servers/literature-search.py"],
      "env": {
        "OPENALEX_EMAIL": "your@email.com",
        "PUBMED_EMAIL": "your@email.com"
      }
    },
    "citations": {
      "command": "python",
      "args": ["/full/path/to/mcp-servers/citation-management.py"]
    },
    "research_db": {
      "command": "python",
      "args": ["/full/path/to/mcp-servers/research-database.py"],
      "env": {
        "DB_HOST": "localhost",
        "DB_NAME": "research_db",
        "DB_USER": "postgres",
        "DB_PASSWORD": "your-password"
      }
    }
  }
}
```

**See `claude_desktop_config.json.template` for complete example.**

---

## Testing

### Test Individual Servers

```bash
# Test literature search
python literature-search.py
# (Will start MCP server, then test with MCP client)

# Test citation management
python citation-management.py

# Test research database (requires PostgreSQL running)
python research-database.py
```

### Integration Test

Once configured in Claude Desktop, test in Claude Code:

```
You: "Search for papers on quantum computing from 2023"

Claude: [Uses literature MCP server]
Found 156 papers from OpenAlex, arXiv, and PubMed.
Removed 23 duplicates. Showing 133 unique papers...
```

---

## API Rate Limits

### OpenAlex
- **Polite pool** (with email): ~10 req/sec
- **Without email**: ~1 req/sec
- **No authentication required**

### PubMed
- **Without API key**: 3 req/sec
- **With API key**: 10 req/sec
- **Email required**
- Get API key: https://www.ncbi.nlm.nih.gov/account/settings/

### arXiv
- **Rate limit**: ~1 req/3 sec
- **No authentication**

### Crossref
- **Polite**: ~1 req/sec (with email in User-Agent)
- **No authentication required**

### OpenCitations
- **Public API**: Limited
- **With token**: Higher limits
- Get token: https://opencitations.net/

---

## Troubleshooting

### "Database connection failed"

```bash
# Check PostgreSQL is running
pg_isready

# Check connection
psql -h localhost -U postgres -d research_db -c "SELECT 1;"

# Verify environment variables
echo $DB_HOST $DB_NAME $DB_USER
```

### "ModuleNotFoundError: No module named 'pyalex'"

```bash
# Install missing dependencies
pip install pyalex arxiv biopython habanero bibtexparser psycopg2-binary
```

### "Rate limit exceeded"

- Set email in environment variables (OPENALEX_EMAIL, PUBMED_EMAIL)
- Get API keys where available (PUBMED_API_KEY, OPENCITATIONS_TOKEN)
- Reduce concurrent requests
- Add delays between batches

### "psycopg2.OperationalError"

```bash
# Install PostgreSQL if not installed
# Ubuntu/Debian:
sudo apt-get install postgresql postgresql-contrib

# macOS:
brew install postgresql

# Start PostgreSQL service
# Ubuntu/Debian:
sudo service postgresql start

# macOS:
brew services start postgresql
```

---

## Production Notes

### Security

- **Never commit** database passwords or API keys
- Use environment variables for all credentials
- Restrict database access to localhost in production
- Use SSL/TLS for database connections in production

### Performance

- **Connection pooling**: For high-volume use, implement connection pooling
- **Caching**: Consider caching frequently accessed papers
- **Batch operations**: Process papers in batches for database operations
- **Indexes**: Database indexes are created automatically for common queries

### Monitoring

```python
# Get database statistics
stats = get_database_stats()
# Returns: counts by source, stage, year

# Monitor API usage
# Check logs for rate limit warnings
tail -f server.log | grep "rate limit"
```

---

## References

- **OpenAlex API**: https://docs.openalex.org/
- **arXiv API**: https://info.arxiv.org/help/api/index.html
- **PubMed E-utilities**: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- **Crossref API**: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- **OpenCitations**: https://opencitations.net/index/api/v1
- **MCP Specification**: https://spec.modelcontextprotocol.io/
- **MCP Python SDK**: https://github.com/modelcontextprotocol/python-sdk

---

**Status:** Production-ready with real API integrations
**Last Updated:** January 5, 2025
