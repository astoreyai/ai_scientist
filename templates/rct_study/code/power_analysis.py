#!/usr/bin/env python3
"""
Power Analysis for RCT

Calculates required sample size for primary outcome using statsmodels.
Generates NIH-formatted justification.

Usage:
    python code/power_analysis.py

Output:
    - Console: Sample size calculation
    - results/power_analysis_report.txt: Formal report
"""

from statsmodels.stats.power import TTestIndPower
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# ============================================================================
# CONFIGURATION - EDIT THESE VALUES FOR YOUR STUDY
# ============================================================================

STUDY_TITLE = "My RCT Study"
EXPECTED_EFFECT_SIZE = 0.5  # Cohen's d (0.2=small, 0.5=medium, 0.8=large)
ALPHA = 0.05  # Type I error rate
POWER = 0.80  # Desired statistical power (0.80 = 80%)
TEST_TYPE = "two-sided"  # "two-sided" or "one-sided"
ALLOCATION_RATIO = 1.0  # 1.0 for 1:1, 2.0 for 2:1, etc.
ANTICIPATED_ATTRITION = 0.20  # 20% expected dropout

# ============================================================================


def calculate_sample_size():
    """Calculate required sample size."""
    analysis = TTestIndPower()
    
    # Calculate sample size for one group
    n_per_group = analysis.solve_power(
        effect_size=EXPECTED_EFFECT_SIZE,
        alpha=ALPHA,
        power=POWER,
        ratio=ALLOCATION_RATIO,
        alternative=TEST_TYPE
    )
    
    # Round up to nearest integer
    n_per_group = int(np.ceil(n_per_group))
    
    # Total N
    if ALLOCATION_RATIO == 1.0:
        total_n = n_per_group * 2
    else:
        total_n = int(n_per_group * (1 + ALLOCATION_RATIO))
    
    # Adjust for attrition
    n_per_group_adjusted = int(np.ceil(n_per_group / (1 - ANTICIPATED_ATTRITION)))
    total_n_adjusted = n_per_group_adjusted * 2 if ALLOCATION_RATIO == 1.0 else int(n_per_group_adjusted * (1 + ALLOCATION_RATIO))
    
    return {
        "n_per_group": n_per_group,
        "total_n": total_n,
        "n_per_group_adjusted": n_per_group_adjusted,
        "total_n_adjusted": total_n_adjusted
    }


def sensitivity_analysis():
    """Calculate power for range of effect sizes."""
    analysis = TTestIndPower()
    effect_sizes = np.arange(0.2, 1.0, 0.1)
    
    results = calculate_sample_size()
    n = results["n_per_group"]
    
    powers = [
        analysis.solve_power(
            effect_size=d,
            nobs1=n,
            alpha=ALPHA,
            ratio=ALLOCATION_RATIO,
            alternative=TEST_TYPE
        )
        for d in effect_sizes
    ]
    
    return effect_sizes, powers


def generate_power_curve(effect_sizes, powers):
    """Generate power curve visualization."""
    plt.figure(figsize=(10, 6))
    plt.plot(effect_sizes, powers, 'b-', linewidth=2)
    plt.axhline(y=0.80, color='r', linestyle='--', label='Target power (0.80)')
    plt.axvline(x=EXPECTED_EFFECT_SIZE, color='g', linestyle='--', label=f'Expected d = {EXPECTED_EFFECT_SIZE}')
    plt.xlabel('Effect Size (Cohen\'s d)', fontsize=12)
    plt.ylabel('Statistical Power', fontsize=12)
    plt.title(f'Power Curve for {STUDY_TITLE}', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.ylim(0, 1)
    
    # Save figure
    plt.savefig('../results/figures/power_curve.png', dpi=300, bbox_inches='tight')
    print("✓ Power curve saved to results/figures/power_curve.png")


def generate_report(results):
    """Generate formal NIH-style report."""
    report = f"""
═══════════════════════════════════════════════════════════════
                POWER ANALYSIS REPORT
═══════════════════════════════════════════════════════════════

Study: {STUDY_TITLE}
Date: {datetime.now().strftime("%Y-%m-%d")}

───────────────────────────────────────────────────────────────
DESIGN PARAMETERS
───────────────────────────────────────────────────────────────

Statistical Test:        Independent samples t-test ({TEST_TYPE})
Expected Effect Size:    Cohen's d = {EXPECTED_EFFECT_SIZE}
Alpha (Type I error):    {ALPHA}
Power (1 - β):           {POWER}
Allocation Ratio:        {ALLOCATION_RATIO}:1
Anticipated Attrition:   {ANTICIPATED_ATTRITION*100:.0f}%

───────────────────────────────────────────────────────────────
SAMPLE SIZE RESULTS
───────────────────────────────────────────────────────────────

Required N (per group):      {results["n_per_group"]} participants
Required N (total):          {results["total_n"]} participants

Adjusted for Attrition:
Required N (per group):      {results["n_per_group_adjusted"]} participants
Required N (total):          {results["total_n_adjusted"]} participants

───────────────────────────────────────────────────────────────
NIH-FORMATTED JUSTIFICATION
───────────────────────────────────────────────────────────────

Sample size was determined using G*Power 3.1 for an independent 
samples t-test. To detect a {"small" if EXPECTED_EFFECT_SIZE < 0.4 else "medium" if EXPECTED_EFFECT_SIZE < 0.7 else "large"} effect 
(Cohen's d = {EXPECTED_EFFECT_SIZE}) with {int(POWER*100)}% power and alpha = {ALPHA}, 
we require {results["n_per_group"]} participants per group ({results["total_n"]} total). 

Accounting for anticipated {int(ANTICIPATED_ATTRITION*100)}% attrition based on 
similar studies in this population, we will recruit {results["n_per_group_adjusted"]} 
participants per group ({results["total_n_adjusted"]} total).

This sample size provides adequate power to detect clinically 
meaningful differences in the primary outcome.

───────────────────────────────────────────────────────────────
SENSITIVITY ANALYSIS
───────────────────────────────────────────────────────────────

Power to detect different effect sizes with N={results["n_per_group"]} per group:

"""
    
    # Add sensitivity results
    effect_sizes, powers = sensitivity_analysis()
    for d, p in zip(effect_sizes, powers):
        report += f"  d = {d:.2f}:  Power = {p:.3f} ({int(p*100)}%)\n"
    
    report += f"""
───────────────────────────────────────────────────────────────
RECOMMENDATIONS
───────────────────────────────────────────────────────────────

✓ RECRUIT: {results["total_n_adjusted"]} participants ({results["n_per_group_adjusted"]} per group)
✓ RANDOMIZE: {ALLOCATION_RATIO}:1 allocation
✓ PRE-REGISTER: Specify this sample size in pre-registration
✓ MONITOR: Track attrition during study

───────────────────────────────────────────────────────────────

Power analysis conducted using statsmodels {datetime.now().year}
Report generated: {datetime.now().isoformat()}
"""
    
    return report


def main():
    """Run complete power analysis."""
    print("═══════════════════════════════════════════════════════════════")
    print("                   POWER ANALYSIS FOR RCT")
    print("═══════════════════════════════════════════════════════════════\n")
    
    print(f"Study: {STUDY_TITLE}")
    print(f"Expected effect size: d = {EXPECTED_EFFECT_SIZE}")
    print(f"Alpha: {ALPHA}, Power: {POWER}\n")
    
    # Calculate sample size
    print("Calculating required sample size...")
    results = calculate_sample_size()
    
    print(f"\n✓ Required N (per group): {results['n_per_group']}")
    print(f"✓ Required N (total): {results['total_n']}")
    print(f"\nAdjusted for {int(ANTICIPATED_ATTRITION*100)}% attrition:")
    print(f"✓ Recruit: {results['n_per_group_adjusted']} per group ({results['total_n_adjusted']} total)\n")
    
    # Sensitivity analysis
    print("Running sensitivity analysis...")
    effect_sizes, powers = sensitivity_analysis()
    
    # Generate power curve
    print("Generating power curve...")
    generate_power_curve(effect_sizes, powers)
    
    # Generate formal report
    print("Generating formal report...")
    report = generate_report(results)
    
    # Save report
    with open('../results/power_analysis_report.txt', 'w') as f:
        f.write(report)
    
    print("✓ Report saved to results/power_analysis_report.txt\n")
    
    print(report)
    
    print("\n═══════════════════════════════════════════════════════════════")
    print("NEXT STEPS:")
    print("1. Review sensitivity analysis")
    print("2. Include justification in grant/protocol")
    print("3. Update docs/protocol.md with sample size")
    print("4. Generate randomization sequence: python code/randomization.py")
    print("═══════════════════════════════════════════════════════════════\n")


if __name__ == "__main__":
    main()
