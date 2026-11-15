# ============================================================
# Program : Streamlit PDF File Upload
# Author  : Ishwari Vijaykumar Surve
# Target:
# Let the user upload a PDF file and confirm the upload
# Run    : streamlit run 04_file_upload.py
# ============================================================

import streamlit as st

st.title("Streamlit Basics : PDF File Upload")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")
