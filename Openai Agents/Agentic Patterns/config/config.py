import os
from tkinter import Image
from dotenv import load_dotenv
from agents import set_default_openai_key, set_tracing_disabled
from agents.extensions.visualization import draw_graph

load_dotenv()

# Set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
set_default_openai_key(openai_api_key)


# Disable tracing
set_tracing_disabled(True)

def draw_graph(agent, filename):
    try:
        # Try to use the graph visualization 
        draw_graph(agent, filename)
        # Comment out the line causing the error
        # display(Image(triage_agent.draw_mermaid_png()))
    except Exception as e:
        print("Graphviz visualization failed. Error:", e)

