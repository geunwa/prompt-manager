# 최종 점검 체크리스트 (동료평가 요청용)

이 문서는 동료평가자가 코드를 열어보지 않고도 무엇이 구현되었는지 한눈에 확인할 수 있도록 정리한 체크리스트입니다. `README.md`는 프로그램 사용법 설명용이고, 이 문서는 **과제 요구사항 대비 구현 여부 점검용**입니다.

## 프로젝트 정보

| 항목 | 내용 |
|---|---|
| 프로젝트명 | AI 프롬프트 관리 프로그램 |
| 개발 언어 | Python (표준 라이브러리만 사용) |
| 실행 방식 | 터미널 기반 CLI 프로그램 (`python main.py`) |
| 저장 방식 | JSON 파일 영속화 (`prompts.json`) |
| 보너스 범위 | 보너스 1 (JSON 영속화 + 카테고리별 Markdown 내보내기)만 구현 |
| GitHub 저장소 | https://github.com/geunwa/prompt-manager |

---

## 1. 개발 환경 체크리스트

| 항목 | 확인 방법 | 상태 |
|---|---|---|
| Python 3.10 이상 설치 | `python --version` | [x] Python 3.14.7 확인 |
| VS Code + Python 확장 설치 | VS Code 확장 탭 확인 | [x] |
| Git 설치 | `git --version` | [x] Git 2.55.0 확인 |
| Git 사용자 정보 설정 | `git config user.name` / `git config user.email` | [x] |
| 기본 브랜치 이름 main 설정 | `git branch --show-current` | [x] |
| VS Code ↔ GitHub 계정 연동 | VS Code 로그인 상태 확인 | [x] |

![개발 환경 확인](./screenshot/01_env_check.png)

---

## 2. 제약 사항 체크리스트

| 항목 | 기준 | 상태 |
|---|---|---|
| Python 버전 | 3.10 이상 | [x] Python 3.14.7 |
| 외부 라이브러리 사용 여부 | 표준 라이브러리(`json`, `os`, `datetime`)만 사용, pip 설치 라이브러리 없음 | [x] |
| 함수 분리 | 모든 기능이 함수 단위로 분리됨 (하나의 함수에 로직 몰아넣지 않음) | [x] |
| 커밋 개수 | 최소 10개 이상 (기능 단위) | [x] 총 23개 커밋 확인 |
| 브랜치 생성 및 병합 | `checkout`/`merge`로 로컬에서 수행 | [x] `feature/update` → `main` 병합 이력 확인 |
| Git 명령어 각 1회 이상 사용 | `init, add, commit, push, pull, checkout, clone, merge` | [x] 전체 사용 완료 (아래 섹션 참고) |
| 기본 프롬프트 3개 이상 | 이전 미션 프롬프트 재사용 | [x] `prompts.json`에 3개 등록 완료 (텍스트 생성/자동화/이미지 생성) |

---

## 3. 필수 기능 요구사항 체크리스트

### 메뉴/실행
- [x] 프로그램 실행 시 메뉴 출력
- [x] 번호 입력으로 기능 선택
- [x] 잘못된 번호 입력 시 안내 메시지 후 메뉴 재출력
- [x] 종료 기능 (0번)
- [x] 각 기능 수행 후 메뉴로 복귀

![프로그램 메뉴](./screenshot/02_program_menu.png)

---

### 기본 프롬프트 데이터
- [x] 리스트 + 딕셔너리 구조로 저장
- [x] 제목, 내용, 카테고리, 즐겨찾기 여부 포함 (+ 태그, 생성일 추가 구현)
- [x] 이전 미션 프롬프트 3개 이상 기본 등록 (`prompts.json` 및 파일이 없을 때를 대비한 코드 내 기본값 이중 구현)

---

### 프롬프트 추가
- [x] 제목/내용/카테고리 입력
- [x] 빈 값 입력 시 재입력 요청
- [x] 카테고리를 미리 정의된 목록(텍스트 생성/이미지 생성/영상 생성/페르소나/자동화/기타)에서 선택하거나 직접 입력
- [x] 즐겨찾기 기본값 False

![프롬프트 추가](./screenshot/03_add_prompt.png)

---

### 프롬프트 목록
- [x] 번호, 제목, 카테고리, 즐겨찾기(⭐) 표시
- [x] 목록이 없을 때 안내 메시지

![전체 프롬프트 목록](./screenshot/04_view_all_prompts.png)

---

### 카테고리별 조회
- [x] 카테고리 목록 표시 후 선택 시 해당 카테고리만 출력
- [x] 프롬프트 없을 때 안내 메시지

![카테고리 목록](./screenshot/05_category_list.png)
![카테고리별 조회](./screenshot/06_view_by_category.png)

---

### 프롬프트 검색
- [x] 키워드로 제목/내용 검색 (카테고리·태그까지 확장 구현)
- [x] 결과 없을 때 안내 메시지

![프롬프트 검색](./screenshot/07_search_prompt.png)

---

### 프롬프트 상세 보기
- [x] 제목/카테고리/즐겨찾기/내용 전체 출력
- [x] 잘못된 번호 입력 시 안내 메시지

![프롬프트 상세 보기](./screenshot/08_prompt_detail.png)

---

### 즐겨찾기 관리
- [x] 번호로 즐겨찾기 추가/해제
- [x] 즐겨찾기만 모아보기

![즐겨찾기](./screenshot/09_favorite.png)

---

### 코드 구조
- [x] 기능별 함수 분리 (`add_prompt`, `list_prompts`, `search_prompts`, `view_prompt_detail`, `toggle_favorite`, `list_favorites` 등)

---

### README.md
- [x] 프로그램 이름/설명
- [x] 실행 방법
- [x] 기능 목록
- [x] 등록된 카테고리 설명

---

## 4. 보너스 1 체크리스트 (구현 범위)

- [x] 프롬프트 데이터를 JSON 파일(`prompts.json`)로 저장/불러오기
- [x] 프로그램 종료 후 재실행해도 데이터 유지
- [x] 전체 프롬프트를 카테고리별 Markdown 파일로 내보내기 (`markdown_exports/` 폴더 자동 생성)
- [x] 파일명에 쓸 수 없는 문자 정리(`sanitize_filename`)

![Markdown 내보내기](./screenshot/10_markdown_export.png)
![내보내기 폴더 확인](./screenshot/11_markdown_exports_folder.png)

> 보너스 2(수정/삭제, 조회수 기록, Top 정렬)는 이번 제출 범위에 포함하지 않습니다. (단, 삭제 기능은 필수 요구사항에는 없지만 편의상 추가 구현되어 있습니다.)

---

## 5. GitHub / Git 이력 체크리스트

- [x] GitHub 원격 저장소 연결 (https://github.com/geunwa/prompt-manager)
- [x] 최소 10개 이상 커밋 — 총 **23개** 커밋 확인
- [x] 브랜치 생성 및 병합(merge commit) 이력 존재 (`feature/update` → `main`)
- [x] `git pull` 실행 완료 — `Already up to date` 확인
- [x] `git clone` 실행 완료 — `Hello-World` 저장소 clone 확인
- [x] 최종본 커밋 & push 완료

### git log 확인

![git log --oneline --graph](./screenshot/13_git_log.png)

### git pull 확인

![git pull origin main](./screenshot/12_git_pull.png)

### git clone 확인

![git clone 실행](./screenshot/14_git_clone.png)

---

## 6. 제출 전 마지막 확인 (실행 순서)

1. 수정된 `main.py`, `prompts.json`, `README.md`, `final_checklist.md`를 프로젝트 폴더에 덮어씁니다.
2. 터미널에서 `prompts.json`을 삭제한 뒤 `python main.py`를 실행해, 기본 프롬프트 3개가 자동으로 다시 생성되는지 확인합니다.
3. 메뉴 1~10번을 순서대로 한 번씩 실행해 보고 에러 없이 동작하는지 확인합니다.
4. `git add`, `git commit`, `git push`로 최종본을 GitHub에 반영합니다.
5. GitHub 저장소 페이지에서 파일 목록과 커밋 이력이 정상적으로 보이는지 웹에서 최종 확인합니다.

---

## 모든 항목 완료! ✅

| 구분 | 상태 |
|---|---|
| 개발 환경 | ✅ 완료 |
| 제약 사항 | ✅ 완료 |
| 필수 기능 9개 | ✅ 완료 |
| 보너스 1 | ✅ 완료 |
| Git 이력 (23커밋, 브랜치, pull, clone) | ✅ 완료 |
| GitHub push | ✅ 완료 |

---

## 한 줄 요약 (동료평가자용)

이전 미션에서 만든 프롬프트 3개를 기본 데이터로 등록하고, 추가/조회/검색/상세보기/즐겨찾기/삭제 기능을 갖춘 터미널 기반 프롬프트 관리 프로그램입니다. JSON 파일로 데이터를 영속화하고, 카테고리별 Markdown 내보내기(보너스 1)까지 구현했습니다.