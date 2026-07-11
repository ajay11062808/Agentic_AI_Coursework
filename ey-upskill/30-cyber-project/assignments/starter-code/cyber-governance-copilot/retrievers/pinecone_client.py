from pinecone import Pinecone

from config.secrets import (
    get_pinecone_key
)

from config.settings import (
    PINECONE_INDEX_NAME
)


class PineconeClient:

    @staticmethod
    def get_index():

        pc = Pinecone(
            api_key=get_pinecone_key()
        )

        return pc.Index(
            PINECONE_INDEX_NAME
        )