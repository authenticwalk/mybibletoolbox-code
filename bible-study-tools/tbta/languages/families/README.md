# Language Families Reference

This directory contains comprehensive linguistic reference material for major language families represented in Bible translation datasets. These resources support TBTA (Text-Based Translation Assistance) by providing:

- Linguistic features and patterns
- Translation challenges and strategies
- Language inventories from translation datasets
- Sub-family classifications
- Curated source references

## Available Language Families

### [Austronesian](./austronesian/)
One of the world's largest language families, spanning from Madagascar to Easter Island. Includes Malay, Tagalog, Indonesian, Hawaiian, and 1,200+ other languages. Known for symmetrical voice systems and complex morphology.

**Files**: 6 documents covering linguistic features, translation patterns, sub-families, and 200+ languages from translation datasets.

### [Trans-New Guinea](./trans-new-guinea/)
The world's third-largest language family by number of languages (300+), spoken across Papua New Guinea and neighboring regions. Features extreme linguistic diversity with complex verb morphology and varied phonological systems.

**Files**: 8 documents including grammatical features (split across 2 files), classification systems, translation guide, and comprehensive language inventory.

### [Indo-European](./indo-european/)
The most widely spoken language family globally, including English, Spanish, Hindi, Russian, and 400+ other languages. Well-documented with extensive scholarly resources and ancient written records.

**Files**: 7 documents covering branch profiles (split across 2 files), proto-language reconstruction, translation analysis, and dataset language inventory.

### [Niger-Congo](./niger-congo/)
Africa's largest language family with 1,500+ languages including Swahili, Yoruba, Zulu, and most Bantu languages. Characterized by noun class systems, tone, and agglutinative morphology.

**Files**: 6 documents covering linguistic features, sub-family organization, translation challenges, and dataset languages.

### [Mayan](./mayan/)
Mesoamerican language family with 22 languages spoken across Mexico, Guatemala, and Belize. Combined speaker population of 6-7 million. Known for ergative-absolutive alignment, extensive positional verb systems, numeral classifiers, and aspect-prominent verbal morphology.

**Files**: 2 documents covering overview/TBTA features and detailed linguistic analysis. **Languages**: 41 documented.

### [Otomanguean](./otomanguean/)
The oldest language family in the Americas (4400+ years) and the only fully tonal family in North/Central America. 69 languages in database with ~2.3 million speakers concentrated in Oaxaca, Mexico. Features complex tone systems (2-5 levels), VSO word order, consonant mutation, and infixation.

**Files**: 2 documents covering overview/TBTA features and detailed linguistic analysis. **Languages**: 69 documented.

### [Other Families](./other-families/)
Comprehensive collection covering 468 languages across 70+ language families not categorized as Austronesian, Trans-New Guinea, Niger-Congo, or Indo-European. Includes major families (Afro-Asiatic, Sino-Tibetan, Australian, Uto-Aztecan, Quechuan), medium families (Arawakan, Tucanoan, Tupian, Sepik, Torricelli), smaller families, language isolates, and creole languages.

**Files**: 7 documents organized by family size (major, medium-part1, medium-part2, smaller, minor-isolates-constructed) plus overview and sources. **Languages**: 468 total across 70+ families.

## Using These Resources

### For Translators
- Check **linguistic-features.md** or **grammatical-features** files for language-specific patterns
- Review **translation-features.md**, **translation-guide.md**, or **translation-challenges.md** for family-specific translation strategies
- Consult **language-inventory.md** or **dataset-languages.md** to see which languages from your family are in translation datasets

### For Researchers
- Start with family **README.md** for overview and key characteristics
- Review **sub-families.md** for classification details
- Check **sources.md** for scholarly references and further reading

### For TBTA Development
- Use linguistic feature descriptions to inform hint generation
- Reference translation challenges when developing family-specific assistance
- Consult language inventories to prioritize feature development

## File Organization

Each family directory follows a consistent structure:

- **README.md**: Overview, classification, key characteristics (≤400 lines)
- **linguistic-features.md** or **grammatical-features-\*.md**: Phonology, morphology, syntax patterns
- **translation-features.md**, **translation-guide.md**, or **translation-challenges.md**: Translation-specific guidance
- **language-inventory.md**, **language-list.md**, or **dataset-languages.md**: Languages in Bible translation datasets
- **sub-families.md**: Classification and sub-groupings
- **sources.md**: Curated scholarly references

## Progressive Disclosure

These files follow progressive disclosure principles:
- READMEs ≤200 lines (self-contained overviews)
- Other files ≤400 lines (focused topics)
- Larger topics split across multiple files (e.g., Indo-European branch profiles)

## Notes on Line Count Compliance

Some files currently exceed the 400-line guideline and may need future splitting:

**Austronesian**: All files compliant (largest: 323 lines)

**Trans-New Guinea**:
- sub-families.md: 379 lines (minor overage)
- All other files compliant

**Indo-European**:
- branch-profiles-1.md: 561 lines (already split topic, part 1)
- branch-profiles-2.md: 982 lines ⚠️ (needs further splitting)
- sources.md: 581 lines (needs splitting)
- translation-analysis.md: 592 lines (needs splitting)

**Niger-Congo**:
- README.md: 389 lines (minor overage)
- All other files compliant

Files marked ⚠️ should be prioritized for future splitting to maintain progressive disclosure standards.

## Parent Directory

See [../README.md](../README.md) for the main TBTA languages documentation.

## Contributing

When adding new language families:
1. Create family directory under `families/`
2. Include core files: README.md, linguistic-features, translation guidance, sources
3. Follow progressive disclosure: README ≤200 lines, other files ≤400 lines
4. Update this index with family description and file count
5. Ensure all sources are properly cited
