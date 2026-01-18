# Network Meta-Analysis Template

**Template Type:** Network Meta-Analysis (NMA) / Mixed Treatment Comparison
**Framework:** Frequentist or Bayesian approaches
**Reporting Standard:** PRISMA-NMA Extension
**Use Case:** Compare multiple interventions simultaneously using direct and indirect evidence

---

## What is a Network Meta-Analysis?

A **network meta-analysis** (NMA) simultaneously compares multiple interventions (≥3) using both direct evidence (head-to-head trials) and indirect evidence (comparing via common comparators).

**Synonyms:**
- Mixed treatment comparison (MTC)
- Multiple treatment meta-analysis
- Network meta-analysis

**When to use NMA:**
- Multiple interventions exist for the same condition
- Few or no head-to-head comparisons between all interventions
- You need to rank interventions by effectiveness
- You want to inform treatment guidelines or decision-making

**Network Meta-Analysis vs. Pairwise Meta-Analysis:**

```
Characteristic        Pairwise MA            Network MA
────────────────────────────────────────────────────────────
Comparisons           A vs. B only           A vs. B vs. C vs. D
Evidence              Direct only            Direct + Indirect
Number of Studies     Typically more         May have sparse networks
Ranking               Not possible           Yes (SUCRA, P-scores)
Assumptions           Fewer                  Transitivity, consistency
Complexity            Lower                  Higher
Software              Standard (R metafor)   Specialized (netmeta, Stan)
────────────────────────────────────────────────────────────
```

---

## Key Concepts

### 1. Network Geometry

The **network** is a visual representation of the evidence:
- **Nodes:** Interventions
- **Edges:** Direct comparisons (at least one trial)
- **Edge thickness:** Number of studies
- **Node size:** Number of patients

**Example Network:**
```
        CBT (n=12 studies)
       /   |   \
      /    |    \
     /     |     \
  SSRI   Placebo   Mindfulness
    \      |      /
     \     |     /
      \    |    /
        Exercise

Connections:
- CBT vs. Placebo: 8 RCTs (direct)
- SSRI vs. Placebo: 15 RCTs (direct)
- CBT vs. SSRI: 3 RCTs (direct)
- Mindfulness vs. Placebo: 5 RCTs (direct)
- Exercise vs. Placebo: 7 RCTs (direct)
- CBT vs. Mindfulness: 0 RCTs (indirect via placebo)
- SSRI vs. Exercise: 0 RCTs (indirect via placebo)
```

### 2. Direct vs. Indirect Evidence

**Direct Evidence:** Head-to-head RCTs comparing A vs. B

**Indirect Evidence:** Infer A vs. B by comparing both to common comparator C
```
If: A vs. C gives effect θ_AC
And: B vs. C gives effect θ_BC
Then: A vs. B indirect effect = θ_AC - θ_BC
```

**Mixed Evidence:** Combines direct + indirect via weighted average

### 3. Transitivity Assumption

**Transitivity:** The assumption that indirect comparisons are valid.

**Requirements:**
- Trials are similar enough across the network
- Patient populations are comparable
- Intervention implementations are similar
- Effect modifiers are balanced

**Checking Transitivity:**
- Compare study characteristics across comparisons
- Assess potential effect modifiers (age, disease severity, year, etc.)
- If violated: Consider subgroup/meta-regression analysis

### 4. Consistency Assumption

**Consistency:** Direct and indirect evidence should agree.

**Example of INconsistency:**
```
Direct:    A vs. B = effect of 5 units
Indirect:  A vs. C = 10, B vs. C = 3 → A vs. B indirect = 7 units

Inconsistency: Direct (5) ≠ Indirect (7)
```

**Checking Consistency:**
- Global test (design-by-treatment interaction, Q statistic)
- Local tests (node-splitting, loop-specific inconsistency)
- If violated: Investigate sources, consider subgroup analysis or exclude problematic studies

### 5. Ranking Interventions

**SUCRA** (Surface Under the Cumulative Ranking curve):
- Range: 0-100%
- 100% = certain to be best treatment
- 0% = certain to be worst treatment
- Example: SUCRA = 85% means treatment has 85% probability of being in top ranks

**Alternative: P-scores** (frequentist analog to SUCRA)

---

## PRISMA-NMA Checklist (32 Items)

**Extension of PRISMA for NMA (Hutton et al., 2015)**

| Section | Item | Description |
|---------|------|-------------|
| **Title** | 1 | Identify as network meta-analysis |
| **Abstract** | 2 | Structured summary |
| **Introduction** | 3-4 | Rationale, objectives |
| **Methods** | 5-12 | Protocol, eligibility, sources, search, selection, data collection, data items, geometry |
| **Risk of Bias** | 13-15 | Within studies, across studies, additional assumptions |
| **Synthesis** | 16-19 | Methods, assessment of inconsistency and transitivity, presentation of network geometry |
| **Results** | 20-27 | Study selection, characteristics, risk of bias, results of syntheses, exploration of heterogeneity/inconsistency, results of sensitivity analyses |
| **Discussion** | 28-30 | Summary, limitations, conclusions |
| **Funding** | 31 | Funding sources |
| **PICO** | S1-S5 | *Supplementary*: Detailed PICO, structure, transitivity, individual study data, bibliography |

**Full checklist:** http://www.prisma-statement.org/Extensions/NetworkMetaAnalysis

---

## Network Meta-Analysis Workflow

### Stage 1: Systematic Review (PRISMA)

Same as standard systematic review:
1. Define PICO question
2. Systematic literature search
3. Study selection (title/abstract, full-text screening)
4. Data extraction
5. Risk of bias assessment

**Key Difference:** Extract data for ALL relevant interventions (not just A vs. B)

**Example:**
```
Study 1: CBT vs. Placebo
Study 2: SSRI vs. Placebo
Study 3: CBT vs. SSRI
Study 4: Mindfulness vs. Placebo
Study 5: Exercise vs. Placebo

→ All studies included in network (5 interventions total)
```

### Stage 2: Assess Feasibility of NMA

**Can you conduct an NMA?**

✓ **YES if:**
- ≥3 interventions
- Studies are sufficiently similar (transitivity)
- Network is connected (all interventions link via some path)
- Outcome measure is comparable across studies

✗ **NO if:**
- Only 2 interventions (use pairwise MA instead)
- Studies too heterogeneous (violates transitivity)
- Network is disconnected (separate sub-networks)
- Incomparable outcomes

### Stage 3: Construct Network Geometry

**Create network diagram:**

```r
# R netmeta package
library(netmeta)

# Example data
data <- data.frame(
  study = c("Study1", "Study2", "Study3", "Study4", "Study5"),
  treat1 = c("CBT", "SSRI", "CBT", "Mindfulness", "Exercise"),
  treat2 = c("Placebo", "Placebo", "SSRI", "Placebo", "Placebo"),
  TE = c(-0.5, -0.6, -0.1, -0.4, -0.35),  # Treatment effects (SMD)
  seTE = c(0.15, 0.12, 0.20, 0.18, 0.16)   # Standard errors
)

# Network meta-analysis
nma <- netmeta(TE = TE, seTE = seTE, 
               treat1 = treat1, treat2 = treat2, 
               studlab = study, data = data, 
               sm = "SMD", reference = "Placebo")

# Plot network
netgraph(nma, 
         points = TRUE, 
         cex.points = 3, 
         col = "blue", 
         number.of.studies = TRUE,
         plastic = FALSE)
```

**Assess network characteristics:**
- Connectedness: All interventions connected?
- Density: How many direct comparisons exist?
- Multi-arm trials: Trials with ≥3 arms?
- Star-shaped: One central comparator (common in drug trials)

### Stage 4: Assess Transitivity

**Compare study characteristics across comparisons:**

| Comparison | n Studies | Mean Age | % Female | Disease Severity | Year Range |
|------------|-----------|----------|----------|------------------|------------|
| CBT vs. Placebo | 8 | 42.3 | 68% | Moderate | 2015-2023 |
| SSRI vs. Placebo | 15 | 44.1 | 71% | Moderate | 2010-2023 |
| CBT vs. SSRI | 3 | 41.8 | 65% | Moderate-Severe | 2018-2022 |
| Mindfulness vs. Placebo | 5 | 39.5 | 73% | Mild-Moderate | 2017-2023 |
| Exercise vs. Placebo | 7 | 43.2 | 62% | Moderate | 2012-2023 |

**Red flags for transitivity violation:**
- Large differences in patient characteristics
- Different outcome measurement tools
- Different time points
- Systematic differences by comparison

### Stage 5: Conduct Network Meta-Analysis

**Choose Model:**

**Fixed-Effect Model:**
- Assumes one true effect across network
- Use if: Low heterogeneity (I² < 25%), few studies

**Random-Effects Model:**
- Assumes distribution of true effects
- Use if: Moderate-high heterogeneity (I² > 25%), typical choice

**Bayesian vs. Frequentist:**
```
Approach      Pros                           Cons
────────────────────────────────────────────────────────────────
Frequentist   Faster, simpler                Fewer options for
(netmeta)     interpretation, no priors      complex models

Bayesian      Flexible, probabilistic        Slower, requires
(Stan, JAGS)  statements, handles sparse     MCMC, prior
              networks better                specification
────────────────────────────────────────────────────────────────
```

**R Code Example (Frequentist):**

```r
library(netmeta)

# Network meta-analysis (random effects)
nma <- netmeta(TE = TE, seTE = seTE, 
               treat1 = treat1, treat2 = treat2, 
               studlab = study, data = data, 
               sm = "SMD", 
               reference = "Placebo",
               comb.fixed = FALSE,  # No fixed effect
               comb.random = TRUE)  # Random effects

# Summary
summary(nma)

# Network plot
netgraph(nma)

# Forest plot (all treatments vs. placebo)
forest(nma, reference.group = "Placebo")

# League table
netleague(nma, digits = 2)

# Ranking (SUCRA)
netrank(nma)
```

**Expected Output:**

```
Network Meta-Analysis (Random Effects Model)

Reference: Placebo

Treatment Effects (SMD, 95% CI):
  CBT vs. Placebo:          -0.48 (-0.65, -0.31)
  SSRI vs. Placebo:         -0.58 (-0.72, -0.44)
  Mindfulness vs. Placebo:  -0.39 (-0.58, -0.20)
  Exercise vs. Placebo:     -0.34 (-0.51, -0.17)
  CBT vs. SSRI:             0.10 (-0.15, 0.35)  [Mixed evidence]
  
Heterogeneity:
  τ² = 0.024 (moderate)
  I² = 54.2%
  
Ranking (P-scores):
  1. SSRI (84%)
  2. CBT (72%)
  3. Mindfulness (46%)
  4. Exercise (38%)
  5. Placebo (10%)
```

### Stage 6: Assess Consistency

**Global Inconsistency Test:**

```r
# Design-by-treatment interaction test
decomp.design(nma)

# Q statistic for inconsistency
# p > 0.05: No evidence of inconsistency (good)
# p < 0.05: Evidence of inconsistency (investigate)
```

**Local Inconsistency: Node-Splitting**

```r
# Split each comparison into direct and indirect evidence
netsplit(nma)

# For each comparison, test if direct ≠ indirect
# p > 0.05: Consistent (good)
# p < 0.05: Inconsistent (investigate why)
```

**If Inconsistency Detected:**
1. Check for outlier studies
2. Examine transitivity violations
3. Consider subgroup analysis
4. May need to exclude problematic studies or comparisons

### Stage 7: Sensitivity Analyses

**Recommended Sensitivity Analyses:**

1. **Exclude high risk of bias studies**
   - Re-run NMA excluding studies with high RoB
   - Compare results to main analysis

2. **Alternative outcome time points**
   - E.g., 8 weeks vs. 12 weeks
   - Assess if choice affects ranking

3. **Different priors (if Bayesian)**
   - Vague vs. informative priors
   - Assess sensitivity to prior choice

4. **Fixed vs. random effects**
   - Compare results under both models

5. **Exclude multi-arm trials**
   - May introduce correlation, assess impact

### Stage 8: Create Visualizations

**1. Network Geometry Plot**
- Shows structure of evidence
- Node size = sample size
- Edge thickness = number of studies

**2. Forest Plot**
- All treatments vs. reference
- Shows pooled effects with 95% CI

**3. League Table**
- Matrix of all pairwise comparisons
- Upper triangle: Effect estimates
- Lower triangle: 95% CI

**4. Ranking Plot (SUCRA)**
- Bar chart or cumulative ranking curves
- Shows probability of each treatment being best

**5. Comparison-Adjusted Funnel Plot**
- Assess small-study effects/publication bias
- Specialized for network geometry

**6. Consistency Plot (if inconsistency)**
- Shows direct vs. indirect estimates
- Identifies inconsistent loops

---

## League Table Example

```
        Placebo    CBT           SSRI          Mindfulness   Exercise
────────────────────────────────────────────────────────────────────────
Placebo    —       -0.48*        -0.58*        -0.39*        -0.34*
                 (-0.65,-0.31) (-0.72,-0.44) (-0.58,-0.20) (-0.51,-0.17)

CBT      0.48*       —           -0.10          0.09          0.14
       (0.31,0.65)             (-0.35,0.15)  (-0.14,0.32)  (-0.07,0.35)

SSRI     0.58*     0.10           —            0.19          0.24
       (0.44,0.72)(−0.15,0.35)               (-0.05,0.43)  (0.02,0.46)

Mind.    0.39*    -0.09         -0.19            —           0.05
       (0.20,0.58)(−0.32,0.14) (-0.43,0.05)                (-0.19,0.29)

Exerc.   0.34*    -0.14         -0.24         -0.05           —
       (0.17,0.51)(−0.35,0.07) (-0.46,-0.02) (-0.29,0.19)
────────────────────────────────────────────────────────────────────────
*Statistically significant at p<0.05
Upper triangle: SMD (negative favors row treatment)
Lower triangle: SMD with 95% CI
```

**Interpretation:**
- All active treatments better than placebo (top row)
- SSRI significantly better than Exercise (0.24, p<0.05)
- CBT vs. SSRI not significantly different (-0.10, p>0.05)

---

## Ranking Interpretation (SUCRA Scores)

```
Treatment      SUCRA    Interpretation
─────────────────────────────────────────────────────────────
SSRI           84%      Highest probability of being best/near-best
CBT            72%      High probability of being effective
Mindfulness    46%      Moderate effectiveness
Exercise       38%      Below-average effectiveness
Placebo        10%      Lowest rank (reference)
─────────────────────────────────────────────────────────────

Note: SUCRA rankings should be interpreted alongside:
- Effect size magnitudes
- Clinical significance
- Certainty of evidence (GRADE)
- Patient preferences and values
```

---

## GRADE for Network Meta-Analysis

**CINeMA** (Confidence in Network Meta-Analysis) framework:

Rate certainty of evidence for each network estimate:

**Domains:**
1. **Within-study bias:** Risk of bias in included studies
2. **Reporting bias:** Publication bias, selective reporting
3. **Indirectness:** Directness of evidence to PICO
4. **Imprecision:** Width of confidence intervals
5. **Heterogeneity:** Between-study variability
6. **Incoherence:** Inconsistency between direct and indirect evidence

**Rating:**
- High certainty: ⊕⊕⊕⊕
- Moderate certainty: ⊕⊕⊕⊝
- Low certainty: ⊕⊕⊝⊝
- Very low certainty: ⊕⊝⊝⊝

---

## Template Files Included

1. **README.md** (this file) - Overview
2. **protocol_template.md** - Complete NMA protocol
3. **prisma_nma_checklist.md** - PRISMA-NMA 32-item checklist
4. **r_code_template.R** - Annotated R code (netmeta package)
5. **stan_code_template.stan** - Bayesian NMA (Stan)
6. **data_extraction_form.md** - NMA-specific extraction form
7. **consistency_assessment.md** - Step-by-step consistency checking

---

## Common Mistakes to Avoid

1. **Assuming transitivity without checking** - Always compare study characteristics
2. **Ignoring inconsistency** - Test and report consistency
3. **Over-interpreting rankings** - SUCRA/P-scores are probabilistic, not definitive
4. **Mixing incompatible outcomes** - Ensure outcome measures are comparable
5. **Not assessing certainty** - Use GRADE/CINeMA framework
6. **Ignoring disconnected networks** - Check all interventions are linked
7. **Not reporting network geometry** - Essential for understanding evidence base

---

## Key References

**Methodology:**
- Salanti G. Indirect and mixed-treatment comparison, network, or multiple-treatments meta-analysis: many names, many benefits, many concerns for the next generation evidence synthesis tool. *Res Synth Methods*. 2012;3(2):80-97.
- Rücker G, Schwarzer G. Ranking treatments in frequentist network meta-analysis works without resampling methods. *BMC Med Res Methodol*. 2015;15:58.
- Dias S, et al. Evidence synthesis for decision making 2: a generalized linear modeling framework for pairwise and network meta-analysis of randomized controlled trials. *Med Decis Making*. 2013;33(5):607-617.

**Reporting:**
- Hutton B, et al. The PRISMA Extension Statement for Reporting of Systematic Reviews Incorporating Network Meta-analyses of Health Care Interventions: Checklist and Explanations. *Ann Intern Med*. 2015;162(11):777-784. [PRISMA-NMA](http://www.prisma-statement.org/Extensions/NetworkMetaAnalysis)

**GRADE for NMA:**
- Salanti G, et al. Evaluating the quality of evidence from a network meta-analysis. *PLoS One*. 2014;9(7):e99682.
- CINeMA: Confidence in Network Meta-Analysis [webapp.imbi.uni-freiburg.de/cinema/](https://cinema.ispm.unibe.ch/)

**Software:**
- Rücker G, Schwarzer G. netmeta: Network Meta-Analysis using Frequentist Methods. R package. [CRAN](https://cran.r-project.org/package=netmeta)
- Dias S, et al. NICE DSU Technical Support Documents on Evidence Synthesis. [nicedsu.org.uk](http://www.nicedsu.org.uk/)

---

**Need Help?** See Tutorial 10 (Meta-Analysis) for foundational meta-analysis concepts.

---

*This template follows PRISMA-NMA (2015) reporting guidelines and incorporates best practices for frequentist and Bayesian network meta-analysis.*
