import streamlit as st
import pandas as pd
from PIL import Image

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="내 소개",
    page_icon="💻",
    layout="centered"
)

# 2. 메인 헤더
st.title("업성고 3-7 담임 소개")
st.divider()

# 3. 프로필 사진과 기본 정보
col1, col2 = st.columns([1, 2])

with col1:
    # 이미지가 없을 때 보여줄 임시 이미지
    st.image("image.jpg", width=200)

with col2:
    st.subheader("기본 정보")
    st.write("**👨‍🏫 이름:** 정준식")
    st.write("**📚 담당 과목:** 정보컴퓨터")
    st.write("**🏫 소속:** 천안업성고 3학년 7반 담임")
    st.write("**MBTI:** INTP")

st.divider()

# 4. 교육 철학
st.subheader("💡 저의 교육 철학")
st.title("상호간 예의 지키기.")
with st.expander("자세히 읽어보기"):
    st.subheader("""
    - **인사부터:** 인사 안해서 인생에서 손해볼거 하나 없음
    """)
    st.subheader("""
    - **메타인지:** 내가 뭘 알고 모르는지에 대해서 알도록 
    """)

st.divider()

# 5. 시간표 (Pandas 데이터프레임 활용)
st.subheader("📅 이번 학기 시간표")
st.write("질문이 있거나 상담이 필요하면 공강 시간을 확인하고 교무실로 찾아오세요!")

# 시간표 데이터 생성
schedule_data = {
    "교시": ["1교시", "2교시", "3교시", "4교시", "점심", "5교시", "6교시", "7교시"],
    "월": ["정보 (1반)", "공강", "프로그래밍 (3반)", "정보 (2반)", "🍽️", "공강", "동아리", ""],
    "화": ["공강", "정보 (4반)", "공강", "프로그래밍 (1반)", "🍽️", "정보 (5반)", "공강", ""],
    "수": ["프로그래밍 (2반)", "정보 (3반)", "공강", "공강", "🍽️", "정보 (6반)", "자율활동", ""],
    "목": ["공강", "공강", "정보 (1반)", "정보 (4반)", "🍽️", "프로그래밍 (3반)", "공강", ""],
    "금": ["정보 (2반)", "프로그래밍 (1반)", "공강", "정보 (5반)", "🍽️", "공강", "동아리", ""]
}
df_schedule = pd.DataFrame(schedule_data)
# '교시' 컬럼을 인덱스로 설정하여 깔끔하게 출력
df_schedule.set_index("교시", inplace=True) 

# 테이블 출력
st.table(df_schedule)

st.divider()

# 6. Q&A 질문 게시판 (Session State 활용)
st.subheader("❓ 무엇이든 물어보세요 (Q&A)")
st.write("수업 내용, 진로 고민, 또는 가벼운 인사도 좋습니다. 자유롭게 남겨주세요!")

# 세션 상태에 질문 리스트가 없으면 초기화
if 'questions' not in st.session_state:
    st.session_state.questions = []

# 질문 입력 폼
with st.form("qa_form"):
    student_name = st.text_input("이름 (익명 가능)", placeholder="예: 3학년 7반 김코딩")
    question_text = st.text_area("질문 내용", placeholder="여기에 질문을 작성해주세요.")
    submitted = st.form_submit_button("질문 등록하기")
    
    if submitted:
        if question_text.strip() == "":
            st.warning("질문 내용을 입력해주세요!")
        else:
            # 질문을 리스트에 추가
            st.session_state.questions.append({
                "name": student_name if student_name.strip() else "익명",
                "question": question_text
            })
            st.success("질문이 성공적으로 등록되었습니다!")

# 등록된 질문 목록 보여주기 (최신 질문이 위로 오도록 역순 정렬)
if st.session_state.questions:
    st.markdown("#### 📝 등록된 질문 목록")
    for q in reversed(st.session_state.questions):
        with st.chat_message("user"):
            st.write(f"**{q['name']}** 학생의 질문:")
            st.write(q['question'])
else:
    st.info("아직 등록된 질문이 없습니다. 첫 번째 질문의 주인공이 되어보세요!")


import streamlit as st
import time

# ... (기존 상단 소개 코드 생략) ...

st.write("---")
st.header("🤖 '정보 쌤' AI 챗봇")
st.caption("선생님께 궁금한 점을 물어보세요! (예: 파이썬 배우려면 어떻게 해요?)")

# 1. 챗봇 상태 관리 (메시지 기록 저장)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "반가워요! 저는 정보 선생님의 AI 분신입니다. 무엇을 도와줄까요?"}
    ]

# 2. 채팅 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. 채팅 입력 및 응답 로직
if prompt := st.chat_input("질문을 입력하세요..."):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 응답 생성 (여기서는 예시 응답 로직을 넣었습니다)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 실제 API 연결 대신 간단한 조건부 로직 (또는 OpenAI 연동)
        if "파이썬" in prompt:
            assistant_response = "파이썬은 정보 교과에서 가장 중요한 언어예요! 기초 문법부터 차근차근 시작해봅시다."
        elif "이름" in prompt:
            assistant_response = "저는 [이름] 선생님의 지식을 학습한 AI입니다!"
        else:
            assistant_response = "좋은 질문이에요! 그 부분은 제가 선생님께 직접 여쭤보고 나중에 더 자세히 알려줄게요."

        # 타이핑 효과 시뮬레이션
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # AI 메시지 기록 저장
    st.session_state.messages.append({"role": "assistant", "content": full_response})