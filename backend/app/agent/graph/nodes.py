from AI_Developer_agent.backend.app.agent.graph.state import AgentState
from AI_Developer_agent.backend.app.llm.client import BaseLLMClient

def create_llm_node(llm: BaseLLMClient):
    async def llm_node(state: AgentState):
        response = await llm.generate(
            messages=state["messages"]
        )
        return {
            "messages":[
                *state["messages"],
                response
            ]
        }
    return llm_node