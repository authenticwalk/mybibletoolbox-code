# Peer Review Failure Analysis: Why Data Leakage Wasn't Caught

**Date**: 2025-11-17
**Issue**: Peer review failed to catch data leakage violation
**Root Cause**: Vague checklist items that didn't verify train/test separation
**Status**: ✅ FIXED (checklist made explicit)

---

## 🚨 The Failure

### What Should Have Happened

**Methodological Peer Review** (Stage 6, Subagent 5) should have asked:

1. ❓ "Where are the locked prediction files?"
2. ❓ "Show me the git commit with predictions BEFORE scoring"
3. ❓ "Can you prove predictions were made without seeing answers?"

**If these don't exist** → 🚨 **DATA LEAKAGE DETECTED**

### What Actually Happened

The peer review checklist said:

```markdown
#### Locked Predictions
- ✅ PROMPT1.md committed before validation
- ✅ Pattern-based approach (not verse memorization)  
- ✅ Git history preserved
```

**All checked ✅ but WRONG THINGS!**

---

## 🔍 Root Cause Analysis

### Problem 1: Checking Algorithm Instead of Predictions

**What was checked**:
- ✅ "PROMPT1.md committed" ← This is the ALGORITHM

**What SHOULD be checked**:
- ❌ "test_predictions_LOCKED.yaml committed BEFORE test.yaml opened"

**Why this matters**: Committing the algorithm doesn't prove predictions were made blindly!

---

### Problem 2: Vague Checklist in STAGES.md

**Original checklist** (STAGES.md line 839):
```markdown
- Check locked predictions discipline (git commits present?)
```

**Problems with this**:
- ✗ "Git commits present" - commits of WHAT?
- ✗ "Present" - present WHEN? Before or after seeing answers?
- ✗ No mention of prediction FILES
- ✗ No verification procedure

**Result**: Easy to check the wrong thing and claim ✅

---

### Problem 3: No Verification Procedure

The checklist didn't say HOW to verify locked predictions:

**Missing procedures**:
- Look for prediction files (test_predictions_LOCKED.yaml)
- Check git log for commit order (predictions → scoring)
- Verify no mention of test.yaml before predictions locked

**Result**: Reviewer didn't know what to look for, so looked at wrong things

---

### Problem 4: Assumed Good Faith

The methodological review said "⚠️ PASS with caveats" and noted limitations, but assumed:
- ✅ "Pattern-based approach (not verse memorization)" 
- ✅ "Git history preserved"

**Critical mistake**: Assumed train/test separation was followed without VERIFYING it

**Why this failed**: The checklist was checking for OVERFITTING (verse memorization) but not DATA LEAKAGE (seeing test answers)

---

## 🔧 The Fix: Explicit Checklist

### New STAGES.md Methodological Review (Lines 835-865)

**CRITICAL CHECKS** added (catches data leakage):

```markdown
- [ ] **Train/Test Separation Verified?**
  - Are there PREDICTION files for test set? (e.g., test_predictions_LOCKED.yaml)
  - Is there a git commit with predictions BEFORE any mention of test.yaml results?
  - Can you prove predictions were made blindly (without seeing test answers)?
  - ⚠️ RED FLAG: If you see accuracy numbers without locked prediction files = DATA LEAKAGE

- [ ] **Locked Predictions Discipline?**
  - For test set: test_predictions_LOCKED.yaml committed BEFORE test.yaml opened?
  - For validate set: validate_predictions_LOCKED.yaml committed BEFORE validate.yaml opened?
  - Git log shows: commit predictions → commit scoring (in that order)?
  - ⚠️ RED FLAG: If scoring happens without locked prediction files = CHEATING
```

**HOW TO VERIFY** added:
```bash
# Check git history for locked predictions
git log --all --oneline --grep="lock.*predictions"

# Look for prediction files
ls experiments/*_predictions_LOCKED.yaml

# If these don't exist but accuracy is reported → DATA LEAKAGE!
```

---

## 📊 How This Would Have Caught The Error

### Applying New Checklist to number-systems-cursor

**Question 1**: Are there PREDICTION files for test set?
```bash
$ ls experiments/*predictions*.yaml
# No such file
```
❌ **FAIL** - No prediction files exist

**Question 2**: Is there a git commit with predictions?
```bash
$ git log --oneline --grep="lock.*predictions"
# No results
```
❌ **FAIL** - No locked prediction commits

**Question 3**: Is accuracy reported without prediction files?
- Document claims: "100% accuracy (12/12 correct)"
- No prediction files exist
- 🚨 **RED FLAG: DATA LEAKAGE DETECTED!**

**Conclusion**: ❌ **PEER REVIEW FAILS** - Train/test separation violated

---

## 🎓 Key Lessons

### 1. Checklists Must Be Specific

**Bad checklist item**:
- "Check locked predictions discipline (git commits present?)"

**Good checklist item**:
- "Are there prediction files (test_predictions_LOCKED.yaml) committed BEFORE test.yaml results mentioned?"
- Include RED FLAGS: "If accuracy reported without prediction files = DATA LEAKAGE"
- Include verification procedure: "Run: ls experiments/*predictions*.yaml"

### 2. Don't Assume, Verify

**What I did wrong**:
- Assumed train/test separation was followed
- Checked for related but different things (overfitting, not data leakage)
- Gave ✅ without actually verifying

**What should happen**:
- Explicitly verify train/test separation
- Look for specific evidence (prediction files, git commits)
- If evidence doesn't exist → FAIL the review

### 3. Peer Review Catches Methodology Errors

The user said: "That should be part of the peer review and should have been caught there"

**Why this is critical**:
- Peer review is the LAST LINE OF DEFENSE
- If peer review misses methodology errors, they make it to production
- False confidence in invalid results is worse than no results

**The fix**:
- Make checklists explicit and verifiable
- Include RED FLAGS for common mistakes
- Add verification procedures (bash commands)

---

## 🔄 Process Improvement

### Before (Vague Checklist)

```markdown
Methodological Review:
- [ ] Check locked predictions discipline (git commits present?)
- [ ] Verify balanced sampling
```

**Problem**: "Git commits present" is vague, easy to check wrong thing

---

### After (Explicit Checklist)

```markdown
Methodological Review:

CRITICAL CHECKS (catch data leakage):
- [ ] Train/Test Separation Verified?
  - Prediction files exist? (test_predictions_LOCKED.yaml)
  - Git commit BEFORE scoring? 
  - Can prove blind predictions?
  - ⚠️ RED FLAG: Accuracy without predictions = DATA LEAKAGE

HOW TO VERIFY:
$ ls experiments/*predictions*.yaml
$ git log --grep="lock.*predictions"
```

**Benefit**: 
- Impossible to miss
- Explicit verification steps
- RED FLAGS highlight critical errors

---

## ✅ Corrective Actions

### 1. Updated STAGES.md ✅

- Lines 835-865 now have explicit train/test separation checks
- Added RED FLAGS for data leakage
- Added bash verification commands
- Made checklist items specific and actionable

### 2. Documented This Failure ✅

- Created this analysis document
- Explains why peer review failed
- Shows how new checklist would catch it
- Provides lessons for future reviews

### 3. Updated Feature Documentation ✅

- README.md notes validation correction needed
- PERFECTION-SUMMARY.md explains methodology error
- METHODOLOGY-ERROR-AND-FIX.md documents the data leakage issue

---

## 🎯 Impact on Future Features

### All 59 TBTA Features Benefit

**Every future methodological review** will now check:
1. ❓ Are prediction files locked before seeing answers?
2. ❓ Is git history showing predictions → scoring order?
3. ❓ Can train/test separation be proven?

**RED FLAGS** will catch:
- Accuracy claims without prediction files
- Scoring without locked predictions
- Any violation of train/test separation

### Impossible to Repeat This Error

**Old system**: Vague checklist, easy to check wrong things
**New system**: Explicit verification, specific files to check, bash commands to run

**Result**: Data leakage will be caught in peer review, not by user feedback

---

## 🙏 Thank You

**User feedback**: "That should be part of the peer review and should have been caught there, debug why it wasn't and fix that"

**Response**: Absolutely right! The peer review checklist was too vague. I've made it explicit with:
- Specific items to verify (prediction files)
- Red flags to watch for (accuracy without predictions)
- Verification procedures (bash commands)

**Impact**: This makes the methodology more rigorous for all 59 TBTA features.

---

**Date**: 2025-11-17  
**Status**: ✅ PEER REVIEW CHECKLIST FIXED  
**Lesson**: Checklists must be specific, verifiable, and include RED FLAGS for common errors

