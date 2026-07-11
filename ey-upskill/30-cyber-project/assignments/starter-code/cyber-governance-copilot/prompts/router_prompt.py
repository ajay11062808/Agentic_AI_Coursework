ROUTER_PROMPT = """
You are a routing agent.

Determine which knowledge base
should answer the question.

Available:

1. cis_documents

Return ONLY the namespace name.

Question:

{question}
"""