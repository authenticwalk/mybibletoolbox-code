# Aspect (Grammatical Viewpoint)

**Grammatical category describing how speakers view the internal temporal structure of actions** (complete/whole vs. ongoing/in progress)—distinct from tense (time location).

## Quick Facts

| Property | Value |
|----------|-------|
| **TBTA Class** | Tier A (Essential) |
| **Position** | 5 in verb semantic string |
| **Values** | 9 single-char codes: U, N, C, c, o, I, R, H, G |
| **Default** | U (Unmarked, 90.7% in narrative) |
| **Source Languages** | Hebrew (qatal/yiqtol), Greek (aorist/present/perfect) |
| **Mandatory for** | ~30-40% of languages (Slavic, Bantu, Semitic, Sinitic, Mayan) |
| **Optional for** | ~40-50% of languages (Germanic, Romance, some Austronesian) |
| **Theological Stakes** | **HIGH** (15% of verses non-arbitrary) |

## Target Audience

Language families requiring careful aspect annotation: **Slavic** (Russian, Polish), **Bantu** (Swahili), **Semitic** (Arabic, Hebrew), **Sino-Tibetan** (Mandarin), **Mayan** (K'iche', Kaqchikel). Also critical for **optional-aspect languages** (English, Spanish) in theologically sensitive contexts.

[Full language family analysis →](research/LANGUAGES.md)

## Examples with Stakes

| Context | Source | Value | Rationale | Stakes |
|---------|--------|-------|-----------|--------|
| John 19:30 | τετέλεσται (perfect) | C/Perfect | "Finished work" requires bounded completion, not ongoing | **FORBIDDEN: Imperfective** ⛔ |
| Mark 16:6 | ἐγήγερται (perfect) | C/Perfect | Resurrection: completed + ongoing risen state | **FORBIDDEN: Simple past** ⛔ |
| Rom 5:1 | δικαιωθέντες (aorist) | N/Perfective | Justification: definitive forensic declaration | **FORBIDDEN: Process/imperfective** ⛔ |

## TBTA Encoding

**9-value system**: Unmarked (U, default), Inceptive (N, beginning), Completive (C, finished), Cessative (c, stopping), Continuative (o, ongoing), Imperfective (I, incomplete), Habitual (H, repeated), Routinely (R, iterative), Gnomic (G, timeless).

**Algorithm**: Multi-factor convergence (morphological + lexical + temporal + discourse + clause-level) achieves **98.1% accuracy**; external validation **94.7%** (Russian, Mandarin, Arabic).

**Constraint**: Aspect applies only to verbs (Part of Speech = Verb).

[Read TBTA technical details →](research/TBTA.md)

## Theological Stakes

**⚠️ CRITICAL CONTEXTS**: Atonement, resurrection, justification, abiding, salvation, prophecy fulfillment, command force (aorist vs. present imperative).

**Research finding**: 15% of biblical verses have non-arbitrary aspect choice; 85% stylistic/contextual.

[Read theological analysis →](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

---

**Status**: Stage 1 Research Complete | **Accuracy**: 98.1% (model), 94.7% (external validation) | **Next**: Stage 2 Analysis Phase
