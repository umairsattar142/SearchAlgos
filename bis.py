class Graph_bis:
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

    def bidirectional_search(self, start, goal):
        forward_visited = {start: 0}
        backward_visited = {goal: 0}
        forward_queue = [(0, start, [])]
        backward_queue = [(0, goal, [])]

        common_node = None
        min_cost = float('inf')

        while forward_queue and backward_queue:
            forward_queue.sort()
            backward_queue.sort()

            forward_cost, forward_node, forward_path = forward_queue.pop(0)
            backward_cost, backward_node, backward_path = backward_queue.pop(0)

            if forward_node in backward_visited:
                cost = forward_cost + backward_visited[forward_node]
                if cost < min_cost:
                    min_cost = cost
                    common_node = forward_node
                    forward_path = forward_path + backward_path[::-1]

            if backward_node in forward_visited:
                cost = backward_cost + forward_visited[backward_node]
                if cost < min_cost:
                    min_cost = cost
                    common_node = backward_node
                    forward_path = forward_path + backward_path[::-1]

            if common_node is not None:
                path = forward_path
                return path , common_node

            for next_node, weight in self.graph[forward_node].items():
                new_cost = forward_cost + weight
                if next_node not in forward_visited or new_cost < forward_visited[next_node]:
                    forward_visited[next_node] = new_cost
                    forward_queue.append((new_cost, next_node, forward_path + [forward_node]))

            for next_node, weight in self.graph[backward_node].items():
                new_cost = backward_cost + weight
                if next_node not in backward_visited or new_cost < backward_visited[next_node]:
                    backward_visited[next_node] = new_cost
                    backward_queue.append((new_cost, next_node, backward_path + [backward_node]))

        return [], None


    def print_path(path):
        print(' -> '.join(path))