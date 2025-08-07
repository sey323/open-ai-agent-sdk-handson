from agents import Agent
from pydantic import BaseModel


class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str


class GuardrailAgent:
    def __init__(self):
        self.agent = Agent(
            name="Guardrail check",
            handoff_description="宿題かどうかを判定するエージェントです",
            instructions="ユーザーが宿題について質問しているかどうかを判定してください。",
            output_type=HomeworkOutput,
        )
