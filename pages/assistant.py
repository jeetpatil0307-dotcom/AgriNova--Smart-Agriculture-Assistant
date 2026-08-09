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
            st.session_state.pop("prefill_chat_text", None)
            st.session_state.pop("user_chat_input", None)
            st.rerun()
            
    st.markdown(t("Ask me anything about farming, crops, diseases, or best practices!"))
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # If coming from Disease Detection page, prefill text in the chat input box
    if "prefill_chat_text" in st.session_state and st.session_state["prefill_chat_text"]:
        st.session_state["user_chat_input"] = st.session_state.pop("prefill_chat_text")
            
    prompt = st.chat_input(t("Type your question here..."), key="user_chat_input")
    
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
