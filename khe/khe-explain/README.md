# khe-explain

코드나 개념을 비유를 들어 쉬운 한국어로 설명해주는 하네스.

## 로컬 테스트 (설치 없이)

레포 루트에서:
```
claude --plugin-dir ./khe/khe-explain
```

## 마켓에서 설치

```
/plugin marketplace add Cohort-based-Learning/cohort14
/plugin install khe-explain@cohort14
/reload-plugins
```

## 사용법

켜진 뒤 그냥 자연어로 물어보면 됩니다:

```
재귀함수가 뭐야? 쉽게 설명해줘
이 코드 비유로 알려줘
async/await 이거 무슨 뜻이야
```

## 답변 형식

이렇게 정리해서 답합니다:

```
## 한 줄 요약
- 초등학생도 알 만한 한 문장

## 비유
- 일상 사물에 빗댄 설명

## 핵심 3가지
1. ...
2. ...
3. ...
```

전문 용어는 옆에 괄호로 쉬운 말을 붙입니다. 예: 캐시(자주 쓰는 걸 가까이 보관해두는 것)
