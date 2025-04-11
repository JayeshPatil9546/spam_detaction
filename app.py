import streamlit as st
import re
from langchain_groq import ChatGroq
import json

# Setup ChatGroq LLM with model and API key
llm = ChatGroq(
    temperature=0,
    groq_api_key='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',  # Replace with your API key
    model_name="llama-3.3-70b-versatile"
)

# Function to preprocess the email text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Removing non-alphabet characters
    return text

# Function to classify the text using the ChatGroq LLM
def classify_text_with_chatgroq(text):
    # Preprocess the input text
    clean_text = preprocess_text(text)
    
    # Query the ChatGroq model to check if the text is spam
    response = llm.invoke(f"Is this email spam? {clean_text}")
    
    # Check result and return classification
    print(response)
    if "spam" in response.content:
        return "Spam"
    else:
        return "Not Spam"

# Set up the Streamlit UI
st.set_page_config(page_title="Spam Mail Detection with ChatGroq", page_icon="📧", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            color: #1E3A8A;
            font-size: 50px;
            font-weight: bold;
            margin-top: 40px;
        }
        .subheader {
            text-align: center;
            color: #4B5563;
            font-size: 24px;
            margin-bottom: 30px;
        }
        .input-area {
            font-size: 18px;
            padding: 20px;
            border-radius: 10px;
            width: 100%;
            max-width: 800px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .button {
            background-color: #2563EB;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 20px 40px;
            cursor: pointer;
            font-size: 22px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            margin-top: 20px;
        }
        .button:hover {
            background-color: #1D4ED8;
        }
        .prediction {
            font-size: 30px;
            font-weight: bold;
            color: #10B981;
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# UI components
st.markdown('<div class="title">Spam Mail Detection with ChatGroq</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Enter your email or message to predict whether it is spam or not.</div>', unsafe_allow_html=True)

# Input form
with st.form(key='email_form', clear_on_submit=True):
    user_input = st.text_area("Enter your email/message", height=250, placeholder="Type or paste an email here...", key="input_area")
    submit_button = st.form_submit_button(label="Predict", use_container_width=True)

# Display the result after prediction
if submit_button:
    if user_input:
        result = classify_text_with_chatgroq(user_input)
        st.markdown(f'<div class="prediction">{result}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a message to classify.")

# Footer with credits
st.markdown("""
    <footer style="text-align:center; padding: 20px;">
        Made with ❤️ by Your Name | <a href="https://github.com/your-github" target="_blank">GitHub</a>
    </footer>
""", unsafe_allow_html=True)
