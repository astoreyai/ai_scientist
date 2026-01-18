#!/usr/bin/env python3
"""
Randomization Sequence Generator for RCT

Generates block randomization sequence with concealed allocation.
Ensures balance across groups and reproducibility.

Usage:
    python code/randomization.py

Output:
    - results/randomization_sequence.csv: Complete allocation sequence
    - results/randomization_report.txt: Documentation
"""

import numpy as np
import pandas as pd
from datetime import datetime
import hashlib

# ============================================================================
# CONFIGURATION - EDIT THESE VALUES FOR YOUR STUDY
# ============================================================================

STUDY_TITLE = "My RCT Study"
TOTAL_N = 100  # Total sample size (from power analysis)
GROUPS = ["Intervention", "Control"]  # Group names
ALLOCATION_RATIO = [1, 1]  # 1:1 ratio (use [2, 1] for 2:1, etc.)
BLOCK_SIZE = 4  # Block size (must be multiple of sum(ALLOCATION_RATIO))
RANDOM_SEED = 12345  # For reproducibility - CHANGE THIS for your study
STRATIFY_BY = None  # Optional: "sex", "site", etc. (not implemented in simple version)

# ============================================================================


def validate_configuration():
    """Validate configuration parameters."""
    errors = []
    
    if TOTAL_N <= 0:
        errors.append("TOTAL_N must be positive")
    
    if len(GROUPS) != len(ALLOCATION_RATIO):
        errors.append("GROUPS and ALLOCATION_RATIO must have same length")
    
    if sum(ALLOCATION_RATIO) != BLOCK_SIZE:
        errors.append(f"BLOCK_SIZE ({BLOCK_SIZE}) must equal sum of ALLOCATION_RATIO ({sum(ALLOCATION_RATIO)})")
    
    if TOTAL_N % BLOCK_SIZE != 0:
        errors.append(f"TOTAL_N ({TOTAL_N}) must be multiple of BLOCK_SIZE ({BLOCK_SIZE})")
    
    if errors:
        print("❌ CONFIGURATION ERRORS:")
        for error in errors:
            print(f"  • {error}")
        print("\nPlease fix configuration and try again.\n")
        return False
    
    return True


def generate_block():
    """Generate a single randomization block."""
    allocations = []
    for group, ratio in zip(GROUPS, ALLOCATION_RATIO):
        allocations.extend([group] * ratio)
    
    # Shuffle within block
    np.random.shuffle(allocations)
    return allocations


def generate_sequence(n_participants, block_size):
    """Generate complete randomization sequence."""
    n_blocks = n_participants // block_size
    sequence = []
    
    for _ in range(n_blocks):
        block = generate_block()
        sequence.extend(block)
    
    return sequence


def create_allocation_dataframe(sequence):
    """Create dataframe with allocation sequence."""
    df = pd.DataFrame({
        'participant_id': range(1, len(sequence) + 1),
        'allocation': sequence,
        'block': [(i // BLOCK_SIZE) + 1 for i in range(len(sequence))],
        'position_in_block': [(i % BLOCK_SIZE) + 1 for i in range(len(sequence))],
        'enrolled': False,
        'enrollment_date': pd.NaT,
        'randomization_date': pd.NaT
    })
    
    return df


def calculate_checksum(sequence):
    """Calculate checksum for verification."""
    sequence_str = "".join(sequence)
    return hashlib.sha256(sequence_str.encode()).hexdigest()[:16]


def generate_report(df, checksum):
    """Generate randomization documentation."""
    report = f"""
═══════════════════════════════════════════════════════════════
            RANDOMIZATION SEQUENCE DOCUMENTATION
═══════════════════════════════════════════════════════════════

Study: {STUDY_TITLE}
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

───────────────────────────────────────────────────────────────
CONFIGURATION
───────────────────────────────────────────────────────────────

Total Participants:     {TOTAL_N}
Groups:                 {', '.join(GROUPS)}
Allocation Ratio:       {':'.join(map(str, ALLOCATION_RATIO))}
Block Size:             {BLOCK_SIZE}
Number of Blocks:       {TOTAL_N // BLOCK_SIZE}
Random Seed:            {RANDOM_SEED}
Checksum:               {checksum}

───────────────────────────────────────────────────────────────
ALLOCATION SUMMARY
───────────────────────────────────────────────────────────────

"""
    
    for group in GROUPS:
        count = (df['allocation'] == group).sum()
        percentage = (count / len(df)) * 100
        report += f"{group}:  {count} participants ({percentage:.1f}%)\n"
    
    report += f"""
───────────────────────────────────────────────────────────────
BALANCE VERIFICATION
───────────────────────────────────────────────────────────────

"""
    
    # Check balance within each block
    for block_num in range(1, (TOTAL_N // BLOCK_SIZE) + 1):
        block_data = df[df['block'] == block_num]
        counts = block_data['allocation'].value_counts()
        report += f"Block {block_num}: "
        report += " | ".join([f"{group}: {counts.get(group, 0)}" for group in GROUPS])
        report += "\n"
    
    report += f"""
───────────────────────────────────────────────────────────────
IMPLEMENTATION INSTRUCTIONS
───────────────────────────────────────────────────────────────

1. SECURITY:
   ✓ Store randomization_sequence.csv in secure location
   ✓ Implement concealed allocation (opaque envelopes or IWRS)
   ✓ Do NOT share sequence with enrollers/assessors

2. ENROLLMENT:
   ✓ Screen participant
   ✓ Obtain informed consent
   ✓ Collect baseline data
   ✓ Assign next available participant_id

3. RANDOMIZATION:
   ✓ Open sealed envelope for participant_id
   ✓ Assign to indicated group
   ✓ Record allocation date
   ✓ Update randomization_sequence.csv

4. BLINDING:
   ✓ Keep allocation concealed from outcome assessors
   ✓ Do not reveal allocation in data collection forms
   ✓ Store allocation separately from outcome data

5. MONITORING:
   ✓ Track enrollment by group
   ✓ Verify balance periodically
   ✓ Document any protocol deviations

───────────────────────────────────────────────────────────────
REPRODUCIBILITY
───────────────────────────────────────────────────────────────

This sequence can be reproduced exactly using:
  - Python version: {np.__version__}
  - Random seed: {RANDOM_SEED}
  - Configuration: As specified above

To verify: Run this script again with same RANDOM_SEED
Expected checksum: {checksum}

───────────────────────────────────────────────────────────────
CONSORT REPORTING
───────────────────────────────────────────────────────────────

Include in manuscript methods section:

"Participants were randomized {':'.join(map(str, ALLOCATION_RATIO))} to 
{' or '.join(GROUPS)} using block randomization (block size = {BLOCK_SIZE}). 
The allocation sequence was computer-generated (Python NumPy, seed = {RANDOM_SEED}) 
prior to study initiation. Allocation was concealed using [DESCRIBE METHOD: 
opaque envelopes / web-based IWRS / pharmacy-controlled]. [DESCRIBE WHO WAS 
BLINDED: Participants, care providers, outcome assessors] were blinded to 
group allocation."

───────────────────────────────────────────────────────────────

Randomization sequence generated using Research Assistant v1.1.0
Report generated: {datetime.now().isoformat()}
"""
    
    return report


def main():
    """Generate randomization sequence."""
    print("═══════════════════════════════════════════════════════════════")
    print("              RANDOMIZATION SEQUENCE GENERATOR")
    print("═══════════════════════════════════════════════════════════════\n")
    
    print(f"Study: {STUDY_TITLE}\n")
    
    # Validate configuration
    print("Validating configuration...")
    if not validate_configuration():
        return
    
    print("✓ Configuration valid\n")
    
    # Set random seed
    print(f"Setting random seed: {RANDOM_SEED}")
    np.random.seed(RANDOM_SEED)
    
    # Generate sequence
    print(f"Generating sequence for {TOTAL_N} participants...")
    sequence = generate_sequence(TOTAL_N, BLOCK_SIZE)
    
    # Create dataframe
    df = create_allocation_dataframe(sequence)
    
    # Calculate checksum
    checksum = calculate_checksum(sequence)
    print(f"✓ Sequence generated (checksum: {checksum})\n")
    
    # Summary
    print("Allocation summary:")
    for group in GROUPS:
        count = (df['allocation'] == group).sum()
        percentage = (count / len(df)) * 100
        print(f"  {group}: {count} participants ({percentage:.1f}%)")
    
    # Save sequence
    print("\nSaving sequence...")
    df.to_csv('../results/randomization_sequence.csv', index=False)
    print("✓ Sequence saved to results/randomization_sequence.csv")
    
    # Generate report
    print("Generating documentation...")
    report = generate_report(df, checksum)
    
    with open('../results/randomization_report.txt', 'w') as f:
        f.write(report)
    
    print("✓ Report saved to results/randomization_report.txt\n")
    
    # Display report
    print(report)
    
    print("\n═══════════════════════════════════════════════════════════════")
    print("⚠️  IMPORTANT SECURITY NOTES:")
    print("═══════════════════════════════════════════════════════════════")
    print("1. Store randomization_sequence.csv in SECURE location")
    print("2. Implement CONCEALED allocation (opaque envelopes/IWRS)")
    print("3. Do NOT share sequence with study personnel")
    print("4. Keep allocation separate from outcome data")
    print("5. Include allocation concealment in protocol/IRB")
    print("═══════════════════════════════════════════════════════════════\n")
    
    print("NEXT STEPS:")
    print("1. Review randomization_report.txt")
    print("2. Prepare allocation concealment method")
    print("3. Update docs/protocol.md with randomization details")
    print("4. Submit protocol amendment if needed")
    print("5. Begin participant enrollment\n")


if __name__ == "__main__":
    main()
