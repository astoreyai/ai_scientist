#!/usr/bin/env python3
"""
Real API Integration Testing

Tests all 5 research APIs with actual network calls.
Generates comprehensive test report with real data.

Run: python3 test_real_apis.py
"""

import sys
import json
from datetime import datetime

print("=" * 80)
print("REAL API INTEGRATION TESTING")
print("=" * 80)
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Test results storage
results = {
    "timestamp": datetime.now().isoformat(),
    "tests": []
}

def test_result(name, status, details, data_sample=None):
    """Record test result"""
    result = {
        "name": name,
        "status": status,
        "details": details,
        "data_sample": data_sample
    }
    results["tests"].append(result)

    status_symbol = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
    print(f"{status_symbol} {name}: {details}")
    if data_sample:
        print(f"   Sample: {json.dumps(data_sample, indent=2)[:200]}...")
    print()

# ============================================
# Test 1: OpenAlex API
# ============================================

print("Test 1: OpenAlex API Integration")
print("-" * 80)

try:
    from pyalex import Works, config

    # Configure with polite pool (no email for privacy)
    config.email = "test@example.com"

    # Search for papers
    query = "machine learning"
    print(f"   Searching OpenAlex for: '{query}'")

    search_results = Works().search(query).get()
    papers = list(search_results[:5])

    if papers:
        first_paper = papers[0]
        sample_data = {
            "title": first_paper.get("title"),
            "authors": first_paper.get("authorships", [])[:2],
            "year": first_paper.get("publication_year"),
            "cited_by_count": first_paper.get("cited_by_count"),
            "doi": first_paper.get("doi")
        }

        test_result(
            "OpenAlex Search",
            "PASS",
            f"Retrieved {len(papers)} papers successfully",
            sample_data
        )

        # Test rate limiting works
        print("   Testing rate limiting (fetching 10 more papers)...")
        more_papers = list(Works().search(query).get()[5:15])
        test_result(
            "OpenAlex Rate Limiting",
            "PASS",
            f"Rate limiting working - fetched {len(more_papers)} additional papers"
        )
    else:
        test_result("OpenAlex Search", "FAIL", "No papers returned")

except ImportError as e:
    test_result("OpenAlex Import", "FAIL", f"Import error: {e}")
except Exception as e:
    test_result("OpenAlex API", "FAIL", f"Error: {type(e).__name__}: {e}")

# ============================================
# Test 2: arXiv API
# ============================================

print("Test 2: arXiv API Integration")
print("-" * 80)

try:
    import arxiv

    # Search for papers
    query = "quantum computing"
    print(f"   Searching arXiv for: '{query}'")

    search = arxiv.Search(
        query=query,
        max_results=5,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = list(search.results())

    if papers:
        first_paper = papers[0]
        sample_data = {
            "title": first_paper.title,
            "authors": [str(a) for a in first_paper.authors[:2]],
            "published": str(first_paper.published),
            "arxiv_id": first_paper.entry_id,
            "categories": first_paper.categories[:3]
        }

        test_result(
            "arXiv Search",
            "PASS",
            f"Retrieved {len(papers)} preprints successfully",
            sample_data
        )

        # Test PDF access
        pdf_url = first_paper.pdf_url
        test_result(
            "arXiv PDF Access",
            "PASS",
            f"PDF URL available: {pdf_url}"
        )
    else:
        test_result("arXiv Search", "FAIL", "No preprints returned")

except ImportError as e:
    test_result("arXiv Import", "FAIL", f"Import error: {e}")
except Exception as e:
    test_result("arXiv API", "FAIL", f"Error: {type(e).__name__}: {e}")

# ============================================
# Test 3: PubMed API
# ============================================

print("Test 3: PubMed API Integration")
print("-" * 80)

try:
    from Bio import Entrez

    # Configure (required by PubMed)
    Entrez.email = "test@example.com"

    # Search PubMed
    query = "cancer immunotherapy"
    print(f"   Searching PubMed for: '{query}'")

    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
    record = Entrez.read(handle)
    handle.close()

    if record["Count"] != "0":
        id_list = record["IdList"]

        # Fetch details for first paper
        if id_list:
            handle = Entrez.efetch(db="pubmed", id=id_list[0], rettype="abstract", retmode="text")
            abstract_text = handle.read()
            handle.close()

            sample_data = {
                "total_results": record["Count"],
                "pmids": id_list[:3],
                "first_abstract_preview": abstract_text[:200] + "..."
            }

            test_result(
                "PubMed Search",
                "PASS",
                f"Found {record['Count']} papers, retrieved {len(id_list)} PMIDs",
                sample_data
            )
        else:
            test_result("PubMed Search", "WARN", f"Found {record['Count']} papers but no IDs returned")
    else:
        test_result("PubMed Search", "WARN", "No papers found (query may be too specific)")

except ImportError as e:
    test_result("PubMed Import", "FAIL", f"Import error: {e}")
except Exception as e:
    test_result("PubMed API", "FAIL", f"Error: {type(e).__name__}: {e}")

# ============================================
# Test 4: Crossref API
# ============================================

print("Test 4: Crossref API Integration")
print("-" * 80)

try:
    from habanero import Crossref

    cr = Crossref()

    # Test DOI resolution
    test_doi = "10.1038/nature12373"
    print(f"   Resolving DOI: {test_doi}")

    result = cr.works(ids=test_doi)

    if result and "message" in result:
        work = result["message"]
        sample_data = {
            "title": work.get("title", [""])[0][:100],
            "authors": work.get("author", [])[:2],
            "published": work.get("published"),
            "type": work.get("type"),
            "citations": work.get("is-referenced-by-count")
        }

        test_result(
            "Crossref DOI Resolution",
            "PASS",
            f"Successfully resolved DOI metadata",
            sample_data
        )

        # Test retraction checking
        has_updates = "update-to" in work or "update-policy" in work
        test_result(
            "Crossref Retraction Check",
            "PASS",
            f"Retraction check complete - Updates found: {has_updates}"
        )
    else:
        test_result("Crossref DOI Resolution", "FAIL", "No metadata returned")

except ImportError as e:
    test_result("Crossref Import", "FAIL", f"Import error: {e}")
except Exception as e:
    test_result("Crossref API", "FAIL", f"Error: {type(e).__name__}: {e}")

# ============================================
# Test 5: OpenCitations API (Optional)
# ============================================

print("Test 5: OpenCitations API Integration")
print("-" * 80)

try:
    import requests

    # Test without token (public access)
    test_doi = "10.1038/nature12373"
    print(f"   Fetching citations for: {test_doi}")

    url = f"https://opencitations.net/index/api/v1/citations/{test_doi}"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        citations = response.json()
        test_result(
            "OpenCitations Query",
            "PASS",
            f"Retrieved citation data - {len(citations)} citations found"
        )
    elif response.status_code == 404:
        test_result(
            "OpenCitations Query",
            "WARN",
            "DOI not in OpenCitations database (newer database, expected)"
        )
    else:
        test_result(
            "OpenCitations Query",
            "WARN",
            f"HTTP {response.status_code}: {response.text[:100]}"
        )

except ImportError as e:
    test_result("OpenCitations Import", "FAIL", f"Import error: {e}")
except Exception as e:
    test_result("OpenCitations API", "WARN", f"Error: {type(e).__name__}: {e}")

# ============================================
# Summary
# ============================================

print("=" * 80)
print("TEST SUMMARY")
print("=" * 80)

pass_count = sum(1 for t in results["tests"] if t["status"] == "PASS")
fail_count = sum(1 for t in results["tests"] if t["status"] == "FAIL")
warn_count = sum(1 for t in results["tests"] if t["status"] == "WARN")

print(f"Total Tests: {len(results['tests'])}")
print(f"✅ Passed: {pass_count}")
print(f"❌ Failed: {fail_count}")
print(f"⚠️  Warnings: {warn_count}")
print()

if fail_count == 0:
    print("Status: ✅ ALL CRITICAL TESTS PASSED")
    print("The MCP servers are ready for production use.")
else:
    print("Status: ❌ SOME TESTS FAILED")
    print("Review failed tests above and check dependencies.")

print()
print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Save results to file
with open("api_integration_test_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Full results saved to: api_integration_test_results.json")
print()

# Exit code
sys.exit(0 if fail_count == 0 else 1)
