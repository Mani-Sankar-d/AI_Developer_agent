from langchain_core.tools import tool
def create_planner(llm, tools):
    tool_info = "\n".join(
        f"""
Tool: {t.name}
Description: {t.description}
Arguments: {t.args}
"""
        for t in tools
    )

    @tool
    async def planner(task: str) -> str:
        """
        Plan a complex task into smaller ordered steps.
        Use this when the task requires multiple actions or dependencies.
        """

        response = await llm.ainvoke(
            f"""
You are a planning component of a software development agent.

Available tools:
{tool_info}

Task:
{task}

Create a concise ordered execution plan.

Rules:
- Only use capabilities provided by the available tools.
- Mention the appropriate tool for each step.
- Do not execute anything.
- Do not call tools.
- Only produce the plan.
"""
        )

        return response.content

    return planner