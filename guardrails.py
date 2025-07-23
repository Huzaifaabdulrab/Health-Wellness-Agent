from pydantic import BaseModel
from agents import (
    Agent,
    RunConfig,
    RunContextWrapper,
    Runner,
    GuardrailFunctionOutput,
    input_guardrail,
    output_guardrail
)

# Health input validation model
class HealthWellness(BaseModel):
    isHealthyAndWellness: bool
    reasoning: str

# Output validation model
class Output(BaseModel):
    is_math: bool
    reasoning: str

# Final output format from main agent
class MessageOutput(BaseModel):
    response: str

def get_guardrail_agents(run_config: RunConfig):
    input_agent = Agent(
        name="Health Wellness Input Guardrail",
        instructions="You are a classifier that checks if the input is related to health and wellness. "
                     "Respond with isHealthyAndWellness=True if the input is related to health or wellness, "
                     "and provide reasoning.",
        output_type=HealthWellness,
    )

    output_agent = Agent(
        name="Math Output Guardrail",
        instructions="You are a classifier that checks if the output is related to math. "
                     "Set is_math=True if the output is related to mathematical content.",
        output_type=Output,
    )

    @input_guardrail
    async def health_input_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str | list) -> GuardrailFunctionOutput:
        result = await Runner.run(input_agent, input, context=ctx, run_config=run_config)
        is_valid = result.final_output.isHealthyAndWellness
        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=not is_valid  
        )

    @output_guardrail
    async def health_output_guardrail(ctx: RunContextWrapper, agent: Agent, output: MessageOutput) -> GuardrailFunctionOutput:
        result = await Runner.run(output_agent, output.response, context=ctx.context, run_config=run_config)
        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=result.final_output.is_math  
        )

    return health_input_guardrail, health_output_guardrail
