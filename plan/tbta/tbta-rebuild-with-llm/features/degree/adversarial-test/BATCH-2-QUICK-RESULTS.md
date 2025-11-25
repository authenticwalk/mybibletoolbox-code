# Batch 2 Quick Results: Major Discoveries

**Date**: 2025-11-09
**Verses tested**: 29 (batch 2)
**Total verses**: 41 (12 previous + 29 batch 2)

---

## CRITICAL DISCOVERIES

### 1. **Intensified Comparative (i) EXISTS!** ✅

**Found in**: MAT 10:31
- "valuable": **Intensified Comparative**
- Previous conclusion: "i doesn't exist" → **WRONG**
- This value DOES exist in TBTA!

### 2. **'too' (Excessive T) EXISTS!** ✅

**Found in**: GEN 4:13
- "much": **'too'** (literal quoted value)
- Hebrew: גָּדוֹל עֲוֺנִי מִנְּשֹׂא "My punishment is too great to bear"
- T value confirmed to exist!

### 3. **'least' Confirmed Multiple Times** ✅

**Found in**:
- LUK 7:28: "important": **'least'**
- LUK 9:48: "important": **'least'**
- Earlier: MAT 5:19: '''least'''

---

## Value Inventory UPDATE

| Value | Previous Status | NEW Status | Evidence |
|-------|----------------|------------|----------|
| i (Intensified Comp) | ❌ Non-existent | ✅ **EXISTS** | MAT 10:31 |
| T (Excessive 'too') | ❓ Unknown | ✅ **EXISTS** | GEN 4:13 |
| l ('least' literal) | ✅ Exists as '''least''' | ✅ Confirmed | MAT 5:19, LUK 7:28, 9:48 |
| E (Extremely Intensified) | ❌ Likely doesn't exist | ❓ Still unknown | Not found yet |
| L (Less) | ❓ Unknown | ❓ Still unknown | Not found yet |
| q (Equative) | ❌ Non-existent | ❌ Still non-existent | PHP 2:6, MAT 10:25 |
| s (Superlative of 2) | ❌ Non-existent | ❌ Still non-existent | MAT 23:17 uses C not s |

---

## Batch 2 Patterns Observed

### Standard Comparatives (Most Common)
- MAT 6:25, 12:6, 12:41, 12:42, 20:31: **Comparative**
- JHN 1:50: **Comparative**
- LUK 11:31, 11:32, 12:7, 12:23, 12:24: **Comparative**
- EXO 18:11: **Comparative**

**Pattern**: Synthetic comparative forms (μείζων, πλεῖον) → Comparative

### Implied Superlatives
- MAT 11:9: **Superlative** (not just "more than prophet")
- LUK 7:28: **Superlative** + 'least' (parallel to MAT 11:11)

### Intensified Forms
- MAT 6:30: **Intensified** (not Comparative!)
- MAT 12:42: "wise": **Intensified**

### Mixed Patterns
- MAT 18:4: Both **Comparative** and **Superlative** in same verse
  - "great" appeared 4 times with mixed degrees
  - Shows context-dependent annotation

### Unexpected No Degree
- MAT 5:37, 10:15, 11:22, 11:24: No degree (expected Comparative)
- MAT 18:6, 21:36: No degree
- GEN 29:19: No degree

---

## Key Insights

### 1. Intensified vs Intensified Comparative Distinction

**Intensified** (I):
- MAT 6:30: "beautiful" → Intensified
- MAT 12:42: "wise" → Intensified

**Intensified Comparative** (i):
- MAT 10:31: "valuable" → Intensified Comparative

**Pattern**: Need to understand when TBTA uses "i" vs "I"
- Likely: "i" = "much more valuable" (πολλῶν... διαφέρετε)
- "I" = general intensification (λίαν, etc.)

### 2. Literal Value Expansion

**Found literal values**:
- '''least''' (MAT 5:19)
- 'least' (LUK 7:28, 9:48) - Note: NO triple quotes!
- 'too' (GEN 4:13)

**Encoding variation**: Sometimes triple quotes, sometimes single quotes

### 3. Hebrew Constructions

**GEN 4:13**: מִן construction → 'too' (not Comparative!)
**EXO 18:011**: מִכָּל "from all" → Comparative (not Superlative)

**Pattern**: Hebrew מִן doesn't automatically mean Comparative
- Context determines whether C, S, or 'too'

---

## Algorithm v2.0 Performance on Batch 2

**Rough estimate** (need full analysis):
- Expected failures on:
  - MAT 10:31 (i value unknown to v2.0)
  - GEN 4:13 ('too' value unknown)
  - Various literal value variations
  - Mixed degree contexts (MAT 18:4)

**Estimated accuracy**: 60-70% (many new patterns v2.0 doesn't handle)

---

## Priority Fixes for v2.1

### Fix 1: Add "i" (Intensified Comparative) to value inventory
- Pattern: πολλῷ, πολλῶν with comparative → "Intensified Comparative"
- Example: πολλῶν στρουθίων διαφέρετε "more valuable than many sparrows"

### Fix 2: Add 'too' (T) to value inventory
- Pattern: Hebrew מִן with excessive meaning
- Example: גָּדוֹל מִן "too great to..."

### Fix 3: Handle literal value encoding variations
- Sometimes triple quotes: '''least'''
- Sometimes single quotes: 'least', 'too'
- Need flexible parsing

### Fix 4: Context-dependent degree assignment
- Same word can have different degrees in same verse (MAT 18:4)
- Need discourse-level analysis

---

## Progress Summary

**Total verses tested**: 41
**Values discovered**:
- ✅ "No Degree", "Comparative", "Superlative", "Intensified"
- ✅ "Intensified Comparative" (NEW!)
- ✅ '''least''', 'least', 'too' (literals)

**Still unknown**:
- E (Extremely Intensified)
- L (Less)

**Confirmed non-existent**:
- q (Equative)
- s (Superlative of 2)

---

**Status**: Major discoveries made, value inventory significantly expanded
**Next**: Update algorithm to handle i and T values, continue to 100 verses
**Goal**: Find E and L values, achieve 90%+ accuracy
