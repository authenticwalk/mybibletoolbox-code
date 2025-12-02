# TBTA Verse Generation (Compressed)

> NIV → Controlled Natural Language via 5 transforms + notation

## Input
NIV verse + reference

## Process

```
1. COPY NIV base text
2. SEGMENT clauses (one predicate each)
3. RESOLVE coreference (pronouns → nouns)
4. RELATIVIZE appositives (→ bracketed clauses)
5. SUBSTITUTE L2/L3 vocabulary (LDV pairings)
6. MARK deixis, imperatives, quotes
7. ADD implicit context (from Greek/Hebrew/culture)
```

## Transforms

| Step | Technique | Example |
|------|-----------|---------|
| Segment | Clause segmentation | "X and Y" → "X. Y." |
| Resolve | Coreference resolution | "he" → "John" |
| Relativize | Explicit relativization | "X, king" → "X, [who was king]" |
| Substitute | LDV substitution | "harvest" → "gather/harvest" |
| Mark | Deixis marking | "I" → "I(Speaker)" |

## Source Exceptions

**From NIV, EXCEPT**:
- Pronouns → explicit nouns
- "LORD" → "Yahweh"
- Compound → segmented
- Idioms → decomposed
- L2+ → paired/explicated

**ADD from Hebrew/Greek/scholarship**:
- Cultural context `(implicit-info)`
- Historical notes `(footnote)`
- Participant tracking

## Notation

| Pattern | Syntax |
|---------|--------|
| Subordinate | `[who/that/which...]` |
| Patient | `knew [X happened]` |
| Purpose | `[in order to...]` |
| Quote | `X said, ["first]. rest."` |
| Imperative | `You(X) (imp) verb` |
| Deixis | `I(Name)`, `my(Name's)` |
| L2 pair | `simple/complex` |
| Implicit | `(implicit-info)` |

## Validation

1. **Coreference**: No he/she/it/they
2. **Segmentation**: One verb per sentence
3. **Brackets**: All subordinates enclosed
4. **LDV**: L2+ words paired
5. **Deixis**: All 1st/2nd marked

## Self-Check
> Can this be translated word-for-word into any language without cultural assumptions?
