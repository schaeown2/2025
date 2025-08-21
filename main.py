import streamlit as st

# MBTI별 추천 직업 데이터
job_recommendations = {
    "INTJ": ["전략기획가", "데이터 사이언티스트", "엔지니어"],
    "ENTP": ["기업가", "마케팅 전문가", "스타트업 창업가"],
    "INFJ": ["상담가", "작가", "교육자"],
    "ESFP": ["배우", "이벤트 플래너", "세일즈 매니저"],
    # 필요한 만큼 추가
}

# 웹앱 제목
st.title("🌱 MBTI 기반 진로 추천 웹앱")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    list(job_recommendations.keys())
)

# 추천 결과 출력
if mbti:
    st.subheader(f"🔎 {mbti} 유형을 위한 추천 직업")
    for job in job_recommendations[mbti]:
        st.write(f"- {job}")
