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
G.add_node(2, pos=(50, 50))
G.add_node(3, pos=(50, -50))
G.add_node(4, pos=(100, 0))
G.add_node(5, pos=(150, 0))

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(4, 5)

pos = nx.get_node_attributes(G, "pos")

nx.draw(G, pos, node_color="#ffffff", node_size=500, with_labels=True)

ax = plt.gca()
ax.collections[0].set_edgecolor("#000000")

plt.savefig("simple_example.png")
