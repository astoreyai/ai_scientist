#!/usr/bin/env python3
"""
Deduplication Script

Purpose: Find and remove duplicate papers from literature search results
Author: PhD Pipeline Automated Tools
Date: October 2025

Usage:
    python deduplication.py              # Run deduplication
    python deduplication.py --review     # Review flagged duplicates
"""

import argparse
import csv
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


class Deduplicator:
    """Find and remove duplicate papers"""

    def __init__(self, config_path: str = "../config/scopus_config.yaml"):
        """Initialize deduplicator with configuration"""
        self.config = self._load_config(config_path)
        self.setup_logging()
        self.duplicates = []

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def setup_logging(self):
        """Setup logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger('Deduplicator')

    def load_all_papers(self, exports_dir: str = "../exports") -> List[Dict]:
        """Load all papers from exported CSV files"""
        exports_path = Path(exports_dir)

        if not exports_path.exists():
            self.logger.error(f"Exports directory not found: {exports_dir}")
            return []

        # Find most recent screening CSV
        csv_files = sorted(exports_path.glob("screening_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)

        if not csv_files:
            self.logger.error("No screening CSV files found. Run result_exporter.py first.")
            return []

        csv_file = csv_files[0]
        self.logger.info(f"Loading papers from: {csv_file}")

        papers = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                papers.append(row)

        self.logger.info(f"Loaded {len(papers)} papers")
        return papers

    def normalize_string(self, s: str) -> str:
        """Normalize string for comparison"""
        if not s:
            return ""
        # Convert to lowercase, remove punctuation, strip whitespace
        import re
        s = s.lower()
        s = re.sub(r'[^\w\s]', '', s)
        s = ' '.join(s.split())
        return s

    def fuzzy_match(self, s1: str, s2: str) -> float:
        """Calculate fuzzy match score (0-100)"""
        from difflib import SequenceMatcher
        s1_norm = self.normalize_string(s1)
        s2_norm = self.normalize_string(s2)

        if not s1_norm or not s2_norm:
            return 0.0

        return SequenceMatcher(None, s1_norm, s2_norm).ratio() * 100

    def find_duplicates_doi(self, papers: List[Dict]) -> List[Tuple[int, int, str]]:
        """Find duplicates by exact DOI match"""
        doi_map = {}
        duplicates = []

        for idx, paper in enumerate(papers):
            doi = paper.get('DOI', '').strip()
            if not doi:
                continue

            doi_lower = doi.lower()

            if doi_lower in doi_map:
                original_idx = doi_map[doi_lower]
                duplicates.append((original_idx, idx, 'doi_exact'))
                self.logger.debug(f"DOI duplicate: {papers[original_idx]['Title'][:50]}...")
            else:
                doi_map[doi_lower] = idx

        return duplicates

    def find_duplicates_title_author(self, papers: List[Dict]) -> List[Tuple[int, int, str]]:
        """Find duplicates by title + first author match"""
        title_author_map = {}
        duplicates = []

        for idx, paper in enumerate(papers):
            title = self.normalize_string(paper.get('Title', ''))
            authors = paper.get('Authors', '')

            if not title or not authors:
                continue

            # Get first author
            first_author = authors.split(',')[0].strip() if ',' in authors else authors.split(';')[0].strip()
            first_author_norm = self.normalize_string(first_author)

            key = f"{title}___{first_author_norm}"

            if key in title_author_map:
                original_idx = title_author_map[key]
                duplicates.append((original_idx, idx, 'title_author'))
                self.logger.debug(f"Title+Author duplicate: {paper['Title'][:50]}...")
            else:
                title_author_map[key] = idx

        return duplicates

    def find_duplicates_fuzzy_title(self, papers: List[Dict]) -> List[Tuple[int, int, str, float]]:
        """Find duplicates by fuzzy title match"""
        threshold = self.config['deduplication']['fuzzy_threshold']
        duplicates = []

        # Compare each paper with all subsequent papers
        for i in range(len(papers)):
            title_i = papers[i].get('Title', '')
            if not title_i:
                continue

            for j in range(i + 1, len(papers)):
                title_j = papers[j].get('Title', '')
                if not title_j:
                    continue

                # Calculate fuzzy match score
                score = self.fuzzy_match(title_i, title_j)

                if score >= threshold:
                    duplicates.append((i, j, 'title_fuzzy', score))
                    self.logger.debug(f"Fuzzy duplicate ({score:.1f}%): {title_i[:50]}...")

        return duplicates

    def deduplicate(self, papers: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
        """Perform deduplication using all strategies"""
        self.logger.info("Finding duplicates...")

        # Track duplicate indices
        duplicate_indices = set()
        all_duplicates = []

        # Strategy 1: Exact DOI match
        doi_duplicates = self.find_duplicates_doi(papers)
        for orig_idx, dup_idx, strategy in doi_duplicates:
            duplicate_indices.add(dup_idx)
            all_duplicates.append({
                'original_idx': orig_idx,
                'duplicate_idx': dup_idx,
                'strategy': strategy,
                'confidence': 'high',
                'original_title': papers[orig_idx]['Title'],
                'duplicate_title': papers[dup_idx]['Title'],
                'original_doi': papers[orig_idx].get('DOI', ''),
                'duplicate_doi': papers[dup_idx].get('DOI', '')
            })

        self.logger.info(f"Found {len(doi_duplicates)} exact DOI duplicates")

        # Strategy 2: Title + Author match
        title_author_duplicates = self.find_duplicates_title_author(papers)
        for orig_idx, dup_idx, strategy in title_author_duplicates:
            if dup_idx not in duplicate_indices:  # Avoid double-counting
                duplicate_indices.add(dup_idx)
                all_duplicates.append({
                    'original_idx': orig_idx,
                    'duplicate_idx': dup_idx,
                    'strategy': strategy,
                    'confidence': 'high',
                    'original_title': papers[orig_idx]['Title'],
                    'duplicate_title': papers[dup_idx]['Title'],
                    'original_authors': papers[orig_idx].get('Authors', ''),
                    'duplicate_authors': papers[dup_idx].get('Authors', '')
                })

        self.logger.info(f"Found {len(title_author_duplicates)} title+author duplicates")

        # Strategy 3: Fuzzy title match (requires review)
        if 'title_fuzzy' in self.config['deduplication']['strategies']:
            fuzzy_duplicates = self.find_duplicates_fuzzy_title(papers)
            for orig_idx, dup_idx, strategy, score in fuzzy_duplicates:
                if dup_idx not in duplicate_indices:  # Avoid double-counting
                    duplicate_indices.add(dup_idx)
                    all_duplicates.append({
                        'original_idx': orig_idx,
                        'duplicate_idx': dup_idx,
                        'strategy': strategy,
                        'confidence': 'medium',
                        'match_score': score,
                        'original_title': papers[orig_idx]['Title'],
                        'duplicate_title': papers[dup_idx]['Title'],
                        'needs_review': True
                    })

            self.logger.info(f"Found {len(fuzzy_duplicates)} fuzzy title matches (review recommended)")

        # Create deduplicated list
        unique_papers = [p for i, p in enumerate(papers) if i not in duplicate_indices]

        self.logger.info(f"Total duplicates found: {len(duplicate_indices)} ({len(duplicate_indices)/len(papers)*100:.1f}%)")
        self.logger.info(f"Unique papers: {len(unique_papers)}")

        self.duplicates = all_duplicates

        return unique_papers, all_duplicates

    def save_deduplication_report(self, papers: List[Dict], unique_papers: List[Dict],
                                   duplicates: List[Dict], reports_dir: str = "../reports"):
        """Generate deduplication report"""
        reports_path = Path(reports_dir)
        reports_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        report_path = reports_path / f"deduplication_report_{timestamp}.md"

        with open(report_path, 'w') as f:
            f.write("# Deduplication Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")

            f.write("## Summary\n\n")
            f.write(f"- **Original Papers:** {len(papers)}\n")
            f.write(f"- **Duplicates Found:** {len(duplicates)} ({len(duplicates)/len(papers)*100:.1f}%)\n")
            f.write(f"- **Unique Papers:** {len(unique_papers)}\n\n")

            f.write("### Duplicates by Strategy\n\n")
            strategies = {}
            for dup in duplicates:
                strategy = dup['strategy']
                strategies[strategy] = strategies.get(strategy, 0) + 1

            for strategy, count in strategies.items():
                f.write(f"- **{strategy}:** {count} duplicates\n")

            f.write("\n## Duplicate Details\n\n")

            # Group by strategy
            for strategy in ['doi_exact', 'title_author', 'title_fuzzy']:
                strategy_dups = [d for d in duplicates if d['strategy'] == strategy]
                if not strategy_dups:
                    continue

                f.write(f"### {strategy.replace('_', ' ').title()} ({len(strategy_dups)} duplicates)\n\n")

                for i, dup in enumerate(strategy_dups[:10], 1):  # Show first 10
                    f.write(f"#### Duplicate {i}\n\n")
                    f.write(f"**Original (kept):** {dup['original_title'][:100]}\n\n")
                    f.write(f"**Duplicate (removed):** {dup['duplicate_title'][:100]}\n\n")

                    if 'match_score' in dup:
                        f.write(f"**Match Score:** {dup['match_score']:.1f}%\n\n")

                    if dup.get('needs_review'):
                        f.write("⚠️ **Needs Manual Review**\n\n")

                    f.write("---\n\n")

                if len(strategy_dups) > 10:
                    f.write(f"*... and {len(strategy_dups) - 10} more*\n\n")

            f.write("## Next Steps\n\n")
            f.write("1. Review duplicates marked for manual review\n")
            f.write("2. Import deduplicated results to reference manager\n")
            f.write("3. Begin title/abstract screening\n\n")

        self.logger.info(f"Deduplication report saved to: {report_path}")

        # Save CSV of duplicates
        csv_path = reports_path / f"duplicates_{timestamp}.csv"
        if duplicates:
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=duplicates[0].keys())
                writer.writeheader()
                writer.writerows(duplicates)

            self.logger.info(f"Duplicates CSV saved to: {csv_path}")

    def save_deduplicated_exports(self, unique_papers: List[Dict], exports_dir: str = "../exports"):
        """Save deduplicated exports"""
        dedupe_dir = Path(exports_dir) / "deduplicated"
        dedupe_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d")

        # Save CSV
        csv_path = dedupe_dir / f"screening_deduplicated_{timestamp}.csv"
        if unique_papers:
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=unique_papers[0].keys())
                writer.writeheader()
                writer.writerows(unique_papers)

            self.logger.info(f"Deduplicated screening CSV saved to: {csv_path}")

        # TODO: Could also regenerate BibTeX and RIS from unique papers


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description="Deduplicate literature search results")
    parser.add_argument('--review', action='store_true', help='Review flagged duplicates')
    parser.add_argument('--config', type=str, default='../config/scopus_config.yaml', help='Path to config file')

    args = parser.parse_args()

    # Initialize deduplicator
    deduplicator = Deduplicator(config_path=args.config)

    print("=" * 60)
    print("Deduplication")
    print("=" * 60)

    # Load papers
    papers = deduplicator.load_all_papers()

    if not papers:
        print("❌ No papers to deduplicate")
        return 1

    # Deduplicate
    unique_papers, duplicates = deduplicator.deduplicate(papers)

    # Generate report
    deduplicator.save_deduplication_report(papers, unique_papers, duplicates)

    # Save deduplicated exports
    if deduplicator.config['deduplication']['export_deduplicated']:
        deduplicator.save_deduplicated_exports(unique_papers)

    # Summary
    print("=" * 60)
    print("✅ Deduplication complete!")
    print(f"\nOriginal papers: {len(papers)}")
    print(f"Duplicates found: {len(duplicates)} ({len(duplicates)/len(papers)*100:.1f}%)")
    print(f"Unique papers: {len(unique_papers)}")
    print("\nReports saved to: ../reports/")
    print("Deduplicated exports saved to: ../exports/deduplicated/")
    print("=" * 60)

    # Check if manual review needed
    needs_review = [d for d in duplicates if d.get('needs_review')]
    if needs_review:
        print(f"\n⚠️  {len(needs_review)} duplicates flagged for manual review")
        print("Check: ../reports/duplicates_*.csv")

    return 0


if __name__ == '__main__':
    sys.exit(main())
