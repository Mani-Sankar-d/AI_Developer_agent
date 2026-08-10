from AI_Developer_agent.backend.app.agent.graph.state import AgentState
from AI_Developer_agent.backend.app.tools import tools
from AI_Developer_agent.backend.app.core.settings import settings
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode
from langgraph.graph import END

def create_llm_node(llm):
    async def llm_node(state: AgentState):
        response = await llm.ainvoke(state["messages"])
        return {"messages":[response]}
    return  llm_node

def should_continue(state:AgentState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END


llm = ChatGoogleGenerativeAI(
    model=settings.MODEL,
    api_key=settings.KEY,
)

llm_with_tools = llm.bind_tools(tools)

tool_node = ToolNode(tools)
llm_node = create_llm_node(llm_with_tools)