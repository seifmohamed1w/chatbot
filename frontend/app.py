import streamlit as st
import requests

st.title("Fils Chatbot")

backend_url = "http://localhost:8000/ask"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(backend_url, json={"input": prompt})
    content = response.json().get("answer", "I don't know the answer to that.")

    with st.chat_message("assistant"):
        st.markdown(content)
        st.session_state.messages.append({"role": "assistant", "content": content})
