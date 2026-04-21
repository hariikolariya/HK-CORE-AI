import streamlit as st
import requests
import os

st.set_page_config(page_title="HK CORE AI", page_icon="🤖")
st.title("🤖 HK CORE AI")

API_KEY = os.getenv("OPENROUTER_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask HK CORE anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        headers = {"Authorization": f"Bearer {API_KEY}"}
        data = {
            "model": "openrouter/auto",
            "messages": st.session_state.messages
        }
        try:
            res = requests.post(URL, headers=headers, json=data).json()
            ans = res['choices'][0]['message']['content']
            st.markdown(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})
        except:
            st.error("Error: Check your API Key in Render Environment settings.")
