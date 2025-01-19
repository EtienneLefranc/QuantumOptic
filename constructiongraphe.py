# coding:utf-8

from igraph import Graph
import igraph as ig
import networkx as nx
import numpy as np


def random_graph_generator(n_nodes):
    """
    Takes a number of nodes and return an adjacency list and an igraph graph
    """
    degree_sequence = [0]*n_nodes
    for i in range(n_nodes):
        degree_sequence[i] = np.random.randint(1, n_nodes//3)
    print(degree_sequence)
    if sum(degree_sequence) < 2*(n_nodes-1):                    # Check is there is enough edges
        for i in range(2*(n_nodes-1)-sum(degree_sequence) + np.random.randint(0, (n_nodes/2))):
            degree_sequence[np.random.randint(0, n_nodes)] += 1
    if sum(degree_sequence) % 2 != 0:                           # Check is degree sum is even
        degree_sequence[np.random.randint(0, n_nodes)] += 1
    # print(degree_sequence)
    random_graph = Graph.Degree_Sequence(degree_sequence, method="vl")
    return [random_graph.get_adjlist(), random_graph]


if __name__ == "__main__":
    for i in range(1):
        random_graph = random_graph_generator(15)
        print(random_graph[0])
        print(random_graph[1])
        ig.plot(random_graph[1])
