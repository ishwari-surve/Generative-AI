# 01 Streamlit Basics

## About
Streamlit is a Python library that turns a Python file into a web page.
You do not need HTML, CSS or JavaScript. These programs build small web apps step by step.
They are the base for a PDF question answering app (RAG).

## How Streamlit works
- The whole file runs from top to bottom each time the user clicks or types something.
- Each st. function adds one element to the page (title, text box, button, message).
- Streamlit apps are started with the streamlit command, not with python.

## Files
| File | What it does | Main functions |
|---|---|---|
| 01_hello_streamlit.py | Shows a title and a line of text | st.title, st.write |
| 02_text_input.py | Takes the user's name and shows a welcome message | st.text_input, st.success |
| 03_button.py | Shows a button and displays a message when clicked | st.button, st.success |
| 04_file_upload.py | Lets the user upload a PDF file | st.file_uploader |
| 05_pdf_text_extraction.py | Reads all pages of the uploaded PDF and shows the text | PyPDF2.PdfReader, extract_text, st.text_area |
| 06_text_chunking.py | Splits a long text into chunks of 100 characters | slicing text[i:i+100], st.info |

## Key points
- st.text_input returns what the user typed. It is empty until the user types.
- st.button returns True only in the run right after the click.
- st.file_uploader(type=["pdf"]) accepts only PDF files.
- PyPDF2 reads text page by page from a PDF.
- Chunking means cutting a big text into small pieces. It is the first step of RAG (Retrieval Augmented Generation).
- In program 06, chunks do not overlap. A sentence can be cut in the middle. Real RAG programs keep some overlap between chunks.

## Concepts covered
- Streamlit page elements
- User input and button handling
- File upload
- PDF text extraction
- Text chunking

## Requirements
- Python 3
- streamlit
- PyPDF2 (files 05 only)

Install: pip install streamlit PyPDF2

## Run
streamlit run 01_hello_streamlit.py

Replace the file name to run another program. The app opens in the browser at http://localhost:8501

## Notes
- Scanned PDFs (only images) have no text. Program 05 may give an error or empty text for them.
