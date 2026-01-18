#!/bin/bash
# Pre-Distribution Verification Script
# Research Assistant Plugin v1.2.0-beta3
# Verifies marketplace readiness before distribution

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Research Assistant Plugin - Pre-Distribution Verification${NC}"
echo -e "${BLUE}  Version: 1.2.0-beta3${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Track errors
ERRORS=0
WARNINGS=0

# =============================================================================
# 1. JSON Validation
# =============================================================================
echo -e "${BLUE}1️⃣  Validating JSON files...${NC}"

if jq empty .claude-plugin/marketplace.json 2>/dev/null; then
    echo -e "   ${GREEN}✅ marketplace.json valid${NC}"
else
    echo -e "   ${RED}❌ marketplace.json invalid${NC}"
    ((ERRORS++))
fi

if jq empty .claude-plugin/plugin.json 2>/dev/null; then
    echo -e "   ${GREEN}✅ plugin.json valid${NC}"
else
    echo -e "   ${RED}❌ plugin.json invalid${NC}"
    ((ERRORS++))
fi

if jq empty .claude/settings.json 2>/dev/null; then
    echo -e "   ${GREEN}✅ settings.json valid${NC}"
else
    echo -e "   ${RED}❌ settings.json invalid${NC}"
    ((ERRORS++))
fi

# =============================================================================
# 2. Skill Validation
# =============================================================================
echo ""
echo -e "${BLUE}2️⃣  Validating skills...${NC}"

skill_count=$(find skills -name "SKILL.md" 2>/dev/null | wc -l)
echo -e "   Found ${skill_count} skills"

if [ "$skill_count" -eq 22 ]; then
    echo -e "   ${GREEN}✅ All 22 skills present${NC}"
else
    echo -e "   ${RED}❌ Expected 22 skills, found ${skill_count}${NC}"
    ((ERRORS++))
fi

# Check for YAML frontmatter in skills
echo -e "   Checking YAML frontmatter..."
for skill in skills/*/SKILL.md; do
    if ! grep -q "^---$" "$skill"; then
        echo -e "   ${RED}❌ Missing frontmatter in $skill${NC}"
        ((ERRORS++))
    fi
done
echo -e "   ${GREEN}✅ All skills have frontmatter${NC}"

# =============================================================================
# 3. Agent Validation
# =============================================================================
echo ""
echo -e "${BLUE}3️⃣  Validating agents...${NC}"

agent_count=$(find .claude/agents -name "*.md" 2>/dev/null | wc -l)
echo -e "   Found ${agent_count} agents"

if [ "$agent_count" -eq 10 ]; then
    echo -e "   ${GREEN}✅ All 10 agents present${NC}"
else
    echo -e "   ${RED}❌ Expected 10 agents, found ${agent_count}${NC}"
    ((ERRORS++))
fi

# =============================================================================
# 4. Version Consistency
# =============================================================================
echo ""
echo -e "${BLUE}4️⃣  Checking version consistency...${NC}"

plugin_version=$(jq -r '.version' .claude-plugin/plugin.json 2>/dev/null)
marketplace_version=$(jq -r '.version' .claude-plugin/marketplace.json 2>/dev/null)
readme_version=$(grep -oP 'version-\K[0-9]+\.[0-9]+\.[0-9]+-[a-z0-9]+' README.md 2>/dev/null | head -1)

echo -e "   plugin.json: ${plugin_version}"
echo -e "   marketplace.json: ${marketplace_version}"
echo -e "   README.md: ${readme_version}"

if [ "$plugin_version" == "1.2.0-beta3" ] && [ "$marketplace_version" == "1.2.0-beta3" ]; then
    echo -e "   ${GREEN}✅ Version consistency check passed${NC}"
else
    echo -e "   ${RED}❌ Version mismatch detected${NC}"
    ((ERRORS++))
fi

# =============================================================================
# 5. Security Checks
# =============================================================================
echo ""
echo -e "${BLUE}5️⃣  Running security checks...${NC}"

# Check for hardcoded secrets
if grep -rE "api[_-]?key\s*=\s*['\"][^'\"]{10,}" --include="*.py" code/ tools/ mcp-servers/ 2>/dev/null | grep -v "your_.*_key_here" | grep -v "# Example:"; then
    echo -e "   ${RED}❌ Potential hardcoded API keys found${NC}"
    ((ERRORS++))
else
    echo -e "   ${GREEN}✅ No hardcoded API keys detected${NC}"
fi

# Check .gitignore includes .env
if grep -q "^\.env$" .gitignore; then
    echo -e "   ${GREEN}✅ .env properly ignored${NC}"
else
    echo -e "   ${YELLOW}⚠️  .env not in .gitignore${NC}"
    ((WARNINGS++))
fi

# =============================================================================
# 6. Hook Files
# =============================================================================
echo ""
echo -e "${BLUE}6️⃣  Validating hooks...${NC}"

hook_files=(
    ".claude/hooks/session-start.sh"
    ".claude/hooks/prompt-validate.py"
    ".claude/hooks/pre-tool-security.py"
    ".claude/hooks/post-tool-log.py"
    ".claude/hooks/pre-compact-backup.py"
    ".claude/hooks/stop-validate-completion.py"
    "hooks/pre-commit-ai-check.py"
)

for hook in "${hook_files[@]}"; do
    if [ -f "$hook" ]; then
        echo -e "   ${GREEN}✅ $hook exists${NC}"
    else
        echo -e "   ${RED}❌ $hook missing${NC}"
        ((ERRORS++))
    fi
done

# =============================================================================
# 7. Documentation Checks
# =============================================================================
echo ""
echo -e "${BLUE}7️⃣  Checking documentation...${NC}"

required_docs=(
    "README.md"
    "CHANGELOG.md"
    "CONTRIBUTING.md"
    "SECURITY.md"
    "LICENSE"
    "TROUBLESHOOTING.md"
    "INSTALLATION.md"
)

for doc in "${required_docs[@]}"; do
    if [ -f "$doc" ]; then
        echo -e "   ${GREEN}✅ $doc present${NC}"
    else
        echo -e "   ${YELLOW}⚠️  $doc missing${NC}"
        ((WARNINGS++))
    fi
done

# =============================================================================
# 8. File Permissions
# =============================================================================
echo ""
echo -e "${BLUE}8️⃣  Checking file permissions...${NC}"

# Check hooks are executable
shopt -s nullglob
for hook in .claude/hooks/*.sh hooks/*.sh; do
    if [ -f "$hook" ]; then
        if [ -x "$hook" ]; then
            echo -e "   ${GREEN}✅ $hook is executable${NC}"
        else
            echo -e "   ${YELLOW}⚠️  $hook not executable${NC}"
            ((WARNINGS++))
        fi
    fi
done
shopt -u nullglob

# =============================================================================
# 9. Git Status
# =============================================================================
echo ""
echo -e "${BLUE}9️⃣  Checking git status...${NC}"

if git status --short 2>/dev/null | grep -q "^??"; then
    echo -e "   ${YELLOW}⚠️  Untracked files present (review before distribution)${NC}"
    git status --short | grep "^??"
    ((WARNINGS++))
else
    echo -e "   ${GREEN}✅ No untracked files${NC}"
fi

# Check for uncommitted changes
if git status --short 2>/dev/null | grep -qE "^[MADRCU]"; then
    echo -e "   ${YELLOW}⚠️  Uncommitted changes present${NC}"
    git status --short | grep -E "^[MADRCU]"
    ((WARNINGS++))
else
    echo -e "   ${GREEN}✅ No uncommitted changes${NC}"
fi

# =============================================================================
# 10. Component Count Summary
# =============================================================================
echo ""
echo -e "${BLUE}🔟  Component Summary...${NC}"

tutorial_count=$(find tutorials -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l || echo "0")
template_count=$(find templates -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l || echo "0")
mcp_count=$(find mcp-servers -maxdepth 1 -name "*.py" -type f 2>/dev/null | wc -l || echo "0")

echo -e "   Skills: ${skill_count}/22"
echo -e "   Agents: ${agent_count}/10"
echo -e "   Tutorials: ${tutorial_count}"
echo -e "   Templates: ${template_count}"
echo -e "   MCP Servers: ${mcp_count}"
echo -e "   Hooks: ${#hook_files[@]}/7"

# =============================================================================
# Final Summary
# =============================================================================
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ ALL CHECKS PASSED - READY FOR DISTRIBUTION${NC}"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  PASSED WITH ${WARNINGS} WARNING(S)${NC}"
    echo -e "${YELLOW}   Review warnings above before proceeding with distribution.${NC}"
    exit 0
else
    echo -e "${RED}❌ FAILED: ${ERRORS} ERROR(S), ${WARNINGS} WARNING(S)${NC}"
    echo -e "${RED}   Fix errors above before proceeding with distribution.${NC}"
    exit 1
fi
