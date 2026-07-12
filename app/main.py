import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.agent_core import ask_agent


st.set_page_config(
    page_title="Smart Inventory Agent",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Smart Inventory Intelligence Agent")
st.subheader("Ask me anything about your inventory!")

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your inventory..."):
    st.session_state.message.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("thinking..."):
                response = ask_agent(prompt)

            st.markdown(response)
        st.session_state.message.append({"role": "assistant", "content": response})