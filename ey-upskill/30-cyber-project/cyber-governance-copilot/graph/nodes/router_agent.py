from graph.state import (
    GraphState
)

from services.llm_service import (
    LLMService
)

from prompts.router_prompt import (
    ROUTER_PROMPT
)


class RouterAgent:

    def __init__(self):

        self.llm = LLMService()

    def __call__(
        self,
        state: GraphState
    ):

        question = state["question"]

        prompt = ROUTER_PROMPT.format(
            question=question
        )

        response = (
            self.llm.invoke(prompt)
        )

        namespace = (
            response
            .strip()
            .lower()
        )

        if (
            namespace
            != "cis_documents"
        ):
            namespace = (
                "cis_documents"
            )

        state["namespace"] = (
            namespace
        )

        print("\n[Agent] Router Agent")

        print(
            f"Question: {question}"
        )

        print(
            f"Namespace selected: {namespace}"
        )

        return state