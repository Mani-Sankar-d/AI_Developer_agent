from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "filesystem": {
            "transport": "stdio",
            "command": "python",
            "args": [
                "-m",
                "AI_Developer_agent.mcp_servers.filesystem.server"
            ],
        }
    }
)


async def test():
    tools = await client.get_tools()

    for tool in tools:
        print("Name:", tool.name)
        print("Description:", tool.description)
        print("Args:", tool.args)
        print()


import asyncio

if __name__ == "__main__":
    asyncio.run(test())