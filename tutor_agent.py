
from sub_agents.Math.math_agent import MathAgent
from sub_agents.Physics.physics_agent import PhysicsAgent
from gemini import ask_gemini


class TutorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()

    def route_query(self, query: str) -> str:
        math_keywords = ["solve", "calculate", "+", "-", "*", "/", "equation"]
        physics_keywords = ["velocity", "force", "mass", "law", "constant", "gravity", "acceleration"]

        if any(k in query.lower() for k in math_keywords):
            return self.math_agent.handle_query(query)
        elif any(k in query.lower() for k in physics_keywords):
            return self.physics_agent.handle_query(query)
        else:
            return ask_gemini(
                f"A student asked: '{query}'. Act as a Math or Physics teacher. Identify the subject and answer only if it's Math or Physics. If not, respond that it's out of scope."
            )

