from agents import Agent, WebSearchTool

class HistoryTutorAgent:
    def __init__(self):
        self.agent = Agent(
            name="History Tutor",
            handoff_description="歴史の質問に特化したエージェントです",
            instructions="歴史に関する質問に丁寧に答えます。重要な出来事や背景を分かりやすく説明してください。より詳細な回答を得るために、必要に応じてWeb検索を行います。検索した結果を引用した場合は、検索元のリンクを明記してください。",
            tools=[WebSearchTool()],
        )
