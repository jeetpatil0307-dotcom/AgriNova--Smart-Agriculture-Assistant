import streamlit as st
from PIL import Image
from utils.translation import t
from utils.disease_model import load_model, predict_disease

def render():
    st.title(t("Plant Disease Detection 🌿"))
    st.markdown(t("Upload an image of a plant leaf to detect potential diseases and get actionable advice."))
    
    uploaded_file = st.file_uploader(t("Choose an image..."), type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Display uploaded image in small preview (width 300px)
        st.image(image, caption=t("Uploaded Image"), width=300)
        
        # "Check Disease" button
        if st.button(t("Check Disease")):
            with st.spinner(t("Analyzing...")):
                loaded_model_data = load_model()
                disease_info, confidence = predict_disease(image, loaded_model_data)
                
                if disease_info is None:
                    st.error(t("Unable to analyze image. Please try again."))
                else:
                    if confidence < 0.60:
                        st.warning(t("Low confidence prediction. Please upload a clear image of a single leaf."))
                    else:
                        st.success(t("Analysis Complete!"))
                    
                    # Display Prediction and Confidence
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric(label=t("Disease Detected"), value=t(disease_info["name"]))
                    with col2:
                        st.metric(label=t("Confidence"), value=f"{confidence*100:.2f}%")
                        
                    st.subheader(t("Diagnosis & Symptoms"))
                    st.write(f"**{t('Description')}:** {t(disease_info['description'])}")
                    st.write(f"**{t('Causes')}:** {t(disease_info['causes'])}")
                    st.write(f"**{t('Symptoms')}:** {t(disease_info['symptoms'])}")
                    
                    st.subheader(t("Actionable Management & Recommendations"))
                    st.write(f"**{t('Prevention')}:** {t(disease_info['prevention'])}")
                    st.write(f"**{t('Treatment')}:** {t(disease_info['treatment'])}")
                    st.write(f"**{t('Recommended Fungicide/Pesticide')}:** {t(disease_info['pesticide'])}")
                    st.write(f"**{t('Organic Control Methods')}:** {t(disease_info['organic_treatment'])}")
                    st.write(f"**{t('Fertilizer Recommendation')}:** {t(disease_info['fertilizer'])}")
