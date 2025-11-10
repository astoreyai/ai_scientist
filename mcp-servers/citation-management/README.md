# Research Citation Management MCP Server

Citation verification, retraction checking, and BibTeX management for academic research.

## Features

- **DOI Verification** via Crossref API
- **Retraction Checking** via Crossref retraction status
- **Citation Counts** via OpenCitations API
- **BibTeX Management** - Parse, clean, deduplicate
- **Multiple Citation Styles** - APA, IEEE, Chicago, Harvard

## Installation

```bash
pip install research-citation-management
```

Or from source:
```bash
cd mcp-servers/citation-management
pip install -e .
```

## Configuration

Add to Claude Desktop config:

```json
{
  "mcpServers": {
    "citations": {
      "command": "python",
      "args": ["-m", "research_citations.server"]
    }
  }
}
```

## MCP Tools

### verify_citations
Batch verify DOIs via Crossref.

**Parameters:**
- `doi_list` (array): List of DOIs to verify

**Returns:** Verification status for each DOI

### check_retractions
Check if papers have been retracted.

**Parameters:**
- `doi_list` (array): List of DOIs to check

**Returns:** Retraction status for each DOI

### format_bibliography
Format citations in specific style.

**Parameters:**
- `bibtex_string` (string): BibTeX entries
- `style` (string): Citation style ("apa", "ieee", "chicago", etc.)

**Returns:** Formatted bibliography

### clean_bibtex_file
Clean and deduplicate BibTeX entries.

**Parameters:**
- `bibtex_string` (string): BibTeX content

**Returns:** Cleaned BibTeX without duplicates

### get_citation_metadata
Get complete metadata for a DOI.

**Parameters:**
- `doi` (string): Paper DOI

**Returns:** Combined Crossref + OpenCitations metadata

## Example Usage

```python
# Verify DOIs
result = await call_tool("citations", "verify_citations", {
    "doi_list": ["10.1000/xyz123", "10.1000/abc456"]
})

# Check for retractions
retractions = await call_tool("citations", "check_retractions", {
    "doi_list": ["10.1000/xyz123"]
})
```

## API Access

- **Crossref**: Public API (no key required, polite pool recommended)
- **OpenCitations**: Public API (no key required)

## Rate Limiting

- Crossref: 50 requests/second (unlimited)
- OpenCitations: No strict limit (implemented 1s delay)

## License

MIT License
