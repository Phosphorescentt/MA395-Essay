import networkx as nx
import matplotlib.pyplot as plt

from networkx.algorithms import bipartite

G = nx.read_edgelist("out.opsahl-southernwomen")

print(nx.is_bipartite(G))

# Not really sure how to do bipartite stuffself.
# Once it's done I'll just make a diagram of the network
# and throw it in - there's a \missingfigure already there.

nx.draw_spring(G, node_size=50, node_color="#000000")
plt.savefig("southernwomen_spring.png")
