# Production Research Assistant System

## System Configuration

**Project:** AI Research Assistant
**Architecture:** Claude Code with MCP servers, hooks, and specialized agents
**Current Phase:** Phase 1 - Foundation & Cleanup
**See:** `PROJECT_STATUS.md` for detailed status

---

## Current Mode: ASSISTANT

### Mode Description

The system operates in two modes that can be switched dynamically:

**ASSISTANT MODE (Current):**
- Human-guided research workflow support
- Interactive hypothesis refinement
- Human-led literature screening with AI assistance
- Collaborative experimental design
- Explanation of all decisions
- Wait for human approval at decision gates
- PhD dissertation assistance focus

**AUTONOMOUS MODE:**
- Full ReAct-style research generation
- Auto-progress through workflow phases
- Generate hypotheses without human approval
- Automated literature screening (inter-rater simulation)
- Self-reflection loops for hypothesis refinement
- Automatic experiment execution and validation
- Minimal human intervention

### Mode Switching

To switch modes, update this section header above and adjust behaviors below.

---

## Research Workflow Phases

### 11-Phase State Machine

1. **Problem Formulation** → FINER criteria validation
2. **Literature Review** → PRISMA 2020 systematic review
3. **Gap Analysis** → Pattern identification, prioritization
4. **Hypothesis Formation** → Tree-of-Thought generation
5. **Experimental Design** → Power analysis, NIH rigor standards
6. **IRB Approval** → Human-guided ethics review
7. **Data Collection** → Real-time validation hooks
8. **Analysis** → Reproducible statistical analysis
9. **Interpretation** → Effect sizes, confidence intervals
10. **Writing** → CONSORT/PRISMA compliant manuscripts
11. **Publication** → DOI generation, archival

### Decision Gates

Each phase has validation criteria that must pass before proceeding. In ASSISTANT mode, wait for human approval. In AUTONOMOUS mode, proceed automatically if validation passes.

---

## Agent Instructions

### When to Use Specialized Agents

Claude Code should delegate to specialized agents for complex, multi-step tasks:

**Use `literature-reviewer` agent when:**
- Conducting PRISMA 2020 systematic reviews
- Multi-database literature searches
- Screening and data extraction
- Risk of bias assessment
- Inter-rater reliability calculations

**Use `experiment-designer` agent when:**
- Designing experiments requiring NIH rigor standards
- Conducting power analysis
- Creating randomization protocols
- Developing pre-registration documents
- FAIR data management plans

**Use `data-analyst` agent when:**
- Performing statistical analyses
- Testing assumptions (normality, homogeneity)
- Calculating effect sizes and confidence intervals
- Running sensitivity analyses
- Reproducibility validation

**Use `hypothesis-generator` agent when (AUTONOMOUS mode):**
- Generating novel research hypotheses
- Tree-of-Thought reasoning
- Hypothesis evolution and refinement
- Falsifiability checking

**Use `citation-manager` agent when:**
- Managing BibTeX/Zotero citations
- Verifying citations via OpenCitations API
- Checking for retractions
- Formatting references

---

## MCP Server Usage

### Available Servers

**Literature Search MCP** (`literature`)
- `search_literature(query, databases)` - Search Semantic Scholar, arXiv, PubMed
- `deduplicate_results(results)` - Remove duplicate papers
- `get_paper_metadata(doi)` - Fetch complete paper metadata

**Citation Management MCP** (`citations`)
- `verify_citations(doi_list)` - Verify via OpenCitations API
- `check_retractions(doi_list)` - Check Crossref for retractions
- `format_bibliography(papers, style)` - Format citations (APA, IEEE, etc.)

**Research Database MCP** (`research_db`)
- `store_extraction(study_id, data)` - Store systematic review data
- `query_literature(search_query, filters)` - Full-text search
- `get_prisma_counts()` - Get PRISMA flow diagram counts

**Memory Keeper MCP** (`memory_keeper`)
- Persistent context across sessions
- Automatically stores key research decisions
- Retrieves relevant prior context

**Standard MCP Servers:**
- `filesystem` - Secure file operations
- `git` - Version control operations
- `fetch` - Web content retrieval

### Usage Guidelines

1. **Always use real APIs** - No mocks or placeholders
2. **Handle rate limits** - Implement backoff for API calls
3. **Validate responses** - Check for errors before proceeding
4. **Log all operations** - PostToolUse hook handles this automatically

---

## Hook Behaviors

### SessionStart Hook

**Loads:**
- Research protocols (PRISMA, CONSORT, NIH guidelines)
- Current mode configuration (ASSISTANT/AUTONOMOUS)
- Active research phase and state
- Memory from previous sessions

### PreToolUse Hook

**Validates:**
- Bash commands for security (blocks dangerous operations)
- File paths for safety (prevents traversal, system file access)
- API rate limits before external calls

**Blocks:**
- `rm -rf /`, `dd if=/dev/zero`, `chmod -R 777 /`
- Path traversal attempts (`../`, `/etc/`)
- Unsafe code execution

### PostToolUse Hook

**Logs:**
- All tool invocations to SQLite database
- Tool inputs, outputs, timestamps
- Success/failure status

**Auto-tracks:**
- Large files (>10MB) with DVC
- Adds to version control automatically

### PreCompact Hook

**Backs up:**
- Current research state (hypotheses, phase, decisions)
- Tool log database
- Memory files (CLAUDE.md, tool_log.db)
- Timestamp-stamped JSON backups

### Stop Hook

**Validates:**
- All phase deliverables completed
- Quality gates passed
- Required files generated

**Archives:**
- Research artifacts
- Generates DOIs if publication phase
- Tags git releases

---

## Quality Standards

### PRISMA 2020 Compliance (Systematic Reviews)
- ✅ 27-item checklist (minimum 24/27 required)
- ✅ PRISMA flow diagram with counts
- ✅ Inter-rater reliability κ > 0.6
- ✅ Risk of bias assessment completed
- ✅ Search strategy fully documented and reproducible

### NIH Rigor Standards (Experimental Design)
- ✅ Power ≥80% with justified effect size
- ✅ Randomization method specified with seed
- ✅ Sex as biological variable (SABV) addressed
- ✅ Pre-registered before data collection
- ✅ FAIR-compliant data management plan

### Reproducibility Requirements
- ✅ All code executable in clean Docker environment
- ✅ Random seeds documented
- ✅ Dependencies pinned with exact versions
- ✅ Data versioned with DVC
- ✅ Experiments tracked with MLflow

---

## File Organization

### Research Artifact Structure

```
research-project/
├── docs/
│   ├── problem_statement.md         # FINER criteria
│   ├── search_strategy.md           # Literature search protocol
│   ├── gap_analysis.md              # Identified gaps
│   ├── hypotheses.md                # Testable hypotheses
│   ├── experimental_protocol.md     # NIH-compliant design
│   └── manuscript/                  # Paper drafts
│
├── data/
│   ├── literature/
│   │   ├── search_results.csv       # Database search results
│   │   ├── screened_abstracts.csv   # Screening decisions
│   │   └── extracted_data.csv       # Structured extraction
│   ├── raw/                         # Original data (DVC tracked)
│   ├── processed/                   # Cleaned data (DVC tracked)
│   └── analysis_dataset.csv         # Final analysis dataset
│
├── code/
│   ├── analysis/
│   │   └── primary_analysis.py      # Reproducible analysis script
│   ├── randomization.py             # Allocation sequence
│   └── prepare.py                   # Data preparation
│
├── results/
│   ├── primary_results.json         # Structured results with CI
│   ├── figures/                     # Publication-ready figures
│   ├── tables/                      # Publication-ready tables
│   └── prisma_flow_diagram.md       # PRISMA diagram data
│
└── .dvc/                            # DVC configuration
```

### Auto-Generated Files

The system automatically generates these files when appropriate:
- `data/*.csv.dvc` - DVC tracking files for large data
- `.claude/backups/*.json` - State backups before compaction
- `.claude/tool_log.db` - Complete tool usage log
- `mlruns/` - MLflow experiment tracking data

---

## Mode-Specific Behaviors

### ASSISTANT Mode Behaviors (Current)

**Literature Review:**
- Present search strategy for approval
- Show screening results for each paper
- Explain inclusion/exclusion decisions
- Request human judgment on borderline cases
- Collaborative data extraction

**Hypothesis Formation:**
- Suggest multiple hypothesis candidates
- Explain rationale for each
- Request human selection or refinement
- Collaborative operationalization of variables

**Experimental Design:**
- Present design options with trade-offs
- Explain power analysis assumptions
- Request approval for sample size
- Collaborative development of protocols

**Analysis:**
- Explain statistical approach before execution
- Present assumption test results
- Request interpretation of borderline findings
- Collaborative sensitivity analyses

**Writing:**
- Draft sections incrementally
- Request feedback at each stage
- Explain reporting guideline compliance
- Collaborative revision process

### AUTONOMOUS Mode Behaviors

**Literature Review:**
- Execute full PRISMA workflow automatically
- Simulate inter-rater reliability (two independent screening passes)
- Auto-resolve conflicts with third reviewer simulation
- Progress to next phase when κ > 0.6

**Hypothesis Formation:**
- Generate 5 candidate hypotheses via Tree-of-Thought
- Rank using falsifiability, novelty, testability
- Select top 3 automatically
- Proceed to experimental design

**Experimental Design:**
- Select most rigorous feasible design
- Conduct power analysis with conservative assumptions
- Generate complete protocols
- Auto-register on OSF (if credentials available)

**Analysis:**
- Execute pre-registered analysis plan exactly
- Run all assumption tests
- Perform pre-specified sensitivity analyses
- Generate structured results automatically

**Writing:**
- Chain-of-Drafts manuscript generation
- Auto-populate reporting guideline checklists
- Verify all citations
- Generate publication-ready document

---

## Research Standards References

### Essential Guidelines

**PRISMA 2020:** https://www.prisma-statement.org/prisma-2020-checklist
- Systematic review reporting standard
- 27-item checklist
- Flow diagram specifications

**CONSORT:** https://www.consort-spirit.org
- RCT reporting standard
- 30-item checklist
- Flow diagram for participant allocation

**NIH Rigor:** https://grants.nih.gov/policy-and-compliance/policy-topics/reproducibility
- Experimental design standards
- Power analysis requirements
- SABV considerations
- Pre-registration requirements

**EQUATOR Network:** https://www.equator-network.org/
- Comprehensive reporting guidelines database
- Domain-specific guidelines (STROBE, STARD, etc.)

### Statistical Resources

**Effect Size Calculators:** Use `statsmodels.stats.power` for power analysis
**GRADE Handbook:** For evidence quality assessment
**Cochrane RoB 2:** Risk of bias tool for RCTs
**ROBINS-I:** Risk of bias tool for observational studies

---

## Error Handling

### Common Issues and Solutions

**API Rate Limit Exceeded:**
- Automatically retry with exponential backoff
- Max 3 retries with 2^n second delays
- Log rate limit warnings

**Literature Search Returns Zero Results:**
- Broaden search terms
- Try alternative databases
- Suggest search strategy refinement

**Statistical Assumptions Violated:**
- Apply appropriate transformations
- Suggest non-parametric alternatives
- Document decisions and run sensitivity analyses

**Git Merge Conflicts:**
- Prioritize keeping both versions for research artifacts
- Never auto-resolve - always request human decision
- Preserve complete history

**DVC Push Fails:**
- Check remote storage credentials
- Verify network connectivity
- Suggest local-only tracking as fallback

---

## Security Guidelines

### Allowed Operations

✅ Read files in project directory
✅ Write files to project subdirectories
✅ Execute Python/R analysis scripts
✅ Call approved APIs (literature, citation databases)
✅ Git operations (add, commit, push to research repos)
✅ DVC operations (add, push data)

### Blocked Operations

❌ System administration commands
❌ File operations outside project directory
❌ Execution of untrusted code
❌ Access to credentials or secrets
❌ Network operations to unapproved domains
❌ Database modifications (use MCP servers instead)

---

## Tips for Effective Use

### For PhD Students (ASSISTANT Mode)

1. **Start with problem formulation** - Use FINER criteria validation
2. **Follow PRISMA for literature reviews** - Ensures systematic approach
3. **Pre-register experiments** - Increases credibility
4. **Use decision gates** - Validates each phase before proceeding
5. **Version everything** - Git for code, DVC for data
6. **Document decisions** - Audit trail helps during defense

### For Autonomous Research (AUTONOMOUS Mode)

1. **Specify clear research question** - System works best with well-defined problems
2. **Provide domain context** - Helps with literature search and gap identification
3. **Set feasibility constraints** - Computational budget, time limits
4. **Review decision gates** - Even in autonomous mode, validate key transitions
5. **Monitor progress** - Check logs for unexpected behaviors

---

## Current Project State

**Phase:** Foundation & Cleanup
**Status:** 40% complete
**Next Steps:**
1. Complete git initialization
2. Implement hook scripts
3. Create first specialized agents
4. Develop MCP servers

**See PROJECT_STATUS.md for detailed roadmap**

---

## Support and Documentation

**Full Documentation:** See `/docs` directory
**Agent Specs:** See `.claude/agents/*.md`
**Hook Implementations:** See `.claude/hooks/*.py`
**Workflow Guides:** See `/workflows/*.md`
**Status Updates:** See `PROJECT_STATUS.md`

---

*This file configures Claude Code's behavior for the Production Research Assistant System. Update mode and phase information as project progresses.*
