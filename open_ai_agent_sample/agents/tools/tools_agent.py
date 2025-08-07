from agents import Agent, WebSearchTool, CodeInterpreterTool, WebSearchTool


class ToolsAgent:
    def __init__(self):
        self.agent = Agent(
            name="ToolsAgent",
            tools=[
                WebSearchTool(),
                # CodeInterpreterTool(),
            ],
        )
