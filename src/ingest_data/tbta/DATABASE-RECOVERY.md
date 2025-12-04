# Database Recovery Guide

## Current Status: ✅ HEALTHY

**Last checked:** 2025-12-04
**Database:** `Bible_unified.sqlite`
**Integrity:** OK
**Tables:** verses (30,629 rows), concepts (5,763 rows)

## Quick Diagnosis

If you see `SQLITE_CORRUPT` error:

```bash
cd databases
sqlite3 Bible_unified.sqlite "PRAGMA integrity_check;"
```

Expected output: `ok`

If you see anything else, the database is corrupted.

## Common Causes of "Corruption" Errors

### 1. Database Lock (Most Common)
**Error:** `database is locked` or `database disk image is malformed`
**Cause:** Another process is accessing the database
**Solution:**
```bash
# Find processes using the database
lsof databases/Bible_unified.sqlite

# Kill if needed (replace PID)
kill <PID>

# Or just wait a moment and retry
```

### 2. Incomplete Write Operation
**Cause:** Script interrupted during database update
**Solution:** The database has WAL mode enabled, so it should auto-recover. Just retry your query.

### 3. Concurrent Writes
**Cause:** Multiple scripts writing to database simultaneously
**Solution:** SQLite doesn't handle concurrent writes well. Ensure only one process writes at a time.

## Recovery Options

### Option 1: Rebuild from Source Databases (Recommended)

```bash
cd databases

# Backup corrupted database (just in case)
cp Bible_unified.sqlite Bible_unified.sqlite.corrupt

# Rebuild from scratch
python3 convert_bible_to_unified.py

# Repopulate TBTA data
cd ..
python3 src/ingest_data/tbta/extract_concepts.py \
    --database databases/Bible_unified.sqlite \
    --populate-senses-json
```

**Time:** ~5 minutes total
- convert_bible_to_unified.py: ~1 minute
- populate-senses-json: ~3 minutes

### Option 2: Export and Reimport

```bash
cd databases

# Export to SQL
sqlite3 Bible_unified.sqlite .dump > backup.sql

# Create new database
rm Bible_unified.sqlite
sqlite3 Bible_unified.sqlite < backup.sql

# Verify
sqlite3 Bible_unified.sqlite "PRAGMA integrity_check;"
```

### Option 3: Use SQLite Recovery Tool

```bash
# Install recovery tool
# brew install sqlite3  # macOS
# apt-get install sqlite3  # Linux

# Recover database
sqlite3 Bible_unified.sqlite.corrupt ".recover" | \
    sqlite3 Bible_unified_recovered.sqlite

# Verify recovered data
sqlite3 Bible_unified_recovered.sqlite "SELECT COUNT(*) FROM verses;"

# Replace if good
mv Bible_unified_recovered.sqlite Bible_unified.sqlite
```

## Verification Checklist

After recovery, verify all data:

```bash
cd databases

# 1. Check integrity
sqlite3 Bible_unified.sqlite "PRAGMA integrity_check;"
# Expected: ok

# 2. Check verse count
sqlite3 Bible_unified.sqlite "SELECT COUNT(*) FROM verses;"
# Expected: 30,629

# 3. Check concepts count
sqlite3 Bible_unified.sqlite "SELECT COUNT(*) FROM concepts;"
# Expected: 5,763

# 4. Check TBTA data
sqlite3 Bible_unified.sqlite "SELECT COUNT(*) FROM verses WHERE AnalyzedVerse IS NOT NULL;"
# Expected: 17,523

# 5. Check word_senses_json
sqlite3 Bible_unified.sqlite "SELECT COUNT(*) FROM verses WHERE word_senses_json IS NOT NULL;"
# Expected: 17,521

# 6. Test JSON query
sqlite3 Bible_unified.sqlite "SELECT json_extract(value, '\$.stem'), json_extract(value, '\$.concept_id') FROM verses, json_each(word_senses_json) WHERE USFM3='GEN' AND ChapterNum=1 AND VerseNum=1 LIMIT 3;"
# Expected: God|1334, make|604, create|253
```

## Database Schema

### verses table
```sql
CREATE TABLE verses (
    Book TEXT NOT NULL,
    USFM3 TEXT NOT NULL,
    ChapterNum INTEGER NOT NULL,
    VerseNum INTEGER NOT NULL,
    Verse TEXT,
    AnalyzedVerse TEXT,
    Notes TEXT,
    NIV TEXT,
    word_senses_json TEXT,  -- JSON array with full word data
    PRIMARY KEY (USFM3, ChapterNum, VerseNum)
);
```

### word_senses_json structure
```json
[
  {
    "stem": "God",
    "sense": null,
    "part_of_speech": "Noun",
    "semantic": "N-1A1SDAnK3NN........",
    "concept_id": 1334
  },
  ...
]
```

### concepts table
```sql
CREATE TABLE concepts (
    id INTEGER,
    stem TEXT,
    sense TEXT,
    part_of_speech TEXT,
    occurrences INTEGER,
    gloss TEXT,
    brief_gloss TEXT,
    note TEXT,
    categorization TEXT,
    curated_examples TEXT,
    level INTEGER
);
```

## Prevention Tips

### 1. Use WAL Mode (Already Enabled)
```bash
sqlite3 Bible_unified.sqlite "PRAGMA journal_mode=WAL;"
```

### 2. Backup Before Major Operations
```bash
# Before running extraction scripts
cp databases/Bible_unified.sqlite databases/Bible_unified.sqlite.backup
```

### 3. Avoid Concurrent Access
- Don't run multiple scripts accessing the database simultaneously
- Close database connections promptly in Python scripts

### 4. Use Transactions for Bulk Updates
Already implemented in `extract_concepts.py` - commits happen after all updates.

## Source Files

If you need to rebuild from scratch:

**Required:**
- `databases/Bible.sqlite` - Source TBTA data
- `databases/Bible - NIV.sqlite` - NIV translation
- `databases/Ontology-download.sqlite` - Concepts table

**Scripts:**
- `databases/convert_bible_to_unified.py` - Creates unified database
- `src/ingest_data/tbta/extract_concepts.py` - Populates word_senses_json

## Support

If you continue to see corruption errors:

1. Check disk space: `df -h`
2. Check file permissions: `ls -la databases/Bible_unified.sqlite`
3. Run disk utility: `fsck` (Linux) or Disk Utility (macOS)
4. Check for hardware issues

## Last Known Good State

**Date:** 2025-12-04 16:56:41
**Git commit:** 4414152
**Verses:** 30,629
**TBTA verses:** 17,521
**Word senses:** 539,063
**Concepts:** 5,763

