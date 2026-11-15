# ============================================================
# Program : Streamlit Button
# Author  : Ishwari Vijaykumar Surve
# Target:
# Show a button and display a message when it is clicked
# Run    : streamlit run 03_button.py
# ============================================================

import streamlit as st

st.title("Streamlit Basics : Button")

if st.button("Python"):
    st.success("Jay Ganesh")
