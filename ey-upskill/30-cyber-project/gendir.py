from pathlib import Path

PROJECT_NAME = "cyber-governance-copilot"

folders = [
    "app",
    "config",
    "graph",
    "graph/nodes",
    "retrievers",
    "services",
    "prompts",
    "models",
    "tests"
]

files = [
    "app/streamlit_app.py",

    "config/settings.py",
    "config/secrets.py",

    "graph/state.py",
    "graph/workflow.py",

    "graph/nodes/router_agent.py",
    "graph/nodes/retrieval_agent.py",
    "graph/nodes/analysis_agent.py",

    "retrievers/pinecone_client.py",
    "retrievers/retrieval_service.py",

    "services/llm_service.py",
    "services/rag_service.py",

    "prompts/router_prompt.py",
    "prompts/analysis_prompt.py",

    "models/graph_state.py",
    "models/response_model.py",

    "tests/test_router.py",
    "tests/test_retrieval.py",
    "tests/test_analysis.py",

    ".env",
    ".env.example",
    "requirements.txt",
    "README.md",
    "main.py"
]

root = Path(PROJECT_NAME)

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    file_path = root / file
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.touch()

print(f"\nProject structure created successfully:")
print(root.resolve())