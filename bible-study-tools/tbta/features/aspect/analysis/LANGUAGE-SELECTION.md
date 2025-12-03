# Language Selection for Aspect Feature

## Selected Translations

### Core Languages (Required)
- `eng-YLT` - Young's Literal Translation (both OT and NT) - English baseline
- `grc` - Greek (NT=grc-BYZ/others, OT=grc-LXX) - Source language NT
- `hbo` - Hebrew (OT only, hbo-WLC) - Source language OT
- `heb-heb` - Modern Hebrew (both OT and NT)
- `lat-VUC` - Latin Vulgate Clementine (both OT and NT) - Historical
- `arb-NAV` - Arabic (both OT and NT) - Semitic, marks aspect
- `deu-1912` - German Luther 1912 (both OT and NT) - Germanic
- `fra-LSG` - French Louis Segond (both OT and NT) - Romance
- `spa-BES` - Spanish (both OT and NT) - Romance
- `ind-AYT` - Indonesian (both OT and NT) - Austronesian

### Additional Languages That Mark Aspect
- `rus-SYN-1876` - Russian (both OT and NT) - Slavic, marks aspect grammatically
- `pol-UBG` - Polish (both OT and NT) - Slavic, marks aspect grammatically
- `bul` - Bulgarian (both OT and NT) - Slavic, marks aspect grammatically
- `ces` - Czech (both OT and NT) - Slavic, marks aspect grammatically
- `zho-CUV-SIMP` - Chinese Simplified (both OT and NT) - Aspect particles
- `tur-YTC` - Turkish (both OT and NT) - Turkic, aspect marking
- `swh` - Swahili (both OT and NT) - Niger-Congo, 5-way aspect system
- `tgl` - Tagalog (both OT and NT) - Austronesian, aspect-voice interaction

## Rationale

### Core Languages
These are required per instructions and provide:
- Source languages (Hebrew, Greek) for biblical text understanding
- Literal translation (YLT) for close formal correspondence
- Major European languages (Latin, German, French, Spanish) for translation tradition
- Major world languages (Arabic, Indonesian) with different linguistic features

### Additional Aspect-Marking Languages

**Slavic Languages (Russian, Polish, Bulgarian, Czech)**:
- Grammatically encode perfective/imperfective aspect
- Will clearly show aspect distinctions in verbal morphology
- Can validate TBTA aspect annotations against native aspect-marking systems

**Chinese**:
- Uses aspect particles (了 le, 着 zhe, 过 guo) to mark completion, duration, experience
- Different system from Slavic but equally relevant for aspect

**Turkish**:
- Marks aspect through verbal suffixes
- Progressive, habitual, and completive aspects encoded

**Swahili**:
- Niger-Congo language with 5-way aspect system (Factative, Imperfective, Perfect, Progressive, Habitual)
- Richer than binary perfective/imperfective distinction
- Major African language, valuable for testing complex aspect systems

**Tagalog**:
- Austronesian language with 4-way aspect system plus outer markers
- Aspect morphology interacts with voice system through infixes
- Tests aspect-voice interaction, different from Slavic paradigm

## Validation Notes

1. **GEN.1.1** - "In beginning created God the heavens and the earth"
   - Hebrew: בָּרָ֣א (bara) - perfective form
   - Greek LXX: ἐποίησεν (epoiesen) - aorist (perfective)
   - Russian: сотворил - perfective aspect
   - Can clearly identify aspect marking in source and target languages

2. **MAT.4.19** - "Come after me, and I will make you fishers of men"
   - Greek: ποιήσω (poieso) - future tense, aspect implications
   - Slavic languages will show aspect clearly in translation choices

Total translations: 18 (10 core + 8 additional aspect-marking)
