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
        image.name = getattr(uploaded_file, 'name', '')
        
        # Reset detection state if a new image file is uploaded
        if st.session_state.get("current_detection_file") != uploaded_file.name:
            st.session_state["current_detection"] = None
            st.session_state["current_detection_file"] = uploaded_file.name

        # Display uploaded image in small preview (width 300px)
        st.image(image, caption=t("Uploaded Image"), width=300)
        
        # "Check Disease" button
        if st.button(t("Check Disease")):
            with st.spinner(t("Analyzing...")):
                loaded_model_data = load_model()
                disease_info, confidence = predict_disease(image, loaded_model_data)
                
                if disease_info:
                    st.session_state["current_detection"] = {
                        "info": disease_info,
                        "confidence": confidence
                    }
                else:
                    st.session_state["current_detection"] = None
                    st.error(t("Unable to analyze image. Please try again."))
                    
        # Render Detection Result & Ask AI Assistant Button if detection is stored
        detection = st.session_state.get("current_detection")
        if detection and detection.get("info"):
            disease_info = detection["info"]
            confidence = detection["confidence"]
            
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
            
            st.markdown("---")
            if st.button(t("💬 Ask AI Assistant")):
                d_name = t(disease_info["name"])
                conf_val = f"{confidence*100:.1f}%" if isinstance(confidence, (int, float)) else str(confidence)
                
                prompt_text = t(
                    f"My plant disease detection result is {d_name} with {conf_val} confidence. "
                    f"Please provide information about its symptoms, causes, prevention, treatment, and suitable organic/fertilizer suggestions."
                )
                
                st.session_state["prefill_chat_text"] = prompt_text
                st.session_state["user_chat_input"] = prompt_text
                st.session_state["navigation_choice"] = "AI Assistant"
                st.rerun()
