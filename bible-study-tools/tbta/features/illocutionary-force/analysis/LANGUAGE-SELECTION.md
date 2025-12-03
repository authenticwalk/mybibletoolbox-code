# Language Selection for Illocutionary Force Feature

## Selection Criteria

Based on `/workspace/bible-study-tools/tbta/features/illocutionary-force/research/LANGUAGES.md`:

1. **Core languages** (required): eng-YLT, grc, hbo, heb-heb, lat-VUC, arb-NAV
2. **Mandatory-marking languages**: Languages that grammatically require illocutionary force marking
3. **Typological diversity**: Represent different language families and marking strategies
4. **Validation**: Can identify target constituent in sample verses and know grammatical rules

## Selected Languages

### Core Languages (6)

| Code | Language | Testament | Rationale |
|------|----------|-----------|-----------|
| `eng-YLT` | Young's Literal Translation | Both | Literal English baseline, explicit force marking |
| `grc` | Koine Greek | NT | NT source language, 4-mood system (indicative/subjunctive/optative/imperative) |
| `hbo` | Biblical Hebrew | OT | OT source language, explicit volitional forms (imperative/cohortative/jussive) |
| `heb-heb` | Modern Hebrew | Both | Continuity with Biblical Hebrew, modern usage |
| `lat-VUC` | Latin Vulgate | Both | Historical base, mood system for force |
| `arb-NAV` | Arabic (Van Dyck) | Both | Semitic like Hebrew, mandatory interrogative particles, jussive mood |

### Mandatory-Marking Languages (5)

| Code | Language | Family | Marking Strategy | Rationale |
|------|----------|--------|------------------|-----------|
| `kor` | Korean | Koreanic | Verb ending suffixes | Sentence type embedded in 6+ politeness levels; critical for Asian mission work |
| `tur` | Turkish | Turkic | Interrogative suffix -mI | Agglutinative morphology, explicit interrogative marking |
| `tgl` | Tagalog | Austronesian | Sentence-final particles (ba, nga, naman) | Philippine-type Austronesian, interrogative/emphasis particles |
| `ind-ind` | Indonesian | Austronesian | Optional particle -kah | Austronesian without Philippine particles, formal register marking |
| `tha` | Thai | Tai-Kadai | Sentence-final particles | Tonal language with mandatory sentence-final marking |

### Optional-Marking Languages (4)

| Code | Language | Family | Marking Strategy | Rationale |
|------|----------|--------|------------------|-----------|
| `deu-1912` | German (Luther 1912) | Indo-European (Germanic) | Word order + particles | Theological tradition, V2/V1 word order for interrogatives |
| `fra-LSG` | French (Louis Segond) | Indo-European (Romance) | Intonation OR est-ce que OR inversion | Multiple interrogative strategies, Romance representative |
| `spa-BES` | Spanish | Indo-European (Romance) | Intonation + ¿...? orthography | Major global language, subjunctive for jussive force |
| `swh-ONEN` | Swahili | Niger-Congo (Bantu) | Intonation, optional je particle | East African lingua franca, Bantu representative |

## Total: 15 Languages

- **6 Core** (baseline + source languages)
- **5 Mandatory-marking** (East Asian, Turkic, Austronesian, Tai-Kadai)
- **4 Optional-marking** (Indo-European, Niger-Congo)

## Validation Sample Verses

### Genesis 1:3 - "Let there be light" (Jussive)

Validated that target constituent (יְהִי "let there be") is identifiable in:
- Hebrew (hbo): יְהִי אֹור (yehi 'or) - jussive form visible
- Greek (grc): Γενηθήτω φῶς (genēthētō phōs) - aorist imperative passive
- Arabic (arb-NAV): ليكن نور (li-yakun nūr) - jussive mood visible
- Korean (kor): 빛이 있으라 (bichi iss-eura) - jussive ending -eura
- Turkish (tur): Işık olsun - optative mood (jussive function)
- Indonesian (ind-ind): Jadilah terang - imperative form for jussive
- Spanish (spa): Sea la luz - subjunctive for jussive
- German (deu): Es werde Licht - subjunctive for jussive
- French (fra): Que la lumière soit - subjunctive for jussive
- Tagalog (tgl): Magkaroon ng liwanag - actor-focus imperative
- Swahili (swh): Iwepo nuru - subjunctive/jussive form

All languages clearly mark the jussive force, making them valid for training data.

## Notes

- Using `grc` (prefix) instead of full code because OT=grc-BRENT, NT varies (grc-BYZ/SR)
- Using `hbo` (prefix) for OT only (hbo-WLC)
- All other codes are full `{lang}-{version}` format covering both testaments
- Thai (tha) added for Tai-Kadai representation and mandatory particle system
- Swahili (swh-ONEN) provides African Bantu perspective
