# ============================================================
# Program : Streamlit PDF Text Extraction
# Author  : Ishwari Vijaykumar Surve
# Target:
# Upload a PDF file and show the text extracted from all its pages
# Run    : streamlit run 05_pdf_text_extraction.py
# ============================================================

import streamlit as st
import PyPDF2

st.title("Streamlit Basics : PDF Text Extraction")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.text_area("Extracted Text", text)
