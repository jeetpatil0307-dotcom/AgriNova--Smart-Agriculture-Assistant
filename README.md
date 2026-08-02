# AgriNova AI 🌾

A professional AI-powered Smart Agriculture web application built entirely using Python and Streamlit. AgriNova AI leverages Deep Learning for plant disease detection and Large Language Models for intelligent farming advice.

## Features
- **Plant Disease Detection**: Upload leaf images to identify diseases and get actionable treatment plans.
- **AI Agriculture Assistant**: Chat with an LLM-powered assistant (Groq) for farming advice.
- **Weather Advisory**: Get real-time weather metrics and localized AI farming recommendations.
- **Multi-Language Support**: Accessible in English, Marathi, and Hindi.
- **Premium Design**: Modern, responsive, and visually appealing Green & White theme.

## Tech Stack
- **Frontend & Routing**: Streamlit
- **Machine Learning**: TensorFlow, Keras
- **Image Processing**: OpenCV, Pillow
- **AI Assistant**: Groq API (LLaMA 3)
- **Translation**: Deep Translator
- **Weather Data**: OpenWeatherMap API

## Setup Instructions

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd AgriNova-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Keys**:
   The application uses placeholder API keys in `utils/llm.py` and `utils/weather.py`. 
   For full functionality, set the following environment variables:
   - `GROQ_API_KEY`: Your Groq API Key
   - `OPENWEATHER_API_KEY`: Your OpenWeatherMap API Key

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Folder Structure
- `app.py`: Main Streamlit application entry point.
- `requirements.txt`: Python dependencies.
- `pages/`: Individual page modules (Home, Disease Detection, Assistant, Weather, About).
- `utils/`: Helper functions and modules (UI, LLM, Weather, Translation, Model).
- `model/`: Directory to place your trained TensorFlow/Keras `.h5` model.
