# Figure, Table, and Equation Guidelines for PhD Dissertations

**PURPOSE:** Create professional, publication-quality figures, tables, and equations that enhance your dissertation.

**WHY THIS MATTERS:**
- Figures/tables are often the first thing readers look at
- Poor quality visuals undermine your credibility
- Proper formatting is required for publication
- Clear visualizations communicate findings better than text alone

**APPLIES TO:** All dissertation chapters, especially Results and Methodology

---

## 📋 TABLE OF CONTENTS

1. [Figures - General Guidelines](#1-figures---general-guidelines)
2. [Figure Creation Tools](#2-figure-creation-tools)
3. [Specific Figure Types](#3-specific-figure-types)
4. [Tables - General Guidelines](#4-tables---general-guidelines)
5. [Table Formatting](#5-table-formatting)
6. [Equations - LaTeX Basics](#6-equations---latex-basics)
7. [Equation Formatting in Word](#7-equation-formatting-in-word)
8. [Numbering and Cross-Referencing](#8-numbering-and-cross-referencing)
9. [Captions and Labels](#9-captions-and-labels)
10. [Common Mistakes to Avoid](#10-common-mistakes-to-avoid)

---

## 1. FIGURES - GENERAL GUIDELINES

### 1.1 When to Use Figures

**USE FIGURES FOR:**
- ✅ **Visualizing data:** Charts, graphs, plots
- ✅ **Showing relationships:** Scatter plots, correlation matrices
- ✅ **Illustrating concepts:** Diagrams, flowcharts, models
- ✅ **Displaying trends:** Line graphs, time series
- ✅ **Comparing groups:** Bar charts, box plots
- ✅ **Showing distributions:** Histograms, density plots
- ✅ **Spatial data:** Maps, heatmaps, network diagrams

**DO NOT USE FIGURES FOR:**
- ❌ **Simple data:** If 3-4 numbers, use text instead
- ❌ **Redundancy:** Don't repeat same data in figure AND table (choose one)
- ❌ **Decoration:** Every figure must serve a purpose

### 1.2 Figure Quality Standards

**RESOLUTION:**
- **Minimum:** 300 DPI (dots per inch) for print
- **Screen display:** 150 DPI acceptable for drafts
- **Vector formats preferred:** PDF, SVG, EPS (scalable without quality loss)
- **Raster formats acceptable:** PNG (not JPEG for charts/graphs - JPEG compresses poorly)

**SIZE:**
- **Width:** Typically 3.5 inches (1 column) or 7 inches (2 columns) for journals
  - Dissertation: Full page width acceptable (6-7 inches)
- **Height:** No taller than page (9-10 inches max)
- **Text size in figure:** 10-12pt font minimum (readable when printed)

**COLOR:**
- **Grayscale-friendly:** Use patterns/textures in addition to color (for B&W printing)
- **Colorblind-friendly:** Avoid red-green combinations
- **High contrast:** Dark colors on light background (or vice versa)

### 1.3 Figure File Formats

| Format | Type | When to Use | Pros | Cons |
|--------|------|-------------|------|------|
| **PDF** | Vector | Diagrams, plots, charts | Scalable, high quality, universal | Large file size |
| **SVG** | Vector | Web figures, diagrams | Scalable, editable, small file | Limited software support |
| **EPS** | Vector | Publication (LaTeX) | Scalable, publication-standard | Not web-friendly |
| **PNG** | Raster | Screenshots, photos, charts | Lossless, supports transparency | Not scalable |
| **TIFF** | Raster | Photos, microscopy | High quality, uncompressed | Very large files |
| **JPEG** | Raster | Photos only | Small file size | Lossy compression (bad for charts) |

**RECOMMENDATION:**
- **For charts/graphs:** PDF or PNG (300 DPI)
- **For photos:** PNG or TIFF
- **For LaTeX:** EPS or PDF
- **For Word:** PNG or PDF (insert as high-quality)

---

## 2. FIGURE CREATION TOOLS

### 2.1 Statistical Plots (Data Visualization)

**R (ggplot2):**
```r
library(ggplot2)

# Example: Scatter plot with regression line
ggplot(data, aes(x = stress, y = coping)) +
  geom_point(size = 3, alpha = 0.6) +
  geom_smooth(method = "lm", color = "blue", se = TRUE) +
  labs(
    title = "Relationship Between Stress and Coping",
    x = "Stress Score",
    y = "Coping Score"
  ) +
  theme_minimal(base_size = 14) +  # Increase font size
  theme(
    plot.title = element_text(hjust = 0.5, size = 16),
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 12)
  )

# Save high-quality figure
ggsave("figure_01_stress_coping.pdf", width = 7, height = 5, dpi = 300)
ggsave("figure_01_stress_coping.png", width = 7, height = 5, dpi = 300)
```

**Python (matplotlib/seaborn):**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['font.size'] = 12

# Example: Box plot
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(x='group', y='score', data=data, ax=ax)
ax.set_xlabel('Group', fontsize=14)
ax.set_ylabel('Score', fontsize=14)
ax.set_title('Score Distribution by Group', fontsize=16)

# Save high-quality
plt.tight_layout()
plt.savefig('figure_02_boxplot.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure_02_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()
```

**Excel (Basic Charts):**
- Create chart → Design tab → "Save as Template" for consistency
- Export: Right-click chart → "Save as Picture" → PNG (300 DPI if option available)
- **Limitations:** Less flexible than R/Python, harder to make publication-quality

### 2.2 Diagrams and Illustrations

**Draw.io / diagrams.net (Free, Web-based):**
- https://www.diagrams.net/
- Use for: Flowcharts, conceptual models, process diagrams
- Export: File → Export as → PDF or PNG (300 DPI)

**Microsoft PowerPoint (Surprisingly Effective):**
- Create diagram in PowerPoint (use shapes, SmartArt)
- Export: File → Export → PDF or PNG (high quality)
- Or: Copy slide → Paste as "Picture (Enhanced Metafile)" in Word

**Adobe Illustrator (Professional, Paid):**
- Industry standard for vector graphics
- Steep learning curve
- Best for: Complex diagrams, publication figures

**Inkscape (Free, Open-Source Alternative to Illustrator):**
- https://inkscape.org/
- Vector graphics editor
- Export to PDF, SVG, EPS, PNG

**BioRender (Life Sciences):**
- https://biorender.com/
- Pre-made scientific icons and templates
- Subscription-based ($10-20/month)

### 2.3 Specialized Tools

**Network Diagrams:**
- **Gephi** (free): https://gephi.org/
- **Cytoscape** (free, bioinformatics): https://cytoscape.org/
- **NetworkX (Python):** Programmatic network visualization

**Mind Maps / Concept Maps:**
- **XMind** (free/paid): https://www.xmind.net/
- **CmapTools** (free): https://cmap.ihmc.us/

**Timelines:**
- **TimelineJS** (free, web): https://timeline.knightlab.com/
- **PowerPoint** (using SmartArt)

**Maps / GIS:**
- **QGIS** (free): https://qgis.org/
- **ArcGIS** (paid, often via university license)

---

## 3. SPECIFIC FIGURE TYPES

### 3.1 Bar Charts (Comparing Categories)

**WHEN TO USE:** Comparing values across categories (e.g., mean scores by group)

**BEST PRACTICES:**
- Start Y-axis at 0 (don't truncate to exaggerate differences)
- Order bars logically (alphabetical, by size, or by category)
- Add error bars (SD, SE, or CI) for inferential data
- Label axes clearly
- Use horizontal bars if category names are long

**R CODE EXAMPLE:**
```r
library(ggplot2)

# Bar chart with error bars
ggplot(summary_data, aes(x = group, y = mean_score)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_errorbar(aes(ymin = mean_score - se, ymax = mean_score + se),
                width = 0.2) +
  labs(
    x = "Group",
    y = "Mean Score",
    title = "Mean Coping Scores by Group"
  ) +
  theme_minimal(base_size = 14) +
  ylim(0, max(summary_data$mean_score) * 1.2)  # Start at 0, add headroom
```

### 3.2 Scatter Plots (Relationships)

**WHEN TO USE:** Showing relationship between two continuous variables

**BEST PRACTICES:**
- Add regression line (if testing linear relationship)
- Include 95% CI shading around regression line
- Adjust point transparency if many points overlap (alpha < 1)
- Annotate with correlation coefficient (r = .42, p < .001)
- Use different shapes/colors for groups if applicable

**R CODE EXAMPLE:**
```r
ggplot(data, aes(x = stress, y = coping)) +
  geom_point(alpha = 0.5, size = 2) +
  geom_smooth(method = "lm", color = "blue", se = TRUE) +
  annotate("text", x = max(data$stress) * 0.8, y = min(data$coping) * 1.1,
           label = "r = .42, p < .001", size = 5) +
  labs(x = "Stress Score", y = "Coping Score") +
  theme_minimal(base_size = 14)
```

### 3.3 Line Graphs (Trends Over Time)

**WHEN TO USE:** Showing change over time or across ordered conditions

**BEST PRACTICES:**
- Use lines for continuous data (time, dose-response)
- Add markers (points) if few data points
- Include error ribbons (shaded area for SE/CI)
- Different line styles for multiple groups (solid, dashed, dotted)
- Label each line (legend or direct labels)

**R CODE EXAMPLE:**
```r
ggplot(time_data, aes(x = time, y = score, color = group)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  geom_ribbon(aes(ymin = score - se, ymax = score + se, fill = group),
              alpha = 0.2) +
  labs(x = "Time (weeks)", y = "Score", color = "Group") +
  theme_minimal(base_size = 14) +
  scale_color_brewer(palette = "Set1")
```

### 3.4 Box Plots (Distributions)

**WHEN TO USE:** Comparing distributions across groups

**BEST PRACTICES:**
- Show all data points (jittered) if n is small (<50 per group)
- Use violin plots if you want to show full distribution shape
- Indicate outliers clearly
- Add significance indicators (*, **, ***) if testing group differences

**R CODE EXAMPLE:**
```r
ggplot(data, aes(x = group, y = score)) +
  geom_boxplot(outlier.shape = NA) +  # Hide outliers (show as jittered points)
  geom_jitter(width = 0.2, alpha = 0.3) +  # Show individual points
  labs(x = "Group", y = "Score") +
  theme_minimal(base_size = 14) +
  stat_compare_means()  # Add p-values (requires ggpubr package)
```

### 3.5 Heatmaps (Correlation Matrices)

**WHEN TO USE:** Showing correlations between many variables

**BEST PRACTICES:**
- Use diverging color scale (e.g., blue-white-red for negative-zero-positive)
- Include correlation values in cells (if not too many variables)
- Cluster rows/columns (if applicable)
- Add significance indicators (*, **, ***)

**R CODE EXAMPLE:**
```r
library(corrplot)

# Correlation matrix
cor_matrix <- cor(data[, numeric_vars], use = "pairwise.complete.obs")

# Heatmap
corrplot(cor_matrix, method = "color", type = "upper",
         tl.col = "black", tl.srt = 45,  # Text label color and rotation
         addCoef.col = "black",  # Add correlation coefficients
         number.cex = 0.7,  # Coefficient size
         col = colorRampPalette(c("blue", "white", "red"))(200))
```

### 3.6 Conceptual Diagrams (Models, Frameworks)

**WHEN TO USE:** Illustrating theoretical models, study design, processes

**BEST PRACTICES:**
- Keep it simple (minimize clutter)
- Use consistent shapes (rectangles for constructs, ovals for processes, arrows for relationships)
- Label all components clearly
- Use alignment and spacing consistently
- Color-code if multiple types of elements

**TOOLS:** PowerPoint, Draw.io, Adobe Illustrator, Inkscape

**EXAMPLE ELEMENTS:**
- **Boxes:** Constructs, variables
- **Arrows:** Causal relationships, processes
- **Circles/Ovals:** Latent variables, processes
- **Dashed lines:** Hypothesized relationships
- **Solid lines:** Established relationships

### 3.7 Qualitative Data Visualization (Themes)

**WHEN TO USE:** Illustrating qualitative themes, coding structure

**OPTIONS:**

1. **Thematic Map:**
   - Hierarchy of themes and subthemes
   - Use tree diagram or nested boxes
   - Tools: Draw.io, PowerPoint

2. **Word Cloud:**
   - Frequency of terms in qualitative data
   - Tools: Wordcloud (R/Python), Wordle
   - **Caution:** Often seen as unscholarly; use sparingly

3. **Sankey Diagram:**
   - Flow of codes through data
   - Tools: RAWGraphs (https://www.rawgraphs.io/), R (ggalluvial)

---

## 4. TABLES - GENERAL GUIDELINES

### 4.1 When to Use Tables

**USE TABLES FOR:**
- ✅ **Exact values:** When precision matters (means, SDs, p-values)
- ✅ **Multiple variables:** Demographics, descriptive statistics
- ✅ **Comparison:** Side-by-side comparison of studies, methods
- ✅ **Detailed results:** Regression coefficients, ANOVA results

**DO NOT USE TABLES FOR:**
- ❌ **Trends:** Use line graph instead
- ❌ **Distributions:** Use histogram or box plot
- ❌ **Relationships:** Use scatter plot
- ❌ **Simple data:** If 2-3 values, state in text

### 4.2 Table Design Principles

**SIMPLICITY:**
- Minimize gridlines (use horizontal lines only, no vertical lines)
- White space is your friend (don't cram)
- Align numbers on decimal point
- Left-align text, right-align numbers

**FORMATTING:**
- **Font:** Same as body text (usually 10-12pt)
- **Lines:** Top, bottom, and below header (APA style)
- **Borders:** Minimal (no boxes around cells)
- **Shading:** Optional for header row (light gray)

**STRUCTURE:**
- **Title:** Above table (Table 1: [Descriptive Title])
- **Column headers:** Clear, concise labels
- **Row labels:** Clear, hierarchical if needed
- **Notes:** Below table (*, **, *** for significance; abbreviations)

### 4.3 Table Numbering and Titles

**NUMBERING:**
- Number tables sequentially within chapters: Table 4.1, Table 4.2, etc.
- OR number consecutively: Table 1, Table 2, Table 3 (throughout dissertation)

**TITLES:**
- Descriptive and standalone (reader should understand without reading text)
- Place title ABOVE table
- Format: **Table X:** [Title] (italicize "Table X" or use bold)

**EXAMPLES:**
- **Good:** "Table 4.1: Descriptive Statistics and Correlations for Study Variables"
- **Bad:** "Table 1: Statistics" (too vague)

---

## 5. TABLE FORMATTING

### 5.1 APA Style Table (Most Common in Social Sciences)

**STRUCTURE:**
```
Table 4.1
Descriptive Statistics and Correlations Among Study Variables

Variable           M     SD    1     2     3     4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Stress         25.3  5.2   —
2. Avoidance Cop. 3.1   0.8  .45** —
3. Reframing Cop. 3.8   0.7 -.32* -.15   —
4. Support Cop.   4.2   0.6 -.28* -.20  .55** —
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Note. N = 250. Cop. = Coping.
*p < .05. **p < .01.
```

**KEY FEATURES:**
- Top line, bottom line, line below header
- No vertical lines
- Align numbers on decimal
- Dashes (—) for diagonal in correlation matrix
- Notes below table

**WORD/GOOGLE DOCS:**
- Insert → Table
- Remove all borders
- Add horizontal lines: Borders → Top, Bottom, and between header and data

### 5.2 Regression Table

**EXAMPLE:**
```
Table 5.2
Hierarchical Regression Analysis Predicting Coping from Stress and Moderators

                          Model 1         Model 2         Model 3
Predictor                 β      SE       β      SE       β      SE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Stress                   .42*** .08      .40*** .08      .38*** .07
Gender                             —      .15*   .07      .14*   .07
Age                                —      .08    .06      .07    .06
Stress × Gender                    —       —      —       .23**  .09
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
R²                        .18            .21             .26
ΔR²                        —             .03*            .05**
F                        18.4***        12.1***         14.8***
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Note. N = 250. β = standardized regression coefficient. SE = standard error.
*p < .05. **p < .01. ***p < .001.
```

### 5.3 Demographic Table

**EXAMPLE:**
```
Table 3.1
Participant Demographic Characteristics

Characteristic                      n       %
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gender
  Male                              80     32.0
  Female                           170     68.0

Age (years)
  18-20                             65     26.0
  21-23                            110     44.0
  24-30                             75     30.0
  M (SD)                        22.3 (2.1)

Ethnicity
  White                            125     50.0
  Black/African American            45     18.0
  Hispanic/Latinx                   50     20.0
  Asian                             25     10.0
  Other                              5      2.0

Education
  Undergraduate                    200     80.0
  Graduate                          50     20.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Note. N = 250.
```

### 5.4 Qualitative Themes Table

**EXAMPLE:**
```
Table 6.1
Qualitative Themes and Representative Quotes

Theme                   Frequency    Representative Quote
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Avoidance Coping        17 (68%)     "I just tried not to think about it.
                                      I distracted myself with Netflix."
                                      (P07)

Reframing               18 (72%)     "I started seeing it as a learning
                                      experience rather than a failure."
                                      (P12)

Seeking Social Support  22 (88%)     "I called my best friend. Just talking
                                      about it helped me feel better." (P18)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Note. N = 25 participants. Frequency = number (%) of participants who
mentioned this theme.
```

### 5.5 Creating Tables in Different Software

**WORD:**
1. Insert → Table → [Choose dimensions]
2. Design → Borders → "No Border"
3. Add horizontal lines: Borders → Top, Bottom, Inside Horizontal (header only)
4. Align text: Right-click column → Table Properties → Cell → Alignment

**LATEX:**
```latex
\begin{table}[h]
\centering
\caption{Descriptive Statistics and Correlations}
\label{tab:descriptives}
\begin{tabular}{lcccccc}
\toprule
Variable & M & SD & 1 & 2 & 3 & 4 \\
\midrule
1. Stress & 25.3 & 5.2 & — & & & \\
2. Avoidance Cop. & 3.1 & 0.8 & .45** & — & & \\
3. Reframing Cop. & 3.8 & 0.7 & -.32* & -.15 & — & \\
4. Support Cop. & 4.2 & 0.6 & -.28* & -.20 & .55** & — \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item \textit{Note.} N = 250. Cop. = Coping.
\item * p < .05. ** p < .01.
\end{tablenotes}
\end{table}
```

**EXCEL → WORD:**
1. Format table in Excel (minimal borders, aligned)
2. Copy table
3. Paste in Word: "Keep Source Formatting" OR "Use Destination Styles"
4. Adjust as needed

---

## 6. EQUATIONS - LATEX BASICS

### 6.1 Why LaTeX for Equations?

**ADVANTAGES:**
- Professional typesetting
- Consistent formatting
- Easy to edit and reuse
- Standard in STEM fields
- Renders beautifully in PDF

**TOOLS:**
- **Overleaf** (online LaTeX editor): https://www.overleaf.com/
- **MathType** (Word plugin, generates LaTeX): https://www.wiris.com/en/mathtype/
- **Word Equation Editor** (built-in, supports LaTeX input in Word 365)

### 6.2 Basic LaTeX Equation Syntax

**INLINE EQUATIONS:** Use `$...$`
```latex
The mean is $\mu = 25.3$ and standard deviation is $\sigma = 5.2$.
```
Output: The mean is μ = 25.3 and standard deviation is σ = 5.2.

**DISPLAY EQUATIONS:** Use `\[...\]` or `$$...$$`
```latex
\[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \epsilon
\]
```
Output: (centered, larger)
y = β₀ + β₁x₁ + β₂x₂ + ε

**NUMBERED EQUATIONS:** Use `equation` environment
```latex
\begin{equation}
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \epsilon
\label{eq:regression}
\end{equation}
```
Output: (centered, with number on right: (1))

### 6.3 Common LaTeX Math Symbols

**GREEK LETTERS:**
```latex
\alpha  \beta  \gamma  \delta  \epsilon  \zeta  \eta  \theta
\mu  \sigma  \tau  \phi  \chi  \psi  \omega
\Alpha  \Beta  \Gamma  \Delta  \Sigma  \Omega  (uppercase)
```

**OPERATORS:**
```latex
+  -  \times  \div  \pm  \mp
=  \neq  \approx  \equiv
<  >  \leq  \geq  \ll  \gg
```

**SUBSCRIPTS & SUPERSCRIPTS:**
```latex
x_1  x^2  x_i^2  x_{i,j}  (use {} for multi-character subscripts)
```

**FRACTIONS:**
```latex
\frac{a}{b}  \frac{x^2 + 1}{x - 3}
```

**SQUARE ROOTS:**
```latex
\sqrt{x}  \sqrt[3]{x}  (cube root)
```

**SUMS & INTEGRALS:**
```latex
\sum_{i=1}^{n} x_i  \int_a^b f(x) dx  \prod_{i=1}^{n} x_i
```

**MATRICES:**
```latex
\begin{pmatrix}  % or bmatrix for brackets
a & b \\
c & d
\end{pmatrix}
```

### 6.4 Example Equations for Dissertations

**LINEAR REGRESSION:**
```latex
\begin{equation}
y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \epsilon_i
\end{equation}
```

**ANOVA F-STATISTIC:**
```latex
\begin{equation}
F = \frac{MS_{\text{between}}}{MS_{\text{within}}} = \frac{\frac{SS_{\text{between}}}{df_{\text{between}}}}{\frac{SS_{\text{within}}}{df_{\text{within}}}}
\end{equation}
```

**CORRELATION:**
```latex
\begin{equation}
r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}
\end{equation}
```

**SHAPLEY VALUE (for XAI dissertations):**
```latex
\begin{equation}
\phi_i(f) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} [f(S \cup \{i\}) - f(S)]
\label{eq:shapley}
\end{equation}
```

**LOSS FUNCTION (for ML dissertations):**
```latex
\begin{equation}
\mathcal{L}(\theta) = \frac{1}{n} \sum_{i=1}^{n} \ell(y_i, \hat{y}_i(\theta)) + \lambda \|\theta\|_2^2
\end{equation}
```

**MULTI-LINE EQUATIONS:** Use `align` environment
```latex
\begin{align}
y &= \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \epsilon \\
  &= 5.3 + 0.42 \cdot x_1 + 0.15 \cdot x_2 + \epsilon
\end{align}
```

---

## 7. EQUATION FORMATTING IN WORD

### 7.1 Word Equation Editor (Built-in)

**INSERT EQUATION:**
1. Insert → Equation (or Alt + =)
2. Type equation using LaTeX-like syntax OR use GUI
3. Equation is automatically formatted

**WORD LATEX INPUT (Word 365+):**
- Type LaTeX directly: `\alpha` → α
- Supports most LaTeX commands
- Press Space to render

**EXAMPLE:**
1. Insert → Equation
2. Type: `y = \beta_0 + \beta_1 x_1 + \epsilon`
3. Press Space → renders as: y = β₀ + β₁x₁ + ε

### 7.2 MathType (Word Plugin, Professional)

**WHY USE MATHTYPE:**
- More features than Word's built-in
- LaTeX export
- Equation numbering
- Professional rendering

**DOWNLOAD:** https://www.wiris.com/en/mathtype/ (free trial, ~$60/year)

**USE:**
1. MathType → Insert Equation
2. Type equation using GUI or LaTeX
3. Insert into Word

### 7.3 Converting LaTeX to Word

**METHOD 1: Pandoc (Free, Command-Line)**
```bash
pandoc input.tex -o output.docx
```
Converts LaTeX equations to Word equations automatically.

**METHOD 2: Copy-Paste from Overleaf**
- Write equations in Overleaf
- Compile to PDF
- Copy from PDF → Paste into Word (may need to re-format)

**METHOD 3: MathJax (Web-Based)**
- Use https://www.mathcha.io/ (online equation editor)
- Type LaTeX → Renders → Copy image to Word

---

## 8. NUMBERING AND CROSS-REFERENCING

### 8.1 Numbering Scheme

**FIGURES:**
- Chapter-based: Figure 4.1, Figure 4.2 (Chapter 4, Figure 1, 2)
- OR consecutive: Figure 1, Figure 2, Figure 3 (throughout dissertation)

**TABLES:**
- Same as figures: Table 4.1, Table 4.2 OR Table 1, Table 2

**EQUATIONS:**
- Chapter-based: Equation (4.1), (4.2)
- OR consecutive: Equation (1), (2), (3)

**RECOMMENDATION:** Use chapter-based numbering (easier to reorganize chapters)

### 8.2 Cross-Referencing in Word

**INSERT CAPTION (Figure/Table):**
1. Right-click figure → Insert Caption
2. Label: "Figure" or "Table"
3. Numbering: Include chapter number (Figure 4.1) OR simple numbering (Figure 1)

**CROSS-REFERENCE IN TEXT:**
1. References → Insert Cross-Reference
2. Reference type: Figure/Table/Equation
3. Insert reference to: Figure 4.1 (or "only label and number")

**BENEFIT:** If you add/delete figures, numbering auto-updates

**UPDATE FIELDS:**
- Select all (Ctrl+A) → Right-click → Update Field (F9)
- Ensures all cross-references are current

### 8.3 Cross-Referencing in LaTeX

**LABEL FIGURES:**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{figure.pdf}
\caption{Scatterplot showing relationship between X and Y.}
\label{fig:scatter}
\end{figure}
```

**REFERENCE IN TEXT:**
```latex
As shown in Figure~\ref{fig:scatter}, there is a positive relationship...
```

**LABEL EQUATIONS:**
```latex
\begin{equation}
y = \beta_0 + \beta_1 x + \epsilon
\label{eq:regression}
\end{equation}
```

**REFERENCE IN TEXT:**
```latex
Equation~\ref{eq:regression} shows the regression model...
```

**BENEFIT:** LaTeX auto-numbers and cross-references update on compile

---

## 9. CAPTIONS AND LABELS

### 9.1 Figure Captions

**FORMAT:**
- **Figure X.** [Brief description]. [Optional: Additional details].

**PLACEMENT:** Below figure

**EXAMPLES:**

**Good:**
> **Figure 4.1.** Scatterplot showing the relationship between stress and coping scores. The blue line represents the linear regression fit (r = .42, p < .001).

**Bad:**
> Figure 1. Scatterplot. (too vague)

**CAPTION GUIDELINES:**
- Be descriptive (reader should understand without reading text)
- Explain what is shown (e.g., "Scatterplot showing...")
- Include key statistics if relevant (r = .42, p < .001)
- Define abbreviations not in text
- Explain symbols, colors, line types if not obvious

### 9.2 Table Titles

**FORMAT:**
- **Table X:** [Descriptive title]

**PLACEMENT:** Above table (unlike figures, which are below)

**EXAMPLES:**

**Good:**
> **Table 4.1:** Descriptive Statistics and Correlations Among Study Variables

**Bad:**
> Table 1: Statistics (too vague)

**TITLE GUIDELINES:**
- Be specific and standalone
- Include variable names or study context
- Capitalize major words
- Don't end with period

### 9.3 Equation Labels

**FORMAT:**
- Equation (X) or (X.Y) for chapter-based

**PLACEMENT:** Right-aligned on same line as equation

**REFERENCE IN TEXT:**
> "As shown in Equation (4.1), the relationship between X and Y is modeled as..."

**WHEN TO NUMBER:**
- If you refer to the equation later in text → Number it
- If it's a one-time equation → Don't number

---

## 10. COMMON MISTAKES TO AVOID

### 10.1 Figure Mistakes

**❌ MISTAKE 1: Low Resolution**
- Problem: Blurry figures (using 72 DPI screenshot)
- Fix: Use 300 DPI minimum, export as PDF or high-quality PNG

**❌ MISTAKE 2: Tiny Text in Figures**
- Problem: Axis labels/legends too small to read when printed
- Fix: Use 10-12pt font minimum in figures, test by printing

**❌ MISTAKE 3: Chart Junk**
- Problem: 3D charts, excessive colors, decorative elements
- Fix: Simplify, remove non-data elements, use 2D charts

**❌ MISTAKE 4: Missing Error Bars**
- Problem: Bar chart without SE/SD/CI (can't assess uncertainty)
- Fix: Always include error bars for inferential statistics

**❌ MISTAKE 5: Truncated Y-Axis**
- Problem: Bar chart starting at 50 instead of 0 (exaggerates differences)
- Fix: Start Y-axis at 0 for bar charts

**❌ MISTAKE 6: Colorblind-Unfriendly**
- Problem: Red-green color scheme (10% of men are red-green colorblind)
- Fix: Use blue-orange or add patterns/textures

### 10.2 Table Mistakes

**❌ MISTAKE 1: Too Many Gridlines**
- Problem: Table looks cluttered with vertical and horizontal lines
- Fix: Use APA style (horizontal lines only: top, bottom, below header)

**❌ MISTAKE 2: Inconsistent Decimal Places**
- Problem: One column has 2.3, another has 2.345678
- Fix: Use consistent rounding (2 decimal places for most statistics)

**❌ MISTAKE 3: No Table Notes**
- Problem: Abbreviations or symbols undefined
- Fix: Add notes below table explaining *, **, abbreviations

**❌ MISTAKE 4: Redundant Tables**
- Problem: Same data in table AND figure
- Fix: Choose one (figure for trends, table for exact values)

**❌ MISTAKE 5: Unaligned Numbers**
- Problem: Decimals not aligned (hard to compare)
- Fix: Right-align numbers, align on decimal point

### 10.3 Equation Mistakes

**❌ MISTAKE 1: Inconsistent Notation**
- Problem: Using β in one equation, b in another for same thing
- Fix: Use consistent notation throughout (define in text)

**❌ MISTAKE 2: Undefined Variables**
- Problem: Equation uses symbols not explained
- Fix: Define all variables: "where β₁ is the regression coefficient for..."

**❌ MISTAKE 3: Poor Formatting (Word)**
- Problem: Inline equations too small or poorly aligned
- Fix: Use Word Equation Editor, adjust size to match text

**❌ MISTAKE 4: Not Numbering Key Equations**
- Problem: Can't refer back to important equations
- Fix: Number equations you reference later, use cross-references

**❌ MISTAKE 5: Copy-Paste Errors (LaTeX)**
- Problem: Equation doesn't compile due to missing $
- Fix: Double-check LaTeX syntax, use Overleaf for error checking

---

## 11. CHECKLIST - Before Submitting

### Figure Checklist
```
For each figure:
- [ ] High resolution (300 DPI minimum)
- [ ] Text readable (10-12pt font minimum)
- [ ] Clear axis labels with units
- [ ] Legend included (if multiple series)
- [ ] Caption is descriptive and standalone
- [ ] Numbered correctly (Figure X.Y or Figure X)
- [ ] Referenced in text ("as shown in Figure 4.1...")
- [ ] File saved in correct format (PDF/PNG for final submission)
- [ ] Colorblind-friendly (or uses patterns)
- [ ] No chart junk (3D, unnecessary decorations)
```

### Table Checklist
```
For each table:
- [ ] Title is descriptive and above table
- [ ] Numbered correctly (Table X.Y or Table X)
- [ ] Minimal gridlines (APA style: top, bottom, below header)
- [ ] Numbers aligned on decimal
- [ ] Consistent decimal places (usually 2)
- [ ] Notes below table (abbreviations, significance indicators)
- [ ] Referenced in text ("as shown in Table 4.1...")
- [ ] Not redundant with figures (choose one: table OR figure)
```

### Equation Checklist
```
For each equation:
- [ ] Numbered if referenced later (Equation X or X.Y)
- [ ] All variables defined in text
- [ ] Consistent notation throughout dissertation
- [ ] Proper formatting (LaTeX or Word Equation Editor)
- [ ] Aligned properly (centered for display equations)
- [ ] Referenced in text ("as shown in Equation 4.1...")
- [ ] Readable (not too small)
```

---

## 12. RESOURCES & TOOLS

### Figure Creation
- **R:** https://ggplot2.tidyverse.org/
- **Python:** https://matplotlib.org/, https://seaborn.pydata.org/
- **Diagrams:** https://www.diagrams.net/ (Draw.io)
- **Inkscape:** https://inkscape.org/ (free vector graphics)

### Table Formatting
- **APA Table Guidelines:** https://apastyle.apa.org/style-grammar-guidelines/tables-figures
- **LaTeX Tables:** https://www.tablesgenerator.com/ (generates LaTeX code)

### Equations
- **LaTeX Math:** https://en.wikibooks.org/wiki/LaTeX/Mathematics
- **Overleaf:** https://www.overleaf.com/ (online LaTeX editor)
- **MathType:** https://www.wiris.com/en/mathtype/ (Word plugin)
- **Detexify:** http://detexify.kirelabs.org/classify.html (draw symbol → get LaTeX code)

### General Guides
- **Data Visualization:** *Fundamentals of Data Visualization* by Claus Wilke (free online)
- **Statistical Graphics:** *The Visual Display of Quantitative Information* by Edward Tufte
- **LaTeX:** *The Not So Short Introduction to LaTeX* (free PDF)

---

**END OF FIGURE, TABLE, AND EQUATION GUIDELINES**

**REMEMBER:**
- **Figures:** Show trends, relationships, distributions (visual > text)
- **Tables:** Show exact values, comparisons, detailed results
- **Equations:** Define relationships, models, formulas
- **All three:** Must be clear, professional, and serve a purpose

**Quality visuals elevate your dissertation from "acceptable" to "excellent."** Take the time to get them right! 📊📈📐
