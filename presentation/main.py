import random
import networkx as nx
import networkx.algorithms.community as nx_comm
import matplotlib.pyplot as plt


ns = 100
p = 0.3

G = nx.connected_caveman_graph(5, 5)

for edge in G.edges():
    if random.random() <= p:
        u, v = edge
        new_v = -1
        new_v = random.choice(list(G.nodes()))
        while u == new_v:
            new_v = random.choice(list(G.nodes()))

        G.add_edge(u, new_v)

comms = nx_comm.louvain_communities(G, seed=1231414)

pos = nx.spring_layout(G, k=0.1, seed=1002931257)

nx.draw(G, node_color="black", node_size=ns, pos=pos)
plt.savefig("no_comms.png")

colours = ["red", "blue", "yellow", "green", "aquamarine", "orange", "pink", "plum", "purple", "black", "white"]

for i, comm in enumerate(comms):
    nx.draw_networkx_nodes(G, pos, node_size=ns, nodelist=comm, node_color=colours[i])

plt.savefig("comms.png")
