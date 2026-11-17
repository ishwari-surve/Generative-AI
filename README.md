# Generative AI

Concept-wise Generative AI programs in Python. They start with building small
web apps using Streamlit, and then build simple AI agents step by step.
Each folder has its own README. More topics will be added as I learn.

## What you will find
- Streamlit basics: title, text input, button, file upload
- Working with PDF files: upload, text extraction and text chunking
- Simple AI agents: rule based agent, tools, multiple tools and memory

The PDF programs and the text chunking program are the base steps of a
RAG (Retrieval Augmented Generation) application.

## Repository structure

| Folder | Topic | Programs |
|---|---|---|
| 01_Streamlit_Basics | Streamlit web apps, PDF upload, PDF text extraction, text chunking | 6 |
| 02_AI_Agents | Rule based agent, calculator tool, multiple tools, memory | 4 |

Total: 2 folders and 10 programs.

## Suggested learning order
1. 01_Streamlit_Basics: build the web page and read a PDF.
2. 02_AI_Agents: build an agent that uses tools and memory.

## Tech stack
Python, Streamlit, PyPDF2

## Setup
1. Install Python 3.9 or newer.
2. Install the libraries (needed only for folder 01):

pip install streamlit PyPDF2

3. Run the programs.

Streamlit programs (folder 01) are started with the streamlit command:

cd 01_Streamlit_Basics
streamlit run 01_hello_streamlit.py

Agent programs (folder 02) use plain Python and need no extra library:

cd 02_AI_Agents
python 01_rule_based_agent.py

## Important notes
- These are learning programs. The agents do not use an AI model. They choose
  their answer by looking for keywords.
- The calculator agents use eval(). eval() runs any Python code that is typed,
  so it is not safe for a real application.
- Agent memory is kept only while the program runs. It is not saved in a file.
- Scanned PDFs (only images) have no text, so the text extraction program may fail on them.

## Related repositories
- Deep-Learning: neural networks, CNN, RNN and Transformers
- Projects: separate repositories

## Author
Ishwari Vijaykumar Surve
