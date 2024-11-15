from router import Router
from network import Network
from visualizer import visualize_topology

def main():
    network = Network()

    r1 = Router("A", {"B": 1, "C": 4})
    r2 = Router("B", {"A": 1, "C": 2, "D": 7})
    r3 = Router("C", {"A": 4, "B": 2, "D": 3})
    r4 = Router("D", {"B": 7, "C": 3})

    for router in [r1, r2, r3, r4]:
        network.add_router(router)

    print("Initial Network Topology:")
    visualize_topology(network)

    print("Simulating distance vector updates...")
    for _ in range(5):
        network.simulate()

    print("Changing link cost between A and C...")
    network.dynamic_link_change("A", "C", 2)
    visualize_topology(network)

if __name__ == "__main__":
    main()
