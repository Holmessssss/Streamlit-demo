import streamlit as st

st.title('欢迎!')
name = st.text_input("请输入你的姓名: ")

if name == " ":
    st.write(f'我叫何藤斌.')
    st.write(f'Hi, My name is Tenbin He, Nice to meet you.')
else:
    st.write(f'我叫{name}.')
    st.write(f'Hi, My name is {name}, Nice to meet you.')



