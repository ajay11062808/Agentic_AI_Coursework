from graph.state import GraphState

from services.llm_service import (
    LLMService
)

from prompts.analysis_prompt import (
    ANALYSIS_PROMPT
)


class AnalysisAgent:

    def __init__(self):

        self.llm = (
            LLMService()
        )

    def __call__(
        self,
        state: GraphState
    ):

        print(
            "\n[Agent] Analysis Agent"
        )

        combined_context = (
            state["cis_context"]
            + "\n\n"
            + state["nist_context"]
            + "\n\n"
            + state["gdpr_context"]
        )

        prompt = (
            ANALYSIS_PROMPT.format(
                question=state["question"],
                context=combined_context
            )
        )

        answer = (
            self.llm.invoke(
                prompt
            )
        )

        state["answer"] = answer

        return state