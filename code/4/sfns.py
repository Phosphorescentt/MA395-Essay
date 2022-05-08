import random
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
N = 100
M = 3
m0 = 3
alpha = 0.01

communities = [[], [], []]

""" Initialisation """
for i in range(M):
    G.add_node(i*3 + 0)
    G.add_node(i*3 + 1)
    G.add_node(i*3 + 2)

    G.add_edge(i*3 + 0, i*3 + 1)
    G.add_edge(i*3 + 1, i*3 + 2)
    G.add_edge(i*3 + 2, i*3 + 0)

    communities[i].append(i*3 + 0)
    communities[i].append(i*3 + 1)
    communities[i].append(i*3 + 3)


""" Growth """
for i in range(M, N+M):
    c_no = random.randint(0, 2)
    communities[c_no].append(i)
    G.add_node(i)

    deg = random.randint(1, m0)
    for j in range(deg):
        # pick a random node
        v = random.choice(communities[c_no])
        G.add_edge(i, v)

nx.draw(G)
plt.savefig("a.png")
