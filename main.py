import json
import os

FILE_NAME = "prompts.json"


default_prompts = [
    {
        "title": "블로그 마케팅 코치 '나비' — 시스템 프롬프트",
        "category": "텍스트 생성",
        "content": "자영업자를 위한 네이버 블로그 원고를 근거 기반으로 작성하도록 돕는 시스템 프롬프트입니다.",
        "favorite": False,
        "source": "GenAI 기초 1 미션 (산출물 2)"
    },
    {
        "title": "인스타그램 게시글 자동 생성 프롬프트",
        "category": "자동화",
        "content": "주제와 톤앤매너를 입력받아 인스타그램 게시글을 JSON 형식으로 생성하는 프롬프트입니다.",
        "favorite": False,
        "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)"
    },
    {
        "title": "인스타그램 대표 이미지 생성 프롬프트",
        "category": "이미지 생성",
        "content": "인스타그램용 4:5 비율 대표 이미지를 만들기 위한 이미지 생성 프롬프트입니다.",
        "favorite": False,
        "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)"
    }
]


def load_prompts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)

                for prompt in data:
                    if "favorite" not in prompt:
                        prompt["favorite"] = False
                    if "source" not in prompt:
                        prompt["source"] = ""

                return data

        except (json.JSONDecodeError, FileNotFoundError):
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(default_prompts, file, ensure_ascii=False, indent=4)
            return default_prompts.copy()
    else:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(default_prompts, file, ensure_ascii=False, indent=4)
        return default_prompts.copy()


def save_prompts_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


prompts = load_prompts()


def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 저장")
    print("2. 전체 프롬프트 조회")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")


def save_prompt():
    title = input("프롬프트 제목: ").strip()
    if not title:
        print("제목은 비워둘 수 없습니다.")
        return

    category = input("카테고리: ").strip()
    if not category:
        print("카테고리는 비워둘 수 없습니다.")
        return

    content = input("프롬프트 내용: ").strip()
    if not content:
        print("프롬프트 내용은 비워둘 수 없습니다.")
        return

    source = input("출처(없으면 엔터): ").strip()

    new_prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False,
        "source": source
    }

    prompts.append(new_prompt)
    save_prompts_to_file()
    print("프롬프트가 저장되었습니다.")


def view_prompts():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    print("\n===== 전체 프롬프트 목록 =====")
    for i, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else ""
        print(f"{i}. {prompt['title']} / {prompt['category']} {favorite_mark}")


def view_by_category():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    category = input("조회할 카테고리를 입력하세요: ").strip()
    if not category:
        print("카테고리를 입력하세요.")
        return

    found = False

    print(f"\n===== '{category}' 카테고리 프롬프트 =====")
    for i, prompt in enumerate(prompts, start=1):
        if prompt["category"] == category:
            favorite_mark = "★" if prompt.get("favorite", False) else ""
            print(f"{i}. {prompt['title']} / {prompt['category']} {favorite_mark}")
            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def search_prompts():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ").strip().lower()
    if not keyword:
        print("검색어를 입력하세요.")
        return

    found = False

    print(f"\n===== '{keyword}' 검색 결과 =====")
    for i, prompt in enumerate(prompts, start=1):
        if keyword in prompt["title"].lower() or keyword in prompt["content"].lower():
            favorite_mark = "★" if prompt.get("favorite", False) else ""
            print(f"{i}. {prompt['title']} / {prompt['category']} {favorite_mark}")
            found = True

    if not found:
        print("검색 결과가 없습니다.")


def view_prompt_detail():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    view_prompts()

    try:
        number = int(input("상세 보기할 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            prompt = prompts[number - 1]
            print("\n===== 프롬프트 상세 보기 =====")
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"내용: {prompt['content']}")
            print(f"출처: {prompt.get('source', '없음') if prompt.get('source', '') else '없음'}")
            print(f"즐겨찾기: {'예' if prompt.get('favorite', False) else '아니오'}")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def toggle_favorite():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    view_prompts()

    try:
        number = int(input("즐겨찾기 추가/해제할 프롬프트 번호를 입력하세요: "))
        if 1 <= number <= len(prompts):
            prompts[number - 1]["favorite"] = not prompts[number - 1].get("favorite", False)
            save_prompts_to_file()

            if prompts[number - 1]["favorite"]:
                print("즐겨찾기에 추가되었습니다.")
            else:
                print("즐겨찾기가 해제되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


def view_favorites():
    found = False
    print("\n===== 즐겨찾기 목록 =====")

    for i, prompt in enumerate(prompts, start=1):
        if prompt.get("favorite", False):
            print(f"{i}. {prompt['title']} / {prompt['category']} ★")
            found = True

    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")


def main():
    while True:
        show_menu()
        choice = input("원하는 기능 번호를 입력하세요: ").strip()

        if choice == "1":
            save_prompt()
        elif choice == "2":
            view_prompts()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            search_prompts()
        elif choice == "5":
            view_prompt_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            view_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력하세요.")


if __name__ == "__main__":
    main()