import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("out.ucidata-zachary")

# pos = nx.spring_layout(G, k=0.001)

nx.draw_spring(G, node_size=50, node_color="#000000")
plt.savefig("zachary_spring.png")

nx.draw_circular(G, node_size=50, node_color="#000000")
plt.savefig("zachary_circle.png")
