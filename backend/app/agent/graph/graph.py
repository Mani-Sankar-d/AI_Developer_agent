from langgraph.graph import StateGraph, START, END
from AI_Developer_agent.backend.app.agent.graph.state import AgentState
from AI_Developer_agent.backend.app.agent.graph.nodes import create_llm_node
from AI_Developer_agent.backend.app.llm.client import BaseLLMClient
from AI_Developer_agent.backend.app.llm.gemini import GeminiClient
from AI_Developer_agent.backend.app.llm.models import LLMMessage

def create_graph(llm:BaseLLMClient):
    graph = StateGraph(AgentState)
    graph.add_node("llm",create_llm_node(llm))
    graph.add_edge(START, "llm")
    graph.add_edge("llm",END)
    agent_graph = graph.compile()
    return agent_graph

llm = GeminiClient(GEMINI_API_KEY,GEMINI_MODEL)

graph = create_graph(llm)