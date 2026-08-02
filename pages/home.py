import streamlit as st
from utils.translation import t

def render():
    st.title(t("Welcome to AgriNova AI 🌾"))
    st.markdown(f"### {t('Your Professional Smart Agriculture Assistant')}")
    
    # Center the home page image and reduce width to 500px
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://images.unsplash.com/photo-1625246333195-78d9c38ad449?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", width=500)
    
    st.markdown(f"""
    **AgriNova AI** {t('is a state-of-the-art platform designed to empower farmers and agricultural enthusiasts with cutting-edge Artificial Intelligence.')}
    
    #### {t('Key Features:')}
    - 🔍 **{t('Plant Disease Detection')}**: {t('Upload an image of a leaf to instantly identify diseases and get treatment recommendations.')}
    - 💬 **{t('AI Agriculture Assistant')}**: {t('Ask any farming-related questions to our intelligent assistant.')}
    - 🌤️ **{t('Weather Advisory')}**: {t('Get real-time weather updates and AI-driven farming advice.')}
    - 🌐 **{t('Multi-Language')}**: {t('Available in English, Marathi, and Hindi.')}
    
    {t('Navigate using the sidebar to explore the features!')}
    """)
