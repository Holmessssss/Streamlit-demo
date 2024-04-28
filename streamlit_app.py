import streamlit as st

st.title('我的第一个Streamlit应用')
st.write('欢迎来到Streamlit的世界！')

sidebar_input = st.sidebar.text_input("在这里输入内容")
sidebar_slider = st.sidebar.slider("选择一个数值", 0, 100)

