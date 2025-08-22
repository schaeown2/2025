import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="하루치 학생 감정 분석", page_icon="📊", layout="wide")

# 제목
st.title("📊 하루치 학생 감정 분석")
st.write("예시 학생들의 하루 일기를 바탕으로 감정을 분석합니다 😊😢😐")

# 🔹 예시 데이터
data = {
    "이름": ["철수", "영희", "민수", "지혜", "현우"],
    "일기": [
        "오늘 수업이 너무 재미있었어요!",
        "친구랑 다퉈서 속상했어요",
        "그냥 평범한 하루였어요",
        "선생님이 칭찬해주셔서 기분이 좋았어요",
        "숙제가 많아서 스트레스 받았어요"
    ]
}

df = pd.DataFrame(data)

# 🔹 감정 분석
results = []
for text in df["일기"]:
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        results.append("긍정 😊")
    elif polarity < 0:
        results.append("부정 😢")
    else:
        results.append("중립 😐")

df["감정 결과"] = results

# 📑 학생별 결과
st.subheader("📑 학생별 감정 분석 결과")
st.dataframe(df)

# 📊 하루 전체 감정 분포 (파이 차트)
st.subheader("📊 하루 전체 감정 분포")
counts = df["감정 결과"].value_counts()
fig, ax = plt.subplots()
counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, ylabel="")
st.pyplot(fig)

# 👩‍🎓 감정별 학생 수 (바 차트)
st.subheader("👩‍🎓 감정별 학생 수")
fig2, ax2 = plt.subplots()
counts.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# 📌 오늘의 요약
st.subheader("📌 오늘의 요약")
st.success(f"😊 긍정적인 학생 수: {sum(df['감정 결과'] == '긍정 😊')}")
st.info(f"😐 중립적인 학생 수: {sum(df['감정 결과'] == '중립 😐')}")
st.warning(f"😢 부정적인 학생 수: {sum(df['감정 결과'] == '부정 😢')}")

# ⚠️ 부정 감정을 보인 학생
st.subheader("⚠️ 부정 감정을 보인 학생")
negative_students = df[df["감정 결과"] == "부정 😢"]["이름"].tolist()
if negative_students:
    st.error(", ".join(negative_students) + " → 격려가 필요합니다 💡")
else:
    st.write("오늘은 부정적인 감정을 가진 학생이 없습니다! 🎉")

