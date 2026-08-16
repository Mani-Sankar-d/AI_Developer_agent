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