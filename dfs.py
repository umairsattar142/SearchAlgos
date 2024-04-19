class Graph_dfs:
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

    def depth_first_search(self, start, goals):
        visited = set()
        stack = [(start, [])]
        while stack:
            node, path = stack.pop()
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return path + [node], node
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [node]))
        return [], None


    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
