from agents.tool import function_tool

@function_tool
def NutrtionExpertAgent(query: str = "daily protein needs") -> str:
    return (
        f"As a certified nutritionist, here’s advice for '{query}': "
        "An average adult needs 0.8g of protein per kg of body weight. "
        "Adjust based on activity level."
    )