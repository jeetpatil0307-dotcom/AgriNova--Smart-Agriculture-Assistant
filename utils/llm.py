import os
import streamlit as st
from groq import Groq

def get_groq_api_key():
    # 1. Check Streamlit secrets (for Streamlit Cloud deployment)
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
        
    # 2. Check Environment Variable
    if "GROQ_API_KEY" in os.environ:
        return os.environ["GROQ_API_KEY"]
        
    # 3. Fallback placeholder
    return "YOUR_GROQ_API_KEY"

def get_groq_client():
    api_key = get_groq_api_key()
    return Groq(api_key=api_key)

def get_ai_response(prompt, context=""):
    try:
        client = get_groq_client()
        messages = [
            {"role": "system", "content": "You are AgriNova AI, a professional and helpful smart agriculture assistant. You provide concise, accurate, and actionable advice to farmers regarding crops, diseases, weather impacts, and general agriculture best practices."}
        ]
        
        if context:
            messages.append({"role": "system", "content": f"Context: {context}"})
            
        messages.append({"role": "user", "content": prompt})
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=1024,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error communicating with AI Assistant. Please ensure your GROQ_API_KEY is set in Streamlit Secrets or Environment Variables. Details: {str(e)}"
