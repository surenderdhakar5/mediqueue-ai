import google.generativeai as genai

from app.core.config import GEMINI_API_KEY
from app.ai.parser import parse_llm_response


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(prompt: str):
    """
    Send prompt to Gemini and return parsed JSON response.
    """

    response = model.generate_content(prompt)

    return parse_llm_response(response.text)