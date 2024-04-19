import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.widgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
from bfs import Graph_bfs
from dfs import Graph_dfs
from astar import Graph_astar
from ids import Graph_ids
from dls import Graph_dls
from ucs import Graph_ucs
from bis import Graph_bis
from bestfirstsearch import Graph_bestFirstSearch
from simulatedannealing import Graph_simulatedAnnealing
from alphabeta import Graph_minmax

DG = nx.DiGraph()
G = nx.Graph()
Node1_arr=['A']*30
Node2_arr=['A']*30
Goal_list = []


class Ui_AISearchingTechniquesMainWindow(object):
    counter = 0
    counterG = 0
    EdgeWeight_arr = [1] * 30
    HeuristicDict = dict()
    H = {}
    graphastar = Graph_astar(directed=False)
    graphastarD = Graph_astar(directed=True)

    def GeneratePathClicked(self):
        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('../test.txt', 'w') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            searchType = str(self.SearchTypecomboBox.currentText())
            graphType = str(self.GraphTypecomboBox.currentText())
            if (graphType == "Undirectd Graph"):
                if searchType == "BFS":
                    print("BFS")
                    graphbfs = Graph_bfs(directed=False)
                    graphbfs.add_edge("s", "a")
                    graphbfs.add_edge("s", "b")
                    graphbfs.add_edge("a", "c")
                    graphbfs.add_edge("a", "d")
                    graphbfs.add_edge("b", "d")
                    graphbfs.add_edge("b", "g")
                    graphbfs.add_edge("d", "c")
                    graphbfs.add_edge("d", "g")
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    for i in range(0,self.counter):
                        graphbfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    print(goals)
                    traced_path1, goal = graphbfs.breadth_first_search(start, goals)
                    if (traced_path1):
                        print('Path:', end=' ')
                        Graph_bfs.print_path(traced_path1, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path1) - 1):
                            G_traced.add_edge(traced_path1[i], traced_path1[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(directed=False)
                    graphdfs.add_edge("s", "a")
                    graphdfs.add_edge("s", "b")
                    graphdfs.add_edge("a", "c")
                    graphdfs.add_edge("a", "d")
                    graphdfs.add_edge("b", "d")
                    graphdfs.add_edge("b", "g")
                    graphdfs.add_edge("d", "c")
                    graphdfs.add_edge("d", "g")
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    for i in range(0, self.counter):
                        graphdfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2, goal = graphdfs.depth_first_search(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        Graph_dfs.print_path(traced_path2, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path2) - 1):
                            G_traced.add_edge(traced_path2[i], traced_path2[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))
                        plt.show()
                        print()

                elif searchType == "A*":
                    self.graphastar.add_edge("s", "a",2)
                    self.graphastar.add_edge("s", "b",5)
                    self.graphastar.add_edge("a", "c",2)
                    self.graphastar.add_edge("a", "d",4)
                    self.graphastar.add_edge("b", "d",1)
                    self.graphastar.add_edge("b", "g",5)
                    self.graphastar.add_edge("d", "c",3)
                    self.graphastar.add_edge("d", "g",2)
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    astarh = {"s":0,"a":2,"b":3,"c":1,"d":1,"g":0}
                    self.graphastar.set_huristics(astarh)
                    for i in range(0, self.counter):
                        self.graphastar.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path5, cost3 = self.graphastar.a_star_search(start, goals)
                    if (traced_path5):
                        print('Path:', end=' ')
                        Graph_astar.print_path(traced_path5)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path5) - 1):
                            G_traced.add_edge(traced_path5[i], traced_path5[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print('\nCost:', cost3)

                elif searchType == "IDS":
                    graphids = Graph_ids(directed=False)
                    for i in range(0, self.counter):
                        graphids.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    print(start, goals)
                    traced_path3, goal = graphids.iterative_deepening_search(start, goals[0])

                    print("hi", traced_path3)
                    if (traced_path3):
                        print("hi2")
                        print('Path:', end=' ')
                        Graph_ids.print_path(traced_path3, goal)
                        print()

                elif searchType == "DLS":
                    print("hi dls")
                    graphdls = Graph_dls(directed=False)
                    for i in range(0, self.counter):
                        graphdls.add_edge(Node1_arr[i], Node2_arr[i], self.EdgeWeight_arr[i])
                    start = self.StartNode_input.text()
                    print("Start:",start)
                    goals = Goal_list
                    print("goal:",goals)
                    depth_limit = self.DepthLimitPushed()
                    # print(type(depth_limit))
                    traced_path4 = graphdls.depth_limited_search(start, goals, depth_limit)

                    if traced_path4:
                        print('Path:', end=' ')
                        Graph_dls.print_path(traced_path4, goals)
                        print()
                    else:
                        print(f"No path found within depth limit of {depth_limit}")

                elif searchType == "UCS":
                    graphucs = Graph_ucs(directed=False)
                    graphucs.add_edge("s", "a",2)
                    graphucs.add_edge("s", "b",5)
                    graphucs.add_edge("a", "c",2)
                    graphucs.add_edge("a", "d",4)
                    graphucs.add_edge("b", "d",1)
                    graphucs.add_edge("b", "g",5)
                    graphucs.add_edge("d", "c",3)
                    graphucs.add_edge("d", "g",2)
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    for i in range(0, self.counter):
                        graphucs.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goal = Goal_list
                    print("goal:",goal)
                    traced_path4 , cost = graphucs.uniform_cost_search(start, goal)
                    Goal_list.clear()
                    if traced_path4:
                        print('Path:', end=' ')
                        Graph_ucs.print_path(traced_path4, cost)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path4) - 1):
                            G_traced.add_edge(traced_path4[i], traced_path4[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()
                elif searchType == "Best First":
                    graphbestfirst = Graph_bestFirstSearch(directed=False)
                    graphbestfirst.add_edge("s", "a",2)
                    graphbestfirst.add_edge("s", "b",5)
                    graphbestfirst.add_edge("a", "c",2)
                    graphbestfirst.add_edge("a", "d",4)
                    graphbestfirst.add_edge("b", "d",1)
                    graphbestfirst.add_edge("b", "g",5)
                    graphbestfirst.add_edge("d", "c",3)
                    graphbestfirst.add_edge("d", "g",2)
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    bestfsh = {"s": 10, "a": 2, "b": 3, "c": 1, "d": 4, "g": 0}
                    graphbestfirst.set_heuristic_dict(bestfsh)
                    for i in range(0, self.counter):
                        graphbestfirst.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goal = Goal_list
                    print("goal:",goal)
                    traced_path4 , cost = graphbestfirst.best_first_search(start, goal)
                    Goal_list.clear()
                    if traced_path4:
                        print('Path:', end=' ')
                        Graph_ucs.print_path(traced_path4, cost)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path4) - 1):
                            G_traced.add_edge(traced_path4[i], traced_path4[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()
                elif searchType == "Bidirectional":
                    graphbis = Graph_bis(directed=False)
                    graphbis.add_edge("s", "a", 2)
                    graphbis.add_edge("s", "b", 5)
                    graphbis.add_edge("a", "c", 2)
                    graphbis.add_edge("a", "d", 4)
                    graphbis.add_edge("b", "d", 1)
                    graphbis.add_edge("b", "g", 5)
                    graphbis.add_edge("d", "c", 3)
                    graphbis.add_edge("d", "g", 2)
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    for i in range(0, self.counter):
                        graphbis.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goal = Goal_list
                    traced_path4, commonNode = graphbis.bidirectional_search(start, goal[0])

                    if traced_path4:
                        print("Common Node:", commonNode)
                        print('Path:', end=' ')
                        Graph_bis.print_path(traced_path4)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path4) - 1):
                            G_traced.add_edge(traced_path4[i], traced_path4[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()
                elif searchType == "Alpha-beta Pruning":
                    start = self.StartNode_input.text()
                    graphMinmax = Graph_minmax(start)
                    graphMinmax.add_node("s", "a", 2)
                    graphMinmax.add_node("s", "b", 5)
                    graphMinmax.add_node("a", "c", 2)
                    graphMinmax.add_node("a", "d", 4)
                    graphMinmax.add_node("b", "d", 1)
                    graphMinmax.add_node("b", "g", 5)
                    graphMinmax.add_node("d", "c", 3)
                    graphMinmax.add_node("d", "g", 2)
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    for i in range(0, self.counter):
                        graphMinmax.add_node(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    minmax_cost, traced_path4 = graphMinmax.alpha_beta(graphMinmax.root, True)
                    graphMinmax.print_path(traced_path4)
                    print("\nCost: ", minmax_cost)
                    G_traced = nx.Graph()
                    for i in range(len(traced_path4) - 1):
                        G_traced.add_edge(traced_path4[i], traced_path4[i + 1])

                    pos = nx.spring_layout(G_traced)
                    nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                    nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                 edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                    plt.show()
                elif searchType == "Simulated Annealing":
                    graphsimulatedannealing = Graph_simulatedAnnealing(directed=False)
                    graphsimulatedannealing.add_edge("s", "a", 2)
                    graphsimulatedannealing.add_edge("s", "b", 5)
                    graphsimulatedannealing.add_edge("a", "c", 2)
                    graphsimulatedannealing.add_edge("a", "d", 4)
                    graphsimulatedannealing.add_edge("b", "d", 1)
                    graphsimulatedannealing.add_edge("b", "g", 5)
                    graphsimulatedannealing.add_edge("d", "c", 3)
                    graphsimulatedannealing.add_edge("d", "g", 2)
                    G.add_edge("s", "a", weight=2)
                    G.add_edge("s", "b", weight=5)
                    G.add_edge("a", "c", weight=2)
                    G.add_edge("a", "d", weight=4)
                    G.add_edge("b", "d", weight=1)
                    G.add_edge("b", "g", weight=5)
                    G.add_edge("d", "c", weight=3)
                    G.add_edge("d", "g", weight=2)
                    DG.add_edge("s", "a", weight=2)
                    DG.add_edge("s", "b", weight=5)
                    DG.add_edge("a", "c", weight=2)
                    DG.add_edge("a", "d", weight=4)
                    DG.add_edge("b", "d", weight=1)
                    DG.add_edge("b", "g", weight=5)
                    DG.add_edge("d", "c", weight=3)
                    DG.add_edge("d", "g", weight=2)
                    for i in range(0, self.counter):
                        graphsimulatedannealing.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goal = Goal_list
                    traced_path4, cost = graphsimulatedannealing.simulated_annealing_search(start, goal)

                    if traced_path4:
                        print("cost:", cost)
                        print('Path:', end=' ')
                        Graph_simulatedAnnealing.print_path(traced_path4,cost)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path4) - 1):
                            G_traced.add_edge(traced_path4[i], traced_path4[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()

            else:
                if searchType == "BFS":
                    graphbfs = Graph_bfs(directed=True)
                    for i in range(0, self.counter):
                        graphbfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path1, goal = graphbfs.breadth_first_search(start, goals)
                    if (traced_path1):
                        print('Path:', end=' ')
                        Graph_bfs.print_path(traced_path1, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path1) - 1):
                            G_traced.add_edge(traced_path1[i], traced_path1[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(directed=True)
                    for i in range(0, self.counter):
                        graphdfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2, goal = graphdfs.depth_first_search(start, goals)
                    if (traced_path2):
                        print('Path:', end=' ')
                        Graph_dfs.print_path(traced_path2, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path2) - 1):
                            G_traced.add_edge(traced_path2[i], traced_path2[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()
                # ask mashood
                elif searchType == "A*":
                    for i in range(0, self.counter):
                        self.graphastar.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path5, cost3, goal = self.graphastar.a_star_search(start, goals)
                    if (traced_path5):
                        print('Path:', end=' ')
                        Graph_astar.print_path(traced_path5, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path5) - 1):
                            G_traced.add_edge(traced_path5[i], traced_path5[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print('\nCost:', cost3)

                elif searchType == "IDS":
                    graphids = Graph_ids(directed=True)
                    for i in range(0, self.counter):
                        graphids.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path3, goal = graphids.depth_first_search(start, goals)
                    if (traced_path3):
                        print('Path:', end=' ')
                        Graph_ids.print_path(traced_path3, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path3) - 1):
                            G_traced.add_edge(traced_path3[i], traced_path3[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()

                elif searchType == "DLS":
                    graphdls = Graph_dls(directed=True)
                    for i in range(0, self.counter):
                        graphdls.add_edge(Node1_arr[i], Node2_arr[i], self.EdgeWeight_arr[i])
                    start = self.StartNode_input.text()
                    goal = Goal_list
                    depth_limit = self.DepthLimitPushed()
                    traced_path4 = graphdls.depth_limited_search(start, goal, depth_limit)
                    if traced_path4:
                        print('Path:', end=' ')
                        Graph_dls.print_path(traced_path4, goal)
                        print()
                    else:
                        print(f"No path found within depth limit of {depth_limit}")

                elif searchType == "Bidirectional":
                    graphbis = Graph_bis(directed=True)
                    for i in range(0, self.counter):
                        graphbis.add_edge(Node1_arr[i], Node2_arr[i], self.EdgeWeight_arr[i])
                    start = self.StartNode_input.text()
                    goal = Goal_list[-1]
                    traced_path4 = graphbis.bidirectional_search(start, goal)
                    if traced_path4:
                        print('Path:', end=' ')
                        Graph_bis.print_path(traced_path4, goal)
                        G_traced = nx.Graph()
                        for i in range(len(traced_path4) - 1):
                            G_traced.add_edge(traced_path4[i], traced_path4[i + 1])

                        pos = nx.spring_layout(G_traced)
                        nx.draw(G_traced, pos, with_labels=True, node_size=1500)
                        nx.draw_networkx_edge_labels(G_traced, pos, font_size=26,
                                                     edge_labels=nx.get_edge_attributes(G_traced, 'weight'))

                        plt.show()
                        print()

        sys.stdout = original_stdout  # Reset the standard output to its original value

        with open("../test.txt") as f:
         contents = f.read()
         
        self.TheResult_Label.setText(contents)

    def GenerateGraphClicked(self):
        if self.GraphTypecomboBox.currentText() == "Undirectd Graph":
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=nx.get_edge_attributes(G, 'weight'))
            plt.show()
        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(DG, pos, font_size=26, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            plt.show()

    def AddNodeClicked(self):
        N1 = self.Node1_input.text()
        N2 = self.Node2_input.text()
        W = self.EdgeWieght_input.text()
        G.add_edge(N1, N2, weight=W)
        DG.add_edge(N1, N2, weight=W)
        Node1_arr[self.counter]=N1
        Node2_arr[self.counter]=N2
        self.EdgeWeight_arr[self.counter]=W
        self.counter = self.counter + 1
        self.Node1_input.clear()
        self.Node2_input.clear()
        self.EdgeWieght_input.clear()

    def HeuristicPushed(self):
        InputHeuristic = int(self.NodeHeuristic_input.text())
        InputNodeH = self.Node_Input.text()
        self.H[self.Node_Input.text()]= self.NodeHeuristic_input.text()
        self.HeuristicDict.update({InputNodeH: InputHeuristic})
        self.graphastar.set_huristics(self.HeuristicDict)
        self.graphastarD.set_huristics(self.HeuristicDict)
        self.Node_Input.clear()
        self.NodeHeuristic_input.clear()

    # def DepthLimitPushed(self):
    #     depth_limit_text = self.DepthLimit_input.text()
    #     if depth_limit_text.isdigit():
    #         self.depth_limit = int(depth_limit_text)
    #         print(f"Depth limit set to {self.depth_limit}")
    #     else:
    #         print("Please enter a valid integer for the depth limit.")
    #     self.DepthLimit_input.clear()

    def DepthLimitPushed(self):
        depth_limit = self.DepthLimit_input.text()
        try:
            depth_limit = int(depth_limit)
            if depth_limit < 0:
                raise ValueError("Depth limit should be a non-negative integer")
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Invalid input", str(e))
            return

        # TODO: Use the depth_limit variable in your search algor ithm
        print(f"Depth limit set to {depth_limit}")
        # self.DepthLimit_input.clear()
        return depth_limit

    def SubmitClicked (self):
        Goal_list.clear()
        G = self.GoalNode_input.text()
        Goal_list.append(G)
        self.GoalNode_input.clear()

    def setupUi(self, AISearchingTechniquesMainWindow):
        AISearchingTechniquesMainWindow.setObjectName("AISearchingTechniquesMainWindow")
        AISearchingTechniquesMainWindow.resize(779, 790)
        self.centralwidget = QtWidgets.QWidget(AISearchingTechniquesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SearchTypecomboBox.setGeometry(QtCore.QRect(630, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchTypecomboBox.setFont(font)
        self.SearchTypecomboBox.setObjectName("SearchTypecomboBox")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 240, 131, 31))
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.GenerateGraphClicked)
        self.Node1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_input.setGeometry(QtCore.QRect(26, 48, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1_input.setFont(font)
        self.Node1_input.setText("")
        self.Node1_input.setObjectName("Node1_input")
        self.Node2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_input.setGeometry(QtCore.QRect(26, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2_input.setFont(font)
        self.Node2_input.setObjectName("Node2_input")
        self.Node1Label = QtWidgets.QLabel(self.centralwidget)
        self.Node1Label.setGeometry(QtCore.QRect(26, 25, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1Label.setFont(font)
        self.Node1Label.setObjectName("Node1Label")
        self.Node2Label = QtWidgets.QLabel(self.centralwidget)
        self.Node2Label.setGeometry(QtCore.QRect(26, 78, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2Label.setFont(font)
        self.Node2Label.setObjectName("Node2Label")
        self.EdgeWieghtLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdgeWieghtLabel.setGeometry(QtCore.QRect(26, 131, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieghtLabel.setFont(font)
        self.EdgeWieghtLabel.setObjectName("EdgeWieghtLabel")
        self.EdgeWieght_input = QtWidgets.QLineEdit(self.centralwidget)
        self.EdgeWieght_input.setGeometry(QtCore.QRect(26, 157, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieght_input.setFont(font)
        self.EdgeWieght_input.setObjectName("EdgeWieght_input")
        self.AddNodesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodesButton.setGeometry(QtCore.QRect(26, 189, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodesButton.setFont(font)
        self.AddNodesButton.setObjectName("AddNodesButton")
        self.AddNodesButton.clicked.connect(self.AddNodeClicked)
        self.TheResult_Label = QtWidgets.QLabel(self.centralwidget)
        self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 751, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TheResult_Label.setFont(font)
        self.TheResult_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.TheResult_Label.setLineWidth(2)
        self.TheResult_Label.setText("")
        self.TheResult_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TheResult_Label.setObjectName("TheResult_Label")
        self.GeneratePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePathButton.setGeometry(QtCore.QRect(460, 240, 131, 31))
        self.GeneratePathButton.setObjectName("GeneratePathButton")
        self.GeneratePathButton.clicked.connect(self.GeneratePathClicked)
        self.TheResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.TheResultLabel.setGeometry(QtCore.QRect(10, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TheResultLabel.setFont(font)
        self.TheResultLabel.setObjectName("TheResultLabel")
        self.Node_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_Input.setGeometry(QtCore.QRect(227, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node_Input.setFont(font)
        self.Node_Input.setText("")
        self.Node_Input.setObjectName("Node_Input")
        self.NodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeLabel.setGeometry(QtCore.QRect(227, 26, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeLabel.setFont(font)
        self.NodeLabel.setObjectName("NodeLabel")
        self.NodeHeuristicLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeHeuristicLabel.setGeometry(QtCore.QRect(227, 78, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristicLabel.setFont(font)
        self.NodeHeuristicLabel.setObjectName("NodeHeuristicLabel")
        self.NodeHeuristic_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NodeHeuristic_input.setGeometry(QtCore.QRect(227, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristic_input.setFont(font)
        self.NodeHeuristic_input.setObjectName("NodeHeuristic_input")
        self.AddNodeHeuristicButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodeHeuristicButton.setGeometry(QtCore.QRect(227, 130, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodeHeuristicButton.setFont(font)
        self.AddNodeHeuristicButton.setObjectName("AddNodeHeuristicButton")
        self.AddNodeHeuristicButton.clicked.connect(self.HeuristicPushed)
        self.StartNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.StartNode_input.setGeometry(QtCore.QRect(430, 49, 137, 22))

        self.DepthLimitLabel = QtWidgets.QLabel(self.centralwidget)
        self.DepthLimitLabel.setGeometry(QtCore.QRect(227, 170, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DepthLimitLabel.setFont(font)
        self.DepthLimitLabel.setObjectName("DepthLimitLabel")

        self.DepthLimit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.DepthLimit_input.setGeometry(QtCore.QRect(227, 193, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DepthLimit_input.setFont(font)
        self.DepthLimit_input.setObjectName("DepthLimit_input")

        self.AddDepthLimitButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddDepthLimitButton.setGeometry(QtCore.QRect(227, 222, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddDepthLimitButton.setFont(font)
        self.AddDepthLimitButton.setObjectName("AddDepthLimitButton")
        self.AddDepthLimitButton.clicked.connect(self.DepthLimitPushed)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNode_input.setFont(font)
        self.StartNode_input.setText("")
        self.StartNode_input.setObjectName("StartNode_input")
        self.StartNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartNodeLabel.setGeometry(QtCore.QRect(430, 26, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNodeLabel.setFont(font)
        self.StartNodeLabel.setObjectName("StartNodeLabel")
        self.GoalNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.GoalNodeLabel.setGeometry(QtCore.QRect(430, 77, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNodeLabel.setFont(font)
        self.GoalNodeLabel.setObjectName("GoalNodeLabel")
        self.GoalNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalNode_input.setGeometry(QtCore.QRect(430, 100, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNode_input.setFont(font)
        self.GoalNode_input.setObjectName("GoalNode_input")
        self.GraphTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.GraphTypecomboBox.setGeometry(QtCore.QRect(630, 100, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GraphTypecomboBox.setFont(font)
        self.GraphTypecomboBox.setObjectName("GraphTypecomboBox")
        self.GraphTypecomboBox.addItem("")
        self.GraphTypecomboBox.addItem("")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(430, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.SubmitClicked)
        AISearchingTechniquesMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AISearchingTechniquesMainWindow)
        self.statusbar.setObjectName("statusbar")
        AISearchingTechniquesMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AISearchingTechniquesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AISearchingTechniquesMainWindow)

    def retranslateUi(self, AISearchingTechniquesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AISearchingTechniquesMainWindow.setWindowTitle(_translate("AISearchingTechniquesMainWindow", "AI Searching Techniques"))
        self.SearchTypecomboBox.setCurrentText(_translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "DFS"))
        self.SearchTypecomboBox.setItemText(2, _translate("AISearchingTechniquesMainWindow", "A*"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "DLS"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "IDS"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "UCS"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "Bidirectional"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "Best First"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "Simulated Annealing"))
        self.SearchTypecomboBox.addItem(_translate("AISearchingTechniquesMainWindow", "Alpha-beta Pruning"))
        self.GenerateGraphButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Graph"))
        self.Node1Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 1"))
        self.Node2Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 2"))
        self.EdgeWieghtLabel.setText(_translate("AISearchingTechniquesMainWindow", "Edge Wieght"))
        self.AddNodesButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Nodes"))
        self.TheResult_Label.setWhatsThis(_translate("AISearchingTechniquesMainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.GeneratePathButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Path"))
        self.TheResultLabel.setText(_translate("AISearchingTechniquesMainWindow", "The Result"))
        self.NodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node "))
        self.NodeHeuristicLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node Heuristic"))
        self.AddNodeHeuristicButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Node Heuristic"))
        self.StartNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Start Node"))
        self.GoalNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Goal Nodes"))
        self.GraphTypecomboBox.setCurrentText(_translate("AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "Undirectd Graph"))
        self.GraphTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "Directed Graph"))
        self.SubmitButton.setText(_translate("AISearchingTechniquesMainWindow", "Submit"))
        self.DepthLimitLabel.setObjectName("DepthLimitLabel")
        self.DepthLimitLabel.setText("Depth Limit:")
        self.AddDepthLimitButton.setObjectName("AddDepthLimitButton")
        self.AddDepthLimitButton.setText("Add Depth Limit")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AISearchingTechniquesMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AISearchingTechniquesMainWindow()
    ui.setupUi(AISearchingTechniquesMainWindow)
    AISearchingTechniquesMainWindow.show()
    sys.exit(app.exec_())
