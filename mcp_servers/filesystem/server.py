from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("Filesystem Server")

@mcp.tool()
def read_file(path: str) -> str:
    """Read and return the contents of a text file"""
    return Path(path).read_text(encoding="utf-8")

@mcp.tool()
def list_directory(path) -> str:
    """List files and directories inside the given directory."""
    directory = Path(path)
    if not directory.is_dir():
        raise ValueError(f"Not a directory: {path}")
    return  "\n".join(
        str(item.relative_to(directory))
        for item in directory.iterdir()
    )

@mcp.tool()
def search_files(path: str, query: str) -> str:
    """Search files recursively for a text query."""
    root = Path(path)

    if not root.is_dir():
        raise ValueError(f"Not a directory: {path}")

    matches = []

    for file in root.rglob("*"):
        if not file.is_file():
            continue

        try:
            text = file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        if query.lower() in text.lower():
            matches.append(str(file))

    return "\n".join(matches)

@mcp.tool()
def write_file(path: str, content: str) -> str:
    """Write content to a file."""
    file = Path(path)

    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding="utf-8")

    return f"Successfully wrote {file}"

@mcp.tool()
def create_directory(path: str) -> str:
    """Create a directory and any missing parent directories."""

    directory = Path(path)

    directory.mkdir(parents=True, exist_ok=True)

    return f"Directory created: {directory}"

if __name__=="__main__":
    mcp.run(transport="stdio")