from google import genai
from google.genai import types
from AI_Developer_agent.backend.app.llm.models import LLMMessage, LLMResponse
from AI_Developer_agent.backend.app.llm.client import BaseLLMClient
from AI_Developer_agent.backend.app.tools.base import BaseTool
from AI_Developer_agent.backend.app.agent.state import AgentState

from AI_Developer_agent.backend.app.agent.prompts import SYSTEM_PROMPT


class GeminiClient(BaseLLMClient):
    def __init__(self, api_key:str, model:str):
        self.client = genai.Client(api_key = api_key)
        self.model = model

    def _build_tools(self, tools:list[BaseTool]|None):
        if not tools:
            return None
        function_declarations = []
        for tool in tools:
            schema = tool.schema()
            function_declarations.append(
                types.FunctionDeclaration(
                    name=schema["name"],
                    description=schema["description"],
                    parameters=schema["parameters"],
                )
            )
        return [
            types.Tool(function_declarations=function_declarations)
        ]

    def _build_contents(self, messages: list[LLMMessage]):
        contents: list[types.Content] = []

        for message in messages:

            if message.role == "user":
                contents.append(
                    types.Content(
                        role="user",
                        parts=[types.Part(text=message.content)],
                    )
                )

            elif message.role == "assistant":

                if message.raw_content:
                    contents.append(message.raw_content)

                else:
                    contents.append(
                        types.Content(
                            role="model",
                            parts=[types.Part(text=message.content)],
                        )
                    )

            elif message.role == "tool":
                contents.append(
                    types.Content(
                        role="user",
                        parts=[
                            types.Part(
                                function_response=types.FunctionResponse(
                                    name=message.name,
                                    response={"result": message.content},
                                )
                            )
                        ],
                    )
                )

        return contents

    async def generate(
            self,
            messages: list[LLMMessage],
            tools: list[BaseTool] | None = None,
    ):
        contents = self._build_contents(messages)
        gemini_tools = self._build_tools(tools)

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=gemini_tools,
                tool_config=types.ToolConfig(
                    function_calling_config=types.FunctionCallingConfig(
                        mode="AUTO",
                    )
                ),
            ),
        )

        parts = response.candidates[0].content.parts

        return LLMResponse(
            content=response.text if response.text else None,
            tool_calls=[
                {
                    "name": part.function_call.name,
                    "arguments": dict(part.function_call.args),
                }
                for part in parts
                if part.function_call
            ],
            raw_content=response.candidates[0].content,
        )