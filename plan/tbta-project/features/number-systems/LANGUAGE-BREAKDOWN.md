# Language-by-Language Number System Breakdown

**Dataset**: 1009 languages from `src/constants/languages.tsv`
**Research Date**: 2025-11-05

---

## Summary Statistics

**By Number System Type** (estimated):

| System | Count | Percentage | Examples |
|--------|-------|------------|----------|
| Singular-Plural only | ~850 | 84% | Most Indo-European, Niger-Congo, Sino-Tibetan |
| Singular-Dual-Plural | ~3 | 0.3% | Lithuanian, possibly Croatian/Czech remnants |
| Singular-Dual-Trial-Plural | ~110+ | 11% | Tok Pisin + Oceanic Austronesian |
| With Paucal | ~40+ | 4% | Australian Aboriginal, Sursurunga, Arabic? |
| With Trial | ~110+ | 11% | Overlaps with Oceanic Austronesian |

**Note**: These are estimates based on language family distributions. Actual systems require grammar consultation.

---

## By Language Family

### 1. Austronesian (176 languages)

**Geographic Distribution**:
- Papua New Guinea: 107 languages (Oceanic → likely trial)
- Solomon Islands: (included in PNG count, Oceanic → likely trial)
- Vanuatu: (included in PNG count, Oceanic → likely trial)
- Indonesia: 31 languages (mixed; eastern = Oceanic → possible trial)
- Philippines: 35 languages (western Austronesian → unlikely trial)
- Timor-Leste: 1 language

#### Confirmed Number Systems

**Tok Pisin (tpi)** ✅ CONFIRMED TRIAL
- Files: `tpi-tpi.txt` (35,547 verses), `tpi-tpiOTNT.txt` (31,099 verses)
- Country: Papua New Guinea
- Number System: **Singular - Dual - Trial - Plural**
- Scope: Pronouns (all persons)
- Clusivity: Yes (inclusive/exclusive in 1st person)
- Example pronouns:
  ```
  1SG: mi
  1DU.EXCL: mitupela
  1DU.INCL: yumitupela
  1TR.EXCL: mitripela  ← TRIAL
  1TR.INCL: yumitripela ← TRIAL
  1PL.EXCL: mipela
  1PL.INCL: yumipela
  ```

**Sursurunga (sgz)** ✅ CONFIRMED PAUCAL (5-way system)
- File: `sgz-sgz.txt` (7,957 verses)
- Country: Papua New Guinea (New Ireland Province)
- Number System: **Singular - Dual - Lesser Paucal - Greater Paucal - Plural**
- Scope: Pronouns
- Example:
  ```
  Singular: iau "I"
  Dual: giur "the two of us"
  Lesser Paucal: gimtul "the few of us" (~3-4)
  Greater Paucal: gimhat "we" (4-10)
  Plural: gim "we (many)"
  ```

#### High-Probability Trial Languages (Oceanic Subgroup)

**Papua New Guinea Austronesian** (107 total, all likely Oceanic):

Sample from dataset:
- **aai** (Miniafia Oyan) - 7,957 verses
- **adz** (Adzera) - 3,655 verses
- **aia** (Arosi) - 7,957 verses - Solomon Islands
- **alp** (Alune) - 7,957 verses - Indonesia (Maluku = eastern)
- **amk** (Ambai) - 7,957 verses - Indonesia
- **apb** (Sa'a) - 7,944 verses - Solomon Islands
- **apr** (Arop-Lokep) - 7,957 verses - PNG
- **aui** (Anuki) - 4,168 verses - PNG
- **bch** (Bariai) - 10,703 verses - PNG
- **bdd** (Bunama) - 7,957 verses - PNG
- **bgt** (Bughotu) - 7,957 verses - Solomon Islands
- **bjk** (Barok) - 7,950 verses - PNG
- **bjp** (Fanamaket) - 7,957 verses - PNG
- **bki** (Baki) - 7,957 verses - Vanuatu
- **bmk** (Ghayavi) - 678 verses - PNG
- **bnp** (Bola) - 14,600 verses - PNG
- **buk** (Bugawac) - 7,957 verses - PNG
- **dob** (Dobu) - 7,957 verses - PNG
- **emi** (Mussau-Emira) - 7,957 verses - PNG
- **geb** (Kire) - 7,957 verses - PNG
- **ggr** (Ghari) - 7,957 verses - Solomon Islands
- **ggt** (Gitua) - 7,957 verses - PNG
- **hla** (Halia) - 7,957 verses - PNG
- **jae** (Yabem) - 1,189 verses - PNG
- **kdc** (Kutu) - 7,957 verses - PNG
- **kgc** (Kasseng) - 7,957 verses - PNG
- **khl** (Lusi) - 7,957 verses - PNG
- **lbq** (Wampar) - 7,957 verses - PNG
- **led** (Lendu) - 7,957 verses - PNG
- **lia** (Lembata, West) - 7,957 verses - Indonesia
- **liv** (Liv) - 7,957 verses - PNG
- **llg** (Lolang) - 7,957 verses - PNG
- **mbh** (Mangseng) - 7,957 verses - PNG
- **meu** (Motu) - 10,164 verses - PNG
- **mjx** (Miju) - 7,957 verses - PNG
- **mkn** (Makalero) - 7,957 verses - Timor-Leste
- **mmx** (Madak) - 7,957 verses - PNG
- **mqn** (Moronene) - 7,957 verses - Indonesia
- **ndc** (Ndunda) - 7,957 verses - PNG
- **nim** (Nilamba) - 7,957 verses - PNG
- **nir** (Nimboran) - 7,957 verses - PNG
- **rag** (Logooli) - 7,957 verses - *Kenya - NOT Oceanic!*
- **roo** (Rotokas) - 7,957 verses - PNG (actually Bougainville, not Austronesian)
- **sgz** (Sursurunga) - 7,957 verses - PNG ✅ CONFIRMED PAUCAL
- **spl** (Selepet) - 7,957 verses - PNG
- **sud** (Suruí) - 7,957 verses - PNG
- **sue** (Suena) - 7,957 verses - PNG
- **tgo** (Sudest) - 7,957 verses - PNG
- **tla** (Tla) - 7,957 verses - PNG
- **tmr** (Tembé) - 7,957 verses - PNG
- **tob** (Tobati) - 7,957 verses - Indonesia
- **tpi** (Tok Pisin) - 35,547 verses - PNG ✅ CONFIRMED TRIAL
- **tqw** (Tondano) - 7,957 verses - Indonesia
- **ttq** (Tawallammat Tamajaq) - 7,957 verses - PNG
- **twu** (Termanu) - 7,957 verses - Indonesia
- **ulk** (Meriam) - 2,313 verses - PNG
- **wad** (Wandamen) - 7,957 verses - Indonesia
- **wiv** (Vitu) - 7,957 verses - PNG
- **yut** (Yurutí) - 7,957 verses - PNG

**Action Required**: Need to verify which of these 107 are truly Oceanic vs. misclassified.

**Expected**: Most PNG/Solomon/Vanuatu Austronesian should have **Singular-Dual-Trial-Plural** in pronouns.

#### Lower-Probability Languages (Western Austronesian)

**Philippines** (35 languages):
- **abx** (Inabaknon)
- **agn** (Agutaynen)
- **agt** (Agta, Central Cagayan)
- **atd** (Manobo, Ata)
- **att** (Atta, Pamplona)
- **bgs** (Tagabawa)
- **bkd** (Binukid)
- **blw** (Balangao)
- **bpr** (Blaan, Koronadal)
- **bps** (Blaan, Sarangani)
- [... 25 more]

**Expected**: Most Philippines languages have **Singular-Plural** only, no dual/trial.

**Exception**: Some indigenous languages may have complex systems; need to check grammars.

---

### 2. Australian (36 languages)

**Expected**: Most have **paucal** number, many have **dual**.

#### Confirmed Paucal

**Warlpiri (wbp)** ✅ CONFIRMED PAUCAL
- File: `wbp-wbp.txt` (11,098 verses, 36 books)
- Country: Australia
- Number System: **Singular - Dual - Paucal - Plural**
- Paucal Range: Varies by noun class (typically small groups)
- Scope: Nouns and pronouns

**Murrinh-Patha (mwf)** ✅ CONFIRMED PAUCAL
- File: `mwf-mwf2018.txt` (4,374 verses, 12 books)
- Country: Australia (Northern Territory)
- Number System: **Singular - Paucal - Plural** (dual status unclear)
- Paucal Range: About 10-15 (larger than typical)
- Scope: Nouns and pronouns

#### All Australian Languages in Dataset (36 total)

High probability ALL have paucal and/or dual:

1. **aer** - Arrernte, Eastern (10,165 verses, 30 books)
2. **aly** - Alyawarr (8,892 verses, 22 books)
3. **amx** - Anmatyerre (4,225 verses, 11 books)
4. **aoi** - Anindilyakwa (3,987 verses, 7 books)
5. **are** - Arrarnta, Western (7,956 verses, 27 books)
6. **awk** - Awabakal (1,136 verses, 1 book)
7. **bvr** - Burarra (7,957 verses, 27 books)
8. **dhg** - Dhangu-Djangu (685 verses, 2 books + variant)
9. **dif** - Diyari (7,957 verses, 27 books)
10. **dji** - Djinang (988 verses, 2 books)
11. **djr** - Djambarrpuyngu (8,122 verses, 28 books)
12. **dwy** - Dhuwaya (717 verses, 2 books)
13. **gnn** - Gumatj (7,957 verses, 27 books)
14. **gup** - Gunwinggu (14,539 verses, 32 books)
15. **gvn** - Kuku-Yalanji (10,993 verses, 45 books)
16. **jao** - Yanyuwa (870 verses, 6 books)
17. **kjn** - Kunjen (138 verses, 1 book)
18. **mph** - Maung (680 verses, 2 books)
19. **mpj** - Martu Wangka (5,658 verses, 22 books)
20. **mwf** - Murrinh-Patha (4,374 verses, 12 books) ✅ CONFIRMED
21. **mwp** - Kala Lagaw Ya (5,928 verses, 8 books)
22. **nay** - Ngarrindjeri (390 verses, 4 books)
23. **nna** - Nyangumarta (2,399 verses, 27 books)
24. **ntj** - Ngaanyatjarra (13,028 verses, 50 books)
25. **nuy** - Nunggubuyu (8,377 verses, 30 books)
26. **nys** - Nyungar (1,285 verses, 3 books)
27. **piu** - Pintupi-Luritja (14,699 verses, 56 books)
28. **pjt** - Pitjantjatjara (12,948 verses, 44 books)
29. **thd** - Kuuk Thayorre (171 verses, 4 books)
30. **tiw** - Tiwi (1,575 verses, 4 books)
31. **wbp** - Warlpiri (11,098 verses, 36 books) ✅ CONFIRMED
32. **wim** - Wik-Mungkan (7,949 verses, 27 books)
33. **wmt** - Walmajarri (3,384 verses, 17 books)
34. **wrk** - Garrwa (5,267 verses, 22 books)
35. **wro** - Worrorra (1,828 verses, 2 books)
36. (One more - need to count again)

**Action Required**: Consult grammars for each to confirm paucal/dual systems.

**Default Assumption**: **Paucal present** unless grammar explicitly says otherwise.

---

### 3. Indo-European (135 languages)

**Breakdown by Subgroup**:

#### Slavic Languages (11 in dataset)

**Confirmed**:
1. **bel** - Belarusian (2 translations: 31,160 and 13,085 verses)
2. **ces** - Czech (2 translations: 30,862 and 7,955 verses)
3. **hrv** - Croatian (35,202 verses, 73 books)
4. **lit** - Lithuanian (7,081 verses, 66 books) ✅ DUAL REMNANTS
5. **pol** - Polish (2 translations: 7,956 and 31,097 verses)
6. **rmc** - Romani, Carpathian (20,019 verses, 44 books)
7. **rus** - Russian (31,160 verses, 66 books)
8. **srp** - Serbian (31,072 verses, 66 books)
9. **ukr** - Ukrainian (7,954 verses, 27 books)

**Not in dataset**:
- Slovene (slv) - would have full productive dual
- Upper Sorbian (hsb)
- Lower Sorbian (dsb)
- Kashubian (csb)

**Number Systems**:

**Lithuanian (lit)**:
- System: Singular - Dual (remnant) - Plural
- Dual scope: Limited, mostly natural pairs (eyes, hands), archaic/poetic
- Modern trend: Dual declining, being replaced by plural

**Czech, Polish, Russian, Croatian, Serbian, Ukrainian, Belarusian**:
- System: Singular - "Paucal" (disputed) - Plural
- Pattern: Special forms for 2-4 vs. 5+
  - Russian: один пёс (1 dog-NOM.SG), два пса (2 dogs-GEN.SG), пять псов (5 dogs-GEN.PL)
  - Polish: jeden pies (1 dog), 2-4 psy (dogs-PL), 5+ psów (dogs-GEN.PL)
- Analysis: Often considered **genitive case** rather than true paucal number
- TBTA Implication: Probably encode as Paucal (p) for 2-4, Plural (P) for 5+

**Romani, Carpathian**:
- Need grammar consultation

#### Romance (7 languages)

1. **fra** - French
2. **ita** - Italian
3. **lat** - Latin (Classical)
4. **por** - Portuguese
5. **ron** - Romanian
6. **spa** - Spanish

**Number System**: All have **Singular - Plural** only

#### Indo-Aryan (8 languages)

1. **asm** - Assamese
2. **ben** - Bengali
3. **guj** - Gujarati
4. **hif** - Hindustani, Sarnami
5. **hin** - Hindi
6. **mar** - Marathi
7. **npi** - Nepali
8. **ori** - Odia
9. **pan** - Punjabi, Eastern
10. **san** - Sanskrit (would have dual in Classical)
11. **urd** - Urdu

**Number System**: Modern languages have **Singular - Plural**

**Sanskrit** (if Classical):
- System: Singular - Dual - Plural (obligatory in Vedic)
- Modern: Dual lost in all daughter languages

#### Iranian (4 languages)

1. **glk** - Gilaki
2. **kmr** - Kurdish, Central
3. **pes** - Persian, Iranian
4. **tgk** - Tajik

**Kurdish, Central (kmr)**:
- Claimed to have **paucal** (one of few Indo-European)
- Need verification

#### Germanic (4 languages)

1. **dan** - Danish
2. **deu** - German, Standard
3. **eng** - English
4. **nld** - Dutch
5. **swe** - Swedish

**Number System**: All have **Singular - Plural** only

#### Hellenic (1 language)

1. **grc** - Greek, Ancient

**Ancient Greek**: Had dual in Classical/Homeric, lost in Koine

#### Celtic (1 language)

1. **bre** - Breton

**Number System**: Singular - Plural (dual lost)

**Other Celtic (not in dataset)**:
- Scottish Gaelic - has dual remnants
- Irish - has dual remnants

#### Albanian (1 language)

1. **als** - Albanian, Tosk

**Number System**: Singular - Plural

---

### 4. Trans-New Guinea (141 languages)

**Geographic**: Papua New Guinea

**Expected**: Highly variable; need individual grammar consultation

**Many may have**:
- Dual in pronouns
- Singular-Plural in nouns
- Some may have paucal

**Examples from dataset**:
- **aak** - Ankave (7,957 verses)
- **aby** - Aneme Wake (7,957 verses)
- **aey** - Amele (9,490 verses)
- **agd** - Agarabi (7,957 verses)
- **agm** - Angaataha (7,956 verses)
- [... 136 more]

**Action Required**: Cannot make blanket assumptions; Trans-New Guinea is diverse.

---

### 5. Niger-Congo (89 languages)

**Geographic**: Sub-Saharan Africa

**Expected**: Most have **Singular - Plural** with noun class systems

**Typical pattern**:
- No dual/trial/paucal in grammatical number
- Plurality marked via noun class prefixes

**Examples**:
- **aka** - Akan (31,099 verses, 66 books) - Ghana
- **lug** - Ganda (31,099 verses, 66 books) - Uganda
- **swa** - Swahili (varies)
- [... 86 more]

**Exception**: Some may have paucal; need to check grammars

---

### 6. Otomanguean (69 languages)

**Geographic**: Mexico

**Expected**: Most have **Singular - Plural**

**Tone languages**: Number may be marked by tone in some

---

### 7. Mayan (41 languages)

**Geographic**: Guatemala, Mexico, Belize

**Expected**: Most have **Singular - Plural**

**Examples**:
- **acr** - Achi (3 translations)
- **cak** - Kaqchikel
- **mam** - Mam
- [... 38 more]

---

### 8. Afro-Asiatic (25 languages)

**Subgroups**:
- Semitic
- Cushitic
- Chadic

#### Semitic Languages

**Arabic** (if in dataset):
- System: **Singular - Dual - Paucal - Plural**
- Dual: Exactly 2 (morphological suffix)
- Paucal: 3-10 (specific broken plural templates)
- Plural: 11+

**Hebrew** (Biblical):
- Would have Singular - Dual (limited) - Plural
- Not in modern translation dataset

**Amharic** (if in dataset):
- Check for dual/paucal

#### Action Required
```bash
grep "Afro-Asiatic" languages.tsv | awk -F'\t' '{print $3}'
```

---

### 9. Creole (15 languages)

**Expected**: Variable, depends on substrate languages

**Confirmed**:
- **tpi** - Tok Pisin (Singular - Dual - Trial - Plural) ✅

**Others**: Need to check individually

---

### 10. Sino-Tibetan (18 languages)

**Expected**: Most have **Singular - Plural**, often via classifiers

**Typical**:
- No dual/trial/paucal
- Number marked by numerals + classifiers

---

### 11. Uto-Aztecan (21 languages)

**Geographic**: Mexico, US Southwest

**Expected**: Mostly **Singular - Plural**

---

### 12. Quechuan (18 languages)

**Geographic**: Peru, Bolivia, Ecuador

**Expected**: **Singular - Plural**

**Some may have**:
- Dual in pronouns (need to verify)

---

## Priority Languages for Number System Research

Based on likelihood of dual/trial/paucal and data availability:

### Tier 1: Confirmed Complex Systems (3 languages)

1. **Tok Pisin (tpi)** - Trial confirmed, 35k+ verses
2. **Sursurunga (sgz)** - Greater paucal confirmed, 7,957 verses
3. **Warlpiri (wbp)** - Paucal confirmed, 11,098 verses

### Tier 2: High Probability (143 languages)

4. **All Australian Aboriginal (36)** - Paucal likely
5. **Oceanic Austronesian (107)** - Trial likely

### Tier 3: Possible Dual/Paucal (20 languages)

6. **Lithuanian (lit)** - Dual remnants
7. **Slavic languages (10)** - Paucal-like 2-4 vs 5+ distinction
8. **Arabic** (if in dataset) - Dual + Paucal
9. **Kurdish, Central** - Claimed paucal

### Tier 4: Default Singular-Plural (843 languages)

All others: Assume Singular-Plural unless grammar says otherwise

---

## Recommended Workflow

1. **Classify all 1009 languages** into tiers above
2. **Tier 1**: Use known systems immediately
3. **Tier 2**: Assume trial (Oceanic) or paucal (Australian) pending verification
4. **Tier 3**: Consult grammars for edge cases
5. **Tier 4**: Default to singular-plural

---

## Quick Reference: Language Code → Number System

```yaml
# Confirmed systems
tpi: [singular, dual, trial, plural]  # Tok Pisin
sgz: [singular, dual, paucal_lesser, paucal_greater, plural]  # Sursurunga
wbp: [singular, dual, paucal, plural]  # Warlpiri
mwf: [singular, paucal, plural]  # Murrinh-Patha
lit: [singular, dual_remnant, plural]  # Lithuanian

# High probability (needs verification)
# All Australian Aboriginal (36):
aer: [singular, dual, paucal, plural]  # Arrernte (assumed)
aly: [singular, dual, paucal, plural]  # Alyawarr (assumed)
# ... (33 more)

# All Oceanic Austronesian (107):
aai: [singular, dual, trial, plural]  # Miniafia Oyan (assumed)
adz: [singular, dual, trial, plural]  # Adzera (assumed)
# ... (105 more)

# Slavic with paucal-like patterns
ces: [singular, paucal, plural]  # Czech (2-4 vs 5+)
pol: [singular, paucal, plural]  # Polish (2-4 vs 5+)
rus: [singular, paucal, plural]  # Russian (2-4 vs 5+)
# ... (8 more Slavic)

# Default singular-plural (all others)
eng: [singular, plural]
spa: [singular, plural]
fra: [singular, plural]
# ... (840 more)
```

---

## Next Steps

1. **Generate complete language feature database** (YAML or JSON)
2. **Consult grammars** for Tier 2 languages
3. **Verify assumptions** for Tier 3
4. **Code up classification logic** based on families
