import streamlit as st
from utils.translation import t
from utils.llm import get_ai_response

def render():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(t("AI Agriculture Assistant 🤖"))
    with col2:
        st.write("") # Spacing
        if st.button(t("🗑 Clear Chat")):
            st.session_state.messages = []
            st.rerun()
            
    st.markdown(t("Ask me anything about farming, crops, diseases, or best practices!"))
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    prompt = st.chat_input(t("Type your question here..."))
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.spinner(t("Thinking...")):
            response = get_ai_response(prompt)
            translated_response = t(response)
            
        st.session_state.messages.append({"role": "assistant", "content": translated_response})
        with st.chat_message("assistant"):
            st.markdown(translated_response)
