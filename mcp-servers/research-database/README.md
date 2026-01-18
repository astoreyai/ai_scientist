# Research Database MCP Server

PostgreSQL-based research data storage for systematic reviews and research workflows.

## Features

- **Literature Management** - Store search results, screening decisions
- **Data Extraction** - Structured extraction with full-text search
- **PRISMA Support** - Track PRISMA flow diagram counts
- **Screening Workflow** - Inter-rater reliability tracking
- **Full-Text Search** - PostgreSQL FTS for literature queries

## Installation

```bash
pip install research-database
```

Or from source:
```bash
cd mcp-servers/research-database
pip install -e .
```

## Prerequisites

**PostgreSQL Database:**
```bash
# Install PostgreSQL
sudo apt-get install postgresql postgresql-contrib  # Linux
brew install postgresql  # macOS

# Create database
createdb research_db
```

## Configuration

Add to Claude Desktop config:

```json
{
  "mcpServers": {
    "research-db": {
      "command": "python",
      "args": ["-m", "research_db.server"],
      "env": {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "research_db",
        "DB_USER": "your_username",
        "DB_PASSWORD": "your_password"
      }
    }
  }
}
```

## Database Schema

**Tables:**
- `literature` - Search results and screening
- `extracted_data` - Study data extraction
- `prisma_flow` - PRISMA diagram counts
- `screening_decisions` - Inter-rater reliability

## MCP Tools

### store_literature
Store literature search results.

**Parameters:**
- `papers` (array): Array of paper objects with metadata

**Returns:** Number of papers stored

### query_literature
Full-text search across stored literature.

**Parameters:**
- `search_query` (string): Search terms
- `filters` (object, optional): Filter by stage, year, etc.

**Returns:** Matching papers

### store_extraction
Store extracted data from a study.

**Parameters:**
- `study_id` (int): Study identifier
- `extracted_data` (object): Structured extraction data

**Returns:** Extraction ID

### get_prisma_counts
Get PRISMA flow diagram counts.

**Parameters:**
- `project_name` (string): Research project identifier

**Returns:** Counts for each PRISMA stage

### update_study_stage
Update screening stage for a study.

**Parameters:**
- `study_id` (int): Study identifier
- `new_stage` (string): Stage name

**Returns:** Success status

### get_database_stats
Get database statistics.

**Returns:** Total studies, by stage, etc.

## Example Usage

```python
# Store literature
result = await call_tool("research-db", "store_literature", {
    "papers": [
        {
            "title": "Paper title",
            "authors": ["Author1", "Author2"],
            "doi": "10.1000/xyz",
            "year": 2024,
            "abstract": "...",
            "stage": "identified"
        }
    ]
})

# Query literature
results = await call_tool("research-db", "query_literature", {
    "search_query": "machine learning",
    "filters": {"stage": "included", "year_min": 2020}
})
```

## Security

- Use environment variables for credentials
- Don't commit database passwords
- Use connection pooling for production
- Implement row-level security if needed

## License

MIT License
