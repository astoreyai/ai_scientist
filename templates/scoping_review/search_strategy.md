# Search Strategy Template

**Review Title:** [Insert title]
**Search Date:** [YYYY-MM-DD]
**Searched By:** [Name]
**Date Range:** [e.g., 2010-2025]

---

## Search Concept Mapping

| PCC Element | Key Concepts | Search Terms |
|-------------|--------------|--------------|
| **Population** | [List concepts] | [List synonyms, related terms] |
| **Concept** | [List concepts] | [List synonyms, related terms] |
| **Context** | [List concepts] | [List synonyms, related terms] |

**Example:**

| PCC Element | Key Concepts | Search Terms |
|-------------|--------------|--------------|
| **Population** | Chronic diseases | chronic disease*, diabetes, "type 2 diabetes", T2DM, hypertension, "high blood pressure", COPD, "chronic obstructive pulmonary disease", "heart disease", "cardiovascular disease", "chronic kidney disease", CKD |
| **Concept** | Mobile health | "mobile health", mHealth, m-health, "mobile app*", "smartphone app*", "text messag*", SMS, "short message service", wearable*, "activity tracker*", "digital health", telehealth, telemedicine |
| **Context** | LMICs | "low income countr*", "middle income countr*", "low-and-middle income", LMIC*, "developing countr*", "resource limited", [+ list of specific LMIC countries] |

---

## Database 1: PubMed/MEDLINE

**Search Date:** [YYYY-MM-DD]
**Results:** [n] records

### Search String

```
#1 Population (Chronic Diseases)
("chronic disease"[MeSH Terms] OR "chronic disease*"[Title/Abstract] OR 
"diabetes mellitus"[MeSH Terms] OR diabetes[Title/Abstract] OR 
"diabetes mellitus, type 2"[MeSH Terms] OR "type 2 diabetes"[Title/Abstract] OR 
T2DM[Title/Abstract] OR "hypertension"[MeSH Terms] OR hypertension[Title/Abstract] OR 
"high blood pressure"[Title/Abstract] OR "pulmonary disease, chronic obstructive"[MeSH Terms] OR 
COPD[Title/Abstract] OR "chronic obstructive pulmonary disease"[Title/Abstract] OR 
"heart diseases"[MeSH Terms] OR "heart disease*"[Title/Abstract] OR 
"cardiovascular diseases"[MeSH Terms] OR "cardiovascular disease*"[Title/Abstract] OR 
"renal insufficiency, chronic"[MeSH Terms] OR "chronic kidney disease"[Title/Abstract] OR 
CKD[Title/Abstract])

#2 Concept (Mobile Health)
("telemedicine"[MeSH Terms] OR "mobile health"[Title/Abstract] OR mHealth[Title/Abstract] OR 
m-health[Title/Abstract] OR "mobile applications"[MeSH Terms] OR "mobile app*"[Title/Abstract] OR 
"smartphone app*"[Title/Abstract] OR "text messaging"[MeSH Terms] OR "text messag*"[Title/Abstract] OR 
SMS[Title/Abstract] OR "short message service"[Title/Abstract] OR 
"wearable electronic devices"[MeSH Terms] OR wearable*[Title/Abstract] OR 
"activity tracker*"[Title/Abstract] OR "digital health"[Title/Abstract] OR 
telehealth[Title/Abstract] OR telemedicine[Title/Abstract])

#3 Context (LMICs)
("developing countries"[MeSH Terms] OR "low income countr*"[Title/Abstract] OR 
"middle income countr*"[Title/Abstract] OR "low-and-middle income"[Title/Abstract] OR 
LMIC*[Title/Abstract] OR "developing countr*"[Title/Abstract] OR 
"resource limited"[Title/Abstract] OR "resource constrained"[Title/Abstract] OR
Afghanistan[Title/Abstract] OR Bangladesh[Title/Abstract] OR [... list all LMICs])

#4 Combine with AND
#1 AND #2 AND #3

#5 Date Filter
#4 AND ("2010/01/01"[Date - Publication] : "2025/12/31"[Date - Publication])

#6 Language Filter (if applicable)
#5 AND (English[Language] OR Spanish[Language] OR French[Language])
```

**Final Result:** [n] records exported

**Notes:**
- [Any modifications or issues encountered]

---

## Database 2: Embase

**Search Date:** [YYYY-MM-DD]
**Results:** [n] records

### Search String

```
#1 Population (Chronic Diseases)
'chronic disease'/exp OR 'chronic disease*':ab,ti OR 
'diabetes mellitus'/exp OR diabetes:ab,ti OR 
'non insulin dependent diabetes mellitus'/exp OR 'type 2 diabetes':ab,ti OR 
T2DM:ab,ti OR 'hypertension'/exp OR hypertension:ab,ti OR 
'high blood pressure':ab,ti OR 'chronic obstructive lung disease'/exp OR 
COPD:ab,ti OR 'chronic obstructive pulmonary disease':ab,ti OR 
'heart disease'/exp OR 'heart disease*':ab,ti OR 
'cardiovascular disease'/exp OR 'cardiovascular disease*':ab,ti OR 
'chronic kidney failure'/exp OR 'chronic kidney disease':ab,ti OR CKD:ab,ti

#2 Concept (Mobile Health)
'telemedicine'/exp OR 'mobile health':ab,ti OR mHealth:ab,ti OR m-health:ab,ti OR 
'mobile application'/exp OR 'mobile app*':ab,ti OR 'smartphone app*':ab,ti OR 
'text messaging'/exp OR 'text messag*':ab,ti OR SMS:ab,ti OR 
'short message service':ab,ti OR 'wearable device'/exp OR wearable*:ab,ti OR 
'activity tracker*':ab,ti OR 'digital health':ab,ti OR telehealth:ab,ti OR 
telemedicine:ab,ti

#3 Context (LMICs)
'developing country'/exp OR 'low income countr*':ab,ti OR 'middle income countr*':ab,ti OR 
'low-and-middle income':ab,ti OR LMIC*:ab,ti OR 'developing countr*':ab,ti OR 
'resource limited':ab,ti OR 'resource constrained':ab,ti OR 
Afghanistan:ab,ti OR Bangladesh:ab,ti OR [... list all LMICs]

#4 Combine with AND
#1 AND #2 AND #3

#5 Date Filter
#4 AND [2010-2025]/py

#6 Limit to Articles
#5 AND ('article'/it OR 'article in press'/it)
```

**Final Result:** [n] records exported

**Notes:**
- [Any modifications or issues encountered]

---

## Database 3: CINAHL

**Search Date:** [YYYY-MM-DD]
**Results:** [n] records

### Search String

```
S1 Population (Chronic Diseases)
(MH "Chronic Disease+" OR TI "chronic disease*" OR AB "chronic disease*" OR 
MH "Diabetes Mellitus+" OR TI diabetes OR AB diabetes OR 
MH "Diabetes Mellitus, Type 2" OR TI "type 2 diabetes" OR AB "type 2 diabetes" OR 
TI T2DM OR AB T2DM OR MH "Hypertension+" OR TI hypertension OR AB hypertension OR 
TI "high blood pressure" OR AB "high blood pressure" OR 
MH "Pulmonary Disease, Chronic Obstructive+" OR TI COPD OR AB COPD OR 
TI "chronic obstructive pulmonary disease" OR AB "chronic obstructive pulmonary disease" OR 
MH "Heart Diseases+" OR TI "heart disease*" OR AB "heart disease*" OR 
MH "Cardiovascular Diseases+" OR TI "cardiovascular disease*" OR AB "cardiovascular disease*" OR 
MH "Renal Insufficiency, Chronic" OR TI "chronic kidney disease" OR AB "chronic kidney disease" OR 
TI CKD OR AB CKD)

S2 Concept (Mobile Health)
(MH "Telemedicine+" OR TI "mobile health" OR AB "mobile health" OR TI mHealth OR AB mHealth OR 
TI m-health OR AB m-health OR MH "Mobile Applications" OR TI "mobile app*" OR AB "mobile app*" OR 
TI "smartphone app*" OR AB "smartphone app*" OR MH "Text Messaging" OR 
TI "text messag*" OR AB "text messag*" OR TI SMS OR AB SMS OR 
TI "short message service" OR AB "short message service" OR 
MH "Wearable Electronic Devices" OR TI wearable* OR AB wearable* OR 
TI "activity tracker*" OR AB "activity tracker*" OR TI "digital health" OR AB "digital health" OR 
TI telehealth OR AB telehealth OR TI telemedicine OR AB telemedicine)

S3 Context (LMICs)
(MH "Developing Countries+" OR TI "low income countr*" OR AB "low income countr*" OR 
TI "middle income countr*" OR AB "middle income countr*" OR 
TI "low-and-middle income" OR AB "low-and-middle income" OR TI LMIC* OR AB LMIC* OR 
TI "developing countr*" OR AB "developing countr*" OR 
TI "resource limited" OR AB "resource limited" OR 
TI "resource constrained" OR AB "resource constrained" OR 
TI Afghanistan OR AB Afghanistan OR TI Bangladesh OR AB Bangladesh OR [... list all LMICs])

S4 Combine with AND
S1 AND S2 AND S3

S5 Date Filter
S4 AND Published Date: 20100101-20251231
```

**Final Result:** [n] records exported

**Notes:**
- [Any modifications or issues encountered]

---

## Database 4: Web of Science

**Search Date:** [YYYY-MM-DD]
**Results:** [n] records

### Search String

```
#1 Population (Chronic Diseases)
TS=("chronic disease*" OR diabetes OR "type 2 diabetes" OR T2DM OR hypertension OR 
"high blood pressure" OR COPD OR "chronic obstructive pulmonary disease" OR 
"heart disease*" OR "cardiovascular disease*" OR "chronic kidney disease" OR CKD)

#2 Concept (Mobile Health)
TS=("mobile health" OR mHealth OR m-health OR "mobile app*" OR "smartphone app*" OR 
"text messag*" OR SMS OR "short message service" OR wearable* OR "activity tracker*" OR 
"digital health" OR telehealth OR telemedicine)

#3 Context (LMICs)
TS=("low income countr*" OR "middle income countr*" OR "low-and-middle income" OR LMIC* OR 
"developing countr*" OR "resource limited" OR "resource constrained" OR 
Afghanistan OR Bangladesh OR [... list all LMICs])

#4 Combine with AND
#1 AND #2 AND #3

#5 Date Filter
#4 AND PY=(2010-2025)

#6 Document Type Filter
#5 AND DT=(Article OR Review OR Proceedings Paper)
```

**Final Result:** [n] records exported

**Notes:**
- [Any modifications or issues encountered]

---

## Database 5: Scopus

**Search Date:** [YYYY-MM-DD]
**Results:** [n] records

### Search String

```
(TITLE-ABS-KEY("chronic disease*" OR diabetes OR "type 2 diabetes" OR T2DM OR 
hypertension OR "high blood pressure" OR COPD OR "chronic obstructive pulmonary disease" OR 
"heart disease*" OR "cardiovascular disease*" OR "chronic kidney disease" OR CKD)) 
AND 
(TITLE-ABS-KEY("mobile health" OR mHealth OR m-health OR "mobile app*" OR "smartphone app*" OR 
"text messag*" OR SMS OR "short message service" OR wearable* OR "activity tracker*" OR 
"digital health" OR telehealth OR telemedicine)) 
AND 
(TITLE-ABS-KEY("low income countr*" OR "middle income countr*" OR "low-and-middle income" OR 
LMIC* OR "developing countr*" OR "resource limited" OR "resource constrained" OR 
Afghanistan OR Bangladesh OR [... list all LMICs])) 
AND 
PUBYEAR > 2009 AND PUBYEAR < 2026
```

**Final Result:** [n] records exported

**Notes:**
- [Any modifications or issues encountered]

---

## Database 6: PsycINFO

**Search Date:** [YYYY-MM-DD]
**Results:** [n] records

### Search String

```
[Similar structure to above databases, adapted for PsycINFO syntax]
```

**Final Result:** [n] records exported

**Notes:**
- [Any modifications or issues encountered]

---

## Grey Literature Searches

### Google Scholar

**Search Date:** [YYYY-MM-DD]
**Search Terms:** [simplified search string]
**Method:** First 200 results screened
**Results:** [n] relevant records identified

### ProQuest Dissertations & Theses

**Search Date:** [YYYY-MM-DD]
**Search String:** [simplified search string]
**Results:** [n] records

### ClinicalTrials.gov

**Search Date:** [YYYY-MM-DD]
**Search Terms:** [simplified search string]
**Filters:** Completed studies, [date range]
**Results:** [n] records

### Conference Proceedings

**Conferences Searched:**
1. [Conference name] [Years]
2. [Conference name] [Years]
3. [Conference name] [Years]

**Results:** [n] records

---

## Hand-Searching

### Reference List Screening

- Included studies: [n] references screened, [n] potentially relevant identified
- Relevant reviews: [n] reviews screened, [n] potentially relevant identified

### Key Journal Hand-Searching

**Journals:**
1. [Journal name] [Years, Issues]
2. [Journal name] [Years, Issues]

**Results:** [n] additional records

### Forward Citation Searching

- Key studies identified for citation tracking: [list]
- Method: Web of Science Cited Reference Search or Google Scholar
- Results: [n] additional records

---

## Search Results Summary

| Source | Records Retrieved | After Deduplication |
|--------|------------------|---------------------|
| PubMed | [n] | |
| Embase | [n] | |
| CINAHL | [n] | |
| Web of Science | [n] | |
| Scopus | [n] | |
| PsycINFO | [n] | |
| Grey Literature | [n] | |
| Hand-Searching | [n] | |
| **TOTAL** | **[n]** | **[n]** |

**Deduplication Method:** [e.g., Covidence automated + manual review]

---

## Search Quality Assurance

### Peer Review of Electronic Search Strategies (PRESS) Checklist

| Element | Status | Notes |
|---------|--------|-------|
| Boolean and proximity operators used correctly | ✓ / ✗ | |
| Subject headings appropriate and exploded | ✓ / ✗ | |
| Text words cover key synonyms | ✓ / ✗ | |
| Spelling, syntax, and line numbers correct | ✓ / ✗ | |
| Limits and filters appropriate | ✓ / ✗ | |
| Search documented and reproducible | ✓ / ✗ | |

**Reviewed By:** [Name, Credentials]
**Date:** [YYYY-MM-DD]

---

## Search Updates

All search updates will be documented here:

| Update Date | Databases Updated | New Records | Notes |
|-------------|-------------------|-------------|-------|
| [YYYY-MM-DD] | [List] | [n] | [Notes] |

---

**Search Strategy Development:** [Names]
**Librarian/Information Specialist Consultation:** [Name]
**Date Finalized:** [YYYY-MM-DD]

---

*This search strategy is designed to be comprehensive and reproducible, following best practices for systematic and scoping reviews.*
