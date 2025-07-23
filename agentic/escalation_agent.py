from agents.tool import function_tool

@function_tool
def EscalationAgent(issue: str = "emergency") -> str:
    return (
        f"This seems critical: '{issue}'. Please seek help from a certified healthcare provider immediately."
    )