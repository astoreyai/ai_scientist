#!/usr/bin/env python3
"""
Protocol Registration Helper

Interactive tool for PROSPERO or OSF protocol registration.
Ensures protocol is registered BEFORE database searches (PRISMA requirement).

Usage:
    python code/register_protocol.py
"""

import yaml
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class ProtocolRegistration:
    """
    Guide users through systematic review protocol registration.
    
    Supports:
    - PROSPERO (health-related reviews)
    - OSF (any field)
    """
    
    def __init__(self):
        self.protocol_data = {}
        
    def run_interactive(self):
        """Run interactive registration workflow."""
        print("═══════════════════════════════════════════════════════════════")
        print("        SYSTEMATIC REVIEW PROTOCOL REGISTRATION")
        print("═══════════════════════════════════════════════════════════════\n")
        
        print("CRITICAL: Protocol must be registered BEFORE database searches.")
        print("This is a PRISMA 2020 requirement (Item 24a).\n")
        
        # Choose registry
        registry = self._choose_registry()
        
        # Collect core information
        self._collect_title()
        self._collect_team()
        self._collect_picos()
        self._collect_methods()
        self._collect_analysis_plan()
        self._collect_timeline()
        
        # Generate registration documents
        self._generate_protocol_document()
        
        if registry == "PROSPERO":
            self._generate_prospero_form()
        else:
            self._generate_osf_project()
        
        # Save data
        self._save_protocol_data()
        
        print("\n═══════════════════════════════════════════════════════════════")
        print("NEXT STEPS:")
        print("═══════════════════════════════════════════════════════════════")
        if registry == "PROSPERO":
            print("1. Go to: https://www.crd.york.ac.uk/prospero/")
            print("2. Create account / log in")
            print("3. Click 'Register new review'")
            print("4. Copy/paste from: docs/prospero_registration_form.txt")
            print("5. Submit for approval (usually 2-7 days)")
            print("6. Add registration number to docs/protocol_registration.md")
        else:
            print("1. Go to: https://osf.io")
            print("2. Create account / log in")
            print("3. Click 'Create new project'")
            print("4. Upload: docs/protocol.md")
            print("5. Make project public")
            print("6. Copy registration DOI to docs/protocol_registration.md")
        print("\n⚠️  DO NOT run database searches until protocol is registered!\n")
    
    def _choose_registry(self) -> str:
        """Choose between PROSPERO and OSF."""
        print("Choose registry:")
        print("1. PROSPERO (health/medical systematic reviews)")
        print("2. OSF (any field, faster registration)\n")
        
        while True:
            choice = input("Enter choice (1 or 2): ").strip()
            if choice == "1":
                print("\n✓ Using PROSPERO")
                print("Note: PROSPERO requires health-related research questions")
                print("      Review process takes 2-7 days\n")
                return "PROSPERO"
            elif choice == "2":
                print("\n✓ Using OSF")
                print("Note: OSF accepts any field, instant registration\n")
                return "OSF"
            else:
                print("Invalid choice. Enter 1 or 2.")
    
    def _collect_title(self):
        """Collect review title."""
        print("─────────────────────────────────────────────────────────────")
        print("REVIEW TITLE")
        print("─────────────────────────────────────────────────────────────")
        print("Title should identify this as a systematic review/meta-analysis")
        print("Example: 'Cognitive Behavioral Therapy for Depression: A Systematic Review and Meta-Analysis'\n")
        
        title = input("Review title: ").strip()
        self.protocol_data['title'] = title
        print(f"\n✓ Title: {title}\n")
    
    def _collect_team(self):
        """Collect team member information."""
        print("─────────────────────────────────────────────────────────────")
        print("REVIEW TEAM")
        print("─────────────────────────────────────────────────────────────")
        
        team = []
        
        # Lead author
        print("Lead author:")
        lead_name = input("  Name: ").strip()
        lead_email = input("  Email: ").strip()
        lead_affiliation = input("  Affiliation: ").strip()
        
        team.append({
            'name': lead_name,
            'email': lead_email,
            'affiliation': lead_affiliation,
            'role': 'Lead reviewer'
        })
        
        # Additional members
        print("\nAdditional team members (press Enter when done):")
        while True:
            name = input("  Name (or Enter to finish): ").strip()
            if not name:
                break
            email = input("  Email: ").strip()
            affiliation = input("  Affiliation: ").strip()
            role = input("  Role (e.g., Co-reviewer, Statistician): ").strip()
            
            team.append({
                'name': name,
                'email': email,
                'affiliation': affiliation,
                'role': role
            })
        
        self.protocol_data['team'] = team
        print(f"\n✓ Team: {len(team)} members\n")
    
    def _collect_picos(self):
        """Collect PICOS framework."""
        print("─────────────────────────────────────────────────────────────")
        print("PICOS FRAMEWORK")
        print("─────────────────────────────────────────────────────────────")
        print("Define your research question using PICOS:\n")
        
        population = input("Population: ").strip()
        intervention = input("Intervention/Exposure: ").strip()
        comparison = input("Comparison: ").strip()
        outcome = input("Outcome: ").strip()
        study_design = input("Study design: ").strip()
        
        self.protocol_data['picos'] = {
            'population': population,
            'intervention': intervention,
            'comparison': comparison,
            'outcome': outcome,
            'study_design': study_design
        }
        
        # Generate research question
        research_question = f"In {population}, does {intervention} compared to {comparison} affect {outcome}?"
        self.protocol_data['research_question'] = research_question
        
        print(f"\n✓ Research question: {research_question}\n")
    
    def _collect_methods(self):
        """Collect methods details."""
        print("─────────────────────────────────────────────────────────────")
        print("METHODS")
        print("─────────────────────────────────────────────────────────────\n")
        
        # Databases
        print("Which databases will you search? (comma-separated)")
        print("Examples: PubMed, Embase, Web of Science, Scopus, CENTRAL")
        databases = input("Databases: ").strip().split(',')
        databases = [db.strip() for db in databases]
        
        # Date range
        from_year = input("Search from year (e.g., 2000): ").strip()
        to_year = input("Search to year (current): ").strip() or str(datetime.now().year)
        
        # Language restrictions
        language = input("Language restrictions (e.g., English only, or 'None'): ").strip()
        
        # Grey literature
        print("\nWill you search grey literature?")
        print("Examples: trial registries, dissertations, conference proceedings")
        grey_lit = input("Grey literature sources (or 'None'): ").strip()
        
        self.protocol_data['methods'] = {
            'databases': databases,
            'date_range': {'from': from_year, 'to': to_year},
            'language': language,
            'grey_literature': grey_lit
        }
        
        print(f"\n✓ Will search {len(databases)} databases from {from_year}-{to_year}\n")
    
    def _collect_analysis_plan(self):
        """Collect analysis plan."""
        print("─────────────────────────────────────────────────────────────")
        print("ANALYSIS PLAN")
        print("─────────────────────────────────────────────────────────────\n")
        
        # Primary outcome
        primary_outcome = input("Primary outcome: ").strip()
        
        # Secondary outcomes
        print("\nSecondary outcomes (comma-separated, or 'None'):")
        secondary = input("Secondary outcomes: ").strip()
        secondary_outcomes = [s.strip() for s in secondary.split(',')] if secondary != 'None' else []
        
        # Effect measure
        print("\nEffect measure (e.g., OR, RR, SMD, MD):")
        effect_measure = input("Effect measure: ").strip()
        
        # Meta-analysis plan
        print("\nMeta-analysis method:")
        print("1. Random-effects (recommended if heterogeneity expected)")
        print("2. Fixed-effect")
        
        ma_method = input("Choice (1 or 2): ").strip()
        ma_method = "random-effects" if ma_method == "1" else "fixed-effect"
        
        # Risk of bias tool
        print("\nRisk of bias tool:")
        print("1. RoB 2 (for RCTs)")
        print("2. ROBINS-I (for non-randomized studies)")
        
        rob_tool = input("Choice (1 or 2): ").strip()
        rob_tool = "RoB 2" if rob_tool == "1" else "ROBINS-I"
        
        self.protocol_data['analysis'] = {
            'primary_outcome': primary_outcome,
            'secondary_outcomes': secondary_outcomes,
            'effect_measure': effect_measure,
            'meta_analysis_method': ma_method,
            'risk_of_bias_tool': rob_tool
        }
        
        print(f"\n✓ Analysis plan: {ma_method} meta-analysis using {rob_tool}\n")
    
    def _collect_timeline(self):
        """Collect expected timeline."""
        print("─────────────────────────────────────────────────────────────")
        print("TIMELINE")
        print("─────────────────────────────────────────────────────────────\n")
        
        start_date = input("Expected start date (YYYY-MM-DD): ").strip()
        completion_date = input("Expected completion date (YYYY-MM-DD): ").strip()
        
        self.protocol_data['timeline'] = {
            'start': start_date,
            'completion': completion_date
        }
        
        print(f"\n✓ Timeline: {start_date} to {completion_date}\n")
    
    def _generate_protocol_document(self):
        """Generate complete protocol document."""
        protocol_md = f"""# Systematic Review Protocol

## Registration Information

- **Registry**: {self.protocol_data.get('registry', 'To be determined')}
- **Registration Number**: [TO BE ADDED AFTER REGISTRATION]
- **Registration Date**: [TO BE ADDED AFTER REGISTRATION]
- **Protocol Version**: 1.0
- **Protocol Date**: {datetime.now().strftime("%Y-%m-%d")}

## Review Title

{self.protocol_data['title']}

## Review Team

"""
        for member in self.protocol_data['team']:
            protocol_md += f"- **{member['name']}** ({member['role']})\n"
            protocol_md += f"  - {member['affiliation']}\n"
            protocol_md += f"  - {member['email']}\n"
        
        protocol_md += f"""
## Research Question

{self.protocol_data['research_question']}

## PICOS Framework

- **Population**: {self.protocol_data['picos']['population']}
- **Intervention**: {self.protocol_data['picos']['intervention']}
- **Comparison**: {self.protocol_data['picos']['comparison']}
- **Outcome**: {self.protocol_data['picos']['outcome']}
- **Study Design**: {self.protocol_data['picos']['study_design']}

## Eligibility Criteria

### Inclusion Criteria
- Population: {self.protocol_data['picos']['population']}
- Study design: {self.protocol_data['picos']['study_design']}
- Published {self.protocol_data['methods']['date_range']['from']}-{self.protocol_data['methods']['date_range']['to']}

### Exclusion Criteria
- Non-relevant study designs
- Non-relevant populations
- Insufficient data for analysis

## Information Sources

### Databases
{chr(10).join(f'- {db}' for db in self.protocol_data['methods']['databases'])}

### Date Range
- From: {self.protocol_data['methods']['date_range']['from']}
- To: {self.protocol_data['methods']['date_range']['to']}

### Language
- {self.protocol_data['methods']['language']}

### Grey Literature
- {self.protocol_data['methods']['grey_literature']}

## Search Strategy

[TO BE DEVELOPED - use code/search_strategy_builder.py]

## Selection Process

1. **Deduplication**: Remove exact and near-duplicates
2. **Title/Abstract Screening**: Dual independent screening (10% minimum)
3. **Inter-rater Reliability**: Calculate Cohen's κ (target ≥0.6)
4. **Full-Text Screening**: Dual independent screening with documented exclusion reasons
5. **Conflict Resolution**: Discussion between reviewers, third reviewer if needed

## Data Extraction

### Study Characteristics
- Author, year, country
- Study design, sample size
- Population characteristics
- Intervention details
- Comparison details
- Funding source, conflicts of interest

### Outcome Data
- Primary outcome: {self.protocol_data['analysis']['primary_outcome']}
- Secondary outcomes: {', '.join(self.protocol_data['analysis']['secondary_outcomes']) if self.protocol_data['analysis']['secondary_outcomes'] else 'None'}
- Effect measure: {self.protocol_data['analysis']['effect_measure']}
- Time points assessed

## Risk of Bias Assessment

- **Tool**: {self.protocol_data['analysis']['risk_of_bias_tool']}
- **Process**: Dual independent assessment with conflict resolution

## Synthesis Methods

### Meta-Analysis
- **Method**: {self.protocol_data['analysis']['meta_analysis_method']} meta-analysis
- **Effect Measure**: {self.protocol_data['analysis']['effect_measure']}
- **Heterogeneity**: I², τ², Q-test
- **Software**: R (metafor package) or Python (statsmodels)

### Subgroup Analyses
[TO BE SPECIFIED]

### Sensitivity Analyses
- Leave-one-out analysis
- Fixed vs random effects comparison
- Risk of bias subgroups (low vs high/unclear)

### Publication Bias
- Funnel plots
- Egger's test (if ≥10 studies)
- Trim-and-fill analysis

## Certainty Assessment

- **Framework**: GRADE
- **Domains**: Risk of bias, inconsistency, indirectness, imprecision, publication bias

## Timeline

- **Start Date**: {self.protocol_data['timeline']['start']}
- **Completion Date**: {self.protocol_data['timeline']['completion']}

## Funding

[TO BE SPECIFIED]

## Conflicts of Interest

[TO BE SPECIFIED]

## Protocol Amendments

Any amendments to this protocol will be documented with date and rationale.

---

*Protocol generated: {datetime.now().isoformat()}*
*Tool: Research Assistant for Claude Code v1.2.0*
"""
        
        # Save protocol
        Path('../docs').mkdir(exist_ok=True)
        with open('../docs/protocol.md', 'w') as f:
            f.write(protocol_md)
        
        print("✓ Protocol document saved: docs/protocol.md\n")
    
    def _generate_prospero_form(self):
        """Generate PROSPERO registration form."""
        form_text = f"""PROSPERO REGISTRATION FORM
Generated: {datetime.now().strftime("%Y-%m-%d")}

Copy this information into the PROSPERO web form:
https://www.crd.york.ac.uk/prospero/

═══════════════════════════════════════════════════════════════

1. REVIEW TITLE
{self.protocol_data['title']}

2. ORIGINAL LANGUAGE TITLE (if not English)
[Leave blank if English]

3. NAMED CONTACT
{self.protocol_data['team'][0]['name']}
Email: {self.protocol_data['team'][0]['email']}

4. REVIEW TEAM MEMBERS
"""
        for i, member in enumerate(self.protocol_data['team'], 1):
            form_text += f"{i}. {member['name']} - {member['role']}\n"
        
        form_text += f"""
5. ORGANIZATIONAL AFFILIATION
{self.protocol_data['team'][0]['affiliation']}

6. REVIEW QUESTION
{self.protocol_data['research_question']}

7. SEARCHES
Databases: {', '.join(self.protocol_data['methods']['databases'])}
Date range: {self.protocol_data['methods']['date_range']['from']} to {self.protocol_data['methods']['date_range']['to']}
Language restrictions: {self.protocol_data['methods']['language']}
Grey literature: {self.protocol_data['methods']['grey_literature']}

8. CONDITION OR DOMAIN
{self.protocol_data['picos']['population']}

9. PARTICIPANTS/POPULATION
Inclusion: {self.protocol_data['picos']['population']}
Exclusion: [Specify exclusion criteria]

10. INTERVENTION(S)/EXPOSURE(S)
{self.protocol_data['picos']['intervention']}

11. COMPARATOR(S)/CONTROL
{self.protocol_data['picos']['comparison']}

12. TYPES OF STUDY TO BE INCLUDED
{self.protocol_data['picos']['study_design']}

13. CONTEXT
[Specify setting/context if relevant]

14. PRIMARY OUTCOME(S)
{self.protocol_data['analysis']['primary_outcome']}

15. SECONDARY OUTCOME(S)
{', '.join(self.protocol_data['analysis']['secondary_outcomes']) if self.protocol_data['analysis']['secondary_outcomes'] else 'None'}

16. DATA EXTRACTION (SELECTION AND CODING)
Dual independent screening for title/abstract and full-text.
Dual independent data extraction.
Conflicts resolved through discussion.

17. RISK OF BIAS ASSESSMENT
Tool: {self.protocol_data['analysis']['risk_of_bias_tool']}
Process: Dual independent assessment

18. STRATEGY FOR DATA SYNTHESIS
Meta-analysis method: {self.protocol_data['analysis']['meta_analysis_method']}
Effect measure: {self.protocol_data['analysis']['effect_measure']}
Heterogeneity: I², τ², Q-test
Publication bias: Funnel plots, Egger's test

19. ANALYSIS OF SUBGROUPS OR SUBSETS
[Specify pre-planned subgroups if any]

20. DISSEMINATION PLANS
Publication in peer-reviewed journal

21. KEYWORDS
[Add relevant keywords]

22. DETAILS OF EXISTING REVIEW
Not applicable (prospective review)

23. CONFLICTS OF INTEREST
[Declare conflicts or state "None"]

24. FUNDING SOURCES/SPONSORS
[Specify funding or state "None"]

═══════════════════════════════════════════════════════════════

NEXT STEPS:
1. Go to https://www.crd.york.ac.uk/prospero/
2. Register/login
3. Click "Register new review"
4. Copy/paste sections above into corresponding form fields
5. Submit for editorial review (2-7 days)
6. Once approved, add registration number to docs/protocol_registration.md
"""
        
        with open('../docs/prospero_registration_form.txt', 'w') as f:
            f.write(form_text)
        
        print("✓ PROSPERO form saved: docs/prospero_registration_form.txt\n")
    
    def _generate_osf_project(self):
        """Generate OSF project instructions."""
        osf_text = f"""OSF REGISTRATION INSTRUCTIONS
Generated: {datetime.now().strftime("%Y-%m-%d")}

═══════════════════════════════════════════════════════════════

1. Go to https://osf.io and create account/login

2. Click "Create new project"

3. Project Details:
   - Title: {self.protocol_data['title']}
   - Description: Systematic review protocol
   - Category: Project

4. Upload these files:
   - docs/protocol.md
   - docs/picos_framework.yaml (after creating)
   - Any other protocol materials

5. Add Contributors:
"""
        for member in self.protocol_data['team']:
            osf_text += f"   - {member['name']} ({member['email']})\n"
        
        osf_text += """
6. Make Project Public:
   - Click "Make Public"
   - Confirm public access

7. Get Registration DOI:
   - Click "Registrations" tab
   - "New Registration"
   - Choose template: "OSF Preregistration"
   - Complete form using protocol.md
   - Submit registration
   - Copy DOI

8. Add DOI to docs/protocol_registration.md

═══════════════════════════════════════════════════════════════

OSF registration is INSTANT (no editorial review).
Your protocol will be publicly accessible immediately.
"""
        
        with open('../docs/osf_registration_instructions.txt', 'w') as f:
            f.write(osf_text)
        
        print("✓ OSF instructions saved: docs/osf_registration_instructions.txt\n")
    
    def _save_protocol_data(self):
        """Save protocol data as YAML."""
        # Save PICOS as YAML
        with open('../docs/picos_framework.yaml', 'w') as f:
            yaml.dump(self.protocol_data['picos'], f, default_flow_style=False)
        
        # Save full protocol data as JSON
        with open('../docs/protocol_data.json', 'w') as f:
            json.dump(self.protocol_data, f, indent=2)
        
        print("✓ Protocol data saved: docs/picos_framework.yaml")
        print("✓ Protocol data saved: docs/protocol_data.json\n")


def main():
    """Run protocol registration helper."""
    reg = ProtocolRegistration()
    reg.run_interactive()


if __name__ == "__main__":
    main()
