# Aspect Research: Stage 1 Findings

**Aspect** is a grammatical category that describes the **internal temporal structure** of an action—how speakers view whether an event is complete, ongoing, or habitual. Unlike tense (which locates events in time), aspect focuses on the **viewpoint** of the speaker.

## Key Values

TBTA encodes **9 aspect values** as single-character codes (position 5 of verb semantic string):

| Value | Code | Frequency | Notes |
|-------|------|-----------|-------|
| Unmarked | U | 90.7% | Default for narrative |
| Inceptive | N | 5.6% | Action beginning |
| Completive | C | Rare | Action finished |
| Cessative | c | Rare | Action stopping |
| Continuative | o | Rare | Action ongoing |
| Imperfective | I | 1.9% | Incomplete/in progress |
| Habitual | H | 1.9% | Repeated pattern |
| Routinely | R | Untested | Iterative action |
| Gnomic | G | Untested | Timeless truth |

**Default policy**: TBTA marks aspect only when semantically necessary; most verbs default to Unmarked.

---

## TBTA Feature Review

TBTA classifies aspect as **Tier A (Essential)**—affecting 1000+ languages (Russian, Polish, Mandarin, Arabic, Turkish, Japanese, Niger-Congo, Austronesian). Aspect occupies position 5 in the verb semantic string with single-character encoding.

**Key research insight**: Multi-factor convergence model (combining morphological, lexical, temporal, discourse, and clause-level factors) achieves **98.1% accuracy** on test set, with 94.7% agreement on real translations (Russian, Mandarin, Arabic).

**Critical gaps**: TBTA shows "overgeneralization of Unmarked aspect" (all tested verbs coded as Unmarked despite semantic distinctions) and lacks systematic Aktionsart (verb lexical aspect) classification.

[Read TBTA analysis →](TBTA.md)

---

## Language Family & Typology

**Source language encoding**: Both Hebrew (qatal=perfective, yiqtol=imperfective) and Greek (aorist=perfective, present/imperfect=imperfective, perfect=stative) **explicitly encode aspect morphologically**.

**Target language distribution**:
- **30-40% MANDATORY**: Slavic, Bantu, Semitic, Sinitic, Mayan (grammatically required)
- **40-50% OPTIONAL**: Germanic, Romance, some Austronesian (periphrastic or lexical)
- **10-20% ABSENT**: Some isolates, Australian languages (only lexical/contextual)

**Critical languages**: English (optional), Spanish (optional), Arabic (mandatory), Russian (mandatory), Swahili (mandatory), Indonesian (optional particles), Mandarin (particle-based).

**Key finding**: Aspect is expressed via three strategies: (1) morphological affixes (Slavic, Semitic, Bantu), (2) periphrastic constructions (Germanic, Romance), (3) particles (Mandarin, Indonesian).

[Read language analysis →](LANGUAGES.md)

---

## Scholarly Foundation

**Typological basis**: 70% of world languages mark perfective/imperfective distinction (Dahl 1985). Comrie's foundational definition: "Perfective describes an eventuality as a complete whole; imperfective focuses on internal temporal structure."

**Greek aspect system**: Porter (1989) and Fanning (1990) established Koine Greek as aspect-prominent: aorist (perfective/external view), present/imperfect (imperfective/internal view), perfect (stative/resultant state).

**Hebrew aspect debate**: Cook (2012) argues Hebrew verbs express aspect (qatal=perfective, yiqtol=imperfective); Joosten (2012) disputes this. TBTA research assumes Cook's position.

**Translation case studies** (Lulogooli, Mandarin, Indonesian, Spanish, Swahili) demonstrate how aspect-sensitive languages require careful mapping: Greek perfective → Spanish preterite (90% match), Mandarin particles (90% match), Bantu prefixes (Lulogooli li-/ka-).

[Read scholarly research →](SCHOLARLY.md)

---

## Theological Significance

**High-stakes contexts** (15% of verses): Aspect choice affects core doctrines—Christ's finished work (John 19:30 perfect τετέλεσται), resurrection (Mark 16:6 perfect ἐγήγερται), justification (Rom 5:1 aorist δικαιωθέντες), abiding (John 15:4 present μείνατε), salvation (Eph 2:8 perfect σεσῳσμένοι).

**Non-arbitrary rationale**: Completed atonement requires perfective/perfect (not imperfective). Resurrection emphasizes ongoing risen state (perfect, not simple past). Justification is definitive declaration (aorist, not process). Abiding requires continuous action (present imperative, not one-time aorist). Salvation balances completed justification with ongoing sanctification (perfect aspect).

**Forbidden/heretical values**:
- ⛔ **John 19:30** (finished work): Never imperfective (would suggest ongoing sacrifice, contradicting Hebrews 10:12)
- ⛔ **Mark 16:6** (resurrection): Never simple past without ongoing state implications
- ⛔ **Rom 5:1** (justification): Never imperfective (would suggest process, not forensic declaration)

**Arbitrary contexts** (85%): Historical narrative, travel descriptions, crowd reactions, incidental actions where aspect choice is stylistic.

[Read theological analysis →](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

---

## Discrepancies & Gaps

1. **Imperfective vs. Continuative**: Not clearly distinguished in TBTA documentation. May represent regional variation or intensity difference.

2. **Habitual vs. Routinely**: Both describe repeated/regular action; distinction unclear.

3. **Completive vs. Unmarked**: When to use each for completed narrative events (both appear valid in TBTA).

4. **Aktionsart integration**: TBTA lacks systematic verb lexical aspect classification; limits prediction accuracy for aspect-prominent languages.

5. **Confidence metadata**: TBTA treats all annotations as equally certain despite variable accuracy (some contexts 65%, others 98%).

6. **Morphology vs. semantic approach**: TBTA encodes semantic aspect but sometimes loses morphological information critical for translation (imperative mood conflation issue).

---

## Summary

Aspect is **Tier A Essential** for 1000+ languages, **explicitly encoded** in source languages (Hebrew, Greek), and critical for 15% of theological content. Research achieves **98.1% accuracy** using multi-factor convergence. Target language strategies vary: 30-40% require mandatory aspect marking, 40-50% use optional/periphrastic marking, 10-20% lack grammaticalized aspect.

**Confidence level**: High for values and frequency; medium for edge cases and distinctions; low for optimal Aktionsart integration.

---

**Research compiled**: 2025-11-25
**Sources**: 4 agent research documents, 45+ scholarly sources, 5 translation case studies
**Status**: Complete. Awaiting feature README synthesis and Stage 2 analysis phase.
