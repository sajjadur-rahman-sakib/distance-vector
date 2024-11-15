import networkx as nx
import matplotlib.pyplot as plt

def visualize_topology(network):
    G = nx.Graph()
    for router in network.routers.values():
        for neighbor, cost in router.neighbors.items():
            G.add_edge(router.name, neighbor, weight=cost)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
