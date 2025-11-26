# Discourse Genre Feature

**Discourse genre** identifies the functional type of discourse (narrative, teaching, law, poetry, etc.) at the clause level. It determines grammatical choices for tense, aspect, word order, vocabulary, and discourse markers in target languages.

## Quick Facts

| Property | Value |
|---|---|
| **TBTA ID** | #14 (Tier A, Clause-level) |
| **Source Encoding** | NOT morphological (Hebrew/Greek) |
| **Documented Values** | 9 (Climactic Narrative, Background, Procedural, Expository, Poetic, Hortatory, Prophetic, Legal, Epistolary) |
| **Data Reality** | 1 value observed in TBTA (11% coverage) |
| **Target Languages Affected** | 300-500+ languages require genre-aware translation |
| **Theological Stakes** | **CRITICAL** (35% non-arbitrary, 20% theological) |

## High-Stakes Examples

| Verse | Genre | **WRONG CHOICE** | **RIGHT CHOICE** |
|---|---|---|---|
| Genesis 1:1-2:3 | Narrative (elevated prose) | ❌ **Myth/allegory** → Denies creation doctrine | ✅ Historical narrative |
| Matthew 5-7 | Teaching (expository) | ❌ Narrative tense → Flattens theological discourse | ✅ Timeless present |
| Exodus 20:13 | Legal (apodictic law) | ❌ Narrative forms → Weakens commands | ✅ Imperative/conditional |
| Psalm 23:1 | Poetry (not narrative) | ❌ Narrative wayyiqtol → Grammatically impossible | ✅ Poetic forms |
| Revelation 1-22 | Apocalyptic (symbolic prophecy) | ❌ Purely literal → False date-setting, absurd interpretation | ✅ Apocalyptic with symbolic conventions |

## Target Audience & Languages

**Mandatory marking**: French, Spanish, Portuguese, Italian, German, Bantu languages (89+), Mandarin, Japanese, most Austronesian (176 languages). Genre-tense mismatch produces ungrammatical sentences.

**Details**: See `research/LANGUAGES.md` for 8 Stage 2 candidate languages and typological classification.

## TBTA Encoding

Clause-level annotation in hierarchical structure: `Discourse Genre: "Climactic Narrative Story"` (context-dependent semantics, NOT part-of-speech rules).

**Data Status**: Only 1 of 9 values observed across 12,091 annotations. Algorithm must rely on linguistic theory + book-type classification; TBTA data currently insufficient for validation except Climactic Narrative.

**Details & Research**: See `research/README.md` (synthesis) and `research/SCHOLARLY.md` (30+ scholarly sources).
