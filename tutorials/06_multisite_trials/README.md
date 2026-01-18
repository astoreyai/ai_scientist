# Tutorial 6: Multi-Site Collaborative Trials

**Duration**: 50 minutes
**Prerequisites**: Tutorials 1, 3, 5 completed
**What you'll learn**: Coordinating multi-center RCTs, harmonizing protocols, central randomization, data sharing, consortium authorship, individual participant data meta-analysis

---

## Overview

This tutorial demonstrates **multi-site collaborative research** - coordinating randomized controlled trials across multiple institutions. You'll learn:

1. Forming research consortia and governance structures
2. Harmonizing study protocols across sites
3. Central vs. site-specific IRB review
4. Central randomization and data management
5. Site monitoring and quality control
6. Data sharing agreements and MTA/DUA
7. Individual participant data (IPD) meta-analysis
8. Consortium authorship and contribution guidelines
9. Coordinating publications and data releases
10. Using collaboration tools (REDCap multi-site, OSF teams)

**Running Example**: We'll coordinate a **5-site collaborative RCT**:
*"Does cognitive behavioral therapy (CBT) reduce depression in primary care patients? A multi-site randomized trial across 5 university health systems."*

**Why Multi-Site**:
- Increases sample size (faster recruitment)
- Enhances generalizability (diverse populations/settings)
- Builds consortia for future studies
- Shares resources and expertise

---

## Part 1: Forming the Consortium (10 minutes)

### Step 1.1: Identify Collaborating Sites

**Our Consortium** (5 sites):

```
═══════════════════════════════════════════════
        MULTI-SITE CBT TRIAL CONSORTIUM
═══════════════════════════════════════════════

Lead Site (Coordinating Center):
─────────────────────────────────────────────────
University of Example Health System
- PI: Dr. Sarah Chen
- Role: Overall coordination, data management, statistical analysis
- Resources: REDCap instance, biostatistician, data manager
- Target enrollment: 100 participants

Participating Sites:
─────────────────────────────────────────────────
Site 2: State University Medical Center
- Site PI: Dr. Michael Johnson
- Target enrollment: 80 participants
- Strengths: Large primary care network, experienced CBT therapists

Site 3: Regional Health Partners
- Site PI: Dr. Lisa Martinez
- Target enrollment: 60 participants
- Strengths: Diverse patient population, bilingual staff

Site 4: Community Health Collaborative
- Site PI: Dr. James Taylor
- Target enrollment: 60 participants
- Strengths: Safety-net population, high depression prevalence

Site 5: Academic Medical Institute
- Site PI: Dr. Emily Wong
- Target enrollment: 100 participants
- Strengths: Research infrastructure, training program for CBT

Total Target Enrollment: 400 participants across 5 sites
```

**Checkpoint**: Sites selected with complementary strengths and adequate enrollment capacity.

---

### Step 1.2: Establish Governance Structure

**Action**: Create governance charter

```yaml
# docs/consortium_governance.yaml

consortium_name: "Multi-Site CBT Trial Consortium"

steering_committee:
  members:
    - Dr. Sarah Chen (Lead PI, University of Example)
    - Dr. Michael Johnson (Site 2 PI)
    - Dr. Lisa Martinez (Site 3 PI)
    - Dr. James Taylor (Site 4 PI)
    - Dr. Emily Wong (Site 5 PI)
    - Dr. Robert Lee (Biostatistician, University of Example)
    - Ms. Karen Smith (Patient Advocate)
  
  decision_making:
    - Majority vote for protocol amendments
    - Consensus required for major changes (e.g., sample size, primary outcome)
    - Lead PI has tie-breaking vote
  
  meeting_frequency: Monthly video conference (first Tuesday, 3pm ET)

coordinating_center:
  institution: University of Example
  responsibilities:
    - Overall project management
    - Central randomization
    - Data management (REDCap multi-site)
    - Statistical analysis
    - Regulatory submissions
    - Publication coordination
  
  staff:
    - Project Manager: Jane Doe (20% FTE)
    - Data Manager: Tom Brown (30% FTE)
    - Biostatistician: Dr. Robert Lee (15% FTE)

site_responsibilities:
  - Participant recruitment and enrollment
  - Informed consent administration
  - Intervention delivery (CBT or usual care)
  - Data collection and entry into REDCap
  - Local IRB compliance
  - Quality monitoring

data_sharing_committee:
  members: [All Site PIs, Biostatistician, 1 External Expert]
  role: Review external data requests after publication
  process: Applications reviewed quarterly

publications_committee:
  members: [All Site PIs, Lead Statistician]
  role: Coordinate manuscript authorship and timelines
  guidelines: CRediT taxonomy, ICMJE criteria
```

**Checkpoint**: Governance structure documented with clear roles and decision-making processes.

---

### Step 1.3: Develop Memorandum of Understanding (MOU)

**Action**: Create legally binding agreement among sites

```bash
python code/generate_mou.py \
  --sites 5 \
  --lead-institution "University of Example" \
  --output docs/multi_site_mou_template.docx
```

**Key MOU Sections**:

```
1. Purpose and Objectives
   - Primary aim: Test CBT efficacy in primary care
   - Secondary aims: Cost-effectiveness, implementation barriers

2. Site Commitments
   - Enrollment targets (with consequences for underperformance)
   - Staff time commitments (PI 10%, coordinator 50%, therapist 30%)
   - Compliance with protocol and timelines

3. Financial Arrangements
   - Lead site receives grant, subcontracts to sites
   - Per-participant payments: $500/enrolled, $200/completed 6mo follow-up
   - Equipment/training costs covered centrally

4. Intellectual Property
   - Consortium owns all data
   - Individual sites cannot publish independently before primary paper
   - All sites credited on main publications
   - Site-specific papers allowed after primary publication

5. Data Ownership and Sharing
   - De-identified data pooled at coordinating center
   - Sites retain access to own site data
   - Aggregate data publicly shared 1 year after publication
   - Individual participant data shared per committee approval

6. Publication Policies
   - Primary outcome paper: All site PIs as co-authors
   - Site-specific papers: That site PI as first author, others acknowledged
   - Authorship order determined by contribution (CRediT)
   - Lead PI final decision on disputes

7. Dispute Resolution
   - Escalation: Site PI → Steering Committee → External Mediator
   - Removal clause: Sites can be terminated for non-compliance

8. Term and Termination
   - 4-year term (2 years enrollment, 2 years follow-up/analysis)
   - Early termination requires 90-day notice
```

**Checkpoint**: MOU signed by all 5 site PIs and institutional officials.

---

## Part 2: Protocol Harmonization (10 minutes)

### Step 2.1: Develop Master Protocol

**Challenge**: Sites have different electronic health records (EHRs), patient populations, and resources.

**Solution**: Master protocol with site-specific appendices

**Action**: Create harmonized protocol

```bash
# Start with single-site protocol from Tutorial 3
cp tutorials/03_experimental_design/docs/trial_protocol_v1.1.docx \
   docs/multi_site_protocol_v1.0.docx

# Add multi-site specific sections
python code/convert_to_multisite_protocol.py \
  --input docs/multi_site_protocol_v1.0.docx \
  --sites 5 \
  --output docs/multi_site_protocol_v1.0_final.docx
```

---

### Step 2.2: Address Site-Specific Variations

**Acceptable Variations**:

```yaml
# docs/site_specific_appendices.yaml

recruitment_methods:
  allowed_variation: yes
  rationale: Sites have different EHR systems and clinic workflows
  
  site_1: EHR flag for PHQ-9 ≥10, automated referral to study
  site_2: Weekly manual chart review, phone outreach
  site_3: Clinic staff screen at check-in, warm handoff to coordinator
  site_4: Community health worker referrals, bilingual recruitment
  site_5: Resident physician referrals from primary care clinics

intervention_delivery:
  allowed_variation: limited
  rationale: CBT must be standardized, but format can vary
  
  core_requirements:
    - 12 sessions over 16 weeks
    - Manualized CBT protocol (same manual all sites)
    - Weekly homework assignments
    - Certified CBT therapists (credential verification required)
  
  allowed_adaptations:
    - In-person vs. telehealth (site preference, patient choice)
    - Individual vs. group format (max 8 per group)
    - Language: English or Spanish (manual translated, back-translated)

outcome_assessment:
  allowed_variation: no
  rationale: Primary outcome must be identical across sites
  
  standardization:
    - Same measure: PHQ-9 (Patient Health Questionnaire-9)
    - Same timepoints: Baseline, 8 weeks, 16 weeks, 6 months
    - Same administration: Self-report via REDCap (sent by email/SMS)
    - Same training: All coordinators complete REDCap training module

usual_care_control:
  allowed_variation: yes
  rationale: "Usual care" naturally differs across health systems
  
  documentation_required:
    - Each site describes usual depression care
    - Track: Medications, therapy referrals, hospitalizatio ns
    - Report in paper: "Usual care ranged from..."
```

**Checkpoint**: Master protocol allows necessary site flexibility while maintaining core standardization.

---

### Step 2.3: Central Training and Certification

**Action**: Ensure all sites deliver intervention identically

```
Training Requirements (Before Site Initiation):
═══════════════════════════════════════════════

CBT Therapists:
─────────────────────────────────────────────────
1. Credential verification (licensed LCSW, PhD, PsyD)
2. 2-day in-person CBT manual training (coordinating center)
3. Role-play certification (pass 3 of 3 standardized patient scenarios)
4. Ongoing supervision: Monthly video conference with expert supervisor
5. Fidelity monitoring: 10% of sessions recorded and rated

Study Coordinators:
─────────────────────────────────────────────────
1. 1-day Good Clinical Practice (GCP) training
2. REDCap data entry training (web-based, 2 hours)
3. Informed consent training (standardized script)
4. Certification exam (80% pass rate required)

Site PIs:
─────────────────────────────────────────────────
1. Webinar on protocol overview (2 hours)
2. Regulatory requirements (IRB, SAE reporting)
3. Enrollment monitoring and quality metrics

Fidelity Monitoring Plan:
─────────────────────────────────────────────────
- 10% of CBT sessions audio/video recorded (random selection)
- Rated by independent coders using CBT Adherence Scale
- Feedback provided monthly
- Therapists scoring <6/10 require remediation
```

**Checkpoint**: All sites trained and certified before enrollment begins.

---

## Part 3: Central Randomization and Data Management (10 minutes)

### Step 3.1: Set Up REDCap Multi-Site Instance

**Action**: Configure REDCap for multi-site trial

```bash
# Coordinating center IT administrator sets up REDCap project
python code/setup_redcap_multisite.py \
  --project-name "Multi-Site CBT Trial" \
  --sites 5 \
  --randomization block \
  --block-size 4 \
  --stratify-by site \
  --output redcap_config.json
```

**REDCap Configuration**:

```yaml
# REDCap Multi-Site Setup

project_settings:
  title: "Multi-Site CBT Trial for Primary Care Depression"
  purpose: Clinical Trial
  randomization: Yes (stratified by site)
  
data_access_groups:
  - Site 1: University of Example
  - Site 2: State University Medical Center
  - Site 3: Regional Health Partners
  - Site 4: Community Health Collaborative
  - Site 5: Academic Medical Institute

user_rights:
  site_coordinators:
    - Can only see own site data
    - Can randomize participants
    - Can enter data for own site
    - Cannot export data
  
  site_pis:
    - Can see own site data
    - Cannot randomize
    - Can generate site-specific reports
  
  coordinating_center:
    - Can see all site data
    - Can manage users
    - Can export aggregate data
    - Controls randomization allocation

randomization_setup:
  method: Stratified block randomization
  strata: 5 (one per site)
  block_size: 4 (within each site)
  allocation: 1:1 (CBT:Usual Care)
  concealment: Yes (coordinating center generates, sites cannot see sequence)

automated_alerts:
  - Email to coordinator when participant randomized
  - Email to PI if site falls behind enrollment target (weekly)
  - Email to data manager if missing data >10% (weekly)
  - Email to all if serious adverse event (SAE) reported (immediate)
```

**Checkpoint**: REDCap configured with appropriate access controls and automated workflows.

---

### Step 3.2: Implement Central Randomization

**Why Central**: Prevents selection bias, ensures concealment across all sites

**Workflow**:

```
Centralized Randomization Workflow:
═══════════════════════════════════════════════

Step 1: Participant Consents (Site Coordinator)
  ↓
Step 2: Complete Baseline Assessment in REDCap
  ↓
Step 3: Verify Eligibility (automated checks in REDCap)
  ↓
Step 4: Click "Randomize" Button
  ↓
Step 5: REDCap Allocates from Pre-Generated Sequence
  - Sequence stratified by site (ensures site balance)
  - Block size 4 within each site
  - Allocation concealed (coordinator cannot predict)
  ↓
Step 6: REDCap Displays Assignment (CBT or Usual Care)
  ↓
Step 7: Automated Email Sent:
  - To coordinator: "Participant X randomized to GROUP"
  - To CBT therapist (if CBT): "New referral: Participant X"
  - To coordinating center: Enrollment log updated
  ↓
Step 8: Coordinator Informs Participant of Assignment
```

**Checkpoint**: Central randomization ensures allocation concealment across all sites.

---

### Step 3.3: Data Quality Monitoring

**Action**: Implement real-time quality control

```python
# Automated Weekly Data Quality Report

import pandas as pd
from datetime import datetime, timedelta

def generate_site_quality_report():
    """Generate quality metrics for each site"""
    
    sites = ['Site 1', 'Site 2', 'Site 3', 'Site 4', 'Site 5']
    
    report = {
        'site': [],
        'enrolled': [],
        'target': [],
        'percent_target': [],
        'missing_data_rate': [],
        'protocol_deviations': [],
        'quality_flag': []
    }
    
    for site in sites:
        data = load_site_data(site)
        
        enrolled = len(data)
        target = get_site_target(site)
        missing_rate = calculate_missing_data(data)
        deviations = count_protocol_deviations(data)
        
        # Flag sites with quality issues
        flag = 'OK'
        if missing_rate > 0.10:
            flag = 'HIGH MISSING DATA'
        if enrolled < target * 0.75 and months_enrolled >= 12:
            flag = 'ENROLLMENT BEHIND'
        if deviations > 5:
            flag = 'PROTOCOL DEVIATIONS'
        
        report['site'].append(site)
        report['enrolled'].append(enrolled)
        report['target'].append(target)
        report['percent_target'].append(f"{enrolled/target*100:.0f}%")
        report['missing_data_rate'].append(f"{missing_rate*100:.1f}%")
        report['protocol_deviations'].append(deviations)
        report['quality_flag'].append(flag)
    
    return pd.DataFrame(report)

# Example output:
"""
══════════════════════════════════════════════════════════════════════
      WEEKLY DATA QUALITY REPORT - Month 18 of 24
══════════════════════════════════════════════════════════════════════

Site         Enrolled  Target  %Target  Missing  Deviations  Flag
──────────────────────────────────────────────────────────────────────
Site 1       87        100     87%      3.2%     2           OK
Site 2       78        80      98%      5.1%     1           OK
Site 3       45        60      75%      8.7%     3           ENROLLMENT BEHIND 
Site 4       58        60      97%      4.3%     0           OK
Site 5       95        100     95%      2.8%     1           OK
──────────────────────────────────────────────────────────────────────
TOTAL        363       400     91%      4.8%     7           ON TRACK ✓

Actions Needed:
- Site 3: Contact Dr. Martinez re: enrollment strategies
- All sites: Missing data acceptable (<10%)
"""
```

**Checkpoint**: Real-time monitoring identifies issues before they compound.

---

## Part 4: IRB and Regulatory Coordination (5 minutes)

### Step 4.1: Choose IRB Review Model

**Options**:

1. **Site-Specific IRBs** (traditional)
   - Each site submits to own IRB
   - Sites familiar with own IRB
   - ✗ 5 separate submissions
   - ✗ Inconsistent requirements
   - ✗ Slow (sequential approvals)

2. **Single IRB (sIRB)** - RECOMMENDED for NIH-funded
   - Lead site IRB reviews for all sites
   - NIH mandate for multi-site trials (2018)
   - Faster approval
   - Harmonized protocol
   - ✗ Sites must cede authority

**Our Choice**: **Single IRB (sIRB) at Lead Site**

---

### Step 4.2: Single IRB Workflow

**Action**: Coordinate sIRB review

```
Single IRB Timeline:
═══════════════════════════════════════════════

Week 1-2: Lead Site Preparation
  ├─ Lead site prepares master IRB application
  ├─ All sites provide local context documents
  └─ All sites execute Reliance Agreement (cede review to lead IRB)

Week 3-4: Lead Site IRB Review
  ├─ Submit to University of Example IRB
  ├─ IRB reviews for ALL 5 sites (reliance agreements uploaded)
  └─ Address contingencies (usually minor clarifications)

Week 5: IRB Approval
  ├─ Approval letter issued
  └─ Covers all 5 sites under single protocol

Week 6: Local Submissions
  ├─ Each site submits to own IRB for "acknowledgment only"
  ├─ Local IRB confirms reliance on lead IRB
  └─ Local IRB tracks as externally reviewed study

Week 7: Site Activation
  └─ All sites can begin enrollment simultaneously ✓

Traditional (5 separate IRBs): 12-20 weeks
Single IRB: 7 weeks (60% faster)
```

**Documents Required**:

```
sIRB Application Package:
─────────────────────────────────────────────────
1. Master Protocol (same for all sites)
2. Master Informed Consent Form (ICF)
3. Site-specific appendices (recruitment methods)
4. Reliance Agreements (all 5 sites)
5. CVs and training records (all site PIs and coordinators)
6. Data and Safety Monitoring Plan (DSMP)
7. REDCap data security documentation
8. Letters of support from site administrators
```

**Checkpoint**: sIRB approval obtained in 7 weeks, all sites activated simultaneously.

---

## Part 5: Data Sharing Agreements (5 minutes)

### Step 5.1: Material Transfer Agreement (MTA)

For sites sharing biospecimens (if applicable), create MTA:

```yaml
# docs/material_transfer_agreement.yaml

# (Not applicable to our CBT trial - behavioral intervention only)
# Include if collecting blood, saliva, or other biological samples

provider_site: Site X
recipient_site: Coordinating Center
material: De-identified plasma samples
purpose: Biomarker analysis (exploratory aim)
quantity: 5mL per participant (n=400, total 2L)
ownership: Samples owned by coordinating center after transfer
publication: Sites acknowledged, not automatic authorship
destruction: After 10 years or upon request
```

---

### Step 5.2: Data Use Agreement (DUA)

**Action**: Govern data access and use

```yaml
# docs/data_use_agreement.yaml

parties:
  - Lead Site (University of Example) - Data Controller
  - Site 2, Site 3, Site 4, Site 5 - Data Contributors

permitted_uses:
  - Primary trial analyses (pre-specified)
  - Secondary analyses approved by Steering Committee
  - Site-specific analyses (own data only)
  - External requests (approved by Data Sharing Committee)

prohibited_uses:
  - Commercial purposes
  - Participant re-identification attempts
  - Sharing with external parties without approval
  - Publication without steering committee notification

data_security:
  - PHI remains at local sites
  - De-identified data transferred via secure REDCap
  - Coordinating center: HIPAA-compliant server, encrypted
  - Access limited to authorized personnel (user logs maintained)

retention_period: 10 years after final publication

termination:
  - Sites can withdraw prospectively (not already collected data)
  - Lead site cannot terminate without Steering Committee approval
```

**Checkpoint**: DUA protects data while enabling collaborative science.

---

## Part 6: Analysis and Publication (10 minutes)

### Step 6.1: Individual Participant Data (IPD) Meta-Analysis

**Why IPD**: More powerful than traditional meta-analysis (uses aggregate data)

**Action**: Analyze pooled participant-level data

```python
# code/ipd_meta_analysis.py

import pandas as pd
import statsmodels.api as sm
from statsmodels.regression.mixed_linear_model import MixedLM

def ipd_meta_analysis():
    """
    Individual Participant Data Meta-Analysis
    Accounts for clustering by site (random effects)
    """
    
    # Load pooled data from all sites
    data = pd.read_csv('data/pooled_data_all_sites.csv')
    
    # Model: PHQ-9 at 6 months ~ treatment + baseline PHQ-9 + site (random effect)
    model = MixedLM.from_formula(
        'phq9_6mo ~ group + phq9_baseline + age + sex',
        data=data,
        groups=data['site'],  # Random intercept for site
        re_formula='1'  # Random intercept only
    )
    
    result = model.fit()
    
    print("═══════════════════════════════════════════════")
    print("  IPD META-ANALYSIS RESULTS (n=363, 5 sites)")
    print("═══════════════════════════════════════════════\n")
    
    # Extract treatment effect
    treatment_effect = result.params['group[T.CBT]']
    se = result.bse['group[T.CBT]']
    ci_lower = treatment_effect - 1.96 * se
    ci_upper = treatment_effect + 1.96 * se
    p_value = result.pvalues['group[T.CBT]']
    
    print(f"Treatment Effect (CBT vs Usual Care):")
    print(f"  Adjusted Mean Difference: {treatment_effect:.2f} points")
    print(f"  95% CI: ({ci_lower:.2f}, {ci_upper:.2f})")
    print(f"  p-value: {p_value:.4f}\n")
    
    # Site-specific effects (random effects)
    print("Site-Specific Random Effects:")
    for site in ['Site 1', 'Site 2', 'Site 3', 'Site 4', 'Site 5']:
        site_effect = result.random_effects[site]
        print(f"  {site}: {site_effect:.2f}")
    
    # Heterogeneity assessment
    tau_squared = result.cov_re.values[0][0]  # Between-site variance
    i_squared = (tau_squared / (tau_squared + result.scale)) * 100
    
    print(f"\nHeterogeneity:")
    print(f"  τ² (tau-squared): {tau_squared:.3f}")
    print(f"  I² statistic: {i_squared:.1f}%")
    
    if i_squared < 25:
        print("  Interpretation: Low heterogeneity (sites similar)")
    elif i_squared < 75:
        print("  Interpretation: Moderate heterogeneity")
    else:
        print("  Interpretation: High heterogeneity (explore site differences)")
    
    return result

# Example Output:
"""
═══════════════════════════════════════════════
  IPD META-ANALYSIS RESULTS (n=363, 5 sites)
═══════════════════════════════════════════════

Treatment Effect (CBT vs Usual Care):
  Adjusted Mean Difference: -3.8 points
  95% CI: (-5.2, -2.4)
  p-value: <0.001

Site-Specific Random Effects:
  Site 1: +0.2 (slightly better outcomes)
  Site 2: -0.1
  Site 3: +0.5 (best outcomes)
  Site 4: -0.3
  Site 5: -0.3

Heterogeneity:
  τ² (tau-squared): 0.18
  I² statistic: 12.3%
  Interpretation: Low heterogeneity (sites similar) ✓

Conclusion: CBT effective across all 5 sites with minimal heterogeneity.
"""
```

**Checkpoint**: IPD meta-analysis leverages full power of multi-site data.

---

### Step 6.2: Consortium Authorship Guidelines

**Action**: Apply CRediT taxonomy for transparent contributions

```yaml
# docs/authorship_guidelines.yaml

primary_outcome_paper:
  title: "Cognitive Behavioral Therapy for Depression in Primary Care: 
          A Multi-Site Randomized Trial"
  
  authorship_order:
    first_author: Lead PI (Dr. Chen)
    second_author: Lead Biostatistician (Dr. Lee)
    middle_authors: Site PIs (alphabetical by site number)
    senior_author: Consortium designee (most senior PI)
  
  credit_contributions:
    Dr. Chen (Lead PI):
      - Conceptualization
      - Methodology
      - Project administration
      - Writing - original draft
      - Funding acquisition
    
    Dr. Lee (Biostatistician):
      - Formal analysis
      - Data curation
      - Visualization (figures)
      - Writing - review & editing
    
    Site PIs (Johnson, Martinez, Taylor, Wong):
      - Investigation
      - Resources
      - Supervision (site-level)
      - Writing - review & editing
    
    Study Coordinators (acknowledged, not authors):
      - Data collection
      - Project administration (site-level)

site_specific_papers:
  allowed: Yes (after primary paper published)
  
  example_titles:
    - "Implementation of CBT in Safety-Net Primary Care" (Site 4 first author)
    - "Bilingual CBT Delivery in Latinx Populations" (Site 3 first author)
  
  authorship:
    - Site PI: First author
    - Site staff: Co-authors
    - Lead PI: Senior author
    - Other site PIs: Acknowledged (not co-authors unless substantial contribution)

author_disputes:
  resolution:
    1. Site PI discusses with lead PI
    2. If unresolved, Steering Committee votes
    3. If still unresolved, external ICMJE expert consulted
  
  removal_criteria:
    - Did not contribute per agreed CRediT roles
    - Site withdrawn from consortium before data collection complete
    - Academic misconduct findings
```

**Checkpoint**: Clear authorship guidelines prevent disputes.

---

### Step 6.3: Coordinated Publication Timeline

**Action**: Plan publication sequence

```
Publication Timeline (after trial completion):
═══════════════════════════════════════════════

Month 0: Data Lock
  └─ No further changes to dataset allowed

Month 1-3: Primary Analysis
  ├─ IPD meta-analysis (all sites pooled)
  ├─ Pre-registered analysis plan executed
  └─ Results presented to Steering Committee

Month 4-6: Primary Manuscript Drafting
  ├─ Lead PI drafts manuscript
  ├─ All co-authors review and edit
  └─ Submit to JAMA or NEJM

Month 7-12: Peer Review
  └─ Address reviewer comments

Month 13: Primary Paper Published 🎉
  └─ CONSORT diagram shows all 5 sites

Month 14-18: Secondary Papers
  ├─ Cost-effectiveness analysis
  ├─ Implementation barriers and facilitators
  └─ Moderator analyses (who benefits most)

Month 19+: Site-Specific Papers
  └─ Sites free to publish site-specific analyses

Month 25: Public Data Release
  ├─ De-identified IPD uploaded to NIMH Data Archive (NDA)
  ├─ DOI minted for dataset
  └─ External researchers can request access
```

**Checkpoint**: Coordinated timeline ensures fair credit and maximum impact.

---

## Part 7: Lessons Learned and Best Practices (5 minutes)

### Common Challenges and Solutions

**Challenge 1: Site Enrollment Disparities**

```
Problem: Site 3 enrolled only 45/60 participants (75% of target)

Solutions Applied:
1. Monthly check-in calls with Site 3 PI
2. Shared successful recruitment strategies from Site 2
3. Extended enrollment period by 2 months (all sites)
4. Redistributed 15-participant shortfall across other sites

Outcome: Total enrollment 363/400 (91% of target) - adequate power
```

---

**Challenge 2: Protocol Deviations**

```
Problem: Site 4 delivered CBT in 10 sessions instead of 12 for some participants

Investigation:
- Therapist reported scheduling difficulties with patients
- Patients missed sessions due to transportation barriers
- Therapist condensed content to fit 10 sessions

Resolution:
1. Documented as protocol deviation (per-protocol analysis will exclude)
2. Retraining provided to Site 4 therapist
3. Offered telehealth option to reduce transportation barriers
4. ITT analysis includes all participants (primary), per-protocol is sensitivity

Impact: 8 participants affected (2% of sample) - minimal impact on results
```

---

**Challenge 3: Data Quality Issues**

```
Problem: Site 2 had 15% missing follow-up data (vs. 5% at other sites)

Investigation:
- Coordinator turnover (2 coordinators quit during trial)
- New coordinator insufficiently trained
- Participants not receiving automated REDCap reminders (technical error)

Resolution:
1. Retraining for new coordinator
2. Fixed REDCap email configuration
3. Manual phone outreach to all Site 2 participants with missing data
4. Multiple imputation for remaining missing data (sensitivity analysis)

Outcome: Recovered 8% (down to 7% missing), imputed rest
```

---

### Multi-Site Best Practices

**Do's**:
- Invest in thorough training upfront (saves problems later)
- Centralize randomization and data management
- Monitor enrollment and quality in real-time (weekly reports)
- Communicate frequently (monthly steering committee calls)
- Build in flexibility for site-specific adaptations
- Celebrate milestones (enrollment targets, publication acceptance)
- Use single IRB (faster, more efficient)

**Don'ts**:
- Assume all sites have same resources/infrastructure
- Allow sites to modify protocol without steering committee approval
- Wait until end to address enrollment or quality issues
- Neglect site-specific barriers (language, transportation, stigma)
- Rush training (quality suffers)
- Forget to recognize site coordinator contributions (acknowledge in papers)

---

## Summary and Next Steps

### What You've Learned

**Multi-Site Coordination**:
- Formed 5-site research consortium with governance structure
- Harmonized protocol with acceptable site variations
- Established central randomization and data management
- Navigated single IRB review (7 weeks vs. 12-20 weeks)
- Implemented data sharing agreements (DUA, MTA)
- Conducted individual participant data (IPD) meta-analysis
- Applied consortium authorship guidelines (CRediT taxonomy)
- Coordinated publication timeline

**Advantages of Multi-Site**:
- Faster recruitment (5 sites enrolling simultaneously)
- Enhanced generalizability (diverse populations, settings)
- Larger sample size (400 vs. 100 single-site)
- Shared resources and expertise
- Built sustainable research network

**Key Files Generated**:
```
multisite_cbt_trial/
├── docs/
│   ├── consortium_governance.yaml
│   ├── multi_site_mou_template.docx (legally binding)
│   ├── multi_site_protocol_v1.0.docx (harmonized across sites)
│   ├── site_specific_appendices.yaml
│   ├── data_use_agreement.yaml
│   └── authorship_guidelines.yaml (CRediT-based)
├── redcap/
│   ├── redcap_multisite_config.json
│   └── data_access_groups_setup.yaml
└── analysis/
    ├── ipd_meta_analysis.py
    └── weekly_site_quality_report.py
```

---

### Tools for Multi-Site Collaboration

**Recommended Platforms**:
- **REDCap**: Multi-site data capture with data access groups
- **OSF Teams**: Collaborative document sharing with version control
- **Slack/Teams**: Real-time communication among sites
- **Zoom**: Monthly steering committee meetings
- **GitHub**: Code sharing and version control for analysis scripts
- **NIMH Data Archive**: Public data sharing after publication

---

### Next Steps

**After Completing This Tutorial**:

1. **Scale Up**: Consider international consortia (requires additional IRB coordination)
2. **Network Trials**: Use existing research networks (e.g., PBRN, CTSA)
3. **Adaptive Designs**: Multi-site platform trials with shared infrastructure

**See Also**:
- Tutorial 7: Qualitative + Quantitative Mixed Methods
- Tutorial 8: Grant Proposal Writing (multi-site R01 budgets)

---

**Tutorial Complete!** You now know how to coordinate multi-site collaborative RCTs from consortium formation to publication.
