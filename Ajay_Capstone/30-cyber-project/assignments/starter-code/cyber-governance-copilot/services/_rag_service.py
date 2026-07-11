from retrievers.retrieval_service import (
    RetrievalService
)

from services.llm_service import (
    LLMService
)

from prompts.analysis_prompt import (
    ANALYSIS_PROMPT
)

from config.settings import (
    CIS_NAMESPACE
)


class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()

        self.llm = LLMService()

    def ask(
        self,
        question: str
    ):

        matches = self.retriever.retrieve(
            question,
            CIS_NAMESPACE
        )

        # print("\n")
        # print("=" * 80)
        # print("RETRIEVAL RESULTS")
        # print("=" * 80)

        context_parts = []

        for idx, match in enumerate(matches):

            # print(
            #     f"\nMatch {idx + 1}"
            # )

            # print(
            #     f"Score: {match.score}"
            # )

            # print(
            #     f"Metadata: {match.metadata}"
            # )

            # print("-" * 80)

            #
            # IMPORTANT:
            # We don't yet know the field name.
            #
            text = (
                match.metadata.get("text", "")
            )

            context_parts.append(text)

        context_text = "\n\n".join(
            context_parts
        )

        # print("\n")
        # print("=" * 80)
        # print("CONTEXT SENT TO LLM")
        # print("=" * 80)

        # print(context_text[:3000])

        # print("\n")
        # print("=" * 80)

        prompt = ANALYSIS_PROMPT.format(
            question=question,
            context=context_text
        )

        return self.llm.invoke(
            prompt
        )