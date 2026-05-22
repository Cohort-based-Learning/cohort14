# Code Review Plugin

학생 팀 프로젝트 코드 리뷰용 Claude Code 플러그인. 설치하면 어느 폴더에서든 작동합니다.

## 설치

```shell
/plugin marketplace add <당신>/code-review-marketplace
/plugin install code-review@code-review-tools
/reload-plugins
```

## 사용

자기 코드 폴더에서 claude를 켜고 말하면, Claude가 알맞은 스킬/에이전트를 자동으로 불러옵니다:

| 말하면 | 동작 |
|---|---|
| `내 코드 리뷰해줘` | 4섹션 리뷰 (질문 유도, 수정코드 X) |
| `커밋 전에 리뷰해줘` | 리뷰 + 이해도 3문제 채점 → 통과 시 커밋 |
| `보안 검토해줘` | 보안 전문 리뷰 |
| `이 리뷰 검수해줘` | 리뷰 품질 검수 |

명시적으로 부르고 싶으면 슬래시도 됩니다: `/code-review:code-review`, `/code-review:pre-commit-review`

설치 시 hook 승인을 한 번 하면, 이후 자동으로 응답은 한국어로, 리뷰 형식은 강제됩니다.
