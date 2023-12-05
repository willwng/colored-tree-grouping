import networkx as nx
import random
from node import Node
from graph import Graph
from protocol import get_random_protocol, Protocol


def assign_protocol(i: int) -> Protocol:
    if i < 3:
        return Protocol.MPC
    elif i > 5:
        return Protocol.ABY
    else:
        return Protocol.WIL


def get_random_dag(n: int, p: float):
    g = nx.gnp_random_graph(n, p, directed=True)
    dag = nx.DiGraph([(u, v, {'weight': random.randint(-n, n)}) for (u, v) in g.edges() if u < v])
    nodes = [Node(data=str(i), protocol=get_random_protocol()) for i in range(n)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in dag.edges()]
    graph = Graph(nodes=nodes, edges=edges)
    return graph


def build_graph1():
    node_data = [str(i) for i in range(10)]
    nodes = [Node(data=data, protocol=assign_protocol(i)) for i, data in enumerate(node_data)]

    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in edges]
    return Graph(nodes=nodes, edges=edges)


def build_graph2():
    # Construct a DAG
    node_data = [str(i) for i in range(10)]
    nodes = [Node(data=data, protocol=assign_protocol(i)) for i, data in enumerate(node_data)]
    edges = [(0, 1), (1, 4), (4, 5), (2, 3), (3, 5), (3, 6), (5, 6), (7, 2), (7, 8), (8, 9), (9, 3)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in edges]
    return Graph(nodes=nodes, edges=edges)


def build_graph3():
    # Construct a DAG
    node_data = [str(i) for i in range(10)]
    nodes = [Node(data=data, protocol=assign_protocol(i)) for i, data in enumerate(node_data)]
    edges = [(0, 1), (1, 4), (4, 5), (2, 3), (3, 5), (3, 6), (5, 6), (7, 8), (8, 9), (9, 6)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in edges]
    return Graph(nodes=nodes, edges=edges)


def build_graph4():
    # Construct a DAG
    node_data = [str(i) for i in range(10)]
    nodes = [Node(data=data, protocol=assign_protocol(i)) for i, data in enumerate(node_data)]
    edges = [(0, 3), (3, 9), (9, 5), (2, 1), (1, 5), (1, 6), (5, 6), (7, 8), (8, 4), (4, 6)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in edges]
    return Graph(nodes=nodes, edges=edges)


def build_graph5():
    # Construct a DAG
    node_data = [str(i) for i in range(10)]
    nodes = [Node(data=data, protocol=assign_protocol(i)) for i, data in enumerate(node_data)]
    edges = [(0, 3), (3, 9), (9, 5), (2, 1), (1, 5), (1, 6), (5, 6), (7, 8), (8, 4), (4, 6)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in edges]
    return Graph(nodes=nodes, edges=edges)
