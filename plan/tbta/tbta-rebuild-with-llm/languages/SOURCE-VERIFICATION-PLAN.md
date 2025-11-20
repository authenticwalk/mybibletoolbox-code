# Source Verification Plan

## Objective

Verify or remove all ~149 claims marked [NEEDS SOURCE] across language family documentation.

## Process

For each [NEEDS SOURCE] claim:
1. **Search for authoritative source** using WebSearch
2. **Verify claim accuracy** - ensure source actually supports the claim
3. **Add inline citation** if source found and authoritative
4. **Remove claim entirely** if no authoritative source can be found

## Authoritative Sources

✓ **Acceptable**:
- Academic publishers (Oxford, Cambridge, MIT Press, Routledge)
- Peer-reviewed journals (Language, Linguistic Typology, etc.)
- SIL International, Ethnologue
- WALS (World Atlas of Language Structures)
- University dissertations and theses
- Academic encyclopedias (Oxford Research Encyclopedia, etc.)

✗ **Not Acceptable**:
- Wikipedia (can use to find primary sources)
- Personal blogs
- Unverified websites
- ChatGPT/LLM outputs without citation

## Parallel Execution

Launch 6 agents in parallel to process all families:
1. Agent 1: Austronesian (37 claims)
2. Agent 2: Indo-European (10 claims)
3. Agent 3: Niger-Congo (34 claims)
4. Agent 4: Trans-New Guinea (31 claims)
5. Agent 5: Other-Families (6 issues)
6. Agent 6: Mayan + Otomanguean (11 + ~30 claims)

## Expected Outcome

All files will have either:
- Properly cited claims with inline sources, OR
- Claims removed as unverifiable

## Progress Tracking

- **Started**: 2025-11-07
- **Completed**: 2025-11-07
- **Claims to verify**: ~149
- **Claims verified**: ~145
- **Claims removed**: <5
- **Sources added**: 50+ authoritative citations

## Results Summary

All language family files successfully verified:
- Austronesian: 37 claims (34 verified, 3 explained, 0 removed)
- Indo-European: 10 claims (9 verified, 1 removed)
- Niger-Congo: 34+ claims (all verified with 5 new sources)
- Trans-New Guinea: 31+ claims (23 verified, 6 modified, 2 major errors corrected)
- Other-Families: 6 issues (all resolved)
- Mayan: 11 categories (all verified, 1 citation error fixed)
- Otomanguean: ~30 claims (all verified)

## Commits

- Trans-New Guinea: 1351ab4
- All others: 130ddae
- Branch: claude/llm-folder-rebuild-011CUsZGwdAqioh1tPZ1XYzs
