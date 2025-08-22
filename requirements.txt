import streamlit as st

# 운동별 칼로리 소모량 (분당 kcal)
exercise_data = {
    "🏃 달리기 (8km/h)": 10,
    "🚴 자전거 (보통)": 8,
    "⛹️‍♂️ 줄넘기": 12,
    "🏊 수영": 11,
    "🚶 빠르게 걷기": 5
}

# 웹앱 기본 설정
st.set_page_config(page_title="🔥 칼로리 → 운동 변환기", page_icon="🔥", layout="centered")

st.title("🔥 먹은 음식 칼로리 → 운동 변환기 🔥")
st.markdown("🍔 먹은 칼로리를 입력하면 👉 몇 분간 운동해야 소모되는지 알려드려요! 💪")

# 사용자 입력
calories = st.number_input("✨ 오늘 먹은 음식 칼로리를 입력하세요 (kcal)", min_value=0, step=50)

if calories > 0:
    st.subheader("📊 운동 소요 시간")
    for exercise, burn_rate in exercise_data.items():
        minutes = round(calories / burn_rate, 1)
        st.markdown(
            f"""
            <div style="background-color:#f0f8ff; border-radius:15px; padding:15px; margin:10px 0;
                        box-shadow:2px 2px 10px rgba(0,0,0,0.1);">
                <h4 style="margin:0;">{exercise}</h4>
                <p style="margin:5px 0;">➡️ 약 <b>{minutes}분</b> 필요 ⚡</p>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.info("⬆️ 먼저 칼로리를 입력해주세요!")

