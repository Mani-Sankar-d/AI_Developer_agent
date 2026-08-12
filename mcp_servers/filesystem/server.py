from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("Filesystem Server")

@mcp.tool()
def read_file(path: str) -> str:
    """Read and return the contents of a text file"""
    return Path(path).read_text(encoding="utf-8")

if __name__=="__main__":
    mcp.run(transport="stdio")