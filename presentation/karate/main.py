import networkx as nx
import networkx.algorithms.community as nx_comms
import matplotlib.pyplot as plt


def draw_save_graph_communities(G, algo):
    ns = 100
    colours = [
        "red",
        "blue",
        "yellow",
        "green",
        "aquamarine",
        "orange",
        "pink",
        "plum",
        "purple",
        "black",
        "white",
    ]
    pos = nx.spring_layout(G, k=0.1, seed=1002931257)
    comms = algo(G)

    nx.draw(G, node_size=ns, pos=pos)
    for i, comm in enumerate(comms):
        nx.draw_networkx_nodes(
            G, pos, node_size=ns, nodelist=comm, node_color=colours[i]
        )

    plt.savefig(f"{algo.__name__}.png")


G = nx.karate_club_graph()

draw_save_graph_communities(G, nx_comms.louvain_communities)
draw_save_graph_communities(G, nx_comms.kernighan_lin_bisection)
draw_save_graph_communities(G, nx_comms.greedy_modularity_communities)
