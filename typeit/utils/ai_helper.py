from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_typing_errors(original_text, typed_text):

    prompt = f"""
    Compare the original text and typed text.

    Original:
    {original_text}

    Typed:
    {typed_text}

    Find:
    1. Most common typing mistake
    2. One short suggestion to improve typing

    Keep response short (2 lines).
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=100
        )
        return response.choices[0].message.content

    except Exception as e:
        print("AI ERROR:", e)
        return "AI feedback unavailable."