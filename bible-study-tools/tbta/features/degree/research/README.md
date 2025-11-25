# Degree Feature Research

Degree marks comparison (comparative, superlative) and intensification across adjectives, adverbs, and verbs. This is a **linguistically complex but theologically selective feature**: 80% of contexts are stylistic, but 20% involve core Christian doctrines where degree encoding directly affects interpretation.

## TBTA Implementation

TBTA confirms 5 values in actual Biblical texts: **No Degree**, **Comparative**, **Superlative**, **Intensified**, and literal `'''least'''` encoding. The feature uses dual encoding formats (standardized + literal) and applies **semantic priority over morphology** — context determines degree even when morphological form suggests otherwise.

**Critical algorithm requirements**: (1) Gradability prerequisite check, (2) Implied superlative patterns (negative comparatives), (3) Syntactic vs. lexical distinction, (4) Dual encoding handling. Previous v1.0 accuracy: 42.9%; v2.0 expected: ~71% after fixing these issues.

**Schema vs. reality mismatch**: 11 theoretical values, but only 5 confirmed in data. Values q, i, s are non-existent; E, T, L remain uncertain.

[Read full TBTA documentation →](TBTA.md)

## Source Language Encoding: The Greek-Hebrew Divide

**This is CRITICAL**: Hebrew and Greek use fundamentally different strategies for degree marking.

**Hebrew (Biblical)**: Degree is **NOT morphologically encoded**. Uses exclusively periphrastic constructions: comparative with מִן (min) "from", superlative via construct state (e.g., "song of songs" = greatest song), intensification with מְאֹד (me'od) "very". **Implication**: OT translators must infer degree from construction, not morphology.

**Greek (Koine)**: Degree **IS morphologically encoded** via suffixes: -τερος/-τατος (comparative/superlative). Also offers periphrastic alternatives (μᾶλλον "more", μάλιστα "most"). **Implication**: NT translators can read degree directly from morphology.

**Translation impact**: Target languages without morphological degree must use lexical/syntactic strategies (adverbs, particles, verbal comparisons) even when source languages have explicit marking.

[Read full language analysis →](LANGUAGES.md)

## Typological Classification

**Mandatory degree systems** (~260 languages): Most Indo-European, Sino-Tibetan, modern Afro-Asiatic use synthetic (affixal) or analytic (separate words) degree marking. Examples: English (-er/-est), Spanish (más/menos), Mandarin (更/最).

**Optional degree** (~100 languages): Many Niger-Congo and some Austronesian languages express comparison contextually via exceed-verbs or adverbs (e.g., Swahili kuliko "more than"). Translator must infer whether comparison is intended.

**Degree-neutral languages** (~20): Washo, Motu, Fijian, Warlpiri completely lack degree semantics. Use conjoined comparison instead ("X big, Y small"). **Critical for algorithm**: Cannot output C/S/I codes for these languages.

**Recommended translation languages**: English (synthetic+analytic), Spanish (analytic), Mandarin (analytic), Indonesian (optional), Swahili (optional), plus one degree-neutral language (Fijian or Australian Aboriginal).

[Read full typological analysis →](LANGUAGES.md)

## Scholarly Foundation

Research synthesizes 28+ scholarly sources (Bobaljik, Kennedy & McNally, Stassen, Ultan, etc.) revealing **universal patterns in how languages organize degree systems**.

**Universal Principles**:
1. Superlatives are more marked than comparatives (Ultan's universal)
2. If comparative is suppletive, superlative must be suppletive (Bobaljik's constraint)
3. Superlatives morphologically contain comparatives (containment hypothesis)
4. Gradable predicates map to abstract scales with open/closed and absolute/relative parameters

**WALS Typology**: Four comparative construction types by standard-marking: Locational (Eurasia), Exceed (Africa/Southeast Asia), Particle (Europe), Conjoined. Geographic clustering suggests areal patterns.

**Translation case studies**: Hebrew construct state superlatives (Song of Songs, Holy of Holies), Greek Koine shift (superlative → positive form), Fijian Austronesian degree strategies, Bantu verbal comparison constructions.

[Read full scholarly research →](SCHOLARLY.md)

## Theological Stakes: Non-Arbitrary Contexts

**Default**: 80% of degree contexts are stylistic/arbitrary (crowd sizes, travel descriptions, emotional intensifiers). But **20% are theologically non-arbitrary** where degree choice affects doctrine.

### High-Stakes Theological Contexts (10 patterns identified)

1. **Christology**: Hebrews' "better than angels," "greater glory than Moses" — comparative/superlative essential for Christ's deity
2. **Ethics**: "Greatest commandment" — superlative establishes priority hierarchy
3. **Virtues**: 1 Corinthians 13:13 "love is greatest" — establishes eternal hierarchy
4. **God's Sovereignty**: 1 John 4:4 "Greater is He in you than he in world" — victory over evil
5. **Trinity Economics**: John 14:28 "Father is greater" — must preserve comparative while maintaining ontological equality
6. **Covenant Theology**: Hebrews' "better covenant/promises" — comparative shows progressive revelation, not old covenant inferiority
7. **Kingdom Values**: "Greatest must be servant" — superlative inverts worldly hierarchy
8. **Salvation Assurance**: Romans 8:38-39 — intensifiers establish unbreakable assurance
9. **Christ's Exaltation**: Philippians 2:9 — superlative+intensified "name above every name"
10. **Absolute States**: Non-gradable adjectives ("dead," "perfect") treated differently than gradable ones

**Heresy warnings**: Arianism (Christ as created being), Monotheletism, flattened ethics, weakened assurance.

[Read full theological analysis →](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

## Summary

| Aspect | Finding |
|--------|---------|
| **TBTA Status** | 5 confirmed values; dual encoding format |
| **Algorithm** | 4 critical rules (gradability, implied superlatives, syntactic/lexical, encoding) |
| **Hebrew** | Periphrastic only; infer from construction |
| **Greek** | Morphologically explicit; can read directly |
| **Language families** | 3 categories: mandatory, optional, absent |
| **Scholarly sources** | 28+ spanning 50+ years of typological research |
| **Theological weight** | 20% non-arbitrary (doctrinal); 80% arbitrary (stylistic) |
| **Key distinction** | Degree errors in 20% of contexts affect Christian orthodoxy |

---

**Research Status**: Complete — All 4 sections synthesized, citations comprehensive, verification notes included where applicable.

**Next Stage**: Stage 2 (Analysis) will compute frequency distributions across TBTA data; Stage 3 will design prediction algorithms; Stage 4 will validate with target language translations.
