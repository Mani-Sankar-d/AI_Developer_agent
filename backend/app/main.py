from AI_Developer_agent.backend.app.agent.graph.graph import agent_graph
result = agent_graph.invoke({
    "messages":["hello"]
})

print(result)