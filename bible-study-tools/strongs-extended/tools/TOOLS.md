# Strong's Extended Tools - Overview

Quick reference for all Strong's enrichment tools. For detailed methodology, see individual tool folders.

## Three Tool Categories

### 1. Lexical Research
**Purpose:** What does this word actually mean?

Extract authoritative lexical data (etymology, semantic range, usage statistics) from published lexicons to create the foundation for all Strong's enrichment work.

**Authority Level:** HIGH - Published lexicons only
**Coverage:** All 14,197 Strong's words (8,674 Hebrew + 5,523 Greek)

### 2. TBTA Hints
**Purpose:** How do different languages grammatically express this word?

Extract cross-linguistic grammatical patterns from 900+ Bible translations to provide translation hints for ambiguous contexts.

**Expected Impact:** +7% overall accuracy (85% → 92%), +25% edge cases (60% → 85%)
**Coverage:** Top 300 high-frequency words (pronouns, demonstratives, particles)

### 3. Cultural Translation
**Purpose:** What should we say when the original concept doesn't exist in the target culture?

Document proven solutions for translating culturally non-existent concepts and taboo subjects.

**Example Solutions:** Snow → Hawaiian "hau" (ice/frost), Lamb → Inuktitut "nattiq" (seal pup)
**Coverage:** Top 300-500 words with highest cultural variation

---

## Available Tools

### ✅ Tool 1: Lexicon Core
**Status:** 🔄 Cycle 4 experiments | **Timeline:** 14 weeks | **See:** `./lexicon-core/docs/`

Extract authoritative lexical data from published lexicons (BDB, Thayer's, BDAG, LSJ, Abbott-Smith, HELPS Word-studies). Uses fair use convergence grouping for multi-source synthesis.

**Output:** `.data/strongs/{num}/{num}-lexicon-core.yaml`

---

### ✅ Tool 3: Web Insights
**Status:** ✅ Production ready | **Timeline:** 12 weeks | **See:** `./web-insights/docs/`

Extract insights from vetted web sources (11 vetted domains) to complement lexical research with contemporary scholarship and error corrections. Features 5-part error correction and multi-perspective framework.

**Output:** `.data/strongs/{num}/{num}-web-insights.yaml`

---

### 🔄 TBTA Hints
**Status:** 📋 Proof-of-concept | **Timeline:** 5 months | **See:** `./tbta-hints/`

Extract cross-linguistic translation patterns from 900+ Bible translations. LLM-based logic tree analyzes 11 TBTA features (number, clusivity, proximity, polarity, etc.) to provide context-dependent translation guidance.

**Output:** `.data/strongs/{num}/{num}-tbta-hints.yaml`

---

### 🔄 Tool 2: Scholarly Analysis
**Status:** 🔄 Experiments complete (5/5) | **Timeline:** TBD | **See:** `./scholarly-analysis/docs/`

Extract academic insights, theological analysis, and scholarly research from peer-reviewed sources. Adds deeper theological significance, scholarly debates, cultural context, and diachronic analysis to complement lexicon-core.

**Output:** `.data/strongs/{num}/{num}-scholarly-analysis.yaml`

---

### ✅ Tool 4: Community Discussions
**Status:** ✅ Production ready | **Timeline:** 7 months | **See:** `./community-discussions/docs/`

Document common misconceptions and popular errors from community discussions, paired with scholarly refutations. Prevents misinformation propagation through error-correction pairing.

**Output:** `.data/strongs/{num}/{num}-community-discussions.yaml`

---

### 📋 Cultural Translation
**Status:** 📋 Planning complete | **Timeline:** 4 months | **See:** `./cultural-translation/docs/`

Document proven cultural adaptation strategies for translating non-existent concepts, untranslatable abstracts, cultural sensitivities, and semantic gaps across 900+ translations.

**Output:** `.data/strongs/{num}/{num}-cultural.yaml`

---

## How Tools Work Together

### Example: Translating "Lamb of God" (G721 ἀρνίον) to Inuktitut (Arctic)

**Tool 1 (Lexicon Core):**
- Etymology: diminutive of ἀρήν (lamb)
- Theological significance: Passover sacrifice, Messianic imagery
- Usage: 30 NT occurrences, primarily John and Revelation

**Tool 2 (TBTA Hints):**
- Number: singular (one specific lamb)
- Definiteness: definite article ("THE lamb")
- Semantic role: patient (the one sacrificed)

**Tool 3 (Cultural Challenges):**
- **Problem:** Inuit have no sheep, no lamb concept
- **Solution:** "nattiq Guutimut" (seal pup of God)
- **Rationale:** Seals are primary food/sacrifice animal
- **Evaluation:** Preserves purity and substitutionary death imagery

**Combined Result:**
```yaml
translation_guidance:
  lexical: "Young sacrificial animal, theologically central"
  grammatical: "Singular definite noun, patient role"
  cultural_solution: "Substitute culturally appropriate sacrificial animal"
  recommended: "seal pup" (nattiq)
  preserve: "Innocence, purity, substitutionary sacrifice imagery"
```

---

## Quality Standards (All Tools)

### Level 1: CRITICAL (100% pass required)
- **No fabrication** - All data from documented sources
- **Inline citations** - Every claim cited: `content {source}`
- **No percentages** - Use "most", "many", "some" (unless from source)
- **Source validation** - All sources listed in `/ATTRIBUTION.md`
- **Fair use compliance** - Convergence grouping, divergence in context

### Level 2: HIGH PRIORITY (80%+ pass required)
- **Multiple sources** - 2+ sources for etymology, semantic range
- **Convergence patterns** - Document where sources agree
- **Divergence documented** - Note scholarly debates when they exist
- **Usage statistics** - Match source data accurately
- **Authority marked** - HIGH/MEDIUM/MEDIUM-LOW clearly indicated

### Level 3: MEDIUM PRIORITY (60%+ pass required)
- **Cross-reference codes** - Extract when available (BDAG, TDNT, etc.)
- **Diachronic analysis** - Classical → Koine changes (when applicable)
- **Fair use verified** - No reconstruction of copyrighted content
- **Complete documentation** - All claims traceable to sources

### Level 4: PEER REVIEW (Usefulness validation)

Real-world validation by target users - Bible translators, pastors, and students.

**Translation Impact Testing:**
- Would a Bible translator copy this to their translation notes?
- Does it prevent documented translation errors?
- Are language-specific patterns actionable (not "some cultures...")?

**See:** STAGES.md §6 "Translation Impact Testing" for evidence-based validation methodology

---

## Implementation Status

| Tool | Status | Next Step |
|------|--------|-----------|
| Lexicon Core | 🔄 Cycle 4 experiments | Validate methodology, begin production |
| Scholarly Analysis | 🔄 Experiments complete (5/5) | Design production methodology |
| Web Insights | ✅ Production ready | Deploy high-priority words |
| Community Discussions | ✅ Production ready | Begin production (500 words) |
| TBTA Hints | 📋 Proof-of-concept | Run pilot with 3 pronouns |
| Cultural Translation | 📋 Planning complete | Begin pilot study (3-5 words) |

---

## Key Planning Documents

**Master Strategy:**
- `/plan/strongs-comprehensive-strategy.md` - Overall vision, three initiatives, integration

**Execution Workflow:**
- `./STAGES.md` - Production workflow (6 stages, 7 cycles)
- `./LEARNINGS.md` - Historical learnings (7 proven patterns with evidence)

**Tool-Specific Documentation:**

**Directory Structure Note:** Strong's tools use `/docs` subdirectory to separate:
- `/docs/` - Methodology, experiments, learnings (documentation)
- `/` - Code, scripts, production configs (implementation)

This differs from TBTA features (flat structure) but is pragmatic for Strong's tools due to extensive experimentation documentation (80+ experiments across tools). The `/docs` separation keeps implementation files clean while preserving complete research trail.

- `./lexicon-core/docs/` - README, METRICS, experiments
- `./scholarly-analysis/docs/` - README (full docs in /plan)
- `./web-insights/docs/` - README, METRICS, experiments
- `./community-discussions/docs/` - README (full docs in /plan)
- `./tbta-hints/` - METHODOLOGY, LOGIC-TREE, METRICS
- `./cultural-translation/docs/` - README, METRICS, planning

**Supporting Documents:**
- `/plan/policy/fair-use.md` - Fair use compliance guidelines
- `/ATTRIBUTION.md` - All sources with copyright notices
- `/STANDARDIZATION.md` - File naming and structure standards
- `/SCHEMA.md` - YAML output schema standards
- `/REVIEW-GUIDELINES.md` - 3-level validation criteria

---

**Last Updated:** 2025-11-15
**Maintained by:** Strong's Extended Tools Development Team
