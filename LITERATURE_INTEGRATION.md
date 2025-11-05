# Enhanced Literature Review Integration Guide

## 🎯 Real API Integration for Autonomous Research

The enhanced literature review module (`enhanced_literature.py`) provides **real API access** to:

- **OpenAlex** - Open replacement for Microsoft Academic (178M+ papers)
- **OpenReview** - Peer reviews and conference papers
- **arXiv** - Preprints in physics, CS, math, etc.
- **Semantic Scholar** - 200M+ papers with citations
- **Web Search** - General academic web content

## 🔌 How to Use with the Research Framework

### 1. Replace Mock Literature Skills

In `skills_hooks.py`, replace the mock `LiteratureSearchSkill` with the real implementation:

```python
from enhanced_literature import ComprehensiveLiteratureReview, Paper

class RealLiteratureSearchSkill(BaseSkill):
    """Real literature search using actual APIs"""
    
    def __init__(self, email: Optional[str] = None):
        super().__init__(
            name="search_literature",
            description="Search real academic databases",
            category="literature"
        )
        self.reviewer = ComprehensiveLiteratureReview(email=email)
        
    def execute(self, 
                query: str, 
                max_results: int = 20,
                sources: Optional[List[str]] = None) -> SkillResult:
        """Search real literature databases"""
        
        try:
            # Use real APIs
            papers = self.reviewer.comprehensive_search(
                query=query,
                sources=sources or ["openalex", "arxiv", "semantic_scholar"],
                max_per_source=max_results
            )
            
            # Convert to expected format
            results = []
            for paper in papers:
                results.append({
                    "title": paper.title,
                    "authors": paper.authors,
                    "year": paper.year,
                    "abstract": paper.abstract,
                    "doi": paper.doi,
                    "citations": paper.citations,
                    "url": paper.url,
                    "pdf_url": paper.pdf_url,
                    "source": paper.source,
                    "relevance_score": paper.relevance_score
                })
                
            return SkillResult(
                success=True,
                data=results,
                metadata={
                    "total_found": len(papers),
                    "sources_searched": sources
                }
            )
            
        except Exception as e:
            return SkillResult(
                success=False,
                data=None,
                error=str(e)
            )
```

### 2. Update Scientific Workflow

In `scientific_workflow.py`, enhance the literature review phase:

```python
def _phase_literature_review(self) -> None:
    """Enhanced literature review with real APIs"""
    
    # Initialize real literature client
    from enhanced_literature import ComprehensiveLiteratureReview
    
    literature_client = ComprehensiveLiteratureReview(
        email="your-email@example.com"  # For polite API access
    )
    
    # Search across multiple databases
    papers = literature_client.comprehensive_search(
        query=self.state.research_goal,
        sources=["openalex", "arxiv", "openreview", "semantic_scholar"],
        max_per_source=25
    )
    
    # Store papers
    self.state.literature_cache["main_search"] = papers
    
    # Identify research gaps
    gaps = literature_client.identify_research_gaps(
        papers, 
        self.state.domain
    )
    
    for gap in gaps:
        self.state.add_knowledge_gap(gap)
        
    # Generate synthesis
    synthesis = literature_client.synthesize_findings(papers)
    
    # Generate literature report
    report = literature_client.generate_literature_report(
        papers, gaps, synthesis
    )
    
    # Store report
    self.state.literature_report = report
```

## 📊 API Configuration

### OpenAlex (Free, No Key Required)
```python
client = OpenAlexClient(email="your-email@example.com")

# Search with filters
papers = client.search(
    query="quantum computing",
    filters={
        "publication_year": "2020-2024",
        "open_access.is_oa": True,
        "cited_by_count": ">50"
    },
    max_results=50
)
```

### arXiv (Free, Rate Limited)
```python
client = ArXivClient()

# Search with categories
papers = client.search(
    query="transformer",
    categories=["cs.LG", "cs.AI"],
    sort_by="relevance",
    max_results=30
)
```

### OpenReview (Free, Conference Papers)
```python
client = OpenReviewClient()

# Search conference papers
papers = client.search(
    query="reinforcement learning",
    venue="NeurIPS",
    year=2024,
    max_results=20
)

# Get peer reviews
reviews = client.get_reviews(forum_id="paper_id")
```

### Semantic Scholar (Free, Optional API Key)
```python
client = SemanticScholarClient(api_key="optional-key")

# Search with specific fields
papers = client.search(
    query="climate change",
    fields=["title", "authors", "abstract", "citationCount"],
    max_results=25
)
```

## 🔄 Complete Integration Example

```python
from enhanced_literature import ComprehensiveLiteratureReview
from main import AutonomousResearchScientist

# Initialize enhanced scientist
scientist = AutonomousResearchScientist()

# Replace mock literature skill with real one
real_literature = RealLiteratureSearchSkill(
    email="research@university.edu"
)
scientist.pipeline.skill_registry.skills["search_literature"] = real_literature

# Conduct research with real literature
results = scientist.conduct_research(
    topic="Novel approaches to carbon capture using MOFs",
    domain="materials_science"
)

# Results now include:
# - Real papers from OpenAlex, arXiv, etc.
# - Actual citation counts
# - Real abstracts and DOIs
# - Peer review data from OpenReview
# - Comprehensive gap analysis
```

## 📈 Benefits of Real Literature Integration

### 1. **Comprehensive Coverage**
- Access to 200M+ papers across databases
- Multiple perspectives from different sources
- Peer review data from conferences

### 2. **Real-Time Updates**
- Latest preprints from arXiv
- Recent publications from OpenAlex
- Current citation counts

### 3. **Advanced Filtering**
- Filter by year, venue, citations
- Open access papers only
- Specific research categories

### 4. **Gap Analysis**
- Based on actual literature
- Identifies real research opportunities
- Temporal and methodological gaps

### 5. **Quality Metrics**
- Real citation counts
- Peer review scores
- Venue impact factors

## 🚀 Usage Patterns

### Pattern 1: Comprehensive Search
```python
# Search all sources for maximum coverage
papers = reviewer.comprehensive_search(
    query="your research topic",
    sources=["openalex", "arxiv", "openreview", "semantic_scholar"],
    max_per_source=50
)
```

### Pattern 2: Focused Search
```python
# Search specific source with filters
openalex_papers = reviewer.openalex.search(
    query="machine learning",
    filters={"publication_year": "2024"},
    max_results=100
)
```

### Pattern 3: Author Tracking
```python
# Get all papers by specific author
author_papers = reviewer.openalex.get_author_works(
    author_id="A2208157607",  # OpenAlex author ID
    max_results=50
)
```

### Pattern 4: Concept Hierarchy
```python
# Get concept hierarchy for better search
concept = reviewer.openalex.get_concept_hierarchy(
    "quantum computing"
)
# Returns concept ID and related concepts
```

## 📊 Research Workflow with Real Literature

```
1. INITIAL SEARCH
   ↓
   ComprehensiveLiteratureReview.comprehensive_search()
   → Returns 100+ real papers
   
2. DEDUPLICATION
   ↓
   Removes duplicates across sources
   → Unique papers with merged metadata
   
3. RANKING
   ↓
   Ranks by relevance + citations + recency
   → Top papers most relevant to research
   
4. GAP ANALYSIS
   ↓
   identify_research_gaps()
   → Real gaps based on actual literature
   
5. SYNTHESIS
   ↓
   synthesize_findings()
   → Statistics, venues, authors, methods
   
6. HYPOTHESIS GENERATION
   ↓
   Based on real gaps and findings
   → Novel research directions
   
7. VALIDATION
   ↓
   Check against latest papers
   → Ensure true novelty
```

## 🔒 Rate Limits and Best Practices

### API Rate Limits
- **OpenAlex**: No hard limit (be polite, use email)
- **arXiv**: 1 request/second (built-in delay)
- **Semantic Scholar**: 100 requests/5 minutes
- **OpenReview**: Reasonable use

### Best Practices
```python
# 1. Use email for polite access
reviewer = ComprehensiveLiteratureReview(
    email="your-email@example.com"
)

# 2. Cache results
papers = reviewer.comprehensive_search(query)
# Save for reuse
with open("papers_cache.json", "w") as f:
    json.dump([p.__dict__ for p in papers], f)

# 3. Batch searches
queries = ["topic1", "topic2", "topic3"]
all_papers = []
for query in queries:
    papers = reviewer.comprehensive_search(query)
    all_papers.extend(papers)
    time.sleep(2)  # Be polite

# 4. Use filters to reduce load
papers = reviewer.openalex.search(
    query="ml",
    filters={"publication_year": "2024"},
    max_results=20  # Limit results
)
```

## 📄 Output Examples

### Literature Report
```markdown
# Literature Review Report

**Date**: 2024-10-22
**Papers Analyzed**: 127

## Summary Statistics
- Year Range: 2019-2024
- Average Citations: 45.3
- Median Citations: 12.0

## Top Venues
- NeurIPS: 15 papers
- ICML: 12 papers
- Nature: 8 papers

## Research Gaps Identified
- Limited application of modern ML methods
- Lack of replication studies
- Limited real-world validation

## Top Cited Papers
1. **Attention Is All You Need**
   - Authors: Vaswani et al.
   - Year: 2017, Citations: 50000
   - Source: semantic_scholar
```

### Gap Analysis
```python
gaps = [
    "Limited recent research (last 2 years)",
    "Lack of classical statistical validation",
    "Limited interdisciplinary approaches",
    "Lack of replication studies",
    "Limited real-world validation",
    "Limited dataset diversity",
    "Weak theoretical foundations"
]
```

## 🎯 Integration Success Metrics

With real literature integration, the research framework can:

✅ **Access 200M+ real papers** instead of mock data
✅ **Get actual citation counts** for impact assessment  
✅ **Find genuine research gaps** based on real literature
✅ **Track latest preprints** from arXiv (updated daily)
✅ **Access peer reviews** from OpenReview conferences
✅ **Generate citations** with real DOIs and URLs
✅ **Validate novelty** against actual published work

## 🚦 Status

- ✅ OpenAlex integration (working, no key required)
- ✅ arXiv integration (working, rate limited)
- ✅ OpenReview integration (working)
- ✅ Semantic Scholar integration (working, optional key)
- ✅ Deduplication across sources
- ✅ Relevance ranking
- ✅ Gap analysis
- ✅ Report generation
- 🚧 Web search (needs API key for production)
- 🚧 Full-text PDF extraction
- 🚧 Citation network analysis

---

This enhanced literature review module transforms the autonomous research scientist from a demonstration into a **production-ready system** that can conduct real literature reviews, identify genuine research gaps, and generate novel hypotheses based on actual scientific literature.
