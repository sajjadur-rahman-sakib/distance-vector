import networkx as nx
import matplotlib.pyplot as plt

class NetworkVisualizer:
    def __init__(self, network):
        self.network = network
        self.graph = nx.Graph()

    def build_graph(self):
        for node_name, node in self.network.nodes.items():
            self.graph.add_node(node_name)
            for neighbor, cost in node.neighbors.items():
                self.graph.add_edge(node_name, neighbor, weight=cost)

    def draw_graph(self, routing_tables=None):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph) 

        nx.draw(self.graph, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight="bold")
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        if routing_tables:
            for node, table in routing_tables.items():
                table_text = "\n".join([f"{dest}: {next_hop}, {cost}" for dest, (next_hop, cost) in table.items()])
                plt.text(pos[node][0], pos[node][1] - 0.1, table_text, fontsize=8, ha="center", bbox=dict(facecolor="white", alpha=0.7))

        plt.title("Network Visualization with Distance Vector Routing")
        plt.show()

    def update_and_draw(self):
        self.build_graph()
        routing_tables = {node_name: node.get_table() for node_name, node in self.network.nodes.items()}
        self.draw_graph(routing_tables)
