class Graph_ids:
    def __init__(self, directed=True):
        self.graph = {}
        self.visited = []
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def depth_limited_search(self, start, goal, depth_limit):
        self.visited.append(start)
        if start in goal:
            return [start]
        if depth_limit <= 0:
            return None
        for neighbor in self.graph[start]:
            if neighbor not in self.visited:
                path = self.depth_limited_search(neighbor, goal, depth_limit + 1)
                if path is not None:
                    return [start] + path
        return None

    def iterative_deepening_search(self, start, goal):
        for depth_limit in range(0, len(self.graph)):
            print("in ids")
            self.visited = []
            path = self.depth_limited_search(start, goal, 0)
            if path is not None:
                print("path haii")
                self.print_path(path, goal)
                return path, goal
            else:
                print("oyee nai hai")
        return None, None


    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
