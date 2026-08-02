import streamlit as st

def apply_theme():
    """Applies a custom Green and White premium theme via CSS injection."""
    st.markdown(
        """
        <style>
        /* Main background */
        .stApp {
            background-color: #F8FDF8;
            color: #2F4F2F;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: #1B4D3E !important;
            font-family: 'Inter', sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #EBF7E3 !important;
            border-right: 1px solid #D4EED1;
        }
        [data-testid="stSidebar"] * {
            color: #2F4F2F !important;
        }
        
        /* Sidebar Radio Navigation Options - Larger, Bolder & Prominent */
        [data-testid="stSidebar"] [data-testid="stRadio"] label {
            font-size: 1.18rem !important;
            font-weight: 600 !important;
            padding: 10px 14px !important;
            margin-bottom: 6px !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            transition: all 0.2s ease-in-out !important;
        }
        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
            background-color: #DCEFD2 !important;
            color: #1B4D3E !important;
            transform: translateX(4px);
        }
        
        /* Buttons */
        .stButton>button {
            background-color: #2E8B57 !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #246B43 !important;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }

        /* Inputs */
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
            border-radius: 8px !important;
            border: 1px solid #C5E1A5 !important;
        }
        
        /* File Uploader */
        [data-testid="stFileUploadDropzone"] {
            border: 2px dashed #4CAF50 !important;
            border-radius: 12px !important;
            background-color: #F1F8E9 !important;
        }

        /* Success/Warning messages */
        .stSuccess {
            background-color: #D4EDDA !important;
            color: #155724 !important;
            border-color: #C3E6CB !important;
        }
        .stWarning {
            background-color: #FFF3CD !important;
            color: #856404 !important;
            border-color: #FFEEBA !important;
        }
        
        /* Hide default Streamlit sidebar navigation */
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )
