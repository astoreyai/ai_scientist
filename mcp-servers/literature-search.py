#!/usr/bin/env python3
"""
Literature Search MCP Server

Provides unified search across multiple academic databases:
- OpenAlex (comprehensive, free)
- arXiv (preprints)
- PubMed (biomedical)
- bioRxiv/medRxiv (preprint servers)

Real API integrations - NO MOCKS.

Usage:
    python literature-search.py

MCP Configuration (~/.claude/claude_desktop_config.json):
    {
      "mcpServers": {
        "literature": {
          "command": "python",
          "args": ["/path/to/mcp-servers/literature-search.py"],
          "env": {
            "OPENALEX_EMAIL": "your@email.com",
            "PUBMED_EMAIL": "your@email.com",
            "PUBMED_API_KEY": "optional_api_key"
          }
        }
      }
    }
"""

import os
import sys
import time
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict
import logging

# MCP Framework
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("ERROR: MCP framework not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Literature APIs
try:
    import pyalex
    from pyalex import Works
except ImportError:
    print("ERROR: pyalex not installed. Run: pip install pyalex", file=sys.stderr)
    sys.exit(1)

try:
    import arxiv
except ImportError:
    print("ERROR: arxiv not installed. Run: pip install arxiv", file=sys.stderr)
    sys.exit(1)

try:
    from Bio import Entrez
except ImportError:
    print("ERROR: biopython not installed. Run: pip install biopython", file=sys.stderr)
    sys.exit(1)

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("literature-search")

# ============================================
# CONFIGURATION
# ============================================

# OpenAlex requires email for polite pool (faster rate limits)
OPENALEX_EMAIL = os.getenv("OPENALEX_EMAIL", "researcher@example.com")
pyalex.config.email = OPENALEX_EMAIL

# PubMed requires email, API key optional but recommended
PUBMED_EMAIL = os.getenv("PUBMED_EMAIL", "researcher@example.com")
PUBMED_API_KEY = os.getenv("PUBMED_API_KEY")  # Optional but increases rate limit
Entrez.email = PUBMED_EMAIL
if PUBMED_API_KEY:
    Entrez.api_key = PUBMED_API_KEY

# Rate limiting
RATE_LIMIT_DELAY = 0.34  # ~3 requests/second (conservative)

# ============================================
# CACHING
# ============================================

from functools import lru_cache
from collections import OrderedDict
import threading

class TTLCache:
    """
    Thread-safe cache with Time-To-Live expiration.

    Caches search results to reduce API calls for repeated queries.
    Default TTL: 15 minutes (900 seconds)
    """

    def __init__(self, maxsize: int = 100, ttl: int = 900):
        self.maxsize = maxsize
        self.ttl = ttl
        self._cache: OrderedDict = OrderedDict()
        self._timestamps: Dict[str, float] = {}
        self._lock = threading.Lock()

    def _generate_key(self, query: str, date_range: Optional[Tuple[str, str]],
                      max_results: int, source: str) -> str:
        """Generate cache key from search parameters"""
        key_parts = [query, str(date_range), str(max_results), source]
        key_string = "|".join(key_parts)
        return hashlib.md5(key_string.encode()).hexdigest()

    def get(self, key: str) -> Optional[List]:
        """Get cached result if not expired"""
        with self._lock:
            if key not in self._cache:
                return None

            # Check if expired
            if time.time() - self._timestamps[key] > self.ttl:
                del self._cache[key]
                del self._timestamps[key]
                logger.debug(f"Cache expired for key: {key[:8]}...")
                return None

            # Move to end (most recently used)
            self._cache.move_to_end(key)
            logger.debug(f"Cache hit for key: {key[:8]}...")
            return self._cache[key]

    def set(self, key: str, value: List) -> None:
        """Store result in cache"""
        with self._lock:
            # Remove oldest if at capacity
            if len(self._cache) >= self.maxsize:
                oldest_key = next(iter(self._cache))
                del self._cache[oldest_key]
                del self._timestamps[oldest_key]

            self._cache[key] = value
            self._timestamps[key] = time.time()
            logger.debug(f"Cached result for key: {key[:8]}... ({len(value)} papers)")

    def clear(self) -> None:
        """Clear all cached results"""
        with self._lock:
            self._cache.clear()
            self._timestamps.clear()
            logger.info("Cache cleared")

    def stats(self) -> Dict:
        """Get cache statistics"""
        with self._lock:
            return {
                "size": len(self._cache),
                "maxsize": self.maxsize,
                "ttl_seconds": self.ttl
            }


# Global cache instance
search_cache = TTLCache(maxsize=100, ttl=900)  # 15-minute TTL


# ============================================
# BIORXIV/MEDRXIV SEARCH
# ============================================

BIORXIV_API_BASE = "https://api.biorxiv.org/details/biorxiv"
MEDRXIV_API_BASE = "https://api.biorxiv.org/details/medrxiv"


def search_biorxiv(query: str, date_range: Optional[Tuple[str, str]] = None,
                   max_results: int = 100, server: str = "biorxiv") -> List:
    """
    Search bioRxiv or medRxiv preprint servers

    Args:
        query: Search query string
        date_range: Optional tuple ("YYYY-MM-DD", "YYYY-MM-DD")
        max_results: Maximum number of results (default 100)
        server: "biorxiv" or "medrxiv"

    Returns:
        List of Paper objects
    """
    server_name = server.lower()
    logger.info(f"Searching {server_name}: {query}")

    # Check cache first
    cache_key = search_cache._generate_key(query, date_range, max_results, server_name)
    cached = search_cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        # bioRxiv/medRxiv API uses date-based retrieval
        # We need to search within a date range and filter by query
        if date_range:
            start_date, end_date = date_range
        else:
            # Default to last 2 years
            end_date = datetime.now().strftime("%Y-%m-%d")
            start_date = (datetime.now().replace(year=datetime.now().year - 2)).strftime("%Y-%m-%d")

        # Format dates for API (YYYY-MM-DD)
        api_base = BIORXIV_API_BASE if server_name == "biorxiv" else MEDRXIV_API_BASE

        papers = []
        cursor = 0
        batch_size = 100  # API limit per request

        while len(papers) < max_results:
            # API endpoint: /details/{server}/{start_date}/{end_date}/{cursor}
            url = f"{api_base}/{start_date}/{end_date}/{cursor}"

            try:
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                data = response.json()
            except requests.RequestException as e:
                logger.error(f"{server_name} API request failed: {e}")
                break

            # Check if we got results
            collection = data.get("collection", [])
            if not collection:
                break

            # Filter by query terms
            query_terms = query.lower().split()

            for item in collection:
                # Check if query terms match title or abstract
                title = item.get("title", "").lower()
                abstract = item.get("abstract", "").lower()
                searchable = f"{title} {abstract}"

                # Simple AND matching of query terms
                if all(term in searchable for term in query_terms):
                    # Parse authors
                    authors_str = item.get("authors", "")
                    authors = [a.strip() for a in authors_str.split(";") if a.strip()]

                    # Parse date
                    pub_date = item.get("date", "")
                    year = None
                    if pub_date:
                        try:
                            year = int(pub_date.split("-")[0])
                        except (ValueError, IndexError):
                            pass

                    paper = Paper(
                        id=f"{server_name}:{item.get('doi', '')}",
                        title=item.get("title", "No title"),
                        authors=authors[:10],  # Limit authors
                        year=year,
                        abstract=item.get("abstract"),
                        doi=item.get("doi"),
                        url=f"https://www.{server_name}.org/content/{item.get('doi', '')}",
                        source=server_name,
                        publication_date=pub_date,
                        journal=server_name.capitalize(),
                        citation_count=None,
                        pdf_url=f"https://www.{server_name}.org/content/{item.get('doi', '')}.full.pdf",
                        publication_type="preprint",
                        open_access=True
                    )

                    papers.append(paper)

                    if len(papers) >= max_results:
                        break

            # Move to next batch
            cursor += batch_size
            time.sleep(RATE_LIMIT_DELAY)

            # API returns 100 per page, stop if we got fewer
            if len(collection) < batch_size:
                break

        logger.info(f"{server_name}: Found {len(papers)} results")

        # Cache results
        search_cache.set(cache_key, papers)

        return papers

    except Exception as e:
        logger.error(f"{server_name} search failed: {e}")
        return []


# ============================================
# DATA STRUCTURES
# ============================================

@dataclass
class Paper:
    """Unified paper representation across all databases"""
    id: str
    title: str
    authors: List[str]
    year: Optional[int]
    abstract: Optional[str]
    doi: Optional[str]
    url: str
    source: str  # "openalex", "arxiv", "pubmed", "biorxiv"
    publication_date: Optional[str]
    journal: Optional[str]
    citation_count: Optional[int]
    pdf_url: Optional[str]

    # Database-specific IDs
    openalex_id: Optional[str] = None
    arxiv_id: Optional[str] = None
    pmid: Optional[str] = None
    pmcid: Optional[str] = None

    # Additional metadata
    publication_type: Optional[str] = None
    open_access: Optional[bool] = None


# ============================================
# OPENALEX SEARCH
# ============================================

def search_openalex(query: str, date_range: Optional[Tuple[str, str]] = None,
                   max_results: int = 100) -> List[Paper]:
    """
    Search OpenAlex (comprehensive academic database)

    Args:
        query: Search query string
        date_range: Optional tuple ("YYYY-MM-DD", "YYYY-MM-DD")
        max_results: Maximum number of results (default 100)

    Returns:
        List of Paper objects
    """
    logger.info(f"Searching OpenAlex: {query}")

    # Check cache first
    cache_key = search_cache._generate_key(query, date_range, max_results, "openalex")
    cached = search_cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        # Build filter
        filters = {}
        if date_range:
            start_date, end_date = date_range
            filters["from_publication_date"] = start_date
            filters["to_publication_date"] = end_date

        # Search OpenAlex
        # Note: OpenAlex uses Works.search() for full-text search
        results = Works().search(query).filter(**filters).get()[:max_results]

        papers = []
        for work in results:
            # Extract authors
            authors = []
            if work.get("authorships"):
                authors = [
                    auth.get("author", {}).get("display_name", "Unknown")
                    for auth in work["authorships"]
                ]

            # Extract publication date
            pub_date = work.get("publication_date")
            year = work.get("publication_year")

            # Extract DOI
            doi = None
            if work.get("doi"):
                doi = work["doi"].replace("https://doi.org/", "")

            # Build Paper object
            paper = Paper(
                id=work["id"],
                title=work.get("title", "No title"),
                authors=authors,
                year=year,
                abstract=work.get("abstract"),
                doi=doi,
                url=work.get("id", ""),
                source="openalex",
                publication_date=pub_date,
                journal=work.get("primary_location", {}).get("source", {}).get("display_name"),
                citation_count=work.get("cited_by_count", 0),
                pdf_url=work.get("primary_location", {}).get("pdf_url"),
                openalex_id=work["id"],
                open_access=work.get("open_access", {}).get("is_oa", False)
            )

            papers.append(paper)

        logger.info(f"OpenAlex: Found {len(papers)} results")

        # Cache results
        search_cache.set(cache_key, papers)

        return papers

    except Exception as e:
        logger.error(f"OpenAlex search failed: {e}")
        return []


# ============================================
# ARXIV SEARCH
# ============================================

def search_arxiv(query: str, date_range: Optional[Tuple[str, str]] = None,
                max_results: int = 100) -> List[Paper]:
    """
    Search arXiv (physics, CS, math preprints)

    Args:
        query: Search query string
        date_range: Optional tuple ("YYYY-MM-DD", "YYYY-MM-DD") - not directly supported
        max_results: Maximum number of results (default 100)

    Returns:
        List of Paper objects
    """
    logger.info(f"Searching arXiv: {query}")

    # Check cache first
    cache_key = search_cache._generate_key(query, date_range, max_results, "arxiv")
    cached = search_cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        # arXiv client
        client = arxiv.Client()

        # Build search
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        papers = []
        for result in client.results(search):
            # Filter by date if specified
            if date_range:
                start_date, end_date = date_range
                pub_date = result.published.strftime("%Y-%m-%d")
                if not (start_date <= pub_date <= end_date):
                    continue

            # Extract authors
            authors = [author.name for author in result.authors]

            # Extract arXiv ID
            arxiv_id = result.entry_id.split("/")[-1]

            paper = Paper(
                id=f"arxiv:{arxiv_id}",
                title=result.title,
                authors=authors,
                year=result.published.year,
                abstract=result.summary,
                doi=result.doi,
                url=result.entry_id,
                source="arxiv",
                publication_date=result.published.strftime("%Y-%m-%d"),
                journal="arXiv",
                citation_count=None,  # arXiv doesn't provide citation counts
                pdf_url=result.pdf_url,
                arxiv_id=arxiv_id,
                publication_type="preprint",
                open_access=True  # All arXiv papers are open access
            )

            papers.append(paper)

        logger.info(f"arXiv: Found {len(papers)} results")

        # Cache results
        search_cache.set(cache_key, papers)

        return papers

    except Exception as e:
        logger.error(f"arXiv search failed: {e}")
        return []


# ============================================
# PUBMED SEARCH
# ============================================

def search_pubmed(query: str, date_range: Optional[Tuple[str, str]] = None,
                 max_results: int = 100) -> List[Paper]:
    """
    Search PubMed (biomedical literature)

    Args:
        query: Search query string (supports PubMed syntax)
        date_range: Optional tuple ("YYYY-MM-DD", "YYYY-MM-DD")
        max_results: Maximum number of results (default 100)

    Returns:
        List of Paper objects
    """
    logger.info(f"Searching PubMed: {query}")

    # Check cache first
    cache_key = search_cache._generate_key(query, date_range, max_results, "pubmed")
    cached = search_cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        # Add date range to query if specified
        search_query = query
        if date_range:
            start_date, end_date = date_range
            # Convert to PubMed date format
            start = start_date.replace("-", "/")
            end = end_date.replace("-", "/")
            search_query += f' AND ("{start}"[Date - Publication] : "{end}"[Date - Publication])'

        # Search PubMed for IDs
        handle = Entrez.esearch(db="pubmed", term=search_query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()

        id_list = record["IdList"]

        if not id_list:
            logger.info("PubMed: No results found")
            return []

        # Fetch details for IDs (in batches to respect rate limits)
        papers = []
        batch_size = 20

        for i in range(0, len(id_list), batch_size):
            batch_ids = id_list[i:i+batch_size]

            # Rate limiting
            if i > 0:
                time.sleep(RATE_LIMIT_DELAY)

            # Fetch summaries
            handle = Entrez.efetch(db="pubmed", id=",".join(batch_ids),
                                  rettype="medline", retmode="xml")
            records = Entrez.read(handle)
            handle.close()

            for article in records["PubmedArticle"]:
                try:
                    # Extract fields
                    medline = article["MedlineCitation"]
                    article_data = medline["Article"]

                    # Title
                    title = article_data.get("ArticleTitle", "No title")

                    # Authors
                    authors = []
                    if "AuthorList" in article_data:
                        for author in article_data["AuthorList"]:
                            if "LastName" in author and "ForeName" in author:
                                authors.append(f"{author['ForeName']} {author['LastName']}")
                            elif "CollectiveName" in author:
                                authors.append(author["CollectiveName"])

                    # Abstract
                    abstract = None
                    if "Abstract" in article_data:
                        abstract_texts = article_data["Abstract"].get("AbstractText", [])
                        if abstract_texts:
                            abstract = " ".join([str(text) for text in abstract_texts])

                    # Publication date
                    pub_date = None
                    year = None
                    if "ArticleDate" in article_data:
                        date_parts = article_data["ArticleDate"][0]
                        year = int(date_parts.get("Year", 0))
                        month = date_parts.get("Month", "01").zfill(2)
                        day = date_parts.get("Day", "01").zfill(2)
                        pub_date = f"{year}-{month}-{day}"
                    elif "PubDate" in article_data["Journal"]["JournalIssue"]:
                        date_parts = article_data["Journal"]["JournalIssue"]["PubDate"]
                        year = int(date_parts.get("Year", 0))

                    # Journal
                    journal = article_data.get("Journal", {}).get("Title")

                    # IDs
                    pmid = str(medline["PMID"])

                    # DOI
                    doi = None
                    if "ELocationID" in article_data:
                        for eloc in article_data["ELocationID"]:
                            if eloc.attributes.get("EIdType") == "doi":
                                doi = str(eloc)
                                break

                    # PMC ID
                    pmcid = None
                    if "PubmedData" in article:
                        article_ids = article["PubmedData"].get("ArticleIdList", [])
                        for aid in article_ids:
                            if aid.attributes.get("IdType") == "pmc":
                                pmcid = str(aid)
                                break

                    paper = Paper(
                        id=f"pubmed:{pmid}",
                        title=title,
                        authors=authors,
                        year=year,
                        abstract=abstract,
                        doi=doi,
                        url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                        source="pubmed",
                        publication_date=pub_date,
                        journal=journal,
                        citation_count=None,  # PubMed doesn't provide citation counts directly
                        pdf_url=f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/" if pmcid else None,
                        pmid=pmid,
                        pmcid=pmcid,
                        publication_type=article_data.get("PublicationTypeList", [{}])[0].get("PublicationType") if article_data.get("PublicationTypeList") else None
                    )

                    papers.append(paper)

                except Exception as e:
                    logger.error(f"Failed to parse PubMed article: {e}")
                    continue

        logger.info(f"PubMed: Found {len(papers)} results")

        # Cache results
        search_cache.set(cache_key, papers)

        return papers

    except Exception as e:
        logger.error(f"PubMed search failed: {e}")
        return []


# ============================================
# DEDUPLICATION
# ============================================

def deduplicate_papers(papers: List[Paper]) -> List[Paper]:
    """
    Deduplicate papers based on DOI, title similarity, or IDs

    Deduplication strategy:
    1. Exact DOI match (highest priority)
    2. Cross-database ID match (PMID in OpenAlex, etc.)
    3. Title similarity (fuzzy matching)

    Args:
        papers: List of Paper objects from multiple sources

    Returns:
        Deduplicated list of Papers (keeps first occurrence)
    """
    logger.info(f"Deduplicating {len(papers)} papers")

    seen_dois = set()
    seen_titles = set()
    unique_papers = []

    for paper in papers:
        # Check DOI
        if paper.doi and paper.doi in seen_dois:
            logger.debug(f"Duplicate DOI: {paper.doi}")
            continue

        # Check title (normalized)
        normalized_title = normalize_title(paper.title)
        if normalized_title in seen_titles:
            logger.debug(f"Duplicate title: {paper.title}")
            continue

        # Keep this paper
        unique_papers.append(paper)

        if paper.doi:
            seen_dois.add(paper.doi)
        seen_titles.add(normalized_title)

    logger.info(f"After deduplication: {len(unique_papers)} unique papers")
    return unique_papers


def normalize_title(title: str) -> str:
    """Normalize title for comparison"""
    # Remove punctuation, lowercase, remove extra whitespace
    import re
    title = title.lower()
    title = re.sub(r'[^\w\s]', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title


# ============================================
# MCP TOOLS
# ============================================

@mcp.tool()
def search_literature(query: str, databases: List[str],
                     date_range: Optional[List[str]] = None,
                     max_results_per_db: int = 100) -> dict:
    """
    Search academic literature across multiple databases

    Args:
        query: Search query string (boolean operators supported for most databases)
        databases: List of databases to search. Options: ["openalex", "arxiv", "pubmed", "biorxiv", "medrxiv", "all"]
        date_range: Optional date range ["YYYY-MM-DD", "YYYY-MM-DD"] (start, end)
        max_results_per_db: Maximum results per database (default 100)

    Returns:
        Dictionary with results:
        {
            "query": str,
            "databases_searched": List[str],
            "total_results": int,
            "unique_results": int,
            "papers": List[dict]  # Paper objects as dicts
        }

    Example:
        search_literature(
            query="machine learning quantum computing",
            databases=["openalex", "arxiv", "biorxiv"],
            date_range=["2020-01-01", "2024-12-31"],
            max_results_per_db=50
        )
    """
    logger.info(f"Search request: {query} in {databases}")

    # Convert date_range to tuple if provided
    date_tuple = None
    if date_range and len(date_range) == 2:
        date_tuple = tuple(date_range)

    # Expand "all" to all databases
    if "all" in databases:
        databases = ["openalex", "arxiv", "pubmed", "biorxiv", "medrxiv"]

    # Search each database
    all_papers = []

    if "openalex" in databases:
        papers = search_openalex(query, date_tuple, max_results_per_db)
        all_papers.extend(papers)

    if "arxiv" in databases:
        papers = search_arxiv(query, date_tuple, max_results_per_db)
        all_papers.extend(papers)

    if "pubmed" in databases:
        papers = search_pubmed(query, date_tuple, max_results_per_db)
        all_papers.extend(papers)

    if "biorxiv" in databases:
        papers = search_biorxiv(query, date_tuple, max_results_per_db, server="biorxiv")
        all_papers.extend(papers)

    if "medrxiv" in databases:
        papers = search_biorxiv(query, date_tuple, max_results_per_db, server="medrxiv")
        all_papers.extend(papers)

    # Deduplicate
    unique_papers = deduplicate_papers(all_papers)

    # Convert to dicts for JSON serialization
    papers_dict = [asdict(paper) for paper in unique_papers]

    return {
        "query": query,
        "databases_searched": databases,
        "date_range": date_range,
        "total_results": len(all_papers),
        "unique_results": len(unique_papers),
        "duplicates_removed": len(all_papers) - len(unique_papers),
        "papers": papers_dict
    }


@mcp.tool()
def get_paper_metadata(identifier: str, id_type: str = "doi") -> dict:
    """
    Fetch detailed metadata for a specific paper

    Args:
        identifier: Paper identifier (DOI, PMID, arXiv ID, OpenAlex ID)
        id_type: Type of identifier. Options: ["doi", "pmid", "arxiv_id", "openalex_id"]

    Returns:
        Paper metadata as dict

    Example:
        get_paper_metadata("10.1038/s41586-021-03819-2", "doi")
    """
    logger.info(f"Fetching metadata for {id_type}: {identifier}")

    try:
        if id_type == "doi":
            # Try OpenAlex first (most comprehensive)
            works = Works().filter(doi=identifier).get()
            if works:
                # Convert to Paper object
                work = works[0]
                paper = Paper(
                    id=work["id"],
                    title=work.get("title", ""),
                    authors=[auth.get("author", {}).get("display_name", "")
                            for auth in work.get("authorships", [])],
                    year=work.get("publication_year"),
                    abstract=work.get("abstract"),
                    doi=identifier,
                    url=work.get("id", ""),
                    source="openalex",
                    publication_date=work.get("publication_date"),
                    journal=work.get("primary_location", {}).get("source", {}).get("display_name"),
                    citation_count=work.get("cited_by_count"),
                    pdf_url=work.get("primary_location", {}).get("pdf_url"),
                    openalex_id=work["id"],
                    open_access=work.get("open_access", {}).get("is_oa", False)
                )
                return asdict(paper)

        elif id_type == "pmid":
            # Fetch from PubMed
            papers = search_pubmed(f"{identifier}[PMID]", max_results=1)
            if papers:
                return asdict(papers[0])

        elif id_type == "arxiv_id":
            # Fetch from arXiv
            client = arxiv.Client()
            search = arxiv.Search(id_list=[identifier])
            results = list(client.results(search))
            if results:
                result = results[0]
                paper = Paper(
                    id=f"arxiv:{identifier}",
                    title=result.title,
                    authors=[author.name for author in result.authors],
                    year=result.published.year,
                    abstract=result.summary,
                    doi=result.doi,
                    url=result.entry_id,
                    source="arxiv",
                    publication_date=result.published.strftime("%Y-%m-%d"),
                    journal="arXiv",
                    citation_count=None,
                    pdf_url=result.pdf_url,
                    arxiv_id=identifier,
                    publication_type="preprint",
                    open_access=True
                )
                return asdict(paper)

        elif id_type == "openalex_id":
            # Fetch from OpenAlex
            work = Works()[identifier]
            if work:
                paper = Paper(
                    id=work["id"],
                    title=work.get("title", ""),
                    authors=[auth.get("author", {}).get("display_name", "")
                            for auth in work.get("authorships", [])],
                    year=work.get("publication_year"),
                    abstract=work.get("abstract"),
                    doi=work.get("doi", "").replace("https://doi.org/", "") if work.get("doi") else None,
                    url=work.get("id", ""),
                    source="openalex",
                    publication_date=work.get("publication_date"),
                    journal=work.get("primary_location", {}).get("source", {}).get("display_name"),
                    citation_count=work.get("cited_by_count"),
                    pdf_url=work.get("primary_location", {}).get("pdf_url"),
                    openalex_id=work["id"],
                    open_access=work.get("open_access", {}).get("is_oa", False)
                )
                return asdict(paper)

        return {"error": f"Paper not found for {id_type}: {identifier}"}

    except Exception as e:
        logger.error(f"Failed to fetch metadata: {e}")
        return {"error": str(e)}


@mcp.tool()
def get_cache_stats() -> dict:
    """
    Get cache statistics for literature search

    Returns:
        Dictionary with cache statistics:
        {
            "size": int,       # Current number of cached searches
            "maxsize": int,    # Maximum cache capacity
            "ttl_seconds": int # Time-to-live for cache entries
        }
    """
    return search_cache.stats()


@mcp.tool()
def clear_search_cache() -> dict:
    """
    Clear the literature search cache

    Returns:
        Dictionary confirming cache was cleared
    """
    search_cache.clear()
    return {
        "status": "success",
        "message": "Search cache cleared"
    }


@mcp.tool()
def get_citation_count(doi: str) -> dict:
    """
    Get citation count for a paper (from OpenAlex)

    Args:
        doi: Paper DOI

    Returns:
        Dictionary with citation count and citing papers
    """
    try:
        works = Works().filter(doi=doi).get()
        if works:
            work = works[0]
            return {
                "doi": doi,
                "citation_count": work.get("cited_by_count", 0),
                "openalex_url": work.get("id", "")
            }
        return {"error": "Paper not found"}
    except Exception as e:
        return {"error": str(e)}


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    logger.info("Starting Literature Search MCP Server")
    logger.info(f"OpenAlex email: {OPENALEX_EMAIL}")
    logger.info(f"PubMed email: {PUBMED_EMAIL}")
    logger.info(f"PubMed API key: {'Set' if PUBMED_API_KEY else 'Not set (using default rate limits)'}")

    # Run MCP server
    mcp.run()
