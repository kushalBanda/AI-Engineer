from agents import build_graph
from IPython.display import Image, display

try:
    graph = build_graph()
    display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
except Exception:
    pass
