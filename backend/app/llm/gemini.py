from google import genai
from google.genai import types

from AI_Developer_agent.backend.app.llm.models import (
    LLMMessage,
    LLMResponse,
)
from AI_Developer_agent.backend.app.llm.client import BaseLLMClient
from AI_Developer_agent.backend.app.agent.prompts import SYSTEM_PROMPT


class GeminiClient(BaseLLMClient):
    def __init__(self, api_key: str, model: str):
        self.client = genai.Client(api_key=api_key)
        self.model = model

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
    ):
        contents = self._build_contents(messages)

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
            ),
        )

        return LLMResponse(
            content=response.text if response.text else None,
        )