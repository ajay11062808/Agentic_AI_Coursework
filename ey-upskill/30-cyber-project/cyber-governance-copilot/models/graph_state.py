from typing import TypedDict


class GraphState(TypedDict):

    question: str

    namespace: str

    cis_context: str

    nist_context: str

    gdpr_context: str

    answer: str