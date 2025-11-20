# Language Family TBTA Feature Enhancement Plan

## Goal

Enhance each language family documentation with TBTA-relevant features unique to that family, using dominant languages as examples and noting important variants.

## Approach

For each family, add sections covering:

1. **Features unique to this family** (not in Greek/Hebrew source texts)
2. **Dominant language examples** showing how features work
3. **Important variants** within the family
4. **Translation implications** for Bible translation

## What NOT to Include

- ❌ Features that don't apply to this family
- ❌ Cross-reference matrices
- ❌ Redundant content already in features directory
- ❌ Trivial variants (only IMPORTANT ones)

## Enhancement Template

```markdown
## TBTA Translation Features

### [Feature Name] - ESSENTIAL/CRITICAL/RELEVANT

**What it is**: Brief description
**Why it matters**: Translation implication
**Pattern**: How it works in this family
**Dominant language example**: [Language] does X
**Variants**: [Language A] differs by Y

#### Biblical Examples
- Verse reference: Translation decision required
```

## By Language Family

### Austronesian (172 languages)

**Current state**: Has voice systems, clusivity, realis/irrealis documented
**Missing**:
- Dual/trial number specifics (which languages have it)
- Dominant examples (Tagalog for clusivity, Samoan for dual)
- Variants (Indonesian simplified voice vs Tagalog 4-voice)

**Add**:
1. **Clusivity** - with Tagalog kita/kami examples, note universal across family
2. **Voice/Focus** - with Tagalog examples, note Indonesian 2-voice variant
3. **Dual/Trial Number** - with Samoan examples, note Oceanic only
4. **Realis/Irrealis** - expand with examples

### Trans-New Guinea (127 languages)

**Current state**: Has switch-reference, evidentiality, SOV documented
**Missing**:
- Specific evidential systems (Fasu, Dani examples)
- Switch-reference with examples
- Elevation deixis specifics
- Highland vs lowland variants

**Add**:
1. **Switch-Reference** - with Amele examples, note nearly universal
2. **Evidentiality** - with Fasu examples, note highlands (~50 langs) vs lowlands (no evidentiality)
3. **Elevation Deixis** - examples of up/down marking

### Niger-Congo (98 languages)

**Current state**: Has noun classes, tone, aspect documented
**Missing**:
- Noun class specifics for Bible translation (abstract concepts)
- Tone grammatical functions
- Bantu vs non-Bantu variants

**Add**:
1. **Noun Classes** - with Swahili examples, note how abstract theological terms assigned
2. **Tone** - with examples of grammatical tone vs lexical
3. **Aspect-Prominence** - note aspect > tense pattern

### Indo-European (123 languages)

**Current state**: Has case, aspect, V2 documented
**Missing**:
- T-V distinctions (tu/vous)
- Slavic aspect as model for Greek
- Dual number (Slovenian, Sorbian)

**Add**:
1. **T-V Distinctions** - with French/German examples, note theological implications (addressing God)
2. **Slavic Aspect** - with Russian examples, note helps understand Greek aspect
3. **Dual Number** - with Slovenian examples, note rare (only 2 in dataset!)

### Mayan (22 languages)

**Current state**: Has ergative, classifiers, positionals, aspect documented
**Missing**:
- Dominant language examples (K'iche' is largest)
- Theological implications of classifiers

**Add**:
1. **Numeral Classifiers** - with K'iche' examples, note all languages have them
2. **Positional Verbs** - with Tzotzil examples, note unique to Mayan
3. **Ergative-Absolutive** - note different passive strategies than Greek

### Otomanguean (69 languages)

**Current state**: Has tone, VSO, complexity documented
**Missing**:
- Obligatory tone marking
- Whistled speech implications

**Add**:
1. **Universal Tonality** - note tone is obligatory, must be marked in writing
2. **Tone Levels** - with Trique 5-level example
3. **Whistled Speech** - note Zapotec, Chinantec, Mazatec

### Other-Families (70+ families)

**Need to identify**: Unique features for each small family
**Priority families**:
- **Quechuan** (18 langs): Evidentiality (3-way system)
- **Algic** (various): Obviation (4th person), animacy
- **East Asian** (various): Honorifics, topic, classifiers
- **Australian** (36 langs): Free word order, complex kinship

## Implementation Steps

1. **Read current family documentation** - understand what's there
2. **Identify missing TBTA features** - compare with features directory
3. **Add dominant language examples** - find major language in family
4. **Note important variants** - languages that differ from pattern
5. **Add Biblical implications** - how this affects translation

## Example: Austronesian Clusivity Section

```markdown
### Clusivity (Inclusive/Exclusive "We") - ESSENTIAL

**What it is**: First-person plural pronouns distinguish whether addressee is included (inclusive) or excluded (exclusive).

**Why it matters**: Critical for theological interpretation. "Let us make mankind" (Gen 1:26) - Trinity speaking (exclusive). "Our Father" (Matt 6:9) - believers including listeners (inclusive).

**Pattern**: Nearly universal across all 172 Austronesian languages. Typically two distinct pronouns.

**Dominant example - Tagalog**:
- `tayo` = inclusive (we including you)
- `kami` = exclusive (we not including you)

**Dominant example - Indonesian**:
- `kita` = inclusive
- `kami` = exclusive

**Variants**: None significant - feature is remarkably stable across entire family.

#### Biblical Translation Examples

**Genesis 1:26** - "Let us make mankind in our image"
- Decision: Exclusive (Trinity speaking to itself, not to humans)
- Tagalog: Use `kami`
- Theological implication: Clarifies Trinity doctrine

**Matthew 6:9** - "Our Father in heaven"
- Decision: Inclusive (Jesus teaching disciples, includes hearers)
- Tagalog: Use `tayo`
- Theological implication: Emphasizes shared relationship with God

**1 Corinthians 1:23** - "But we preach Christ crucified"
- Decision: Exclusive (Paul and apostles, not including Corinthians)
- Tagalog: Use `kami`
- Theological implication: Apostolic authority distinct from congregation
```

## Success Criteria

For each family:
✅ Dominant language examples provided
✅ Important variants noted
✅ Biblical translation implications clear
✅ Features organized by importance (ESSENTIAL/CRITICAL/RELEVANT)
✅ No irrelevant features included
✅ Clear, actionable for translators
