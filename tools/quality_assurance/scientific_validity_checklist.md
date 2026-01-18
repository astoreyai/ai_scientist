# Scientific Validity Checklist

**RULE 1: Every statement must be truthful and scientifically valid**

Use this checklist before marking any section as complete.

---

## For Every Claim Made

### □ Evidence Requirement
- [ ] Does this claim have supporting evidence?
- [ ] Is the evidence cited with a proper reference?
- [ ] Is the reference from a peer-reviewed source?
- [ ] If citing your own results, have you shown the data?

**RED FLAGS:**
- ❌ "It is well-known that..." (without citation)
- ❌ "Obviously..." (without proof)
- ❌ "Clearly..." (without demonstration)
- ✅ "Smith et al. (2023) showed that..." (with citation)

---

## For Experimental Claims

### □ Reproducibility
- [ ] Are all hyperparameters listed?
- [ ] Is the random seed specified?
- [ ] Is the dataset version specified?
- [ ] Is the hardware configuration documented?
- [ ] Can someone else reproduce your results?

###□ Statistical Rigor
- [ ] Are means accompanied by standard deviations?
- [ ] Are confidence intervals reported?
- [ ] Is statistical significance tested (p-values)?
- [ ] Is the sample size sufficient?
- [ ] Are multiple runs performed (not just one)?

**Requirements:**
- Report mean ± std dev, not just mean
- State number of runs (minimum 3-5 recommended)
- Use appropriate statistical tests (t-test, ANOVA, etc.)
- Report effect sizes, not just p-values

---

## For Theoretical Claims

### □ Mathematical Correctness
- [ ] Are all equations correctly formatted?
- [ ] Are all variables defined before use?
- [ ] Are assumptions explicitly stated?
- [ ] Are proofs complete (no hand-waving)?
- [ ] Have you checked your math?

### □ Logical Consistency
- [ ] Does A logically lead to B?
- [ ] Are there any circular arguments?
- [ ] Are counterexamples considered?
- [ ] Are edge cases handled?

---

## For Literature Claims

### □ Citation Accuracy
- [ ] Have you read the paper you're citing?
- [ ] Does the citation support your claim?
- [ ] Are you citing the original source (not secondary)?
- [ ] Is the citation correctly formatted?

**RED FLAGS:**
- ❌ Citing based on abstract alone
- ❌ Misrepresenting what a paper says
- ❌ Cherry-picking citations that support your view
- ❌ Citing papers you haven't read

### □ Literature Coverage
- [ ] Have you cited seminal papers in the area?
- [ ] Have you cited recent work (last 2-3 years)?
- [ ] Have you cited work that contradicts yours?
- [ ] Is your review balanced (not biased)?

---

## For Methodological Claims

### □ Validity
- [ ] Does your method measure what you claim?
- [ ] Are there confounding variables?
- [ ] Is your experimental design sound?
- [ ] Have you controlled for biases?

### □ Limitations
- [ ] Have you identified limitations?
- [ ] Have you explained why they exist?
- [ ] Have you stated what you cannot claim?
- [ ] Are you honest about failures?

---

## For Comparative Claims

### □ Fair Comparison
- [ ] Are you comparing against strong baselines?
- [ ] Are all methods using the same data?
- [ ] Are hyperparameters tuned fairly?
- [ ] Are you cherry-picking favorable comparisons?

**Requirements:**
- Use standard benchmarks
- Compare against state-of-the-art
- Report results from original papers
- Use same evaluation metrics

---

## For Implementation Claims

### □ Code Correctness
- [ ] Have you tested your code?
- [ ] Have you verified outputs manually?
- [ ] Have you checked for bugs?
- [ ] Does your code match your description?

### □ Performance Claims
- [ ] Are latency measurements averaged over multiple runs?
- [ ] Is hardware specified?
- [ ] Are warm-up runs excluded?
- [ ] Are you reporting realistic scenarios (not best-case)?

---

## Honesty Requirements

### What You CAN Claim
✅ "We propose..." (describing your contribution)
✅ "We implement..." (what you built)
✅ "Our experiments show..." (based on data)
✅ "We achieve X accuracy on dataset Y" (measured)

### What You CANNOT Claim
❌ Aspirational future work as completed
❌ Results you plan to get but haven't
❌ Industry validation without actual partners
❌ Human study results without IRB and actual study
❌ Deployment success without actual deployment

---

## Before Submitting Any Section

### Final Checks
- [ ] Every claim has evidence
- [ ] Every fact has a citation or data
- [ ] No exaggerations or overselling
- [ ] Limitations are acknowledged
- [ ] Results are reproducible
- [ ] Writing is precise (not vague)

### Truth Test
Ask yourself:
- **Can I defend this claim in my defense?**
- **Would an expert agree with this statement?**
- **Is there evidence for this in my thesis?**
- **Am I being intellectually honest?**

If you answer "no" or "maybe" to any, revise the claim.

---

## Common Violations to Avoid

### Vague Claims
❌ "Significant improvement"
✅ "15.3% improvement (p < 0.01)"

### Unsupported Claims
❌ "Method X is widely used"
✅ "Method X is used in recent work [cite, cite, cite]"

### Aspirational Claims
❌ "Our system can be deployed in production"
✅ "Our system meets production latency requirements (<50ms)"

### Cherry-Picked Results
❌ Showing only best run
✅ Showing mean ± std over 5 runs

---

## Review Process

### Self-Review
1. Read your section aloud
2. Question every claim
3. Verify every citation
4. Check every number
5. Look for weasel words ("might", "could", "possibly")

### Advisor Review
- Highlight any claims you're uncertain about
- Ask for verification of technical accuracy
- Request feedback on interpretation

### Peer Review (Dissertation Committee)
- Your claims will be scrutinized
- Be prepared to defend everything
- Honesty is better than overselling

---

## Scientific Integrity

Remember:
- **Truth > Impact**
- **Accuracy > Novelty**
- **Honesty > Impressiveness**

A modest, honest dissertation is better than an impressive, dishonest one.

**Your scientific reputation depends on your integrity.**

---

## Use This Checklist

**Before every commit:**
- Review changes against this checklist

**Before every chapter submission:**
- Complete full checklist

**Before defense:**
- Verify entire dissertation meets all criteria

---

**RULE 1: Every statement must be truthful and scientifically valid.**

If you follow this rule, your dissertation will be defensible, credible, and valuable.
