# code-review (예시 하네스)

학생 팀 프로젝트 코드 리뷰용 Claude Code 플러그인. **하네스를 어떻게 만드는지 보여주는 참고용 완성본**입니다.

## 구성

| 폴더 | 내용 |
|---|---|
| `skills/` | code-review, pre-commit-review, git-convention, feedback-tone |
| `agents/` | review-checker, security-reviewer |
| `hooks/hooks.json` | 응답 한국어 강제 + 리뷰 형식 검증 |
| `scripts/` | hook이 부르는 파이썬 스크립트 |

## 로컬 테스트

```bash
# 레포 루트에서
claude --plugin-dir ./examples/code-review
```

## 마켓에서 설치

```shell
/plugin marketplace add Cohort-based-Learning/cohort14
/plugin install code-review@cohort14
```

## 사용

| 말하면 | 동작 |
|---|---|
| `내 코드 리뷰해줘` | 4섹션 리뷰 (질문 유도, 수정코드 X) |
| `커밋 전에 리뷰해줘` | 리뷰 + 이해도 3문제 대화형 채점 |
| `보안 검토해줘` | 보안 전문 리뷰 |

> 자기 하네스를 만들 때 이 폴더 구조를 그대로 베껴 시작하세요. 전체 가이드는 [레포 README](../../README.md) 참고.
