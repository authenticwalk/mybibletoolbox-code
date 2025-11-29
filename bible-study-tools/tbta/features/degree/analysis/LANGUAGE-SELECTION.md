# Language Selection for Degree Feature Analysis

## Selection Criteria

Degree systems (comparative, superlative, intensification) are marked differently across languages. Selected languages based on:

1. **Core translations required** (OT/NT coverage)
2. **Morphological degree marking** (languages that grammatically mark comparison)
3. **Lexical/syntactic degree marking** (useful for contrast)

## Selected Translations

### Core Languages (Required)

| Code | Language | Testament Coverage | Reason |
|------|----------|-------------------|--------|
| `eng-YLT` | English (Young's Literal) | Both OT & NT | Literal translation, preserves source patterns |
| `grc` | Greek | Prefix match (NT primary) | Original NT language, rich degree morphology |
| `hbo` | Hebrew | Prefix match (OT only) | Original OT language, construct state patterns |
| `heb-heb` | Modern Hebrew | Both OT & NT | Modern degree marking patterns |
| `lat-VUC` | Latin (Vulgate Clementine) | Both OT & NT | Classical comparative/superlative morphology |
| `arb-NAV` | Arabic (Van Dyke) | Both OT & NT | Elative and comparative patterns |

### Additional Helpful Languages (3-5 languages)

| Code | Language | Testament Coverage | Reason for Selection |
|------|----------|-------------------|---------------------|
| `deu-1912` | German (Luther 1912) | Both OT & NT | Germanic comparison with -er/-est patterns |
| `fra-LSG` | French (Louis Segond) | Both OT & NT | Romance degree marking (plus/moins) |
| `spa-BES` | Spanish (Biblia Reina Valera) | Both OT & NT | Romance comparison patterns |
| `rus` | Russian | Prefix match | Slavic degree morphology (prefixes, suffixes) |
| `cmn` | Mandarin Chinese | Prefix match (NT primary, 33% coverage) | Sino-Tibetan particle-based system (更 gèng, 最 zuì), 1.1B speakers |
| `ind-AYT` | Indonesian (Alkitab Yang Terbuka) | Both OT & NT (99% coverage) | Austronesian analytic system (lebih/paling) |
| `swh` | Swahili | Prefix match (99% coverage) | Niger-Congo postposed degree words (zaidi, kuliko) |

## Translation Code Format Notes

- **Full code** (e.g., `eng-YLT`): Used when translation exists in BOTH OT and NT
- **Prefix code** (e.g., `grc`, `hbo`): Used when OT/NT have different versions
  - `grc` matches: NT=grc-BYZ or grc-SR, OT=grc-BRENT (LXX)
  - `hbo` matches: OT=hbo-WLC only

## Validation Notes

Languages selected provide:
- **Morphological markers**: Latin, Greek, German, Russian show inflectional degree
- **Periphrastic markers**: English, French, Spanish use "more/most" constructions
- **Construct patterns**: Hebrew, Arabic show different strategies
- **Literalness spectrum**: YLT (most literal) to modern translations (more dynamic)

This diversity helps identify:
- When degree is explicit vs. implicit
- How languages handle intensification
- Comparative and superlative strategies
- Adversarial cases (e.g., "better" vs. "more good")

## Expected Coverage

With these 13 translations, we should be able to:
1. Identify the target word/phrase in most verses
2. See how different language families mark degree
3. Validate TBTA annotations against translator choices
4. Discover patterns for algorithmic prediction

## Language Family Representation

The selected translations represent key typological diversity:
- **Indo-European**: English, Latin, German, French, Spanish, Russian (morphological + analytic)
- **Afro-Asiatic**: Hebrew, Arabic (periphrastic + templatic morphology)
- **Sino-Tibetan**: Mandarin Chinese (particle-based)
- **Austronesian**: Indonesian (analytic)
- **Niger-Congo**: Swahili (postposed degree words)

---

*Created: 2025-11-29 for Stage 2.1 dataset enrichment*
*Updated: 2025-11-29 - Added cmn, ind-AYT, swh for typological diversity*
