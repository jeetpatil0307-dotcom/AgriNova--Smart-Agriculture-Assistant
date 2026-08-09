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
            st.session_state.active_disease_context = ""
            st.session_state.detected_disease_context = None
            st.rerun()
            
    st.markdown(t("Ask me anything about farming, crops, diseases, or best practices!"))
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    if "active_disease_context" not in st.session_state:
        st.session_state.active_disease_context = ""

    # Check if passed detected disease info from Disease Detection page
    if st.session_state.get("detected_disease_context"):
        context_data = st.session_state.pop("detected_disease_context")
        info = context_data.get("info", {})
        conf = context_data.get("confidence", 0.0)
        
        disease_name = info.get("name", "Unknown Disease")
        conf_str = f"{conf * 100:.2f}%" if isinstance(conf, (int, float)) else str(conf)
        
        # System context string for Groq LLM background awareness
        ctx_str = (
            f"Detected Disease: {disease_name} (Confidence: {conf_str}). "
            f"Description: {info.get('description', '')}. "
            f"Causes: {info.get('causes', '')}. "
            f"Symptoms: {info.get('symptoms', '')}. "
            f"Prevention: {info.get('prevention', '')}. "
            f"Treatment: {info.get('treatment', '')}. "
            f"Pesticide: {info.get('pesticide', '')}. "
            f"Organic Treatment: {info.get('organic_treatment', '')}. "
            f"Fertilizer: {info.get('fertilizer', '')}."
        )
        st.session_state.active_disease_context = ctx_str
        
        # User-facing initial chat message summarizing detected disease details
        initial_msg = (
            f"🌿 **{t('Detected Disease Context Loaded')}:**\n\n"
            f"• **{t('Disease Detected')}:** {t(disease_name)} ({conf_str})\n"
            f"• **{t('Description')}:** {t(info.get('description', ''))}\n"
            f"• **{t('Symptoms')}:** {t(info.get('symptoms', ''))}\n"
            f"• **{t('Prevention')}:** {t(info.get('prevention', ''))}\n"
            f"• **{t('Treatment')}:** {t(info.get('treatment', ''))}\n"
            f"• **{t('Recommended Fungicide/Pesticide')}:** {t(info.get('pesticide', ''))}\n"
            f"• **{t('Fertilizer Recommendation')}:** {t(info.get('fertilizer', ''))}\n\n"
            f"💬 {t('I have loaded this disease context. How can I help you further with managing this plant condition?')}"
        )
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": initial_msg
        })

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    prompt = st.chat_input(t("Type your question here..."))
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.spinner(t("Thinking...")):
            ctx = st.session_state.get("active_disease_context", "")
            response = get_ai_response(prompt, context=ctx)
            translated_response = t(response)
            
        st.session_state.messages.append({"role": "assistant", "content": translated_response})
        with st.chat_message("assistant"):
            st.markdown(translated_response)
