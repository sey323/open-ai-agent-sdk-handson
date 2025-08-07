from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX


class MathTutorAgent:
    def __init__(self):
        self.agent = Agent(
            name="Math Tutor",
            handoff_description="数学の質問に特化したエージェントです",
            instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
            あなたは数学の問題を分かりやすく解説し、例を交えて丁寧に説明してください。""",
        )
