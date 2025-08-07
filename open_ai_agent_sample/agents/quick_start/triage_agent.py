from agents import Agent, InputGuardrail, Runner, GuardrailFunctionOutput
from open_ai_agent_sample.agents.quick_start.guardrail_agent import GuardrailAgent, HomeworkOutput
from open_ai_agent_sample.agents.quick_start.history_tutor_agent import HistoryTutorAgent


class TriageAgent:
    def __init__(self):
        self.agent = Agent(
            name="Triage Agent",
            instructions="ユーザーの質問内容に応じて適切なエージェントに振り分けます。",
            handoffs=[
                HistoryTutorAgent().agent,
            ],
            input_guardrails=[
                InputGuardrail(guardrail_function=self.homework_guardrail),
            ],
        )

    async def homework_guardrail(self, ctx, agent, input_data):
        guardrail_agent = GuardrailAgent().agent
        result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
        final_output = result.final_output_as(HomeworkOutput)
        return GuardrailFunctionOutput(
            output_info=final_output,
            tripwire_triggered=not final_output.is_homework,
        )
