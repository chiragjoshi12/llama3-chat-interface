from dotenv import load_dotenv
import os

load_dotenv()

from groq import Groq
import streamlit as st

# Groq API
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chat Interface", layout="wide")

# model selection
model = st.sidebar.selectbox(
    "Select Model",
    ("llama3-8b-8192", "llama-3.1-70b-versatile", "llama-3.1-8b-instant", )
)

st.title(f"{model}")

user_input = st.text_area("Enter your prompt:", height=100)

if st.button("Send"):
    if user_input:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model=model,
            )
            
            ai_response = chat_completion.choices[0].message.content
            st.markdown(f"**AI:** {ai_response}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt.")
