import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="AgriNova AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.ui import apply_theme
from pages import home, disease_detection, assistant, about

def main():
    # Apply custom CSS theme
    apply_theme()
    
    # Initialize session state for language if not exists
    if 'language' not in st.session_state:
        st.session_state.language = 'English'
        
    # Sidebar Navigation
    with st.sidebar:
        # Center the logo in the sidebar and resize to 120-150px
        import os
        logo_path = os.path.join(os.path.dirname(__file__), "assets", "agrinova_logo.jpg")
        if os.path.exists(logo_path):
            st.image(logo_path, width=140)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/2103/2103446.png", width=120)
            
        st.title("AgriNova AI")
        
        # Language Selector
        st.session_state.language = st.selectbox(
            "Select Language / भाषा निवडा / भाषा चुनें",
            ["English", "Marathi", "Hindi"],
            index=["English", "Marathi", "Hindi"].index(st.session_state.language)
        )
        
        st.markdown("---")
        
        # Menu Options
        menu = ["Home", "Disease Detection", "AI Assistant", "About"]
        if "navigation_choice" not in st.session_state:
            st.session_state.navigation_choice = "Home"
            
        current_index = menu.index(st.session_state.navigation_choice) if st.session_state.navigation_choice in menu else 0
        choice = st.radio("Navigation", menu, index=current_index)
        st.session_state.navigation_choice = choice
        
    # Route to the selected page
    if choice == "Home":
        home.render()
    elif choice == "Disease Detection":
        disease_detection.render()
    elif choice == "AI Assistant":
        assistant.render()
    elif choice == "About":
        about.render()

if __name__ == "__main__":
    main()
