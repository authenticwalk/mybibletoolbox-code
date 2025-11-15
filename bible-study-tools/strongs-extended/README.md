# Strong's Research

Strong's Concordance provides standardized reference numbers for Greek (G####) and Hebrew (H####) words in the Bible. These numbers enable consistent identification and cross-referencing of original language terms across translations and scholarly resources.

## Goal

This directory enriches Strong's data through research from published lexicons, cross-linguistic translation patterns, and cultural adaptation solutions. All research follows the [Fair Use Policy](/plan/policy/fair-use.md) for copyrighted resources, anchoring analysis in public domain source texts while documenting scholarly consensus and divergence patterns.

# Data and Structure

Data is stored in according to [STANDARDIZATON policy](/STANDARDIZATION.md) as (G|H){num:04d}

```
.data/strongs/G0026/G0026-{tool}.yaml
.data/strongs/H0157/H0157-{tool}.yaml
```

**Initialize the data directory** by running `setup-minimal-data.sh` from the project root. This clones the data repository with git sparse-checkout enabled, downloading only essential files initially. To work with specific Strong's numbers, add them to the sparse-checkout scope: `cd .data && git sparse-checkout add strongs/G0026` (or use `git sparse-checkout disable` to download everything). See [CLAUDE.md § Working with Sparse Checkout](/CLAUDE.md#working-with-sparse-checkout) for complete details on managing the sparse-checkout scope.

## Tools

Strong's enrichment comprises three complementary types of tools:

1. **Lexical Research** - Etymology and scholarly analysis from published lexicons (BDB, Thayer's, BDAG, LSJ)
2. **TBTA Hints** - Cross-linguistic grammatical patterns extracted from 900+ Bible translations
3. **Cultural Translation** - Solutions for translating culturally non-existent concepts (snow in tropics, lambs in Arctic)

**Available Tools:**
- ✅ **Tool 1: Lexicon Core** - Foundation tool extracting authoritative lexical data (etymology, semantic range, usage statistics) from published lexicons. Status: Research phase complete, experiments ongoing.
- ✅ **Tool 3: Web Insights** - Modern scholarly insights, error corrections, and practical applications from vetted expert sources (Bill Mounce, seminary sites). Status: Production-ready.
- 🔄 **TBTA Hints** - Grammatical translation patterns (clusivity, number systems, proximity) from translation corpus. Status: Proof-of-concept phase.
- 📋 **Cultural Translation** - Documented solutions for non-existent concepts and cultural taboos. Status: Planning complete.

**Coverage:** Tool 1 targets all 14,197 Strong's words; Tool 3 covers ~1,500 high-value words; TBTA/Cultural focus on top 300-500 words with highest variation.

**Quality Standards:** All tools enforce no-fabrication policy, inline citations, fair use compliance, and 3-level validation (Critical 100%, High 80%+, Medium 60%+).

For detailed methodology, experimentation results, and implementation status, see [tools/TOOLS.md](tools/TOOLS.md).

All markdown files must follow [Progressive Disclosure of Documentation Policy](/.claude/skills/progressive-disclosure/SKILL.md)