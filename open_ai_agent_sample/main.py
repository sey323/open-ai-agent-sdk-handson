import asyncio
import os
from dotenv import load_dotenv
from open_ai_agent_sample.agents.triage_agent import TriageAgent
from agents import Runner
from agents.exceptions import InputGuardrailTripwireTriggered

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

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
                print("Guardrail blocked this input:", e)
    except KeyboardInterrupt:
        print("\n終了します")

if __name__ == "__main__":
    asyncio.run(main())
