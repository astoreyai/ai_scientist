# Network Meta-Analysis in R using netmeta
# Template Code with Annotations

# ============================================================================
# SETUP
# ============================================================================

# Install packages (run once)
# install.packages("netmeta")
# install.packages("meta")
# install.packages("dplyr")

# Load libraries
library(netmeta)
library(meta)
library(dplyr)

# ============================================================================
# 1. PREPARE DATA
# ============================================================================

# Data format: One row per comparison (2-arm or multi-arm trials)
# Required columns:
#   - study: Study ID
#   - treat1: Treatment 1 name
#   - treat2: Treatment 2 name  
#   - TE: Treatment effect (e.g., SMD, log OR, MD)
#   - seTE: Standard error of treatment effect

# Example: Depression treatments (CBT, SSRI, Mindfulness, Exercise, Placebo)
nma_data <- data.frame(
  study = c("Smith2019", "Jones2020", "Garcia2018", "Chen2021", "Lee2022",
            "Park2020", "Wilson2019", "Taylor2023", "Brown2017"),
  treat1 = c("CBT", "SSRI", "CBT", "Mindfulness", "Exercise",
             "CBT", "SSRI", "Mindfulness", "Exercise"),
  treat2 = c("Placebo", "Placebo", "Placebo", "Placebo", "Placebo",
             "SSRI", "Placebo", "Placebo", "Placebo"),
  TE = c(-0.52, -0.61, -0.45, -0.38, -0.33,
         -0.08, -0.55, -0.41, -0.36),  # Standardized mean difference
  seTE = c(0.14, 0.11, 0.18, 0.17, 0.15,
           0.22, 0.13, 0.19, 0.14),
  n1 = c(60, 80, 45, 52, 65, 50, 90, 48, 70),  # Sample size arm 1
  n2 = c(58, 82, 43, 50, 63, 48, 88, 46, 68)   # Sample size arm 2
)

# View data
head(nma_data)

# ============================================================================
# 2. CONDUCT NETWORK META-ANALYSIS
# ============================================================================

# Run network meta-analysis (random effects model)
nma <- netmeta(
  TE = TE,                    # Treatment effect
  seTE = seTE,                # Standard error
  treat1 = treat1,            # Treatment 1
  treat2 = treat2,            # Treatment 2
  studlab = study,            # Study labels
  data = nma_data,
  sm = "SMD",                 # Summary measure (SMD, OR, MD, etc.)
  reference.group = "Placebo", # Reference treatment for forest plot
  comb.fixed = FALSE,         # Don't use fixed effect model
  comb.random = TRUE,         # Use random effects model
  tol.multiarm = 0.05         # Tolerance for multi-arm trials
)

# Print summary
summary(nma)

# ============================================================================
# 3. NETWORK GEOMETRY
# ============================================================================

# Plot network
netgraph(nma, 
         points = TRUE,              # Show treatment nodes
         cex.points = 5,             # Node size
         col = "steelblue",          # Node color
         number.of.studies = TRUE,   # Show # studies on edges
         plastic = FALSE,            # Use straight lines
         thickness = "number.of.studies",  # Edge thickness by # studies
         cex = 1.2)                  # Text size

# Get network characteristics
print(paste("Number of treatments:", nma$n))
print(paste("Number of studies:", nma$k))
print(paste("Number of comparisons with direct evidence:", nma$m))

# ============================================================================
# 4. FOREST PLOT (All treatments vs. reference)
# ============================================================================

# Forest plot: All treatments compared to placebo
forest(nma, 
       reference.group = "Placebo",
       sortvar = TE,               # Sort by effect size
       smlab = "Treatment vs. Placebo\n(Standardized Mean Difference)",
       drop.reference.group = FALSE,
       xlab = "Favors Treatment  ←  →  Favors Placebo",
       col.square = "steelblue",
       col.square.lines = "steelblue",
       col.diamond = "darkred",
       col.diamond.lines = "darkred")

# ============================================================================
# 5. LEAGUE TABLE (All pairwise comparisons)
# ============================================================================

# Generate league table
league <- netleague(nma, 
                    digits = 2,
                    bracket = "(")

# Print league table (SMD with 95% CI)
print(league$random)  # Random effects results

# Export to CSV
write.csv(league$random, "league_table.csv", row.names = TRUE)

# ============================================================================
# 6. RANKING TREATMENTS (SUCRA / P-scores)
# ============================================================================

# Calculate treatment rankings
rankings <- netrank(nma, small.values = "desirable")  # Lower values = better

# Print rankings
print(rankings)

# Plot ranking (P-scores)
plot(rankings, 
     main = "Treatment Rankings (P-scores)",
     xlab = "P-score (%)",
     col = "steelblue")

# Extract P-scores
pscores <- rankings$Pscore.random
print("P-scores (0-100%, higher = better):")
print(sort(pscores, decreasing = TRUE))

# ============================================================================
# 7. ASSESS HETEROGENEITY
# ============================================================================

# Heterogeneity statistics
cat("\nHeterogeneity Assessment:\n")
cat(paste("τ² =", round(nma$tau^2, 3), "\n"))
cat(paste("I² =", round(nma$I2, 1), "%\n"))

# Interpretation
if (nma$I2 < 25) {
  cat("Interpretation: Low heterogeneity\n")
} else if (nma$I2 < 50) {
  cat("Interpretation: Moderate heterogeneity\n")
} else if (nma$I2 < 75) {
  cat("Interpretation: Substantial heterogeneity\n")
} else {
  cat("Interpretation: Considerable heterogeneity\n")
}

# ============================================================================
# 8. ASSESS CONSISTENCY (Global & Local)
# ============================================================================

# Global inconsistency test (design-by-treatment interaction)
decomp <- decomp.design(nma)
print(decomp)

cat("\nGlobal Inconsistency Test:\n")
cat(paste("Q statistic:", round(decomp$Q.inc.random, 2), "\n"))
cat(paste("p-value:", round(decomp$pval.Q.inc.random, 4), "\n"))

if (decomp$pval.Q.inc.random > 0.05) {
  cat("Interpretation: No significant inconsistency detected (p > 0.05)\n")
} else {
  cat("WARNING: Significant inconsistency detected (p < 0.05)\n")
  cat("Action: Investigate with node-splitting\n")
}

# Local inconsistency test (node-splitting)
# For each comparison with both direct and indirect evidence
netsplit_results <- netsplit(nma)
print(netsplit_results)

# Plot node-splitting results
forest(netsplit_results, 
       show = "both",  # Show direct, indirect, and network estimates
       col.diamond = c("blue", "red", "green"))

# ============================================================================
# 9. COMPARISON-ADJUSTED FUNNEL PLOT (Publication Bias)
# ============================================================================

# Funnel plot for network meta-analysis
funnel(nma, 
       order = pscores,  # Order by treatment ranking
       col = "steelblue",
       main = "Comparison-Adjusted Funnel Plot")

# Egger's test for small-study effects (adapted for NMA)
# Note: This is an approximation, interpret with caution
# metabias(nma, method.bias = "Egger")

# ============================================================================
# 10. SENSITIVITY ANALYSES
# ============================================================================

# Example: Exclude high risk of bias studies
# Assume we have risk of bias indicator
nma_data_lowrob <- nma_data %>%
  filter(!(study %in% c("Brown2017")))  # Example: exclude one study

# Re-run NMA
nma_sensitivity <- netmeta(
  TE = TE, seTE = seTE, treat1 = treat1, treat2 = treat2, 
  studlab = study, data = nma_data_lowrob, sm = "SMD", 
  reference.group = "Placebo", comb.fixed = FALSE, comb.random = TRUE
)

# Compare rankings
rankings_main <- netrank(nma, small.values = "desirable")
rankings_sens <- netrank(nma_sensitivity, small.values = "desirable")

cat("\nSensitivity Analysis: Ranking Comparison\n")
cat("Main Analysis P-scores:\n")
print(sort(rankings_main$Pscore.random, decreasing = TRUE))
cat("\nSensitivity Analysis P-scores (excluding high RoB):\n")
print(sort(rankings_sens$Pscore.random, decreasing = TRUE))

# ============================================================================
# 11. EXPORT RESULTS
# ============================================================================

# Create summary data frame
results_summary <- data.frame(
  Comparison = rownames(nma$TE.random),
  SMD = round(nma$TE.random[, "Placebo"], 2),
  Lower_CI = round(nma$lower.random[, "Placebo"], 2),
  Upper_CI = round(nma$upper.random[, "Placebo"], 2),
  P_value = round(nma$pval.random[, "Placebo"], 4)
)

# Remove NA rows (reference treatment)
results_summary <- results_summary[complete.cases(results_summary), ]

# Add P-scores
results_summary$P_score <- round(pscores[results_summary$Comparison], 1)

# View
print(results_summary)

# Export to CSV
write.csv(results_summary, "nma_results_summary.csv", row.names = FALSE)

# Export network graph as PDF
pdf("network_graph.pdf", width = 8, height = 6)
netgraph(nma, points = TRUE, cex.points = 5, col = "steelblue", 
         number.of.studies = TRUE, plastic = FALSE)
dev.off()

# Export forest plot as PDF
pdf("forest_plot.pdf", width = 10, height = 6)
forest(nma, reference.group = "Placebo", sortvar = TE,
       smlab = "Treatment vs. Placebo (SMD)",
       xlab = "Favors Treatment  ←  →  Favors Placebo")
dev.off()

# Export ranking plot as PDF
pdf("ranking_plot.pdf", width = 8, height = 6)
plot(rankings, main = "Treatment Rankings", xlab = "P-score (%)", 
     col = "steelblue")
dev.off()

cat("\n=== Analysis Complete ===\n")
cat("Outputs saved:\n")
cat("  - league_table.csv\n")
cat("  - nma_results_summary.csv\n")
cat("  - network_graph.pdf\n")
cat("  - forest_plot.pdf\n")
cat("  - ranking_plot.pdf\n")

# ============================================================================
# ADDITIONAL NOTES
# ============================================================================

# Multi-arm trials:
# - If a study has 3+ arms, create multiple rows (one per pairwise comparison)
# - netmeta automatically accounts for correlation within multi-arm trials

# Alternative effect measures:
# - sm = "OR" for odds ratio (use log OR as TE)
# - sm = "RR" for risk ratio (use log RR as TE)
# - sm = "MD" for mean difference

# Bayesian NMA:
# - For Bayesian approach, see stan_code_template.stan
# - Use rstan or brms packages in R

# GRADE assessment:
# - Use CINeMA web app: https://cinema.ispm.unibe.ch/
# - Or manually assess: within-study bias, reporting bias, indirectness, 
#   imprecision, heterogeneity, incoherence

# ============================================================================
