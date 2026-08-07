from AI_Developer_agent.backend.app.tools.base import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"
    description =  "Performs basic arithmetic calculations."
    def schema(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression to evaluate."
                    }
                },
                "required": ["expression"]
            }
        }
    async def run(self, expression:str):
        return eval(expression,{"__builtins__":{}},{})