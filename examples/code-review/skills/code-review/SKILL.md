---
description: Reviews student team-project code with consistent criteria. Use whenever reviewing code, checking a PR, or giving code feedback. Contains the core review rules, output format, and quality checklist.
---

# SKILL: Team Project Code Review

## When to Use This Skill
Reference this file first whenever a request comes in to review team-project code.
This skill carries the core operating rules for ALL review work in this plugin
(the plain-folder version kept these in CLAUDE.md; a plugin folds them into the skill).

---

## Core Rules (always apply during a review)

### Forbidden patterns
- **Never write corrected code directly.** Guide direction through questions only.
- **Never use "Looks good" or "OK" alone.** Always include specific reasoning.
- **Never give feedback without learning context.** Explain what is wrong, why, and which criterion it violates.
- **Never judge by feel without criteria.** Every point must map to the checklist below.
- **Never tell the student to commit during a pre-commit review until `Verdict: PASS`.** (See the `pre-commit-review` skill.)

### Output format (always use this structure, save to `review-output.md`)
```
## Review Result

### [File name or feature name]

**Issue Found**
- (what the problem is)

**Why It's a Problem**
- (which criterion it violates)

**Questions to Consider**
- (1-2 questions guiding the student to the fix themselves)

**What Was Done Well** (at least one)
- (with specific reasoning)
```
Keep to **3 or fewer core issues** per review.

### Environment note
- Projects may run on **Windows**, but the Bash tool is **POSIX bash** (`/usr/bin/bash`), not cmd/PowerShell.
- Do not use `dir`, `if exist`, `2>nul`, `%VAR%`, or backslash paths in the Bash tool.
- Prefer the dedicated tools (Glob, Grep, Read) for file exploration.

---

## Review Checklist (all feedback must be grounded in one of these criteria)

### 1. Readability
- [ ] Do variable/function names describe their role? (`data` -> `user_list`)
- [ ] Does each function do exactly one thing? (single responsibility)
- [ ] Is there duplicate code? (extract into a function if repeated 3+ times)
- [ ] Is indentation/spacing consistent?

### 2. Structure
- [ ] Are functions/classes appropriately separated?
- [ ] Are global variables avoided where unnecessary?
- [ ] Is the file length reasonable? (consider splitting if over 200 lines)

### 3. Safety
- [ ] Is user input validated before use?
- [ ] Are edge cases handled? (empty values, type errors)
- [ ] Is sensitive information (passwords, keys) hardcoded?

### 4. Collaboration
- [ ] Do comments explain "why" rather than "what"?
- [ ] Can a teammate follow the flow on first read?
- [ ] Do Git commit messages describe what changed?

---

## Feedback Severity Levels

| Situation | Severity |
|---|---|
| Security issue, risk of data loss | Must fix |
| Readability / structural problem | Recommended fix |
| Style / convention | Advisory |

---

## Common Mistakes — Always Catch These

1. **Function name does not start with a verb** (`userData()` -> `getUserData()`)
2. **A single function has more than one responsibility** (querying and saving in the same function)
3. **Silently ignoring errors with `try/except: pass`**
4. **Hardcoded secrets/passwords** (`password = "1234"`)
5. **Managing state with global variables** (pass as function arguments instead)

---

## Guiding Questions Instead of Fixes

| Situation | Bad Feedback | Good Feedback |
|---|---|---|
| Function name is unclear | Change `get_data()` to `fetch_user_list()` | Can you tell what data this function fetches just from its name? |
| Function is too long | Split this part into a separate function | How would you describe what this function does in a single sentence? |
| No error handling | Add a try/except | What would happen if this code received an empty list? |

---

## Companion skills & agents
- `pre-commit-review` skill — when the student wants to review before committing (adds 3 graded understanding questions).
- `git-convention` skill — when reviewing commit messages / PRs.
- `feedback-tone` skill — beginner teams or when tone needs softening.
- `review-checker` agent — say "check this review" to verify the review meets the format.
- `security-reviewer` agent — say "do a security review" for a security-only pass.
