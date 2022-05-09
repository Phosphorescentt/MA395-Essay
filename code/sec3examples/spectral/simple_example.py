import networkx as nx
import matplotlib.pyplot as plt

# G = nx.read_edgelist("simple_example.edges")

# pos = {1: (0, 0),
#        2: (100, 100),
#        3: (100, -100),
#        4: (0, 200),
#        5: (0, 300)}

G = nx.Graph()

G.add_node(1, pos=(0, 0))
G.add_node(2, pos=(1, 1))
G.add_node(3, pos=(1, -1))
G.add_node(4, pos=(2, 0))
G.add_node(5, pos=(3, 0))
G.add_node(6, pos=(4, 1))
G.add_node(7, pos=(4, -1))
G.add_node(8, pos=(5, 0))

G.add_edge(1, 2, color="black", style="solid")
G.add_edge(1, 3, color="black", style="solid")
G.add_edge(2, 4, color="black", style="solid")
G.add_edge(3, 4, color="black", style="solid")
G.add_edge(4, 5, color="red", style="dashed")
G.add_edge(5, 6, color="black", style="solid")
G.add_edge(5, 7, color="black", style="solid")
G.add_edge(6, 8, color="black", style="solid")
G.add_edge(7, 8, color="black", style="solid")

pos = nx.get_node_attributes(G, "pos")

edges = G.edges()
colours = [G[u][v]["color"] for u, v in edges]
styles = [G[u][v]["style"] for u, v in edges]

nx.draw(G, pos, width=5, edge_color=colours, style=styles, node_color="#000000", node_size=500)

ax = plt.gca()
ax.collections[0].set_edgecolor("#000000")

plt.savefig("simple_example.png")
