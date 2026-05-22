---
description: Reviews Git commit messages and PR writing practices. Use when checking commit messages, PR descriptions, or git history conventions in a team project.
---

# SKILL: Git Commit & PR Convention Review

## When to Use This Skill
When a request comes in to review Git commit messages or PR writing practices in a team project.

---

## Commit Message Checklist

### Format
- [ ] Does it follow the `type: description` structure? (e.g. `feat: 로그인 기능 추가`)
- [ ] Is the type one of: `feat / fix / docs / style / refactor / test / chore`?
- [ ] Is the description in imperative present tense? (`추가했음` ❌ → `추가` ✅)
- [ ] Is it 50 characters or fewer?

### Content
- [ ] Does it make clear what was done (what)?
- [ ] If needed, is the reason it was done (why) included in the body?
- [ ] Does it avoid vague words like "수정", "업데이트", "변경" alone?

## Bad Examples / Good Examples

| Bad Example | Good Example |
|---|---|
| `수정` | `fix: 로그인 시 비밀번호 공백 검증 누락 수정` |
| `기능 추가했음` | `feat: 회원가입 이메일 중복 체크 추가` |
| `asdfasdf` | — |

## Guiding Questions

- "If you only read this commit message 3 months from now, would you know what the work was?"
- "You only wrote '수정' — what if you included what was changed and why?"
