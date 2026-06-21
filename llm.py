import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(question, context=""):
    prompt = f"""
You are a financial AI assistant.

Question:
{question}

Context:
{context}

Give clear financial insights and suggestions.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text