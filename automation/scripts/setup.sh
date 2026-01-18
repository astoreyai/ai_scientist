#!/bin/bash

# PhD Dissertation Pipeline - Setup Script
# This script initializes a new dissertation project using the pipeline templates

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PIPELINE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Target directory
TARGET_DIR="${1:-MY_DISSERTATION}"

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}PhD Dissertation Pipeline - Setup${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check if target directory already exists
if [ -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}Warning: Directory '$TARGET_DIR' already exists.${NC}"
    read -p "Do you want to overwrite it? (yes/no): " -r
    echo
    if [[ ! $REPLY =~ ^[Yy]es$ ]]; then
        echo -e "${RED}Setup cancelled.${NC}"
        exit 1
    fi
    rm -rf "$TARGET_DIR"
fi

echo -e "${GREEN}Creating dissertation directory structure...${NC}"

# Create directory structure
mkdir -p "$TARGET_DIR"/{chapters,latex/chapters,bibliography,figures,code,data/{raw,processed,results},progress,notes}

echo -e "${GREEN}✓ Directory structure created${NC}"
echo ""

# Copy templates
echo -e "${GREEN}Copying chapter templates...${NC}"

if [ -d "$PIPELINE_DIR/templates/dissertation" ]; then
    cp "$PIPELINE_DIR/templates/dissertation"/*.md "$TARGET_DIR/chapters/" 2>/dev/null || echo -e "${YELLOW}Note: Some chapter templates may not exist yet${NC}"
fi

echo -e "${GREEN}✓ Chapter templates copied${NC}"
echo ""

# Copy config template
echo -e "${GREEN}Creating configuration file...${NC}"

if [ -f "$PIPELINE_DIR/templates/config.yaml" ]; then
    cp "$PIPELINE_DIR/templates/config.yaml" "$TARGET_DIR/config.yaml"
    echo -e "${GREEN}✓ config.yaml created${NC}"
else
    echo -e "${YELLOW}! config.yaml template not found, creating basic version${NC}"
    cat > "$TARGET_DIR/config.yaml" << 'EOF'
# PhD Dissertation Configuration
title: "Your Dissertation Title"
author: "Your Name"
degree: "PhD in Computer Science"
university: "Your University"
advisor: "Dr. Advisor Name"
timeline_months: 12
EOF
fi

echo ""

# Copy LaTeX templates
echo -e "${GREEN}Setting up LaTeX templates...${NC}"

if [ -d "$PIPELINE_DIR/templates/latex" ]; then
    cp -r "$PIPELINE_DIR/templates/latex"/* "$TARGET_DIR/latex/" 2>/dev/null || echo -e "${YELLOW}Note: Some LaTeX templates may not exist yet${NC}"
fi

# Create basic LaTeX template if doesn't exist
if [ ! -f "$TARGET_DIR/latex/dissertation.tex" ]; then
    cat > "$TARGET_DIR/latex/dissertation.tex" << 'EOF'
\documentclass[12pt,oneside]{book}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{hyperref}
\usepackage{cite}

% Metadata
\title{Your Dissertation Title}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

\tableofcontents

% Include chapters here
% \include{chapters/chapter01}

\bibliographystyle{plain}
\bibliography{../bibliography/references}

\end{document}
EOF
fi

echo -e "${GREEN}✓ LaTeX templates created${NC}"
echo ""

# Create initial progress tracking files
echo -e "${GREEN}Initializing progress tracking...${NC}"

cat > "$TARGET_DIR/progress/todo.md" << 'EOF'
# PhD Dissertation TODO List

## Phase 1: Planning (Weeks 1-4)
- [ ] Define research questions
- [ ] Complete literature review
- [ ] Create research framework

## Phase 2: Methodology (Weeks 5-8)
- [ ] Write theoretical foundation
- [ ] Design experimental protocol
- [ ] Draft methodology chapter

## Phase 3: Execution (Weeks 9-24)
- [ ] Implement system/algorithm
- [ ] Run experiments
- [ ] Collect results

## Phase 4: Writing (Weeks 25-36)
- [ ] Draft all chapters
- [ ] Revise chapters
- [ ] Create figures/tables

## Phase 5: Finalization (Weeks 37-40)
- [ ] Convert to LaTeX
- [ ] Complete bibliography
- [ ] Prepare defense
EOF

cat > "$TARGET_DIR/progress/timeline.md" << 'EOF'
# PhD Dissertation Timeline

## Current Status
- **Phase:** Planning
- **Progress:** 0%
- **Target Defense:** [Set your date]

## Milestones
- [ ] Literature review complete
- [ ] Methodology draft complete
- [ ] Implementation complete
- [ ] Experiments complete
- [ ] All chapters drafted
- [ ] LaTeX compiled
- [ ] Defense scheduled

## Weekly Goals
Track your weekly progress here.

### Week 1
- Goal 1
- Goal 2

### Week 2
- Goal 1
- Goal 2
EOF

echo -e "${GREEN}✓ Progress tracking initialized${NC}"
echo ""

# Create README
echo -e "${GREEN}Creating README...${NC}"

cat > "$TARGET_DIR/README.md" << 'EOF'
# My PhD Dissertation

## Overview

[Brief description of your research]

## Structure

- `chapters/` - Markdown chapter files
- `latex/` - LaTeX compilation files
- `bibliography/` - References
- `figures/` - Figures and diagrams
- `code/` - Implementation code
- `data/` - Datasets and results
- `progress/` - TODO lists and timeline
- `notes/` - Research notes

## Getting Started

1. Edit `config.yaml` with your information
2. Start with `chapters/chapter_01_introduction.md`
3. Follow the templates and fill in content
4. Track progress in `progress/todo.md`

## Compilation

To compile to PDF:
```bash
cd latex
pdflatex dissertation.tex
bibtex dissertation
pdflatex dissertation.tex
pdflatex dissertation.tex
```

## Resources

- See PHD_PIPELINE/README.md for full documentation
- Follow workflows in PHD_PIPELINE/workflows/
- Use quality checklists in PHD_PIPELINE/tools/quality_assurance/
EOF

echo -e "${GREEN}✓ README created${NC}"
echo ""

# Create .gitignore
cat > "$TARGET_DIR/.gitignore" << 'EOF'
# LaTeX auxiliary files
*.aux
*.log
*.out
*.toc
*.lof
*.lot
*.bbl
*.blg
*.bcf
*.run.xml

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/

# Data
data/raw/
*.csv
*.h5
*.pkl

# OS
.DS_Store
Thumbs.db

# Backup
*~
*.bak
EOF

echo ""
echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}Setup complete!${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""
echo -e "${GREEN}Your dissertation has been initialized in: ${BLUE}$TARGET_DIR${NC}"
echo ""
echo -e "Next steps:"
echo -e "  1. ${YELLOW}cd $TARGET_DIR${NC}"
echo -e "  2. ${YELLOW}Edit config.yaml with your information${NC}"
echo -e "  3. ${YELLOW}Start with chapters/chapter_01_introduction.md${NC}"
echo -e "  4. ${YELLOW}Follow PHD_PIPELINE/workflows/ in order${NC}"
echo ""
echo -e "Resources:"
echo -e "  - ${BLUE}PHD_PIPELINE/README.md${NC} - Quick start guide"
echo -e "  - ${BLUE}PHD_PIPELINE/PIPELINE_GUIDE.md${NC} - Comprehensive guide"
echo -e "  - ${BLUE}PHD_PIPELINE/workflows/${NC} - Step-by-step processes"
echo ""
echo -e "${GREEN}Good luck with your PhD! 🎓${NC}"
echo ""
