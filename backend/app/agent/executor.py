from AI_Developer_agent.backend.app.agent.state import AgentState
from AI_Developer_agent.backend.app.llm.client import BaseLLMClient
from AI_Developer_agent.backend.app.llm.models import LLMMessage
from AI_Developer_agent.backend.app.agent.prompts import SYSTEM_PROMPT
from AI_Developer_agent.backend.app.tools import tool_registry


class AgentExecutor:
    def __init__(self, llm: BaseLLMClient):
        self.llm = llm

    async def execute_tool(self, tool_name: str, **kwargs):
        tool = tool_registry.get(tool_name)
        return await tool.run(**kwargs)

    async def run(self, state: AgentState):
        while True:
            response = await self.llm.generate(
                messages=state.messages,
                tools=tool_registry.list(),
            )
            if not response.tool_calls:
                state.final_response = response.content
                state.messages.append(
                    LLMMessage(
                        role="assistant",
                        content=response.content,
                    )
                )
                return state.final_response

            for tool_call in response.tool_calls:
                state.messages.append(
                    LLMMessage(
                        role="assistant",
                        content=None,
                        tool_call=tool_call,
                    )
                )
                result = await self.execute_tool(
                    tool_call["name"],
                    **tool_call["arguments"],
                )
                state.messages.append(
                    LLMMessage(
                        role="tool",
                        name=tool_call["name"],
                        content=str(result),
                    )
                )
                state.tool_results.append({
                    "name": tool_call["name"],
                    "result": result,
                })