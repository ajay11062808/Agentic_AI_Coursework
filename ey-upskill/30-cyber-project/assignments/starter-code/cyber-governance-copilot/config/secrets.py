from dotenv import load_dotenv
import os

load_dotenv()


def get_openai_key():

    key = os.getenv(
        "OPENAI_API_KEY"
    )

    if not key:
        raise ValueError(
            "OPENAI_API_KEY missing"
        )

    return key


def get_groq_key():

    key = os.getenv(
        "GROQ_API_KEY"
    )

    if not key:
        raise ValueError(
            "GROQ_API_KEY missing"
        )

    return key


def get_pinecone_key():

    key = os.getenv(
        "PINECONE_API_KEY"
    )

    if not key:
        raise ValueError(
            "PINECONE_API_KEY missing"
        )

    return key