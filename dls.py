class Graph_dls:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed
        self.goal = ""

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append((node2, weight))

        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append((node1, weight))

    def depth_limited_search(self, current_node, goal_node, limit):
        if current_node in goal_node:
            self.goal = goal_node
            return [current_node]

        if limit <= 0:
            return []

        for next_node, weight in self.graph[current_node]:
            path = self.depth_limited_search(next_node, goal_node, limit-1)
            if path:
                return [current_node] + path

        return []

    @staticmethod
    def print_path(path, goal):
        print('->'.join(path), '->', goal)

