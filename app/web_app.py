import streamlit as st
from src.pdf_extractor import extract_text_from_pdf
from src.summarizer import SummarizerAgent

st.title("📄 AI PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.success("PDF text extracted successfully!")

    summarizer = SummarizerAgent()
    if st.button("Summarize"):
        summary = summarizer.summarize(text)
        st.subheader("🧠 Summary")
        st.write(summary)
