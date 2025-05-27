import re
from gemini import ask_gemini
class MathAgent:
    def calculator(self, expression: str):
        try:
            return eval(expression)
        except Exception as e:
            return f"Error in calculation: {e}"

    def handle_query(self, query: str) -> str:
        match = re.search(r"([-+/*()\d\s\.]+)", query)
        if match:
            expression = match.group(1)
            result = self.calculator(expression)
            gemini_prompt = (
                f"A student asked: '{query}'. My math agent calculated it to be {result}."
                "If it is syntax error don't mention it."
                "Can you explain the steps or verify the reasoning?"
            )
        else:
            gemini_prompt = f"A student asked: '{query}'. Please help with the math explanation."
        return ask_gemini(gemini_prompt)