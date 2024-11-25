import math

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}
        self.neighbors = {}

    def initialize_table(self, all_nodes):
        for node in all_nodes:
            if node == self.name:
                self.routing_table[node] = (self.name, 0)  
            elif node in self.neighbors:
                self.routing_table[node] = (node, self.neighbors[node])  
            else:
                self.routing_table[node] = (None, math.inf) 

    def update_table(self, neighbor, neighbor_table):
        updated = False
        for dest, (next_hop, cost_to_dest) in neighbor_table.items():
            if dest == self.name: 
                continue
            new_cost = self.neighbors[neighbor] + cost_to_dest
            if new_cost < self.routing_table[dest][1]: 
                self.routing_table[dest] = (neighbor, new_cost)
                updated = True
        return updated

    def get_table(self):
        return self.routing_table


class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = Node(name)

    def add_link(self, node1, node2, cost):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].neighbors[node2] = cost
            self.nodes[node2].neighbors[node1] = cost

    def initialize_routing(self):
        all_nodes = self.nodes.keys()
        for node in self.nodes.values():
            node.initialize_table(all_nodes)

    def run_distance_vector(self, iterations=10):
        for _ in range(iterations):
            updates = False
            for node in self.nodes.values():
                for neighbor in node.neighbors:
                    updates |= node.update_table(neighbor, self.nodes[neighbor].get_table())
            if not updates:
                break  

    def display_routing_tables(self):
        for node_name, node in self.nodes.items():
            print(f"Routing table for {node_name}:")
            for dest, (next_hop, cost) in node.get_table().items():
                print(f"  {dest} -> Next hop: {next_hop}, Cost: {cost}")
            print()
