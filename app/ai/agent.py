from app.ai.llm import ask_llm
from app.ai.prompts import SYSTEM_PROMPT
from app.ai.tools import execute_tool
from app.ai.registry import TOOL_REGISTRY


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

    ai_response = ask_llm(prompt)

    tool_name = ai_response.get(
        "tool",
        "GENERAL_CHAT"
    ).upper()

    print(f"\nAI Selected Tool -> {tool_name}\n")

    if tool_name not in TOOL_REGISTRY:

        return {
            "tool": tool_name,
            "response": "Unknown Tool"
        }

    return execute_tool(
        tool_name=tool_name,
        db=db,
        doctor_id=ai_response.get(
            "doctor_id",
            doctor_id
        ),
        patient_id=patient_id,
        appointment_date=ai_response.get(
            "appointment_date"
        ),
        appointment_time=ai_response.get(
            "appointment_time"
        ),
        appointment_id=ai_response.get(
            "appointment_id"
        )
    )