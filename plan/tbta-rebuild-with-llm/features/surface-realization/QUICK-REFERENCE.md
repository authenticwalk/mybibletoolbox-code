# Surface Realization Quick Reference

## The Four Realization Types

| Type | Form | When to Use | Example |
|------|------|-------------|---------|
| **Noun** | Full lexical NP | First mention, emphasis, disambiguation | "Jesus went to the temple" |
| **Pronoun** | Standalone pronoun | Established, non-pro-drop languages | "He went to the temple" |
| **Zero** | ∅ (nothing) | Pro-drop languages, established topic | "∅ went to the temple" |
| **Clitic** | Reduced form on verb | Romance/Greek, obligatory | Spanish: "Lo vi" (I saw-it) |

## Pro-Drop by Language Family

### Full Pro-Drop (All persons, all contexts)
- **East Asian**: Chinese (Mandarin, Cantonese), Japanese, Korean, Vietnamese, Thai
- **Some Austronesian**: Indonesian, Javanese
- **Quechuan**: Quechua languages

### Subject Pro-Drop (Most persons)
- **Romance**: Spanish, Portuguese, Italian, Catalan, Galician
- **Some Trans-New Guinea**: Variable, context-dependent
- **Modern Greek**: Subject drop allowed

### Limited Pro-Drop (3rd person mainly)
- **Russian**: 3rd person only
- **Some Slavic**: Limited contexts
- **Polish**: Limited to infinitives

### Clitic-Based (Objects as clitics, subjects can drop)
- **Spanish, Portuguese, French, Italian, Romanian**: Obligatory clitics
- **Modern Greek**: Obligatory clitics
- **Balkan languages**: Complex clitic systems

### No Pro-Drop
- **English**: Pronouns required always
- **German, Dutch, Swedish**: Very limited
- **Most other Germanic**: No pro-drop

## Quick Decision Tree

```
Is this the first mention of this entity?
├─ YES → Use NOUN (all languages)
└─ NO → Is the language pro-drop?
        ├─ NO (English, German, etc.)
        │  └─ Use PRONOUN (required by grammar)
        └─ YES → Is there a clitic system?
                 ├─ YES (Spanish, Italian, French, etc.)
                 │  ├─ Subject → Can use ZERO or PRONOUN
                 │  └─ Object → Must use CLITIC
                 └─ NO (Japanese, Chinese, etc.)
                    └─ Use ZERO for established topic
                    └─ Use PRONOUN for emphasis/clarity
```

## Pro-Drop by Person/Number in Major Languages

| Language | 1sg | 2sg | 3sg | 1pl | 2pl | 3pl |
|----------|-----|-----|-----|-----|-----|-----|
| Spanish | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Portuguese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Italian | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| French | (✓) | (✓) | ✓ | (✓) | (✓) | ✓ |
| Russian | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| English | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Japanese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Mandarin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Korean | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

(✓) = allowed in some contexts; ✗ = not allowed

## Information Structure Guide

### First Mention (New Entity)
```
All languages: Use NOUN
"A rabbi came to the synagogue"
"Un rabino llegó a la sinagoga" (Spanish)
"Una rabino wa kita" (Japanese - indefinite)
```

### Established Topic (Same Subject as Previous Clause)
```
Pro-drop language: Use ZERO
"The disciples approached him. ∅ Asked about the future."
Spanish: "Los discípulos se acercaron. ∅ Preguntaron sobre el futuro."
Japanese: "弟子たちが近づいた。∅ 未来について尋ねた。"

Non-pro-drop language: Use PRONOUN
English: "The disciples approached him. They asked about the future."
German: "Die Jünger näherten sich. Sie fragten nach der Zukunft."
```

### Subject Change (Different Subject from Previous Clause)
```
All languages: Use NOUN or PRONOUN
"Jesus entered the temple. The disciples followed him."
Spanish: "Jesús entró al templo. Los discípulos lo siguieron."
         or "Jesús entró al templo. Ellos lo siguieron." (emphatic)
```

### Emphasis/Contrast
```
Even pro-drop languages use explicit forms
Spanish: "Yo voy" (emphatic "I" go, not you)
Japanese: "私が行く" (I-emph go, emphasizing that it's specifically I)
```

### Object Reference (Romance Languages)
```
Spanish: "vi a Juan" (I saw ACC Juan)
→ "lo vi" (I saw-him CL) - clitic required in casual speech
→ "a él lo vi" (to him him-CL I-saw) - emphatic, clitic + noun

French: "J'ai vu Jean"
→ "Je l'ai vu" (I him-CL have seen) - clitic required
```

## Common Errors and Fixes

### Error 1: Overusing Pronouns in Pro-Drop Languages
**Wrong**: "Jesús entró al templo. Él miró alrededor. Él habló a los discípulos."
**Right**: "Jesús entró al templo. ∅ Miró alrededor. ∅ Habló a los discípulos."
**Why**: Spanish naturally drops established subjects; explicit pronouns are emphatic

### Error 2: Forgetting Clitics in Romance Languages
**Wrong**: Spanish "Vi a María" (I saw to Mary) + another clause "Le pregunté" (to-her asked)
**Missing**: The clitic "le" is obligatory, not optional
**Right**: Consistent use of "le" for indirect objects: "Le pregunté" (to-her I-asked)

### Error 3: Using Zero in Non-Pro-Drop Languages
**Wrong**: English "*Went to the temple" (zero subject)
**Right**: "He went to the temple" (explicit pronoun)
**Why**: English grammar requires explicit subjects

### Error 4: Inconsistent Participant Tracking
**Wrong**: Same character sometimes noun, sometimes pronoun, sometimes zero with no pattern
**Right**: Develop consistent strategy:
- Noun for first mention
- Zero for 1-2 subsequent clauses (if pro-drop language)
- Pronoun if distance increases or reintroduction needed

### Error 5: Ignoring Register
**Wrong**: Using casual pro-drop patterns in formal/liturgical Bible text
**Right**: Match register:
- Formal/liturgical: More explicit nouns
- Narrative: More natural pro-drop
- Epistolary: Varies by tradition

## Pro-Drop Language Families in Our TSV

### By Count
1. **Austronesian** (176 languages): Mostly moderate to high pro-drop
2. **Trans-New Guinea** (141 languages): Highly variable, often with switch-reference
3. **Indo-European** (135 languages):
   - Romance subgroup: High pro-drop
   - Slavic subgroup: Limited pro-drop
   - Germanic subgroup: No pro-drop
4. **Niger-Congo** (89 languages): Variable
5. **Sino-Tibetan** (18 languages): East Asian = high pro-drop
6. **Quechuan** (18 languages): High pro-drop
7. **Afro-Asiatic** (25 languages): Varies (Arabic high, Hebrew limited)

### Regions with Extensive Pro-Drop
- **East Asia**: Nearly all pro-drop (Chinese, Japanese, Korean, Vietnamese, Thai)
- **Southeast Asia/Pacific**: Most Austronesian languages
- **Western Europe**: Most Romance languages
- **South America**: Many indigenous languages

### Regions with Limited/No Pro-Drop
- **Northern Europe**: Germanic languages (English, German, Dutch)
- **Parts of Africa**: Many Niger-Congo languages
- **Parts of Eastern Europe**: Some Slavic languages (Russian)

## Testing Checklist for Translations

For each participant in a passage, ask:

- [ ] Is this the first mention? → Use NOUN
- [ ] Is the language pro-drop? → Check constraints
- [ ] How far from previous mention? → Affects choice
- [ ] Is the entity still the discourse topic? → Affects choice
- [ ] Is there emphasis or contrast? → Use NOUN or PRONOUN
- [ ] What's the register? → Affects choice
- [ ] Does the language have clitics? → Check if applicable
- [ ] Is the realization consistent with similar passages? → Check pattern
- [ ] Would a native speaker find this natural? → Best validation

## Key Concept: Pro-Drop Hierarchy

If a language allows pro-drop, it typically follows this pattern:

```
Subject > Object (pro-drop more likely for subjects)
3rd person > 2nd person > 1st person (in some languages)
Main clause > Embedded clause (in some languages)
Animate > Inanimate (in some languages)
Salient topics > Low-salience entities (discourse-driven)
```

**Implication**: If your language allows object pro-drop, it definitely allows subject pro-drop. If it allows 2nd person drop, it allows 1st person drop.

## Resources in This Documentation

- **README.md**: Comprehensive feature overview with language-specific details
- **LEARNINGS.md**: Key findings and translator implications
- **experiment-001.md**: Detailed testing methodology and case studies
- **QUICK-REFERENCE.md**: This document - quick lookup tables and decision trees

## For Tool Development

**Input needed from language metadata**:
- Pro-drop type: none/limited/moderate/extensive
- Which persons drop (if limited)
- Clitic system: yes/no; type if yes
- Topic/focus prominence
- Register conventions
- Switch-reference: yes/no

**Analysis needed from discourse context**:
- Previous mention distance
- Discourse topic status
- Information structure
- Register/style
- Clause type (main/embedded)
- Semantic role (agent/patient/etc.)

**Output for translators**:
- Surface realization type recommendation
- Confidence level
- Explanation of choice
- Alternative options (if applicable)
- Register considerations
