import networkx as nx
import networkx.algorithms.community as nx_comm
import matplotlib.pyplot as plt


ns = 200

G = nx.read_edgelist("out.ucidata-zachary")
comms = nx_comm.kernighan_lin_bisection(G, seed=1231414)

pos = nx.spring_layout(G, seed=1002931257)

nx.draw(G, node_color="black", node_size=ns, pos=pos)
plt.savefig("zachary_no_comm.png")

nx.draw_networkx_nodes(G, pos, node_size=ns, nodelist=comms[0], node_color="tab:red")
nx.draw_networkx_nodes(G, pos, node_size=ns, nodelist=comms[1], node_color="tab:blue")

plt.savefig("zachary_comm.png")
