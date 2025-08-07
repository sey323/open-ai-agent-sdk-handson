from agents import Agent
from pydantic import BaseModel


class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str


class GuardrailAgent:
    def __init__(self):
        self.agent = Agent(
            name="Guardrail check",
            instructions="Check if the user is asking about homework.",
            output_type=HomeworkOutput,
        )
