import os
import sys
import streamlit as st

# Ensure project root is on sys.path so sibling packages can be imported
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from services.rag_service import (
    RAGService
)

st.set_page_config(
    page_title="Cyber Governance Copilot"
)

st.title(
    "Cyber Governance Copilot"
)

question = st.text_area(
    "Ask a question"
)

if st.button("Submit"):

    rag = RAGService()

    answer = rag.ask(
        question
    )

    st.markdown(answer)