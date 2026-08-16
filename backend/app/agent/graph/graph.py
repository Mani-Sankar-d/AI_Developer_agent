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

from langchain_core.messages import HumanMessage
async def test():

    agent_graph = await create_graph()

    result = await agent_graph.ainvoke({
        "messages": [
            HumanMessage(
                content="E:/Academics/dummy is ur project directory in there you create a login page UI make the project structure look good use the planner tool to break down the steps and create two or three files and one file within one folder jjust for fun write the html css and js write the js in scripts directory in project keep it minimal maybe 2-3 lines of code"
            )
        ]
    })

    for message in result["messages"]:
        print(message)

import asyncio

if __name__ == "__main__":
    asyncio.run(test())