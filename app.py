import streamlit as st
import google.generativeai as genai
import os

# 1. 화면 제목 설정
st.title("🍱 인공지능 점심 메뉴 추천기")
st.write("못 먹는 음식이나 선호하는 스타일을 입력하면 메뉴를 추천해드려요!")

# 2. 사용자 입력 받기
user_input = st.text_input("예: 매운 거 못 먹어, 일식 좋아해", placeholder="내용을 입력하세요.")

# 3. 버튼 클릭 시 작동
if st.button("메뉴 추천받기"):
    # Streamlit 관리자 화면에 등록할 API 키를 가져오는 코드
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # AI에게 보낼 명령(프롬프트) 조합
    prompt = f"너는 최고의 요리사야. 사용자의 요구사항 '{user_input}'에 맞는 점심 메뉴 3가지를 추천하고 이유를 짧게 설명해줘."
    
    with st.spinner('AI가 메뉴를 고민 중입니다...'):
        response = model.generate_content(prompt)
        st.success("추천 결과입니다!")

        st.write(response.text)
