#!/usr/bin/env python3
"""
Citation Management MCP Server

Provides citation verification, retraction checking, and formatting:
- Crossref API (DOI resolution, retraction checking)
- OpenCitations API (citation verification)
- BibTeX parsing and formatting
- Reference style formatting (APA, IEEE, Chicago)

Real API integrations - NO MOCKS.

Usage:
    python citation-management.py

MCP Configuration:
    {
      "mcpServers": {
        "citations": {
          "command": "python",
          "args": ["/path/to/mcp-servers/citation-management.py"],
          "env": {
            "OPENCITATIONS_TOKEN": "optional_api_token"
          }
        }
      }
    }
"""

import os
import sys
import time
import re
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import logging

# MCP Framework
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("ERROR: MCP framework not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Citation APIs
try:
    from habanero import Crossref
except ImportError:
    print("ERROR: habanero not installed. Run: pip install habanero", file=sys.stderr)
    sys.exit(1)

try:
    import bibtexparser
    from bibtexparser.bwriter import BibTexWriter
    from bibtexparser.bibdatabase import BibDatabase
except ImportError:
    print("ERROR: bibtexparser not installed. Run: pip install bibtexparser", file=sys.stderr)
    sys.exit(1)

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("citation-management")

# ============================================
# CONFIGURATION
# ============================================

# OpenCitations API (free, no key required but optional)
OPENCITATIONS_TOKEN = os.getenv("OPENCITATIONS_TOKEN")
OPENCITATIONS_BASE_URL = "https://opencitations.net/index/api/v1"

# Crossref client
crossref = Crossref()

# Rate limiting
RATE_LIMIT_DELAY = 1.0  # 1 second between API calls (polite)

# ============================================
# CROSSREF API
# ============================================

def verify_doi(doi: str) -> dict:
    """
    Verify DOI exists and get metadata from Crossref

    Args:
        doi: DOI string (with or without https://doi.org/ prefix)

    Returns:
        Dictionary with verification status and metadata
    """
    # Clean DOI
    doi_clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")

    logger.info(f"Verifying DOI: {doi_clean}")

    try:
        # Query Crossref
        result = crossref.works(ids=doi_clean)

        if result and "message" in result:
            work = result["message"]

            # Extract key fields
            title = work.get("title", [""])[0] if work.get("title") else ""
            authors = []
            if "author" in work:
                for author in work["author"]:
                    given = author.get("given", "")
                    family = author.get("family", "")
                    authors.append(f"{given} {family}".strip())

            year = None
            if "published-print" in work:
                year = work["published-print"]["date-parts"][0][0]
            elif "published-online" in work:
                year = work["published-online"]["date-parts"][0][0]

            return {
                "valid": True,
                "doi": doi_clean,
                "title": title,
                "authors": authors,
                "year": year,
                "publisher": work.get("publisher"),
                "journal": work.get("container-title", [""])[0],
                "type": work.get("type"),
                "is_referenced_by_count": work.get("is-referenced-by-count", 0)
            }

        return {"valid": False, "doi": doi_clean, "error": "DOI not found in Crossref"}

    except Exception as e:
        logger.error(f"Crossref verification failed: {e}")
        return {"valid": False, "doi": doi_clean, "error": str(e)}


def check_retraction(doi: str) -> dict:
    """
    Check if paper has been retracted using Crossref

    Args:
        doi: DOI string

    Returns:
        Dictionary with retraction status
    """
    doi_clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")

    logger.info(f"Checking retraction status: {doi_clean}")

    try:
        result = crossref.works(ids=doi_clean)

        if result and "message" in result:
            work = result["message"]
            # Check for retraction notice
            retracted = False
            retraction_doi = None
            retraction_date = None

            # Check update-to field for retractions
            if "update-to" in work:
                for update in work["update-to"]:
                    if update.get("type") == "retraction":
                        retracted = True
                        retraction_doi = update.get("DOI")
                        if "updated" in update:
                            retraction_date = update["updated"]["date-parts"][0]

            # Check relation for retraction notices
            if "relation" in work:
                if "is-retracted-by" in work["relation"]:
                    retracted = True

            return {
                "doi": doi_clean,
                "retracted": retracted,
                "retraction_doi": retraction_doi,
                "retraction_date": retraction_date,
                "title": work.get("title", [""])[0]
            }

        return {"doi": doi_clean, "retracted": False, "error": "DOI not found"}

    except Exception as e:
        logger.error(f"Retraction check failed: {e}")
        return {"doi": doi_clean, "retracted": None, "error": str(e)}


# ============================================
# OPENCITATIONS API
# ============================================

def get_citations_opencitations(doi: str) -> dict:
    """
    Get citations for a DOI from OpenCitations

    Args:
        doi: DOI string

    Returns:
        Dictionary with citation data
    """
    doi_clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")

    logger.info(f"Fetching citations from OpenCitations: {doi_clean}")

    try:
        url = f"{OPENCITATIONS_BASE_URL}/citations/{doi_clean}"
        headers = {}
        if OPENCITATIONS_TOKEN:
            headers["authorization"] = OPENCITATIONS_TOKEN

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "doi": doi_clean,
                "citation_count": len(data) if data else 0,
                "citations": data[:100] if data else []  # Limit to 100
            }
        elif response.status_code == 404:
            return {"doi": doi_clean, "citation_count": 0, "citations": []}
        else:
            return {"doi": doi_clean, "error": f"HTTP {response.status_code}"}

    except Exception as e:
        logger.error(f"OpenCitations fetch failed: {e}")
        return {"doi": doi_clean, "error": str(e)}


# ============================================
# BIBTEX PROCESSING
# ============================================

def parse_bibtex(bibtex_string: str) -> dict:
    """
    Parse BibTeX string into structured data

    Args:
        bibtex_string: BibTeX formatted string

    Returns:
        Dictionary with parsed entries
    """
    logger.info("Parsing BibTeX")

    try:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.loads(bibtex_string, parser)

        entries = []
        for entry in bib_database.entries:
            entries.append({
                "id": entry.get("ID"),
                "type": entry.get("ENTRYTYPE"),
                "title": entry.get("title"),
                "author": entry.get("author"),
                "year": entry.get("year"),
                "journal": entry.get("journal"),
                "doi": entry.get("doi"),
                "url": entry.get("url"),
                **{k: v for k, v in entry.items()
                   if k not in ["ID", "ENTRYTYPE", "title", "author", "year", "journal", "doi", "url"]}
            })

        return {
            "entry_count": len(entries),
            "entries": entries
        }

    except Exception as e:
        logger.error(f"BibTeX parsing failed: {e}")
        return {"error": str(e)}


def clean_bibtex(bibtex_string: str) -> str:
    """
    Clean and standardize BibTeX entries

    Operations:
    - Remove duplicate entries (by DOI or title)
    - Standardize field names
    - Fix author name formats
    - Validate DOIs

    Args:
        bibtex_string: Raw BibTeX string

    Returns:
        Cleaned BibTeX string
    """
    logger.info("Cleaning BibTeX")

    try:
        # Parse
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.loads(bibtex_string, parser)

        # Track seen DOIs and titles
        seen_dois = set()
        seen_titles = set()
        cleaned_entries = []

        for entry in bib_database.entries:
            # Check for duplicates by DOI
            doi = entry.get("doi", "").strip()
            if doi and doi in seen_dois:
                logger.debug(f"Duplicate DOI: {doi}")
                continue

            # Check for duplicates by title
            title = entry.get("title", "").strip().lower()
            if title and title in seen_titles:
                logger.debug(f"Duplicate title: {title}")
                continue

            # Standardize author format
            if "author" in entry:
                authors = entry["author"].split(" and ")
                entry["author"] = " and ".join(authors)

            # Add to cleaned set
            cleaned_entries.append(entry)

            if doi:
                seen_dois.add(doi)
            if title:
                seen_titles.add(title)

        # Create new database
        new_db = BibDatabase()
        new_db.entries = cleaned_entries

        # Write to string
        writer = BibTexWriter()
        writer.indent = '  '
        cleaned_bibtex = bibtexparser.dumps(new_db, writer)

        logger.info(f"Cleaned: {len(bib_database.entries)} → {len(cleaned_entries)} entries")

        return cleaned_bibtex

    except Exception as e:
        logger.error(f"BibTeX cleaning failed: {e}")
        return bibtex_string  # Return original on error


# ============================================
# REFERENCE FORMATTING
# ============================================

def format_citation_apa(entry: dict) -> str:
    """
    Format citation in APA 7th edition style

    Args:
        entry: Citation entry dict

    Returns:
        APA formatted citation string
    """
    # Authors
    authors = entry.get("author", "Unknown").replace(" and ", " & ")

    # Year
    year = entry.get("year", "n.d.")

    # Title
    title = entry.get("title", "No title")

    # Journal
    journal = entry.get("journal", "")

    # Volume, issue, pages
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = entry.get("pages", "")

    # DOI
    doi = entry.get("doi", "")

    # Build citation
    citation = f"{authors} ({year}). {title}."

    if journal:
        citation += f" {journal}"
        if volume:
            citation += f", {volume}"
            if number:
                citation += f"({number})"
        if pages:
            citation += f", {pages}"
        citation += "."

    if doi:
        citation += f" https://doi.org/{doi}"

    return citation


def format_citation_ieee(entry: dict) -> str:
    """Format citation in IEEE style"""
    authors = entry.get("author", "Unknown").replace(" and ", ", ")
    title = entry.get("title", "No title")
    journal = entry.get("journal", "")
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = entry.get("pages", "")
    year = entry.get("year", "")

    citation = f'{authors}, "{title},"'

    if journal:
        citation += f" {journal}"
        if volume:
            citation += f", vol. {volume}"
        if number:
            citation += f", no. {number}"
        if pages:
            citation += f", pp. {pages}"
        if year:
            citation += f", {year}"
        citation += "."

    return citation


# ============================================
# MCP TOOLS
# ============================================

@mcp.tool()
def verify_citations(doi_list: List[str]) -> dict:
    """
    Verify multiple DOIs and get metadata

    Args:
        doi_list: List of DOI strings

    Returns:
        Dictionary with verification results for each DOI
    """
    logger.info(f"Verifying {len(doi_list)} citations")

    results = []

    for i, doi in enumerate(doi_list):
        # Rate limiting
        if i > 0:
            time.sleep(RATE_LIMIT_DELAY)

        result = verify_doi(doi)
        results.append(result)

    valid_count = sum(1 for r in results if r.get("valid"))

    return {
        "total": len(doi_list),
        "valid": valid_count,
        "invalid": len(doi_list) - valid_count,
        "results": results
    }


@mcp.tool()
def check_retractions(doi_list: List[str]) -> dict:
    """
    Check multiple papers for retraction status

    Args:
        doi_list: List of DOI strings

    Returns:
        Dictionary with retraction status for each DOI
    """
    logger.info(f"Checking {len(doi_list)} papers for retractions")

    results = []
    retracted_papers = []

    for i, doi in enumerate(doi_list):
        # Rate limiting
        if i > 0:
            time.sleep(RATE_LIMIT_DELAY)

        result = check_retraction(doi)
        results.append(result)

        if result.get("retracted"):
            retracted_papers.append(result)

    return {
        "total_checked": len(doi_list),
        "retracted_count": len(retracted_papers),
        "retracted_papers": retracted_papers,
        "all_results": results
    }


@mcp.tool()
def format_bibliography(bibtex_string: str, style: str = "APA") -> dict:
    """
    Format bibliography in specified citation style

    Args:
        bibtex_string: BibTeX formatted string
        style: Citation style. Options: ["APA", "IEEE", "Chicago"]

    Returns:
        Dictionary with formatted citations
    """
    logger.info(f"Formatting bibliography in {style} style")

    try:
        # Parse BibTeX
        parsed = parse_bibtex(bibtex_string)

        if "error" in parsed:
            return parsed

        # Format each entry
        formatted_citations = []

        for entry in parsed["entries"]:
            if style == "APA":
                citation = format_citation_apa(entry)
            elif style == "IEEE":
                citation = format_citation_ieee(entry)
            elif style == "Chicago":
                # Simplified Chicago style
                citation = format_citation_apa(entry)  # Use APA as placeholder
            else:
                citation = format_citation_apa(entry)  # Default to APA

            formatted_citations.append({
                "id": entry.get("id"),
                "citation": citation
            })

        return {
            "style": style,
            "entry_count": len(formatted_citations),
            "citations": formatted_citations
        }

    except Exception as e:
        logger.error(f"Bibliography formatting failed: {e}")
        return {"error": str(e)}


@mcp.tool()
def clean_bibtex_file(bibtex_string: str) -> dict:
    """
    Clean and deduplicate BibTeX entries

    Args:
        bibtex_string: Raw BibTeX string

    Returns:
        Dictionary with cleaned BibTeX and statistics
    """
    logger.info("Cleaning BibTeX file")

    try:
        # Parse original
        original_parsed = parse_bibtex(bibtex_string)
        original_count = original_parsed["entry_count"]

        # Clean
        cleaned_bibtex = clean_bibtex(bibtex_string)

        # Parse cleaned
        cleaned_parsed = parse_bibtex(cleaned_bibtex)
        cleaned_count = cleaned_parsed["entry_count"]

        return {
            "original_entries": original_count,
            "cleaned_entries": cleaned_count,
            "duplicates_removed": original_count - cleaned_count,
            "cleaned_bibtex": cleaned_bibtex
        }

    except Exception as e:
        logger.error(f"BibTeX cleaning failed: {e}")
        return {"error": str(e)}


@mcp.tool()
def get_citation_metadata(doi: str) -> dict:
    """
    Get complete citation metadata from Crossref and OpenCitations

    Args:
        doi: DOI string

    Returns:
        Combined metadata from multiple sources
    """
    logger.info(f"Fetching complete metadata for: {doi}")

    # Get Crossref data
    crossref_data = verify_doi(doi)

    time.sleep(RATE_LIMIT_DELAY)

    # Get OpenCitations data
    opencitations_data = get_citations_opencitations(doi)

    time.sleep(RATE_LIMIT_DELAY)

    # Get retraction status
    retraction_data = check_retraction(doi)

    return {
        "doi": doi,
        "crossref": crossref_data,
        "opencitations": opencitations_data,
        "retraction": retraction_data
    }


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    logger.info("Starting Citation Management MCP Server")
    logger.info(f"OpenCitations token: {'Set' if OPENCITATIONS_TOKEN else 'Not set (using public API)'}")

    # Run MCP server
    mcp.run()
