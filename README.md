# Cohort 14 플러그인 마켓

우리 반 전용 Claude Code 플러그인 마켓입니다. 각자 자기 하네스(플러그인)를 만들어 올리고, 서로 설치해 씁니다.

## 레포 구조

```
cohort14/
├─ .claude-plugin/marketplace.json   ← 마켓 목록 1개 (다 같이 공유, 루트에 고정)
├─ examples/code-review/             ← 예시 하네스 (참고용 완성본)
└─ <내이름>/<플러그인>/              ← 내가 만드는 곳
```

## 먼저 알아둘 것: 파일 두 종류

| 파일 | 위치 | 개수 | 내가 할 일 |
|---|---|---|---|
| `marketplace.json` | 레포 루트 `.claude-plugin/` | 1개 (공유) | 목록에 내 줄 한 줄 추가 |
| `plugin.json` | 내 플러그인 폴더 `.claude-plugin/` | 내 플러그인마다 1개 | 내가 만듦 |

루트 `marketplace.json`은 모두 같이 쓰는 목록이라 그대로 둡니다. 학생은 자기 폴더에 `plugin.json`을 만들고, 목록에 한 줄만 추가합니다.

---

## 내 하네스 만들기

### 1단계 — Fork 후 내 폴더 만들기

```
<내이름>/<플러그인>/
├─ .claude-plugin/
│  └─ plugin.json
└─ skills/
   └─ <스킬이름>/SKILL.md
```

`plugin.json` (필수):
```json
{
  "name": "my-plugin",
  "description": "한 줄 설명",
  "version": "1.0.0"
}
```

`skills/hello/SKILL.md`:
```markdown
---
description: 언제 이 스킬을 쓸지. Claude가 이 설명을 보고 자동으로 꺼냅니다.
---

Claude가 따라야 할 지침을 여기에 적습니다.
```

agents, hooks, scripts는 필요할 때만.

### 2단계 — 로컬 테스트 (설치 없이)

```
claude --plugin-dir ./<내이름>/<플러그인>
```

- 그 세션에서만 임시로 켜짐
- 켜진 뒤 `/help`로 내 스킬 확인, 또는 자연어로 시켜보기
- 경로는 `plugin.json`이 들어있는 폴더까지 정확히

### 3단계 — 마켓 목록에 등록

루트 `.claude-plugin/marketplace.json`의 `plugins` 배열에 내 줄 추가:

```json
{
  "name": "my-plugin",
  "source": "./<내이름>/<플러그인>",
  "description": "한 줄 설명"
}
```

### 4단계 — 검증

```
claude plugin validate .
```

### 5단계 — 올리기

```
git add .
git commit -m "add my-plugin"
git push
```

반 마켓에 합치려면 Pull Request를 보냅니다.

---

## 남의 플러그인 설치해서 쓰기

```
/plugin marketplace add Cohort-based-Learning/cohort14
/plugin install code-review@cohort14
/reload-plugins
```

설치하면 어느 폴더에서 claude를 켜든 그 플러그인이 따라옵니다.

설치 명령에서:
- `Cohort-based-Learning/cohort14` = GitHub 저장소
- `code-review@cohort14` = (플러그인 이름)@(마켓 이름)
