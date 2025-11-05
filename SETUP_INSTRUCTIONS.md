# 🚀 Autonomous AI Research Scientist - Setup & Usage Guide

## 📦 Package Contents

This package contains a complete autonomous AI research scientist framework with:

- **Core Framework** (9 Python modules)
  - `react_core.py` - ReAct reasoning framework
  - `scientific_agents.py` - Specialized research agents
  - `skills_hooks.py` - Modular skills system
  - `scientific_workflow.py` - Research pipeline orchestrator
  - `human_interface.py` - Human-in-the-loop system
  - `llm_integration.py` - LLM and API connectors
  - `enhanced_literature.py` - Real literature APIs
  - `main.py` - Main entry point
  - `demo.py` - Demonstration script

- **Documentation**
  - `README.md` - Framework overview
  - `SETUP_INSTRUCTIONS.md` - This file
  - `IMPLEMENTATION_SUMMARY.md` - Technical details
  - `LITERATURE_INTEGRATION.md` - Literature API guide

- **Configuration**
  - `requirements.txt` - Python dependencies

## 🛠️ Installation

### Step 1: Extract the Package
```bash
unzip autonomous_research_scientist.zip
cd autonomous_research_scientist
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Keys (Optional but Recommended)

Create a `.env` file in the project directory:

```bash
# LLM APIs (choose one or more)
ANTHROPIC_API_KEY=your-anthropic-key-here
OPENAI_API_KEY=your-openai-key-here

# Optional: Semantic Scholar API key for higher rate limits
SEMANTIC_SCHOLAR_API_KEY=your-ss-key-here

# Your email for polite API access to OpenAlex
RESEARCHER_EMAIL=your-email@example.com
```

## 🎯 Quick Start

### 1. Run the Demo (No API Keys Required)
```bash
python demo.py
```

This runs a complete demonstration showing all capabilities with simulated data.

### 2. Basic Research (Mock Mode)
```bash
python main.py "Your research topic" --domain physics --demo
```

### 3. Research with Real Literature
```python
from enhanced_literature import ComprehensiveLiteratureReview
from main import AutonomousResearchScientist

# Initialize with real literature access
scientist = AutonomousResearchScientist()
reviewer = ComprehensiveLiteratureReview(email="your-email@example.com")

# Conduct research
results = scientist.conduct_research(
    topic="Novel approaches to quantum error correction",
    domain="quantum_computing"
)
```

## 📊 Usage Examples

### Example 1: Complete Autonomous Research
```python
from main import AutonomousResearchScientist

# Initialize
scientist = AutonomousResearchScientist({
    "enable_human_interaction": True,
    "max_compute_hours": 24.0
})

# Conduct research
results = scientist.conduct_research(
    topic="Machine learning for drug discovery",
    domain="computational_biology",
    output_path="research_results.json"
)

# Results include:
# - Generated hypotheses with scores
# - Literature review
# - Experimental designs
# - Validation results
# - Complete research report
```

### Example 2: Literature Review Only
```python
from enhanced_literature import ComprehensiveLiteratureReview

# Initialize reviewer
reviewer = ComprehensiveLiteratureReview(email="researcher@university.edu")

# Search across all sources
papers = reviewer.comprehensive_search(
    query="transformer models for protein folding",
    sources=["openalex", "arxiv", "semantic_scholar"],
    max_per_source=50
)

# Identify gaps
gaps = reviewer.identify_research_gaps(papers, "bioinformatics")

# Generate report
synthesis = reviewer.synthesize_findings(papers)
report = reviewer.generate_literature_report(papers, gaps, synthesis)
```

### Example 3: With Claude API
```python
from llm_integration import AnthropicClient
from main import AutonomousResearchScientist

# Use Claude as reasoning engine
claude = AnthropicClient(
    api_key="your-anthropic-api-key",
    model="claude-3-sonnet"
)

# Initialize scientist with Claude
scientist = AutonomousResearchScientist()
scientist.pipeline.llm_client = claude

# Now Claude powers all reasoning
results = scientist.conduct_research(
    topic="Your research question"
)
```

### Example 4: Human-in-the-Loop Mode
```python
from human_interface import HumanInTheLoopInterface, GuidanceProtocol

# Initialize interface
interface = HumanInTheLoopInterface(mode="interactive")
protocol = GuidanceProtocol(interface)

# System will request human input when needed
approved = protocol.request_experiment_approval(
    experiment_plan={"type": "computational", "cost": 5000},
    estimated_cost=5000
)

if approved:
    # Proceed with experiment
    pass
```

## 🔧 Configuration Options

### Research Configuration
```python
config = {
    # LLM Settings
    "llm_provider": "anthropic",  # or "openai", "local"
    "llm_model": "claude-3-sonnet",
    
    # Research Settings
    "max_iterations": 10,
    "max_compute_hours": 24.0,
    "enable_human_interaction": True,
    
    # Hypothesis Generation
    "initial_hypotheses": 50,
    "evolution_rounds": 3,
    "tournament_comparisons": 100,
    
    # Validation
    "confidence_threshold": 0.7,
    "min_validity_score": 0.6,
    
    # Literature Search
    "max_papers_per_source": 25,
    "literature_sources": ["openalex", "arxiv", "semantic_scholar"]
}

scientist = AutonomousResearchScientist(config)
```

## 📚 API Documentation

### Core Classes

#### `AutonomousResearchScientist`
Main interface for conducting research.

```python
scientist = AutonomousResearchScientist(config)
results = scientist.conduct_research(topic, domain, initial_context, output_path)
```

#### `ScientificResearchPipeline`
Orchestrates the 10-phase research workflow.

```python
pipeline = ScientificResearchPipeline(llm_client, enable_human_interaction=True)
results = pipeline.research(goal, domain, initial_context)
```

#### `ComprehensiveLiteratureReview`
Manages literature search across multiple databases.

```python
reviewer = ComprehensiveLiteratureReview(email="your-email")
papers = reviewer.comprehensive_search(query, sources, max_per_source)
gaps = reviewer.identify_research_gaps(papers, domain)
```

#### `ReActCycle`
Implements reasoning + acting pattern.

```python
react = ReActCycle(max_iterations=10)
react.register_skill("search", search_function)
result = react.iterate(goal, context)
```

## 🌐 Real Literature APIs

### OpenAlex (No Key Required)
```python
from enhanced_literature import OpenAlexClient

client = OpenAlexClient(email="your-email@example.com")
papers = client.search(
    query="quantum computing",
    filters={"publication_year": "2020-2024"},
    max_results=50
)
```

### arXiv (Rate Limited)
```python
from enhanced_literature import ArXivClient

client = ArXivClient()
papers = client.search(
    query="transformers",
    categories=["cs.LG", "cs.AI"],
    max_results=30
)
```

### Semantic Scholar (Optional Key)
```python
from enhanced_literature import SemanticScholarClient

client = SemanticScholarClient(api_key="optional-key")
papers = client.search(query="climate change", max_results=25)
```

## 🧪 Testing

### Run Unit Tests
```bash
pytest tests/
```

### Run Integration Tests
```bash
pytest tests/integration/ --slow
```

### Test Literature APIs
```python
python -c "from enhanced_literature import ComprehensiveLiteratureReview; \
          r = ComprehensiveLiteratureReview(); \
          papers = r.comprehensive_search('test query', max_per_source=5); \
          print(f'Found {len(papers)} papers')"
```

## 📊 Output Files

The system generates several output files:

- `research_results.json` - Complete research results
- `research_results_report.md` - Formatted research report  
- `literature_review_report.md` - Literature analysis
- `interaction_history.json` - Human interactions log
- `react_trace.json` - Complete reasoning trace

## 🚨 Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors
```bash
# Ensure all files are in the same directory
ls *.py  # Should show all 9 Python modules

# Reinstall requirements
pip install -r requirements.txt --upgrade
```

#### 2. API Rate Limits
```python
# Add delays between requests
import time
time.sleep(2)  # Wait 2 seconds between API calls

# Use email for polite access
reviewer = ComprehensiveLiteratureReview(email="your-email@example.com")
```

#### 3. Memory Issues with Large Searches
```python
# Reduce papers per source
papers = reviewer.comprehensive_search(
    query="your topic",
    max_per_source=10  # Reduce from default 20
)
```

#### 4. No API Keys Available
```bash
# Run in demo mode
python main.py "your topic" --demo

# Or use only free APIs (OpenAlex, arXiv)
sources = ["openalex", "arxiv"]  # Don't include APIs requiring keys
```

## 🎯 Best Practices

1. **Start Small**: Test with simple topics before complex research
2. **Use Caching**: Save results to avoid repeated API calls
3. **Monitor Costs**: LLM API calls can add up - use cheaper models for testing
4. **Review Outputs**: Always validate AI-generated hypotheses
5. **Iterate**: Use human feedback to improve results
6. **Document**: Keep logs of successful research patterns

## 📈 Performance Tips

### Optimize Literature Search
```python
# Use filters to reduce API calls
papers = reviewer.openalex.search(
    query="ml",
    filters={
        "publication_year": "2023-2024",
        "cited_by_count": ">10"
    },
    max_results=20
)
```

### Reduce LLM Costs
```python
# Use smaller models for testing
config = {
    "llm_model": "gpt-3.5-turbo",  # Cheaper than GPT-4
    "max_tokens": 1000  # Limit response length
}
```

### Enable Caching
```python
# Cache literature searches
import json

# Save results
with open("paper_cache.json", "w") as f:
    json.dump(papers, f)

# Load cached results
with open("paper_cache.json", "r") as f:
    papers = json.load(f)
```

## 🤝 Support & Contributions

### Getting Help
1. Check the documentation files
2. Review example code in `demo.py`
3. Look at test files for usage patterns

### Contributing
Contributions welcome! Areas of interest:
- Additional literature sources
- New agent types
- Domain-specific templates
- Visualization tools
- Web interface

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

This framework synthesizes research from:
- Together Computer (Open Data Scientist)
- Sakana AI (The AI Scientist)
- Google Research (AI Co-Scientist)
- OpenAlex, arXiv, Semantic Scholar APIs

---

## 🚀 Quick Command Reference

```bash
# Run demo
python demo.py

# Basic research
python main.py "research topic" --domain physics

# With output
python main.py "research topic" --output results.json

# No human interaction
python main.py "research topic" --no-human

# Set time limit
python main.py "research topic" --max-hours 12

# Test literature search
python -c "from enhanced_literature import *; demonstrate_literature_review()"
```

---

**Ready to conduct autonomous research!** Start with the demo, then try your own research questions.
