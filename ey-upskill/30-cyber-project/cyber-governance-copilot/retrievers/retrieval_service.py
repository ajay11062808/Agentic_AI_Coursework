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
        namespace: str
    ):
        embedding = self.create_embedding(query)

        print(f"Embedding length: {len(embedding)}")
        print(f"Namespace: {namespace}")

        result = self.index.query(
            namespace=namespace,
            vector=embedding,
            top_k=10,
            include_metadata=True
        )

        print("\nRAW PINECONE RESPONSE")
        print(result)

        return result.matches
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