from graph.state import GraphState

from retrievers.retrieval_service import (
    RetrievalService
)

from config.settings import (
    CIS_NAMESPACE
)


class CISRetrievalAgent:

    def __init__(self):

        self.retriever = (
            RetrievalService()
        )

    def __call__(
        self,
        state: GraphState
    ):

        print(
            "\n[Agent] CIS Retrieval Agent"
        )

        matches = (
            self.retriever.retrieve(
                state["question"],
                CIS_NAMESPACE
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
            "cis_context": "\n\n".join(context)
        }       