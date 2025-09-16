import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=httpx.Client(verify=False)
)

# Custom CSS for beautification
st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
        }
        h1 {
            color: #2c3e50;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #ffffff;
            border: 1px solid #2c3e50;
            padding: 10px;
            border-radius: 8px;
        }
        .stButton > button {
            background-color: #2c3e50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #1a252f;
            color: #f0f8ff;
        }
        .stWarning, .stInfo, .stError {
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("🩺 MediBot - Your Medical Assistant")
st.write("Welcome to **MediBot**! Ask me about medical questions, health advice, or summarize symptoms. 🧠💬")

# Disclaimer
st.warning("⚠️ **Disclaimer:** This chatbot provides general information and is not a replacement for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for personalized guidance.")

# Input field
user_query = st.text_input("💬 Enter your medical question, symptoms, or request for advice:")

# Button and response
if st.button("🔍 Ask MediBot"):
    if user_query.strip():
        if "flu" in user_query.lower():
            bot_response = "🤒 Common symptoms of the flu include fever, chills, cough, sore throat, runny or stuffy nose, muscle or body aches, headaches, and fatigue. Rest, stay hydrated, and consult a doctor if symptoms worsen."
        elif "headache" in user_query.lower():
            bot_response = "🧠 Headaches can be caused by stress, dehydration, lack of sleep, or underlying conditions. Try resting in a quiet room, drinking water, and over-the-counter pain relievers. If persistent, see a healthcare professional."
        elif "diabetes" in user_query.lower():
            bot_response = "🩸 Diabetes is a condition where blood sugar levels are too high. Symptoms may include frequent urination, excessive thirst, fatigue, and slow-healing sores. Management involves diet, exercise, and medication. Consult an endocrinologist for diagnosis and treatment."
        else:
            bot_response = "🤷 I'm sorry, I can provide general information on common medical topics. For personalized advice, please consult a qualified healthcare provider. What specific question do you have?"

        st.subheader("🧑‍⚕️ MediBot's Response:")
        st.write(bot_response)
        st.info("📌 **Reminder:** This response is for informational purposes only. Please seek advice from a licensed medical professional for any health concerns.")
    else:
        st.error("🚫 Please enter a query.")

# Footer
st.write("---")
st.markdown("🔋 Powered by **OpenAI GPT-3.5-turbo**")

