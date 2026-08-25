import json
import os

FILE_NAME = "prompts.json"


default_prompts = [
    {
        "title": "자기소개서 작성 도우미",
        "category": "취업",
        "content": "자기소개서를 자연스럽고 설득력 있게 작성하도록 도와줘.",
        "favorite": False
    },
    {
        "title": "영어 단어 암기 도우미",
        "category": "학습",
        "content": "영어 단어를 예문과 함께 외우기 쉽게 정리해줘.",
        "favorite": False
    },
    {
        "title": "파이썬 코드 설명",
        "category": "프로그래밍",
        "content": "초보자도 이해할 수 있게 파이썬 코드를 쉽게 설명해줘.",
        "favorite": False
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

                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return default_prompts.copy()
    else:
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
    title = input("프롬프트 제목: ")
    category = input("카테고리: ")
    content = input("프롬프트 내용: ")

    new_prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False
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
        favorite_mark = "★" if prompt["favorite"] else ""
        print(f"{i}. {prompt['title']} / {prompt['category']} {favorite_mark}")


def view_by_category():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    category = input("조회할 카테고리를 입력하세요: ")
    found = False

    print(f"\n===== '{category}' 카테고리 프롬프트 =====")
    for i, prompt in enumerate(prompts, start=1):
        if prompt["category"] == category:
            favorite_mark = "★" if prompt["favorite"] else ""
            print(f"{i}. {prompt['title']} / {prompt['category']} {favorite_mark}")
            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def search_prompts():
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ").lower()
    found = False

    print(f"\n===== '{keyword}' 검색 결과 =====")
    for i, prompt in enumerate(prompts, start=1):
        if keyword in prompt["title"].lower() or keyword in prompt["content"].lower():
            favorite_mark = "★" if prompt["favorite"] else ""
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
            print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
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
            prompts[number - 1]["favorite"] = not prompts[number - 1]["favorite"]
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
        if prompt["favorite"]:
            print(f"{i}. {prompt['title']} / {prompt['category']} ★")
            found = True

    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")


def main():
    save_prompts_to_file()

    while True:
        show_menu()
        choice = input("원하는 기능 번호를 입력하세요: ")

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


main()