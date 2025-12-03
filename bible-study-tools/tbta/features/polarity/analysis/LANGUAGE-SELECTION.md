# Language Selection for Polarity Feature Analysis

## Validation Process

Polarity (affirmative vs. negative) is a universal linguistic feature - all languages mark negation. The question is HOW they mark it (particles, affixes, tone, etc.).

### Sample Verses Used for Validation

1. **GEN.022.012** - "Do NOT lay a hand on the boy, do NOT do anything to him"
   - Clear multiple negative commands
   - Hebrew: אַל (al) negative imperative particle

2. **MAT.005.020** - "unless your righteousness... you will NOT enter"
   - Negative with future/conditional
   - Greek: οὐ μὴ (ou mē) emphatic double negative

## Core Required Languages

These languages MUST be included per instructions:

| Code | Format | Coverage | Reason |
|------|--------|----------|---------|
| `eng-YLT` | full | OT+NT | Young's Literal Translation - consistent negation rendering |
| `grc` | prefix | NT only | Greek source language - rich negation system (οὐ, μή, οὐ μή) |
| `hbo` | prefix | OT only | Biblical Hebrew - לֹא (lo), אַל (al) particles |
| `heb-heb` | full | OT+NT | Modern Hebrew Bible - full coverage |
| `lat-VUC` | full | OT+NT | Latin Vulgate Clementine - "non", "nec" particles |
| `arb-NAV` | full | OT+NT | Arabic Van Dyck - لا (lā), لم (lam) negation |
| `deu-1912` | full | OT+NT | German Luther - "nicht", "kein" negation |
| `fra-LSG` | full | OT+NT | French Louis Segond - "ne...pas", "ne...point" |
| `spa-BES` | full | OT+NT | Spanish Biblia Española - "no" particle |
| `ind-AYT` | full | OT+NT | Indonesian Alkitab Yang Terbuka - "tidak", "jangan" |

## Additional Selected Languages

Selected for clear polarity marking and typological diversity:

| Code | Format | Coverage | Negation Strategy | Example | Status |
|------|--------|----------|-------------------|---------|--------|
| `rus-SYN` | full | OT+NT | не (ne) particle + genitive case | "не делай" (don't do) | ✓ Available |
| `tha` | prefix | OT+NT | ไม่ (mâi) / อย่า (yàa) particles | ไม่ทำ (not do) | ✓ Available (tha-KJV) |
| `tur` | prefix | OT+NT | Agglutinative negative suffix -mA | yapmamak (not to do) | ✓ Available (tur-YTC) |
| `tgl` | prefix | OT+NT | Austronesian; hindi/huwag distinction | hindi gumawa (not do) | ✓ Available (tgl-ULB) |

**Note**: The following languages from research/LANGUAGES.md are NOT available in the eBible corpus:
- `por-JFA` (Portuguese) - not in eBible
- `ita-RIV` (Italian) - not in eBible
- `zho-CUV-SIMP` (Chinese) - not in eBible
- `jpn-JAP` (Japanese) - not in eBible
- `kor` (Korean) - not in eBible
- `swa-ONEN` (Swahili) - not in eBible
- `fin` (Finnish) - not in eBible (requested for addition but unavailable)

## Validation Results

For each selected language, I validated:
1. Can identify the target constituent in sample verses? ✓ YES for all
2. Can see clear negation marking? ✓ YES for all
3. Know the grammatical rules well enough to use as hints? ✓ YES for all

## Total Languages in Dataset: 13 unique translations

**Core languages** (10):
- eng-YLT, grc (grc-SR/grc-BYZ/grc-BRENT), hbo (hbo-hbo), heb-heb, lat-VUC, arb-NAV, deu-1912, fra-LSG, spa-BES, ind-AYT

**Additional languages** (4):
- rus-SYN, tha-KJV, tur-YTC, tgl-ULB

**Note**: Some language codes appear as multiple variants (e.g., grc-SR, grc-BYZ, grc-BRENT) depending on testament (OT uses grc-BRENT/BYZ, NT uses grc-SR).

## Polarity Marking Strategies Represented

1. **Particles** (most common): eng, grc, hbo, lat, arb, fra, spa, deu, rus, tha
2. **Affixes**: tur (agglutinative negative suffix)
3. **Discontinuous** (circumfix): fra "ne...pas"
4. **Multiple particles for different contexts**: arb (لا/لم), tha (ไม่/อย่า), tgl (hindi/huwag)
