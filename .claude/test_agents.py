#!/usr/bin/env python3
"""
Agent Specification Testing

Tests all 10 research agents for completeness, validity, and compliance with
agent specification standards.

Run: python3 test_agents.py
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

print("=" * 80)
print("AGENT SPECIFICATION TESTING")
print("=" * 80)
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Test results storage
results = {
    "timestamp": datetime.now().isoformat(),
    "agents_tested": 0,
    "tests": []
}

def test_result(agent_name, test_name, status, details):
    """Record test result"""
    result = {
        "agent": agent_name,
        "test": test_name,
        "status": status,
        "details": details
    }
    results["tests"].append(result)

    status_symbol = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
    print(f"{status_symbol} {agent_name} - {test_name}: {details}")

# Expected agents
EXPECTED_AGENTS = [
    # Phase 2 agents (existing)
    "literature-reviewer",
    "experiment-designer",
    "data-analyst",
    "hypothesis-generator",
    "citation-manager",
    # Phase 4 agents (new)
    "gap-analyst",
    "manuscript-writer",
    "meta-reviewer",
    "quality-assurance",
    "code-reviewer"
]

# Agent directory
AGENTS_DIR = Path(".claude/agents")

# Test 1: Agent Files Exist
print("Test 1: Agent File Existence")
print("-" * 80)

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if agent_file.exists():
        test_result(agent_name, "File Exists", "PASS", f"Found at {agent_file}")
        results["agents_tested"] += 1
    else:
        test_result(agent_name, "File Exists", "FAIL", f"Not found: {agent_file}")

print()

# Test 2: YAML Frontmatter Validation
print("Test 2: YAML Frontmatter Validation")
print("-" * 80)

REQUIRED_FRONTMATTER_FIELDS = ["name", "description", "tools", "model", "color"]

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "YAML Frontmatter", "SKIP", "File not found")
        continue

    with open(agent_file, 'r') as f:
        content = f.read()

    # Extract YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)

    if not match:
        test_result(agent_name, "YAML Frontmatter", "FAIL", "No YAML frontmatter found")
        continue

    try:
        frontmatter = yaml.safe_load(match.group(1))

        # Check required fields
        missing_fields = [field for field in REQUIRED_FRONTMATTER_FIELDS if field not in frontmatter]

        if missing_fields:
            test_result(agent_name, "YAML Frontmatter", "FAIL",
                       f"Missing fields: {', '.join(missing_fields)}")
        else:
            # Validate name matches filename
            if frontmatter["name"] != agent_name:
                test_result(agent_name, "YAML Frontmatter", "FAIL",
                           f"Name mismatch: {frontmatter['name']} != {agent_name}")
            else:
                test_result(agent_name, "YAML Frontmatter", "PASS",
                           f"All required fields present")

    except yaml.YAMLError as e:
        test_result(agent_name, "YAML Frontmatter", "FAIL", f"YAML parsing error: {e}")

print()

# Test 3: Content Structure
print("Test 3: Content Structure Validation")
print("-" * 80)

REQUIRED_SECTIONS = [
    "Core Responsibilities",
    "Mode-Specific Behaviors",
    "Output Files",
    "Quality Standards"
]

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "Content Structure", "SKIP", "File not found")
        continue

    with open(agent_file, 'r') as f:
        content = f.read()

    # Check for required sections
    missing_sections = []
    for section in REQUIRED_SECTIONS:
        # Check for heading with section name
        if not re.search(rf'## {re.escape(section)}', content):
            missing_sections.append(section)

    if missing_sections:
        test_result(agent_name, "Content Structure", "FAIL",
                   f"Missing sections: {', '.join(missing_sections)}")
    else:
        test_result(agent_name, "Content Structure", "PASS",
                   "All required sections present")

print()

# Test 4: Mode Behavior Specification
print("Test 4: Mode Behavior Specification")
print("-" * 80)

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "Mode Behaviors", "SKIP", "File not found")
        continue

    with open(agent_file, 'r') as f:
        content = f.read()

    # Check for both ASSISTANT and AUTONOMOUS mode specifications
    has_assistant = bool(re.search(r'\*\*ASSISTANT Mode[:\*]', content, re.IGNORECASE))
    has_autonomous = bool(re.search(r'\*\*AUTONOMOUS Mode[:\*]', content, re.IGNORECASE))

    if has_assistant and has_autonomous:
        test_result(agent_name, "Mode Behaviors", "PASS",
                   "Both ASSISTANT and AUTONOMOUS modes specified")
    else:
        missing = []
        if not has_assistant:
            missing.append("ASSISTANT")
        if not has_autonomous:
            missing.append("AUTONOMOUS")
        test_result(agent_name, "Mode Behaviors", "FAIL",
                   f"Missing mode specifications: {', '.join(missing)}")

print()

# Test 5: Code Examples
print("Test 5: Code Examples Presence")
print("-" * 80)

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "Code Examples", "SKIP", "File not found")
        continue

    with open(agent_file, 'r') as f:
        content = f.read()

    # Count code blocks
    code_blocks = re.findall(r'```[\w]*\n.*?```', content, re.DOTALL)
    code_block_count = len(code_blocks)

    if code_block_count >= 3:
        test_result(agent_name, "Code Examples", "PASS",
                   f"{code_block_count} code blocks found")
    else:
        test_result(agent_name, "Code Examples", "WARN",
                   f"Only {code_block_count} code blocks (expected ≥3)")

print()

# Test 6: File Size (Completeness Indicator)
print("Test 6: Specification Completeness (File Size)")
print("-" * 80)

MIN_SIZE_KB = 5  # Minimum 5KB for comprehensive spec

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "Completeness", "SKIP", "File not found")
        continue

    size_bytes = agent_file.stat().st_size
    size_kb = size_bytes / 1024

    if size_kb >= MIN_SIZE_KB:
        test_result(agent_name, "Completeness", "PASS",
                   f"{size_kb:.1f} KB (comprehensive)")
    else:
        test_result(agent_name, "Completeness", "WARN",
                   f"{size_kb:.1f} KB (may need more detail)")

print()

# Test 7: Quality Standards
print("Test 7: Quality Standards Section")
print("-" * 80)

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "Quality Standards", "SKIP", "File not found")
        continue

    with open(agent_file, 'r') as f:
        content = f.read()

    # Check for Quality Standards section with checklist items
    quality_section = re.search(r'## Quality Standards.*?(?=##|\Z)', content, re.DOTALL)

    if quality_section:
        section_content = quality_section.group(0)
        # Count checklist items (✅ or ☐)
        checklist_items = len(re.findall(r'[✅☐☑]', section_content))

        if checklist_items >= 3:
            test_result(agent_name, "Quality Standards", "PASS",
                       f"{checklist_items} checklist items found")
        else:
            test_result(agent_name, "Quality Standards", "WARN",
                       f"Only {checklist_items} checklist items")
    else:
        test_result(agent_name, "Quality Standards", "FAIL",
                   "Quality Standards section not found")

print()

# Test 8: Output Files Specification
print("Test 8: Output Files Specification")
print("-" * 80)

for agent_name in EXPECTED_AGENTS:
    agent_file = AGENTS_DIR / f"{agent_name}.md"

    if not agent_file.exists():
        test_result(agent_name, "Output Files", "SKIP", "File not found")
        continue

    with open(agent_file, 'r') as f:
        content = f.read()

    # Check for Output Files section
    output_section = re.search(r'## Output Files.*?(?=##|\Z)', content, re.DOTALL)

    if output_section:
        section_content = output_section.group(0)
        # Count file paths mentioned (look for .md, .csv, .json, .py, etc.)
        file_mentions = len(re.findall(r'[`"][\w/\-]+\.(md|csv|json|py|txt|pdf)[`"]', section_content))

        if file_mentions >= 2:
            test_result(agent_name, "Output Files", "PASS",
                       f"{file_mentions} output files specified")
        else:
            test_result(agent_name, "Output Files", "WARN",
                       f"Only {file_mentions} output files specified")
    else:
        test_result(agent_name, "Output Files", "FAIL",
                   "Output Files section not found")

print()

# Summary
print("=" * 80)
print("TEST SUMMARY")
print("=" * 80)

pass_count = sum(1 for t in results["tests"] if t["status"] == "PASS")
fail_count = sum(1 for t in results["tests"] if t["status"] == "FAIL")
warn_count = sum(1 for t in results["tests"] if t["status"] == "WARN")
skip_count = sum(1 for t in results["tests"] if t["status"] == "SKIP")

print(f"Agents Tested: {results['agents_tested']}/{len(EXPECTED_AGENTS)}")
print(f"Total Tests: {len(results['tests'])}")
print(f"✅ Passed: {pass_count}")
print(f"❌ Failed: {fail_count}")
print(f"⚠️  Warnings: {warn_count}")
print(f"⏭️  Skipped: {skip_count}")
print()

# Quality score
total_tests = pass_count + fail_count + warn_count
if total_tests > 0:
    quality_score = (pass_count + 0.5 * warn_count) / total_tests * 100
    print(f"Quality Score: {quality_score:.1f}%")
    print()

if fail_count == 0 and results['agents_tested'] == len(EXPECTED_AGENTS):
    print("Status: ✅ ALL AGENTS PASS")
    print("All 10 agents are complete and ready for use.")
elif fail_count == 0:
    print("Status: ⚠️  SOME AGENTS MISSING")
    print("Existing agents pass all tests, but not all agents created.")
else:
    print("Status: ❌ SOME TESTS FAILED")
    print("Review failed tests above and update agent specifications.")

print()
print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Exit code
import sys
sys.exit(0 if fail_count == 0 else 1)
