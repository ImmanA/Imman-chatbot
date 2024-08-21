import streamlit as st
import google.generativeai as genai

st.title("Imman-GPT")

genai.configure(api_key="AIzaSyCoLRyHJsTp_EuOtfCwaG6pbWQ5pcsMwMw")

text=st.text_input("Enter your prompt")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
