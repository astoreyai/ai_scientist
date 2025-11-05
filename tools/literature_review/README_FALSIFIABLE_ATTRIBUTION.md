# Systematic Literature Review for "Falsifiable Attribution for Face Verification"

**Generated:** October 16, 2025
**Status:** Complete and ready for execution
**Estimated Timeline:** 7-9 weeks

---

## 📚 What This Package Provides

This comprehensive systematic literature review package includes:

1. **7 detailed Scopus search queries** covering all aspects of your research
2. **Complete search strategy documentation** with rationale and validation
3. **Quick reference guide** with copy-paste queries
4. **Visual coverage diagrams** showing how searches map to research questions
5. **Step-by-step execution checklist** for the entire review process

**Everything you need to conduct a rigorous, PRISMA-compliant systematic literature review for your PhD dissertation.**

---

## 📁 Files in This Package

### Core Files (USE THESE)

1. **`scopus_search_queries_falsifiable_attribution.yaml`**
   - Complete YAML file with all 7 search queries
   - Includes keywords, Boolean queries, filters, RQ mapping
   - **USE THIS:** For automated search pipeline or reference

2. **`SCOPUS_QUERIES_QUICK_REFERENCE.md`**
   - Copy-paste ready queries for manual execution
   - One page per search with filters
   - **USE THIS:** For manual search in Scopus web interface

3. **`SEARCH_STRATEGY_FALSIFIABLE_ATTRIBUTION.md`**
   - Comprehensive 30-page strategy document
   - Rationale for each search, keyword development, validation
   - **USE THIS:** To understand the search strategy and document methodology

4. **`SEARCH_COVERAGE_DIAGRAM.md`**
   - Visual diagrams showing RQ coverage, search overlap, expected results funnel
   - **USE THIS:** For understanding how searches fit together

5. **`EXECUTION_CHECKLIST.md`**
   - Week-by-week, day-by-day checklist for entire review process
   - **USE THIS:** As your roadmap through the 7-9 week process

6. **`README_FALSIFIABLE_ATTRIBUTION.md`** (this file)
   - Overview and quick start guide
   - **USE THIS:** As your entry point

---

## 🚀 Quick Start Guide

### Option 1: Manual Execution (Recommended for First Time)

**Step 1:** Open `SCOPUS_QUERIES_QUICK_REFERENCE.md`

**Step 2:** Go to https://www.scopus.com/ → Advanced Search

**Step 3:** Copy and paste **Search 1** query, apply filters, review results

**Step 4:** If results look good (100-300 papers, first 20 relevant), export to reference manager

**Step 5:** Repeat for Searches 2-7

**Step 6:** Follow `EXECUTION_CHECKLIST.md` for screening process

### Option 2: Automated Execution (Advanced)

**Step 1:** Set up Scopus API (see `automated_scopus/README.md`)

**Step 2:** Use `scopus_search_queries_falsifiable_attribution.yaml` as input

**Step 3:** Run automated pipeline:
```bash
cd /home/aaron/projects/xai/PHD_PIPELINE/tools/literature_review/automated_scopus
python scopus_search.py --config ../scopus_search_queries_falsifiable_attribution.yaml
```

**Step 4:** Export results and follow `EXECUTION_CHECKLIST.md` for screening

---

## 🎯 Research Questions Addressed

Your dissertation investigates:

**RQ1:** Can attribution techniques satisfy formal falsifiability criteria?
**RQ2:** What are theoretical/empirical limits of attribution faithfulness in face verification?
**RQ3:** How do current methods (Grad-CAM, IG, SHAP, LIME) perform under falsifiability testing?
**RQ4:** What constitutes sufficient faithfulness for legal/forensic deployment?

**All 4 RQs are covered by multiple searches**, ensuring comprehensive literature coverage.

---

## 🔍 The 7 Search Queries

### HIGH PRIORITY (Execute First)

**SEARCH 1: XAI in Face Verification** (100-300 papers)
- Primary search at core intersection
- Addresses ALL 4 research questions
- Start here

**SEARCH 7: Falsifiability Gap** (5-30 papers) ★ CRITICAL ★
- Establishes novelty of your research
- Expected to return very few papers
- If <30 papers → Strong novelty claim
- If >100 papers → Novelty weakened, discuss with advisor

**SEARCH 2: Specific XAI Techniques** (200-500 papers)
- Grad-CAM, SHAP, LIME, Integrated Gradients
- Foundational literature on methods being evaluated
- Addresses RQ2, RQ3

**SEARCH 3: Faithfulness Evaluation** (100-250 papers)
- Counterfactual explanations, sanity checks, fidelity metrics
- Core evaluation methodology
- Addresses RQ1, RQ2, RQ3

**SEARCH 4: Face Verification Architectures** (150-400 papers)
- ArcFace, CosFace, metric learning, hypersphere embeddings
- Technical background on models being used
- Addresses RQ2, RQ3

### MEDIUM PRIORITY (Execute Later)

**SEARCH 5: Legal/Forensic Context** (80-200 papers)
- GDPR, EU AI Act, wrongful arrests, Daubert standard
- Application motivation and context
- Addresses RQ4

**SEARCH 6: Theoretical Foundations** (50-150 papers)
- Manifold learning, hypersphere geometry, attribution theory
- Deep theoretical background
- Addresses RQ1, RQ2

---

## 📊 Expected Results

| Stage | Expected Results |
|-------|------------------|
| **Initial retrieval** | 685-1,530 papers (across 7 searches) |
| **After deduplication** | 400-800 unique papers (30-50% overlap) |
| **After title screening** | 250-450 papers (50-60% retention) |
| **After abstract screening** | 150-300 papers (60% retention) |
| **After full-text screening** | 80-150 papers (50-60% retention) |

**Final corpus:** 80-150 papers for synthesis and writing Chapter 2

---

## ✅ Key Success Criteria

**Your literature review is successful if:**

1. ✅ **Search 1 returns 150-250 papers** (core coverage without overwhelm)
2. ✅ **Search 7 returns <30 papers** (confirms novelty gap)
3. ✅ **30-50% deduplication rate** (validates search strategy)
4. ✅ **Key papers captured** (DeepFace, FaceNet, Grad-CAM, LIME, SHAP, IG, etc.)
5. ✅ **All 4 RQs covered** by multiple searches
6. ✅ **Final corpus of 80-150 papers** for synthesis

---

## 📅 Timeline (7-9 Weeks)

### Week 0: Preparation (2-3 days)
- Set up reference manager
- Test all 7 queries in Scopus
- Validate result counts and relevance
- Refine queries if needed

### Week 1: Execution (5 days)
- Execute all 7 searches in Scopus
- Export results to reference manager
- Deduplicate across searches

### Week 2: Title Screening (5 days)
- Screen all titles (400-800 papers)
- Apply inclusion/exclusion criteria
- Retain 250-450 papers

### Week 3: Abstract Screening (5 days)
- Screen all abstracts (250-450 papers)
- Apply full criteria
- Retain 150-300 papers

### Week 4: Full-Text Retrieval (5 days)
- Download/request all full texts
- Organize files
- Handle access issues

### Week 5-6: Full-Text Screening (10 days)
- Read full texts (150-300 papers)
- Extract data to synthesis matrix
- Assess quality
- Retain 80-150 papers

### Week 7: Synthesis & Documentation (5 days)
- Complete PRISMA flow diagram
- Finalize synthesis matrix
- Document search process
- Prepare for writing

### Week 8-11: Write Chapter 2 (3-4 weeks)
- Use template: `PHD_PIPELINE/templates/dissertation/chapter_02_literature_review.md`
- Target: 15,000-20,000 words
- Multiple revision passes

**TOTAL: 7-9 weeks for complete systematic literature review**

---

## 🛠️ Tools You'll Need

**Required:**
- [ ] **Scopus access** (university subscription or API key)
- [ ] **Reference manager** (Zotero or Mendeley recommended)
- [ ] **Spreadsheet software** (Excel or Google Sheets)
- [ ] **PDF reader** (for full-text screening)

**Recommended:**
- [ ] **PRISMA flow diagram tool** (online or manual)
- [ ] **Citation manager** (BibTeX/EndNote)
- [ ] **Text editor** (for writing Chapter 2)

---

## 📋 Step-by-Step Process

### Phase 1: Query Validation
1. Open `SCOPUS_QUERIES_QUICK_REFERENCE.md`
2. Test each query in Scopus web interface
3. Check result counts and relevance
4. Document any needed refinements
5. **Checkpoint:** All queries validated ✓

### Phase 2: Search Execution
1. Execute all 7 searches in priority order
2. Record date, time, result count for each
3. Export results in RIS or BibTeX format
4. Save searches in Scopus for reproducibility
5. **Checkpoint:** All searches executed ✓

### Phase 3: Deduplication
1. Import all results to reference manager
2. Run automatic deduplication
3. Manual review for missed duplicates
4. Calculate deduplication rate (expect 30-50%)
5. **Checkpoint:** Unique corpus created ✓

### Phase 4: Title Screening
1. Export titles to spreadsheet
2. Screen each title: Include / Exclude / Uncertain
3. Apply decision rules from inclusion criteria
4. Daily target: 100-150 titles
5. **Checkpoint:** Title screening complete ✓

### Phase 5: Abstract Screening
1. Retrieve abstracts for Include + Uncertain
2. Screen abstracts against full criteria
3. Document exclusion reasons
4. Daily target: 50-80 abstracts
5. **Checkpoint:** Abstract screening complete ✓

### Phase 6: Full-Text Screening
1. Obtain all full texts (download, request, contact authors)
2. Read full texts and apply all criteria
3. Extract data to synthesis matrix
4. Assess quality using checklist
5. **Checkpoint:** Full-text screening complete ✓

### Phase 7: Synthesis
1. Complete PRISMA flow diagram
2. Finalize synthesis matrix
3. Organize by themes/RQs
4. Identify key findings and gaps
5. **Checkpoint:** Ready for writing ✓

### Phase 8: Writing
1. Use Chapter 2 template from PhD Pipeline
2. Structure: Introduction → Methods → Results → Gap → Conclusion
3. Synthesize (don't just summarize)
4. Cite all 80-150 papers appropriately
5. **Checkpoint:** Chapter 2 draft complete ✓

---

## 🎯 Critical Checkpoints

### Checkpoint 1: After Query Testing
**Questions to ask:**
- [ ] Are result counts within expected ranges?
- [ ] Are first 20 results >80% relevant?
- [ ] Are key papers (DeepFace, Grad-CAM, etc.) captured?
- [ ] Is Search 7 returning <30 papers? (novelty check)

**If NO to any → Refine queries before execution**

### Checkpoint 2: After Deduplication
**Questions to ask:**
- [ ] Is deduplication rate 30-50%?
- [ ] Do we have 400-800 unique papers?
- [ ] Is there overlap between searches? (good!)

**If NO → Review search strategy**

### Checkpoint 3: After Each Screening Stage
**Questions to ask:**
- [ ] Is retention rate reasonable? (50-60% per stage)
- [ ] Are exclusions justified and documented?
- [ ] Are we on track for 80-150 final papers?

**If NO → Review inclusion/exclusion criteria**

### Checkpoint 4: After Full-Text Screening
**Questions to ask:**
- [ ] Do we have 80-150 papers in final corpus?
- [ ] Are all 4 RQs adequately covered?
- [ ] Are key papers included?
- [ ] Is quality assessment complete?

**If NO → Consider backward/forward citation search**

---

## 🔧 Troubleshooting

### Problem: Search 1 returns <50 papers
**Diagnosis:** Keywords too restrictive
**Solution:** Add synonyms, expand date range, broaden terms

### Problem: Search 7 returns >100 papers
**Diagnosis:** Falsifiability may be well-explored (weakens novelty)
**Solution:** Review papers carefully, narrow to Popperian falsifiability, discuss with advisor

### Problem: Overall results >2000 papers
**Diagnosis:** Too broad, screening will be overwhelming
**Solution:** Add TITLE-only searches, narrow date ranges, restrict to journals only

### Problem: Key papers missing (DeepFace, Grad-CAM, etc.)
**Diagnosis:** Search not comprehensive
**Solution:** Backward/forward citation search, hand search key venues

### Problem: <20% deduplication rate
**Diagnosis:** Searches too disconnected
**Solution:** Review search strategy, ensure overlap is intentional

---

## 📖 Integration with PhD Pipeline

This literature review package is **Phase 2** of the PhD Pipeline workflow.

**Your dissertation structure:**
1. **Chapter 1:** Introduction (completed before this)
2. **Chapter 2:** Literature Review ← **YOU ARE HERE**
3. **Chapter 3:** Theoretical Framework (next step)
4. **Chapter 4:** Methodology
5. **Chapter 5:** Implementation
6. **Chapter 6:** Results
7. **Chapter 7:** Discussion
8. **Chapter 8:** Conclusion

**After completing this literature review, you will:**
- Have a comprehensive understanding of the field
- Clearly articulate your research gap (falsifiability in XAI)
- Position your contribution within existing work
- Have 80-150 papers to cite in Chapter 2
- Be ready to write your theoretical framework (Chapter 3)

---

## 📚 Key Papers to Validate

**Your searches MUST capture these foundational papers:**

**XAI Methods:**
- Selvaraju et al. (2017) - Grad-CAM
- Ribeiro et al. (2016) - LIME
- Lundberg & Lee (2017) - SHAP
- Sundararajan et al. (2017) - Integrated Gradients

**XAI Evaluation:**
- Adebayo et al. (2018) - Sanity Checks for Saliency Maps
- Hooker et al. (2019) - Benchmark for Interpretability Methods

**Face Verification:**
- Taigman et al. (2014) - DeepFace
- Schroff et al. (2015) - FaceNet
- Liu et al. (2017) - SphereFace
- Wang et al. (2018) - CosFace
- Deng et al. (2019) - ArcFace

**If any are missing after Search 1, investigate and add manually.**

---

## 💡 Tips for Success

### DO:
✅ Test all queries manually before automating
✅ Document everything (dates, counts, decisions)
✅ Follow PRISMA guidelines for transparency
✅ Use reference manager from the start
✅ Screen consistently (same criteria throughout)
✅ Extract data systematically to synthesis matrix
✅ Synthesize, don't just summarize

### DON'T:
❌ Skip query validation (test first!)
❌ Modify queries after execution (create new IDs instead)
❌ Rush screening (quality over speed)
❌ Cherry-pick papers (be systematic)
❌ Forget to document exclusions
❌ Leave citation management to the end

---

## 📞 Support and Resources

**For questions about:**
- **Scopus syntax:** https://dev.elsevier.com/sc_search_tips.html
- **PRISMA methodology:** http://prisma-statement.org/
- **PhD Pipeline:** See `PHD_PIPELINE/README.md`

**For help with:**
- **Query refinement:** Test in Scopus web interface first
- **API issues:** Check `automated_scopus/README.md`
- **Screening decisions:** Use `inclusion_exclusion_criteria_template.md`
- **Data extraction:** Use `synthesis_matrix_template.csv`

---

## ✅ Final Deliverables

**By the end of this systematic literature review, you will have:**

1. ✅ **PRISMA-compliant search strategy** (documented in `SEARCH_STRATEGY_FALSIFIABLE_ATTRIBUTION.md`)
2. ✅ **7 executed Scopus searches** (with dates, counts, exports saved)
3. ✅ **PRISMA flow diagram** (showing screening process and numbers)
4. ✅ **Synthesis matrix** (80-150 papers with extracted data)
5. ✅ **Quality assessment** (all papers rated high/medium/low)
6. ✅ **Research gap identification** (novelty confirmed via Search 7)
7. ✅ **Chapter 2 draft** (15,000-20,000 words, 150-200 citations)
8. ✅ **BibTeX bibliography** (all references formatted)

**These deliverables form the foundation of your literature review chapter and demonstrate rigorous, systematic methodology.**

---

## 🚦 Current Status

**Status:** ✅ **Complete and ready for execution**

**Next steps:**
1. Start with `EXECUTION_CHECKLIST.md` → Week 0, Day 1
2. Test queries in Scopus web interface
3. Begin systematic execution

**Estimated completion:** 7-9 weeks from start

---

## 📄 File Listing

```
literature_review/
├── scopus_search_queries_falsifiable_attribution.yaml (YAML search config)
├── SCOPUS_QUERIES_QUICK_REFERENCE.md (copy-paste queries)
├── SEARCH_STRATEGY_FALSIFIABLE_ATTRIBUTION.md (30-page strategy)
├── SEARCH_COVERAGE_DIAGRAM.md (visual diagrams)
├── EXECUTION_CHECKLIST.md (week-by-week checklist)
└── README_FALSIFIABLE_ATTRIBUTION.md (this file)
```

**All files are complete and production-ready.**

---

## 🎓 Academic Rigor

This systematic literature review package follows:

- ✅ **PRISMA 2020 guidelines** (Preferred Reporting Items for Systematic Reviews)
- ✅ **Transparent search strategy** (all queries documented)
- ✅ **Reproducible methodology** (other researchers can replicate)
- ✅ **Comprehensive coverage** (7 complementary searches)
- ✅ **Quality assurance** (multiple checkpoints and validation)
- ✅ **Systematic screening** (clear inclusion/exclusion criteria)

**This meets PhD-level standards for systematic literature reviews.**

---

## 🔬 Research Contribution

**This literature review will demonstrate:**

1. **Comprehensive understanding** of XAI in face verification
2. **Clear research gap** (falsifiability has not been applied to XAI evaluation)
3. **Strong positioning** of your counterfactual score prediction framework
4. **Awareness of context** (legal/forensic requirements driving need for faithful explanations)
5. **Theoretical grounding** (understanding of hypersphere embeddings and attribution theory)

**This forms the essential foundation for a successful PhD dissertation.**

---

**You now have everything needed to conduct a rigorous, comprehensive systematic literature review. Good luck! 📚🎓**

---

**Questions? Issues? Feedback?**

Document all notes, issues, and decisions as you go. This is part of the systematic process and demonstrates rigor.

**Ready to start? Open `EXECUTION_CHECKLIST.md` and begin Week 0, Day 1. ✅**
