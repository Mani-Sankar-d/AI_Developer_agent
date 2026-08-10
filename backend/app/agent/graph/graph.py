from langgraph.graph import StateGraph, START, END
from AI_Developer_agent.backend.app.agent.graph.state import AgentState
from AI_Developer_agent.backend.app.agent.graph.nodes import llm_node,tool_node,should_continue


def create_graph():
    graph = StateGraph(AgentState)
    graph.add_node("llm",llm_node)
    graph.add_node("tools",tool_node)
    graph.add_edge(START, "llm")
    graph.add_conditional_edges(
        "llm",
        should_continue,
    {"tools":"tools",END:END}
    )
    graph.add_edge("tools","llm")
    return graph.compile()

from langchain_core.messages import HumanMessage
agent_graph = create_graph()

async def test():
    result = await agent_graph.ainvoke({
        "messages": [
            HumanMessage(content="What is 234 * 567?")
        ]
    })

    for message in result["messages"]:
        print(message)
import asyncio
asyncio.run(test())