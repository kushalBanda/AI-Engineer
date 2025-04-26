#!/usr/bin/env python3
"""
Simple script to run the MCP calculator client directly.
"""
import asyncio
from src.calculator.client import interactive_client

if __name__ == "__main__":
    asyncio.run(interactive_client()) 