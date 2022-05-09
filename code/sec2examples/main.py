import networkx as nx
import matplotlib.pyplot as plt

# n = 50
# p = 0.055
#
# G1 = nx.erdos_renyi_graph(n, p)
#
# nx.draw_spring(G1, node_size=50, node_color="#000000")
# plt.savefig("high_prob.png")

G1 = nx.complete_graph(5)
G2 = nx.path_graph(5)

nx.draw_spring(G1, node_size=150, node_color="#000000")
plt.savefig("complete.png")

plt.cla()

nx.draw_spring(G2, node_size=150, node_color="#000000")
plt.savefig("path.png")
