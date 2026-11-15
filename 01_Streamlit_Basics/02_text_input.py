# ============================================================
# Program : Streamlit Text Input
# Author  : Ishwari Vijaykumar Surve
# Target:
# Take text from the user with a text box and show a welcome message
# Run    : streamlit run 02_text_input.py
# ============================================================

import streamlit as st

st.title("Streamlit Basics : Text Input")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")
