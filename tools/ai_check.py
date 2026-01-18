#!/usr/bin/env python3
"""
CLI tool for AI-generated text detection.

Usage:
    python tools/ai_check.py path/to/file.md
    python tools/ai_check.py --directory docs/
    python tools/ai_check.py --format html --output report.html
"""
import argparse
import sys
from pathlib import Path

# Add support library to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "support"))

from ai_detection.detector import AITextDetector
from ai_detection.config import AICheckConfig
from ai_detection.suggestions import SuggestionGenerator
from ai_detection.tracker import AICheckTracker


def format_markdown_report(result, suggestions):
    """Format detection result as markdown."""
    report = []
    report.append(f"# AI-Check Report: {result.file_path}")
    report.append(f"\n**Date:** {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"\n## Overall Assessment\n")
    report.append(f"**Confidence Score:** {result.overall_confidence:.1%}")
    
    if result.overall_confidence >= 0.70:
        report.append("**Status:** 🚫 HIGH - Likely AI-generated")
    elif result.overall_confidence >= 0.30:
        report.append("**Status:** ⚠️ MEDIUM - Possible AI assistance")
    else:
        report.append("**Status:** ✅ LOW - Appears human-written")
    
    report.append(f"\n## Metric Breakdown\n")
    report.append(f"- Grammar Perfection: {result.grammar_score:.1f}%")
    report.append(f"- Sentence Uniformity: {result.sentence_score:.1f}%")
    report.append(f"- Paragraph Structure: {result.paragraph_score:.1f}%")
    report.append(f"- AI-Typical Words: {result.word_frequency_score:.1f}%")
    report.append(f"- Punctuation Patterns: {result.punctuation_score:.1f}%")
    
    if result.ai_words_found:
        report.append(f"\n## AI-Typical Words Found\n")
        for word, count in sorted(result.ai_words_found.items(), key=lambda x: x[1], reverse=True)[:10]:
            report.append(f"- **{word}**: {count} occurrences")
        report.append(f"\n**Total:** {result.ai_words_per_1000:.1f} AI-typical words per 1000 words")
        report.append(f"(Human baseline: ~1.5 per 1000)")
    
    if result.flagged_sections:
        report.append(f"\n## Flagged Sections\n")
        for section in result.flagged_sections[:5]:
            report.append(f"\n### Lines {section.start_line}-{section.end_line} ({section.confidence:.1%} confidence)")
            report.append(f"**Patterns:** {', '.join(section.patterns)}")
            if section.ai_words:
                report.append(f"**AI Words:** {', '.join(section.ai_words)}")
    
    if suggestions:
        report.append(f"\n## Suggestions for Improvement\n")
        for i, sug in enumerate(suggestions, 1):
            report.append(f"\n### {i}. {sug.issue}")
            report.append(f"**{sug.suggestion}**")
            if sug.example_before and sug.example_after:
                report.append(f"\n❌ Before: `{sug.example_before}`")
                report.append(f"✅ After: `{sug.example_after}`")
    
    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="AI-generated text detection tool")
    parser.add_argument("path", help="File or directory to check")
    parser.add_argument("--config", help="Path to config file", default=".ai-check-config.yaml")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", help="Output file path (default: stdout)")
    parser.add_argument("--track", action="store_true", help="Track results in history database")
    
    args = parser.parse_args()
    
    # Load configuration
    config_path = Path(args.config)
    config = AICheckConfig(str(config_path) if config_path.exists() else None)
    
    # Initialize components
    detector = AITextDetector(config)
    suggestion_gen = SuggestionGenerator()
    tracker = AICheckTracker() if args.track else None
    
    # Process file(s)
    path = Path(args.path)
    
    if path.is_file():
        files_to_check = [path]
    elif path.is_dir():
        files_to_check = list(path.glob("**/*.md")) + list(path.glob("**/*.tex"))
    else:
        print(f"Error: {path} not found", file=sys.stderr)
        return 1
    
    # Generate reports
    for file_path in files_to_check:
        with open(file_path, 'r') as f:
            text = f.read()
        
        result = detector.analyze(text, str(file_path))
        suggestions = suggestion_gen.generate_suggestions(result)
        
        if args.format == "markdown":
            report = format_markdown_report(result, suggestions)
        else:  # json
            import json
            report = json.dumps(result.to_dict(), indent=2)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
        else:
            print(report)
        
        if tracker:
            tracker.log_detection(result)
            print(f"\nResults logged to history database")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
