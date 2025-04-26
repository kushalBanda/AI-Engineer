import asyncio
import logging
import sys
from typing import List, Dict, Any

from mcp import Server, ServerBuilder, Tool, ToolParameter, ToolCallContext

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Define our tools
add_tool = Tool(
    name="add",
    description="Adds two numbers together",
    parameters=[
        ToolParameter(
            name="a",
            description="First number",
            type="number",
            required=True,
        ),
        ToolParameter(
            name="b",
            description="Second number",
            type="number",
            required=True,
        ),
    ],
    handler=lambda context, a, b: a + b,
)

subtract_tool = Tool(
    name="subtract",
    description="Subtracts the second number from the first",
    parameters=[
        ToolParameter(
            name="a",
            description="First number",
            type="number",
            required=True,
        ),
        ToolParameter(
            name="b",
            description="Second number",
            type="number",
            required=True,
        ),
    ],
    handler=lambda context, a, b: a - b,
)

multiply_tool = Tool(
    name="multiply",
    description="Multiplies two numbers together",
    parameters=[
        ToolParameter(
            name="a",
            description="First number",
            type="number",
            required=True,
        ),
        ToolParameter(
            name="b",
            description="Second number",
            type="number",
            required=True,
        ),
    ],
    handler=lambda context, a, b: a * b,
)

divide_tool = Tool(
    name="divide",
    description="Divides the first number by the second",
    parameters=[
        ToolParameter(
            name="a",
            description="First number (dividend)",
            type="number",
            required=True,
        ),
        ToolParameter(
            name="b",
            description="Second number (divisor)",
            type="number",
            required=True,
        ),
    ],
    handler=lambda context, a, b: a / b if b != 0 else "Error: Division by zero",
)

power_tool = Tool(
    name="power",
    description="Raises the first number to the power of the second",
    parameters=[
        ToolParameter(
            name="base",
            description="The base number",
            type="number",
            required=True,
        ),
        ToolParameter(
            name="exponent",
            description="The exponent",
            type="number",
            required=True,
        ),
    ],
    handler=lambda context, base, exponent: base ** exponent,
)

async def main():
    """Start the MCP calculator server."""
    logger.info("Starting MCP Calculator Server")
    
    # Create the server
    server = ServerBuilder.create_server(
        name="calculator",
        description="A simple calculator service with basic math operations",
        version="0.1.0"
    )
    
    # Register our tools
    server.register_tool(add_tool)
    server.register_tool(subtract_tool)
    server.register_tool(multiply_tool)
    server.register_tool(divide_tool)
    server.register_tool(power_tool)
    
    # Start the server
    await server.start()
    
    try:
        # Keep the server running until interrupted
        await asyncio.Future()
    except KeyboardInterrupt:
        logger.info("Shutting down server...")
    finally:
        await server.stop()
        logger.info("Server stopped")

if __name__ == "__main__":
    asyncio.run(main())
