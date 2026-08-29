import json
import os

FILE_NAME = "prompts.json"


default_prompts = [
    {
        "title": "블로그 마케팅 코치 네비",
        "content": "당신은 초보 사업자를 위한 블로그 마케팅 코치입니다. 사용자의 업종, 타깃 고객, 목표를 묻고 블로그 글 주제 5개와 각 주제별 소개문을 제안하세요.",
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
        "title": "업무 자동화 아이디어 메이커",
        "content": "당신은 업무 자동화 컨설턴트입니다. 사용자가 하는 반복 업무를 입력하면 자동화 가능한 아이디어 3가지를 난이도와 함께 제안하세요.",
        "category": "자동화",
        "favorite": False,
        "source": "기본 프롬프트"
    }
]


def load_prompts():
    if not os.path.exists(FILE_NAME):
        save_prompts(default_prompts)
        return default_prompts.copy()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return default_prompts.copy()
    except (json.JSONDecodeError, FileNotFoundError):
        save_prompts(default_prompts)
        return default_prompts.copy()


def save_prompts(prompts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


def display_menu():
    print("\n===== AI 프롬프트 관리 프로그램 =====")
    print("1. 전체 프롬프트 조회")
    print("2. 프롬프트 추가")
    print("3. 프롬프트 검색")
    print("4. 프롬프트 상세 보기")
    print("5. 즐겨찾기 토글")
    print("6. 프롬프트 삭제")
    print("7. 카테고리별 Markdown 내보내기")
    print("0. 종료")


def view_all_prompts(prompts):
    if not prompts:
        print("\n저장된 프롬프트가 없습니다.")
        return

    print("\n===== 전체 프롬프트 목록 =====")
    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else " "
        print(f"{index}. [{favorite_mark}] {prompt['title']} / {prompt['category']}")


def add_prompt(prompts):
    print("\n===== 새 프롬프트 추가 =====")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    category = input("카테고리: ").strip()
    source = input("출처: ").strip()

    if not title or not content or not category:
        print("제목, 내용, 카테고리는 비워둘 수 없습니다.")
        return

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "source": source if source else "직접 작성"
    }

    prompts.append(new_prompt)
    save_prompts(prompts)
    print("프롬프트가 저장되었습니다.")


def search_prompts(prompts):
    keyword = input("\n검색어를 입력하세요: ").strip().lower()

    if not keyword:
        print("검색어를 입력해야 합니다.")
        return

    results = []
    for index, prompt in enumerate(prompts, start=1):
        title = prompt.get("title", "").lower()
        content = prompt.get("content", "").lower()
        category = prompt.get("category", "").lower()

        if keyword in title or keyword in content or keyword in category:
            results.append((index, prompt))

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n===== 검색 결과 =====")
    for index, prompt in results:
        favorite_mark = "★" if prompt.get("favorite", False) else " "
        print(f"{index}. [{favorite_mark}] {prompt['title']} / {prompt['category']}")


def view_prompt_detail(prompts):
    if not prompts:
        print("\n저장된 프롬프트가 없습니다.")
        return

    view_all_prompts(prompts)

    try:
        choice = int(input("\n상세 보기할 번호를 입력하세요: "))
        if choice < 1 or choice > len(prompts):
            print("올바른 번호를 입력하세요.")
            return
    except ValueError:
        print("숫자를 입력하세요.")
        return

    prompt = prompts[choice - 1]
    print("\n===== 프롬프트 상세 정보 =====")
    print(f"제목: {prompt.get('title', '')}")
    print(f"카테고리: {prompt.get('category', '')}")
    print(f"즐겨찾기: {'예' if prompt.get('favorite', False) else '아니오'}")
    print(f"출처: {prompt.get('source', '')}")
    print(f"내용: {prompt.get('content', '')}")


def toggle_favorite(prompts):
    if not prompts:
        print("\n저장된 프롬프트가 없습니다.")
        return

    view_all_prompts(prompts)

    try:
        choice = int(input("\n즐겨찾기 상태를 바꿀 번호를 입력하세요: "))
        if choice < 1 or choice > len(prompts):
            print("올바른 번호를 입력하세요.")
            return
    except ValueError:
        print("숫자를 입력하세요.")
        return

    prompts[choice - 1]["favorite"] = not prompts[choice - 1].get("favorite", False)
    save_prompts(prompts)

    if prompts[choice - 1]["favorite"]:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기에서 해제되었습니다.")


def delete_prompt(prompts):
    if not prompts:
        print("\n저장된 프롬프트가 없습니다.")
        return

    view_all_prompts(prompts)

    try:
        choice = int(input("\n삭제할 번호를 입력하세요: "))
        if choice < 1 or choice > len(prompts):
            print("올바른 번호를 입력하세요.")
            return
    except ValueError:
        print("숫자를 입력하세요.")
        return

    deleted_prompt = prompts.pop(choice - 1)
    save_prompts(prompts)
    print(f"'{deleted_prompt['title']}' 프롬프트가 삭제되었습니다.")


def sanitize_filename(name):
    invalid_chars = '<>:"/\\|?*'
    safe_name = name.strip()
    for char in invalid_chars:
        safe_name = safe_name.replace(char, "_")
    return safe_name if safe_name else "기타"


def export_markdown_by_category(prompts):
    if not prompts:
        print("\n내보낼 프롬프트가 없습니다.")
        return

    export_dir = "markdown_exports"
    os.makedirs(export_dir, exist_ok=True)

    grouped_prompts = {}
    for prompt in prompts:
        category = prompt.get("category", "기타").strip()
        if not category:
            category = "기타"
        grouped_prompts.setdefault(category, []).append(prompt)

    for category, items in grouped_prompts.items():
        safe_category = sanitize_filename(category)
        file_path = os.path.join(export_dir, f"{safe_category}.md")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {category} 프롬프트 모음\n\n")

            for index, prompt in enumerate(items, start=1):
                favorite_text = "예" if prompt.get("favorite", False) else "아니오"
                file.write(f"## {index}. {prompt.get('title', '')}\n\n")
                file.write(f"- 카테고리: {prompt.get('category', '')}\n")
                file.write(f"- 즐겨찾기: {favorite_text}\n")
                file.write(f"- 출처: {prompt.get('source', '')}\n\n")
                file.write("### 내용\n")
                file.write(f"{prompt.get('content', '')}\n\n")
                file.write("---\n\n")

    print(f"\nMarkdown 내보내기가 완료되었습니다. '{export_dir}' 폴더를 확인하세요.")


def main():
    prompts = load_prompts()

    while True:
        display_menu()
        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            view_all_prompts(prompts)
        elif choice == "2":
            add_prompt(prompts)
        elif choice == "3":
            search_prompts(prompts)
        elif choice == "4":
            view_prompt_detail(prompts)
        elif choice == "5":
            toggle_favorite(prompts)
        elif choice == "6":
            delete_prompt(prompts)
        elif choice == "7":
            export_markdown_by_category(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    main()