import streamlit as st
from agents.basic_agent import query_basic_agent

st.title("test")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"ai", "content": "Hello"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:=st.chat_input("Enter something: "):
    with st.chat_message("user"):
        st.markdown(prompt)
    response = query_basic_agent(prompt)
    with st.chat_message("ai"):
        st.markdown(response)
    st.session_state.messages.append({"role":"user", "content": prompt}) 
    st.session_state.messages.append({"role":"ai", "content": response})