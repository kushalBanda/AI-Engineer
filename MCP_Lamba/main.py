from fastmcp import FastMCP

mcp = FastMCP("Hello World")

@mcp.tool
def say_hello(name: str = "World") -> str:
    """Returns a greeting."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
