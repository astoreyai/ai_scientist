# List Research Protocols and Checklists

Display available research protocols, reporting guidelines, and compliance checklists.

## Instructions

1. Read protocol files from `.claude/protocols/`
2. List all available protocols with their purpose
3. Show key compliance requirements for each
4. Provide quick access information
5. Include links to official documentation

## Available Protocols

### PRISMA 2020 (Systematic Reviews)
- **File**: `.claude/protocols/prisma_2020_checklist.md`
- **Purpose**: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
- **Items**: 27-item checklist
- **Sections**: Title, Abstract, Introduction, Methods (11 items), Results (6 items), Discussion (4 items)
- **Required**: For all systematic reviews and meta-analyses
- **Official**: https://www.prisma-statement.org

### NIH Rigor and Reproducibility Standards
- **File**: `.claude/protocols/nih_rigor_checklist.md`
- **Purpose**: NIH-required rigor and reproducibility standards for experimental design
- **Requirements**:
  - Robust experimental design (controls, randomization, blinding)
  - Power analysis ≥80%
  - Sex as biological variable (SABV)
  - Pre-registration before data collection
  - FAIR-compliant data management
- **Target**: ≥90% compliance required
- **Official**: https://grants.nih.gov/policy-and-compliance/policy-topics/reproducibility

### Additional Reporting Guidelines Referenced

**CONSORT** (RCTs):
- 30-item checklist for randomized controlled trials
- Flow diagram for participant allocation
- See templates/rct_study/ for full template

**STROBE** (Observational Studies):
- 22-item checklist for cohort, case-control, and cross-sectional studies
- See templates/observational_study/ for full template

**SQUIRE 2.0** (Quality Improvement):
- 18-item checklist for quality improvement reports
- See templates/quality_improvement/ for full template

**COREQ** (Qualitative Research):
- 32-item checklist for qualitative research interviews and focus groups
- See tutorials/09_qualitative_research/ for guidance

**PRECIS-2** (Pragmatic Trials):
- 9-domain scoring tool for pragmatic trial design
- See templates/pragmatic_trial/ for full template

## Output Format

Present as a well-organized reference guide:

```
📋 Research Protocols & Compliance Checklists

SYSTEMATIC REVIEWS & META-ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 PRISMA 2020 (27 items)
   Purpose: Systematic review and meta-analysis reporting
   Sections: Title, Abstract, Methods (11), Results (6), Discussion (4)
   File: .claude/protocols/prisma_2020_checklist.md
   Official: https://www.prisma-statement.org

EXPERIMENTAL RIGOR & REPRODUCIBILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 NIH Rigor Standards
   Purpose: Experimental design rigor and reproducibility
   Requirements:
   ✓ Power analysis ≥80%
   ✓ Pre-registration (OSF/ClinicalTrials.gov)
   ✓ Sex as biological variable (SABV)
   ✓ FAIR data management
   ✓ Public code/data sharing
   File: .claude/protocols/nih_rigor_checklist.md
   Target: ≥90% compliance
   Official: https://grants.nih.gov/policy/reproducibility

STUDY-SPECIFIC REPORTING GUIDELINES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONSORT (RCTs) - 30 items → /templates for full template
📌 STROBE (Observational) - 22 items → /templates for full template
📌 SQUIRE 2.0 (QI) - 18 items → /templates for full template
📌 COREQ (Qualitative) - 32 items → /tutorials for guidance
📌 PRECIS-2 (Pragmatic) - 9 domains → /templates for full template

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Usage:
   View protocol: Read .claude/protocols/[protocol-name].md
   Use in workflow: Agents automatically check compliance
   Get template: /templates for study-specific templates

🎯 Quality Assurance:
   /agent quality-assurance - Validates protocol adherence
   /skill ai-check - Detects AI-generated text

📚 Learn More: /tutorials for step-by-step protocol application
```

## Implementation Notes

- Read from: `/home/aaron/github/astoreyai/ai_scientist/.claude/protocols/`
- List protocols in order of frequency of use
- Include compliance targets and requirements
- Cross-reference with templates and tutorials
- Provide official URLs for authoritative guidance
