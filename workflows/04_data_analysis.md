# Stage 4: Data Collection & Analysis Execution
## Detailed Prompt Chain

**⚠️ CRITICAL:** Only begin Stage 4 after:
1. IRB approval obtained (if required)
2. Committee approved methodology
3. All instruments finalized and tested
4. Data management plan in place

---

## 🎯 SUBCOMPONENTS

1. Data Collection Management
2. Data Quality Monitoring
3. Data Organization & Cleaning
4. Quantitative Data Analysis
5. Qualitative Data Analysis
6. Mixed Methods Integration
7. Results Interpretation
8. Results Visualization & Writing

---

## 📥 REQUIRED INFORMATION (INPUTS)

- Approved methodology (from Stage 3)
- IRB approval (if required)
- Data collection instruments (finalized)
- Analysis plan (detailed)
- Software setup and functioning
- Secure storage for data

---

## 📤 DELIVERABLES (OUTPUTS)

1. Raw data files (secured appropriately)
2. Cleaned data files
3. Data collection log/audit trail
4. Analysis outputs (statistics, themes, codes)
5. Figures and tables (publication-quality)
6. Findings summary document
7. Results interpretation memos
8. Complete Chapter 6: Results (10,000-15,000 words)

---

## 🤖 AI PROMPT CHAINS

### Prompt 4.1: Create Data Collection Management System

**USER INPUT REQUIRED:**
- Data collection plan from Stage 3
- Timeline and target N
- Team members (if applicable)

**PROMPT:**
```
My data collection plan:
- Method: [surveys/interviews/observations/experiments/computational]
- Timeline: [start date to end date]
- Target: [number of participants or data points]
- Team: [solo or number of research assistants]

Help me create a comprehensive data collection management system:

1. TRACKING SYSTEM:

   Design participant tracking spreadsheet:

   | Participant ID | Contact | Invited Date | Responded | Consent Signed | Data Collected | Completed | Notes |
   |----------------|---------|--------------|-----------|----------------|----------------|-----------|-------|
   | P001 | email@... | 2024-01-15 | Yes | Yes | 2024-01-20 | Yes | No issues |
   | P002 | email@... | 2024-01-15 | No | -- | -- | No | Follow-up sent |

   Columns to include:
   - Participant ID (never use names in data files)
   - Contact information (separate secure file)
   - Recruitment date
   - Response status
   - Consent status (signed Y/N, date)
   - Data collection date(s)
   - Completion status
   - Compensation status (if applicable)
   - Notes/issues

2. DATA COLLECTION LOG:

   Template to record details of each session:

   ```
   Date: [YYYY-MM-DD]
   Participant ID: [P###]
   Data Collector: [Your name or RA name]
   Start Time: [HH:MM]
   End Time: [HH:MM]
   Method: [Survey/Interview/Observation/Experiment]
   Location: [If relevant]

   Equipment/Materials:
   - [ ] Consent form
   - [ ] Recording device (if applicable)
   - [ ] Survey instrument
   - [ ] Compensation

   Session Notes:
   - [Any issues, observations, deviations from protocol]

   Data Quality:
   - Completeness: [Complete / Partial - explain]
   - Audio quality (if recorded): [Excellent / Good / Poor]
   - Participant engagement: [High / Medium / Low]

   Data Saved:
   - File name: [consistent naming convention]
   - Backup location: [confirmed Y/N]

   Follow-up needed: [Y/N - explain]
   ```

3. QUALITY CHECKS:

   PRE-SESSION CHECKLIST:
   - [ ] Participant confirmed attendance
   - [ ] Consent form printed/ready
   - [ ] Instruments/materials ready
   - [ ] Recording equipment tested (if applicable)
   - [ ] Quiet/appropriate space secured
   - [ ] Compensation ready (if applicable)

   DURING-SESSION CHECKLIST:
   - [ ] Consent obtained and signed
   - [ ] Confidentiality explained
   - [ ] Participant comfortable and willing
   - [ ] Recording started (if applicable)
   - [ ] All questions asked/all measures collected
   - [ ] Debriefing conducted (if applicable)

   POST-SESSION CHECKLIST:
   - [ ] Data file saved with correct naming
   - [ ] Data backed up to secure location
   - [ ] Equipment returned/stored
   - [ ] Session log completed
   - [ ] Any issues documented
   - [ ] Compensation provided (if applicable)

4. FILE NAMING CONVENTION:

   Establish consistent naming:

   For human subjects data:
   - `P###_[DataType]_[YYYYMMDD].ext`
   - Example: `P001_interview_20240115.mp3`
   - Example: `P042_survey_20240228.csv`

   For computational experiments:
   - `experiment_[name]_run[#]_seed[###]_[YYYYMMDD].csv`
   - Example: `experiment_latency_run1_seed42_20240115.csv`

   NEVER include names or identifiable info in file names!

5. BACKUP PROTOCOL:

   Implement 3-2-1 rule:
   - 3 copies of data
   - 2 different storage media
   - 1 off-site

   Backup schedule:
   - **Daily**: After each data collection session
   - **Weekly**: Full backup to external drive
   - **Monthly**: Cloud backup (encrypted)

   Backup checklist:
   - [ ] Data copied to encrypted external drive
   - [ ] Data copied to secure university server
   - [ ] Cloud backup updated (if permitted by IRB)
   - [ ] Backup integrity verified (spot check files open correctly)
   - [ ] Backup log updated with date and contents

6. SECURITY PROTOCOLS:

   For human subjects data:
   - Encrypt all data files
   - Password-protect spreadsheets
   - Store consent forms separately from data (locked cabinet)
   - Never email unencrypted data
   - Limit access to research team only
   - Delete data from recording devices after transfer

   For computational data:
   - Version control (Git)
   - Document preprocessing steps
   - Keep raw data immutable (never overwrite originals)

Generate templates for:
1. Participant tracking spreadsheet
2. Data collection log template
3. Quality checklist
4. Backup log
```

**EXPECTED OUTPUT:** Complete data management system (templates and protocols)

**SAVE AS:** `/04_Data_Analysis/data_management_system/` directory with all templates

---

### Prompt 4.2: Monitor Data Quality During Collection

**USER INPUT REQUIRED:**
- Type of data being collected
- Quality criteria from methodology

**PROMPT:**
```
Type of data: [quantitative/qualitative/computational/mixed]

Quality criteria: [completeness, validity, reliability, etc.]

Help me establish real-time data quality monitoring:

1. QUANTITATIVE DATA QUALITY:

   Check after every 10-20 participants:

   A. Completeness:
   - Missing data rate: [Calculate % missing per variable]
   - Target: <5% missing for key variables
   - Action if exceeded: Review instructions, follow up with participants

   B. Range/validity:
   - Check for out-of-range values (e.g., age = 200, Likert scale = 8 when max is 5)
   - Action: Investigate and correct or exclude

   C. Consistency:
   - Check for contradictory responses
   - Check for straight-lining (all same response)
   - Action: Flag suspicious cases for review

   D. Reliability (if multi-item scales):
   - Calculate Cronbach's alpha early (after n=30)
   - Target: α ≥ 0.70
   - Action if low: Review items, consider removing problematic items

2. QUALITATIVE DATA QUALITY:

   Check after every 3-5 interviews:

   A. Audio quality:
   - Can you clearly hear both interviewer and participant?
   - Action if poor: Adjust recording setup, get closer mic

   B. Depth of responses:
   - Are participants giving detailed answers or one-word responses?
   - Action if shallow: Adjust interview approach, use more probes

   C. Data saturation:
   - Are you hearing new information or same themes repeating?
   - Action if saturated early: May need fewer participants than planned
   - Action if not saturating: May need more participants

   D. Interviewer consistency:
   - If multiple interviewers, are they using same protocol?
   - Action: Compare sessions, provide feedback

3. COMPUTATIONAL DATA QUALITY:

   Check before and after each experiment run:

   A. Data integrity:
   - Check for corrupted files
   - Verify correct number of samples
   - Action: Re-run if issues detected

   B. Distribution checks:
   - Plot distributions of key variables
   - Check for anomalies (unexpected spikes, outliers)
   - Action: Investigate cause

   C. Reproducibility:
   - Re-run with same seed, verify same results
   - Action if not reproducible: Debug code, fix sources of randomness

   D. Resource usage:
   - Monitor GPU/CPU usage, memory, disk space
   - Action: Optimize if approaching limits

4. WHEN TO PAUSE AND REASSESS:

   STOP data collection if:
   - Missing data rate >20%
   - Internal consistency (Cronbach's α) <0.60
   - Participants consistently confused by instruments
   - Audio quality consistently poor
   - IRB concerns arise
   - Safety/ethical issues emerge

   Consult advisor before continuing.

5. MID-COLLECTION CHECK-IN:

   After collecting ~30% of data:
   - [ ] Run preliminary analyses
   - [ ] Check if patterns emerging
   - [ ] Verify instruments working as intended
   - [ ] Assess if on track to answer RQs
   - [ ] Calculate estimated completion date
   - [ ] Update advisor

Generate:
1. Quality monitoring checklist
2. Red flags that require immediate action
3. Mid-collection analysis plan
```

**EXPECTED OUTPUT:** Quality monitoring protocol

**SAVE AS:** `/04_Data_Analysis/quality_monitoring_protocol.md`

---

### Prompt 4.3: Clean and Organize Data

**USER INPUT REQUIRED:**
- Raw data files
- Data dictionary/codebook
- Software preference

**PROMPT:**
```
I've completed data collection.

Raw data: [Describe: format, size, number of files]

Software: [R, Python, SPSS, Excel, NVivo, etc.]

Help me clean and organize my data systematically:

1. DATA CLEANING WORKFLOW:

   STEP 1: Import and Inspect
   - Import raw data
   - Check dimensions (N rows, M columns expected?)
   - View first/last rows
   - Check variable types (numeric, string, date, etc.)

   Code example (Python/pandas):
   ```python
   import pandas as pd
   df = pd.read_csv('raw_data.csv')
   print(df.shape)  # Check dimensions
   print(df.head())  # View first 5 rows
   print(df.info())  # Check data types
   print(df.describe())  # Summary statistics
   ```

   STEP 2: Identify Issues
   - Missing values (how many? which variables?)
   - Duplicates (check participant IDs)
   - Out-of-range values
   - Impossible values
   - Inconsistent formatting (e.g., dates as "1/5/24" vs "2024-01-05")

   Code example:
   ```python
   # Check missing values
   print(df.isnull().sum())

   # Check duplicates
   print(df.duplicated(subset=['ParticipantID']).sum())

   # Check value ranges
   print(df['Age'].min(), df['Age'].max())  # Should be reasonable?
   ```

   STEP 3: Handle Missing Data

   Strategies:
   A. Listwise deletion (remove entire case if any missing)
      - Use when: <5% missing, missing completely at random
      - Code: `df_complete = df.dropna()`

   B. Pairwise deletion (use available data for each analysis)
      - Use when: Missing data scattered across variables
      - Most stats software does this by default

   C. Imputation (fill in missing values)
      - Mean imputation: `df['Variable'].fillna(df['Variable'].mean())`
      - Regression imputation
      - Multiple imputation (more advanced)
      - Use when: >5% missing, missing at random

   Document your choice and justify in Chapter 4.

   STEP 4: Fix Errors
   - Correct out-of-range values (if you can verify correct value)
   - Standardize formatting
   - Recode as needed

   Code example:
   ```python
   # Fix out-of-range (if typo identified)
   df.loc[df['Age'] == 200, 'Age'] = 20  # If clearly a typo

   # Or exclude if cannot verify
   df = df[df['Age'] <= 120]  # Reasonable upper bound

   # Standardize text
   df['Gender'] = df['Gender'].str.lower()
   df['Gender'] = df['Gender'].replace({'m': 'male', 'f': 'female'})
   ```

   STEP 5: Create Derived Variables
   - Calculate scale scores (sum or mean of items)
   - Reverse-code items as needed
   - Create categorical variables from continuous (if needed)

   Code example:
   ```python
   # Reverse code items (if 5-point scale)
   df['Item3_R'] = 6 - df['Item3']

   # Calculate scale score (mean of items 1-5)
   df['SatisfactionScore'] = df[['Item1', 'Item2', 'Item3_R', 'Item4', 'Item5']].mean(axis=1)
   ```

2. DATA ORGANIZATION:

   Create clean folder structure:
   ```
   /04_Data_Analysis/
     /raw_data/             (NEVER MODIFY - keep originals)
       - survey_raw.csv
       - interview_P001.mp3
       - ...
     /cleaned_data/         (Output of cleaning process)
       - survey_cleaned.csv
       - data_dictionary.xlsx
     /transcripts/          (If qualitative)
       - P001_transcript.docx
       - ...
     /analysis_code/        (Scripts for cleaning and analysis)
       - 01_data_cleaning.py
       - 02_descriptive_stats.py
       - 03_inferential_stats.py
     /analysis_outputs/     (Results)
       - descriptive_stats.txt
       - regression_output.txt
       - themes_codebook.xlsx
     /figures_tables/       (Visualizations)
       - Figure1_demographics.png
       - Table1_descriptive_stats.xlsx
   ```

3. DOCUMENTATION:

   Create data cleaning log:
   ```
   DATA CLEANING LOG
   Date: [YYYY-MM-DD]
   Analyst: [Your name]
   Software: [R version X.X.X / Python 3.X / SPSS 28]

   ORIGINAL DATA:
   - File: raw_data.csv
   - N = 150 participants
   - Variables: 45

   CLEANING STEPS:
   1. Removed 3 duplicates (IDs: P012, P047, P089)
      - Kept first occurrence, deleted subsequent
   2. Handled missing data:
      - Age: 2 missing (1.3%) - mean imputation
      - Satisfaction items: 5 missing (3.3%) - listwise deletion for scale score
   3. Fixed errors:
      - P034 Age = 200 changed to 20 (confirmed with participant)
      - P067 Gender = "N/A" changed to "Other"
   4. Reverse-coded items 3, 7, 11 (see codebook)
   5. Created scale scores:
      - Satisfaction = mean(Item1-Item5)
      - Engagement = mean(Item6-Item10)

   FINAL CLEAN DATA:
   - File: survey_cleaned.csv
   - N = 145 participants (3 duplicates, 2 with >20% missing removed)
   - Variables: 48 (added 3 scale scores)

   QUALITY CHECKS:
   - Missing data: <2% on all variables
   - Cronbach's alpha: Satisfaction = 0.85, Engagement = 0.81
   - Value ranges: All within expected bounds
   ```

4. REPRODUCIBLE WORKFLOW:

   Create cleaning script that can be re-run:
   - Start with raw data
   - Apply all cleaning steps in code
   - Output clean data
   - Document every change

   Benefits:
   - Transparent
   - Reproducible
   - Can redo if errors found
   - Meets open science standards

Generate:
1. Data cleaning script (in your chosen software)
2. Data cleaning log template
3. Final clean dataset with data dictionary
```

**EXPECTED OUTPUT:** Clean data + documentation

**SAVE AS:** `/04_Data_Analysis/cleaned_data/` and `/04_Data_Analysis/data_cleaning_log.md`

---

### Prompt 4.4: Execute Quantitative Analysis

**USER INPUT REQUIRED:**
- Research questions
- Clean data
- Analysis plan from Stage 3
- Software (SPSS, R, Python, etc.)

**PROMPT:**
```
Research Questions: [PASTE]

Clean data: [File name and location]

Analysis Plan: [From Stage 3, Prompt 3.5]

Software: [SPSS / R / Python]

Guide me through systematic quantitative analysis:

1. DESCRIPTIVE STATISTICS:

   Calculate for all variables:
   - Continuous: mean, median, SD, min, max, skew, kurtosis
   - Categorical: frequencies, percentages

   Python example:
   ```python
   import pandas as pd
   df = pd.read_csv('cleaned_data.csv')

   # Continuous variables
   print(df[['Age', 'Satisfaction', 'Engagement']].describe())

   # Categorical variables
   print(df['Gender'].value_counts())
   print(df['Gender'].value_counts(normalize=True))  # Percentages
   ```

   Create Table 6.1: Descriptive Statistics and Participant Demographics

2. ASSUMPTION CHECKING:

   Before inferential stats, check assumptions:

   A. Normality (for t-tests, ANOVA, regression):
   - Visual: Histogram, Q-Q plot
   - Statistical: Shapiro-Wilk test (if N < 50), Kolmogorov-Smirnov (if N > 50)

   Python example:
   ```python
   from scipy import stats
   import matplotlib.pyplot as plt

   # Visual check
   df['Satisfaction'].hist()
   plt.show()

   # Statistical test
   stat, p = stats.shapiro(df['Satisfaction'])
   print(f'Shapiro-Wilk: statistic={stat:.4f}, p={p:.4f}')
   # If p > 0.05, assume normality
   ```

   B. Homogeneity of variance (for t-tests, ANOVA):
   - Levene's test

   Python example:
   ```python
   # Compare variance across groups
   group1 = df[df['Condition']=='A']['Satisfaction']
   group2 = df[df['Condition']=='B']['Satisfaction']
   stat, p = stats.levene(group1, group2)
   print(f'Levene test: statistic={stat:.4f}, p={p:.4f}')
   # If p > 0.05, variances are equal
   ```

   C. Linearity (for regression):
   - Scatterplot

   D. Independence of observations:
   - Check study design (should be independent if properly randomized/sampled)

   If assumptions violated:
   - Use non-parametric alternatives
   - Transform data (log, sqrt)
   - Use robust statistics

3. INFERENTIAL STATISTICS (For Each RQ):

   RQ1: [PASTE RQ1]

   Analysis plan: [e.g., "Independent samples t-test comparing Group A vs. Group B on Satisfaction"]

   STEP 1: State hypotheses
   - H0: μ₁ = μ₂ (no difference between groups)
   - H1: μ₁ ≠ μ₂ (groups differ)

   STEP 2: Check assumptions
   - Normality: [Check as above]
   - Homogeneity: [Check as above]

   STEP 3: Run test

   Python example (independent t-test):
   ```python
   from scipy import stats

   groupA = df[df['Condition']=='A']['Satisfaction']
   groupB = df[df['Condition']=='B']['Satisfaction']

   # Independent t-test
   t_stat, p_value = stats.ttest_ind(groupA, groupB)

   print(f't-statistic: {t_stat:.3f}')
   print(f'p-value: {p_value:.4f}')

   # Calculate means and SDs
   print(f'Group A: M={groupA.mean():.2f}, SD={groupA.std():.2f}')
   print(f'Group B: M={groupB.mean():.2f}, SD={groupB.std():.2f}')
   ```

   STEP 4: Calculate effect size

   For t-test: Cohen's d
   ```python
   import numpy as np

   pooled_std = np.sqrt((groupA.std()**2 + groupB.std()**2) / 2)
   cohens_d = (groupA.mean() - groupB.mean()) / pooled_std
   print(f"Cohen's d: {cohens_d:.3f}")

   # Interpretation: Small (0.2), Medium (0.5), Large (0.8)
   ```

   STEP 5: Report results

   Template:
   "An independent samples t-test revealed that Group A (M = X.XX, SD = Y.YY) scored significantly [higher/lower] on Satisfaction than Group B (M = X.XX, SD = Y.YY), t(df) = X.XX, p = .XXX, Cohen's d = X.XX."

   Repeat for RQ2, RQ3, etc. with appropriate tests:
   - Two groups: t-test
   - Three+ groups: ANOVA (then post-hoc tests)
   - Relationship between two continuous: Correlation
   - Predicting outcome from predictors: Regression
   - Categorical outcome: Chi-square or logistic regression

4. ADDITIONAL ANALYSES:

   A. Correlation matrix (if examining relationships):
   ```python
   corr_matrix = df[['Var1', 'Var2', 'Var3', 'Var4']].corr()
   print(corr_matrix)
   ```

   B. Regression (if predicting outcome):
   ```python
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import r2_score
   import statsmodels.api as sm

   X = df[['Predictor1', 'Predictor2']]
   X = sm.add_constant(X)  # Add intercept
   y = df['Outcome']

   model = sm.OLS(y, X).fit()
   print(model.summary())

   # Interpret: R², F-statistic, p-values, coefficients
   ```

   C. Repeated measures (if within-subjects design):
   - Use paired t-test or repeated measures ANOVA

5. HANDLING MULTIPLE COMPARISONS:

   If running many tests, adjust alpha:
   - Bonferroni correction: α_adjusted = 0.05 / number_of_tests
   - False Discovery Rate (FDR) control

6. CREATE OUTPUTS:

   Generate:
   - Table of descriptive statistics
   - Table of inferential statistics (test results)
   - Correlation matrix
   - Regression table

Generate complete analysis script and interpret all results.
```

**EXPECTED OUTPUT:** Analysis script + results + interpretation

**SAVE AS:** `/04_Data_Analysis/analysis_code/quantitative_analysis.py` and `/04_Data_Analysis/analysis_outputs/`

---

### Prompt 4.5: Execute Qualitative Analysis

**USER INPUT REQUIRED:**
- Research questions
- Transcripts or text data
- Analysis approach (thematic, content, grounded theory, etc.)
- Software (NVivo, MAXQDA, Atlas.ti, manual)

**PROMPT:**
```
Research Questions: [PASTE]

Data: [Number of interviews/focus groups/documents, total pages]

Analysis Approach: [Thematic analysis / Grounded theory / Phenomenological / Content analysis]

Software: [NVivo / MAXQDA / Atlas.ti / Manual (Word + Excel)]

Guide me through systematic qualitative analysis:

1. PREPARE DATA:

   - Transcribe all recordings (if not already done)
     * Verbatim transcription (every word, pause, laughter)
     * Intelligent transcription (clean up grammar, remove filler words)
     * Recommendation: Start with verbatim, can clean later

   - Anonymize transcripts
     * Remove names, locations, identifying details
     * Use pseudonyms or codes

   - Format consistently
     * Speaker labels: "Interviewer:", "Participant:"
     * Paragraph breaks for new topics
     * Timestamps if needed

2. FAMILIARIZE YOURSELF WITH DATA:

   Phase 1: Initial reading
   - Read all transcripts without coding
   - Immerse yourself in the data
   - Write memos: initial thoughts, patterns, questions

   Example memo:
   ```
   Memo after reading P001-P005:
   Emerging pattern - all participants mentioned feeling "overwhelmed"
   by technology. They describe similar frustrations with complexity.
   Possible theme: Technology overload?
   Also noting that younger participants adapt faster. Age a factor?
   ```

3. INITIAL CODING (Open Coding):

   Phase 2: Line-by-line or paragraph-by-paragraph coding
   - Apply descriptive codes to segments
   - Code inductively (from data, not forcing pre-conceived codes)
   - Use participants' own words when possible (in vivo codes)

   Example:
   ```
   Transcript excerpt (P001):
   "I just felt completely lost when I tried to use the new system.
   Everything was so complicated, I didn't know where to start."

   Codes applied:
   - Feeling lost
   - Complexity
   - Difficulty starting
   - Negative initial experience
   ```

   Coding tips:
   - Be generous with codes at this stage (can consolidate later)
   - Code the same segment with multiple codes if relevant
   - Create code definitions as you go

   If using software:
   - NVivo: Create "nodes" for each code
   - MAXQDA: Create "codes"
   - Manual: Use Excel with columns: Participant ID, Quote, Code(s)

4. FOCUSED CODING (Axial Coding):

   Phase 3: Group related codes into categories
   - Look for patterns across codes
   - Merge similar codes
   - Create hierarchies (parent codes, subcodes)

   Example:
   ```
   Initial codes:                Grouped into category:
   - Feeling lost                → Emotional Responses
   - Frustration                   - Feeling lost
   - Confusion                     - Frustration
   - Anxiety                       - Confusion
   - Excitement                    - Anxiety
                                   - Excitement (different cluster?)

   - Complexity                  → Usability Issues
   - Difficult interface           - Complexity
   - Too many steps                - Difficult interface
   - Confusing labels              - Too many steps
                                   - Confusing labels
   ```

   Create codebook:
   | Code | Definition | When to apply | Example |
   |------|------------|---------------|---------|
   | Emotional Responses | Expressions of feelings | When P describes emotions | "I felt frustrated" |
   | Complexity | References to system being complicated | When P mentions difficulty due to complexity | "Too many options" |

5. THEME DEVELOPMENT (Selective Coding):

   Phase 4: Identify overarching themes
   - What are the main patterns?
   - What connects the categories?
   - What answers your research questions?

   Example themes:
   ```
   Theme 1: Technology Overwhelm
   - Definition: Participants experience cognitive and emotional overload
     when faced with complex technology
   - Sub-themes:
     * Initial intimidation
     * Difficulty navigating
     * Desire for simplicity
   - Supporting quotes: [Collect 3-5 representative quotes]

   Theme 2: Adaptation Strategies
   - Definition: Ways participants cope with technology challenges
   - Sub-themes:
     * Trial and error
     * Seeking help from others
     * Avoiding advanced features
   - Supporting quotes: [Collect quotes]

   Theme 3: [etc.]
   ```

6. THEORY/NARRATIVE BUILDING:

   Phase 5: Connect themes into coherent narrative
   - How do themes relate to each other?
   - What story do they tell?
   - How do they answer your research questions?

   Create visual map:
   ```
   Technology Overwhelm → Negative emotions → Avoidance → Underutilization
                                                ↓
                                           Adaptation Strategies
                                                ↓
                                      Gradual Comfort → Effective Use
   ```

7. ENSURE RIGOR:

   A. Credibility (internal validity):
   - Member checking: Share findings with 2-3 participants, ask if rings true
   - Triangulation: Use multiple data sources (interviews + observations)
   - Peer debriefing: Discuss with colleague, get their take

   B. Dependability (reliability):
   - Inter-coder reliability: Have second coder code 20% of data
     * Calculate Cohen's kappa (target ≥ 0.70)
     * Discuss disagreements, refine codebook
   - Audit trail: Document all coding decisions

   C. Confirmability (objectivity):
   - Reflexivity: Acknowledge your biases
     * "As someone who works in tech, I may have underestimated the difficulty participants faced"
   - Negative case analysis: Look for data that doesn't fit themes
     * "P007 reported feeling excited, not overwhelmed"

   D. Transferability (external validity):
   - Thick description: Provide rich context so readers can judge applicability

8. WRITE UP FINDINGS:

   Structure for qualitative results (Chapter 6):

   ```
   **6.X Qualitative Findings: [RQ]**

   We conducted thematic analysis of [N] interviews ([total pages/hours]).
   Analysis revealed [N] major themes: [list themes].

   **Theme 1: [Name]**
   [Description of theme in 1-2 paragraphs]

   Participants described [key aspect]. For example, P003 stated:
   > "Quote illustrating theme"

   This was echoed by P007:
   > "Another quote"

   [Frequency: X out of N participants (Y%) mentioned this theme]

   **Theme 2: [Name]**
   [Repeat structure]

   **Relationships Between Themes**
   [How themes connect, overall narrative]

   **Answer to RQ:**
   [Direct answer based on themes]
   ```

Generate:
1. Coding manual
2. List of themes with definitions and quotes
3. Thematic map (visual)
4. Findings write-up
```

**EXPECTED OUTPUT:** Codebook + themes + findings narrative

**SAVE AS:** `/04_Data_Analysis/qualitative_analysis/codebook.xlsx` and `/04_Data_Analysis/qualitative_analysis/themes.md`

---

### Prompt 4.6: Integrate Mixed Methods (If Applicable)

**USER INPUT REQUIRED:**
- Quantitative results
- Qualitative results
- Mixed methods design type

**PROMPT:**
```
I have both quantitative and qualitative results.

Mixed methods design: [Convergent / Explanatory Sequential / Exploratory Sequential]

Help me integrate findings:

1. CONVERGENT DESIGN (Collected simultaneously):

   Goal: Compare and synthesize both data types

   Integration strategies:
   A. Side-by-side comparison
   - Present quant results, then qual results that corroborate or contradict
   - Example: "Quantitatively, satisfaction was high (M=4.2/5). Qualitatively,
     participants described feeling 'very pleased' and 'happy with the outcome.'"

   B. Joint display table
   - Create table showing both types of data together

   | Quantitative Finding | Qualitative Finding | Integration |
   |----------------------|---------------------|-------------|
   | High satisfaction (M=4.2) | Theme: Positive emotions | Convergence - both show satisfaction |
   | Low engagement (M=2.1) | Theme: Avoidance behaviors | Convergence - both show disengagement |
   | No gender difference (p=.45) | Theme: Gender-specific experiences | Divergence - qual reveals differences |

   C. Transformation
   - "Quantitize" qual data: Count theme frequencies
   - "Qualitize" quant data: Interpret numbers narratively

2. EXPLANATORY SEQUENTIAL (Quant → Qual):

   Goal: Use qual to explain quant results

   Structure:
   ```
   **Quantitative Phase**
   Survey results showed significant difference (p<.001) between groups,
   but unexpected pattern: Group A scored lower than Group B.

   **Qualitative Phase**
   To understand why, we interviewed 10 participants from each group.
   Interviews revealed that Group A interpreted the questions differently,
   explaining the unexpected result.

   **Integration**
   Qualitative findings clarify that quantitative difference was due to
   interpretation issues, not actual difference in construct.
   ```

3. EXPLORATORY SEQUENTIAL (Qual → Quant):

   Goal: Use quant to test/generalize qual findings

   Structure:
   ```
   **Qualitative Phase**
   Interviews revealed 3 main coping strategies: seeking help, trial-and-error,
   and avoidance.

   **Quantitative Phase**
   We developed a survey based on these strategies and administered to N=200.
   Results confirmed that seeking help was most common (65%), followed by
   trial-and-error (25%), and avoidance (10%).

   **Integration**
   Quantitative phase confirmed qualitative findings and provided prevalence
   estimates, showing seeking help is dominant strategy.
   ```

4. WRITING INTEGRATED RESULTS:

   Chapter 6 structure:
   ```
   6.1 Overview
   6.2 Quantitative Results (RQ1-RQ3)
   6.3 Qualitative Results (RQ1-RQ3)
   6.4 Integrated Findings (Synthesis)
     6.4.1 Areas of Convergence
     6.4.2 Areas of Divergence
     6.4.3 Complementarity (each adds different insight)
   6.5 Summary
   ```

Generate integrated findings report showing how both data types inform each other.
```

**EXPECTED OUTPUT:** Integrated findings document

**SAVE AS:** `/04_Data_Analysis/mixed_methods_integration.md`

---

### Prompt 4.7: Interpret and Discuss Results

**USER INPUT REQUIRED:**
- All analysis results (quant, qual, or mixed)
- Research questions
- Hypotheses (if any)

**PROMPT:**
```
I've completed all analyses.

Results summary: [Brief overview of key findings]

Help me interpret results thoughtfully:

1. FOR EACH RESEARCH QUESTION:

   RQ1: [PASTE]

   **Direct Answer:**
   - Answer the RQ directly and clearly
   - Use specific numbers from results
   - Example: "RQ1 asked whether Method A would be faster than Method B.
     Results show Method A was significantly faster (M=45ms vs. 78ms, p<.001,
     d=1.2), supporting our hypothesis."

   **Interpretation:**
   - What do these results mean?
   - Why might we have observed this pattern?
   - How do results compare to prior work?

   Example:
   "This finding aligns with prior research (Author, Year) suggesting that
   Method A's hierarchical approach reduces computational complexity. However,
   our effect size is larger than previously reported, possibly due to our
   use of GPU acceleration."

   **Alternative Explanations:**
   - Could results be explained differently?
   - What confounds might exist?
   - Be honest about limitations

   Example:
   "While we attribute the speed improvement to the hierarchical approach,
   it's possible that our larger batch size also contributed. Further research
   isolating these factors is needed."

2. UNEXPECTED FINDINGS:

   - Did anything surprise you?
   - Results contrary to hypotheses?
   - Patterns you didn't anticipate?

   Example:
   "Contrary to our hypothesis, we found no relationship between user
   experience and satisfaction (r=.05, p=.62). This was unexpected given
   prior literature (Author, Year). Possible explanations include:
   1) Our sample was more homogeneous, 2) Satisfaction may depend on other
   factors in our context, or 3) Measurement issues with our satisfaction
   scale (see limitations)."

3. PATTERNS ACROSS FINDINGS:

   - What overarching story emerges?
   - How do findings connect?
   - What's the big picture?

   Example:
   "Across all three research questions, we see a consistent pattern:
   users value simplicity over advanced features. RQ1 showed preference
   for basic interface, RQ2 found advanced features rarely used, and RQ3
   revealed frustration with complexity. Together, these suggest that
   'less is more' in this domain."

4. COMPARISON TO LITERATURE:

   - How do your results compare to prior research?

   Categories:
   A. **Convergence:** Your results agree with prior work
      - "Our findings align with Author (Year) who also found..."

   B. **Divergence:** Your results disagree with prior work
      - "In contrast to Author (Year), we found... This discrepancy may be
        due to differences in [methodology/sample/context]."

   C. **Extension:** Your results add to prior work
      - "Building on Author (Year), we demonstrate that this effect also
        holds in [new context/population]."

   D. **Novel:** Your results are new
      - "To our knowledge, this is the first study to examine..."

5. PRACTICAL IMPLICATIONS:

   - So what? Why should anyone care?
   - What are practical applications?
   - Who benefits and how?

   Example:
   "These findings have implications for practitioners designing [systems].
   Our results suggest that prioritizing simplicity and reducing feature
   clutter will improve user satisfaction. Specifically, designers should:
   1) Limit options to 3-5 key features, 2) Hide advanced features,
   3) Provide progressive disclosure."

6. THEORETICAL IMPLICATIONS:

   - What do results say about theory?
   - Support existing theory?
   - Challenge existing theory?
   - Suggest new theoretical insights?

   Example:
   "Our results support Cognitive Load Theory (Sweller, 1988), demonstrating
   that reducing extraneous cognitive load (through simplicity) improves
   performance. However, we found that even low load can be problematic if
   users lack mental models, suggesting that theory should incorporate
   prior knowledge as a moderator."

7. LIMITATIONS AFFECTING INTERPRETATION:

   Be honest about what limits your conclusions:
   - Sample limitations (size, representativeness)
   - Measurement limitations (reliability, validity)
   - Design limitations (no random assignment, confounds)
   - Generalizability limitations

   Example:
   "Results should be interpreted with several limitations in mind. First,
   our sample was limited to university students, limiting generalizability
   to other populations. Second, we used self-report measures, which may be
   subject to social desirability bias. Third, our cross-sectional design
   prevents causal conclusions."

8. UNANSWERED QUESTIONS:

   - What remains unknown?
   - What should future research examine?

   Example:
   "While our study demonstrates that simplicity improves satisfaction,
   we did not examine the optimal level of simplicity. Future research
   should identify the 'sweet spot' between too simple (boring) and too
   complex (overwhelming)."

Generate interpretation memo addressing all points above for each RQ.
```

**EXPECTED OUTPUT:** Results interpretation document

**SAVE AS:** `/04_Data_Analysis/results_interpretation.md`

**NOTE:** This document will feed directly into Chapter 7: Discussion

---

### Prompt 4.8: Create Results Visualizations

**USER INPUT REQUIRED:**
- Analysis results
- Target audience (dissertation committee, journal, conference)
- Software preference (Python/matplotlib, R/ggplot2, Excel, Prism)

**PROMPT:**
```
Analysis results: [Summary]

Target: [Dissertation / Journal Publication / Conference Presentation]

Software: [Python/R/Excel/GraphPad Prism/etc.]

Help me create publication-quality visualizations:

1. DETERMINE WHICH FIGURES TO CREATE:

   Essential figures:
   - Participant demographics (bar chart or table)
   - Main results for each RQ (bar chart, scatter, box plot)
   - Key comparisons (your method vs. baselines)
   - Effect sizes with confidence intervals

   Optional but valuable:
   - Correlation matrix (heatmap)
   - Distribution of key variables (histograms, violin plots)
   - Longitudinal trends (line plots if applicable)
   - Qualitative themes (word cloud, thematic map)

2. FIGURE DESIGN PRINCIPLES:

   A. Clarity:
   - One message per figure
   - Clear title describing what figure shows
   - Labeled axes with units
   - Legend if multiple series

   B. Accessibility:
   - Colorblind-friendly palettes
     * Use: Blue, orange, green (avoid red-green combinations)
     * Tools: ColorBrewer, viridis
   - High contrast
   - Text large enough to read (min 10pt font)

   C. Honesty:
   - Start axes at zero (unless good reason not to)
   - Show error bars (SD, SEM, or 95% CI - specify which)
   - Don't cherry-pick data
   - Show individual data points when possible

3. SPECIFIC FIGURE TYPES:

   A. BAR CHART (For comparing groups):

   Python example:
   ```python
   import matplotlib.pyplot as plt
   import numpy as np

   groups = ['Method A', 'Method B', 'Method C']
   means = [45, 78, 62]
   sds = [8, 12, 10]

   fig, ax = plt.subplots(figsize=(8, 6))
   x_pos = np.arange(len(groups))
   ax.bar(x_pos, means, yerr=sds, capsize=5, color=['#2E86AB', '#A23B72', '#F18F01'])
   ax.set_xticks(x_pos)
   ax.set_xticklabels(groups)
   ax.set_ylabel('Latency (ms)')
   ax.set_xlabel('Method')
   ax.set_title('Comparison of Computational Latency Across Methods')
   plt.tight_layout()
   plt.savefig('Figure1_latency_comparison.png', dpi=300)
   plt.show()
   ```

   B. BOX PLOT (For showing distribution):

   Python example:
   ```python
   import seaborn as sns

   sns.boxplot(data=df, x='Condition', y='Satisfaction', palette='Set2')
   plt.ylabel('Satisfaction Score (1-5)')
   plt.xlabel('Experimental Condition')
   plt.title('Distribution of Satisfaction Scores by Condition')
   plt.tight_layout()
   plt.savefig('Figure2_satisfaction_boxplot.png', dpi=300)
   plt.show()
   ```

   C. SCATTER PLOT (For correlations):

   Python example:
   ```python
   from scipy import stats

   plt.scatter(df['Experience'], df['Performance'], alpha=0.6, color='#2E86AB')

   # Add regression line
   z = np.polyfit(df['Experience'], df['Performance'], 1)
   p = np.poly1d(z)
   plt.plot(df['Experience'], p(df['Experience']), 'r--', linewidth=2)

   # Add correlation
   r, p_val = stats.pearsonr(df['Experience'], df['Performance'])
   plt.text(0.05, 0.95, f'r = {r:.2f}, p = {p_val:.3f}',
            transform=plt.gca().transAxes, verticalalignment='top')

   plt.xlabel('Years of Experience')
   plt.ylabel('Performance Score')
   plt.title('Relationship Between Experience and Performance')
   plt.tight_layout()
   plt.savefig('Figure3_correlation.png', dpi=300)
   plt.show()
   ```

   D. HEATMAP (For correlation matrix):

   Python example:
   ```python
   import seaborn as sns

   corr = df[['Var1', 'Var2', 'Var3', 'Var4']].corr()
   sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1,
               square=True, linewidths=0.5)
   plt.title('Correlation Matrix')
   plt.tight_layout()
   plt.savefig('Figure4_correlation_matrix.png', dpi=300)
   plt.show()
   ```

   E. ERROR BAR PLOT (For effect sizes with CIs):

   Python example:
   ```python
   effects = [0.45, 0.78, 0.32]
   ci_lower = [0.32, 0.60, 0.18]
   ci_upper = [0.58, 0.96, 0.46]
   comparisons = ['A vs B', 'A vs C', 'B vs C']

   fig, ax = plt.subplots(figsize=(8, 6))
   y_pos = np.arange(len(comparisons))

   ax.errorbar(effects, y_pos,
                xerr=[[e - ci_lower[i] for i, e in enumerate(effects)],
                      [ci_upper[i] - e for i, e in enumerate(effects)]],
                fmt='o', markersize=8, capsize=5, color='#2E86AB')
   ax.axvline(x=0, color='gray', linestyle='--', linewidth=1)
   ax.set_yticks(y_pos)
   ax.set_yticklabels(comparisons)
   ax.set_xlabel("Cohen's d (Effect Size)")
   ax.set_title('Effect Sizes with 95% Confidence Intervals')
   plt.tight_layout()
   plt.savefig('Figure5_effect_sizes.png', dpi=300)
   plt.show()
   ```

4. TABLES:

   Create formatted tables for:
   - Descriptive statistics
   - Regression results
   - ANOVA tables
   - Comparison tables

   Example (create in Excel or LaTeX):
   ```
   Table 1: Descriptive Statistics and Demographic Characteristics

   | Variable      | n   | M    | SD   | Min | Max | Skew | Kurt |
   |---------------|-----|------|------|-----|-----|------|------|
   | Age           | 145 | 22.3 | 3.1  | 18  | 35  | 0.8  | 0.2  |
   | Satisfaction  | 145 | 4.2  | 0.7  | 2.0 | 5.0  | -0.5 | -0.1 |
   | Engagement    | 145 | 3.8  | 0.9  | 1.5 | 5.0  | -0.2 | -0.4 |

   Note: M = mean, SD = standard deviation, Skew = skewness, Kurt = kurtosis
   ```

5. FIGURE CAPTIONS:

   Write informative captions:

   Template:
   "Figure X. [Descriptive title]. [Explanation of what's shown]. [Key takeaway].
   [Any abbreviations or symbols explained]. Error bars represent [SD/SEM/95%CI]."

   Example:
   "Figure 1. Computational latency comparison across three methods. Bar chart
   shows mean latency (ms) for Method A (hierarchical SHAP), Method B (LIME),
   and Method C (GradCAM) on the LFW dataset. Method A is significantly faster
   than both baselines (p < .001). Error bars represent standard deviation
   over 5 runs with different random seeds."

6. QUALITY CHECKLIST:

   Before finalizing, verify:
   - [ ] High resolution (300 DPI minimum for publication)
   - [ ] Colorblind-friendly colors
   - [ ] All text readable (font size ≥10pt)
   - [ ] Axes labeled with units
   - [ ] Legend present (if needed)
   - [ ] Error bars shown and explained
   - [ ] Caption is informative
   - [ ] Figure referenced in text
   - [ ] Consistent style across all figures
   - [ ] Saved in appropriate format (PNG/PDF for publication)

Generate all figures with code and captions.
```

**EXPECTED OUTPUT:** All figures (PNG, 300 DPI) + code + captions

**SAVE AS:** `/04_Data_Analysis/figures_tables/` with clear file names

---

## ✅ QUALITY CHECKS FOR STAGE 4

Before moving to Stage 5 (Writing), verify:

### Data Collection
- [ ] Data collection complete and documented
- [ ] All sessions logged
- [ ] Data quality acceptable
- [ ] IRB protocols followed (if applicable)
- [ ] Data backed up (3 copies, 2 media, 1 off-site)

### Data Management
- [ ] Raw data secured and never modified
- [ ] Clean data created with documentation
- [ ] Data cleaning log complete
- [ ] File naming consistent
- [ ] Codebook/data dictionary created

### Analysis
- [ ] All analyses from analysis plan completed
- [ ] Assumptions checked and documented
- [ ] Statistical significance tested
- [ ] Effect sizes calculated
- [ ] Results interpreted correctly

### Findings
- [ ] All research questions addressed
- [ ] Results answer RQs
- [ ] Findings are honest (RULE 1)
- [ ] Unexpected results explained
- [ ] Limitations acknowledged

### Visualization
- [ ] All figures and tables created
- [ ] High quality (300 DPI)
- [ ] Clear and accessible
- [ ] Captions informative
- [ ] Consistent style

### Reproducibility
- [ ] Analysis code documented and saved
- [ ] Can reproduce all results from code
- [ ] Random seeds documented
- [ ] Software versions noted

---

## 📁 SAVE YOUR OUTPUTS

```
/Dissertation_Project/
  /04_Data_Analysis/
    /data_management_system/
      - participant_tracker.xlsx
      - data_collection_log_template.md
      - quality_checklist.md
      - backup_log.xlsx
    /raw_data/ (SECURE, ENCRYPTED, BACKED UP)
      - [Original data files - NEVER MODIFY]
    /cleaned_data/
      - data_cleaned.csv
      - data_dictionary.xlsx
      - data_cleaning_log.md
    /analysis_code/
      - 01_data_cleaning.py
      - 02_descriptive_stats.py
      - 03_inferential_stats.py
      - 04_qualitative_coding.xlsx (if manual)
    /analysis_outputs/
      - descriptive_stats.txt
      - inferential_results.txt
      - qualitative_themes.md
    /figures_tables/
      - Figure1_demographics.png (300 DPI)
      - Figure2_main_results.png
      - Table1_descriptive_stats.xlsx
      - Table2_inferential_stats.xlsx
    - results_interpretation.md
    - findings_summary.md
```

---

## 📚 RESOURCES

### Statistical Analysis:
- **Python**: scipy.stats, statsmodels, pingouin
- **R**: tidyverse, psych, lme4
- **SPSS**: Commercial, point-and-click interface
- **G*Power**: Free power analysis tool

### Qualitative Analysis:
- **NVivo**: https://www.qsrinternational.com/nvivo
- **MAXQDA**: https://www.maxqda.com/
- **Atlas.ti**: https://atlasti.com/
- **Dedoose**: https://www.dedoose.com/ (web-based, affordable)

### Visualization:
- **Python**: matplotlib, seaborn, plotly
- **R**: ggplot2 (highly recommended for publication figures)
- **GraphPad Prism**: Biomedical/scientific figures
- **ColorBrewer**: Colorblind-friendly palettes

### Learning Resources:
- **Statistics**: Andy Field's books, Khan Academy
- **Qualitative**: Johnny Saldaña's *Coding Manual*
- **R**: R for Data Science (free online)
- **Python**: Python for Data Analysis (Wes McKinney)

---

## ⏱️ EXPECTED TIMELINE FOR STAGE 4

**Total Time:** Varies greatly by method (8-24 weeks)

| Task | Quantitative | Qualitative | Computational |
|------|--------------|-------------|---------------|
| Data collection | 4-8 weeks | 6-12 weeks | 2-4 weeks |
| Data cleaning | 1-2 weeks | 2-4 weeks (transcription) | 1 week |
| Analysis | 2-4 weeks | 4-8 weeks | 2-4 weeks |
| Interpretation | 1-2 weeks | 2-3 weeks | 1-2 weeks |
| Visualization | 1 week | 1 week | 1-2 weeks |

**Total:** 9-17 weeks (quant), 15-28 weeks (qual), 7-13 weeks (computational)

**Note:** Qualitative takes longer due to transcription and iterative coding.

---

**⚠️ CRITICAL REMINDERS:**

1. **Data Security:** Follow IRB protocols for storing sensitive data
2. **Reproducibility:** Document everything so results can be reproduced
3. **Honesty (RULE 1):** Report what you found, not what you hoped to find
4. **Statistical Power:** If results are non-significant, check if you had adequate power
5. **Advisor Check-ins:** Share preliminary results, don't wait until the end

---

**Feed outputs from Stage 4 into Stage 5: Writing Results and Discussion (Chapters 6-7)**

---

**END OF STAGE 4: DATA COLLECTION & ANALYSIS EXECUTION**
