# @citation-format - Format Academic Citations

Convert references to proper citation formats (APA, IEEE, Chicago, etc.) for academic writing.

## Skill Type
**Category:** Literature Review / Writing
**Tier:** Core (Tier 1)
**Reusability:** High - works for any academic paper

## What This Skill Does

1. Converts raw citation data to formatted citations
2. Supports multiple citation styles
3. Validates citation completeness
4. Generates both in-text and bibliography entries
5. Checks for common formatting errors

## Invocation

```
@citation-format [style] [citations]
```

## Supported Styles

- **APA 7th Edition** (default for social sciences)
- **IEEE** (engineering, computer science)
- **Chicago** (humanities)
- **MLA** (literature)
- **Vancouver** (medicine)
- **Harvard** (business, UK)

## Input Formats

### Raw Text
```
Smith, John and Jane Doe, "Explainable AI for Biometrics",
Journal of AI Research, vol 45 no 2, pages 123-145, 2023
```

### Structured Data
```json
{
  "authors": ["Smith, J.", "Doe, J."],
  "title": "Explainable AI for Biometrics",
  "journal": "Journal of AI Research",
  "volume": 45,
  "issue": 2,
  "pages": "123-145",
  "year": 2023,
  "doi": "10.1234/jair.2023.123"
}
```

### BibTeX
```bibtex
@article{smith2023explainable,
  author = {Smith, John and Doe, Jane},
  title = {Explainable AI for Biometrics},
  journal = {Journal of AI Research},
  volume = {45},
  number = {2},
  pages = {123--145},
  year = {2023},
  doi = {10.1234/jair.2023.123}
}
```

## Output

### APA 7th Edition

**In-text citation:**
```
(Smith & Doe, 2023)
Smith and Doe (2023) demonstrated...
```

**Reference list entry:**
```
Smith, J., & Doe, J. (2023). Explainable AI for biometrics.
    Journal of AI Research, 45(2), 123-145.
    https://doi.org/10.1234/jair.2023.123
```

### IEEE

**In-text citation:**
```
[1]
Smith and Doe [1] demonstrated...
```

**Reference list entry:**
```
[1] J. Smith and J. Doe, "Explainable AI for biometrics,"
    Journal of AI Research, vol. 45, no. 2, pp. 123-145, 2023,
    doi: 10.1234/jair.2023.123.
```

## Usage Examples

### Example 1: Quick Format

**Input:**
```
@citation-format APA

Smith, John; Doe, Jane. 2023. Explainable AI for Biometrics.
Journal of AI Research 45(2):123-145
```

**Output:**
```
Smith, J., & Doe, J. (2023). Explainable AI for biometrics.
    Journal of AI Research, 45(2), 123-145.
```

### Example 2: Multiple Citations

**Input:**
```
@citation-format IEEE

1. Smith et al, XAI Survey, AI Review 2023
2. Jones, Deep Learning Methods, IEEE Trans 2022
3. Brown, Face Recognition, CVPR 2021
```

**Output:**
```
[1] J. Smith et al., "XAI survey," AI Review, 2023.
[2] M. Jones, "Deep learning methods," IEEE Trans., 2022.
[3] A. Brown, "Face recognition," in Proc. CVPR, 2021.
```

### Example 3: Format Conversion

**Input:**
```
@citation-format APA

Convert from IEEE:
[1] J. Smith, "Paper title," Journal, vol. 1, no. 2, pp. 3-4, 2023.
```

**Output:**
```
Smith, J. (2023). Paper title. Journal, 1(2), 3-4.
```

## Common Errors Fixed

### Missing Elements
- ❌ No author → ✅ Uses editor or organization
- ❌ No date → ✅ Adds (n.d.)
- ❌ No page numbers → ✅ Omits properly

### Formatting Issues
- ❌ "and" between authors → ✅ "&" or "and" per style
- ❌ Inconsistent capitalization → ✅ Title case or sentence case
- ❌ Wrong punctuation → ✅ Style-appropriate punctuation

### Author Names
- ❌ "John Smith" → ✅ "Smith, J."
- ❌ "Smith, J. and Doe, J." → ✅ "Smith, J., & Doe, J." (APA)
- ❌ "et al" issues → ✅ Proper et al. rules

## Validation Checks

The skill checks for:
- ✅ All required fields present
- ✅ Author names properly formatted
- ✅ DOI format valid
- ✅ Year is reasonable (1900-2025)
- ✅ Volume/issue/pages format correct
- ✅ URL accessibility

## Advanced Features

### Hanging Indent
```
Smith, J., & Doe, J. (2023). Very long title that wraps to
    multiple lines with proper hanging indent. Journal of
    Research, 45(2), 123-145.
```

### Multiple Authors
```
APA: Up to 20 authors listed, then et al.
IEEE: Up to 6 authors, then et al.
Chicago: All authors listed
```

### Special Cases
- **No author:** Organization or "Anonymous"
- **No date:** (n.d.) for APA
- **Online source:** Include retrieval date if needed
- **Conference paper:** Proper proceedings format

## Integration with LaTeX

### BibTeX Generation
```bibtex
@article{smith2023explainable,
  author = {Smith, John and Doe, Jane},
  title = {Explainable {AI} for Biometrics},
  journal = {Journal of AI Research},
  volume = {45},
  number = {2},
  pages = {123--145},
  year = {2023},
  doi = {10.1234/jair.2023.123}
}
```

### LaTeX Citation Commands
```latex
\cite{smith2023explainable}          % Numbered
\citep{smith2023explainable}         % (Smith & Doe, 2023)
\citet{smith2023explainable}         % Smith and Doe (2023)
```

## Time Savings

**Manual formatting:** 2-3 hours for 50 citations
**Using @citation-format:** 5-10 minutes
**Saved:** ~2.5 hours per paper 🎉

## Best Practices

### 1. Start Early
Format citations as you collect them, not at the end.

### 2. Use Reference Manager
- Zotero
- Mendeley
- EndNote

Then use this skill to verify and clean.

### 3. Check Journal Requirements
Some journals have specific citation styles or modifications.

### 4. Validate DOIs
Always include DOIs when available - helps readers find papers.

### 5. Consistency
Use the same citation style throughout your paper.

## Common Use Cases

### PhD Dissertation
```
@citation-format APA

Format my 150 references for Chapter 2
[paste references]
```

### Journal Paper
```
@citation-format IEEE

Convert these 30 citations from APA to IEEE
[paste citations]
```

### Grant Proposal
```
@citation-format Chicago

Format bibliography for NSF proposal
[paste citations]
```

## Troubleshooting

### Issue: Author name parsing fails
**Solution:** Provide in "Last, First" format explicitly

### Issue: Conference paper not recognized
**Solution:** Specify it's a conference paper in the input

### Issue: Multiple DOIs
**Solution:** Include only the primary DOI

### Issue: Old paper (pre-DOI era)
**Solution:** Omit DOI field, include URL if available

## Related Skills

- `@bibtex-clean` - Clean BibTeX entries
- `@validate-citations` (slash command) - Check all citations
- `@academic-grammar` - Overall writing quality

## Quality Standards

This skill ensures:
- ✅ Style guide compliance
- ✅ Consistency across all citations
- ✅ Complete required information
- ✅ Proper author name formatting
- ✅ Correct punctuation and spacing

## Example Workflow

```
1. Collect papers during literature review
2. Export to BibTeX from reference manager
3. Use @citation-format to verify formatting
4. Generate both in-text and bibliography entries
5. Paste into dissertation
6. Cross-check with journal requirements
```

## Field-Specific Notes

### Computer Science / Engineering
- Use IEEE typically
- Include DOI
- Conference papers common

### Social Sciences
- Use APA
- Focus on author-date style
- Include retrieval dates for online sources

### Humanities
- Use Chicago or MLA
- Full names sometimes used
- Page numbers critical

---

**Status:** Documented
**Complexity:** Medium
**Time to use:** 5-10 minutes
**Time saved:** 2-3 hours
**Reusability:** Very High (any academic paper)
