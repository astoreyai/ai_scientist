#!/bin/bash

# PhD Dissertation Pipeline - LaTeX Build Script
# This script compiles the dissertation to PDF

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}Building Dissertation PDF${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "dissertation.tex" ]; then
    echo -e "${RED}Error: dissertation.tex not found!${NC}"
    echo -e "${YELLOW}Please run this script from your dissertation's latex/ directory${NC}"
    echo -e "Example: cd MY_DISSERTATION/latex && ../../PHD_PIPELINE/automation/scripts/build_latex.sh"
    exit 1
fi

# Check if pdflatex is installed
if ! command -v pdflatex &> /dev/null; then
    echo -e "${RED}Error: pdflatex not found!${NC}"
    echo -e "${YELLOW}Please install LaTeX. On Ubuntu/Debian:${NC}"
    echo -e "  sudo apt-get install texlive-full"
    exit 1
fi

# Clean previous build
echo -e "${GREEN}Cleaning previous build files...${NC}"
rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.bcf *.run.xml
echo -e "${GREEN}✓ Cleaned${NC}"
echo ""

# First pass
echo -e "${GREEN}Running pdflatex (pass 1/3)...${NC}"
pdflatex -interaction=nonstopmode dissertation.tex > /dev/null 2>&1 || {
    echo -e "${RED}✗ First pass failed${NC}"
    echo -e "${YELLOW}Check the log file for errors: dissertation.log${NC}"
    exit 1
}
echo -e "${GREEN}✓ Pass 1 complete${NC}"
echo ""

# Run bibtex if bibliography exists
if [ -f "../bibliography/references.bib" ] || [ -f "references.bib" ]; then
    echo -e "${GREEN}Running bibtex...${NC}"
    bibtex dissertation > /dev/null 2>&1 || {
        echo -e "${YELLOW}! BibTeX had warnings (this is often normal)${NC}"
    }
    echo -e "${GREEN}✓ BibTeX complete${NC}"
    echo ""
fi

# Second pass
echo -e "${GREEN}Running pdflatex (pass 2/3)...${NC}"
pdflatex -interaction=nonstopmode dissertation.tex > /dev/null 2>&1 || {
    echo -e "${RED}✗ Second pass failed${NC}"
    echo -e "${YELLOW}Check the log file for errors: dissertation.log${NC}"
    exit 1
}
echo -e "${GREEN}✓ Pass 2 complete${NC}"
echo ""

# Third pass
echo -e "${GREEN}Running pdflatex (pass 3/3)...${NC}"
pdflatex -interaction=nonstopmode dissertation.tex > /dev/null 2>&1 || {
    echo -e "${RED}✗ Third pass failed${NC}"
    echo -e "${YELLOW}Check the log file for errors: dissertation.log${NC}"
    exit 1
}
echo -e "${GREEN}✓ Pass 3 complete${NC}"
echo ""

# Check if PDF was created
if [ -f "dissertation.pdf" ]; then
    PDF_SIZE=$(du -h dissertation.pdf | cut -f1)
    PDF_PAGES=$(pdfinfo dissertation.pdf 2>/dev/null | grep Pages | awk '{print $2}')

    echo -e "${BLUE}================================================${NC}"
    echo -e "${GREEN}✓ Build successful!${NC}"
    echo -e "${BLUE}================================================${NC}"
    echo ""
    echo -e "PDF created: ${BLUE}dissertation.pdf${NC}"
    echo -e "Size: ${BLUE}$PDF_SIZE${NC}"
    if [ -n "$PDF_PAGES" ]; then
        echo -e "Pages: ${BLUE}$PDF_PAGES${NC}"
    fi
    echo ""
else
    echo -e "${RED}✗ Build failed - PDF not created${NC}"
    exit 1
fi

# Optional: Open PDF (uncomment for your platform)
# Linux: xdg-open dissertation.pdf
# macOS: open dissertation.pdf
# Windows: start dissertation.pdf
