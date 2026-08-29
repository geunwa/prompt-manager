```python
import json
import os

FILE_NAME = "prompts.json"

default_prompts = [
    {
        "title": "블로그 마케팅 코치 네비",
        "content": "당신은 초보 사장님을 위한 블로그 마케팅 코치입니다. 사용자의 업종, 타깃 고객, 목표를 묻고 블로그 글 주제 5개와 각 주제별 소제목을 제안하세요.",
        "category": "텍스트 생성",
        "favorite": False,
        "source": "기본 프롬프트"
    },
    {
        "title": "학습 도우미 튜터",
        "content": "당신은 친절한 학습 도우미입니다. 학생의 수준을 먼저 파악하고, 개념 설명 → 쉬운 예시 → 짧은 확인 문제 순서로 답변하세요.",
        "category": "학습",
        "favorite": True,
        "source": "기본 프롬프트"
    },
    {
        "title": "업무 자동화 아이디어 생성기",
        "content": "사용자가 하는 반복 업무를 입력하면 자동화할 수 있는 아이디어 3가지를 제안하고, 각 방법의 장단점을 정리하세요.",
        "category": "자동화",
        "favorite": False,
        "source": "기본 프롬프트"
    }
]


def load_prompts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise json.JSONDecodeError("Invalid format", "", 0)

            for prompt in data:
                if "title" not in prompt:
                    prompt["title"] = "제목 없음"
                if "content" not in prompt:
                    prompt["content"] = ""
                if "category" not in prompt or not str(prompt["category"]).strip():
                    prompt["category"] = "미분류"
                if "favorite" not in prompt:
                    prompt["favorite"] = False
                if "source" not in prompt:
                    prompt["source"] = ""

            return data

        except (json.JSONDecodeError, FileNotFoundError):
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(default_prompts, file, ensure_ascii=False, indent=4)
            return [prompt.copy() for prompt in default_prompts]

    else:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(default_prompts, file, ensure_ascii=False, indent=4)
        return [prompt.copy() for prompt in default_prompts]


def save_prompts_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 프롬프트 조회")
    print("3. 프롬프트 검색")
    print("4. 프롬프트 상세 보기")
    print("5. 즐겨찾기 토글")
    print("6. 프롬프트 삭제")
    print("7. 카테고리별 Markdown 파일로 내보내기")
    print("0. 종료")


def add_prompt():
    print("\n[프롬프트 추가]")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    category = input("카테고리: ").strip()
    source = input("출처(없으면 엔터): ").strip()

    if not title:
        print("제목은 비워둘 수 없습니다.")
        return

    if not content:
        print("내용은 비워둘 수 없습니다.")
        return

    if not category:
        category = "미분류"

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "source": source
    }

    prompts.append(new_prompt)
    save_prompts_to_file()
    print(f"\"{title}\" 프롬프트가 저장되었습니다.")


def show_all_prompts():
    print("\n[전체 프롬프트 조회]")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        favorite_mark = "★" if prompt.get("favorite", False) else " "
        print(f"{i}. [{favorite_mark}] {prompt['title']} / 카테고리: {prompt['category']}")


def search_prompts():
    print("\n[프롬프트 검색]")
    keyword = input("검색어를 입력하세요: ").strip().lower()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for i, prompt in enumerate(prompts, 1):
        if (
            keyword in prompt.get("title", "").lower()
            or keyword in prompt.get("content", "").lower()
            or keyword in prompt.get("category", "").lower()
        ):
            results.append((i, prompt))

    if not results:
        print("검색 결과가 없습니다.")
        return

    print(f"\"{keyword}\" 검색 결과:")
    for index, prompt in results:
        favorite_mark = "★" if prompt.get("favorite", False) else " "
        print(f"{index}. [{favorite_mark}] {prompt['title']} / 카테고리: {prompt['category']}")


def show_prompt_detail():
    print("\n[프롬프트 상세 보기]")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    show_all_prompts()

    try:
        number = int(input("상세히 볼 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            prompt = prompts[number - 1]
            print("\n----- 프롬프트 상세 정보 -----")
            print(f"제목: {prompt.get('title', '제목 없음')}")
            print(f"카테고리: {prompt.get('category', '미분류')}")
            print(f"즐겨찾기: {'Yes' if prompt.get('favorite', False) else 'No'}")
            print(f"출처: {prompt.get('source', '') if prompt.get('source', '') else '없음'}")
            print("내용:")
            print(prompt.get("content", ""))
            print("-----------------------------")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def toggle_favorite():
    print("\n[즐겨찾기 토글]")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    show_all_prompts()

    try:
        number = int(input("즐겨찾기를 변경할 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            prompts[number - 1]["favorite"] = not prompts[number - 1].get("favorite", False)
            save_prompts_to_file()

            if prompts[number - 1]["favorite"]:
                print("즐겨찾기에 추가되었습니다.")
            else:
                print("즐겨찾기에서 해제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def delete_prompt():
    print("\n[프롬프트 삭제]")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    show_all_prompts()

    try:
        number = int(input("삭제할 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            deleted = prompts.pop(number - 1)
            save_prompts_to_file()
            print(f"\"{deleted['title']}\" 프롬프트가 삭제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def sanitize_filename(name):
    invalid_chars = '\\/:*?"<>|'
    for char in invalid_chars:
        name = name.replace(char, "_")
    return name.strip() if name.strip() else "미분류"


def export_prompts_to_markdown():
    print("\n[카테고리별 Markdown 내보내기]")

    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    export_dir = "markdown_exports"
    os.makedirs(export_dir, exist_ok=True)

    categories = {}

    for prompt in prompts:
        category = str(prompt.get("category", "미분류")).strip()
        if not category:
            category = "미분류"

        if category not in categories:
            categories[category] = []

        categories[category].append(prompt)

    for category, prompt_list in categories.items():
        safe_name = sanitize_filename(category)
        file_path = os.path.join(export_dir, f"{safe_name}.md")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {category} 프롬프트 모음\n\n")
            file.write(f"- 총 개수: {len(prompt_list)}개\n\n")

            for i, prompt in enumerate(prompt_list, 1):
                title = prompt.get("title", "제목 없음")
                content = prompt.get("content", "")
                favorite = "Yes" if prompt.get("favorite", False) else "No"
                source = prompt.get("source", "")

                file.write(f"## {i}. {title}\n\n")
                file.write(f"- 카테고리: {category}\n")
                file.write(f"- 즐겨찾기: {favorite}\n")
                file.write(f"- 출처: {source if source else '없음'}\n\n")
                file.write("### 내용\n\n")
                file.write(f"{content}\n\n")
                file.write("---\n\n")

    print(f"Markdown 파일이 \"{export_dir}\" 폴더에 저장되었습니다.")


prompts = load_prompts()


def main():
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_all_prompts()
        elif choice == "3":
            search_prompts()
        elif choice == "4":
            show_prompt_detail()
        elif choice == "5":
            toggle_favorite()
        elif choice == "6":
            delete_prompt()
        elif choice == "7":
            export_prompts_to_markdown()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    main()
```

## 실행 방법

```bash
python main.py
```

## 보너스 과제 확인 방법

1. 프로그램 실행
2. 메뉴에서 `7` 선택
3. 프로젝트 폴더 안에 `markdown_exports` 폴더가 생성되는지 확인
4. 카테고리별 `.md` 파일이 생성되는지 확인

예:
- `markdown_exports/텍스트 생성.md`
- `markdown_exports/학습.md`
- `markdown_exports/자동화.md`

## 추천 커밋 메시지

```bash
git add .
git commit -m "feat: 카테고리별 markdown 내보내기 기능 추가"
git push
```
