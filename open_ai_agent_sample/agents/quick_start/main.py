import asyncio
from open_ai_agent_sample.config import get_env
from open_ai_agent_sample.agents.quick_start.triage_agent import TriageAgent
from agents import Runner
from agents.exceptions import InputGuardrailTripwireTriggered

async def stream_output(text):
    for chunk in text.split("。"):
        if chunk:
            print(chunk + "。", end="", flush=True)
            await asyncio.sleep(0.2)
    print()

async def main():
    triage_agent = TriageAgent().agent
    print("インタラクティブモード: 質問を入力してください (Ctrl+Cで終了)")
    try:
        while True:
            user_input = input("> ")
            if not user_input.strip():
                continue
            try:
                result = await Runner.run(triage_agent, user_input)
                await stream_output(str(result.final_output))
            except InputGuardrailTripwireTriggered as e:
                await stream_output(f"宿題に関係ない質問だったので、ガードレールでブロックされました: {e}")
    except KeyboardInterrupt:
        print("\n終了します")

if __name__ == "__main__":
    asyncio.run(main())
