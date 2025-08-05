from agents import Agent

class MathTutorAgent:
    def __init__(self):
        self.agent = Agent(
            name="Math Tutor",
            handoff_description="Specialist agent for math questions",
            instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
        )
