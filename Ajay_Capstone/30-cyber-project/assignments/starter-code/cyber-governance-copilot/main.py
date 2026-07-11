from graph.workflow import (
    build_graph
)


def main():

    graph = build_graph()

    print(
        "\nCyber Governance Copilot"
    )

    print("=" * 50)

    while True:

        question = input(
            "\nAsk a question (q to quit): "
        )

        if (
            question.lower()
            in ["q", "quit"]
        ):
            break

        # result = graph.invoke(
        #     {
        #         "question": question,
        #         "namespace": "",
        #         "context": "",
        #         "answer": ""
        #     }
        # )


        result = graph.invoke(
            {
                "question": question,
                "namespace": "",
                "cis_context": "",
                "nist_context": "",
                "gdpr_context": "",
                "answer": ""
            }
        )

        print("\n")

        print(
            result["answer"]
        )


if __name__ == "__main__":
    main()