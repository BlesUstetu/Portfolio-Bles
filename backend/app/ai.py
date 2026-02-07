import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_ai(message: str) -> str:
    """Send a user message to the LLM and return the assistant reply."""
    if not message or not message.strip():
        return "Please enter a message."

    res = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.strip()},
        ],
    )
    return res.choices[0].message.content
