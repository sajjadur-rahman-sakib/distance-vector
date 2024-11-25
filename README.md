# Distance Vector Routing Algorithm Simulator

## Overview

This project demonstrates the implementation of a **Distance Vector Routing Algorithm**, a fundamental concept in computer networking. The simulation involves routers exchanging routing tables periodically to calculate the shortest paths to various destinations within a dynamic network topology.

---

## Features

- **Dynamic Routing Updates**: Simulates periodic updates of routing tables based on the distance vector protocol.
- **Shortest Path Calculation**: Determines the shortest paths between nodes in the network.
- **Interactive Visualization**: Provides a graphical representation of the network topology and routing table updates.
- **Customizable Network**: Allows users to modify the network topology and observe its effects in real-time.

---

## Technologies Used

- **Python**: Core language for implementing the algorithm.
- **Matplotlib/NetworkX**: For visualizing the network topology and routing table updates.
- **Flask**: For creating a simple web interface (optional).

---

## How It Works

1. **Initialization**:

   - Define a set of routers and their connections (graph representation).
   - Assign initial costs (distances) between directly connected routers.

2. **Distance Vector Updates**:

   - Each router maintains a routing table with distances to all other routers.
   - Periodically, routers exchange their routing tables and update distances based on the Bellman-Ford algorithm.

3. **Dynamic Topology Simulation**:

   - Modify the network (e.g., add/remove routers or links) to simulate dynamic changes.
   - Observe how routers adapt to new topologies.

4. **Visualization**:
   - Display the network graph with nodes (routers) and edges (connections).
   - Show routing table updates visually or in tabular format.

---

## Getting Started

### Prerequisites

- **Python 3.x**
- Install the following libraries:
  ```bash
  pip install matplotlib networkx flask
  ```

---

## Authors

- Md. Sajjadur Rahman

---
