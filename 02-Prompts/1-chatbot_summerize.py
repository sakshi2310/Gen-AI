from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


st.header("Research tool")
user_input = st.text_input("Enter your input:")
model = ChatOpenAI(model='')

if st.button("summerize"):
    result = model.invoke(user_input)
    st.write(result)