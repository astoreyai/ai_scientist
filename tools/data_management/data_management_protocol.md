# PhD Research Data Management Protocol

**PURPOSE:** Establish systematic procedures for organizing, storing, backing up, and securing research data throughout your PhD journey.

**WHY THIS MATTERS:**
- Prevents data loss (the #1 cause of PhD delays)
- Ensures research reproducibility
- Maintains data security and compliance
- Enables efficient collaboration
- Facilitates future reuse of data

**TIMELINE:** Implement from Day 1 of PhD through dissertation submission

---

## 📋 TABLE OF CONTENTS

1. [Data Management Plan (DMP) Template](#1-data-management-plan-dmp-template)
2. [File Organization System](#2-file-organization-system)
3. [File Naming Conventions](#3-file-naming-conventions)
4. [Version Control Strategy](#4-version-control-strategy)
5. [Backup Protocol (3-2-1 Rule)](#5-backup-protocol-3-2-1-rule)
6. [Data Security & Compliance](#6-data-security--compliance)
7. [Data Documentation](#7-data-documentation)
8. [Collaboration & Sharing](#8-collaboration--sharing)
9. [Data Archiving & Preservation](#9-data-archiving--preservation)
10. [Emergency Recovery Procedures](#10-emergency-recovery-procedures)

---

## 1. DATA MANAGEMENT PLAN (DMP) TEMPLATE

**WHEN TO CREATE:** At the start of your PhD (often required for IRB approval or funding)

**WHAT TO INCLUDE:**

### 1.1 Data Description

**Describe your data:**
```
DATA TYPES:
- [ ] Quantitative survey data (e.g., CSV, SPSS, Excel)
- [ ] Qualitative interview transcripts (e.g., Word, NVivo)
- [ ] Audiovisual recordings (e.g., MP3, MP4)
- [ ] Images/photos (e.g., JPEG, PNG, TIFF)
- [ ] Code/software (e.g., Python, R, MATLAB)
- [ ] Publications/manuscripts (e.g., Word, PDF, LaTeX)
- [ ] Other: [specify]

ESTIMATED VOLUME:
- Total size: [e.g., 50 GB]
- Growth rate: [e.g., 5 GB/month]
- Final estimated size: [e.g., 250 GB]

FILE FORMATS:
- Raw data: [e.g., .csv, .xlsx]
- Processed data: [e.g., .sav (SPSS), .Rdata]
- Analysis outputs: [e.g., .pdf, .html]
- Documentation: [e.g., .docx, .md]
```

### 1.2 Data Collection & Processing

**How you'll collect and process data:**
```
COLLECTION METHODS:
- [ ] Online surveys (Qualtrics, Google Forms)
- [ ] In-person interviews (recorded with consent)
- [ ] Experiments (lab notebook, digital logs)
- [ ] Secondary data (public datasets, archives)
- [ ] Other: [specify]

PROCESSING STEPS:
1. Raw data collection → stored in `/01_raw_data/`
2. Data cleaning (remove duplicates, handle missing) → `/02_processed_data/`
3. Analysis (statistical, qualitative) → `/03_analysis_outputs/`
4. Visualization (figures, tables) → `/04_figures_tables/`

QUALITY ASSURANCE:
- [ ] Data validation checks (e.g., range checks, logic checks)
- [ ] Double-entry verification (if applicable)
- [ ] Peer review of coding (for qualitative data)
```

### 1.3 Data Storage & Backup

**Where and how you'll store data:**
```
PRIMARY STORAGE:
- Location: [e.g., University-provided OneDrive, external hard drive]
- Capacity: [e.g., 1 TB]
- Access: [e.g., password-protected, encrypted]

BACKUP STORAGE (3-2-1 Rule):
- Backup 1: [e.g., External hard drive (weekly)]
- Backup 2: [e.g., Cloud storage - Dropbox (daily auto-sync)]
- Backup 3: [e.g., University network drive (monthly)]

RETENTION PERIOD:
- During PhD: Active storage and backup
- After PhD: [e.g., 7 years as per university policy]
```

### 1.4 Data Security & Privacy

**How you'll protect sensitive data:**
```
SENSITIVITY LEVEL:
- [ ] Public (no restrictions)
- [ ] Internal (university community only)
- [ ] Confidential (restricted access, contains PII)
- [ ] Highly confidential (human subjects, health data)

SECURITY MEASURES:
- [ ] Encryption (AES-256 for files at rest)
- [ ] Password protection (strong passwords, 2FA)
- [ ] Access control (only authorized personnel)
- [ ] Anonymization/de-identification (remove PII)
- [ ] Secure transfer (encrypted channels only)

COMPLIANCE:
- [ ] IRB/Ethics approval obtained
- [ ] GDPR compliance (if EU participants)
- [ ] HIPAA compliance (if health data)
- [ ] Informed consent includes data storage/sharing clauses
```

### 1.5 Data Sharing & Preservation

**How you'll share data (if applicable):**
```
SHARING PLAN:
- [ ] Public repository (e.g., OSF, Zenodo, Figshare)
- [ ] Restricted access (upon request, with agreements)
- [ ] Embargoed until [date] (e.g., until publication)
- [ ] No sharing (sensitive data)

DATA REPOSITORY:
- Repository: [e.g., Open Science Framework (OSF)]
- DOI: [will be assigned upon deposit]
- Access conditions: [e.g., Creative Commons CC-BY license]

PRESERVATION:
- Format: Convert to open formats (CSV, TXT, PDF/A)
- Documentation: README, codebook, data dictionary
- Retention: [e.g., Permanent archival in university repository]
```

**TEMPLATE FILE:** Save as `/00_Admin/data_management_plan.docx`

---

## 2. FILE ORGANIZATION SYSTEM

**PRINCIPLE:** Consistent folder structure prevents chaos

### 2.1 Master Directory Structure

**Recommended PhD project structure:**

```
/PhD_Project_[YourName]/
│
├── /00_Admin/                          # Administrative documents
│   ├── data_management_plan.docx
│   ├── irb_approval.pdf
│   ├── consent_forms/
│   ├── ethics_documents/
│   └── progress_reports/
│
├── /01_Literature/                     # Literature review materials
│   ├── /pdfs/                          # All papers organized by topic
│   │   ├── /topic_1_stress_coping/
│   │   ├── /topic_2_methodology/
│   │   └── /topic_3_theory/
│   ├── /notes/                         # Reading notes, summaries
│   ├── /synthesis_matrix.xlsx         # Literature comparison table
│   └── /reference_library.bib         # Zotero/Mendeley library
│
├── /02_Data_Collection/                # Raw and processed data
│   ├── /01_raw_data/                   # NEVER EDIT - Read-only originals
│   │   ├── /surveys/
│   │   ├── /interviews/
│   │   └── /experiments/
│   ├── /02_processed_data/             # Cleaned, coded, analyzed
│   │   ├── survey_data_cleaned.csv
│   │   ├── interview_transcripts_coded/
│   │   └── analysis_datasets/
│   ├── /03_analysis_outputs/           # Statistical outputs, themes
│   │   ├── /quantitative/              # SPSS/R outputs
│   │   ├── /qualitative/               # NVivo/Atlas.ti outputs
│   │   └── /mixed_methods/
│   └── /04_figures_tables/             # All visualizations
│       ├── /figures/                   # Charts, graphs, images
│       └── /tables/                    # Data tables
│
├── /03_Analysis_Code/                  # All analysis scripts
│   ├── /01_data_cleaning/              # Data prep scripts
│   ├── /02_analysis_scripts/           # Main analysis (R, Python, SPSS syntax)
│   ├── /03_visualization/              # Figure generation scripts
│   └── README.md                       # How to run the code
│
├── /04_Writing/                        # Dissertation chapters
│   ├── /01_introduction/
│   ├── /02_literature_review/
│   ├── /03_methodology/
│   ├── /04_results/
│   ├── /05_discussion/
│   ├── /06_conclusion/
│   ├── /drafts/                        # Version-controlled drafts
│   └── /FINAL_DISSERTATION.docx
│
├── /05_Presentations/                  # Conference talks, defense
│   ├── /conference_2023/
│   ├── /proposal_defense/
│   └── /final_defense/
│
├── /06_Publications/                   # Papers derived from dissertation
│   ├── /paper_1_submitted/
│   └── /paper_2_draft/
│
├── /07_Supplementary_Materials/        # Appendices, extra data
│   ├── /appendix_A_survey_instrument.pdf
│   ├── /appendix_B_interview_protocol.docx
│   └── /appendix_C_additional_analyses/
│
└── /08_Archive/                        # Deprecated or old files
    ├── /old_drafts/
    └── /unused_analyses/
```

### 2.2 Subfolder Organization Tips

**Best practices:**
- ✅ Use clear, descriptive folder names
- ✅ Nest folders max 3-4 levels deep (avoid /folder/sub/sub/sub/sub/file.doc)
- ✅ Create a `/README.md` in each main folder explaining contents
- ✅ Use consistent naming: `/01_`, `/02_`, `/03_` for ordered folders
- ❌ NO spaces in folder names (use underscores: `my_folder` NOT `my folder`)
- ❌ NO special characters: `#`, `%`, `&`, `@` in folder names

---

## 3. FILE NAMING CONVENTIONS

**PRINCIPLE:** Filenames should be self-explanatory and sortable

### 3.1 General Naming Rules

**FORMAT:** `YYYY-MM-DD_ProjectAbbrev_Description_vX.ext`

**COMPONENTS:**
1. **Date (optional, but recommended for versions):** `YYYY-MM-DD` (ISO 8601 format)
   - Ensures chronological sorting
   - Example: `2025-03-15`

2. **Project abbreviation (optional):** Short code for project
   - Example: `PHDD` for "PhD Dissertation"

3. **Description:** Clear, concise description
   - Use underscores `_` instead of spaces
   - Use lowercase or CamelCase consistently
   - Example: `survey_data_cleaned` or `SurveyDataCleaned`

4. **Version number:** `_vX` or `_v1.2`
   - Increment for each revision
   - Example: `_v1`, `_v2`, `_v3` or `_v1.0`, `_v1.1`, `_v2.0`

5. **Extension:** File type
   - Example: `.csv`, `.docx`, `.pdf`, `.R`, `.py`

### 3.2 Examples by File Type

**DATA FILES:**
```
✅ GOOD:
- 2025-01-15_PHDD_survey_data_raw_v1.csv
- 2025-02-20_PHDD_survey_data_cleaned_v2.csv
- 2025-03-10_interview_transcripts_participant_001.docx
- analysis_dataset_final_v3.sav

❌ BAD:
- data.csv (not descriptive)
- Survey Data V2 Final FINAL.xlsx (spaces, inconsistent versioning)
- participant1.doc (ambiguous, no context)
```

**ANALYSIS SCRIPTS:**
```
✅ GOOD:
- 01_data_cleaning.R
- 02_descriptive_statistics.R
- 03_regression_analysis.py
- 04_thematic_analysis.nvp (NVivo project)

❌ BAD:
- analysis.R (not descriptive)
- Script 1.py (spaces, vague)
- final_analysis_NEW.R (ambiguous version)
```

**DISSERTATION CHAPTERS:**
```
✅ GOOD:
- 2025-03-01_chapter_01_introduction_v5.docx
- 2025-03-15_chapter_02_literature_review_v3.docx
- 2025-04-10_FULL_DISSERTATION_DRAFT_v2.docx

❌ BAD:
- chapter 1.docx (spaces, no version)
- Intro FINAL.docx (no date, vague)
- dissertation_v10_revised_FINAL_FINAL.docx (version chaos)
```

**FIGURES & TABLES:**
```
✅ GOOD:
- figure_01_conceptual_model.png
- figure_02_scatterplot_X_vs_Y.pdf
- table_01_participant_demographics.docx
- table_02_regression_results.xlsx

❌ BAD:
- fig1.jpg (not descriptive)
- Table 1 Updated.docx (spaces, no version)
- graph.png (too vague)
```

### 3.3 Version Control Naming

**For documents with frequent revisions (e.g., dissertation drafts):**

**OPTION 1: Date-based versioning**
```
2025-01-10_dissertation_draft.docx
2025-01-17_dissertation_draft.docx
2025-01-24_dissertation_draft.docx
```
*Pros:* Automatically chronological
*Cons:* Doesn't indicate major vs. minor changes

**OPTION 2: Semantic versioning**
```
dissertation_draft_v1.0.docx  (initial draft)
dissertation_draft_v1.1.docx  (minor revisions)
dissertation_draft_v2.0.docx  (major revision after advisor feedback)
dissertation_draft_v3.0.docx  (post-defense revisions)
```
*Pros:* Indicates magnitude of changes
*Cons:* Requires manual tracking

**OPTION 3: Descriptive versioning**
```
dissertation_draft_pre_proposal.docx
dissertation_draft_post_proposal.docx
dissertation_draft_pre_defense.docx
dissertation_draft_post_defense.docx
dissertation_FINAL_submitted.docx
```
*Pros:* Contextually meaningful
*Cons:* Limited granularity

**RECOMMENDATION:** Combine date + semantic version for critical documents
```
2025-03-15_dissertation_draft_v2.1.docx
```

---

## 4. VERSION CONTROL STRATEGY

**PRINCIPLE:** Never lose work; always be able to revert to earlier versions

### 4.1 Manual Version Control (Documents)

**For Word docs, Excel, SPSS files:**

1. **Keep master folder:**
   ```
   /04_Writing/
     ├── /drafts/
     │   ├── 2025-01-10_chapter_01_v1.docx
     │   ├── 2025-01-17_chapter_01_v2.docx
     │   └── 2025-01-24_chapter_01_v3.docx
     └── chapter_01_CURRENT.docx  (latest working version)
   ```

2. **Save milestones:**
   - Before major revisions: Save copy with date
   - After advisor feedback: Save copy with version increment
   - Before defense: Save copy labeled `_pre_defense`

3. **Use "Track Changes":**
   - In Word: Review → Track Changes
   - Shows edits, allows reversion
   - Save copies before accepting/rejecting changes

### 4.2 Git Version Control (Code & Analysis)

**For analysis scripts (R, Python, MATLAB):**

**SETUP:**
```bash
# Initialize Git in your analysis folder
cd /PhD_Project/03_Analysis_Code/
git init

# Create .gitignore file (exclude large data files)
echo "*.csv" >> .gitignore
echo "*.sav" >> .gitignore
echo "*.Rdata" >> .gitignore

# Make first commit
git add .
git commit -m "Initial commit: analysis setup"
```

**WORKFLOW:**
```bash
# Work on your analysis script
# ... edit 01_data_cleaning.R ...

# Save changes
git add 01_data_cleaning.R
git commit -m "Add outlier detection to data cleaning"

# Continue working
# ... edit 02_descriptive_statistics.R ...

git add 02_descriptive_statistics.R
git commit -m "Generate descriptive statistics table"

# View history
git log --oneline

# Revert to earlier version if needed
git checkout [commit-hash] 01_data_cleaning.R
```

**BACKUP TO GITHUB (OPTIONAL):**
```bash
# Create private repository on GitHub
# Link local repo to GitHub
git remote add origin https://github.com/yourusername/phd-analysis.git
git branch -M main
git push -u origin main

# Future pushes
git push
```

**BENEFITS:**
- Every save point is recoverable
- See exactly what changed between versions
- Collaborate with advisor/peers
- Automatic backup to cloud (GitHub)

### 4.3 Cloud Auto-Versioning

**Use built-in versioning in cloud storage:**

**OneDrive/Dropbox:**
- Automatically saves versions of files
- Right-click file → "Version history"
- Restore previous version if needed
- Retention: 30-90 days depending on plan

**Google Drive:**
- File → Version history → See version history
- Name versions: "Pre-defense draft", "Post-advisor feedback"
- Restore any previous version

**RECOMMENDATION:** Combine manual versioning + cloud auto-versioning for redundancy

---

## 5. BACKUP PROTOCOL (3-2-1 RULE)

**PRINCIPLE:** Never rely on a single copy of your data

### 5.1 The 3-2-1 Backup Rule

**3 COPIES** of your data:
1. Primary working copy (your laptop/desktop)
2. Backup copy 1 (external hard drive)
3. Backup copy 2 (cloud storage or offsite)

**2 DIFFERENT MEDIA TYPES:**
- Local storage (computer, external drive)
- Cloud storage (OneDrive, Dropbox, Google Drive)

**1 OFFSITE BACKUP:**
- Cloud storage (protects against fire, theft, disaster)
- University network drive (if available)

### 5.2 Backup Schedule

**FREQUENCY:**

**DAILY (Automated):**
- Cloud sync (Dropbox, OneDrive, Google Drive)
  - Set up auto-sync for `/PhD_Project/` folder
  - Runs in background, no manual action needed

**WEEKLY (Manual):**
- External hard drive backup
  - Every Friday: Copy entire `/PhD_Project/` to external drive
  - Label drive: "PhD Backup - [Your Name]"
  - Store drive in safe location

**MONTHLY (Manual):**
- University network drive (if available)
  - First Monday of month: Copy to university server
  - OR: Create compressed archive (.zip) and upload to cloud

**MILESTONE-BASED (Manual):**
- Before major events:
  - Before proposal defense: Full backup
  - Before final defense: Full backup
  - Before dissertation submission: Full backup

### 5.3 Backup Checklist

**BEFORE EACH BACKUP SESSION:**
```
Pre-Backup Checklist:
- [ ] Close all open files (ensure latest version is saved)
- [ ] Check primary storage space (ensure not full)
- [ ] Identify new/modified files since last backup
- [ ] Verify backup destination has sufficient space

Backup Steps:
- [ ] Copy entire `/PhD_Project/` folder to backup location
- [ ] Verify file count matches (source vs. destination)
- [ ] Spot-check critical files (open a few to ensure not corrupted)
- [ ] Record backup in log: Date, location, size

Post-Backup Verification:
- [ ] Check backup completed successfully (no errors)
- [ ] Confirm important files are present in backup
- [ ] Update backup log spreadsheet
```

**BACKUP LOG TEMPLATE:**
```
| Date       | Backup Type | Location              | Size  | Status | Notes              |
|------------|-------------|-----------------------|-------|--------|--------------------|
| 2025-03-15 | Daily       | Dropbox (auto-sync)   | 45 GB | ✅     | Auto-sync complete |
| 2025-03-15 | Weekly      | External HD (Seagate) | 45 GB | ✅     | Manual copy        |
| 2025-04-01 | Monthly     | Univ Network Drive    | 47 GB | ✅     | Compressed .zip    |
| 2025-05-10 | Milestone   | All locations         | 52 GB | ✅     | Pre-defense backup |
```

**SAVE LOG AS:** `/00_Admin/backup_log.xlsx`

### 5.4 Recommended Backup Tools

**FREE OPTIONS:**

1. **Cloud Storage (auto-sync):**
   - **Google Drive** (15 GB free, unlimited via university)
   - **Dropbox** (2 GB free, often expanded via university)
   - **OneDrive** (5 GB free, 1 TB via Office 365 Education)
   - **University-provided storage** (check your institution)

2. **External Hard Drive (manual):**
   - **Seagate Backup Plus** (1-5 TB, ~$50-150)
   - **Western Digital My Passport** (1-5 TB, ~$50-150)
   - **SanDisk Extreme Portable SSD** (500 GB-2 TB, faster, ~$80-300)

3. **Backup Software (optional):**
   - **FreeFileSync** (free, open-source, sync folders)
   - **Duplicati** (free, encrypted backups to cloud)
   - **rsync** (Linux/Mac command-line tool)

**PAID OPTIONS (if budget allows):**
- **Backblaze** ($7/month, unlimited cloud backup)
- **Crashplan** ($10/month, continuous backup)

---

## 6. DATA SECURITY & COMPLIANCE

**PRINCIPLE:** Protect sensitive data and comply with regulations

### 6.1 Data Classification

**CLASSIFY YOUR DATA:**

**PUBLIC (Level 0):**
- No restrictions
- Can be shared openly
- Examples: Published papers, public datasets, general methodology
- **Action:** No special security needed

**INTERNAL (Level 1):**
- University community only
- Not publicly shared
- Examples: Unpublished drafts, analysis code, non-sensitive research notes
- **Action:** Password-protect files, don't share outside institution

**CONFIDENTIAL (Level 2):**
- Restricted access, contains Personally Identifiable Information (PII)
- Examples: Survey data with names/emails, interview transcripts with identifiers
- **Action:** Encryption, de-identification, access controls

**HIGHLY CONFIDENTIAL (Level 3):**
- Strictly restricted, human subjects, health data
- Examples: Medical records, video recordings of participants, sensitive personal data
- **Action:** Full encryption, secure storage, IRB compliance, HIPAA compliance (if applicable)

**DETERMINE YOUR DATA LEVEL:**
```
My data is classified as: [PUBLIC / INTERNAL / CONFIDENTIAL / HIGHLY CONFIDENTIAL]

Justification: [e.g., Contains interview transcripts with participant pseudonyms but no direct identifiers]

Required security measures: [e.g., Encryption, password protection, de-identification]
```

### 6.2 De-Identification & Anonymization

**For human subjects research:**

**REMOVE DIRECT IDENTIFIERS:**
- [ ] Names (replace with pseudonyms or codes: P001, P002)
- [ ] Email addresses
- [ ] Phone numbers
- [ ] Addresses (or generalize: "Northeast US" instead of "Boston, MA")
- [ ] Dates of birth (or use age ranges: "25-30" instead of "27")
- [ ] Social Security Numbers
- [ ] IP addresses (if digital data)

**SEPARATE IDENTIFIABLE DATA:**
- **Consent forms** (contain names, signatures) → Store separately in encrypted folder
- **Contact list** (for follow-up) → Store separately, link by participant ID only
- **De-identified dataset** → Use for analysis, safe to share with collaborators

**EXAMPLE:**
```
BEFORE DE-IDENTIFICATION:
Name: Jane Doe
Email: jane.doe@email.com
Age: 27
City: Boston, MA

AFTER DE-IDENTIFICATION:
Participant ID: P001
Email: [REMOVED]
Age Range: 25-30
Region: Northeast US
```

### 6.3 Encryption

**WHEN TO ENCRYPT:**
- Data contains PII
- Data is confidential or highly confidential
- Data is stored on portable devices (laptop, USB drive)
- Data is transmitted over internet

**HOW TO ENCRYPT:**

**OPTION 1: File/Folder Encryption (Windows - BitLocker, Mac - FileVault)**

**Windows (BitLocker):**
```
1. Right-click external drive or folder
2. Select "Turn on BitLocker"
3. Choose "Use a password to unlock the drive"
4. Set strong password (12+ characters, mix of upper/lower/numbers/symbols)
5. Save recovery key in secure location (NOT on same drive)
6. Encrypt
```

**Mac (FileVault):**
```
1. System Preferences → Security & Privacy → FileVault
2. Turn On FileVault
3. Choose recovery method (save to iCloud or create recovery key)
4. Restart to encrypt
```

**OPTION 2: File-Level Encryption (7-Zip, VeraCrypt)**

**7-Zip (Free, cross-platform):**
```
1. Right-click folder → 7-Zip → Add to archive
2. Archive format: .7z
3. Encryption method: AES-256
4. Enter password (strong password)
5. Click OK
6. Delete original folder (after verifying encrypted archive works)
```

**VeraCrypt (Free, advanced):**
```
1. Download VeraCrypt
2. Create encrypted volume (container)
3. Set password
4. Mount volume to access files
5. Dismount when done
```

**OPTION 3: Cloud Encryption (Cryptomator, Boxcryptor)**

**Cryptomator (Free, encrypts cloud-synced folders):**
```
1. Download Cryptomator
2. Create vault in Dropbox/Google Drive folder
3. Set password
4. Unlock vault to access files
5. Files are encrypted before upload to cloud
```

**PASSWORD MANAGEMENT:**
- Use a **password manager** (LastPass, 1Password, Bitwarden) to store encryption passwords
- ❌ DON'T write passwords on sticky notes or in plain text files
- ✅ DO use strong, unique passwords for each encrypted volume

### 6.4 Access Control

**RESTRICT WHO CAN ACCESS DATA:**

**LOCAL COMPUTER:**
- Set up user account with password
- Enable auto-lock after 5-10 minutes of inactivity
- Use strong password (12+ characters)

**SHARED FOLDERS (OneDrive, Google Drive, Dropbox):**
- Don't share entire PhD folder publicly
- Share specific subfolders only with collaborators/advisor
- Set permissions:
  - **View only:** For reviewers who should not edit
  - **Edit:** For co-authors, advisor
  - **Owner:** You only
- Use expiring links (auto-expire after 30 days) for temporary sharing

**COLLABORATION:**
- Create `/Shared/` subfolder for collaborative work
- Keep confidential data in `/Private/` (not synced to cloud)

### 6.5 Secure Data Transfer

**WHEN SENDING FILES:**

**EMAIL (for small files <25 MB):**
- ✅ Encrypt sensitive files before attaching (use 7-Zip with password)
- ✅ Send password via separate channel (text message, phone call)
- ❌ DON'T email unencrypted sensitive data

**CLOUD SHARING (for large files):**
- ✅ Upload to secure cloud (OneDrive, Google Drive, Dropbox)
- ✅ Set password-protected link
- ✅ Set expiration date
- ✅ Send password via separate channel

**SECURE FILE TRANSFER SERVICES:**
- **Box** (university often provides)
- **Tresorit** (end-to-end encrypted)
- **Send** by Firefox (free, encrypted, self-destructing links)

### 6.6 Compliance Checklists

**IRB COMPLIANCE (Human Subjects Research):**
```
- [ ] IRB approval obtained before data collection
- [ ] Informed consent forms signed by all participants
- [ ] Consent forms mention data storage, sharing, retention
- [ ] Participant data de-identified (remove PII)
- [ ] Data stored securely (encrypted if confidential)
- [ ] Access restricted to authorized research team only
- [ ] Data retention plan follows IRB-approved timeline
- [ ] Data destruction plan in place (if required by IRB)
```

**GDPR COMPLIANCE (EU Participants):**
```
- [ ] Participants informed about data collection, use, storage
- [ ] Explicit consent obtained (opt-in, not opt-out)
- [ ] Right to access: Participants can request their data
- [ ] Right to erasure: Participants can request deletion
- [ ] Data minimization: Collect only necessary data
- [ ] Data stored securely (encryption)
- [ ] Data breach notification plan in place
```

**HIPAA COMPLIANCE (Health Data, US):**
```
- [ ] HIPAA training completed
- [ ] Protected Health Information (PHI) de-identified
- [ ] Minimum necessary standard (only collect needed data)
- [ ] Encryption of ePHI (electronic PHI)
- [ ] Access controls (who can access PHI)
- [ ] Audit trail (log who accesses data, when)
- [ ] Business Associate Agreements (if working with third parties)
```

**SAVE COMPLIANCE RECORDS:** `/00_Admin/ethics_compliance/`

---

## 7. DATA DOCUMENTATION

**PRINCIPLE:** Future-you (and others) should understand your data without you present

### 7.1 README Files

**CREATE A README IN EVERY MAJOR FOLDER:**

**TEMPLATE:**
```markdown
# [Folder Name] - README

**Purpose:** [What is this folder for?]

**Contents:** [What files/subfolders are here?]

**Key Files:**
- `file_1.csv`: [Description]
- `file_2.docx`: [Description]

**How to Use:**
[Step-by-step instructions if applicable]

**Last Updated:** [YYYY-MM-DD]

**Contact:** [Your name, email]
```

**EXAMPLE - `/02_Data_Collection/README.md`:**
```markdown
# Data Collection - README

**Purpose:** This folder contains all raw and processed data for the PhD dissertation on university student coping strategies.

**Contents:**
- `/01_raw_data/`: Original data files (READ-ONLY, never edit)
- `/02_processed_data/`: Cleaned and coded datasets
- `/03_analysis_outputs/`: Statistical and qualitative analysis results
- `/04_figures_tables/`: All visualizations and tables

**Key Files:**
- `survey_data_raw_v1.csv`: Raw survey responses (n=250) collected 2025-01-15
- `survey_data_cleaned_v2.csv`: Cleaned survey data (outliers removed, missing data handled)
- `interview_transcripts_coded/`: 25 interview transcripts with thematic coding in NVivo

**How to Use:**
1. Start with raw data in `/01_raw_data/` (if replication needed)
2. Use cleaned data in `/02_processed_data/` for analysis
3. Analysis scripts in `/03_Analysis_Code/` generate outputs in `/03_analysis_outputs/`

**Last Updated:** 2025-03-15

**Contact:** [Your Name], [your.email@university.edu]
```

### 7.2 Data Dictionary / Codebook

**For quantitative datasets:**

**TEMPLATE:**
```
| Variable Name | Description | Type | Values/Range | Missing Data Code | Notes |
|---------------|-------------|------|--------------|-------------------|-------|
| participant_id | Unique participant identifier | Numeric | 1-250 | N/A | Primary key |
| age | Participant age in years | Numeric | 18-65 | 999 | Self-reported |
| gender | Participant gender | Categorical | 1=Male, 2=Female, 3=Non-binary, 4=Prefer not to say | 9 | |
| stress_score | Perceived Stress Scale total | Numeric | 0-40 | 999 | Higher = more stress |
| coping_avoid | Avoidance coping subscale | Numeric | 1-5 (Likert) | 9 | Higher = more avoidance |
| coping_reframe | Reframing coping subscale | Numeric | 1-5 (Likert) | 9 | Higher = more reframing |
```

**EXAMPLE - Survey Codebook:**
```
DATASET: survey_data_cleaned_v2.csv
N = 250 participants
Data collection: 2025-01-15 to 2025-02-28

VARIABLES:
1. participant_id: Unique ID (1-250)
2. age: Age in years (18-65)
   - Missing: 999 (n=3 participants)
3. gender: 1=Male (n=80), 2=Female (n=170), 3=Non-binary (n=0), 4=Prefer not to say (n=0)
4. stress_score: Perceived Stress Scale (PSS-10) total score (0-40)
   - Scale: Cohen et al. (1983)
   - Interpretation: 0-13 (low), 14-26 (moderate), 27-40 (high)
   - Cronbach's α = .85
5. coping_avoid: Avoidance coping subscale (Brief COPE)
   - 4 items, 1-5 Likert scale
   - Mean score (1-5)
   - Higher = more avoidance coping
6. coping_reframe: Reframing coping subscale (Brief COPE)
   - 4 items, 1-5 Likert scale
   - Mean score (1-5)
   - Higher = more reframing coping
```

**SAVE AS:** `/02_Data_Collection/02_processed_data/survey_data_codebook.xlsx`

### 7.3 Analysis Documentation

**For each analysis script:**

**INCLUDE IN SCRIPT:**
```R
# ============================================================
# SCRIPT: 02_descriptive_statistics.R
# PURPOSE: Generate descriptive statistics for survey data
# AUTHOR: [Your Name]
# DATE: 2025-03-15
# LAST UPDATED: 2025-03-20
# ============================================================

# INPUT FILES:
# - survey_data_cleaned_v2.csv

# OUTPUT FILES:
# - descriptive_stats_table.html
# - descriptive_stats_by_group.xlsx

# DEPENDENCIES:
# - R version 4.2.0 or higher
# - Packages: dplyr, psych, gt

# CHANGELOG:
# 2025-03-15: Initial script created
# 2025-03-20: Added stratification by gender
# ============================================================

# Load libraries
library(dplyr)
library(psych)
library(gt)

# Load data
data <- read.csv("../02_Data_Collection/02_processed_data/survey_data_cleaned_v2.csv")

# ... [rest of code] ...
```

### 7.4 Method Logs

**For qualitative research:**

**KEEP A RESEARCH LOG:**
```
RESEARCH LOG - Interview Data Collection

DATE: 2025-02-15
PARTICIPANT: P007
INTERVIEW DURATION: 45 minutes
LOCATION: University counseling center (private room)
INTERVIEWER: [Your Name]

NOTES:
- Participant was initially reserved but opened up midway
- Asked for clarification on Q3 (reworded: "How do you typically respond to stress?")
- Mentioned recent exam stress as example
- Recording quality: Good (clear audio)
- Transcription: Completed 2025-02-18 by [transcriber name]

FOLLOW-UP NEEDED:
- None

MEMOS:
- P007's description of "compartmentalization" aligns with avoidance coping theme
- Consider adding probing question about long-term effectiveness of strategies
```

**SAVE AS:** `/02_Data_Collection/01_raw_data/interviews/interview_log.docx`

---

## 8. COLLABORATION & SHARING

**PRINCIPLE:** Share data safely and efficiently with collaborators

### 8.1 Shared Folder Structure

**CREATE A SHARED WORKSPACE:**
```
/PhD_Project/
  ├── /00_Shared/                  # ONLY this folder is shared
  │   ├── /manuscripts/            # Co-authored papers
  │   ├── /presentations/          # Shared slides
  │   ├── /analysis_outputs/       # Results to discuss
  │   └── README.md                # Collaboration guidelines
  │
  └── /00_Private/                 # NOT SHARED
      ├── /raw_data/               # Confidential participant data
      ├── /personal_notes/         # Research journal, memos
      └── /admin/                  # IRB docs, passwords
```

### 8.2 Sharing Best Practices

**WITH ADVISOR:**
- Share specific drafts for feedback (not entire project folder)
- Use cloud sharing with "Comment" permissions (not "Edit" unless co-writing)
- Version control: `2025-03-15_chapter_01_v3_FOR_REVIEW.docx`
- Track changes: Enable "Track Changes" in Word for revisions

**WITH CO-AUTHORS:**
- Use collaborative writing tools:
  - **Google Docs** (real-time collaboration)
  - **Overleaf** (LaTeX collaboration)
  - **Microsoft Word Online** (co-authoring)
- Agree on file naming conventions upfront
- Designate one person as "version manager" to merge edits

**WITH REVIEWERS (CONFERENCE, JOURNAL):**
- Share only de-identified data and analysis code
- Use anonymous repositories (e.g., OSF with anonymous link)
- Include README explaining how to run code/reproduce results

### 8.3 Data Sharing Agreements

**IF SHARING SENSITIVE DATA WITH COLLABORATORS:**

**TEMPLATE - Data Use Agreement (DUA):**
```
DATA USE AGREEMENT

This agreement is between:
- Data Provider: [Your Name], [University]
- Data User: [Collaborator Name], [Their Institution]

DATA DESCRIPTION:
- Dataset: [e.g., Survey data on university student coping strategies]
- Format: [e.g., De-identified .csv file]
- Size: [e.g., n=250 participants, 15 variables]

PERMITTED USES:
- [ ] Analysis for research purposes only
- [ ] Inclusion in publications (with acknowledgment)
- [ ] Presentation at conferences
- [ ] NOT permitted: Commercial use, redistribution

SECURITY REQUIREMENTS:
- [ ] Data must be stored on password-protected computer
- [ ] Data must be encrypted if stored on portable devices
- [ ] Data must not be shared with third parties without consent
- [ ] Data must be deleted after project completion (specify date)

DATA PROVIDER OBLIGATIONS:
- Provide de-identified dataset
- Provide codebook and documentation
- Respond to questions about data

DATA USER OBLIGATIONS:
- Use data only for agreed purposes
- Acknowledge data source in publications
- Report any data breaches immediately
- Delete data after project completion

SIGNATURES:
Data Provider: __________________ Date: __________
Data User: _____________________ Date: __________
```

**SAVE AS:** `/00_Admin/data_use_agreement_[collaborator_name].pdf`

---

## 9. DATA ARCHIVING & PRESERVATION

**PRINCIPLE:** Ensure your data survives long-term (5-10 years post-PhD)

### 9.1 When to Archive

**ARCHIVE DATA:**
- After dissertation defense
- Before leaving university (graduation)
- After publication (journal may require data deposit)
- At end of retention period (per IRB/university policy)

### 9.2 Archiving Checklist

**PREPARE DATA FOR ARCHIVING:**
```
Pre-Archive Checklist:
- [ ] De-identify all data (remove PII if not already done)
- [ ] Convert to open formats (see Section 9.3)
- [ ] Create comprehensive documentation (README, codebook, method notes)
- [ ] Include analysis code and scripts
- [ ] Organize folder structure logically
- [ ] Test that someone else can understand/reproduce your work
- [ ] Compress files if needed (.zip or .tar.gz)

Archive Submission:
- [ ] Choose repository (see Section 9.4)
- [ ] Upload data and documentation
- [ ] Add metadata (title, author, abstract, keywords)
- [ ] Assign license (CC-BY, CC0, or restricted access)
- [ ] Obtain DOI (Digital Object Identifier)
- [ ] Record DOI in dissertation and publications

Post-Archive:
- [ ] Verify archive is accessible
- [ ] Add DOI to dissertation acknowledgments
- [ ] Update CV with data publication
```

### 9.3 File Format Conversion (Open Formats)

**CONVERT PROPRIETARY FORMATS TO OPEN FORMATS FOR LONG-TERM PRESERVATION:**

| Proprietary Format | Open Format | Conversion Tool |
|--------------------|-------------|-----------------|
| `.xlsx` (Excel) | `.csv` (Comma-separated values) | Excel: Save As → CSV |
| `.sav` (SPSS) | `.csv` + `.txt` codebook | SPSS: Export → CSV |
| `.docx` (Word) | `.pdf/A` or `.txt` | Word: Save As → PDF |
| `.nvp` (NVivo) | `.txt` transcripts + `.xlsx` coding | NVivo: Export → Text |
| `.pptx` (PowerPoint) | `.pdf` | PowerPoint: Save As → PDF |
| `.R` (R script) | `.R` (already open) | No conversion needed |
| `.py` (Python) | `.py` (already open) | No conversion needed |

**RECOMMENDED OPEN FORMATS:**
- **Data:** `.csv`, `.txt`, `.json`, `.xml`
- **Documents:** `.pdf/A`, `.txt`, `.md` (Markdown)
- **Images:** `.png`, `.tiff`, `.svg`
- **Code:** `.R`, `.py`, `.m`, `.do` (already text-based, no conversion needed)

### 9.4 Data Repositories

**WHERE TO ARCHIVE:**

**GENERAL-PURPOSE REPOSITORIES (accept any discipline):**
1. **Open Science Framework (OSF)** - https://osf.io/
   - Free, unlimited storage
   - DOI provided
   - Private or public
   - Integrates with analysis tools

2. **Zenodo** - https://zenodo.org/
   - Free (up to 50 GB per dataset)
   - DOI provided
   - Run by CERN, long-term preservation guaranteed

3. **Figshare** - https://figshare.com/
   - Free (20 GB per file, unlimited files)
   - DOI provided
   - Good for figures, tables, presentations

**DISCIPLINE-SPECIFIC REPOSITORIES:**
- **Social Sciences:** ICPSR, UK Data Archive, Harvard Dataverse
- **Psychology:** PsychArchives
- **Biology:** GenBank, Dryad
- **Health:** dbGaP, NIMH Data Archive
- **Physics/Astronomy:** arXiv, ADS

**INSTITUTIONAL REPOSITORIES:**
- Check your university library (most have data repositories)
- Often required for theses/dissertations
- Long-term preservation guaranteed by institution

**CHOOSING A REPOSITORY:**
```
Decision Tree:

1. Does my journal/funder require specific repository?
   YES → Use that repository
   NO → Go to 2

2. Is there a discipline-specific repository for my field?
   YES → Use discipline-specific (better discoverability)
   NO → Go to 3

3. Does my university have a data repository?
   YES → Use university repository (easy, required for thesis)
   NO → Go to 4

4. Use general-purpose repository:
   - OSF (if you used OSF for project management)
   - Zenodo (if you want long-term CERN backing)
   - Figshare (if you have many figures/visualizations)
```

### 9.5 Data Licensing

**CHOOSE A LICENSE FOR SHARED DATA:**

**OPEN LICENSES (encourage reuse):**
- **CC0 (Public Domain):** No restrictions, anyone can use for any purpose
  - Best for: Maximum reuse, no attribution required

- **CC-BY (Attribution):** Reuse allowed with credit
  - Best for: Most research data (standard choice)

- **CC-BY-SA (Attribution-ShareAlike):** Reuse with credit, derivatives must use same license
  - Best for: Ensuring downstream data remains open

**RESTRICTED ACCESS:**
- **Embargo:** Public after [date] (e.g., after publication)
- **Upon Request:** Data available only after contacting author
- **No Sharing:** Data not shared (only metadata visible)

**RECOMMENDATION:** Use **CC-BY** for most research data (allows reuse with credit)

**ADD TO README:**
```markdown
## License

This dataset is licensed under a Creative Commons Attribution 4.0 International License (CC-BY 4.0).

You are free to:
- Share: Copy and redistribute the material
- Adapt: Remix, transform, and build upon the material

Under the following terms:
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Full license: https://creativecommons.org/licenses/by/4.0/
```

---

## 10. EMERGENCY RECOVERY PROCEDURES

**PRINCIPLE:** Have a plan BEFORE disaster strikes

### 10.1 Disaster Scenarios & Recovery Steps

**SCENARIO 1: Laptop Stolen/Lost**

**IMMEDIATE ACTIONS:**
1. Report to campus police/local authorities
2. Change passwords (email, cloud storage, university accounts)
3. Check backups:
   - Cloud storage: Log in from another device, verify data intact
   - External hard drive: If not stolen, data is safe
4. Notify advisor of situation

**RECOVERY:**
- Restore data from cloud backup to new device
- If no backups exist: Attempt to recover from collaborators, advisor shared folders
- If data lost: Report to IRB (if human subjects), assess impact on research timeline

**PREVENTION:**
- Enable "Find My Device" (Windows, Mac) to track stolen laptop
- Full-disk encryption (BitLocker, FileVault) prevents data theft
- Never leave laptop unattended in public

---

**SCENARIO 2: Ransomware/Malware Attack**

**IMMEDIATE ACTIONS:**
1. Disconnect from internet (Wi-Fi off, unplug Ethernet)
2. Do NOT pay ransom
3. Do NOT open any files or click links
4. Contact university IT security team

**RECOVERY:**
1. Wipe infected computer (reinstall OS)
2. Restore data from clean backup (before infection date)
3. Scan backups for malware before restoring
4. Change all passwords after recovery

**PREVENTION:**
- Keep OS and software updated (auto-updates on)
- Use antivirus software (Windows Defender, Malwarebytes)
- Don't open suspicious emails or attachments
- Backup regularly (3-2-1 rule) so you can restore from clean backup

---

**SCENARIO 3: Cloud Storage Account Hacked**

**IMMEDIATE ACTIONS:**
1. Change password immediately
2. Enable two-factor authentication (2FA)
3. Check account activity (login history, file changes)
4. Revoke access from unrecognized devices/apps

**RECOVERY:**
1. Restore deleted files from cloud version history (if applicable)
2. If files modified: Restore from local backup or external drive
3. Review shared links (revoke any suspicious shares)

**PREVENTION:**
- Use strong, unique passwords (password manager)
- Enable 2FA on all cloud accounts
- Monitor account activity regularly
- Use university-provided cloud storage (often more secure than personal accounts)

---

**SCENARIO 4: Accidental File Deletion**

**IMMEDIATE ACTIONS:**
1. Check Recycle Bin/Trash (restore if present)
2. Check cloud version history (OneDrive, Dropbox, Google Drive)
3. Check local backups (external drive, Time Machine)

**RECOVERY:**
- Cloud: Right-click file → "Version history" → Restore previous version
- Windows: Right-click folder → "Restore previous versions"
- Mac: Time Machine → Browse backups → Restore
- External drive: Copy file back from backup

**PREVENTION:**
- Don't empty Recycle Bin too frequently (gives buffer time to recover)
- Use version control (Git for code, cloud auto-versioning for docs)
- Regular backups (3-2-1 rule)

---

**SCENARIO 5: Hard Drive Failure**

**IMMEDIATE ACTIONS:**
1. Stop using the drive immediately (don't write any new data)
2. If clicking/grinding sounds: Power off, seek professional data recovery
3. If no physical damage: Attempt recovery using data recovery software

**RECOVERY:**
- DIY recovery: Use software (Recuva, EaseUS, PhotoRec) to scan for files
- Professional recovery: Send drive to data recovery service ($500-3,000, not guaranteed)
- If no recovery possible: Restore from backups

**PREVENTION:**
- Use SSDs (more reliable than HDDs)
- Monitor drive health (CrystalDiskInfo for Windows, DriveDx for Mac)
- Regular backups (3-2-1 rule) - hardware failure is WHEN, not IF

---

### 10.2 Emergency Contact List

**KEEP THIS INFORMATION ACCESSIBLE (print and keep with backups):**

```
EMERGENCY CONTACT LIST - PhD Data Recovery

PhD CANDIDATE:
Name: [Your Name]
Email: [your.email@university.edu]
Phone: [Your Phone]

ADVISOR:
Name: [Advisor Name]
Email: [advisor@university.edu]
Phone: [Advisor Phone]

UNIVERSITY IT SUPPORT:
Department: [IT Help Desk]
Email: [ithelpdesk@university.edu]
Phone: [IT Phone]
Hours: [M-F 9am-5pm]

UNIVERSITY DATA SECURITY:
Department: [IT Security / Information Security Office]
Email: [security@university.edu]
Phone: [Security Phone]

IRB CONTACT (for data breach reporting):
Department: [Institutional Review Board]
Email: [irb@university.edu]
Phone: [IRB Phone]

CLOUD STORAGE SUPPORT:
- OneDrive: https://support.microsoft.com/ | 1-800-xxx-xxxx
- Dropbox: https://www.dropbox.com/support | support ticket
- Google Drive: https://support.google.com/drive | support ticket

DATA RECOVERY SERVICE (if needed):
- [Company Name]
- Phone: [Phone]
- Website: [URL]

BACKUP LOCATIONS:
- Primary: [e.g., Laptop - C:/PhD_Project/]
- Backup 1: [e.g., External HD - Seagate 2TB, stored at home]
- Backup 2: [e.g., OneDrive - auto-sync]
- Backup 3: [e.g., University network drive - \\uni-server\phd_data\]
```

**SAVE AS:** `/00_Admin/emergency_contacts.pdf` + **Print and keep with external hard drive**

---

## 11. FINAL CHECKLIST - Data Management Readiness

**BEFORE STARTING DATA COLLECTION:**
```
Setup Checklist:
- [ ] Data Management Plan (DMP) created and approved
- [ ] Folder structure established (see Section 2)
- [ ] File naming conventions agreed upon (see Section 3)
- [ ] Backup system in place (3-2-1 rule, see Section 5)
- [ ] Cloud storage set up and tested
- [ ] External hard drive purchased and labeled
- [ ] Encryption enabled (if handling sensitive data, see Section 6.3)
- [ ] IRB approval obtained (if human subjects)
- [ ] README files created in main folders (see Section 7.1)
- [ ] Emergency contact list printed (see Section 10.2)
```

**DURING PhD (MONTHLY CHECK):**
```
Maintenance Checklist:
- [ ] Backups completed on schedule (daily cloud, weekly external HD, monthly offsite)
- [ ] Backup log updated (see Section 5.3)
- [ ] New files organized according to folder structure
- [ ] New files named according to conventions
- [ ] README files updated with new files/changes
- [ ] Version control used for drafts and code
- [ ] No confidential data in shared folders
- [ ] Cloud storage space sufficient (<80% full)
```

**BEFORE DISSERTATION SUBMISSION:**
```
Archiving Checklist:
- [ ] All data de-identified (PII removed)
- [ ] Files converted to open formats (see Section 9.3)
- [ ] Comprehensive documentation created (README, codebook, method notes)
- [ ] Analysis code cleaned and commented
- [ ] Data uploaded to repository (OSF, Zenodo, institutional)
- [ ] DOI obtained and added to dissertation
- [ ] License assigned (CC-BY recommended)
- [ ] Final backup created (all locations)
- [ ] Data destruction plan followed (if required by IRB)
```

---

## 12. ADDITIONAL RESOURCES

**TOOLS:**
- **File Organization:** FreeFileSync (folder synchronization)
- **Encryption:** VeraCrypt, Cryptomator, 7-Zip
- **Backup:** Backblaze, Duplicati, rsync
- **Version Control:** Git, GitHub Desktop, GitKraken
- **Cloud Storage:** OneDrive (university), Google Drive, Dropbox
- **Data Repositories:** OSF, Zenodo, Figshare, institutional repository
- **Password Management:** LastPass, 1Password, Bitwarden

**GUIDES:**
- **Data Management Plans:** DMP Tool (https://dmptool.org/)
- **File Naming:** UK Data Service (https://ukdataservice.ac.uk/learning-hub/research-data-management/format-your-data/naming/)
- **Research Data Management:** MANTRA (https://mantra.ed.ac.uk/)
- **Open Science:** Center for Open Science (https://www.cos.io/)

**UNIVERSITY RESOURCES:**
- Library data services (consult librarian specializing in research data)
- IT support (cloud storage, network drives, encryption)
- Research office (DMP templates, compliance guidance)
- IRB office (data security requirements)

---

**END OF DATA MANAGEMENT PROTOCOL**

**REMEMBER:**
- **Prevention > Recovery:** Set up systems BEFORE you need them
- **Consistency:** Follow the same procedures every time
- **Documentation:** Future-you will thank present-you
- **Backup, Backup, Backup:** Data loss is the #1 avoidable PhD disaster

**YOU GOT THIS!** 🎓📊🔒
