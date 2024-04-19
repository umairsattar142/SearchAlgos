from queue import PriorityQueue

class Graph_bestFirstSearch:
    def __init__(self, directed):
        self.graph = {}
        self.H = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = {}
            self.graph[node2][node1] = weight

    def set_heuristic_dict(self, heuristic):
        self.H = heuristic

    def best_first_search(self, start, goals):
        visited = []
        que = [(self.H[start], 0, start, [])]
        visited.append(start)
        Cost = {start: 0}
        while que:
            que.sort()
            print(que)
            cost, notH, node, path = que.pop(0)
            if node in goals:
                return path + [node], notH
            for neighbour in self.graph[node]:
                newCost = Cost[node] + self.graph[node][neighbour]
                if neighbour not in visited:
                    Cost[neighbour] = newCost
                    visited.append(neighbour)
                    que.append((self.H[neighbour], newCost, neighbour, path + [node]))
        return [], None



    def print_path(self,path, cost):
        if path is None:
            print("No path found")
        else:
            print("Path found:")
            print(" -> ".join(path))
            print("Total cost:", cost)
