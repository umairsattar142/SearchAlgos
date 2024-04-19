import random
import math

class Graph_simulatedAnnealing:
    def __init__(self,directed):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.edges:
            self.edges[node1] = []
        self.edges[node1].append((node2, weight))
        if node2 not in self.edges:
            self.edges[node2] = []
        self.edges[node2].append((node1, weight))

    def simulated_annealing_search(self, start, goal, initial_temperature=1000, cooling_factor=0.99, max_iterations=10000):
        current_node = start
        current_cost = 0
        current_path = [start]
        temperature = initial_temperature

        for i in range(max_iterations):
            if current_node in goal:
                return current_path, current_cost

            neighbors = []
            for successor, edge_cost in self.edges[current_node]:
                if successor not in current_path:
                    neighbors.append((successor, edge_cost))

            if not neighbors:
                return None, None

            random_neighbor, neighbor_cost = random.choice(neighbors)
            delta_cost = neighbor_cost - current_cost

            if delta_cost < 0 or math.exp(-delta_cost/temperature) > random.random():
                current_node = random_neighbor
                current_cost += neighbor_cost
                current_path.append(current_node)

            temperature *= cooling_factor

        return None, None

    def print_path( path, cost):
        if path is None:
            print("No path found")
        else:
            print("Path found:")
            print(" -> ".join(path))
            print("Total cost:", cost)