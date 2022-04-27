import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("out.ucidata-zachary")

degrees = [G.degree(n) for n in G.nodes()]

plt.hist(degrees, color="white", edgecolor="black", align="mid", cumulative=-1)
plt.xlabel("k")
plt.ylabel("p(k)")
plt.savefig("zachary_degree_hist.png")
