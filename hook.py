from agents import RunHooks
from openai.types import ToolStartEvent, ToolEndEvent, AgentStartEvent, AgentEndEvent, HandoffEvent
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

class MyHooks(RunHooks):
    async def on_tool_start(self, event: ToolStartEvent):
        logging.info(f"[{datetime.now()}]  Tool started: {event.tool.name} with input: {event.input}")

    async def on_tool_end(self, event: ToolEndEvent):
        logging.info(f"[{datetime.now()}]  Tool ended: {event.tool.name} with output: {event.output}")

    async def on_agent_start(self, event: AgentStartEvent):
        logging.info(f"[{datetime.now()}]  Agent started: {event.agent.name} with input: {event.input}")

    async def on_agent_end(self, event: AgentEndEvent):
        logging.info(f"[{datetime.now()}]  Agent ended: {event.agent.name} with output: {event.output}")

    async def on_handoff(self, event: HandoffEvent):
        logging.info(f"[{datetime.now()}]  Handoff from {event.from_agent.name} to {event.target_agent.name}")
        if hasattr(event.context, "handoff_logs"):
            event.context.handoff_logs.append(f"Handoff from {event.from_agent.name} to {event.target_agent.name} at {datetime.now()}")
