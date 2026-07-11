# Cyber Governance Copilot -- Multi-Agent Capstone (Finalized)

## Overview

A multi-agent system for
cybersecurity governance using:

-   OpenAI `text-embedding-3-small` (embeddings)
-   Pinecone (vector database)
-   Groq `llama-3.3-70b-versatile` (LLM)
-   LangGraph (agent orchestration)
-   Python CLI

## Project Phases

### Phase 1

-   Basic RAG
-   OpenAI embeddings
-   Pinecone retrieval
-   Groq answer generation
-   CLI chatbot

### Phase 2

-   Router Agent
-   LangGraph workflow
-   Retrieval Agent

### Phase 3

Parallel retrieval architecture:

``` text
                Router
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
      CIS        NIST       GDPR
        │          │          │
        └──────────┼──────────┘
                   ▼
             Analysis Agent
                   ▼
                 Answer
```

Current status: - CIS implemented - NIST placeholder - GDPR placeholder

### Phase 4

Analysis Agent: - Summarization - Recommendations - Framework
comparison - Evidence-based responses

## Agents

1.  Router Agent
2.  CIS Retrieval Agent
3.  NIST Retrieval Agent (planned)
4.  GDPR Retrieval Agent (planned)
5.  Analysis Agent

## Pinecone Namespaces

  Namespace       Status
  --------------- -------------
  cis_documents   Implemented
  nist_800_53     Planned
  gdpr            Planned

## Directory Structure

``` text
cyber-governance-copilot/
├── config/
├── graph/
│   ├── nodes/
│   ├── state.py
│   └── workflow.py
├── models/
├── prompts/
├── retrievers/
├── services/
├── tests/
├── .env
├── requirements.txt
└── main.py
```

## Example Queries

### CIS

-   What are the CIS password requirements?
-   Explain the CIS account lockout policy.
-   Summarize CIS recommendations for Windows authentication.

### Multi-Framework

-   Compare password requirements across CIS, NIST 800-53, and GDPR.
-   What do CIS, NIST, and GDPR collectively recommend for protecting
    privileged administrator accounts?
-   Which CIS controls best support NIST access control requirements,
    and where are the gaps?
-   Generate an executive summary for a CIO on user authentication,
    combining guidance from CIS, NIST, and GDPR.
-   An organization uses MFA, 14-character passwords, and retains logs
    for 30 days. Evaluate this approach against CIS, NIST, and GDPR and
    provide consolidated recommendations.

## Learning Outcomes

-   Agentic RAG
-   Pinecone namespaces
-   LangGraph orchestration
-   Multi-agent systems
-   Prompt engineering
-   Grounded AI
-   Modular Python architecture

## Future Enhancements

-   Load NIST namespace
-   Load GDPR namespace
-   Enable true parallel retrieval
-   Smart routing
-   Confidence scoring
-   Citation validation
-   Architecture assessment agent
-   Streamlit UI
