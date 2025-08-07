import asyncio
from open_ai_agent_sample.config import get_env
from open_ai_agent_sample.agents.quick_start.triage_agent import TriageAgent
from agents import Runner
from agents.exceptions import InputGuardrailTripwireTriggered



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
                print(result.final_output)
            except InputGuardrailTripwireTriggered as e:
                print("宿題に関係ない質問だったので、ガードレールでブロックされました:", e)
    except KeyboardInterrupt:
        print("\n終了します")

if __name__ == "__main__":
    asyncio.run(main())
