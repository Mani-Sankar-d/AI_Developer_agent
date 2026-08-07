from AI_Developer_agent.backend.app.tools.registry import ToolRegistry
from AI_Developer_agent.backend.app.tools.implementations.calculator import CalculatorTool

tool_registry = ToolRegistry()
tool_registry.register(CalculatorTool())