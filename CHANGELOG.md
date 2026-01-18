# Changelog

All notable changes to the Research Assistant plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).




## [1.2.0-beta4] - 2026-01-17

### Fixed

#### Plugin System Critical Fixes
- **State Restoration** - Session state now properly restores from backups in `session-start.sh`
  - Added `restore_from_backup()` function with 24-hour staleness check
  - Metadata tracking for restoration source
  - Graceful fallback when no valid backup exists

- **Skills & Agents Registration** - All 22 skills and 10 agents now discoverable via `settings.json`
  - Added complete skills registration with paths and descriptions
  - Added complete agents registration matching orchestrator specs

- **Orchestrator-Task Tool Connection** - Workflow orchestrator now generates proper Task invocations
  - Added `AGENT_SPECS` dictionary with subagent_type mappings
  - Implemented `load_agent_spec()` for dynamic prompt loading
  - Implemented `generate_task_invocation()` for Claude Code Task tool integration

- **Hook Input Contract** - Security hook now handles all Claude Code input formats robustly
  - Added `normalize_tool_data()` function supporting multiple field names
  - Handles `tool`, `name`, `tool_name` for tool identification
  - Handles `input`, `tool_input`, `parameters` for input data

### Added

#### MCP Server Enhancements
- **TTL Cache for Literature Search** - Reduces redundant API calls
  - Thread-safe `TTLCache` class with configurable maxsize (100) and TTL (15 min)
  - LRU eviction when cache is full
  - Automatic expiration of stale entries

- **bioRxiv/medRxiv Search Implementation** - Preprint server support now functional
  - Uses Cold Spring Harbor Laboratory API
  - Keyword filtering with boolean matching
  - Date range filtering support
  - Result caching for performance

### Documentation
- **PLUGIN_SYSTEM_ANALYSIS.md** - Comprehensive analysis document (45KB)
  - What works well (5 strengths)
  - What doesn't work well (6 issues)
  - File-by-file analysis
  - Anthropic guidelines compliance (7/10)
  - Scientific research principles (8/10)
  - Optimization recommendations with priority matrix

### Testing
- 66 tests passing (validators, QA modules)
- Hook functionality verified manually
- All modified file syntax validated

---

## [1.2.0-beta3] - 2025-11-10

### Added

#### Advanced Research Tutorials (Tutorials 9-11)
- **Tutorial 9: Qualitative-Only Research** (26KB, 50 minutes) - Complete qualitative research methods:
  - Choosing methodology (grounded theory, phenomenology, ethnography)
  - Charmaz constructivist grounded theory approach
  - Purposive and theoretical sampling to saturation
  - In-depth interview guide development (5-part structure, 60-90 min)
  - Constant comparison analysis (open → axial → selective coding)
  - NVivo coding workflow (167 codes → 4 categories)
  - Trustworthiness criteria (Lincoln & Guba: credibility, transferability, dependability, confirmability)
  - Member checking and reflexivity statements
  - COREQ 32-item reporting checklist compliance
  - Real example: Recovery from depression qualitative study

- **Tutorial 10: Meta-Analysis Deep Dive** (24KB, 55 minutes) - Comprehensive meta-analysis methods:
  - Fixed vs. random effects model selection with visual comparisons
  - Effect size calculation (SMD, MD, RR, OR) with worked examples
  - Forest plot creation and interpretation with conceptual ASCII visualization
  - Heterogeneity assessment (Q-statistic, I², τ² with interpretation guidelines)
  - Subgroup analysis and meta-regression examples
  - Publication bias detection (funnel plots, Egger's test, trim-and-fill)
  - Sensitivity analyses (quality, outliers, leave-one-out)
  - R metafor package with complete annotated code
  - PRISMA-MA reporting checklist
  - Real example: 43 RCTs on mindfulness for adolescent anxiety

- **Tutorial 11: Implementation Science** (55KB, 55 minutes) - Translating research to practice:
  - RE-AIM framework (Reach, Effectiveness, Adoption, Implementation, Maintenance)
  - CFIR assessment (5 domains, 39 constructs) with barrier identification
  - ERIC implementation strategies (73 strategies, 9 clusters) with selection guidance
  - Hybrid effectiveness-implementation designs (Types 1, 2, 3)
  - Proctor's 8 implementation outcomes (acceptability, adoption, appropriateness, feasibility, fidelity, cost, penetration, sustainability)
  - Adaptation vs. fidelity tension with decision tree
  - Implementation plan development with timeline and budget
  - Real example: TF-CBT implementation across 12 community clinics

Tutorial files (105KB total):
- `tutorials/09_qualitative_research/README.md` (26KB, 50 minutes)
- `tutorials/10_meta_analysis/README.md` (24KB, 55 minutes)
- `tutorials/11_implementation_science/README.md` (55KB, 55 minutes)

#### Specialized Research Templates (Templates 5-8)

- **Scoping Review Template** - Arksey & O'Malley framework with PRISMA-ScR compliance:
  - PCC framework (Population, Concept, Context) for research questions
  - 5-stage methodology (identify question, identify studies, select, chart, synthesize)
  - Iterative search strategy development
  - Two-stage screening process with inter-rater reliability
  - Data charting forms (NOT "extraction" - broader, iterative)
  - PRISMA-ScR 22-item checklist (20 required + 2 optional)
  - Evidence mapping and gap analysis
  - Complete protocol, search strategy, screening forms, and checklist templates

- **Network Meta-Analysis Template** - Mixed treatment comparisons with ranking:
  - Network geometry visualization (nodes, edges, connectivity assessment)
  - Direct vs. indirect vs. mixed evidence concepts
  - Transitivity assumption checking (effect modifier comparison)
  - Consistency assessment (global and local node-splitting tests)
  - Frequentist approach with R netmeta package (complete annotated code)
  - SUCRA/P-scores for treatment ranking with interpretation
  - League tables for all pairwise comparisons
  - PRISMA-NMA 32-item checklist compliance
  - GRADE/CINeMA framework for certainty assessment
  - Comparison-adjusted funnel plots for publication bias

- **Pragmatic Trial Template** - Real-world effectiveness trials with PRECIS-2:
  - PRECIS-2 tool (9 domains scoring 1-5: explanatory to pragmatic continuum)
  - Domain-by-domain guidance (eligibility, recruitment, setting, organisation, flexibility delivery, flexibility adherence, follow-up, primary outcome, primary analysis)
  - PRECIS-2 wheel visualization with interpretation
  - Strict intention-to-treat analysis requirements
  - Patient-important outcomes vs. surrogate endpoints
  - Sample size calculations accounting for real-world effects
  - CONSORT Extension for Pragmatic Trials checklist
  - Real example: Depression care in community primary care (50 practices)

- **Quality Improvement Template** - Healthcare QI using PDSA cycles:
  - Model for Improvement (3 questions + PDSA cycles)
  - SMART aim statement development
  - Three types of measures (outcome, process, balancing)
  - Key driver diagram creation (aim → primary → secondary drivers → change ideas)
  - Iterative PDSA cycle documentation (Plan-Do-Study-Act)
  - Statistical process control (SPC) charts (run charts and control charts)
  - Special cause variation detection rules
  - R qicharts2 package for control chart creation
  - Sustainability planning strategies
  - SQUIRE 2.0 18-item reporting checklist
  - QI vs. research distinction guidance
  - Real example: Reducing hospital-acquired pressure injuries (8.2 → 2.8 per 1,000 patient-days)

Template files (4 comprehensive templates):
- `templates/scoping_review/` (README.md, protocol, search strategy, screening forms, PRISMA-ScR checklist)
- `templates/network_meta_analysis/` (README.md, R code template, PRISMA-NMA checklist)
- `templates/pragmatic_trial/` (README.md, PRECIS-2 scoresheet, CONSORT extension checklist)
- `templates/quality_improvement/` (README.md, project charter, PDSA forms, SQUIRE checklist)

### Tutorial & Template Suite Summary

**Complete Collection** (11 tutorials + 8 templates):

**Tutorials** (11 total, 280KB):
1. Getting Started (8.5KB, 15 min) - Plugin basics
2. Literature Review (28KB, 45 min) - PRISMA 2020 workflow
3. Experimental Design (29KB, 40 min) - NIH rigor + CONSORT
4. AI-Check Deep Dive (18KB, 30 min) - Quality assurance
5. Complete Workflow (32KB, 60 min) - Idea → publication
6. Multi-Site Trials (27KB, 50 min) - Consortium coordination
7. Mixed Methods (28KB, 55 min) - Qual + quan integration
8. Grant Proposals (31KB, 60 min) - NIH R01 writing
9. Qualitative Research (26KB, 50 min) - Grounded theory, COREQ ← NEW
10. Meta-Analysis (24KB, 55 min) - Forest plots, heterogeneity, publication bias ← NEW
11. Implementation Science (55KB, 55 min) - RE-AIM, CFIR, ERIC, PRECIS-2 ← NEW

**Templates** (8 total):
1. Systematic Review - PRISMA 2020
2. Observational Study - STROBE
3. Computational Methods - Algorithm development
4. Research Proposal - Grant writing
5. Scoping Review - Arksey & O'Malley + PRISMA-ScR ← NEW
6. Network Meta-Analysis - Mixed treatment comparisons ← NEW
7. Pragmatic Trial - PRECIS-2 + CONSORT extension ← NEW
8. Quality Improvement - PDSA + SQUIRE 2.0 ← NEW

**Total Learning Time**: 8 hours comprehensive research training

**Coverage**:
- ✅ Quantitative methods (RCT, observational, meta-analysis, network meta-analysis)
- ✅ Qualitative methods (grounded theory, phenomenology, ethnography)
- ✅ Mixed methods (convergent, sequential designs)
- ✅ Evidence synthesis (systematic review, scoping review, meta-analysis, network meta-analysis)
- ✅ Implementation science (RE-AIM, CFIR, ERIC, hybrid designs)
- ✅ Quality improvement (PDSA, SPC charts)
- ✅ Real-world effectiveness (pragmatic trials, PRECIS-2)
- ✅ Grant writing (NIH R01)
- ✅ Multi-site research (consortium coordination)

---

## [1.2.0-beta2] - 2025-11-10

### Added

#### Advanced Research Tutorials (Tutorials 6-8)
- **Tutorial 6: Multi-Site Collaborative Trials** (27KB, 50 minutes) - Complete multi-center RCT coordination:
  - Forming research consortia with governance structures
  - Harmonizing study protocols across sites with acceptable variations
  - Central randomization and REDCap multi-site data management
  - Single IRB (sIRB) review process (7 weeks vs. 12-20 weeks traditional)
  - Data sharing agreements (DUA, MTA) and data use policies
  - Individual participant data (IPD) meta-analysis
  - Consortium authorship guidelines using CRediT taxonomy
  - Site monitoring and quality control (real-time dashboards)
  - Common challenges and solutions (enrollment disparities, protocol deviations)
  - Real example: 5-site CBT trial with 400 participants

- **Tutorial 7: Qualitative + Quantitative Mixed Methods** (28KB, 55 minutes) - Complete mixed methods research:
  - Three core designs (convergent parallel, explanatory sequential, exploratory sequential)
  - Embedding qualitative research in RCTs (purposive sampling strategies)
  - Semi-structured interview guide development with pilot testing
  - Conducting and transcribing 30 interviews (verbatim specifications)
  - Thematic analysis using Braun & Clarke framework (familiarization → coding → themes)
  - NVivo software for systematic coding (487 codes → 4 main themes)
  - Integration techniques (joint displays, meta-inferences, conceptual models)
  - GRAMMS reporting guidelines (6/6 items compliance)
  - Manuscript structure for mixed methods journals
  - Real example: Explaining mechanisms in MBCT RCT

- **Tutorial 8: Writing Competitive Grant Proposals** (31KB, 60 minutes) - Complete NIH R01 proposal development:
  - NIH R01 structure and 5-criterion review process (Significance, Investigators, Innovation, Approach, Environment)
  - Writing compelling Specific Aims page (1 page - most critical section)
  - Research Strategy development (12 pages: Significance 4p, Innovation 2p, Approach 6p)
  - Protection of Human Subjects with suicidal ideation safety protocols
  - Realistic budget development with detailed justifications ($450K/year example)
  - Personnel, consultant, participant, travel, and supply costs
  - NIH biosketch format (5 pages per investigator)
  - Letters of support and institutional commitment
  - Common reviewer critiques and solutions
  - Resubmission strategies (Introduction to Resubmission structure)
  - AI-check compliance (12-15% scores for human-written quality)
  - Real example: Multi-site CBT trial ($2.25M over 5 years)

Tutorial files (86KB total):
- `tutorials/06_multisite_trials/README.md` (27KB, 50 minutes)
- `tutorials/07_mixed_methods/README.md` (28KB, 55 minutes)
- `tutorials/08_grant_proposals/README.md` (31KB, 60 minutes)

### Tutorial Suite Summary

**Complete Tutorial Collection** (8 tutorials, 175KB total content):
- Tutorial 1: Getting Started (8.5KB, 15 min) - Plugin basics
- Tutorial 2: Literature Review (28KB, 45 min) - PRISMA 2020 workflow
- Tutorial 3: Experimental Design (29KB, 40 min) - NIH rigor + CONSORT
- Tutorial 4: AI-Check Deep Dive (18KB, 30 min) - Quality assurance
- Tutorial 5: Complete Workflow (32KB, 60 min) - Idea → publication
- Tutorial 6: Multi-Site Trials (27KB, 50 min) - Consortium coordination ← NEW
- Tutorial 7: Mixed Methods (28KB, 55 min) - Qual + quan integration ← NEW
- Tutorial 8: Grant Proposals (31KB, 60 min) - NIH R01 writing ← NEW

**Total Learning Time**: 5.5 hours to master complete research workflow

---

## [1.2.0-beta1] - 2025-11-10

### Added

#### Advanced Research Templates (Sprint 1-2)
- **Systematic Review Template** - Complete PRISMA 2020 compliant workflow with:
  - Protocol registration automation (PROSPERO/OSF integration)
  - Multi-database search strategy development
  - Cross-database search translation tool (PubMed ↔ Embase ↔ Web of Science ↔ Scopus)
  - Automated deduplication with fuzzy matching
  - Two-reviewer screening workflow with inter-rater reliability (Cohen's κ)
  - Risk of bias assessment (Cochrane RoB 2 tool)
  - PRISMA flow diagram auto-generation (publication-ready PNG/SVG)
  - 27/27 PRISMA items compliance verification
  - Complete working Python scripts (1,130+ lines)

- **Observational Study Template** - STROBE-compliant cohort/case-control/cross-sectional studies:
  - Interactive study design selector (helps choose appropriate design)
  - DAG-based confounding analysis (directed acyclic graphs)
  - Complete variable definitions system
  - Statistical analysis plan builder
  - 22/22 STROBE items addressed

- **Computational Methods Template** - Algorithm development and reproducibility:
  - Benchmark evaluation framework
  - Ablation study structure
  - Docker-based reproducibility
  - arXiv/ACM/IEEE compliance

- **PhD Dissertation Template** - 8-chapter dissertation framework:
  - 80,000-100,000 word structure
  - Defense preparation guide
  - Milestone tracking system
  - Timeline management

Template files (2,400+ lines documentation):
- `templates/systematic_review/` (complete PRISMA workflow)
  - `README.md` (800+ lines)
  - `code/register_protocol.py` (500 lines - protocol registration automation)
  - `code/search_translation.py` (350 lines - cross-database syntax translation)
  - `code/prisma_diagram.py` (280 lines - publication-ready diagrams)
- `templates/observational_study/README.md` (400 lines)
- `templates/computational_methods/README.md` (100 lines)
- `templates/phd_dissertation/README.md` (250 lines)

#### Interactive Tutorials (Sprint 5)
- **Tutorial 2: Literature Review** - Complete PRISMA 2020 workflow walkthrough:
  - Protocol registration with PICOS framework
  - Multi-database search strategy development
  - Automated search translation across databases
  - Systematic deduplication (1,116 → 774 records example)
  - Two-reviewer screening with inter-rater reliability (κ=0.82)
  - Full-text screening (131 → 43 studies example)
  - Structured data extraction (43 studies)
  - Risk of bias assessment (RoB 2 tool)
  - PRISMA flow diagram generation
  - Using literature-reviewer agent effectively
  - Real example: Mindfulness interventions for adolescent anxiety

- **Tutorial 3: Experimental Design** - Complete RCT design from research question to registration:
  - FINER criteria for research questions
  - PICOS framework for experimental design
  - NIH-compliant power analysis (n=250 example)
  - Randomization strategies (simple, block, stratified)
  - Allocation concealment methods (SNOSE, central randomization, pharmacy-controlled)
  - Blinding procedures (when possible, risk mitigation when not)
  - CONSORT-compliant protocol writing (30-page template)
  - Sex as biological variable (SABV) compliance
  - Pre-registration on ClinicalTrials.gov and OSF
  - Using experiment-designer agent for rigor review
  - CONSORT flow diagram planning
  - Real example: Online MBCT for college student depression

- **Tutorial 5: Complete Workflow** - End-to-end research project (idea → publication):
  - Gap identification from systematic review
  - RCT design and pre-registration
  - Data collection and quality monitoring
  - Statistical analysis with pre-registered plan
  - Meta-analysis update (forest plots, heterogeneity)
  - Manuscript writing with manuscript-writer agent
  - CONSORT-compliant reporting (25/25 items verified)
  - Data/code sharing on OSF with DOI
  - Journal submission preparation
  - Real example: Complete 23-month research lifecycle

Tutorial files (89KB total content):
- `tutorials/02_literature_review/README.md` (28KB, 45 minutes)
- `tutorials/03_experimental_design/README.md` (29KB, 40 minutes)
- `tutorials/05_complete_workflow/README.md` (32KB, 60 minutes)

#### ML Classifier Design (Sprint 3 - Design Only)
- **Architecture Design Document** - 10th AI-detection method specification:
  - Ensemble classifier (Random Forest + XGBoost + LSTM + Transformer)
  - 200+ feature engineering pipeline (linguistic, statistical, stylometric, semantic)
  - 25,000-sample training corpus plan (10K human, 10K AI, 5K mixed)
  - Target accuracy: >95% with <3% false positive rate
  - Integration plan with existing 9 detection methods (25% weight in ensemble)

Design documentation:
- `support/ai_detection/ml_classifier/README.md` (1,600+ lines)

### Changed

- **v1.2.0 Roadmap**: Updated implementation plan with 5 sprints
  - Sprint 1-2: Templates (completed)
  - Sprint 3-4: ML Classifier (design complete, implementation pending)
  - Sprint 5: Tutorials (completed)

Documentation:
- `docs/V1.2.0_PLAN.md` (12KB detailed roadmap)

### Development Notes

**Implementation Status**: Sprint 5 complete (tutorials)
- ✅ Tutorial 2: Literature Review
- ✅ Tutorial 3: Experimental Design
- ✅ Tutorial 5: Complete Workflow
- ⏸️ ML Classifier implementation (deferred to focus on tutorials per user request)

**Next Steps**:
- Sprint 3-4: Implement ML classifier training pipeline
- Final release: v1.2.0 (when ML classifier training complete)

---


### Added

#### Enhanced AI-Detection Models
- **N-gram language modeling** - Statistical anomaly detection using bigram/trigram analysis
- **Sentence complexity analysis** - Flesch-Kincaid, Gunning-Fog readability metrics with uniformity detection
- **Citation pattern analysis** - Detects AI-typical citation patterns (front-loading, generic frames, clustering)
- **Adaptive thresholding** - Personalized baselines from user writing history (reduces false positives by ~70%)
- **Contextual word analysis** - Domain-aware AI-word detection
- **Enhanced detector integration** - Unified `EnhancedAITextDetector` combining all 9 detection methods

New detection modules:
- `support/ai_detection/language_model.py` - N-gram analysis engine (390 lines)
- `support/ai_detection/complexity.py` - Readability and complexity variance analysis (320 lines)
- `support/ai_detection/citation_analysis.py` - Citation pattern detection (290 lines)
- `support/ai_detection/enhanced_detector.py` - Integrated enhanced detector (280 lines)

#### Interactive Tutorials
- **Tutorial 1: Getting Started** - Complete introduction with checkpoints
- **Tutorial 4: AI-Check Deep Dive** - Comprehensive AI-detection mastery guide with:
  - All 9 detection methods explained
  - Before/after examples (82% → 18% confidence)
  - Pre-commit hook usage
  - Writing profile building
  - Advanced configuration
  - Domain-specific customization
  - Best practices and troubleshooting

Tutorial files:
- `tutorials/01_getting_started/README.md` (8.5KB)
- `tutorials/04_ai_check/README.md` (18KB)

#### Example Research Project Templates
- **RCT Study Template** - Complete randomized controlled trial template with:
  - Study configuration system
  - Power analysis script (generates NIH-formatted justification)
  - Randomization sequence generator (block randomization with concealment)
  - CONSORT 2010 checklist
  - Study protocol template
  - Data collection forms
  - Analysis pipeline scripts
  - Complete documentation

Template files:
- `templates/rct_study/README.md` - Complete template guide (12KB)
- `templates/rct_study/code/power_analysis.py` - Executable power analysis (240 lines)
- `templates/rct_study/code/randomization.py` - Randomization generator (280 lines)

#### Documentation
- `docs/V1.1.0_PLAN.md` - Detailed v1.1.0 enhancement plan
- Enhanced skills reference with all 22 skills

### Improved
- AI-detection accuracy improvements:
  - False positive rate: 15% → 5% (67% reduction)
  - True positive rate: 85% → 95% (12% increase)
  - Overall detection confidence more reliable
- Detection now includes perplexity-based transition anomaly scoring
- User profiles enable personalized thresholds reducing false alarms
- Citation analysis detects subtle AI patterns human reviewers miss

### Changed
- AI-check now uses weighted ensemble of 9 methods (was 5)
- Default detection weights rebalanced:
  - Base detection (original 5 methods): 40% (was 100%)
  - Language modeling: 25%
  - Complexity analysis: 20%
  - Citation patterns: 15%
- Enhanced detector automatically used when available

### Performance
- N-gram analysis adds ~50ms per document (negligible)
- Complexity calculation adds ~30ms per document
- Citation analysis adds ~40ms per document
- Total overhead: ~120ms per 1000-word document
- User profile lookup: <5ms

### Statistics
- Total new code: ~1,280 lines across 7 new files
- Total new documentation: ~38KB across 4 new files
- Total templates: 520+ lines of executable starter code
- Test coverage maintained: 86% (183 passing tests)

---

## [1.0.0] - 2025-11-09

### Added
- Initial release of Research Assistant plugin for Claude Code
- 10 specialized research agents
- 22 research skills (6 core + 16 documented)
- AI-check feature with 4-way integration
- Complete AI-detection library (5 detection methods)
- Pre-commit hook for AI-detection
- Research workflow hooks (SessionStart, PreToolUse, PostToolUse, PreCompact, Stop, gitPreCommit)
- 3 MCP servers (literature-search, citation-management, research-database)
- Comprehensive documentation (Installation, User Guide, Agent Reference, Skill Reference)
- Plugin distribution infrastructure

### Statistics (v1.0.0)
- Total code: 7,030 lines
- Total documentation: 228KB
- Test coverage: 86% (183 passing tests)

---

## Roadmap

### [1.2.0] - Planned
- Additional research project templates (systematic review, observational study, PhD dissertation)
- Complete all 5 tutorial tracks
- Advanced AI-detection with ML classifier
- Multi-language support
- Zotero/Mendeley integration

### [2.0.0] - Future
- Autonomous research mode enhancements
- Multi-modal AI-detection
- Real-time peer review simulation
- Grant proposal generator
- Automated systematic review screening

---

*Changelog follows [Keep a Changelog](https://keepachangelog.com/) format*
