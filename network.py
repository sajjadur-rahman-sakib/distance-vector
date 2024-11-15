import threading

class Network:
    def __init__(self):
        self.routers = {}

    def add_router(self, router):
        self.routers[router.name] = router

    def send_to_router(self, destination, source, distance_vector):
        if destination in self.routers:
            self.routers[destination].receive_distance_vector(source, distance_vector)

    def simulate(self):
        """Simulate periodic updates."""
        for router in self.routers.values():
            threading.Thread(target=router.send_distance_vector, args=(self,)).start()

    def dynamic_link_change(self, router1, router2, cost):
        """Dynamically change the link cost."""
        if router1 in self.routers and router2 in self.routers:
            self.routers[router1].neighbors[router2] = cost
            self.routers[router2].neighbors[router1] = cost
