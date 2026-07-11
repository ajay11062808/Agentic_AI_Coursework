from openai import OpenAI

from config.settings import (
    TOP_K
)

from config.secrets import (
    get_openai_key
)

from retrievers.pinecone_client import (
    PineconeClient
)


class RetrievalService:

    def __init__(self):

        self.index = (
            PineconeClient.get_index()
        )

        self.client = OpenAI(
            api_key=get_openai_key()
        )

    def create_embedding(
        self,
        query: str
    ):

        response = (
            self.client.embeddings.create(
                model="text-embedding-3-small",
                input=query
            )
        )

        return (
            response
            .data[0]
            .embedding
        )

    def retrieve(
        self,
        query: str,
        *namespaces
    ):
        # Accept either multiple namespace args or a single iterable
        if len(namespaces) == 1 and isinstance(namespaces[0], (list, tuple)):
            namespaces = namespaces[0]

        embedding = self.create_embedding(query)

        if self:
            pass

        print(f"Embedding length: {len(embedding)}")
        print(f"Namespaces: {namespaces}")

        all_matches = []

        # If no namespace provided, query default (no namespace)
        if not namespaces:
            result = self.index.query(
                vector=embedding,
                top_k=TOP_K,
                include_metadata=True
            )

            all_matches = result.matches

        else:
            for ns in namespaces:
                result = self.index.query(
                    namespace=ns,
                    vector=embedding,
                    top_k=TOP_K,
                    include_metadata=True
                )

                print(f"\nRAW PINECONE RESPONSE for namespace={ns}")
                print(result)

                all_matches.extend(result.matches)

        # Deduplicate matches by id, keeping the highest score
        best = {}

        for m in all_matches:
            mid = getattr(m, 'id', None) or getattr(m, 'match_id', None) or str(m)

            if mid not in best or float(m.score) > float(best[mid].score):
                best[mid] = m

        return list(best.values())
        # embedding = (
        #     self.create_embedding(query)
        # )

        # result = self.index.query(
        #     namespace=namespace,
        #     vector=embedding,
        #     top_k=TOP_K,
        #     include_metadata=True
        # )

        # return result.matches