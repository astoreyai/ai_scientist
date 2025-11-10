#!/usr/bin/env python3
"""
Pre-commit hook to detect AI-generated text in staged files.
Blocks commits with high AI-confidence scores.
"""
import json
import sys
import subprocess
from pathlib import Path

# Add support library to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "support"))

try:
    from ai_detection.detector import AITextDetector
    from ai_detection.config import AICheckConfig
except ImportError:
    # Gracefully fail if library not available
    print("Warning: AI-check library not found, skipping AI detection", file=sys.stderr)
    sys.exit(0)


def get_staged_files():
    """Get list of staged files from git."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except subprocess.CalledProcessError:
        return []


def should_check_file(file_path: str, config: AICheckConfig) -> bool:
    """Determine if file should be checked for AI patterns."""
    # Check file extension
    relevant_extensions = ['.md', '.tex', '.rst', '.txt']
    if not any(file_path.endswith(ext) for ext in relevant_extensions):
        return False
    
    # Check exclude patterns (if configured)
    exclude_patterns = ['examples/', 'tests/', 'node_modules/', '.venv/']
    if any(pattern in file_path for pattern in exclude_patterns):
        return False
    
    return True


def main():
    """Main pre-commit hook logic."""
    # Load configuration
    config_path = project_root / ".ai-check-config.yaml"
    config = AICheckConfig(str(config_path) if config_path.exists() else None)
    
    # Get staged files
    staged_files = get_staged_files()
    
    if not staged_files:
        sys.exit(0)  # No files to check
    
    # Filter files to check
    files_to_check = [f for f in staged_files if should_check_file(f, config)]
    
    if not files_to_check:
        sys.exit(0)  # No relevant files
    
    # Initialize detector
    detector = AITextDetector(config)
    
    # Track results
    high_confidence_files = []
    medium_confidence_files = []
    
    for file_path in files_to_check:
        full_path = project_root / file_path
        
        if not full_path.exists():
            continue
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
            continue
        
        # Run detection
        result = detector.analyze(text, file_path)
        
        # Check thresholds
        block_threshold = config.thresholds.get("block_threshold", 0.70)
        warn_threshold = config.thresholds.get("warn_threshold", 0.30)
        
        if result.overall_confidence >= block_threshold:
            high_confidence_files.append((file_path, result))
        elif result.overall_confidence >= warn_threshold:
            medium_confidence_files.append((file_path, result))
    
    # Report findings
    exit_code = 0
    
    if high_confidence_files:
        print("\n" + "="*60, file=sys.stderr)
        print("🚫 AI-GENERATED TEXT DETECTED (HIGH CONFIDENCE)", file=sys.stderr)
        print("="*60 + "\n", file=sys.stderr)
        
        for file_path, result in high_confidence_files:
            print(f"📄 {file_path}:", file=sys.stderr)
            print(f"   Confidence: {result.overall_confidence:.1%} (BLOCKING)", file=sys.stderr)
            print(f"   AI words: {result.ai_words_per_1000:.1f} per 1000 words", file=sys.stderr)
            
            if result.patterns_detected:
                print(f"   Patterns: {', '.join(result.patterns_detected[:3])}", file=sys.stderr)
            
            if result.ai_words_found:
                top_words = list(result.ai_words_found.keys())[:5]
                print(f"   AI-typical words: {', '.join(top_words)}", file=sys.stderr)
            
            print(file=sys.stderr)
        
        print("❌ COMMIT BLOCKED", file=sys.stderr)
        print("\nPlease revise the flagged files to use more natural writing.", file=sys.stderr)
        print("Review AI-typical words and apply suggestions from ai-check skill.", file=sys.stderr)
        print("\nTo override this check, use: git commit --no-verify", file=sys.stderr)
        print("="*60 + "\n", file=sys.stderr)
        
        exit_code = 2  # Block commit
    
    if medium_confidence_files and exit_code == 0:
        print("\n" + "="*60, file=sys.stderr)
        print("⚠️  POSSIBLE AI PATTERNS DETECTED (MEDIUM CONFIDENCE)", file=sys.stderr)
        print("="*60 + "\n", file=sys.stderr)
        
        for file_path, result in medium_confidence_files:
            print(f"📄 {file_path}:", file=sys.stderr)
            print(f"   Confidence: {result.overall_confidence:.1%} (WARNING)", file=sys.stderr)
            
            if result.ai_words_found:
                top_words = list(result.ai_words_found.keys())[:3]
                print(f"   AI-typical words: {', '.join(top_words)}", file=sys.stderr)
            
            print(file=sys.stderr)
        
        print("⚠️  COMMIT ALLOWED (with warnings)", file=sys.stderr)
        print("\nConsider reviewing these files for AI patterns.", file=sys.stderr)
        print("Run 'python tools/ai_check.py <file>' for detailed analysis.", file=sys.stderr)
        print("="*60 + "\n", file=sys.stderr)
        
        # Allow commit with warnings (exit 0)
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
