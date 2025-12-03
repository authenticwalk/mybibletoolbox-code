# TBTA Phase1 Verse Rule Reverse Engineering (GPT-5.1, No-CSV Variant)

## Overview

- **Objective**: Reverse engineer TBTA's Verse column rules from NIV → Controlled Natural Language (CNL) using the compressed 12-rule set in `plan/tbta/phase1-policy/RULES.md`.
- **Method**: Use a combination of existing TBTA worked examples (mainly in Ruth, Genesis) and the model's internal knowledge of NIV, other major English translations, and source languages—**no CSV downloads, external verse lookups, or custom analysis scripts**.
- **Deliverable**: For each of the 12 rules, attach up to 5 **supporting** and up to 3 **contradicting / edge-case** references, and document style and edge-case behaviour (He1 vs He2) plus mental validation scenarios.

This directory only adds **meta-analysis** and **guidance**. All references and paraphrases here are based on a mix of:

- Existing TBTA examples in this repository (especially Ruth 1–2, Genesis 22, Romans 8)
- The model's internal memory of the NIV text and common translation patterns

They are intended as **hypotheses to be verified** against the full TBTA data, not as final gold standard data files.

## Files in this Directory

- `rules-evidence.md` — Per-rule evidence: references, patterns, and short explanations.
- `style-and-edge-cases.md` — He1 vs He2 style differences and key edge-case patterns, including results from mental validation scenarios.

## Relationship to Policy Files

- **Core rules**: [`plan/tbta/phase1-policy/RULES.md`](../phase1-policy/RULES.md) (compressed 12-rule version).
- **Verbose commentary**: [`plan/tbta/phase1-policy/RULES-VERBOSE.md`](../phase1-policy/RULES-VERBOSE.md).
- **Generation skill**: [`plan/tbta/phase1-policy/SKILL.md`](../phase1-policy/SKILL.md) and [`bible-study-tools/tbta/phase1/policies/SKILL.md`](../../../bible-study-tools/tbta/phase1/policies/SKILL.md).
- **Worked examples**: [`bible-study-tools/tbta/phase1/policies/examples.md`](../../../bible-study-tools/tbta/phase1/policies/examples.md) and [`plan/tbta/phase1-policy/TEST-RESULTS.md`](../phase1-policy/TEST-RESULTS.md).

The evidence strings now attached under each rule heading in `RULES.md` are concise summaries of the more detailed reasoning captured in `rules-evidence.md` and `style-and-edge-cases.md`.

## Caveats and Intended Use

- **Verification required**: Verse references and paraphrased transformations should be checked against the actual TBTA CSV corpus and linter when that workflow is re-enabled.
- **Scope of books**: Examples prioritize the 15-book TBTA Phase1 scope (Genesis, Joshua, Ruth, 1–2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John), but occasionally draw on highly diagnostic verses slightly outside that set when useful.
- **He1 vs He2**: Observations about style differences come from Ruth/Genesis/Jonah (He1) and Matthew/Mark/Acts (He2-leaning) patterns described in existing docs plus internal intuition about how the rules would scale.

Future work should treat this directory as a **starting point for data-backed refinement**, not as a replacement for corpus-level analysis.


