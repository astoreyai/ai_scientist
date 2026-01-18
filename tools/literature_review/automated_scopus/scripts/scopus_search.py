#!/usr/bin/env python3
"""
Scopus Search Automation Script

Purpose: Execute systematic literature searches using Scopus API
Author: PhD Pipeline Automated Tools
Date: October 2025

Usage:
    python scopus_search.py                 # Execute all enabled queries
    python scopus_search.py --query ID      # Execute specific query
    python scopus_search.py --dry-run       # Validate without executing
    python scopus_search.py --resume        # Resume interrupted search
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
import yaml


class ScopusSearcher:
    """Main class for Scopus API search automation"""

    def __init__(self, config_path: str = "../config/scopus_config.yaml"):
        """Initialize searcher with configuration"""
        self.config = self._load_config(config_path)
        self.api_key = self.config['scopus']['api_key']
        self.base_url = self.config['scopus']['base_url']
        self.setup_logging()
        self.api_calls_count = 0
        self.start_time = datetime.now()

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def setup_logging(self):
        """Setup logging to file and console"""
        log_config = self.config['logging']
        log_dir = Path(self.config['output']['logs_dir'])
        log_dir.mkdir(parents=True, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger('ScopusSearcher')
        self.logger.setLevel(getattr(logging, log_config['level']))

        # File handler
        if log_config['log_to_file']:
            log_file = log_dir / f"scopus_search_{datetime.now().strftime('%Y-%m-%d')}.log"
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging.Formatter(
                log_config['format'],
                datefmt=log_config['date_format']
            ))
            self.logger.addHandler(fh)

        # Console handler
        if log_config['log_to_console']:
            ch = logging.StreamHandler()
            ch.setLevel(getattr(logging, log_config['level']))
            ch.setFormatter(logging.Formatter(
                log_config['format'],
                datefmt=log_config['date_format']
            ))
            self.logger.addHandler(ch)

    def load_queries(self, queries_path: str = "../config/search_queries.yaml") -> List[Dict]:
        """Load search queries from YAML file"""
        with open(queries_path, 'r') as f:
            data = yaml.safe_load(f)

        queries = data['searches']

        # Filter enabled queries if configured
        if data.get('config', {}).get('execute_enabled_only', True):
            queries = [q for q in queries if q.get('enabled', True)]

        self.logger.info(f"Loaded {len(queries)} enabled queries")
        return queries

    def validate_query(self, query: Dict) -> Tuple[bool, str]:
        """Validate query syntax and configuration"""
        # Check required fields
        required = ['id', 'name', 'query']
        for field in required:
            if field not in query:
                return False, f"Missing required field: {field}"

        # Check API key
        if self.api_key == "YOUR_API_KEY_HERE":
            return False, "API key not configured in scopus_config.yaml"

        # Basic query syntax check
        query_str = query['query'].strip()
        if not query_str:
            return False, "Query string is empty"

        return True, "Valid"

    def build_query_params(self, query: Dict, start: int = 0) -> Dict:
        """Build API query parameters from query configuration"""
        params = {
            'apiKey': self.api_key,
            'query': query['query'].strip(),
            'count': self.config['scopus']['max_results_per_request'],
            'start': start,
            'view': 'COMPLETE'  # Get all metadata
        }

        # Add date range if specified
        if 'date_range' in query:
            dr = query['date_range']
            if 'start' in dr and 'end' in dr:
                params['date'] = f"{dr['start']}-{dr['end']}"

        # Add subject areas if specified
        if 'subject_areas' in query and query['subject_areas']:
            params['subj'] = ','.join(query['subject_areas'])

        # Add document types if specified
        if 'document_types' in query and query['document_types']:
            # Convert to Scopus format
            doc_types = ' OR '.join([f'DOCTYPE({dt})' for dt in query['document_types']])
            params['query'] += f' AND ({doc_types})'

        return params

    def execute_search(self, query: Dict, dry_run: bool = False) -> Optional[Dict]:
        """Execute a single search query with pagination"""
        query_id = query['id']
        self.logger.info(f"Executing query {query_id}: {query['name']}")

        # Validate query
        valid, msg = self.validate_query(query)
        if not valid:
            self.logger.error(f"Query validation failed: {msg}")
            return None

        if dry_run:
            self.logger.info("DRY RUN - Query would be executed with parameters:")
            params = self.build_query_params(query, start=0)
            self.logger.info(json.dumps(params, indent=2))
            return None

        # Execute search with pagination
        all_results = []
        start = 0
        total_results = None
        page = 1

        while True:
            params = self.build_query_params(query, start=start)

            self.logger.debug(f"API call {self.api_calls_count + 1}: start={start}")

            # Execute API request with retry logic
            response_data = self._api_request_with_retry(params)

            if response_data is None:
                self.logger.error(f"Failed to retrieve results for query {query_id}")
                break

            self.api_calls_count += 1

            # Parse response
            search_results = response_data.get('search-results', {})

            # Get total results on first page
            if total_results is None:
                total_results = int(search_results.get('opensearch:totalResults', 0))
                self.logger.info(f"Total results: {total_results}")

                if total_results == 0:
                    self.logger.warning(f"No results found for query {query_id}")
                    break

            # Extract entries
            entries = search_results.get('entry', [])
            all_results.extend(entries)

            self.logger.info(f"Page {page}: Retrieved {len(entries)} results (Total: {len(all_results)}/{total_results})")

            # Check if we have all results
            if len(all_results) >= total_results:
                break

            # Move to next page
            start += self.config['scopus']['max_results_per_request']
            page += 1

            # Small delay to be nice to API
            time.sleep(0.5)

        # Save results
        if all_results:
            result_data = {
                'query': query,
                'execution': {
                    'timestamp': datetime.now().isoformat(),
                    'total_results': len(all_results),
                    'api_calls': self.api_calls_count
                },
                'results': all_results
            }

            self._save_results(query_id, result_data)

            self.logger.info(f"Successfully retrieved {len(all_results)} results for query {query_id}")
            return result_data

        return None

    def _api_request_with_retry(self, params: Dict) -> Optional[Dict]:
        """Execute API request with retry logic"""
        max_retries = self.config['scopus']['max_retries']
        retry_delay = self.config['scopus']['retry_delay']
        timeout = self.config['scopus']['timeout']

        for attempt in range(max_retries):
            try:
                response = requests.get(
                    self.base_url,
                    params=params,
                    timeout=timeout,
                    headers={'Accept': 'application/json'}
                )

                # Check response status
                if response.status_code == 200:
                    return response.json()

                elif response.status_code == 429:
                    # Rate limit exceeded
                    self.logger.warning(f"Rate limit exceeded. Waiting {retry_delay * (attempt + 1)} seconds...")
                    time.sleep(retry_delay * (attempt + 1))
                    continue

                elif response.status_code == 401:
                    self.logger.error("Authentication failed. Check API key.")
                    return None

                elif response.status_code == 400:
                    self.logger.error(f"Bad request. Response: {response.text}")
                    return None

                else:
                    self.logger.warning(f"Unexpected status code: {response.status_code}")
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                    return None

            except requests.exceptions.Timeout:
                self.logger.warning(f"Request timeout. Attempt {attempt + 1}/{max_retries}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                return None

            except requests.exceptions.RequestException as e:
                self.logger.error(f"Request error: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                return None

        self.logger.error("Max retries exceeded")
        return None

    def _save_results(self, query_id: str, result_data: Dict):
        """Save results to JSON file"""
        results_dir = Path(self.config['output']['results_dir'])
        results_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime(self.config['output']['timestamp_format'])
        filename = f"{query_id}_{timestamp}.json"
        filepath = results_dir / filename

        with open(filepath, 'w') as f:
            json.dump(result_data, f, indent=2)

        self.logger.info(f"Results saved to: {filepath}")

    def generate_search_log(self, queries: List[Dict], results: List[Dict]):
        """Generate comprehensive search log"""
        logs_dir = Path(self.config['output']['logs_dir'])
        logs_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d")
        log_path = logs_dir / f"search_log_{timestamp}.md"

        with open(log_path, 'w') as f:
            f.write("# Scopus Search Execution Log\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Execution Duration:** {(datetime.now() - self.start_time).total_seconds():.1f} seconds\n\n")
            f.write(f"**Total API Calls:** {self.api_calls_count}\n\n")
            f.write("---\n\n")

            total_results = 0

            for i, query in enumerate(queries):
                f.write(f"## Search {i + 1}: {query['name']}\n\n")
                f.write(f"**Query ID:** `{query['id']}`\n\n")
                f.write(f"**Description:** {query.get('description', 'N/A')}\n\n")
                f.write(f"**Query String:**\n```\n{query['query']}\n```\n\n")

                # Date range
                if 'date_range' in query:
                    dr = query['date_range']
                    f.write(f"**Date Range:** {dr.get('start', 'N/A')} - {dr.get('end', 'N/A')}\n\n")

                # Subject areas
                if 'subject_areas' in query:
                    f.write(f"**Subject Areas:** {', '.join(query['subject_areas'])}\n\n")

                # Results
                result = next((r for r in results if r and r['query']['id'] == query['id']), None)
                if result:
                    count = result['execution']['total_results']
                    total_results += count
                    f.write(f"**Results:** {count} papers\n\n")
                    f.write(f"**API Calls:** {result['execution']['api_calls']}\n\n")
                    f.write(f"**Timestamp:** {result['execution']['timestamp']}\n\n")
                else:
                    f.write(f"**Results:** Failed or skipped\n\n")

                # Research questions
                if 'research_questions' in query:
                    f.write(f"**Research Questions:**\n")
                    for rq in query['research_questions']:
                        f.write(f"- {rq}\n")
                    f.write("\n")

                f.write("---\n\n")

            f.write(f"## Summary\n\n")
            f.write(f"**Total Queries Executed:** {len([r for r in results if r is not None])}\n\n")
            f.write(f"**Total Results Retrieved:** {total_results} papers\n\n")
            f.write(f"**Total API Calls:** {self.api_calls_count}\n\n")
            f.write(f"**Average Results per Query:** {total_results / max(len(queries), 1):.1f}\n\n")

        self.logger.info(f"Search log saved to: {log_path}")

    def check_quota_usage(self):
        """Check and warn about API quota usage"""
        quota_limit = self.config['scopus']['quota_limit']
        warning_threshold = self.config['scopus']['quota_warning_threshold']

        usage_percent = (self.api_calls_count / quota_limit) * 100

        if usage_percent > warning_threshold * 100:
            self.logger.warning(f"API quota usage: {usage_percent:.1f}% ({self.api_calls_count}/{quota_limit} calls)")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Execute Scopus literature searches using API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scopus_search.py                    # Execute all enabled queries
  python scopus_search.py --query search_001 # Execute specific query
  python scopus_search.py --dry-run          # Validate without executing
  python scopus_search.py --resume           # Resume interrupted search
        """
    )

    parser.add_argument('--query', type=str, help='Execute specific query by ID')
    parser.add_argument('--dry-run', action='store_true', help='Validate queries without executing')
    parser.add_argument('--resume', action='store_true', help='Resume interrupted search')
    parser.add_argument('--config', type=str, default='../config/scopus_config.yaml', help='Path to config file')
    parser.add_argument('--queries', type=str, default='../config/search_queries.yaml', help='Path to queries file')

    args = parser.parse_args()

    # Initialize searcher
    searcher = ScopusSearcher(config_path=args.config)
    searcher.logger.info("=" * 60)
    searcher.logger.info("Scopus Search Pipeline Starting")
    searcher.logger.info("=" * 60)

    # Load queries
    queries = searcher.load_queries(queries_path=args.queries)

    if not queries:
        searcher.logger.error("No queries found or all queries disabled")
        return 1

    # Filter specific query if requested
    if args.query:
        queries = [q for q in queries if q['id'] == args.query]
        if not queries:
            searcher.logger.error(f"Query '{args.query}' not found")
            return 1

    # Execute searches
    results = []
    for query in queries:
        result = searcher.execute_search(query, dry_run=args.dry_run)
        results.append(result)

        # Check quota usage
        searcher.check_quota_usage()

    if not args.dry_run:
        # Generate search log
        searcher.generate_search_log(queries, results)

        # Summary
        successful = len([r for r in results if r is not None])
        total_papers = sum(r['execution']['total_results'] for r in results if r is not None)

        searcher.logger.info("=" * 60)
        searcher.logger.info("Search Pipeline Complete")
        searcher.logger.info(f"Queries Executed: {successful}/{len(queries)}")
        searcher.logger.info(f"Total Papers Retrieved: {total_papers}")
        searcher.logger.info(f"Total API Calls: {searcher.api_calls_count}")
        searcher.logger.info("=" * 60)

        # Next steps
        print("\n" + "=" * 60)
        print("✅ Search complete! Next steps:")
        print("1. Run: python result_exporter.py")
        print("2. Run: python deduplication.py")
        print("3. Import results to reference manager")
        print("=" * 60)

    return 0


if __name__ == '__main__':
    sys.exit(main())
