# Research Literature Search MCP Server

Multi-database literature search for academic research projects.

## Features

- **OpenAlex** - Comprehensive academic database with 250M+ works
- **arXiv** - Physics, CS, math preprint server  
- **PubMed** - Biomedical literature database
- Automatic deduplication by DOI and title similarity
- Parallel database searching
- Rate limiting to respect API guidelines

## Installation

```bash
pip install research-literature-search
```

Or install from source:
```bash
cd mcp-servers/literature-search
pip install -e .
```

## Configuration

Add to Claude Desktop config or project `.mcp.json`:

```json
{
  "mcpServers": {
    "literature": {
      "command": "python",
      "args": ["-m", "research_lit_search.server"],
      "env": {
        "OPENALEX_EMAIL": "your-email@example.com"
      }
    }
  }
}
```

## MCP Tools

### search_literature
Search multiple literature databases simultaneously.

**Parameters:**
- `query` (string): Search query
- `databases` (array): List of databases ["openalex", "arxiv", "pubmed"]
- `date_range` (object, optional): {start_year: 2020, end_year: 2024}
- `max_results_per_db` (int, optional): Maximum results per database (default: 50)

**Returns:** Array of papers with metadata (title, authors, DOI, abstract, year)

### get_paper_metadata
Get detailed metadata for a specific paper.

**Parameters:**
- `identifier` (string): DOI or arXiv ID
- `id_type` (string): "doi" or "arxiv"

**Returns:** Complete paper metadata

### get_citation_count
Get citation count for a paper.

**Parameters:**
- `doi` (string): Paper DOI

**Returns:** Citation count from OpenAlex

## Example Usage

```python
# Through MCP
result = await call_tool("literature", "search_literature", {
    "query": "machine learning attention mechanisms",
    "databases": ["openalex", "arxiv"],
    "date_range": {"start_year": 2020, "end_year": 2024},
    "max_results_per_db": 20
})
```

## API Keys

- **OpenAlex**: Requires email in config (for polite pool access)
- **arXiv**: No key required
- **PubMed**: No key required (uses public Entrez API)

## Rate Limiting

- OpenAlex: 10 requests/second (polite pool with email)
- arXiv: 3 requests/second (built-in delay)
- PubMed: 3 requests/second (NCBI guidelines)

## License

MIT License
