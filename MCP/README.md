# MCP Calculator

A simple calculator service built using the Model Context Protocol (MCP).

## Features

This project demonstrates:

- A basic MCP server with multiple tools:
  - `add`: Adds two numbers together
  - `subtract`: Subtracts the second number from the first
  - `multiply`: Multiplies two numbers together
  - `divide`: Divides the first number by the second
  - `power`: Raises a base number to a power

- A simple interactive client that connects to the server

## Setup

### Prerequisites

- Python 3.9 or higher
- `uv` package manager (recommended)

### Installation

1. Clone this repository:
   ```
   git clone [repository-url]
   cd mcp-calculator
   ```

2. Set up a virtual environment and install dependencies:
   
   Using `uv`:
   ```
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

   Using `pip`:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

## Usage

### Running the Server

Quick method:
```
./run_server.py
```

Alternative method:
```
python -m calculator.server
```

This will start the MCP calculator server on the default port (8080).

### Using the Interactive Client

Quick method:
```
./run_client.py
```

Alternative method:
```
python -m calculator.client
```

Follow the on-screen prompts to interact with the calculator:

```
MCP Calculator Client
====================
Available operations: add, subtract, multiply, divide, power
Type 'exit' to quit

Operation: add
First number: 5
Second number: 3
Result: 8
```

### Connecting to Claude Desktop

1. Start the calculator server
2. Open Claude Desktop
3. Look for the "Connected Apps" section
4. Your calculator should appear in the available servers
5. Connect to it and start using the calculator tools in your conversation

## Project Structure

```
mcp-calculator/
├── README.md
├── pyproject.toml
├── run_server.py
├── run_client.py
└── src/
    └── calculator/
        ├── __init__.py
        ├── server.py
        └── client.py
```

## License

MIT 