import json
import re


def parse_llm_response(text: str):
    """
    Parse Gemini/OpenAI response safely.
    Supports:
    - Plain JSON
    - ```json ... ``` blocks
    - Fallback to GENERAL_CHAT
    """

    text = text.strip()

    # Remove markdown code blocks
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    text = text.strip()

    try:
        return json.loads(text)

    except Exception:

        return {
            "tool": "GENERAL_CHAT",
            "response": text
        }