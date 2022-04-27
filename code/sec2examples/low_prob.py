import networkx as nx
import matplotlib.pyplot as plt

n = 50
p = 0.01

G2 = nx.erdos_renyi_graph(n, p)

nx.draw_spring(G2, node_size=50, node_color="#000000")
plt.savefig("low_prob.png")
