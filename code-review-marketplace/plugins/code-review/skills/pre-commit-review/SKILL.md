---
description: Pre-commit code review with an interactive understanding quiz. Use whenever a student wants to review, check, test, inspect, or look over their code BEFORE committing — including phrasings like "커밋 전에 리뷰/테스트/확인/점검/봐줘", "review/check/test before I commit", "커밋해도 될까?". This is a code REVIEW (not running the program), then a 3-question chat quiz confirming each answer right after.
---

# SKILL: Pre-Commit Review with Understanding Check

## When to use this skill
When a student wants to look over their code **before committing**, no matter the exact verb.
Trigger on any of: review, check, test, inspect, "봐줘", "리뷰", "테스트", "확인", "점검",
"커밋 전에 ~", "커밋해도 될까?".

> Note: "테스트해줘" here means **review the code before commit** — do a code review,
> do NOT just run/execute the program. (If the student clearly wants to run tests,
> ask whether they want a code review or to actually run the program.)

## Goal
Review the code, then run an **interactive quiz in chat**: ask 3 comprehension
questions one at a time, the student answers in chat, and you confirm the correct
answer immediately after each. The student answers in conversation —
**never by editing a file.**

---

## Procedure

### 1. Run the normal review
Use the `code-review` skill checklist and write the standard review into
`review-output.md`, with `<!-- mode: pre-commit -->` on the FIRST line.

### 2. Record the 3 questions in the file (behind the scenes, for the Stop hook)
Add an `## Understanding Check (before commit)` section with exactly 3 questions
(`**Q1.**`, `**Q2.**`, `**Q3.**`) and a `Verdict: AWAITING_ANSWERS` line.
This is a record only — **do NOT ask the student to type into the file.**

### 3. Run the quiz IN CHAT (the main interaction)
Go through the questions **one at a time**:
1. Ask the question in chat.
2. Wait for the student's answer in chat.
3. **Immediately** tell them whether they got it right, then give the correct
   answer and a one-line explanation.
4. Move on to the next question.

Each question tests **WHY an issue matters** (not how to fix it).
You may use the AskUserQuestion tool for multiple-choice if it suits the student's
level; otherwise just ask in plain chat.

### 4. Record results + set the verdict
After all 3, update `review-output.md`:
- Under `### Student Answers`, briefly record each answer and whether it was correct.
- Set `Verdict: PASS` if they understood all 3 (one minor gap is OK at your judgment),
  otherwise `Verdict: NEEDS_REVIEW` and note what to revisit.

### 5. Commit gate
- Tell the student "you're ready to commit" only when `Verdict: PASS`.
- If `Verdict: NEEDS_REVIEW`, do **not** run `git commit` and do **not** say it's ready.

---

## Question quality

| Bad (fix-guidance) | Good (comprehension check) |
|---|---|
| "이 쿼리를 어떻게 안전하게 고칠까요?" | "이 코드가 SQL Injection에 취약한 *이유*를 한 문장으로 설명해보세요." |
| "빈 리스트 검사를 추가하세요." | "조회 결과가 빈 리스트일 때 `users[0]`이 *왜* 문제가 되나요?" |
| "비밀번호를 환경변수로 옮기세요." | "비밀번호를 코드에 하드코딩하면 *어떤 위험*이 생기나요?" |

---

## review-output.md shape (pre-commit mode)
The file is a **record** for the Stop hook. The real Q&A happens in chat.
```
<!-- mode: pre-commit -->
## Review Result
... (normal review, up to 3 issues) ...

## Understanding Check (before commit)
**Q1.** ...
**Q2.** ...
**Q3.** ...

### Student Answers
(filled in by YOU after the chat quiz — student's answer + correct/incorrect)

Verdict: AWAITING_ANSWERS   <- becomes PASS or NEEDS_REVIEW after the quiz
```
