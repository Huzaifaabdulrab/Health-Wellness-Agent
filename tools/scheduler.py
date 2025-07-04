from agents.tool import function_tool

@function_tool
def CheakShaduletool(day: str = "Sunday") -> str:
    return f"Health check-in set for {day} at 8 AM."