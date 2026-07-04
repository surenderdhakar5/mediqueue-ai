from app.ai.llm import ask_llm
from app.ai.prompts import SYSTEM_PROMPT
from app.ai.tools import execute_tool


def run_agent(
    user_input: str,
    db=None,
    doctor_id=None,
    patient_id=None
):
    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_input}
"""

    tool_name = ask_llm(prompt).strip().upper()

    print(f"\nAI Selected Tool -> {tool_name}\n")

    if tool_name == "DOCTOR_DASHBOARD":
        return execute_tool(
            tool_name,
            db=db,
            doctor_id=doctor_id
        )

    elif tool_name == "PATIENT_DASHBOARD":
        return execute_tool(
            tool_name,
            db=db,
            patient_id=patient_id
        )

    elif tool_name == "GENERAL_CHAT":
        return {
            "tool": tool_name,
            "response": "Hello! How can I help you today?"
        }

    return {
        "tool": tool_name,
        "response": "Tool not implemented yet."
    }