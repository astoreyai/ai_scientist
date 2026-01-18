#!/usr/bin/env python3
"""
Research Database MCP Server

PostgreSQL database for research data storage:
- Literature records (search results, screening decisions)
- Extracted data (systematic review data extraction)
- PRISMA flow counts
- Full-text search capabilities

Real PostgreSQL integration - NO MOCKS.

Setup:
    1. Create PostgreSQL database: createdb research_db
    2. Set environment variables (see below)
    3. Run server: python research-database.py

MCP Configuration:
    {
      "mcpServers": {
        "research_db": {
          "command": "python",
          "args": ["/path/to/mcp-servers/research-database.py"],
          "env": {
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
            "DB_NAME": "research_db",
            "DB_USER": "postgres",
            "DB_PASSWORD": "your_password"
          }
        }
      }
    }
"""

import os
import sys
import json
from typing import List, Dict, Optional
from datetime import datetime
import logging

# MCP Framework
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("ERROR: MCP framework not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Database
try:
    import psycopg2
    from psycopg2.extras import RealDictCursor, Json
    from psycopg2 import sql
except ImportError:
    print("ERROR: psycopg2 not installed. Run: pip install psycopg2-binary", file=sys.stderr)
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("research-database")

# ============================================
# CONFIGURATION
# ============================================

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "research_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
}

# ============================================
# DATABASE CONNECTION
# ============================================

def get_connection():
    """Get database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise


# ============================================
# SCHEMA INITIALIZATION
# ============================================

def initialize_schema():
    """Create database schema if not exists"""
    logger.info("Initializing database schema")

    schema_sql = """
    -- Literature table (stores search results)
    CREATE TABLE IF NOT EXISTS literature (
        id SERIAL PRIMARY KEY,
        study_id VARCHAR(255) UNIQUE NOT NULL,
        title TEXT NOT NULL,
        authors TEXT[],
        year INTEGER,
        abstract TEXT,
        doi VARCHAR(255),
        url TEXT,
        source VARCHAR(50),  -- openalex, arxiv, pubmed, etc.
        publication_date DATE,
        journal TEXT,
        citation_count INTEGER,
        pdf_url TEXT,
        metadata JSONB,  -- Additional metadata
        stage VARCHAR(50) DEFAULT 'identified',  -- identified, screened, eligible, included, excluded
        exclusion_reason TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Create indexes for performance
    CREATE INDEX IF NOT EXISTS idx_literature_doi ON literature(doi);
    CREATE INDEX IF NOT EXISTS idx_literature_stage ON literature(stage);
    CREATE INDEX IF NOT EXISTS idx_literature_year ON literature(year);
    CREATE INDEX IF NOT EXISTS idx_literature_title_fts ON literature USING gin(to_tsvector('english', title));
    CREATE INDEX IF NOT EXISTS idx_literature_abstract_fts ON literature USING gin(to_tsvector('english', COALESCE(abstract, '')));

    -- Extracted data table (systematic review data extraction)
    CREATE TABLE IF NOT EXISTS extracted_data (
        id SERIAL PRIMARY KEY,
        study_id VARCHAR(255) REFERENCES literature(study_id) ON DELETE CASCADE,
        data JSONB NOT NULL,  -- Structured extraction data
        extracted_by VARCHAR(100),
        extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(study_id)
    );

    -- PRISMA flow tracking
    CREATE TABLE IF NOT EXISTS prisma_flow (
        id SERIAL PRIMARY KEY,
        project_name VARCHAR(255) NOT NULL,
        stage VARCHAR(50) NOT NULL,  -- identification, screening, eligibility, included
        count INTEGER NOT NULL,
        details JSONB,  -- Additional details (e.g., exclusion reasons breakdown)
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(project_name, stage)
    );

    -- Screening decisions (for inter-rater reliability)
    CREATE TABLE IF NOT EXISTS screening_decisions (
        id SERIAL PRIMARY KEY,
        study_id VARCHAR(255) REFERENCES literature(study_id) ON DELETE CASCADE,
        reviewer VARCHAR(100) NOT NULL,
        stage VARCHAR(50) NOT NULL,  -- title_abstract, full_text
        decision BOOLEAN NOT NULL,  -- include (TRUE) or exclude (FALSE)
        reason TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE INDEX IF NOT EXISTS idx_screening_study ON screening_decisions(study_id);
    CREATE INDEX IF NOT EXISTS idx_screening_reviewer ON screening_decisions(reviewer);
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(schema_sql)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Database schema initialized successfully")
    except Exception as e:
        logger.error(f"Schema initialization failed: {e}")
        raise


# ============================================
# MCP TOOLS
# ============================================

@mcp.tool()
def store_literature(papers: List[Dict]) -> dict:
    """
    Store literature search results in database

    Args:
        papers: List of paper dictionaries (from literature-search MCP server)

    Returns:
        Dictionary with storage statistics
    """
    logger.info(f"Storing {len(papers)} papers")

    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0
    updated = 0
    errors = []

    for paper in papers:
        try:
            # Generate study_id if not present
            study_id = paper.get("id", f"{paper['source']}:{paper.get('doi', paper['title'][:50])}")

            # Insert or update
            cursor.execute("""
                INSERT INTO literature (
                    study_id, title, authors, year, abstract, doi, url,
                    source, publication_date, journal, citation_count, pdf_url, metadata, stage
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'identified')
                ON CONFLICT (study_id) DO UPDATE SET
                    title = EXCLUDED.title,
                    authors = EXCLUDED.authors,
                    year = EXCLUDED.year,
                    abstract = EXCLUDED.abstract,
                    doi = EXCLUDED.doi,
                    url = EXCLUDED.url,
                    source = EXCLUDED.source,
                    publication_date = EXCLUDED.publication_date,
                    journal = EXCLUDED.journal,
                    citation_count = EXCLUDED.citation_count,
                    pdf_url = EXCLUDED.pdf_url,
                    metadata = EXCLUDED.metadata,
                    updated_at = CURRENT_TIMESTAMP
                RETURNING (xmax = 0) AS inserted
            """, (
                study_id,
                paper.get("title"),
                paper.get("authors"),
                paper.get("year"),
                paper.get("abstract"),
                paper.get("doi"),
                paper.get("url"),
                paper.get("source"),
                paper.get("publication_date"),
                paper.get("journal"),
                paper.get("citation_count"),
                paper.get("pdf_url"),
                Json(paper)  # Store full paper data as JSONB
            ))

            result = cursor.fetchone()
            if result and result[0]:
                inserted += 1
            else:
                updated += 1

        except Exception as e:
            errors.append({"study_id": study_id, "error": str(e)})
            logger.error(f"Failed to store paper {study_id}: {e}")

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "total_processed": len(papers),
        "inserted": inserted,
        "updated": updated,
        "errors": len(errors),
        "error_details": errors[:10]  # Limit error details
    }


@mcp.tool()
def query_literature(search_query: str, filters: Optional[Dict] = None,
                    limit: int = 100) -> dict:
    """
    Search literature database with full-text search and filters

    Args:
        search_query: Full-text search query (searches title and abstract)
        filters: Optional filters dict. Supported keys:
                 - year_min: int
                 - year_max: int
                 - stage: str (identified, screened, eligible, included, excluded)
                 - source: str (openalex, arxiv, pubmed)
        limit: Maximum results (default 100)

    Returns:
        Dictionary with search results
    """
    logger.info(f"Querying literature: {search_query}")

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Build query
    where_clauses = [
        "to_tsvector('english', title || ' ' || COALESCE(abstract, '')) @@ plainto_tsquery('english', %s)"
    ]
    params = [search_query]

    if filters:
        if "year_min" in filters:
            where_clauses.append("year >= %s")
            params.append(filters["year_min"])

        if "year_max" in filters:
            where_clauses.append("year <= %s")
            params.append(filters["year_max"])

        if "stage" in filters:
            where_clauses.append("stage = %s")
            params.append(filters["stage"])

        if "source" in filters:
            where_clauses.append("source = %s")
            params.append(filters["source"])

    where_sql = " AND ".join(where_clauses)
    params.append(limit)

    query = f"""
        SELECT study_id, title, authors, year, abstract, doi, url,
               source, publication_date, journal, citation_count,
               pdf_url, stage, exclusion_reason
        FROM literature
        WHERE {where_sql}
        ORDER BY year DESC, citation_count DESC NULLS LAST
        LIMIT %s
    """

    cursor.execute(query, params)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convert to list of dicts
    papers = [dict(row) for row in results]

    return {
        "query": search_query,
        "filters": filters,
        "result_count": len(papers),
        "papers": papers
    }


@mcp.tool()
def store_extraction(study_id: str, extracted_data: Dict) -> dict:
    """
    Store extracted data from systematic review

    Args:
        study_id: Study identifier
        extracted_data: Structured extraction data (dict)

    Returns:
        Confirmation message
    """
    logger.info(f"Storing extraction for: {study_id}")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO extracted_data (study_id, data)
            VALUES (%s, %s)
            ON CONFLICT (study_id) DO UPDATE
            SET data = EXCLUDED.data,
                extracted_at = CURRENT_TIMESTAMP
        """, (study_id, Json(extracted_data)))

        conn.commit()
        cursor.close()
        conn.close()

        return {"status": "success", "study_id": study_id}

    except Exception as e:
        logger.error(f"Failed to store extraction: {e}")
        return {"status": "error", "study_id": study_id, "error": str(e)}


@mcp.tool()
def get_prisma_counts(project_name: str = "default") -> dict:
    """
    Get PRISMA flow diagram counts

    Args:
        project_name: Project identifier (default: "default")

    Returns:
        Dictionary with counts at each stage
    """
    logger.info(f"Fetching PRISMA counts for: {project_name}")

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Get actual counts from literature table
    cursor.execute("""
        SELECT
            COUNT(*) FILTER (WHERE stage = 'identified') as identified,
            COUNT(*) FILTER (WHERE stage = 'screened') as screened,
            COUNT(*) FILTER (WHERE stage = 'eligible') as eligible,
            COUNT(*) FILTER (WHERE stage = 'included') as included,
            COUNT(*) FILTER (WHERE stage = 'excluded') as excluded
        FROM literature
    """)

    result = cursor.fetchone()

    # Get exclusion reasons breakdown
    cursor.execute("""
        SELECT exclusion_reason, COUNT(*) as count
        FROM literature
        WHERE stage = 'excluded' AND exclusion_reason IS NOT NULL
        GROUP BY exclusion_reason
        ORDER BY count DESC
    """)

    exclusion_reasons = {row["exclusion_reason"]: row["count"]
                        for row in cursor.fetchall()}

    cursor.close()
    conn.close()

    counts = dict(result)
    counts["exclusion_reasons"] = exclusion_reasons

    return {
        "project": project_name,
        "counts": counts,
        "duplicates_removed": 0,  # Would need separate tracking
        "timestamp": datetime.now().isoformat()
    }


@mcp.tool()
def update_study_stage(study_id: str, new_stage: str,
                      exclusion_reason: Optional[str] = None) -> dict:
    """
    Update the stage of a study in the PRISMA workflow

    Args:
        study_id: Study identifier
        new_stage: New stage (identified, screened, eligible, included, excluded)
        exclusion_reason: Reason for exclusion (if stage=excluded)

    Returns:
        Confirmation message
    """
    logger.info(f"Updating {study_id} to stage: {new_stage}")

    valid_stages = ["identified", "screened", "eligible", "included", "excluded"]
    if new_stage not in valid_stages:
        return {"status": "error", "error": f"Invalid stage. Must be one of: {valid_stages}"}

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE literature
            SET stage = %s,
                exclusion_reason = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE study_id = %s
        """, (new_stage, exclusion_reason, study_id))

        if cursor.rowcount == 0:
            return {"status": "error", "error": "Study not found"}

        conn.commit()
        cursor.close()
        conn.close()

        return {"status": "success", "study_id": study_id, "new_stage": new_stage}

    except Exception as e:
        logger.error(f"Failed to update stage: {e}")
        return {"status": "error", "study_id": study_id, "error": str(e)}


@mcp.tool()
def get_database_stats() -> dict:
    """Get database statistics"""
    logger.info("Fetching database statistics")

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Count by source
    cursor.execute("""
        SELECT source, COUNT(*) as count
        FROM literature
        GROUP BY source
        ORDER BY count DESC
    """)
    by_source = {row["source"]: row["count"] for row in cursor.fetchall()}

    # Count by stage
    cursor.execute("""
        SELECT stage, COUNT(*) as count
        FROM literature
        GROUP BY stage
        ORDER BY count DESC
    """)
    by_stage = {row["stage"]: row["count"] for row in cursor.fetchall()}

    # Count by year
    cursor.execute("""
        SELECT year, COUNT(*) as count
        FROM literature
        WHERE year IS NOT NULL
        GROUP BY year
        ORDER BY year DESC
        LIMIT 10
    """)
    by_year = {row["year"]: row["count"] for row in cursor.fetchall()}

    # Total counts
    cursor.execute("SELECT COUNT(*) as total FROM literature")
    total_papers = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) as total FROM extracted_data")
    total_extractions = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return {
        "total_papers": total_papers,
        "total_extractions": total_extractions,
        "by_source": by_source,
        "by_stage": by_stage,
        "by_year": by_year
    }


# ============================================
# STARTUP
# ============================================

def startup():
    """Initialize database on server startup"""
    logger.info("Research Database MCP Server starting up")
    logger.info(f"Database: {DB_CONFIG['database']} at {DB_CONFIG['host']}:{DB_CONFIG['port']}")

    try:
        # Test connection
        conn = get_connection()
        conn.close()
        logger.info("Database connection successful")

        # Initialize schema
        initialize_schema()

    except Exception as e:
        logger.error(f"Startup failed: {e}")
        logger.error("Please ensure PostgreSQL is running and credentials are correct")
        sys.exit(1)


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    startup()
    mcp.run()
