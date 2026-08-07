from AI_Developer_agent.backend.app.tools.base import BaseTool

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        self._tools[tool.name] = tool

    def get(self, name:str):
        return self._tools[name]

    def list(self):
        return list(self._tools.values())

    def schemas(self):
        return [tool.schema() for tool in self._tools.values()]