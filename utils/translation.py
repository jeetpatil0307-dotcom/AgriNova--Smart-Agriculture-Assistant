from deep_translator import GoogleTranslator
import streamlit as st

def get_translator(target_lang):
    """Returns a translator function for the given language."""
    lang_map = {
        "English": "en",
        "Marathi": "mr",
        "Hindi": "hi"
    }
    target_code = lang_map.get(target_lang, "en")
    
    if target_code == "en":
        return lambda text: text # No translation needed
        
    def translate(text):
        if not text:
            return text
        try:
            return GoogleTranslator(source='auto', target=target_code).translate(text)
        except Exception as e:
            return text
            
    return translate

def t(text):
    """Helper function to translate text based on session state."""
    lang = st.session_state.get('language', 'English')
    translator = get_translator(lang)
    return translator(text)
