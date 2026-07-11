# tests/test_namespaces.py

from retrievers.pinecone_client import PineconeClient

index = PineconeClient.get_index()

stats = index.describe_index_stats()

print(stats.to_dict())