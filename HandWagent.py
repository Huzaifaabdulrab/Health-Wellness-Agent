# HandWagent.py

from openai import AsyncOpenAI
from agents import Agent, RunConfig, OpenAIChatCompletionsModel
from tools.goal_analyzer import GoaAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheakShaduletool
from tools.tracker import ProgressTrackerTool
from agentic.nutrition_expert import NutrtionExpertAgent
from agentic.injury_support_agent import InjurySupportAgent
from agentic.escalation_agent import EscalationAgent
import os
def health_Wellness_agent():
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    provider = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-1.5-flash",
        openai_client=provider
    )

    run_config = RunConfig(
        model=model,
        model_provider=provider,
        tracing_disabled=True
    )

    agent = Agent(
        instructions="You are Health wellness agent",
        name="Health Wellness expert",
        tools=[
            GoaAnalyzerTool,
            MealPlannerTool,
            WorkoutRecommenderTool,
            CheakShaduletool,
            ProgressTrackerTool,
            NutrtionExpertAgent,
            InjurySupportAgent,
            EscalationAgent
        ]
    )

    return agent, run_config
