from agents.tool import function_tool

@function_tool
def GoaAnalyzerTool(goal :str)-> str:
    return f"your Goal {goal} sound achievable and inspiring!"