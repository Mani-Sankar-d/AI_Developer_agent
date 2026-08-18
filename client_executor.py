from langchain_core.messages import HumanMessage
from AI_Developer_agent.backend.app.agent.graph.graph import create_graph
from AI_Developer_agent.backend.app.agent.graph.state import AgentState


async def execute():
    agent_graph = await create_graph()
    state = AgentState(messages=[])
    while True:
        query = input("USER: ")
        if(query=="exit"):
            break
        state["messages"].append(
            HumanMessage(content=query)
        )
        result = await agent_graph.ainvoke(state)
        state = result
        message = state["messages"][-1].content

        if isinstance(message, list):
            message = "\n".join(
                block["text"]
                for block in message
                if block.get("type") == "text"
            )

        print(f"AGENT:\n{message}")

import asyncio

if __name__ == "__main__":
    asyncio.run(execute())