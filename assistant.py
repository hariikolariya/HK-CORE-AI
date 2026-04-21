import streamlit as st
import requests
import os

# Page Config
st.set_page_config(page_title="HK CORE AI", page_icon="🤖")
st.title("🤖 HK CORE AI")
st.caption("Created by Harii Kolariya")

# Secure Key
API_KEY = os.getenv("OPENROUTER_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask HK CORE anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call AI
    with st.chat_message("assistant"):
        headers = {"Authorization": f"Bearer {API_KEY}"}
        data = {
            "model": "openrouter/auto",
            "messages": st.session_state.messages
        }
        try:
            response = requests.post(URL, headers=headers, json=data).json()
            answer = response['choices'][0]['message']['content']
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except:
            st.error("Connection lost. Check your API Key.")
