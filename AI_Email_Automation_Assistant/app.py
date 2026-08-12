import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="AI Email Automation Assistant", page_icon="🤖")
st.title("🤖 AI Email Automation Assistant")
st.write("Generate professional email replies using an LLM API.")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Add GEMINI_API_KEY to your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

email = st.text_area("Paste the email", height=220)
tone = st.selectbox("Reply tone", ["Professional", "Friendly", "Concise", "Formal"])

if st.button("Generate Reply"):
    if not email.strip():
        st.warning("Please enter an email.")
    else:
        prompt = f"""
You are an email automation assistant.
Read the email below and generate a useful reply.

Tone: {tone}

Email:
{email}

Return only the email reply.
"""
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            st.subheader("Generated Reply")
            st.write(response.text)
        except Exception as e:
            st.error(f"API error: {e}")
