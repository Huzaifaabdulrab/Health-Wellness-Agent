from agents.tool import function_tool

@function_tool
def InjurySupportAgent(injury: str = "knee pain") -> str:
    return (
        f"For injury like '{injury}', apply rest and cold packs. "
        "If pain persists, consult a physiotherapist or medical expert."
    )