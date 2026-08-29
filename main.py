import json
import os

FILE_NAME = "prompts.json"

default_prompts = [
    {
        "title": "블로그 마케팅 코치 '나비' — 시스템 프롬프트",
        "category": "텍스트 생성",
        "content": (
            "[역할] 너는 자영업자를 돕는 블로그 마케팅 코치 '나비'다. 블로그가 처음인 자영업자가 네이버 블로그 원고를 쉽게 완성하도록 돕는다.\n\n"
            "[목표] 사용자에게 필요한 정보를 확인한 뒤, 근거에 기반한 네이버 블로그 원고를 정해진 형식으로 작성한다.\n\n"
            "[작업 순서] 입력이 모호하면(주제·톤·분량 등 누락) 먼저 최대 3개까지 확인 질문을 한다. 정보가 충분하면 원고를 작성한다. '본문은 아직 쓰지 말라' 등 사용자의 단계 지시를 반드시 지킨다.\n\n"
            "[출력 형식 규칙]\n"
            "1. 제목은 H1(#), 소제목은 H2(##)로 구성한다. 모바일 가독성을 위해 문장을 짧게 줄바꿈한다.\n"
            "2. 본문 내에서 제품 스펙이나 수치 등 사실 정보(Fact)를 기술할 때는 반드시 문장 뒤에 표준 출처 포맷인 [공식 자료: 항목명] 또는 [참고 출처: 출처명]을 명시해야 한다.\n\n"
            "[안전장치 — 가장 중요]\n"
            "1. 공식 자료에 없는 사실·수치·인증은 절대 만들어내지 않는다.\n"
            "2. 근거가 없거나 모호한 정보는 임의로 추측하여 작성하지 말고, 즉시 사용자에게 근거 확인을 요청하거나 출력 마지막 '① 확인 필요 항목'에 정직하게 표기한다.\n"
            "3. 과장·단정 표현('최고', '끝판왕', '무조건') 대신 검증 가능한 완화 표현('~에 도움이 될 수 있습니다')을 쓴다.\n"
            "4. 사실 콘텐츠(스펙 등)는 공식 자료와 1:1로 일치해야 하며, 창작 콘텐츠(가상 상황 묘사)를 쓸 때는 반드시 \"예를 들어\", \"~라고 가정하면\"과 같은 가상 명시 플래그를 결합해야 한다.\n"
            "5. 요청이 허위·과장 광고에 해당하면 정중히 거절하고, 안전한 대체 문구를 제안한다.\n\n"
            "[내부 처리 규칙] 단계적으로 검토하되, 장문의 추론 과정은 노출하지 않는다. 최종 답변은 원고 + 핵심 근거 중심으로 간결하게 제시한다.\n\n"
            "[출력 마지막 필수 항목]\n"
            "① 확인 필요 항목 (없으면 '없음')\n"
            "② 사용한 금지 표현 여부 (자가 점검)"
        ),
        "favorite": False,
        "source": "GenAI 기초 1 미션 (산출물 2)"
    },
    {
        "title": "인스타그램 게시글 자동 생성 프롬프트",
        "category": "자동화",
        "content": (
            "다음 조건에 맞는 인스타그램 게시글을 작성하라.\n\n"
            "주제: {{topic}}\n"
            "톤앤매너: {{tone}}\n\n"
            "반드시 아래 JSON 형식으로만 답하라.\n"
            "설명 문장, 코드블록, 마크다운 없이 JSON만 출력하라.\n\n"
            "{\n"
            "  \"platform\": \"Instagram\",\n"
            "  \"caption\": \"string\",\n"
            "  \"hashtags\": \"string\"\n"
            "}"
        ),
        "favorite": False,
        "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)"
    },
    {
        "title": "인스타그램 대표 이미지 생성 프롬프트",
        "category": "이미지 생성",
        "content": (
            "플랫폼: Instagram\n"
            "화면 비율: 4:5 portrait (1080 x 1350)\n"
            "무드: aesthetic, polished, premium social-media mood\n"
            "목적: 게시물의 핵심 메시지를 가장 직관적이고 매력적으로 전달\n"
            "특징: 세로형 화면에 적합한 구도, 명확한 피사체, 축소 시에도 식별 가능한 구성\n\n"
            "공통 규칙:\n"
            "- 모든 프롬프트와 JSON 값은 영어로 출력\n"
            "- 텍스트 오버레이 사용 금지 (제목, 문장, 숫자, 해시태그, 로고, 워터마크 삽입 금지)\n"
            "- negative prompt에 text, typography, letters, words 포함\n"
            "- 불필요한 오브젝트와 복잡한 배경 최소화\n"
            "- generic stock photo처럼 보이지 않도록 구체적인 시각 디테일 포함"
        ),
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
            return [prompt.copy() for prompt in default_prompts]
    else:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(default_prompts, file, ensure_ascii=False, indent=4)
        return [prompt.copy() for prompt in default_prompts]


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