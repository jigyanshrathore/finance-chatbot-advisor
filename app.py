import streamlit as st
from utils import extract_text_from_pdf
from summarizer import summarize_text
from qa_chain import answer_question
from dotenv import load_dotenv
import os

import os

# If running on Streamlit Cloud, get from secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

st.set_page_config(page_title="📊 Finance Report Analyzer", layout="wide")
st.title("📊 Upload, Summarize & Chat with Financial Reports")

uploaded_file = st.file_uploader("Upload a PDF financial report", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Text extracted.")

    if st.button("Summarize Report"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(raw_text)
        st.subheader("📌 Summary")
        st.write(summary)

    st.subheader("💬 Ask Questions about the Report")
    question = st.text_input("Your question:")
    if st.button("Ask") and question:
        with st.spinner("Getting answer..."):
            response = answer_question(question, raw_text)
        st.markdown(f"**Answer:** {response}")
