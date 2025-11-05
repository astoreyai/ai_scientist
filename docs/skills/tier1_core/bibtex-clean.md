# @bibtex-clean - Clean and Validate BibTeX Entries

Clean, validate, and standardize BibTeX bibliography entries for LaTeX dissertations.

## Skill Type
**Category:** Literature Review / Citations
**Tier:** Core (Tier 1)
**Reusability:** Very High - every LaTeX dissertation needs clean BibTeX

## What This Skill Does

1. Validates BibTeX syntax and structure
2. Standardizes field formatting
3. Removes duplicates
4. Fixes common errors (missing fields, bad characters)
5. Ensures LaTeX compilation compatibility
6. Generates clean, consistent bibliography

## Invocation

```
@bibtex-clean [file] [options]
```

## Common BibTeX Problems

### 1. Missing Required Fields
```bibtex
@article{smith2023,
  author = {Smith, John},
  title = {Paper Title}
  % ❌ Missing: journal, year
}
```

### 2. Bad Character Encoding
```bibtex
@article{müller2023,  % ❌ Umlaut not escaped
  author = {Müller, Hans}
}
```

### 3. Inconsistent Field Order
Different papers have fields in different orders, making manual review difficult.

### 4. Duplicate Entries
Same paper cited with different keys (`smith2023`, `smith2023a`, `Smith2023`).

### 5. URL/DOI Formatting
```bibtex
doi = {doi.org/10.1234/example}  % ❌ Wrong format
doi = {10.1234/example}  % ✅ Correct
```

## Input Format

### BibTeX File
```
@bibtex-clean

File: references.bib
Check for: duplicates, missing fields, formatting
```

### Direct Paste
```
@bibtex-clean

@article{smith2023,
  author = {Smith, John and Doe, Jane},
  title = {Explainable AI for Biometrics},
  journal = {IEEE Trans. on AI},
  year = 2023,
  volume = 45,
  pages = {123-145}
}
```

### Multiple Files
```
@bibtex-clean

Merge and clean:
- chapter2_refs.bib
- chapter3_refs.bib
- chapter4_refs.bib

Output: dissertation_references.bib
```

## Output Examples

### Example 1: Missing Fields

**Input:**
```bibtex
@article{smith2023,
  author = {Smith, John},
  title = {XAI Methods},
  year = 2023
}
```

**Output:**

```markdown
## BibTeX Validation Results

### ❌ Errors Found: 1

**Entry:** `smith2023`
**Type:** `@article`
**Problem:** Missing required field `journal`

**Required fields for @article:**
- ✅ author
- ✅ title
- ✅ year
- ❌ journal (MISSING)

**Fix:**
Add the journal name. Check the original paper or use Google Scholar to find it.

---

### Cleaned Entry

```bibtex
@article{smith2023,
  author = {Smith, John},
  title = {{XAI} Methods},
  journal = {[JOURNAL NAME NEEDED]},
  year = {2023},
  note = {Original entry missing journal name}
}
```

**Action required:** Fill in `[JOURNAL NAME NEEDED]` before compiling.
```

### Example 2: Character Encoding Issues

**Input:**
```bibtex
@article{müller2023,
  author = {Müller, Hans and López, María},
  title = {Über explainable AI},
  journal = {Künstliche Intelligenz},
  year = {2023}
}
```

**Output:**

```markdown
## Character Encoding Fixes

### Issues Found: 4 special characters

**Entry:** `müller2023` → **Renamed to:** `muller2023`
(BibTeX keys should use ASCII only)

---

### Character Replacements

| Field | Original | Fixed |
|-------|----------|-------|
| key | `müller2023` | `muller2023` |
| author | `Müller` | `M{\"{u}}ller` |
| author | `López` | `L{\'{o}}pez` |
| title | `Über` | `{\"{U}}ber` |
| journal | `Künstliche` | `K{\"{u}}nstliche` |

---

### Cleaned Entry

```bibtex
@article{muller2023,
  author = {M{\"{u}}ller, Hans and L{\'{o}}pez, Mar{\'{i}}a},
  title = {{{\"{U}}ber Explainable {AI}}},
  journal = {K{\"{u}}nstliche Intelligenz},
  year = {2023}
}
```

**LaTeX output:**
> Müller, Hans and López, María. "Über explainable AI." *Künstliche Intelligenz*, 2023.

**Note:** Double braces protect capitalization in title.
```

### Example 3: Duplicate Detection

**Input:**
```bibtex
@article{smith2023,
  author = {Smith, John},
  title = {XAI for Biometrics},
  journal = {IEEE Trans.},
  year = {2023}
}

@article{Smith2023a,
  author = {Smith, J.},
  title = {XAI for Biometrics},
  journal = {IEEE Transactions on AI},
  year = {2023}
}
```

**Output:**

```markdown
## Duplicate Detection

### ⚠️ Potential Duplicates Found: 1 pair

**Entry 1:** `smith2023`
**Entry 2:** `Smith2023a`

**Similarity:** 95% (likely same paper)

**Comparison:**

| Field | Entry 1 | Entry 2 | Match? |
|-------|---------|---------|--------|
| Author | Smith, John | Smith, J. | ✅ (same person) |
| Title | XAI for Biometrics | XAI for Biometrics | ✅ (exact) |
| Journal | IEEE Trans. | IEEE Transactions on AI | ✅ (abbreviated) |
| Year | 2023 | 2023 | ✅ |
| Pages | (missing) | (missing) | - |

**Recommendation:** Merge into single entry with most complete information.

---

### Merged Entry (Recommended)

```bibtex
@article{smith2023,
  author = {Smith, John},
  title = {{XAI} for Biometrics},
  journal = {IEEE Transactions on Artificial Intelligence},
  year = {2023},
  note = {Merged from duplicate entry Smith2023a}
}
```

**Action:**
1. Delete `Smith2023a` entry
2. Update citations in text from `\cite{Smith2023a}` to `\cite{smith2023}`
3. Run `grep -r "Smith2023a" *.tex` to find all citations
```

### Example 4: Field Standardization

**Input (inconsistent formatting):**
```bibtex
@article{smith2023,
  AUTHOR = {Smith, John},
  Title = {XAI Methods},
  journal={IEEE Trans. AI},
  Year = 2023,
  Volume={45},
  number = {2},
  PAGES = {123--145},
}
```

**Output:**

```markdown
## Standardization Applied

### Issues Fixed:

1. ✅ Field names normalized to lowercase
2. ✅ Consistent spacing added
3. ✅ Braces added to protect capitalization
4. ✅ Trailing comma removed
5. ✅ Fields reordered (author, title, journal, year, volume, number, pages)

---

### Cleaned Entry

```bibtex
@article{smith2023,
  author = {Smith, John},
  title = {{XAI} Methods},
  journal = {IEEE Transactions on Artificial Intelligence},
  year = {2023},
  volume = {45},
  number = {2},
  pages = {123--145}
}
```

**Improvements:**
- Consistent field order (easier to review)
- Protected capitals in title (`{XAI}`)
- Full journal name (not abbreviated)
- Proper en-dash for page range (`--` not `-`)
```

## Validation Rules

### Required Fields by Entry Type

**@article:**
- author, title, journal, year

**@inproceedings (conference):**
- author, title, booktitle, year

**@book:**
- author OR editor, title, publisher, year

**@phdthesis:**
- author, title, school, year

**@techreport:**
- author, title, institution, year

**@misc (for websites, datasets):**
- author OR title, howpublished, year (recommended)

## Common Fixes Applied

### 1. Protected Capitals
```bibtex
title = {XAI Methods}  % ❌ Will lowercase in some styles
title = {{XAI} Methods}  % ✅ Protected
```

### 2. Page Ranges
```bibtex
pages = {123-145}  % ❌ Hyphen (wrong)
pages = {123--145}  % ✅ En-dash (correct)
```

### 3. Month Format
```bibtex
month = {January}  % ❌ Full name
month = jan  % ✅ Three-letter abbreviation (no braces)
```

### 4. DOI Format
```bibtex
doi = {https://doi.org/10.1234/example}  % ❌ Full URL
doi = {10.1234/example}  % ✅ Just the DOI
```

### 5. URL Field
```bibtex
url = {doi.org/10.1234/example}  % ❌ Missing protocol
url = {https://doi.org/10.1234/example}  % ✅ Full URL
```

## Integration with LaTeX

### In Your Dissertation

**main.tex:**
```latex
\documentclass[12pt]{report}
\usepackage{natbib}  % For author-year citations

\begin{document}
...
\bibliographystyle{plainnat}  % or: apalike, ieeetr, etc.
\bibliography{references}  % references.bib file
\end{document}
```

**Compilation:**
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex  # Yes, run twice after bibtex
```

### Citation Commands

**natbib package:**
```latex
\citep{smith2023}  % (Smith, 2023)
\citet{smith2023}  % Smith (2023)
\citep{smith2023,jones2022}  % (Smith, 2023; Jones, 2022)
```

**Standard LaTeX:**
```latex
\cite{smith2023}  % [1]
```

## Time Savings

**Manual cleaning:** 3-4 hours for 150 references
**Using @bibtex-clean:** 15-20 minutes
**Saved:** ~3 hours 🎉

## Best Practices

### 1. Clean Early and Often
Don't wait until the end - clean as you add references.

### 2. Use Consistent Keys
```
Format: firstauthor + year + letter
Examples: smith2023, smith2023a, jones2022
```

### 3. One File per Chapter (Initially)
Easier to manage. Merge at the end.

### 4. Backup Before Cleaning
```bash
cp references.bib references_backup.bib
```

### 5. Use Reference Manager
- Zotero (free, open source)
- Mendeley (free)
- EndNote (paid)

Export to BibTeX, then clean with @bibtex-clean.

## Common Workflow

```
1. Export from reference manager (Zotero, etc.)
2. Use @bibtex-clean to validate
3. Fix errors flagged
4. Compile LaTeX (pdflatex + bibtex)
5. Check bibliography in PDF
6. Repeat if needed
```

## Software Integration

### Command-Line Tools

**BibTool:**
```bash
bibtool -s -i references.bib -o references_clean.bib
```

**bibclean:**
```bash
bibclean references.bib > references_clean.bib
```

**This skill (@bibtex-clean) combines:**
- Automated tool capabilities
- AI-powered duplicate detection
- Context-aware suggestions
- Discipline-specific conventions

## Troubleshooting

### Issue 1: LaTeX Won't Compile
**Error:** `! Undefined control sequence. \url`

**Solution:** Add `\usepackage{url}` or `\usepackage{hyperref}` to preamble.

---

### Issue 2: Bibliography Not Showing
**Problem:** Compiled but no bibliography appears.

**Solution:** Ensure you have `\cite{}` commands in text. LaTeX only includes cited entries.

**Workaround:** Add `\nocite{*}` to include all entries.

---

### Issue 3: "?" Instead of Citations
**Problem:** See `[?]` or `(?)` in PDF.

**Solution:** Run bibtex and pdflatex again:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

---

### Issue 4: Duplicate Bibliography Entries
**Problem:** Same paper appears twice in bibliography.

**Solution:** Use @bibtex-clean to detect and merge duplicates.

## Related Skills

- `/validate-citations` - Check citations in dissertation match .bib file
- `@citation-format` - Format citations in specific styles
- `/run-literature-search` - Find papers to add to bibliography

## Quality Checklist

Before finalizing bibliography:
- [ ] All required fields present
- [ ] No duplicate entries
- [ ] Special characters escaped
- [ ] DOIs in correct format
- [ ] Consistent key naming
- [ ] Protected capitals in titles
- [ ] Page ranges use en-dash (`--`)
- [ ] Compiles without errors
- [ ] All in-text citations have BibTeX entries
- [ ] No "?" citations in PDF

---

**Status:** Documented
**Complexity:** Low-Medium
**Time to use:** 15-20 minutes
**Time saved:** ~3 hours
**Reusability:** Very High (every LaTeX dissertation)
**Critical for:** Bibliography quality, LaTeX compilation
