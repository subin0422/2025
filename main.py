import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링 (예쁘게 꾸미기)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f8cdda, #1d2b64);
        color: white;
        font-family: 'Pretendard', sans-serif;
    }
    .stSelectbox div div {
        background-color: white;
        color: black;
        border-radius: 8px;
    }
    .stButton button {
        background: linear-gradient(90deg, #ff758c, #ff7eb3);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.5em 1.5em;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
        transition: 0.3s;
    }
    .stButton button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #ff9a9e, #fad0c4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "변호사", "군인", "공무원"],
    "ISFJ": ["교사", "간호사", "사회복지사", "행정직"],
    "INFJ": ["심리상담사", "작가", "교수", "디자이너"],
    "INTJ": ["과학자", "엔지니어", "전략가", "데이터 분석가"],
    "ISTP": ["파일럿", "소방관", "엔지니어", "운동선수"],
    "ISFP": ["예술가", "디자이너", "작곡가", "패션스타일리스트"],
    "INFP": ["작가", "심리학자", "상담사", "언어학자"],
    "INTP": ["연구원", "발명가", "프로그래머", "분석가"],
    "ESTP": ["기업가", "스포츠 선수", "마케팅 전문가", "소방관"],
    "ESFP": ["배우", "가수", "MC", "연예기획자"],
    "ENFP": ["광고 기획자", "스타트업 창업자", "작가", "강연자"],
    "ENTP": ["변호사", "벤처 사업가", "방송인", "정치가"],
    "ESTJ": ["경영자", "군인", "판사", "공무원"],
    "ESFJ": ["교사", "간호사", "인사 담당자", "사회복지사"],
    "ENFJ": ["리더", "강연가", "교수", "심리상담가"],
    "ENTJ": ["CEO", "변호사", "정치가", "전략 컨설턴트"],
}

# 제목
st.markdown("<h1 style='text-align:center; font-size:3em;'>✨ MBTI 기반 진로 추천 ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2em;'>당신의 MBTI를 선택하면, 어울리는 직업을 추천해드립니다 💡</p>", unsafe_allow_html=True)
st.write("---")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 추천 버튼
if st.button("🚀 추천받기"):
    st.markdown(f"<h2 style='text-align:center;'>당신({mbti})에게 추천하는 직업</h2>", unsafe_allow_html=True)

    jobs = mbti_jobs.get(mbti, ["추천 직업 없음"])
    
    cols = st.columns(len(jobs))
    for i, job in enumerate(jobs):
        with cols[i]:
            st.markdown(
                f"""
                <div style="background: rgba(255,255,255,0.2); padding:20px; border-radius:15px; 
                text-align:center; box-shadow:0px 4px 12px rgba(0,0,0,0.3);">
                    <h3 style="color:white;">{job}</h3>
                    <p>💡 이 직업은 {mbti} 성향과 잘 맞아요!</p>
                </div>
                """,
                unsafe_allow_html=True
            )

