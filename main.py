# 초기 프롬프트 데이터
프롬프트_목록 = [
    {
        "title": "블로그 마케팅 코치 '나비' — 시스템 프롬프트",
        "category": "텍스트 생성",
        "favorite": False,
        "source": "GenAI 기초 1 미션 (산출물 2)",
        "content": """[역할] 너는 자영업자를 돕는 블로그 마케팅 코치 '나비'다. 블로그가 처음인 자영업자가 네이버 블로그 원고를 쉽게 완성하도록 돕는다.

[목표] 사용자에게 필요한 정보를 확인한 뒤, 근거에 기반한 네이버 블로그 원고를 정해진 형식으로 작성한다.

[작업 순서] 입력이 모호하면(주제·톤·분량 등 누락) 먼저 최대 3개까지 확인 질문을 한다. 정보가 충분하면 원고를 작성한다. '본문은 아직 쓰지 말라' 등 사용자의 단계 지시를 반드시 지킨다.

[출력 형식 규칙]
1. 제목은 H1(#), 소제목은 H2(##)로 구성한다. 모바일 가독성을 위해 문장을 짧게 줄바꿈한다.
2. 본문 내에서 제품 스펙이나 수치 등 사실 정보(Fact)를 기술할 때는 반드시 문장 뒤에 표준 출처 포맷인 [공식 자료: 항목명] 또는 [참고 출처: 출처명]을 명시해야 한다.

[안전장치 — 가장 중요]
1. 공식 자료에 없는 사실·수치·인증은 절대 만들어내지 않는다.
2. 근거가 없거나 모호한 정보는 임의로 추측하여 작성하지 말고, 즉시 사용자에게 근거 확인을 요청하거나 출력 마지막 '① 확인 필요 항목'에 정직하게 표기한다.
3. 과장·단정 표현('최고', '끝판왕', '무조건') 대신 검증 가능한 완화 표현('~에 도움이 될 수 있습니다')을 쓴다.
4. 사실 콘텐츠(스펙 등)는 공식 자료와 1:1로 일치해야 하며, 창작 콘텐츠(가상 상황 묘사)를 쓸 때는 반드시 "예를 들어", "~라고 가정하면"과 같은 가상 명시 플래그를 결합해야 한다.
5. 요청이 허위·과장 광고에 해당하면 정중히 거절하고, 안전한 대체 문구를 제안한다.

[내부 처리 규칙] 단계적으로 검토하되, 장문의 추론 과정은 노출하지 않는다. 최종 답변은 원고 + 핵심 근거 중심으로 간결하게 제시한다.

[출력 마지막 필수 항목]
① 확인 필요 항목 (없으면 '없음')
② 사용한 금지 표현 여부 (자가 점검)"""
    },
    {
        "title": "인스타그램 게시글 자동 생성 프롬프트",
        "category": "자동화",
        "favorite": False,
        "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)",
        "content": """다음 조건에 맞는 인스타그램 게시글을 작성하라.

주제: {{topic}}
톤앤매너: {{tone}}

반드시 아래 JSON 형식으로만 답하라.
설명 문장, 코드블록, 마크다운 없이 JSON만 출력하라.

{
  "platform": "Instagram",
  "caption": "string",
  "hashtags": "string"
}"""
    },
    {
        "title": "인스타그램 대표 이미지 생성 프롬프트",
        "category": "이미지 생성",
        "favorite": False,
        "source": "팀프로젝트 14조 (SNS 콘텐츠 자동화)",
        "content": """플랫폼: Instagram
화면 비율: 4:5 portrait (1080 x 1350)
무드: aesthetic, polished, premium social-media mood
목적: 게시물의 핵심 메시지를 가장 직관적이고 매력적으로 전달
특징: 세로형 화면에 적합한 구도, 명확한 피사체, 축소 시에도 식별 가능한 구성

공통 규칙:
- 모든 프롬프트와 JSON 값은 영어로 출력
- 텍스트 오버레이 사용 금지 (제목, 문장, 숫자, 해시태그, 로고, 워터마크 삽입 금지)
- negative prompt에 text, typography, letters, words 포함
- 불필요한 오브젝트와 복잡한 배경 최소화
- generic stock photo처럼 보이지 않도록 구체적인 시각 디테일 포함"""
    }
]


def show_menu():
    print("\n=== 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 저장")
    print("2. 프롬프트 조회")
    print("3. 종료")


def save_prompt():
    print("\n[프롬프트 저장]")

    title = input("제목: ")
    category = input("카테고리: ")
    source = input("출처: ")
    content = input("프롬프트 내용: ")

    새_프롬프트 = {
        "title": title,
        "category": category,
        "favorite": False,
        "source": source,
        "content": content
    }

    프롬프트_목록.append(새_프롬프트)
    print("프롬프트가 저장되었습니다.")


def view_prompts():
    print("\n[프롬프트 조회]")

    if len(프롬프트_목록) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(프롬프트_목록, start=1):
        print(f"{i}. {prompt['title']} ({prompt['category']})")

    choice = input("\n상세 조회할 번호를 입력하세요 (엔터만 누르면 뒤로가기): ")

    if choice == "":
        return

    if not choice.isdigit():
        print("숫자를 입력하세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(프롬프트_목록):
        print("올바른 번호를 입력하세요.")
        return

    prompt = 프롬프트_목록[index]

    print("\n=== 프롬프트 상세 정보 ===")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {prompt['favorite']}")
    print(f"출처: {prompt['source']}")
    print("내용:")
    print(prompt["content"])


def main():
    while True:
        show_menu()
        choice = input("원하는 기능 번호를 입력하세요: ")

        if choice == "1":
            save_prompt()
        elif choice == "2":
            view_prompts()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력하세요.")


main()