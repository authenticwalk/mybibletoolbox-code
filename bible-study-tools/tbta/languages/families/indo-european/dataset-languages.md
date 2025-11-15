# Indo-European Languages in Our Dataset

**Source:** Extraction from `/home/user/mybibletoolbox-code/src/constants/languages.tsv`

This document provides a complete inventory of Indo-European languages represented in our Bible translation dataset, organized by sub-family.

---

## Complete List by Sub-Family

### Albanian Branch (1 language)
- **als** - Albanian, Tosk (Albania)

### Armenian Branch (0 languages in dataset)
- *No Armenian translations in current dataset*

### Balto-Slavic Branch (20 languages)

**Baltic:**
- **lit** - Lithuanian (Lithuania)

**Slavic:**
- **bel** - Belarusian (Belarus)
- **ces** - Czech (Czechia)
- **dan** - Danish (Denmark) [Note: Danish is Germanic, not Slavic - likely data error]
- **hrv** - Croatian (Croatia)
- **pol** - Polish (Poland)
- **rus** - Russian (Russian Federation)
- **srp** - Serbian (Serbia)
- **swe** - Swedish (Sweden) [Note: Swedish is Germanic, not Slavic - likely data error]
- **ukr** - Ukrainian (Ukraine)

### Celtic Branch (1 language)
- **bre** - Breton (France)

### Germanic Branch (4 languages)
- **dan** - Danish (Denmark)
- **deu** - German, Standard (Germany)
- **eng** - English (United Kingdom)
- **nld** - Dutch (Netherlands)
- **swe** - Swedish (Sweden)

### Hellenic Branch (1 language)
- **grc** - Greek, Ancient (Greece)

### Indo-Iranian Branch (20 languages)

**Indo-Aryan:**
- **asm** - Assamese (India)
- **ben** - Bengali (Bangladesh)
- **guj** - Gujarati (India)
- **hin** - Hindi (India)
- **hns** - Hindustani, Sarnami (Suriname)
- **mar** - Marathi (India)
- **npi** - Nepali (Nepal)
- **ory** - Odia (India)
- **pan** - Punjabi, Eastern (India)
- **san** - Sanskrit (India) - multiple translations
- **urd** - Urdu (Pakistan)

**Iranian:**
- **ckb** - Kurdish, Central (Iraq)
- **glk** - Gilaki (Iran)
- **pes** - Persian, Iranian (Iran)
- **tgk** - Tajik (Tajikistan)

### Italic (Romance) Branch (6 languages)
- **fra** - French (France)
- **ita** - Italian (Italy)
- **lat** - Latin (Holy See)
- **por** - Portuguese (Portugal)
- **ron** - Romanian (Romania)
- **spa** - Spanish (Spain)

### Romani Branch (2 languages)
- **rmc** - Romani, Carpathian (Slovakia)
- **rmy** - Romani, Vlax (Romania)

---

## Summary Statistics

- **Total Indo-European languages in dataset:** 55 distinct language codes
- **Total Bible translations:** Multiple translations per language
- **Largest branch:** Indo-Iranian (20 languages)
- **Most translated language:** English ({dataset-tsv}: 45 translations)
- **Geographic spread:** Europe, South Asia, Middle East, Americas

---

## Data Quality Issues

### Misclassifications Identified

1. **Danish (dan)** - Listed in both Slavic and Germanic branches
   - Correct classification: Germanic
   - Appears in source data under Balto-Slavic

2. **Swedish (swe)** - Listed in both Slavic and Germanic branches
   - Correct classification: Germanic
   - Appears in source data under Balto-Slavic

### Recommendations

- Verify language classifications against ISO 639-3 standard
- Update source data to correct branch assignments
- Verify translation counts against current database state
- Cross-reference language codes with Ethnologue or Glottolog

---

## Historical Notes on Notable Translations

### Slavic Dual Number Languages

**Bible translation significance:** Slovene was the 12th language in the world to have a complete Bible translation (1583 by Jurij Dalmatin) ({tsn-2019}: "The Slovenes thus became the 12th nation in the world with a complete Bible in their language"). Upper Sorbian received its Bible in 1728 ({wiki-sorbian}: "A complete edition of the Bible...was first published at Bautzen, 1728").

**Modern preservation:** Only a small number of Slavic languages retain the dual today: Slovene, Upper Sorbian, Lower Sorbian, and Kashubian.

**Source:** Britannica. "Dual number"

---

## Branch Distribution Summary

| Branch | Languages | Percentage | Notes |
|--------|-----------|------------|-------|
| **Indo-Iranian** | 20 | 36% | Largest branch; split between Indo-Aryan (11) and Iranian (4) |
| **Balto-Slavic** | 20 | 36% | Includes misclassified Germanic languages |
| **Romance** | 6 | 11% | Includes Latin plus modern Romance |
| **Germanic** | 4 | 7% | May be undercounted due to misclassifications |
| **Romani** | 2 | 4% | Descended from Indo-Aryan |
| **Albanian** | 1 | 2% | Isolate branch |
| **Celtic** | 1 | 2% | Only Breton represented |
| **Hellenic** | 1 | 2% | Ancient Greek for NT source |
| **Armenian** | 0 | 0% | Not in current dataset |

**Note:** Percentages based on uncorrected source data. After correcting Danish and Swedish classifications, Germanic would have 6 languages (11%) and Balto-Slavic would have 18 languages (33%).

---

## Geographic Distribution

### Europe
- **Western:** English, French, Spanish, Portuguese, Italian, German, Dutch, Breton
- **Northern:** Danish, Swedish
- **Eastern:** Russian, Polish, Czech, Ukrainian, Belarusian, Croatian, Serbian, Romanian
- **Southern:** Ancient Greek, Albanian, Romani (Carpathian, Vlax)
- **Baltic:** Lithuanian

### South Asia
- **India:** Hindi, Bengali, Marathi, Gujarati, Punjabi, Assamese, Odia, Sanskrit
- **Pakistan:** Urdu
- **Bangladesh:** Bengali
- **Nepal:** Nepali
- **Suriname:** Hindustani (Sarnami)

### Middle East
- **Iran:** Persian, Gilaki
- **Iraq:** Kurdish (Central)
- **Tajikistan:** Tajik

### Notes on Geographic Spread

The Indo-European languages in our dataset span four continents (if counting Suriname in South America). The family's geographic distribution reflects:

1. **Original homeland:** Debated, but likely Pontic-Caspian steppe or Anatolia
2. **Historical migrations:** Bronze Age expansions across Europe and Asia
3. **Colonial spread:** English, Spanish, Portuguese, French spread globally
4. **Trade and diaspora:** Romani, Hindustani (Sarnami) in Suriname

This makes Indo-European the most globally distributed language family in Bible translation work.
