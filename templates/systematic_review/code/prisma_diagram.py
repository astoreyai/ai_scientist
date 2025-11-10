#!/usr/bin/env python3
"""
PRISMA 2020 Flow Diagram Generator

Generates publication-ready PRISMA flow diagrams from screening data.
Complies with PRISMA 2020 specifications.

Usage:
    python code/prisma_diagram.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Dict, Optional
from pathlib import Path


class PRISMADiagramGenerator:
    """Generate PRISMA 2020 flow diagrams."""
    
    def __init__(self):
        self.counts = {}
        
    def load_from_files(self):
        """Load counts from screening data files."""
        # Load search results
        search_files = list(Path('../data/search_results').glob('*_results.csv'))
        total_records = 0
        for file in search_files:
            df = pd.read_csv(file)
            total_records += len(df)
        
        # Load deduplication data
        dedup_file = Path('../data/search_results/deduplicated_results.csv')
        if dedup_file.exists():
            dedup_df = pd.read_csv(dedup_file)
            records_after_dedup = len(dedup_df)
            duplicates_removed = total_records - records_after_dedup
        else:
            records_after_dedup = total_records
            duplicates_removed = 0
        
        # Load screening data
        title_ab_file = Path('../data/screening/title_abstract_screening.csv')
        if title_ab_file.exists():
            ta_df = pd.read_csv(title_ab_file)
            records_screened = len(ta_df)
            records_excluded_ta = (ta_df['decision'] == 'exclude').sum()
        else:
            records_screened = records_after_dedup
            records_excluded_ta = 0
        
        # Load full-text screening
        ft_file = Path('../data/screening/full_text_screening.csv')
        if ft_file.exists():
            ft_df = pd.read_csv(ft_file)
            ft_assessed = len(ft_df)
            ft_excluded = (ft_df['decision'] == 'exclude').sum()
            studies_included = ft_assessed - ft_excluded
        else:
            ft_assessed = records_screened - records_excluded_ta
            ft_excluded = 0
            studies_included = ft_assessed
        
        # Get exclusion reasons
        exclusion_file = Path('../data/screening/exclusion_reasons.csv')
        exclusion_reasons = {}
        if exclusion_file.exists():
            exc_df = pd.read_csv(exclusion_file)
            exclusion_reasons = exc_df.groupby('reason').size().to_dict()
        
        self.counts = {
            'identification': {
                'total_records': total_records,
                'duplicates_removed': duplicates_removed,
                'records_after_dedup': records_after_dedup
            },
            'screening': {
                'records_screened': records_screened,
                'records_excluded': records_excluded_ta
            },
            'eligibility': {
                'full_text_assessed': ft_assessed,
                'full_text_excluded': ft_excluded,
                'exclusion_reasons': exclusion_reasons
            },
            'included': {
                'studies_included': studies_included
            }
        }
        
        return self.counts
    
    def generate_diagram(self, output_path: str = '../results/prisma_flow_diagram.png'):
        """
        Generate PRISMA flow diagram.
        
        Args:
            output_path: Where to save the diagram
        """
        # Load counts if not already loaded
        if not self.counts:
            self.load_from_files()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 14))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.axis('off')
        
        # Box styling
        box_style = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black', linewidth=1.5)
        
        # IDENTIFICATION section
        y = 13
        self._draw_box(ax, 5, y, 3, 1, 
                      f"Records identified from:\nDatabases (n = {self.counts['identification']['total_records']})",
                      box_style)
        
        # Arrow down
        ax.arrow(5, y-0.5, 0, -0.8, head_width=0.2, head_length=0.1, fc='black', ec='black')
        
        # Duplicates removed (side box)
        y -= 2
        self._draw_box(ax, 8, y, 2, 0.8,
                      f"Records removed:\nDuplicates (n = {self.counts['identification']['duplicates_removed']})",
                      dict(boxstyle='round,pad=0.2', facecolor='lightgray', edgecolor='black', linewidth=1))
        
        # Records after deduplication
        self._draw_box(ax, 5, y, 3, 1,
                      f"Records after duplicates removed\n(n = {self.counts['identification']['records_after_dedup']})",
                      box_style)
        
        # Arrow down
        ax.arrow(5, y-0.5, 0, -0.8, head_width=0.2, head_length=0.1, fc='black', ec='black')
        
        # SCREENING section
        y -= 2.5
        ax.text(0.5, y+0.5, "SCREENING", fontsize=12, fontweight='bold')
        
        # Records screened (side box)
        self._draw_box(ax, 8, y, 2, 0.8,
                      f"Records excluded:\n(n = {self.counts['screening']['records_excluded']})",
                      dict(boxstyle='round,pad=0.2', facecolor='lightgray', edgecolor='black', linewidth=1))
        
        # Records screened
        self._draw_box(ax, 5, y, 3, 1,
                      f"Records screened\n(n = {self.counts['screening']['records_screened']})",
                      box_style)
        
        # Arrow down
        ax.arrow(5, y-0.5, 0, -0.8, head_width=0.2, head_length=0.1, fc='black', ec='black')
        
        # ELIGIBILITY section
        y -= 2.5
        ax.text(0.5, y+0.5, "ELIGIBILITY", fontsize=12, fontweight='bold')
        
        # Full-text excluded (side box with reasons)
        exclusion_text = f"Full-text excluded:\n(n = {self.counts['eligibility']['full_text_excluded']})\n"
        if self.counts['eligibility']['exclusion_reasons']:
            for reason, count in list(self.counts['eligibility']['exclusion_reasons'].items())[:3]:
                exclusion_text += f"• {reason}: {count}\n"
        
        self._draw_box(ax, 8, y, 2, 1.2,
                      exclusion_text.strip(),
                      dict(boxstyle='round,pad=0.2', facecolor='lightgray', edgecolor='black', linewidth=1),
                      fontsize=8)
        
        # Full-text assessed
        self._draw_box(ax, 5, y, 3, 1,
                      f"Full-text articles assessed\n(n = {self.counts['eligibility']['full_text_assessed']})",
                      box_style)
        
        # Arrow down
        ax.arrow(5, y-0.5, 0, -1.3, head_width=0.2, head_length=0.1, fc='black', ec='black')
        
        # INCLUDED section
        y -= 3
        ax.text(0.5, y+0.5, "INCLUDED", fontsize=12, fontweight='bold')
        
        self._draw_box(ax, 5, y, 3, 1,
                      f"Studies included in review\n(n = {self.counts['included']['studies_included']})",
                      dict(boxstyle='round,pad=0.3', facecolor='lightblue', edgecolor='black', linewidth=2))
        
        # Title
        ax.text(5, 13.8, "PRISMA 2020 Flow Diagram", 
               ha='center', fontsize=14, fontweight='bold')
        
        # Save
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✓ PRISMA diagram saved: {output_path}")
        
        # Also save as SVG for editing
        svg_path = output_path.replace('.png', '.svg')
        plt.savefig(svg_path, format='svg', bbox_inches='tight')
        print(f"✓ PRISMA diagram saved (editable): {svg_path}")
    
    def _draw_box(self, ax, x, y, width, height, text, style, fontsize=9):
        """Draw a box with text."""
        # Create box
        box = patches.FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            **style
        )
        ax.add_patch(box)
        
        # Add text
        ax.text(x, y, text, ha='center', va='center', 
               fontsize=fontsize, wrap=True)
    
    def print_summary(self):
        """Print text summary of PRISMA counts."""
        if not self.counts:
            self.load_from_files()
        
        print("═══════════════════════════════════════════════════════════════")
        print("                PRISMA FLOW DIAGRAM SUMMARY")
        print("═══════════════════════════════════════════════════════════════\n")
        
        print("IDENTIFICATION:")
        print(f"  Records identified: {self.counts['identification']['total_records']}")
        print(f"  Duplicates removed: {self.counts['identification']['duplicates_removed']}")
        print(f"  After deduplication: {self.counts['identification']['records_after_dedup']}\n")
        
        print("SCREENING:")
        print(f"  Records screened: {self.counts['screening']['records_screened']}")
        print(f"  Records excluded: {self.counts['screening']['records_excluded']}\n")
        
        print("ELIGIBILITY:")
        print(f"  Full-text assessed: {self.counts['eligibility']['full_text_assessed']}")
        print(f"  Full-text excluded: {self.counts['eligibility']['full_text_excluded']}")
        if self.counts['eligibility']['exclusion_reasons']:
            print("  Exclusion reasons:")
            for reason, count in self.counts['eligibility']['exclusion_reasons'].items():
                print(f"    • {reason}: {count}")
        print()
        
        print("INCLUDED:")
        print(f"  Studies in review: {self.counts['included']['studies_included']}\n")
        
        print("═══════════════════════════════════════════════════════════════\n")


def main():
    """Generate PRISMA diagram from screening data."""
    generator = PRISMADiagramGenerator()
    generator.load_from_files()
    generator.print_summary()
    generator.generate_diagram()


if __name__ == "__main__":
    main()
