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

        self.last_context = ""

        self.last_sources = []

        self.debug = True

    def ask(
        self,
        question: str
    ):

        #
        # Special Commands
        #

        if question.strip() == "/show_context":

            return self._show_context()

        if question.strip() == "/show_sources":

            return self._show_sources()

        matches = self.retriever.retrieve(
            question,
            CIS_NAMESPACE
        )

        context_parts = []

        sources = []

        if self.debug:

            print("\n")
            print("=" * 80)
            print("RETRIEVAL RESULTS")
            print("=" * 80)

        for idx, match in enumerate(matches):

            metadata = match.metadata

            score = round(
                float(match.score),
                4
            )

            #
            # Update this if your metadata
            # field name differs.
            #
            text = metadata.get(
                "text",
                ""
            )

            page = metadata.get(
                "page",
                "Unknown"
            )

            source = metadata.get(
                "source",
                "CIS Benchmark"
            )

            context_parts.append(
                text
            )

            sources.append(
                {
                    "page": page,
                    "source": source,
                    "score": score
                }
            )

            if self.debug:

                print(
                    f"\nMatch {idx + 1}"
                )

                print(
                    f"Score: {score}"
                )

                print(
                    f"Page: {page}"
                )

                print(
                    f"Source: {source}"
                )

                print("-" * 80)

        context_text = "\n\n".join(
            context_parts
        )

        self.last_context = context_text

        self.last_sources = sources

        prompt = (
            ANALYSIS_PROMPT.format(
                question=question,
                context=context_text
            )
        )

        answer = self.llm.invoke(
            prompt
        )

        answer += (
            "\n\n"
            "Retrieved Sources:\n"
        )

        for source in sources:

            answer += (
                f"- Page {source['page']} "
                f"(score={source['score']})\n"
            )

        return answer

    def _show_context(self):

        if not self.last_context:

            return (
                "No context available."
            )

        return (
            "\n"
            + "=" * 80
            + "\nLAST RETRIEVED CONTEXT\n"
            + "=" * 80
            + "\n"
            + self.last_context
        )

    def _show_sources(self):

        if not self.last_sources:

            return (
                "No sources available."
            )

        result = (
            "\n"
            + "=" * 80
            + "\nLAST SOURCES\n"
            + "=" * 80
            + "\n"
        )

        for source in self.last_sources:

            result += (
                f"\nPage: {source['page']}"
                f"\nScore: {source['score']}"
                f"\nSource: {source['source']}\n"
            )

        return result