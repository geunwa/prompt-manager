import json
import os
from datetime import datetime

DATA_FILE = "prompts.json"
EXPORT_DIR = "markdown_exports"
CATEGORY_OPTIONS = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def get_default_prompts():
    """이전 미션에서 작성한 기본 프롬프트 3개를 반환합니다.

    prompts.json 파일이 없거나 손상된 경우에도 과제 요구사항(기본 프롬프트
    최소 3개 등록)을 항상 만족하도록 하기 위한 안전장치입니다.
    """
    return [
        {
            "id": 1,
            "title": "블로그 마케팅 코치 '나비' — 시스템 프롬프트",
            "content": (
                "[역할] 너는 자영업자를 돕는 블로그 마케팅 코치 '나비'다. "
                "블로그가 처음인 자영업자가 네이버 블로그 원고를 쉽게 완성하도록 돕는다.\n\n"
                "[목표] 사용자에게 필요한 정보를 확인한 뒤, 근거에 기반한 네이버 블로그 원고를 "
                "정해진 형식으로 작성한다.\n\n"
                "[작업 순서] 입력이 모호하면(주제·톤·분량 등 누락) 먼저 최대 3개까지 확인 질문을 "
                "한다. 정보가 충분하면 원고를 작성한다. '본문은 아직 쓰지 말라' 등 사용자의 단계 "
                "지시를 반드시 지킨다.\n\n"
                "[출력 형식 규칙]\n"
                "1. 제목은 H1(#), 소제목은 H2(##)로 구성한다. 모바일 가독성을 위해 문장을 짧게 "
                "줄바꿈한다.\n"
                "2. 본문 내에서 제품 스펙이나 수치 등 사실 정보(Fact)를 기술할 때는 반드시 문장 뒤에 "
                "표준 출처 포맷인 [공식 자료: 항목명] 또는 [참고 출처: 출처명]을 명시해야 한다.\n\n"
                "[안전장치 — 가장 중요]\n"
                "1. 공식 자료에 없는 사실·수치·인증은 절대 만들어내지 않는다.\n"
                "2. 근거가 없거나 모호한 정보는 임의로 추측하여 작성하지 말고, 즉시 사용자에게 근거 "
                "확인을 요청하거나 출력 마지막 '① 확인 필요 항목'에 정직하게 표기한다.\n"
                "3. 과장·단정 표현('최고', '끝판왕', '무조건') 대신 검증 가능한 완화 표현('~에 도움이 "
                "될 수 있습니다')을 쓴다.\n"
                "4. 사실 콘텐츠(스펙 등)는 공식 자료와 1:1로 일치해야 하며, 창작 콘텐츠(가상 상황 "
                "묘사)를 쓸 때는 반드시 \"예를 들어\", \"~라고 가정하면\"과 같은 가상 명시 플래그를 "
                "결합해야 한다.\n"
                "5. 요청이 허위·과장 광고에 해당하면 정중히 거절하고, 안전한 대체 문구를 제안한다.\n\n"
                "[내부 처리 규칙] 단계적으로 검토하되, 장문의 추론 과정은 노출하지 않는다. 최종 답변은 "
                "원고 + 핵심 근거 중심으로 간결하게 제시한다.\n\n"
                "[출력 마지막 필수 항목]\n"
                "① 확인 필요 항목 (없으면 '없음')\n"
                "② 사용한 금지 표현 여부 (자가 점검)"
            ),
            "category": "텍스트 생성",
            "tags": [],
            "favorite": False,
            "source": "GenAI 기초 1 미션 (산출물 2)",
            "created_at": "이전 미션 작성",
        },
        {
            "id": 2,
            "title": "인스타그램 게시글 자동 생성 프롬프트",
            "content": (
                "다음 조건에 맞는 인스타그램 게시글을 작성하라.\n\n"
                "주제: {{topic}}\n"
                "톤앤매너: {{tone}}\n\n"
                "반드시 아래 JSON 형식으로만 답하라.\n"
                "설명 문장, 코드블록, 마크다운 없이 JSON만 출력하라.\n\n"
                "{\n"
                '  "platform": "Instagram",\n'
                '  "caption": "string",\n'
                '  "hashtags": "string"\n'
                "}"
            ),
            "category": "자동화",
            "tags": [],
            "favorite": False,
            "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)",
            "created_at": "이전 미션 작성",
        },
        {
            "id": 3,
            "title": "인스타그램 대표 이미지 생성 프롬프트",
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
            "category": "이미지 생성",
            "tags": [],
            "favorite": False,
            "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)",
            "created_at": "이전 미션 작성",
        },
    ]


def load_prompts():
    """JSON 파일에서 프롬프트 목록을 불러옵니다.

    파일이 없거나, 비어 있거나, 형식이 손상된 경우에는 기본 프롬프트 3개로
    자동 초기화합니다. 또한 id/tags/favorite 같은 필수 키가 빠진 항목이
    있으면 자동으로 채워 넣어 프로그램이 죽지 않도록 방어합니다.
    """
    if not os.path.exists(DATA_FILE):
        prompts = get_default_prompts()
        save_prompts(prompts)
        return prompts

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("저장된 데이터를 불러오는 중 문제가 발생했습니다. 기본 프롬프트로 시작합니다.")
        prompts = get_default_prompts()
        save_prompts(prompts)
        return prompts

    if not isinstance(data, list) or not data:
        prompts = get_default_prompts()
        save_prompts(prompts)
        return prompts

    changed = False
    for index, prompt in enumerate(data, start=1):
        if "id" not in prompt:
            prompt["id"] = index
            changed = True
        if "tags" not in prompt:
            prompt["tags"] = []
            changed = True
        if "favorite" not in prompt:
            prompt["favorite"] = False
            changed = True

    if changed:
        save_prompts(data)

    return data


def save_prompts(prompts):
    """프롬프트 목록을 JSON 파일에 저장합니다."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(prompts, file, ensure_ascii=False, indent=2)
    except OSError:
        print("데이터 저장 중 오류가 발생했습니다.")


def generate_id(prompts):
    """다음 프롬프트 ID를 생성합니다."""
    if not prompts:
        return 1
    return max(prompt["id"] for prompt in prompts) + 1


def is_duplicate_title(prompts, title):
    """제목 중복 여부를 확인합니다."""
    normalized = title.strip().lower()
    for prompt in prompts:
        if prompt["title"].strip().lower() == normalized:
            return True
    return False


def input_non_empty(message):
    """비어 있지 않은 문자열을 입력받습니다."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


def choose_category():
    """미리 정의된 목록에서 카테고리를 선택하거나 직접 입력받습니다."""
    print("카테고리를 선택하세요.")
    for index, category in enumerate(CATEGORY_OPTIONS, start=1):
        print(f"{index}. {category}")
    print("(목록에 없는 이름을 쓰려면 번호 대신 카테고리 이름을 바로 입력하세요.)")

    choice = input_non_empty("카테고리 번호 또는 이름: ")

    if choice.isdigit():
        index = int(choice)
        if 1 <= index <= len(CATEGORY_OPTIONS):
            selected = CATEGORY_OPTIONS[index - 1]
            if selected == "기타":
                return input_non_empty("사용할 카테고리 이름을 입력하세요: ")
            return selected
        print("목록에 없는 번호입니다. 입력하신 값을 카테고리명으로 사용합니다.")
        return choice

    return choice


def add_prompt(prompts):
    """새 프롬프트를 추가합니다."""
    print("\n[ 프롬프트 추가 ]")
    title = input_non_empty("제목: ")

    if is_duplicate_title(prompts, title):
        print("같은 제목의 프롬프트가 이미 존재합니다. 다른 제목을 사용해주세요.")
        return

    content = input_non_empty("내용: ")
    category = choose_category()
    tags_input = input("태그(쉼표로 구분, 선택): ").strip()

    tags = []
    if tags_input:
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

    prompt = {
        "id": generate_id(prompts),
        "title": title,
        "content": content,
        "category": category,
        "tags": tags,
        "favorite": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    prompts.append(prompt)
    save_prompts(prompts)
    print("프롬프트가 저장되었습니다.")


def list_prompts(prompts):
    """전체 프롬프트 목록을 출력합니다."""
    print("\n[ 전체 프롬프트 목록 ]")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    for prompt in prompts:
        star = "★" if prompt.get("favorite") else " "
        print(f"[{prompt['id']}] {star} {prompt['title']} / {prompt['category']}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def search_prompts(prompts):
    """키워드로 프롬프트를 검색합니다."""
    print("\n[ 프롬프트 검색 ]")
    keyword = input_non_empty("검색어를 입력하세요: ").lower()

    results = []
    for prompt in prompts:
        title = prompt["title"].lower()
        content = prompt["content"].lower()
        category = prompt["category"].lower()
        tags = " ".join(prompt.get("tags", [])).lower()

        if keyword in title or keyword in content or keyword in category or keyword in tags:
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    print(f"\n검색 결과: {len(results)}건")
    for prompt in results:
        star = "★" if prompt.get("favorite") else " "
        print(f"[{prompt['id']}] {star} {prompt['title']} / {prompt['category']}")


def find_prompt_by_id(prompts, prompt_id):
    """ID로 프롬프트를 찾습니다."""
    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt
    return None


def view_prompt_detail(prompts):
    """프롬프트 상세 정보를 출력합니다."""
    print("\n[ 프롬프트 상세 보기 ]")
    try:
        prompt_id = int(input("상세 보기할 프롬프트 ID: "))
    except ValueError:
        print("숫자 ID를 입력해주세요.")
        return

    prompt = find_prompt_by_id(prompts, prompt_id)
    if not prompt:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    print("\n--- 프롬프트 상세 정보 ---")
    print(f"ID: {prompt['id']}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"태그: {', '.join(prompt.get('tags', [])) if prompt.get('tags') else '없음'}")
    print(f"즐겨찾기: {'예' if prompt.get('favorite') else '아니오'}")
    print(f"생성일: {prompt.get('created_at', '정보 없음')}")
    print("내용:")
    print(prompt["content"])
    print("-------------------------")


def toggle_favorite(prompts):
    """즐겨찾기 상태를 변경합니다."""
    print("\n[ 즐겨찾기 설정/해제 ]")
    try:
        prompt_id = int(input("프롬프트 ID: "))
    except ValueError:
        print("숫자 ID를 입력해주세요.")
        return

    prompt = find_prompt_by_id(prompts, prompt_id)
    if not prompt:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    prompt["favorite"] = not prompt.get("favorite", False)
    save_prompts(prompts)

    if prompt["favorite"]:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기에서 해제되었습니다.")


def list_favorites(prompts):
    """즐겨찾기 프롬프트만 출력합니다."""
    print("\n[ 즐겨찾기 목록 ]")
    favorites = [prompt for prompt in prompts if prompt.get("favorite")]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for prompt in favorites:
        print(f"[{prompt['id']}] ★ {prompt['title']} / {prompt['category']}")

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def delete_prompt(prompts):
    """프롬프트를 삭제합니다."""
    print("\n[ 프롬프트 삭제 ]")
    try:
        prompt_id = int(input("삭제할 프롬프트 ID: "))
    except ValueError:
        print("숫자 ID를 입력해주세요.")
        return

    prompt = find_prompt_by_id(prompts, prompt_id)
    if not prompt:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    confirm = input(f"정말 '{prompt['title']}' 프롬프트를 삭제할까요? (y/n): ").strip().lower()
    if confirm == "y":
        prompts.remove(prompt)
        save_prompts(prompts)
        print("프롬프트가 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다.")


def list_categories(prompts):
    """카테고리 목록을 출력합니다."""
    print("\n[ 카테고리 목록 ]")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    categories = sorted(set(prompt["category"] for prompt in prompts))
    for index, category in enumerate(categories, start=1):
        count = sum(1 for prompt in prompts if prompt["category"] == category)
        print(f"{index}. {category} ({count}개)")


def view_by_category(prompts):
    """선택한 카테고리의 프롬프트를 출력합니다."""
    print("\n[ 카테고리별 조회 ]")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    categories = sorted(set(prompt["category"] for prompt in prompts))
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        choice = int(input("카테고리 번호를 선택하세요: "))
        if choice < 1 or choice > len(categories):
            print("올바른 번호를 선택해주세요.")
            return
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    selected = categories[choice - 1]
    filtered = [prompt for prompt in prompts if prompt["category"] == selected]

    print(f"\n[{selected}] 카테고리 프롬프트")
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for prompt in filtered:
        star = "★" if prompt.get("favorite") else " "
        print(f"[{prompt['id']}] {star} {prompt['title']}")

    print(f"\n총 {len(filtered)}개의 프롬프트")


def sanitize_filename(name):
    """파일명에 사용할 수 있도록 문자열을 정리합니다."""
    invalid_chars = '<>:"/\\|?*'
    result = name.strip()
    for ch in invalid_chars:
        result = result.replace(ch, "_")
    return result.replace(" ", "_")


def export_category_markdown(prompts):
    """카테고리별로 Markdown 파일을 생성합니다. (보너스 1)"""
    print("\n[ 카테고리별 Markdown 내보내기 ]")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    os.makedirs(EXPORT_DIR, exist_ok=True)
    categories = sorted(set(prompt["category"] for prompt in prompts))

    for category in categories:
        filename = os.path.join(EXPORT_DIR, f"{sanitize_filename(category)}.md")
        filtered = [prompt for prompt in prompts if prompt["category"] == category]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# {category} 프롬프트 모음\n\n")
            for prompt in filtered:
                file.write(f"## {prompt['title']}\n\n")
                file.write(f"- ID: {prompt['id']}\n")
                file.write(f"- 즐겨찾기: {'예' if prompt.get('favorite') else '아니오'}\n")
                file.write(f"- 태그: {', '.join(prompt.get('tags', [])) if prompt.get('tags') else '없음'}\n")
                file.write(f"- 생성일: {prompt.get('created_at', '정보 없음')}\n\n")
                file.write("### 내용\n")
                file.write(f"{prompt['content']}\n\n---\n\n")

    print(f"카테고리별 Markdown 파일 생성이 완료되었습니다. '{EXPORT_DIR}' 폴더를 확인하세요.")


def print_menu():
    """메인 메뉴를 출력합니다."""
    print("\n===== AI 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 프롬프트 조회")
    print("3. 프롬프트 검색")
    print("4. 프롬프트 상세 보기")
    print("5. 즐겨찾기 설정/해제")
    print("6. 즐겨찾기 목록 보기")
    print("7. 프롬프트 삭제")
    print("8. 카테고리 목록 보기")
    print("9. 카테고리별 조회")
    print("10. 카테고리별 Markdown 내보내기")
    print("0. 종료")


def main():
    prompts = load_prompts()

    while True:
        print_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            list_prompts(prompts)
        elif choice == "3":
            search_prompts(prompts)
        elif choice == "4":
            view_prompt_detail(prompts)
        elif choice == "5":
            toggle_favorite(prompts)
        elif choice == "6":
            list_favorites(prompts)
        elif choice == "7":
            delete_prompt(prompts)
        elif choice == "8":
            list_categories(prompts)
        elif choice == "9":
            view_by_category(prompts)
        elif choice == "10":
            export_category_markdown(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()