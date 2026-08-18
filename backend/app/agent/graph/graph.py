from langgraph.graph import StateGraph, START, END
from AI_Developer_agent.backend.app.agent.graph.state import AgentState
from AI_Developer_agent.backend.app.agent.graph.nodes import (
    create_llm_node,
    should_continue,
)
from AI_Developer_agent.mcp_client.client import client
from AI_Developer_agent.backend.app.core.settings import settings
from langgraph.prebuilt import ToolNode
from AI_Developer_agent.mcp_client.client import client
from AI_Developer_agent.backend.app.rag.rag_tool import search_documents
from AI_Developer_agent.backend.app import llm
from AI_Developer_agent.backend.app.plan.plan_tool import create_planner


async def create_graph():
    mcp_tools = await client.get_tools()
    tools = [*mcp_tools, search_documents]
    planner = create_planner(llm,tools)
    tools = [*tools, planner]
    llm_with_tools = llm.bind_tools(tools)
    tool_node = ToolNode(tools)
    llm_node = create_llm_node(llm_with_tools)
    graph = StateGraph(AgentState)
    graph.add_node("llm", llm_node)
    graph.add_node("tools", tool_node)
    graph.add_edge(START, "llm")
    graph.add_conditional_edges(
        "llm",
        should_continue,
        {
            "tools": "tools",
            END: END,
        }
    )
    graph.add_edge("tools", "llm")
    return graph.compile()