from retrievers.retrieval_service import (
    RetrievalService
)

service = RetrievalService()

results = service.retrieve(
    "password requirements",
    "cis_windows"
)

print("\nMATCHES")

for r in results:

    print("\nSCORE:", r.score)

    print("\nMETADATA:")

    print(r.metadata)