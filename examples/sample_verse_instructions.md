# Sample Verse Analysis Instructions

This is a sample instruction file for the verse_parser.py script.

## Task

Analyze the given Bible verse and provide:

1. **Source Language Analysis**: Identify key Greek/Hebrew words and their meanings
2. **Translation Comparison**: Compare how different translations render key phrases
3. **Theological Themes**: Identify main theological concepts
4. **Cross-References**: Find related verses that expand on the same theme
5. **Cultural Context**: Note any cultural or historical context needed for understanding

## Output Format

Provide your analysis in YAML format with the following structure:

```yaml
verse: {VERSE_REF}
source_language:
  - word: {original word}
    transliteration: {transliteration}
    strongs: {strongs number}
    meaning: {definition}
translation_notes:
  - translation: {translation key}
    text: {verse text}
    note: {any notable rendering}
themes:
  - {theme 1}
  - {theme 2}
cross_references:
  - ref: {verse ref}
    note: {relationship}
cultural_context: |
  {multi-line cultural context}
sources:
  - {source citation}
```

## Guidelines

- Always cite sources using inline format: {source-id}
- Use standardized verse references: BOOK.CCC.VVV
- Follow STANDARDIZATION.md for book codes and formatting
- Never fabricate translations - only use data from provided context
- If data is missing, indicate clearly rather than guessing

## Example

For Matthew 5:3 (MAT.005.003):

```yaml
verse: MAT.005.003
source_language:
  - word: μακάριοι
    transliteration: makarioi
    strongs: G3107
    meaning: blessed, happy, fortunate
  - word: πτωχοὶ
    transliteration: ptōchoi
    strongs: G4434
    meaning: poor, destitute, helpless
translation_notes:
  - translation: eng-ESV
    text: "Blessed are the poor in spirit"
    note: "Emphasizes spiritual poverty, not material"
themes:
  - BT750/beatitudes
  - BV210/humility
cross_references:
  - ref: LUK.006.020
    note: "Luke's parallel account"
  - ref: ISA.057.015
    note: "OT background on God dwelling with the humble"
cultural_context: |
  In 1st century Jewish culture, "poor in spirit" contrasted with
  the religious pride of some Pharisees. The phrase indicates
  spiritual humility and recognition of one's need for God.
sources:
  - grc-NA28
  - eng-ESV
  - llm-cs45
```
