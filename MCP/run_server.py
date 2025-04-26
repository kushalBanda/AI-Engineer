#!/usr/bin/env python3
"""
Simple script to run the MCP calculator server directly.
"""
import asyncio
from src.calculator.server import main

if __name__ == "__main__":
    asyncio.run(main()) 