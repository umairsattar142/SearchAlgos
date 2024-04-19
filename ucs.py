class Graph_ucs:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = {}
            self.graph[node2][node1] = weight

    def uniform_cost_search(self, start, goals):
        visited = []
        que = [(0, start, [])]
        newCost = 0
        while que:
            que.sort()
            print(que)
            (cost, node, path) = que.pop(0)  # pop from start
            if node in goals:
                return path + [node], cost
            for neighbour in self.graph[node]:
                newCost = cost + self.graph[node][neighbour]
                if neighbour not in visited:
                    visited.append(node)
                    que.append((newCost, neighbour, path + [node]))

        return [], None


    def print_path(path, new_cost):
        print(' -> '.join(path))
        print(f'Cost = {new_cost}')