#!/usr/bin/env python3
"""
Result Exporter

Purpose: Convert Scopus API results to multiple formats (BibTeX, RIS, CSV)
Author: PhD Pipeline Automated Tools
Date: October 2025

Usage:
    python result_exporter.py                  # Export all results
    python result_exporter.py --search ID      # Export specific search
    python result_exporter.py --format bibtex  # Export specific format
"""

import argparse
import csv
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import yaml


class ResultExporter:
    """Export Scopus results to multiple formats"""

    def __init__(self, config_path: str = "../config/scopus_config.yaml"):
        """Initialize exporter with configuration"""
        self.config = self._load_config(config_path)
        self.setup_logging()

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
        self.logger = logging.getLogger('ResultExporter')

    def load_results(self, results_dir: str = "../results") -> List[Dict]:
        """Load all result JSON files from results directory"""
        results_path = Path(results_dir)

        if not results_path.exists():
            self.logger.error(f"Results directory not found: {results_dir}")
            return []

        # Find all JSON files
        json_files = sorted(results_path.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)

        if not json_files:
            self.logger.error("No result files found")
            return []

        # Load results
        all_results = []
        for json_file in json_files:
            with open(json_file, 'r') as f:
                data = json.load(f)
                all_results.append(data)

        self.logger.info(f"Loaded {len(all_results)} result files")
        return all_results

    def export_bibtex(self, results: List[Dict], output_path: Path):
        """Export results to BibTeX format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for result_set in results:
                query_id = result_set['query']['id']

                for idx, entry in enumerate(result_set['results']):
                    # Extract metadata
                    doi = entry.get('prism:doi', '')
                    title = entry.get('dc:title', 'Unknown Title')
                    authors = entry.get('dc:creator', 'Unknown Author')
                    year = entry.get('prism:coverDate', '')[:4] if entry.get('prism:coverDate') else 'Unknown'
                    journal = entry.get('prism:publicationName', 'Unknown')
                    volume = entry.get('prism:volume', '')
                    issue = entry.get('prism:issueIdentifier', '')
                    pages = entry.get('prism:pageRange', '')
                    abstract = entry.get('dc:description', '')
                    eid = entry.get('eid', f'{query_id}_{idx}')

                    # Create BibTeX entry
                    cite_key = f"{query_id}_{eid.replace(':', '_')}"

                    f.write(f"@article{{{cite_key},\n")
                    f.write(f"  title = {{{{{title}}}}},\n")
                    f.write(f"  author = {{{{{authors}}}}},\n")
                    f.write(f"  year = {{{{{year}}}}},\n")
                    f.write(f"  journal = {{{{{journal}}}}},\n")

                    if volume:
                        f.write(f"  volume = {{{{{volume}}}}},\n")
                    if issue:
                        f.write(f"  number = {{{{{issue}}}}},\n")
                    if pages:
                        f.write(f"  pages = {{{{{pages}}}}},\n")
                    if doi:
                        f.write(f"  doi = {{{{{doi}}}}},\n")
                    if abstract:
                        # Clean abstract
                        abstract_clean = abstract.replace('{', '').replace('}', '').replace('\n', ' ')
                        f.write(f"  abstract = {{{{{abstract_clean}}}}},\n")

                    f.write(f"  scopus_id = {{{{{eid}}}}},\n")
                    f.write(f"  query_id = {{{{{query_id}}}}}\n")
                    f.write("}\n\n")

        self.logger.info(f"BibTeX export saved to: {output_path}")

    def export_ris(self, results: List[Dict], output_path: Path):
        """Export results to RIS format (for Zotero, Mendeley, EndNote)"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for result_set in results:
                query_id = result_set['query']['id']

                for entry in result_set['results']:
                    # Extract metadata
                    title = entry.get('dc:title', 'Unknown Title')
                    authors = entry.get('dc:creator', 'Unknown Author')
                    year = entry.get('prism:coverDate', '')[:4] if entry.get('prism:coverDate') else ''
                    journal = entry.get('prism:publicationName', '')
                    volume = entry.get('prism:volume', '')
                    issue = entry.get('prism:issueIdentifier', '')
                    pages = entry.get('prism:pageRange', '')
                    doi = entry.get('prism:doi', '')
                    abstract = entry.get('dc:description', '')
                    url = entry.get('prism:url', '')

                    # RIS format
                    f.write("TY  - JOUR\n")  # Journal article
                    f.write(f"TI  - {title}\n")
                    f.write(f"AU  - {authors}\n")
                    if year:
                        f.write(f"PY  - {year}\n")
                    if journal:
                        f.write(f"JO  - {journal}\n")
                    if volume:
                        f.write(f"VL  - {volume}\n")
                    if issue:
                        f.write(f"IS  - {issue}\n")
                    if pages:
                        f.write(f"SP  - {pages.split('-')[0] if '-' in pages else pages}\n")
                        if '-' in pages:
                            f.write(f"EP  - {pages.split('-')[1]}\n")
                    if doi:
                        f.write(f"DO  - {doi}\n")
                    if abstract:
                        f.write(f"AB  - {abstract}\n")
                    if url:
                        f.write(f"UR  - {url}\n")

                    f.write(f"N1  - Query ID: {query_id}\n")
                    f.write("ER  - \n\n")

        self.logger.info(f"RIS export saved to: {output_path}")

    def export_csv(self, results: List[Dict], output_path: Path):
        """Export results to CSV format (for screening spreadsheet)"""
        rows = []

        for result_set in results:
            query_id = result_set['query']['id']
            query_name = result_set['query']['name']

            for entry in result_set['results']:
                row = {
                    'Query_ID': query_id,
                    'Query_Name': query_name,
                    'EID': entry.get('eid', ''),
                    'DOI': entry.get('prism:doi', ''),
                    'Title': entry.get('dc:title', ''),
                    'Authors': entry.get('dc:creator', ''),
                    'Year': entry.get('prism:coverDate', '')[:4] if entry.get('prism:coverDate') else '',
                    'Journal': entry.get('prism:publicationName', ''),
                    'Volume': entry.get('prism:volume', ''),
                    'Issue': entry.get('prism:issueIdentifier', ''),
                    'Pages': entry.get('prism:pageRange', ''),
                    'Abstract': entry.get('dc:description', ''),
                    'Citations': entry.get('citedby-count', '0'),
                    'URL': entry.get('prism:url', ''),
                    'Title_Screen': '',  # For manual screening
                    'Abstract_Screen': '',
                    'Full_Text_Screen': '',
                    'Exclusion_Reason': '',
                    'Notes': ''
                }
                rows.append(row)

        # Write to CSV
        if rows:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)

            self.logger.info(f"CSV export saved to: {output_path}")
        else:
            self.logger.warning("No data to export to CSV")

    def export_json(self, results: List[Dict], output_path: Path):
        """Export combined results to JSON"""
        # Combine all results
        combined = {
            'export_date': datetime.now().isoformat(),
            'total_searches': len(results),
            'total_results': sum(r['execution']['total_results'] for r in results),
            'searches': results
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(combined, f, indent=2)

        self.logger.info(f"JSON export saved to: {output_path}")

    def export_all_formats(self, results: List[Dict], exports_dir: str = "../exports"):
        """Export to all configured formats"""
        exports_path = Path(exports_dir)
        exports_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        formats = self.config['output'].get('formats', ['bibtex', 'ris', 'csv', 'json'])

        self.logger.info(f"Exporting to {len(formats)} formats...")

        # Calculate total papers
        total_papers = sum(r['execution']['total_results'] for r in results)

        # Export each format
        if 'bibtex' in formats:
            output_path = exports_path / f"all_results_{timestamp}.bib"
            self.export_bibtex(results, output_path)
            print(f"✅ BibTeX: {output_path} ({total_papers} entries)")

        if 'ris' in formats:
            output_path = exports_path / f"all_results_{timestamp}.ris"
            self.export_ris(results, output_path)
            print(f"✅ RIS: {output_path} ({total_papers} entries)")

        if 'csv' in formats:
            output_path = exports_path / f"screening_{timestamp}.csv"
            self.export_csv(results, output_path)
            print(f"✅ CSV: {output_path} ({total_papers} rows)")

        if 'json' in formats:
            output_path = exports_path / f"all_results_{timestamp}.json"
            self.export_json(results, output_path)
            print(f"✅ JSON: {output_path}")

        # Export individual searches
        for result in results:
            query_id = result['query']['id']

            if 'bibtex' in formats:
                output_path = exports_path / f"{query_id}_{timestamp}.bib"
                self.export_bibtex([result], output_path)

            if 'ris' in formats:
                output_path = exports_path / f"{query_id}_{timestamp}.ris"
                self.export_ris([result], output_path)

            if 'csv' in formats:
                output_path = exports_path / f"{query_id}_{timestamp}.csv"
                self.export_csv([result], output_path)

        self.logger.info("All exports complete!")

    def generate_export_report(self, results: List[Dict], reports_dir: str = "../reports"):
        """Generate export summary report"""
        reports_path = Path(reports_dir)
        reports_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        report_path = reports_path / f"export_report_{timestamp}.md"

        with open(report_path, 'w') as f:
            f.write("# Export Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")

            total_papers = sum(r['execution']['total_results'] for r in results)

            f.write(f"## Summary\n\n")
            f.write(f"- **Total Searches:** {len(results)}\n")
            f.write(f"- **Total Papers:** {total_papers}\n")
            f.write(f"- **Export Formats:** {', '.join(self.config['output']['formats'])}\n\n")

            f.write(f"## Searches\n\n")
            for result in results:
                query = result['query']
                f.write(f"### {query['name']} (`{query['id']}`)\n\n")
                f.write(f"- **Results:** {result['execution']['total_results']} papers\n")
                f.write(f"- **Execution Date:** {result['execution']['timestamp']}\n")
                f.write(f"- **API Calls:** {result['execution']['api_calls']}\n\n")

            f.write("## Next Steps\n\n")
            f.write("1. Import results to reference manager (Zotero/Mendeley/EndNote)\n")
            f.write("2. Run deduplication: `python deduplication.py`\n")
            f.write("3. Begin title/abstract screening\n\n")

        self.logger.info(f"Export report saved to: {report_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description="Export Scopus results to multiple formats")
    parser.add_argument('--search', type=str, help='Export specific search by ID')
    parser.add_argument('--format', type=str, choices=['bibtex', 'ris', 'csv', 'json'], help='Export specific format')
    parser.add_argument('--config', type=str, default='../config/scopus_config.yaml', help='Path to config file')

    args = parser.parse_args()

    # Initialize exporter
    exporter = ResultExporter(config_path=args.config)

    print("=" * 60)
    print("Result Exporter")
    print("=" * 60)

    # Load results
    results = exporter.load_results()

    if not results:
        print("❌ No results to export")
        return 1

    # Filter specific search if requested
    if args.search:
        results = [r for r in results if r['query']['id'] == args.search]
        if not results:
            print(f"❌ Search '{args.search}' not found")
            return 1

    # Export
    exporter.export_all_formats(results)

    # Generate report
    exporter.generate_export_report(results)

    print("=" * 60)
    print("✅ Export complete!")
    print("\nNext step: python deduplication.py")
    print("=" * 60)

    return 0


if __name__ == '__main__':
    sys.exit(main())
