import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("out2.topology")

nx.draw_spring(G, node_size=10, node_color="#000000")
plt.savefig("topology.png")
