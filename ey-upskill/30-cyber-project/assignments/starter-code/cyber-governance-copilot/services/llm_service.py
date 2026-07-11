from groq import Groq

from config.settings import (
    GROQ_MODEL
)

from config.secrets import (
    get_groq_key
)


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=get_groq_key()
        )

    def invoke(
        self,
        prompt: str
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model=GROQ_MODEL,
                temperature=0.2,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )