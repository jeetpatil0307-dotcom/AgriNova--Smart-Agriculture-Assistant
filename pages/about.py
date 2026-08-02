import streamlit as st
from utils.translation import t

def render():
    st.title(t("About AgriNova AI ℹ️"))
    
    st.markdown(f"""
    ### {t('Our Mission')}
    **AgriNova AI** {t('is built with a singular mission: to empower farmers with accessible, actionable, and cutting-edge artificial intelligence. We aim to revolutionize traditional farming by bringing smart, data-driven insights directly to the hands of those who feed the world.')}
    
    ### {t('The Purpose')}
    {t('By bridging the gap between advanced technology and everyday agriculture, AgriNova AI serves as a comprehensive smart farming platform. It helps users quickly diagnose plant health issues, adapt to changing weather conditions, and receive expert-level guidance without needing deep technical or agronomic knowledge.')}
    
    ### {t('Core Features')}
    - 🔍 **{t('Plant Disease Detection')}**: {t('Leveraging state-of-the-art Deep Learning, our platform can identify numerous plant diseases early, preventing crop loss.')}
    - 💬 **{t('AI Agriculture Assistant')}**: {t('A conversational AI trained to provide smart crop guidance and solve complex farming queries.')}
    - 🌤️ **{t('Weather Information')}**: {t('Localized weather tracking that influences AI-generated farming recommendations.')}
    - 🌐 **{t('Multi-language Support')}**: {t('Breaking language barriers by supporting English, Marathi, and Hindi.')}
    
    ### {t('Key Benefits')}
    - 🌱 **{t('Early Disease Detection')}**: {t('Spot problems before they spread, saving time and resources.')}
    - 📈 **{t('Increased Productivity')}**: {t('Optimize yields through precision farming techniques.')}
    - 🛡️ **{t('Improved Crop Health')}**: {t('Targeted treatments lead to stronger, healthier plants.')}
    - 💡 **{t('Better Farming Decisions')}**: {t('Data-backed insights reduce guesswork.')}
    - 🌍 **{t('Sustainable Agriculture')}**: {t('Promotes efficient use of fertilizers and pesticides, protecting the environment.')}
    
    ### {t('Future Vision of AgriNova AI')}
    {t('We envision a future where every farmer, regardless of the size of their operation, has a dedicated AI agronomist in their pocket. AgriNova AI will continue to expand its disease database, integrate with IoT soil sensors, and provide market price forecasting to create a truly holistic smart farming ecosystem.')}
    """)
