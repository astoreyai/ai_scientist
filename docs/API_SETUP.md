# API Setup Guide - Research Assistant System

**Complete guide to configuring external research APIs**

---

## Overview

The Research Assistant System integrates with multiple academic APIs for literature search and citation management. Most APIs are **free** and require only an email address for higher rate limits.

**Summary:**

| API | Required | Cost | Setup Time | Rate Limit |
|-----|----------|------|------------|------------|
| OpenAlex | No | Free | 1 min | 10 req/sec |
| arXiv | No | Free | None | 1 req/3 sec |
| PubMed | No | Free | 2 min | 3-10 req/sec |
| Crossref | No | Free | None | ~1 req/sec |
| OpenCitations | No | Free | 5 min | Limited |

**None of these APIs require payment or complex registration.**

---

## OpenAlex API

**Purpose:** Comprehensive academic literature search (250M+ works)

### Features
- Largest open academic database
- Works, authors, institutions, concepts
- Citation data included
- Completely free, no authentication required

### Setup

**Option 1: No Setup (Basic)**
- Works immediately
- Rate limit: ~1 req/sec

**Option 2: Add Email (Recommended)**
- Rate limit: ~10 req/sec
- No registration needed

Add to MCP config (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "literature": {
      "env": {
        "OPENALEX_EMAIL": "your-email@example.com"
      }
    }
  }
}
```

### Rate Limits

- **Without email:** ~1 request/second
- **With email (polite pool):** ~10 requests/second
- **Hard limits:** None enforced
- **Recommended:** Always provide email

### Documentation

- Website: https://openalex.org/
- API Docs: https://docs.openalex.org/
- Python Library: `pyalex` (pip install pyalex)

### Example Usage

```python
from pyalex import Works

# Configure email (optional but recommended)
Works.config(email="your-email@example.com")

# Search for papers
results = Works().search("machine learning").get()
```

### Troubleshooting

**Issue:** Slow responses
- **Solution:** Add email to polite pool

**Issue:** Too many requests error
- **Solution:** Add delays between requests (automatically handled by our server)

---

## arXiv API

**Purpose:** Physics, computer science, and mathematics preprints

### Features
- Free, open access preprints
- Latest research before publication
- Full-text PDFs available
- No authentication required

### Setup

**No setup required** - arXiv API is completely open

### Rate Limits

- **Rate:** 1 request per 3 seconds
- **Automatic:** Python library handles rate limiting
- **Recommendation:** Use conservative batch sizes

### Documentation

- Website: https://arxiv.org/
- API Docs: https://info.arxiv.org/help/api/index.html
- Python Library: `arxiv` (pip install arxiv)

### Example Usage

```python
import arxiv

# Search for papers
search = arxiv.Search(
    query="machine learning",
    max_results=100,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

# Get results (rate limiting automatic)
for result in search.results():
    print(result.title, result.pdf_url)
```

### Troubleshooting

**Issue:** Rate limit errors
- **Solution:** Reduce batch size, add delays (handled automatically)

**Issue:** Missing papers
- **Solution:** arXiv only has preprints, not all published papers

---

## PubMed API (E-utilities)

**Purpose:** Biomedical literature (35M+ citations)

### Features
- NIH-maintained database
- Medical and life sciences
- Abstract and citation data
- Free for non-commercial use

### Setup

#### Step 1: Register for API Key (Optional but Recommended)

**Why:** Increases rate limit from 3 to 10 requests/second

1. **Create NCBI Account:**
   - Go to: https://www.ncbi.nlm.nih.gov/account/
   - Click "Register"
   - Verify email

2. **Generate API Key:**
   - Log in to NCBI account
   - Go to: https://www.ncbi.nlm.nih.gov/account/settings/
   - Click "Create an API Key"
   - Copy the key (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

3. **Add to Configuration:**

```json
{
  "mcpServers": {
    "literature": {
      "env": {
        "PUBMED_EMAIL": "your-email@example.com",
        "PUBMED_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

#### Step 2: Provide Email (Required)

Even without API key, email is **required** by PubMed terms of service:

```json
{
  "mcpServers": {
    "literature": {
      "env": {
        "PUBMED_EMAIL": "your-email@example.com"
      }
    }
  }
}
```

### Rate Limits

- **Without API key:** 3 requests/second
- **With API key:** 10 requests/second
- **Burst limit:** Short bursts allowed
- **Recommendation:** Always use API key for research projects

### Documentation

- Website: https://pubmed.ncbi.nlm.nih.gov/
- API Docs: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- Python Library: Biopython `Bio.Entrez` (pip install biopython)

### Example Usage

```python
from Bio import Entrez

# Configure (required)
Entrez.email = "your-email@example.com"
Entrez.api_key = "your-api-key"  # Optional

# Search PubMed
handle = Entrez.esearch(db="pubmed", term="machine learning", retmax=100)
record = Entrez.read(handle)
handle.close()

print(f"Found {record['Count']} papers")
```

### Troubleshooting

**Issue:** "Email parameter required"
- **Solution:** Set PUBMED_EMAIL environment variable

**Issue:** Rate limit exceeded (HTTP 429)
- **Solution:** Get API key or reduce request rate

**Issue:** No results found
- **Solution:** PubMed is biomedical focused, try OpenAlex for other fields

---

## Crossref API

**Purpose:** DOI resolution, metadata, retraction checking

### Features
- 140M+ scholarly records
- DOI-based metadata retrieval
- Retraction notices
- Citation data
- Completely free

### Setup

**No setup required** - Crossref API is open

**Optional:** Add user agent for better support

```json
{
  "mcpServers": {
    "citations": {
      "env": {
        "CROSSREF_EMAIL": "your-email@example.com"
      }
    }
  }
}
```

### Rate Limits

- **Without email:** ~1 request/second
- **With polite email:** Higher priority
- **Hard limit:** None enforced
- **Recommendation:** Add email in User-Agent

### Documentation

- Website: https://www.crossref.org/
- API Docs: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- Python Library: `habanero` (pip install habanero)

### Example Usage

```python
from habanero import Crossref

cr = Crossref()

# Get metadata for DOI
result = cr.works(ids="10.1038/nature12345")

# Check for retraction
if "update-to" in result["message"]:
    print("This paper has updates (possible retraction)")
```

### Troubleshooting

**Issue:** Slow responses
- **Solution:** Add email to request headers (automatic in our server)

**Issue:** DOI not found
- **Solution:** Verify DOI format (10.xxxx/xxxx)

---

## OpenCitations API

**Purpose:** Citation network data

### Features
- Citation counts
- Citation relationships
- Open citation data
- Free tier available

### Setup

**Option 1: No Setup (Limited)**
- Works immediately
- Lower rate limits

**Option 2: Request Token (Recommended for Heavy Use)**

1. **Visit:** https://opencitations.net/
2. **Request Access:** Fill out form
3. **Receive Token:** Via email (usually within 24 hours)
4. **Add to Config:**

```json
{
  "mcpServers": {
    "citations": {
      "env": {
        "OPENCITATIONS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Rate Limits

- **Without token:** Limited requests
- **With token:** Higher limits
- **Recommendation:** Request token if using extensively

### Documentation

- Website: https://opencitations.net/
- API Docs: https://opencitations.net/index/api/v1
- Python: Standard `requests` library

### Example Usage

```python
import requests

url = f"https://opencitations.net/index/api/v1/citations/{doi}"
headers = {"Authorization": f"Bearer {token}"}  # Optional

response = requests.get(url, headers=headers)
citations = response.json()
```

### Troubleshooting

**Issue:** Rate limited
- **Solution:** Request access token

**Issue:** DOI not found
- **Solution:** Not all DOIs are in OpenCitations (newer than Crossref)

---

## Summary: Recommended Setup

### Minimal Setup (5 minutes)

```json
{
  "mcpServers": {
    "literature": {
      "env": {
        "OPENALEX_EMAIL": "your-email@example.com",
        "PUBMED_EMAIL": "your-email@example.com"
      }
    }
  }
}
```

**Gets you:**
- 10x faster OpenAlex searches
- PubMed compliance
- All basic features

---

### Optimal Setup (10 minutes)

```json
{
  "mcpServers": {
    "literature": {
      "env": {
        "OPENALEX_EMAIL": "your-email@example.com",
        "PUBMED_EMAIL": "your-email@example.com",
        "PUBMED_API_KEY": "your-ncbi-api-key"
      }
    },
    "citations": {
      "env": {
        "OPENCITATIONS_TOKEN": "your-token"
      }
    }
  }
}
```

**Gets you:**
- Maximum rate limits (10 req/sec PubMed)
- Priority API access
- Full citation network data

---

## Testing API Setup

### Test OpenAlex

```bash
python3 << 'EOF'
from pyalex import Works
Works.config(email="your-email@example.com")
results = list(Works().search("machine learning").get()[:5])
print(f"✅ Found {len(results)} papers from OpenAlex")
EOF
```

### Test arXiv

```bash
python3 << 'EOF'
import arxiv
search = arxiv.Search(query="quantum computing", max_results=5)
results = list(search.results())
print(f"✅ Found {len(results)} papers from arXiv")
EOF
```

### Test PubMed

```bash
python3 << 'EOF'
from Bio import Entrez
Entrez.email = "your-email@example.com"
handle = Entrez.esearch(db="pubmed", term="cancer", retmax=5)
record = Entrez.read(handle)
handle.close()
print(f"✅ Found {record['Count']} papers in PubMed")
EOF
```

### Test Crossref

```bash
python3 << 'EOF'
from habanero import Crossref
cr = Crossref()
result = cr.works(ids="10.1038/nature")
print("✅ Crossref API working")
EOF
```

---

## Best Practices

### Rate Limiting

1. **Always provide email addresses**
2. **Use API keys when available**
3. **Batch requests where possible**
4. **Add delays between large batches**
5. **Handle 429 errors gracefully** (retry with backoff)

### Security

1. **Never commit API keys to git**
2. **Use environment variables**
3. **Rotate keys periodically**
4. **Use separate keys for development/production**

### Performance

1. **Cache frequently accessed data**
2. **Use database for persistent storage**
3. **Implement local deduplication**
4. **Monitor rate limit usage**

---

## Common Issues

### "403 Forbidden" Error

**Causes:**
- Missing email
- IP address blocked (rare)
- Terms of service violation

**Solutions:**
- Add email to configuration
- Check API documentation
- Contact API support if needed

### "429 Too Many Requests"

**Causes:**
- Rate limit exceeded
- Too many concurrent requests

**Solutions:**
- Add delays between requests
- Get API key for higher limits
- Use exponential backoff

### "No results found"

**Causes:**
- Query too specific
- Wrong database for topic
- API downtime

**Solutions:**
- Broaden search terms
- Try different API (OpenAlex is most comprehensive)
- Check API status pages

---

## Cost Analysis

### All APIs: $0/month

Every API used in this system is **completely free** for research use.

**Total Cost:** $0
**Credit Card Required:** No
**Subscription Needed:** No

### Fair Use Guidelines

While free, please:
- ✅ Use reasonable rate limits
- ✅ Cache results locally
- ✅ Provide email addresses
- ✅ Follow terms of service
- ❌ Don't abuse APIs
- ❌ Don't resell data
- ❌ Don't remove attribution

---

## Support

### API-Specific Support

- **OpenAlex:** https://groups.google.com/g/openalex-users
- **arXiv:** help@arxiv.org
- **PubMed:** https://support.ncbi.nlm.nih.gov/
- **Crossref:** support@crossref.org
- **OpenCitations:** contact@opencitations.net

### System Support

Check logs for API-related issues:
```bash
# Literature search logs
tail -f .claude/literature-search.log

# Citation management logs
tail -f .claude/citation-management.log
```

---

**API Setup Complete!** 🎉

Your system now has access to:
- 250M+ papers (OpenAlex)
- Latest preprints (arXiv)
- 35M+ biomedical citations (PubMed)
- Complete DOI metadata (Crossref)
- Citation networks (OpenCitations)

**All for $0/month.**
