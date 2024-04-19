from collections import deque

class Graph_bfs:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if not self.directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)

    def breadth_first_search(self, start, goals):
        visited = set()
        queue = deque([(start, [])])
        while queue:
            node, path = queue.popleft()
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return path + [node], node
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [node]))
        return [], None

    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
