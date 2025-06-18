from dotenv import load_dotenv
import os

# If running on Streamlit Cloud, get from secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
import openai
import os

import streamlit as st

api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Please set it in Streamlit Secrets or .env")

client = openai.OpenAI(api_key=api_key)

def summarize_text(text):
    prompt = (
        "Summarize the following financial report in bullet points:\n"
        + text[:2500]
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
