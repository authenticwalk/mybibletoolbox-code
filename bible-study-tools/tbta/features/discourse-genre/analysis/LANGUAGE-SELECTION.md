# Language Selection for Discourse Genre Feature

## Selection Criteria

Based on research/LANGUAGES.md, selected languages that:
1. **Mark discourse genre** through morphological, syntactic, or lexical means
2. **Represent typological diversity** across major language families
3. **Are available in eBible corpus** with both OT and NT coverage
4. **Were validated** against sample verses (GEN.001.026, MAT.004.019)

## Core Translations (Required)

| Code | Format | Language | Testament Coverage | Reason |
|------|--------|----------|-------------------|--------|
| `eng-YLT` | full | English (Young's Literal) | OT + NT | Literal translation, preserves Hebrew/Greek discourse patterns |
| `grc` | prefix | Greek (source) | NT (grc-BYZ/SR), OT (grc-LXX) | Source language for NT, LXX for OT |
| `hbo` | prefix | Hebrew (source) | OT only (hbo-WLC) | Source language for OT |
| `heb-heb` | full | Modern Hebrew | OT + NT | Modern Hebrew shows how contemporary speakers handle genre |
| `lat-VUL` | full | Latin Vulgate | OT + NT | Historic translation, rich genre tradition |
| `arb-NAV` | full | Arabic (New Arabic Version) | OT + NT | Afro-Asiatic, VSO word order, rich genre conventions |

## Additional Languages for Genre Feature (Validated)

Based on LANGUAGES.md control languages and genre marking strategies:

| Code | Language | Family | Genre Marking Strategy | Validated |
|------|----------|--------|------------------------|-----------|
| `deu-1912` | German (Luther 1912) | Indo-European | Connectives, word order, compound structures | ✓ (GEN.1.26) |
| `fra-LSG` | French (Louis Segond) | Indo-European | Similar to Spanish/English, connectives | ✓ (GEN.1.26) |
| `spa-BES` | Spanish (Biblia Español Sencillo) | Indo-European | Preterite/imperfect aspect for narrative | ✓ (available) |
| `ind-AYT` | Indonesian (Alkitab Yang Terbuka) | Austronesian | Particles, voice, topic-prominence | ✓ (GEN.1.26) |
| `rus-CARS` | Russian (Synodal) | Indo-European | Perfective/imperfective aspect distribution by genre | If available |
| `zho-CUV` | Chinese (Union Version) | Sino-Tibetan | Particles, aspect markers, topic-prominent | ✓ (GEN.1.26) |

## Rationale for Each Language

### English (eng-YLT)
- **Why**: Preserves word order and discourse particles from source
- **Genre marking**: Lexical connectives, punctuation, register
- **Validation**: All sample verses show clear narrative markers ("And God said")

### Greek (grc) - NT Source
- **Why**: Source language particles (γάρ, δέ, οὖν) signal discourse relationships
- **Genre marking**: Verb forms (aorist sequences), particles, formulas
- **Validation**: NT verses show epistolary formulas, narrative sequences

### Hebrew (hbo) - OT Source
- **Why**: Source language discourse patterns (wayyiqtol, parallelism)
- **Genre marking**: Verb chains, formulas, parallelism
- **Validation**: GEN.1.26 shows narrative wayyiqtol sequences

### Latin (lat-VUL)
- **Why**: Historic translation with established genre conventions
- **Genre marking**: Case system, word order, discourse markers
- **Validation**: Vulgate preserves formal/elevated style for sacred text

### Arabic (arb-NAV)
- **Why**: VSO language with complex verb patterns, classical genre tradition
- **Genre marking**: Verb patterns, particles (fa, thumma), word order shifts
- **Validation**: Arabic shows VSO narrative structure

### German (deu-1912)
- **Why**: Complex clause structures, verb-final subordinate clauses
- **Genre marking**: Connectives, word order, compound structures
- **Validation**: Luther Bible shows formal register for sacred narrative

### French (fra-LSG)
- **Why**: Similar Romance patterns to Spanish, literary tradition
- **Genre marking**: Tense/aspect, connectives, register
- **Validation**: French shows formal biblical register

### Spanish (spa-BES)
- **Why**: Preterite/imperfect distinction critical for narrative
- **Genre marking**: Verbal aspect, subjunctive for hortatory
- **Validation**: Spanish marks narrative foreground (preterite) vs background (imperfect)

### Indonesian (ind-AYT)
- **Why**: Austronesian topic-prominent structure, particle-based
- **Genre marking**: Particles, voice systems, topic markers
- **Validation**: Indonesian shows flexible genre marking via particles

### Russian (rus-CARS) [if available]
- **Why**: Perfective/imperfective aspect distribution varies by genre
- **Genre marking**: Aspect, particles, word order
- **Validation**: Russian aspect choice reflects narrative vs expository genre

### Chinese (zho-CUV)
- **Why**: Ancient literary tradition, particles signal discourse relations
- **Genre marking**: Particles, aspect markers, topic-prominence
- **Validation**: Chinese shows topic-comment structures, genre particles

## Translation Code Selection Strategy

- **Full codes** (`eng-YLT`, `lat-VUL`): Used when same version covers OT + NT
- **Prefix codes** (`grc`, `hbo`): Used when OT/NT have different versions
  - `grc` → OT: grc-LXX (Septuagint), NT: grc-BYZ or grc-SR (Byzantine/Stephanus)
  - `hbo` → OT only: hbo-WLC (Westminster Leningrad Codex)

## Final Translation List for Enrichment

```
eng-YLT,grc,hbo,heb-heb,lat-VUL,arb-NAV,deu-1912,fra-LSG,spa-BES,ind-AYT,zho-CUV
```

If `rus-CARS` is available in eBible corpus, add it. Otherwise use the 11 languages above.

## Notes

- Avoided duplicate language families where possible (only one English, one German, etc.)
- Prioritized languages that show **different genre marking strategies**:
  - Morphological: Spanish (aspect), Russian (aspect)
  - Syntactic: Arabic (VSO), Chinese (topic-prominence), Indonesian (voice)
  - Lexical: English (connectives), German (particles), French (register)
- All languages have rich written genre traditions (narrative, legal, epistolary, etc.)
- Total: 11 languages representing 5 major families + source languages
