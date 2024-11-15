import threading

class Router:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors 
        self.routing_table = {name: 0} 
        self.lock = threading.Lock()
    
    def send_distance_vector(self, network):
        """Send distance vector to neighbors."""
        distance_vector = self.routing_table.copy()
        for neighbor in self.neighbors:
            network.send_to_router(neighbor, self.name, distance_vector)
    
    def receive_distance_vector(self, source, vector):
        """Receive a distance vector from a neighbor."""
        with self.lock:
            updated = False
            for dest, cost in vector.items():
                new_cost = self.neighbors[source] + cost
                if dest not in self.routing_table or new_cost < self.routing_table[dest]:
                    self.routing_table[dest] = new_cost
                    updated = True
            return updated
