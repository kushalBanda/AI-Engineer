import asyncio
import json
import logging
import sys
from typing import Dict, Any

import httpx

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

class CalculatorClient:
    def __init__(self, server_url: str = "http://localhost:8880"):
        self.server_url = server_url
        self.client = httpx.AsyncClient()
    
    async def close(self):
        await self.client.aclose()
    
    async def call_tool(self, tool_name: str, params: Dict[str, Any]) -> Any:
        """Call a tool on the calculator server."""
        url = f"{self.server_url}/tools/{tool_name}"
        
        try:
            logger.info(f"Calling tool {tool_name} with params {params}")
            response = await self.client.post(url, json=params)
            response.raise_for_status()
            result = response.json()
            logger.info(f"Result: {result}")
            return result.get("result")
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e}")
            return f"Error: {e}"
        except httpx.RequestError as e:
            logger.error(f"Request error occurred: {e}")
            return f"Error: {e}"
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return f"Error: {e}"

async def interactive_client():
    """Start an interactive client session."""
    client = CalculatorClient()
    
    try:
        print("MCP Calculator Client")
        print("====================")
        print("Available operations: add, subtract, multiply, divide, power")
        print("Type 'exit' to quit")
        print()
        
        while True:
            operation = input("Operation: ").strip().lower()
            if operation == "exit":
                break
            
            if operation not in ["add", "subtract", "multiply", "divide", "power"]:
                print("Invalid operation. Try again.")
                continue
            
            if operation == "power":
                base = float(input("Base: "))
                exponent = float(input("Exponent: "))
                params = {"base": base, "exponent": exponent}
            else:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                params = {"a": a, "b": b}
            
            result = await client.call_tool(operation, params)
            print(f"Result: {result}")
            print()
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        await client.close()

def main():
    """Entry point for the client application."""
    asyncio.run(interactive_client())

if __name__ == "__main__":
    main()
