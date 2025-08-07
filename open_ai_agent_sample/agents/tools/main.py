import asyncio
from open_ai_agent_sample.config import get_env
from open_ai_agent_sample.agents.tools.tools_agent import ToolsAgent
from agents import Runner

async def stream_output(text):
    for chunk in text.split("。"):
        if chunk:
            print(chunk + "。", end="", flush=True)
            await asyncio.sleep(0.2)
    print()

async def main():
    tools_agent = ToolsAgent().agent
    print("ツールエージェントCLI: 質問を入力してください (Ctrl+Cで終了)")
    try:
        while True:
            user_input = input("> ")
            if not user_input.strip():
                continue
            result = await Runner.run(tools_agent, user_input)
            await stream_output(str(result.final_output))
    except KeyboardInterrupt:
        print("\n終了します")

if __name__ == "__main__":
    asyncio.run(main())
