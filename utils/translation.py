from deep_translator import GoogleTranslator
import streamlit as st

# Pre-defined UI Translation Dictionary for instant fallback and reliability
UI_TRANSLATIONS = {
    "mr": {
        "Welcome to AgriNova AI 🌾": "ॲग्रीनोव्हा AI मध्ये आपले स्वागत आहे 🌾",
        "Your Professional Smart Agriculture Assistant": "तुमचा व्यावसायिक स्मार्ट कृषी सहाय्यक",
        "Plant Disease Detection 🌿": "वनस्पती रोग निदान 🌿",
        "Upload an image of a plant leaf to detect potential diseases and get actionable advice.": "संभाव्य रोगांचे निदान करण्यासाठी आणि उपाययोजना मिळवण्यासाठी वनस्पतींच्या पानांचे चित्र अपलोड करा.",
        "Choose an image...": "प्रतिमा निवडा...",
        "Uploaded Image": "अपलोड केलेली प्रतिमा",
        "Check Disease": "रोग तपासा",
        "Analyzing...": "विश्लेषण करत आहे...",
        "Analysis Complete!": "विश्लेषण पूर्ण झाले!",
        "Unable to analyze image. Please try again.": "प्रतिमेचे विश्लेषण करण्यात अक्षम. कृपया पुन्हा प्रयत्न करा.",
        "Low confidence prediction. Please upload a clear image of a single leaf.": "कमी खात्रीची शक्यता. कृपया एकाच पानाचे स्पष्ट चित्र अपलोड करा.",
        "Disease Detected": "आढळलेला रोग",
        "Confidence": "खात्री (Confidence)",
        "Diagnosis & Symptoms": "निदान आणि लक्षणे",
        "Description": "वर्णन",
        "Causes": "कारणे",
        "Symptoms": "लक्षणे",
        "Actionable Management & Recommendations": "उपाययोजना आणि शिफारसी",
        "Prevention": "प्रतिबंध / प्रतिबंधात्मक उपाय",
        "Treatment": "उपचार",
        "Recommended Fungicide/Pesticide": "शिफारस केलेले बुरशीनाशक/कीटकनाशक",
        "Organic Control Methods": "जैविक नियंत्रण पद्धती",
        "Fertilizer Recommendation": "खत शिफारस",
        "💬 Ask AI Assistant": "💬 AI सहाय्यकाला विचारा",
        "AI Agriculture Assistant 🤖": "AI कृषी सहाय्यक 🤖",
        "Ask me anything about farming, crops, diseases, or best practices!": "मला शेती, पिके, रोग किंवा उत्तम पद्धतींबद्दल काहीही विचारा!",
        "Type your question here...": "तुमचा प्रश्न येथे टाईप करा...",
        "🗑 Clear Chat": "🗑 चॅट साफ करा",
        "Thinking...": "विचार करत आहे...",
        "About AgriNova AI ℹ️": "ॲग्रीनोव्हा AI बद्दल ℹ️",
        "Our Mission": "आमचे ध्येय",
        "The Purpose": "उद्देश",
        "Core Features": "मुख्य वैशिष्ट्ये",
        "Key Features:": "मुख्य वैशिष्ट्ये:",
        "Key Benefits": "प्रमुख फायदे",
        "Future Vision of AgriNova AI": "ॲग्रीनोव्हा AI चे भविष्यकालीन व्हिजन",
        "Home": "मुख्यपृष्ठ",
        "Disease Detection": "रोग निदान",
        "AI Assistant": "AI सहाय्यक",
        "About": "माहिती",
        "Multi-Language": "बहु-भाषा",
        "Available in English, Marathi, and Hindi.": "इंग्रजी, मराठी आणि हिंदीमध्ये उपलब्ध.",
        "Navigate using the sidebar to explore the features!": "वैशिष्ट्ये पाहण्यासाठी साइडबार वापरून नेव्हिगेट करा!"
    },
    "hi": {
        "Welcome to AgriNova AI 🌾": "एग्रीनोवा AI में आपका स्वागत है 🌾",
        "Your Professional Smart Agriculture Assistant": "आपका पेशेवर स्मार्ट कृषि सहायक",
        "Plant Disease Detection 🌿": "पौधों के रोग का पता लगाना 🌿",
        "Upload an image of a plant leaf to detect potential diseases and get actionable advice.": "संभावित रोगों का पता लगाने और उपाय पाने के लिए पौधे की पत्ती की छवि अपलोड करें।",
        "Choose an image...": "एक छवि चुनें...",
        "Uploaded Image": "अपलोड की गई छवि",
        "Check Disease": "रोग की जांच करें",
        "Analyzing...": "विश्लेषण हो रहा है...",
        "Analysis Complete!": "विश्लेषण पूरा हुआ!",
        "Unable to analyze image. Please try again.": "छवि का विश्लेषण करने में असमर्थ। कृपया पुनः प्रयास करें।",
        "Low confidence prediction. Please upload a clear image of a single leaf.": "कम सटीकता की संभावना। कृपया एक स्पष्ट पत्ती की छवि अपलोड करें।",
        "Disease Detected": "पाया गया रोग",
        "Confidence": "विश्वसनीयता",
        "Diagnosis & Symptoms": "निदान और लक्षण",
        "Description": "विवरण",
        "Causes": "कारण",
        "Symptoms": "लक्षण",
        "Actionable Management & Recommendations": "प्रबंधन और सिफारिशें",
        "Prevention": "रोकथाम",
        "Treatment": "उपचार",
        "Recommended Fungicide/Pesticide": "अनुशंसित कवकनाशी/कीटनाशक",
        "Organic Control Methods": "जैविक नियंत्रण तरीके",
        "Fertilizer Recommendation": "उर्वरक सिफारिश",
        "💬 Ask AI Assistant": "💬 AI सहायक से पूछें",
        "AI Agriculture Assistant 🤖": "AI कृषि सहायक 🤖",
        "Ask me anything about farming, crops, diseases, or best practices!": "मुझसे खेती, फसलों, बीमारियों या सर्वोत्तम तरीकों के बारे में कुछ भी पूछें!",
        "Type your question here...": "अपना प्रश्न यहाँ टाइप करें...",
        "🗑 Clear Chat": "🗑 चैट साफ़ करें",
        "Thinking...": "सोच रहा है...",
        "About AgriNova AI ℹ️": "एग्रीनोवा AI के बारे में ℹ️",
        "Our Mission": "हमारा मिशन",
        "The Purpose": "उद्देश्य",
        "Core Features": "मुख्य विशेषताएं",
        "Key Features:": "मुख्य विशेषताएं:",
        "Key Benefits": "मुख्य लाभ",
        "Future Vision of AgriNova AI": "एग्रीनोवा AI का भविष्य का विज़न",
        "Home": "होम",
        "Disease Detection": "रोग पहचान",
        "AI Assistant": "AI सहायक",
        "About": "के बारे में",
        "Multi-Language": "बहु-भाषा",
        "Available in English, Marathi, and Hindi.": "अंग्रेजी, मराठी और हिंदी में उपलब्ध।",
        "Navigate using the sidebar to explore the features!": "सुविधाओं का पता लगाने के लिए साइडबार का उपयोग करके नेविगेट करें!"
    }
}

def is_error_result(res):
    """Detect if GoogleTranslator returned an error page / error string."""
    if not res or not isinstance(res, str):
        return True
    error_indicators = ["Error 500", "Server Error", "That's an error", "That’s an error", "1500.That"]
    return any(ind in res for ind in error_indicators)

def get_translator(target_lang):
    """Returns a translator function for the given language."""
    lang_map = {
        "English": "en",
        "Marathi": "mr",
        "Hindi": "hi"
    }
    target_code = lang_map.get(target_lang, "en")
    
    if target_code == "en":
        return lambda text: text  # No translation needed
        
    def translate(text):
        if not text or not isinstance(text, str):
            return text
            
        # Fast path check in UI_TRANSLATIONS dictionary first
        cached = UI_TRANSLATIONS.get(target_code, {}).get(text)
        if cached:
            return cached
            
        try:
            res = GoogleTranslator(source='auto', target=target_code).translate(text)
            if is_error_result(res):
                return text
            return res
        except Exception:
            return text
            
    return translate

def t(text):
    """Helper function to translate text based on session state."""
    lang = st.session_state.get('language', 'English')
    translator = get_translator(lang)
    return translator(text)
