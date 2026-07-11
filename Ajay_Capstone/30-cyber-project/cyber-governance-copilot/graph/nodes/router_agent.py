from graph.state import (
    GraphState
)

from services.llm_service import (
    LLMService
)

from prompts.router_prompt import (
    ROUTER_PROMPT
)
from config.settings import (
    CIS_NAMESPACE,
    NIST_NAMESPACE,
    GDPR_NAMESPACE
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

        raw = response.strip().lower()

        # Map LLM outputs to known namespace constants
        if "nist" in raw or "800" in raw:
            namespace = NIST_NAMESPACE
        elif "gdpr" in raw:
            namespace = GDPR_NAMESPACE
        elif "cis" in raw:
            namespace = CIS_NAMESPACE
        else:
            # default to CIS if unsure
            namespace = CIS_NAMESPACE

        state["namespace"] = (
            namespace
        )

        print("\n[Agent] Router Agent")

        print(f"Question: {question}")
        print(f"Namespace selected: {namespace}")

        return state