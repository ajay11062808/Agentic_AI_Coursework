import streamlit as st

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