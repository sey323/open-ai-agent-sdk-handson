from agents import Agent

class MathTutorAgent:
    def __init__(self):
        self.agent = Agent(
            name="Math Tutor",
            handoff_description="数学の質問に特化したエージェントです",
            instructions="数学の問題を分かりやすく解説し、例を交えて丁寧に説明してください。",
        )
