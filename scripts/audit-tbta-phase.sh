#!/bin/bash
# TBTA Migration Phase Audit Script
# Usage: ./scripts/audit-tbta-phase.sh <phase>
# Example: ./scripts/audit-tbta-phase.sh 1a

set -e

PHASE=$1
TBTA_DIR="/workspaces/mybibletoolbox-code/bible-study-tools/tbta"
PASS=0
FAIL=0

echo "🔍 Auditing TBTA Migration Phase $PHASE..."
echo ""

audit_file_exists() {
    local file=$1
    local desc=$2
    if [ -f "$TBTA_DIR/$file" ]; then
        echo "✅ $desc: $file exists"
        ((PASS++))
    else
        echo "❌ $desc: $file missing"
        ((FAIL++))
    fi
}

audit_line_count() {
    local file=$1
    local min=$2
    local max=$3
    local desc=$4
    if [ -f "$TBTA_DIR/$file" ]; then
        local lines=$(wc -l < "$TBTA_DIR/$file")
        if [ $lines -ge $min ] && [ $lines -le $max ]; then
            echo "✅ $desc: $file has $lines lines ($min-$max expected)"
            ((PASS++))
        else
            echo "❌ $desc: $file has $lines lines ($min-$max expected)"
            ((FAIL++))
        fi
    else
        echo "❌ $desc: $file not found"
        ((FAIL++))
    fi
}

audit_no_todos() {
    local file=$1
    local desc=$2
    if [ -f "$TBTA_DIR/$file" ]; then
        local todos=$(grep -c "TODO" "$TBTA_DIR/$file" 2>/dev/null || echo "0")
        if [ $todos -eq 0 ]; then
            echo "✅ $desc: No TODOs in $file"
            ((PASS++))
        else
            echo "❌ $desc: Found $todos TODOs in $file"
            ((FAIL++))
        fi
    else
        echo "❌ $desc: $file not found"
        ((FAIL++))
    fi
}

audit_content_contains() {
    local file=$1
    local pattern=$2
    local desc=$3
    if [ -f "$TBTA_DIR/$file" ]; then
        if grep -q "$pattern" "$TBTA_DIR/$file"; then
            echo "✅ $desc: Found '$pattern' in $file"
            ((PASS++))
        else
            echo "❌ $desc: Missing '$pattern' in $file"
            ((FAIL++))
        fi
    else
        echo "❌ $desc: $file not found"
        ((FAIL++))
    fi
}

case $PHASE in
    "1a")
        echo "=== Phase 1A Audit ==="
        audit_line_count "features/STAGES.md" 600 1000 "STAGES.md size"
        audit_no_todos "features/STAGES.md" "STAGES.md TODOs"
        audit_content_contains "features/STAGES.md" "Stage 4" "STAGES.md has Stage 4"
        audit_content_contains "features/STAGES.md" "locked predictions" "STAGES.md has locked predictions protocol"
        audit_content_contains "features/STAGES.md" "6-step error analysis" "STAGES.md has error analysis"
        audit_content_contains "README.md" "11,649 verses" "README.md has correct coverage"
        audit_content_contains "README.md" "Genesis 1:26" "README.md has example 1"
        ;;
    "1b")
        echo "=== Phase 1B Audit ==="
        audit_file_exists "tbta-source/COVERAGE.md" "COVERAGE.md"
        audit_file_exists "tbta-source/TBTA-FEATURES.md" "TBTA-FEATURES.md"
        audit_file_exists "tbta-source/TRANSLATION-EDGE-CASES.md" "EDGE-CASES"
        audit_file_exists "tbta-source/ACCURACY-RESULTS.md" "ACCURACY-RESULTS"
        audit_file_exists "tbta-source/DATA-ACCESS.md" "DATA-ACCESS"
        audit_file_exists "tbta-source/METHODOLOGY.md" "METHODOLOGY"
        audit_file_exists "tbta-source/CRITIQUE.md" "CRITIQUE"
        audit_content_contains "tbta-source/COVERAGE.md" "11,649 verses" "COVERAGE has correct number"
        ;;
    "3")
        echo "=== Phase 3 Audit ==="
        audit_file_exists "features/TEMPLATE.md" "TEMPLATE.md"
        audit_content_contains "features/TEMPLATE.md" "STAGES.md" "TEMPLATE references STAGES"
        audit_line_count "README.md" 150 600 "README.md progressive disclosure"
        ;;
    *)
        echo "❌ Unknown phase: $PHASE"
        echo "Usage: $0 <1a|1b|3>"
        exit 1
        ;;
esac

echo ""
echo "=== Audit Results ==="
echo "✅ Passed: $PASS"
echo "❌ Failed: $FAIL"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "🎉 Phase $PHASE PASSED all audits!"
    exit 0
else
    echo "⚠️  Phase $PHASE FAILED $FAIL audit(s)"
    exit 1
fi
