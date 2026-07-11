from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = "Cyber Governance Copilot"

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

PINECONE_INDEX_NAME = os.getenv(
    "PINECONE_INDEX_NAME"
)

TOP_K = 5

CIS_NAMESPACE = "cis-docs"
NIST_NAMESPACE = "nist_800_53"
GDPR_NAMESPACE = "gdpr"