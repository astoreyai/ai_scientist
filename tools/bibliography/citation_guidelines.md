# Citation Guidelines

**RULE: Every claim must be cited or supported by your own data**

---

## When to Cite

### ALWAYS Cite
✅ Facts that are not common knowledge
✅ Ideas from other researchers
✅ Methods from other papers
✅ Results from other papers
✅ Definitions from specific sources
✅ Quotes (always with page number)
✅ Data/statistics from external sources

### NEVER Cite
❌ Your own original ideas
❌ Your own results
❌ Common knowledge in your field
❌ Your own methodology (describe it instead)

---

## Citation Formats

### In-Text Citations

**Single author:**
- Smith (2023) showed that...
- Previous work demonstrated this [Smith 2023]

**Two authors:**
- Smith and Jones (2023) found that...
- This was demonstrated [Smith and Jones 2023]

**Three or more authors:**
- Smith et al. (2023) proposed...
- Multiple approaches exist [Smith et al. 2023]

**Multiple citations:**
- Several studies [Smith 2021, Jones 2022, Lee 2023] have shown...
- This is well-established [Smith 2021; Jones 2022; Lee 2023]

---

## BibTeX Entry Types

### @article (Journal Paper)
```bibtex
@article{smith2023deep,
  author = {Smith, John and Jones, Mary},
  title = {Deep Learning for Image Classification},
  journal = {Journal of Machine Learning Research},
  year = {2023},
  volume = {24},
  number = {1},
  pages = {123--145},
  doi = {10.1234/jmlr.2023.456}
}
```

### @inproceedings (Conference Paper)
```bibtex
@inproceedings{jones2023transformer,
  author = {Jones, Mary and Lee, David},
  title = {Transformer Models for NLP},
  booktitle = {Proceedings of the 2023 Conference on Neural Information Processing Systems},
  year = {2023},
  pages = {456--468},
  address = {New Orleans, LA},
  publisher = {NeurIPS}
}
```

### @book
```bibtex
@book{goodfellow2016deep,
  author = {Goodfellow, Ian and Bengio, Yoshua and Courville, Aaron},
  title = {Deep Learning},
  publisher = {MIT Press},
  year = {2016},
  address = {Cambridge, MA}
}
```

### @phdthesis
```bibtex
@phdthesis{lee2022neural,
  author = {Lee, David},
  title = {Neural Network Architectures for Computer Vision},
  school = {Stanford University},
  year = {2022}
}
```

### @misc (arXiv, Tech Reports)
```bibtex
@misc{brown2020gpt3,
  author = {Brown, Tom B. and others},
  title = {Language Models are Few-Shot Learners},
  year = {2020},
  eprint = {2005.14165},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL}
}
```

---

## Citation Best Practices

### Quality Over Quantity
- Cite authoritative sources
- Prefer peer-reviewed publications
- Use primary sources (not secondary)
- Cite recent work (last 5 years when possible)
- Include seminal/foundational papers

### Accuracy
- ✅ Read papers before citing them
- ✅ Verify the paper says what you claim
- ✅ Check citation details are correct
- ❌ Don't cite based on abstract alone
- ❌ Don't misrepresent what papers say

### Completeness
- Cite all relevant prior work
- Include work that contradicts yours
- Credit ideas appropriately
- Don't cherry-pick favorable citations

---

## Common Citation Patterns

### Introducing a Topic
> "Deep learning has revolutionized computer vision [LeCun et al. 2015; Krizhevsky et al. 2012]. Recent transformer architectures [Vaswani et al. 2017; Dosovitskiy et al. 2020] have further improved performance."

### Describing Related Work
> "Smith et al. (2023) proposed a method for X, achieving 95% accuracy. However, their approach requires Y, limiting applicability [Smith et al. 2023]."

### Citing Methods
> "We use the Adam optimizer [Kingma and Ba 2015] with a learning rate of 0.001."

### Citing Definitions
> "We define explainability following the framework of Ribeiro et al. (2016), where..."

### Citing Datasets
> "We evaluate our method on the ImageNet dataset [Deng et al. 2009], which contains 1.2M training images."

---

## Managing Citations

### Tools
**Recommended:**
- Zotero (free, open-source, exports BibTeX)
- Mendeley (free, exports BibTeX)
- EndNote (paid, institutional licenses)

**For BibTeX:**
- JabRef (free, BibTeX editor)
- BibDesk (macOS, free)
- Manual editing (any text editor)

### Workflow
1. **Collect:** Save papers as you read them
2. **Organize:** Add to reference manager
3. **Export:** Generate .bib file
4. **Cite:** Reference in LaTeX (\cite{key})
5. **Verify:** Check all citations compile
6. **Proofread:** Check formatting is correct

---

## Bibliography Organization

### Naming Keys
Use consistent key format:
- `lastname2023keyword` (e.g., `smith2023transformer`)
- `lastname2023a`, `lastname2023b` if multiple from same author/year
- All lowercase, no special characters

### Required Fields
**Minimum for @article:**
- author, title, journal, year

**Minimum for @inproceedings:**
- author, title, booktitle, year

**Minimum for @book:**
- author, title, publisher, year

**Recommended additions:**
- doi (for articles)
- pages (for articles and proceedings)
- volume/number (for journals)
- url (for online sources)

---

## Citation Verification Checklist

### Before Submission
- [ ] Every cited paper is in bibliography
- [ ] Every bibliography entry is cited in text
- [ ] All author names are correct
- [ ] All titles are correct
- [ ] All years are correct
- [ ] All venues are correct
- [ ] DOIs are included where available
- [ ] No broken LaTeX references
- [ ] Formatting is consistent

### Common Errors to Check
- ❌ Missing citations (claims without support)
- ❌ Orphaned bibliography entries (in .bib but not cited)
- ❌ Incorrect author names
- ❌ Wrong publication year
- ❌ Inconsistent citation format
- ❌ Missing DOIs
- ❌ "et al." used with fewer than 3 authors

---

## Plagiarism Avoidance

### Paraphrasing
**Original:**
> "Deep learning models have achieved state-of-the-art results on image classification tasks."

**Bad paraphrase (too similar):**
> "Deep learning models have obtained state-of-the-art performance on image classification." [Smith 2023]

**Good paraphrase:**
> "Recent neural network architectures have significantly improved image classification accuracy [Smith 2023]."

### Direct Quotes
Use sparingly and only when:
- The exact wording is important
- Defining a term
- The original is particularly well-stated

**Format:**
> As Smith et al. (2023) state, "exact quote here" (p. 45).

### Self-Plagiarism
- Don't reuse your own published text without attribution
- If using your prior work, cite it properly
- Paraphrase even your own prior writing

---

## Field-Specific Guidelines

### Computer Science
- Cite conference papers (often more current than journals)
- Include arXiv papers (but prefer published versions)
- Cite code/data repositories when used
- Include software/library versions

### Mathematics
- Cite original theorem proofs
- Include textbooks for definitions
- Reference classic papers even if old

### Experimental Sciences
- Cite measurement protocols
- Reference dataset papers
- Include equipment specifications
- Cite statistical methods

---

## Example Bibliography Section

```latex
\bibliographystyle{plain}  % or alpha, ieeetr, acm, etc.
\bibliography{references}   % your .bib file name
```

Common styles:
- `plain` - [1], [2], [3] (numbered, alphabetical by author)
- `alpha` - [Smi23], [Jon22] (author initials + year)
- `ieeetr` - [1], [2], [3] (numbered, order of appearance)
- `acm` - ACM style
- `apa` - APA style

---

## Quick Reference

### Citation Checklist
- [ ] Claim is not common knowledge
- [ ] Source is authoritative
- [ ] Citation is accurate
- [ ] BibTeX entry is complete
- [ ] Formatting is correct

### Common Verbs for Citations
- X **showed** that...
- X **demonstrated** that...
- X **proposed** a method for...
- X **found** that...
- X **proved** that...
- X **argued** that...
- According to X, ...
- As **shown** by X, ...

---

## Resources

### Finding Papers
- Google Scholar
- Semantic Scholar
- arXiv
- IEEE Xplore
- ACM Digital Library
- DBLP (Computer Science)
- PubMed (Medicine/Biology)

### Citation Tools
- Google Scholar "Cite" button (exports BibTeX)
- DOI lookup: https://www.doi2bib.org
- arXiv citation export
- Conference/journal website citation export

---

## Remember

**Good citation practices:**
1. Cite honestly and accurately
2. Credit others' work appropriately
3. Maintain a complete bibliography
4. Verify all citations before submission
5. Follow field conventions

**Your citations demonstrate:**
- Your knowledge of the field
- Your academic integrity
- The foundation for your work

**Take citation seriously - it matters!**
