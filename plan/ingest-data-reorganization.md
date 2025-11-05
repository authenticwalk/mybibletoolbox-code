# Ingest-Data Reorganization Plan

Date: 2025-11-05

## Problem

The data ingestion code is split across two locations creating confusion:

1. **Macula split across two directories:**
   - `src/ingest-data/macula/macula_fetcher.py` - Downloads raw XML
   - `src/lib/macula/macula_processor.py` - Processes XML to YAML ❌ Wrong location

2. **TBTA only in lib:**
   - `src/lib/tbta/tbta_processor.py` - Processes TBTA JSON ❌ Should be in ingest-data

3. **Source-languages confusing:**
   - Name implies it's a separate data source, but it's really just a convenience wrapper
   - Actually combines: Macula data + Strong's dictionary lookups
   - "Two steps" is confusing (fetch vs process vs combine)

---

## Proposed Structure

### Option A: Consolidate Everything Under ingest-data (RECOMMENDED)

```
src/ingest-data/
├── __init__.py
├── README.md
│
├── ebible/
│   ├── __init__.py
│   └── ebible_fetcher.py          # ✅ Already correct
│
├── strongs/
│   ├── __init__.py
│   └── strongs_fetcher.py          # ✅ Already correct
│
├── macula/
│   ├── __init__.py
│   ├── macula_fetcher.py           # ✅ Already here (downloads raw data)
│   ├── macula_processor.py         # MOVE from src/lib/macula/
│   ├── README.md                   # MOVE from src/lib/macula/
│   ├── MACULA-FIELD-DEFINITIONS.md # MOVE from src/lib/macula/
│   └── XML_NESTING_ANALYSIS.md     # MOVE from src/lib/macula/
│
└── tbta/
    ├── __init__.py
    ├── tbta_processor.py            # MOVE from src/lib/tbta/
    └── README.md                    # MOVE from src/lib/tbta/
```

**Remove:**
- `src/ingest-data/source-languages/` - This functionality moves to macula
- `src/lib/macula/` - Delete entire directory after moving
- `src/lib/tbta/` - Delete entire directory after moving

### What Happens to source-languages?

The source-languages fetcher is really just:
1. Load macula data for a verse
2. Extract Strong's numbers from it
3. Load Strong's dictionary entries
4. Merge them together

**This should become a function in macula_processor.py**, not a separate module:

```python
# In macula_processor.py
def fetch_with_strongs_data(verse_ref: str) -> Dict[str, Any]:
    """
    Fetch Macula data for a verse with Strong's dictionary entries merged in.
    
    This combines:
    1. Macula source word data
    2. Strong's dictionary definitions
    3. Cross-references between them
    """
    # ... (current source_languages_fetcher logic)
```

---

## Changes Required

### 1. Move Files

```bash
# Move macula processor and docs
mv src/lib/macula/macula_processor.py src/ingest-data/macula/
mv src/lib/macula/*.md src/ingest-data/macula/

# Move tbta processor and docs  
mv src/lib/tbta/tbta_processor.py src/ingest-data/tbta/
mv src/lib/tbta/README.md src/ingest-data/tbta/
mkdir -p src/ingest-data/tbta/

# Remove old directories
rmdir src/lib/macula
rmdir src/lib/tbta
```

### 2. Update Imports

**File: `src/ingest-data/macula/macula_processor.py`**
- No changes needed (doesn't import from lib)

**File: macula_processor.py** (add source-languages functionality)
- Add `fetch_with_strongs_data()` function from source_languages_fetcher.py
- Move Strong's extraction and merging logic

### 3. Fix References

**Files that reference lib.macula or lib.tbta:**
- `plan/code-cleanup/CLEANUP-ANALYSIS.md` - Update documentation
- `plan/strongs-enhancement-research.md` - Update paths
- `plan/morphhb-vs-macula.md` - Update paths
- READMEs - Update command examples

### 4. Update src/lib Structure

After moves, `src/lib/` should contain only TRUE library code:
- `get_strongs.py` - Utility for Strong's lookups
- `scripture_study.py` - Bible study utilities
- Any other shared utility modules

---

## Rationale

### Why Move Processors to ingest-data?

1. **They ARE data ingestion**: They fetch external data and write to DATA_DIR
2. **Semantic clarity**: "lib" should be utilities, not data pipelines
3. **Consistency**: Keep fetch + process together for each source
4. **Single responsibility**: One directory per data source

### Why Remove source-languages?

1. **Not a separate data source**: It doesn't fetch new data, just combines existing
2. **Confusing name**: Implies it's distinct from macula
3. **Unnecessary abstraction**: The combining logic is simple enough to be a function
4. **Reduces complexity**: One less directory to understand

### Why This Is Better

**Before:**
```
User: "Where does macula data come from?"
Answer: "Well, macula_fetcher downloads it, but you also need 
         macula_processor from a different directory, and if you 
         want Strong's data with it use source_languages_fetcher"
```

**After:**
```
User: "Where does macula data come from?"  
Answer: "src/ingest-data/macula/ - everything you need is there"
```

---

## Migration Checklist

### Phase 1: Setup
- [ ] Create `src/ingest-data/tbta/` directory
- [ ] Create `__init__.py` files

### Phase 2: Move Files (use git mv to preserve history)
- [ ] `git mv src/lib/macula/macula_processor.py src/ingest-data/macula/`
- [ ] `git mv src/lib/macula/*.md src/ingest-data/macula/`
- [ ] `git mv src/lib/tbta/* src/ingest-data/tbta/`

### Phase 3: Merge source-languages Into Macula
- [ ] Copy `fetch_source_languages()` logic into macula_processor.py
- [ ] Rename to `fetch_with_strongs_data()` 
- [ ] Add Strong's merging as optional feature in macula_processor
- [ ] Update macula_processor CLI to support `--with-strongs` flag
- [ ] Delete `src/ingest-data/source-languages/` directory

### Phase 4: Update References
- [ ] Update README examples in macula/README.md
- [ ] Update README examples in tbta/README.md  
- [ ] Update plan/*.md files with new paths
- [ ] Update ingest-data/README.md

### Phase 5: Cleanup
- [ ] Remove `src/lib/macula/` directory
- [ ] Remove `src/lib/tbta/` directory
- [ ] Verify no broken imports: `grep -r "lib.macula\|lib.tbta"`

### Phase 6: Test
- [ ] Run macula_processor with test verse
- [ ] Run tbta_processor with test verse
- [ ] Verify output files are correct
- [ ] Run any existing tests

---

## Implementation Commands

```bash
#!/bin/bash
# reorganize-ingest-data.sh

set -e  # Exit on error

echo "=== Phase 1: Setup ==="
mkdir -p src/ingest-data/tbta

echo "=== Phase 2: Move Files (preserving git history) ==="
git mv src/lib/macula/macula_processor.py src/ingest-data/macula/
git mv src/lib/macula/README.md src/ingest-data/macula/
git mv src/lib/macula/MACULA-FIELD-DEFINITIONS.md src/ingest-data/macula/
git mv src/lib/macula/XML_NESTING_ANALYSIS.md src/ingest-data/macula/
git mv src/lib/tbta/tbta_processor.py src/ingest-data/tbta/
git mv src/lib/tbta/README.md src/ingest-data/tbta/

echo "=== Phase 3: Will require manual code changes ==="
echo "TODO: Merge source_languages_fetcher.py into macula_processor.py"
echo "TODO: Add fetch_with_strongs_data() function"

echo "=== Phase 4: Update Documentation ==="
# Update command paths in READMEs
find src/ingest-data -name "README.md" -exec sed -i '' 's|src/lib/macula/|src/ingest-data/macula/|g' {} \;
find src/ingest-data -name "README.md" -exec sed -i '' 's|src/lib/tbta/|src/ingest-data/tbta/|g' {} \;

echo "=== Phase 5: Cleanup ==="
git rm -r src/lib/macula
git rm -r src/lib/tbta

echo "=== Done! ==="
echo "Next steps:"
echo "1. Manually merge source-languages into macula_processor.py"
echo "2. Test the moved processors"
echo "3. Review and commit changes"
```

---

## Testing After Migration

```bash
# Test macula processor
cd /path/to/mybibletoolbox-code
python3 src/ingest-data/macula/macula_processor.py --verse "JHN 3:16"

# Test tbta processor
python3 src/ingest-data/tbta/tbta_processor.py --verse "GEN 1:1"

# Verify no broken imports
grep -r "from lib.macula" src/
grep -r "from lib.tbta" src/
# Should return no results

# Check that src/lib only has utilities
ls -la src/lib/
# Should only show: get_strongs.py, scripture_study.py, etc.
```

---

## Benefits

1. ✅ **Single Source of Truth**: Each data source has ONE directory
2. ✅ **Clear Organization**: ingest-data/ contains all ingestion pipelines
3. ✅ **Easier Discovery**: New users can find everything in one place
4. ✅ **Logical Grouping**: Fetcher + Processor together per source
5. ✅ **Reduced Confusion**: No more "two steps" or split functionality
6. ✅ **Better Semantics**: lib/ contains actual libraries, not data pipelines

---

## Notes

- Use `git mv` to preserve file history
- Test thoroughly after each phase
- Update documentation as you go
- Consider this an opportunity to clean up any outdated docs

