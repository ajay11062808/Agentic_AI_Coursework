from graph.state import (
    GraphState
)

from retrievers.retrieval_service import (
    RetrievalService
)

from services.llm_service import (
    LLMService
)

from prompts.analysis_prompt import (
    ANALYSIS_PROMPT
)


class RetrievalAgent:

    def __init__(self):

        self.retriever = (
            RetrievalService()
        )

        self.llm = (
            LLMService()
        )

    def __call__(
        self,
        state: GraphState
    ):

        question = (
            state["question"]
        )

        namespace = (
            state["namespace"]
        )


        print(
            "\n[Agent] Retrieval Agent"
        )

        print(
            f"Namespace: {namespace}"
        )

        print(
            f"Matches retrieved: {len(matches)}"
        )

        

        matches = (
            self.retriever.retrieve(
                question,
                namespace
            )
        )

        context_parts = []

        for match in matches:

            text = (
                match.metadata.get(
                    "text",
                    ""
                )
            )

            context_parts.append(
                text
            )

        context = "\n\n".join(
            context_parts
        )

        state["context"] = (
            context
        )

        prompt = (
            ANALYSIS_PROMPT.format(
                question=question,
                context=context
            )
        )

        answer = (
            self.llm.invoke(
                prompt
            )
        )

        state["answer"] = answer

        return state