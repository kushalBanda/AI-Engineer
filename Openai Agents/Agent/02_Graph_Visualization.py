from tkinter import Image
from agents import Agent, Runner
from agents.extensions.visualization import draw_graph


import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


agent = Agent(
    name="Math Tutor",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)


history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent]
)

try:
    # Try to use the graph visualization 
    draw_graph(triage_agent, filename="agent_graph.png")
    # Comment out the line causing the error
    # display(Image(triage_agent.draw_mermaid_png()))
except Exception as e:
    print("Graphviz visualization failed. Error:", e)


