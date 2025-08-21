import streamlit as st

# 🎭 MBTI별 추천 직업 데이터
job_recommendations = {
    "INTJ": ["🧠 전략기획가", "📊 데이터 사이언티스트", "⚙️ 엔지니어"],
    "ENTP": ["🚀 기업가", "🎯 마케팅 전문가", "💡 스타트업 창업가"],
    "INFJ": ["🧘 상담가", "✍️ 작가", "📚 교육자"],
    "ESFP": ["🎭 배우", "🎉 이벤트 플래너", "🤝 세일즈 매니저"],
    "ISTP": ["🔧 기술자", "🏍️ 모험가", "🕹️ 게임 개발자"],
    "ENFP": ["🌍 여행가", "🎤 방송인", "🎨 크리에이터"],
}

# 🌟 웹앱 제목
st.markdown(
    """
    <h1 style="text-align:center; color:#FF69B4; font-size:50px;">
        🌱✨ MBTI 진로 추천 앱 ✨🌱
    </h1>
    <p style="text-align:center; font-size:20px; color:#555;">
        당신의 성격 유형에 딱 맞는 직업을 찾아보세요! 🚀💡
    </p>
    """,
    unsafe_allow_html=True
)

# 🎯 MBTI 선택
mbti = st.selectbox(
    "💖 당신의 MBTI를 선택하세요:",
    list(job_recommendations.keys())
)

# 🔮 추천 결과 출력
if mbti:
    st.markdown(
        f"""
        <h2 style="color:#4B0082;">
            🔮 {mbti} 유형을 위한 추천 직업 리스트 🎉
        </h2>
        """,
        unsafe_allow_html=True
    )

    for job in job_recommendations[mbti]:
        st.markdown(f"👉 {job}")

    # 🎁 추가 메시지
    st.success("🌟 당신의 미래가 반짝이길 응원합니다! 🌈💼")

# 📌 사이드바 꾸미기
st.sidebar.markdown(
    """
    ## 🎨 앱 가이드  
    1️⃣ MBTI를 선택하세요.  
    2️⃣ 추천 직업을 확인하세요.  
    3️⃣ 새로운 가능성을 발견해 보세요! ✨  

    ---
    🌟 **TIP:**  
    친구들과 함께 비교해도 재미있어요! 🎉  
    """
)
