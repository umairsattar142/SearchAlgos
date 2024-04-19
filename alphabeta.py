class Node:
    def __init__(self, state, value=None):
        self.state = state
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def terminal(self):
        if len(self.children) == 0:
            return True
        return False

class Graph_minmax:
    def __init__(self, root_state):
        self.root = Node(root_state)
        self.visited=[]


    def add_node(self, parent, child, value=None):
        parent_node = self.search_node(parent, self.root)
        if parent_node:
            child_node = Node(child, value)
            parent_node.add_child(child_node)

    def search_node(self, state, node):
        if node.state == state:
            return node
        for child in node.children:
            found = self.search_node(state, child)
            if found:
                return found
        return None

    def alpha_beta(self, node, max_player, a=float("-inf"), b=float("+inf")):
        if node.terminal():
            return node.value, [node.state]

        if max_player:
            val = float("-inf")
        else:
            val = float("+inf")

        if node == self.root:
            self.visited.append(node.state)

        best_path = []

        for c in node.children:
            self.visited.append(c.state)
            s, path = self.alpha_beta(c, not max_player, a, b)
            path = [node.state] + path

            if max_player:
                if s is not None:
                    val = max(val, s)
                else:
                    s = val
                a = max(a, s)
            else:
                if s is not None:
                    val = min(val, s)
                else:
                    s = val
                b = min(b, s)

            if a >= b:
                break

            if s == val:
                best_path = path

        return val, best_path

    def print_path(self, path):
        print("Path: ", end=" ")
        for i in range(len(path)):
            if i + 1 != len(path):
                print(path[i], '-->', end=" ")
            else:
                print(path[i], end=" ")
