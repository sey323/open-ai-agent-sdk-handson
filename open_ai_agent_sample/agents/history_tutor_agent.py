from agents import Agent

class HistoryTutorAgent:
    def __init__(self):
        self.agent = Agent(
            name="History Tutor",
            handoff_description="Specialist agent for historical questions",
            instructions="You provide assistance with historical queries. Explain important events and context clearly.",
        )
