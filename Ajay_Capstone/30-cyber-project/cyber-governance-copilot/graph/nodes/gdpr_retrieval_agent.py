from graph.state import GraphState

from retrievers.retrieval_service import (
    RetrievalService
)

from config.settings import (
    GDPR_NAMESPACE
)


class GDPRRetrievalAgent:

    def __init__(self):

        self.retriever = (
            RetrievalService()
        )

    def __call__(
        self,
        state: GraphState
    ):

        print(
            "\n[Agent] GDPR Retrieval Agent"
        )

        matches = (
            self.retriever.retrieve(
                state["question"],
                GDPR_NAMESPACE
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
            "gdpr_context": "\n\n".join(context)
        }