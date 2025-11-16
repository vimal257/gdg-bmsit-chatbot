import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the page
st.set_page_config(page_title="Simple Chatbot")

# ===================== CUSTOM BACKGROUND (LEFT HALF WHITE) =====================

st.markdown("""
    <style>
        /* Make the left 50% white and the right 50% default color */
        .main {
            background: linear-gradient(to right, white 50%, #f0f2f6 50%);
        }

        /* Optional: center container styling */
        .chat-container {
            background: rgba(255, 255, 255, 0.7);
            padding: 30px;
            margin-top: 30px;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Start chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Title
st.title("Simple Gemini Chatbot")
st.write("Ask me anything!")

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # User input
    user_question = st.text_input("Your question:", key="question")

    # Send button
    if (st.button("Send") or user_question) and user_question:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_question)

                # Show response
                st.write("**AI:**", response.text)

            except Exception as e:
                st.error("Something went wrong! Please check your API key in .env file.")

else:
    st.error("API key not found! Please add your GEMINI_API_KEY to the .env file.")

# End container
st.markdown('</div>', unsafe_allow_html=True)
