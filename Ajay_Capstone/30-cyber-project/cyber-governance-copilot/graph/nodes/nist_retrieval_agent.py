from graph.state import GraphState

from retrievers.retrieval_service import (
    RetrievalService
)

from config.settings import (
    NIST_NAMESPACE
)


class NISTRetrievalAgent:

    def __init__(self):

        self.retriever = (
            RetrievalService()
        )

    def __call__(
        self,
        state: GraphState
    ):

        print(
            "\n[Agent] NIST Retrieval Agent"
        )

        matches = (
            self.retriever.retrieve(
                state["question"],
                NIST_NAMESPACE
            )
        )

        context = []

        for match in matches:

            text = (
                match.metadata.get(
                    "text",
                    ""
                )
            )

            context.append(text)

        return {
            "nist_context": "\n\n".join(context)
        }