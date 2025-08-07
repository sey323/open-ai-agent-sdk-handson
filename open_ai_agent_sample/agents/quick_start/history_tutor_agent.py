from agents import Agent

class HistoryTutorAgent:
    def __init__(self):
        self.agent = Agent(
            name="History Tutor",
            handoff_description="歴史の質問に特化したエージェントです",
            instructions="歴史に関する質問に丁寧に答えます。重要な出来事や背景を分かりやすく説明してください。",
        )
