from random import uniform, randint
from typing import List

import matplotlib.pyplot as plt

from all_topo import graph_to_topo_graph, get_best_swaps
from block import Block
from graph import Graph
from graph_generator import get_random_dag
from node import Node
from protocol import Protocol
from reorder import create_blocks, topo_sort, rank_sort, protocol_sort


def assign_protocol(i: int) -> Protocol:
    if i < 3:
        return Protocol.MPC
    elif i > 5:
        return Protocol.ABY
    else:
        return Protocol.WIL


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


def create_basic_blocks(graph: Graph) -> List[Block]:
    return create_blocks(graph=graph)


def get_num_protocol_swaps(nodes: List[Node]) -> int:
    swaps = 0
    for i in range(len(nodes) - 1):
        if nodes[i].protocol != nodes[i + 1].protocol:
            swaps += 1
    return swaps


def main():
    # graph = build_graph1()
    # print(graph)
    # blocks = create_basic_blocks(graph=graph)
    # print(blocks)`
    # sorted_graph = Graph(nodes=sorted_nodes, edges=[])
    # sorted_graph.to_graphviz().render('test-output/graph1_sorted.gv', view=True)
    n_swaps = []
    for i in range(100):
        p = uniform(0.1, 0.5)
        n = randint(5, 9)
        graph = get_random_dag(n=n, p=p)
        graph.prune()
        # graph.to_graphviz().render('test-output/graph1.gv', view=True)
        # print(", ".join([node.simple_str() for node in sorted_nodes]))
        # joins = graph.get_joins()
        sorted_nodes = rank_sort(graph)
        num_swaps = get_num_protocol_swaps(sorted_nodes)

        topo_graph = graph_to_topo_graph(graph)
        best_swaps = get_best_swaps(topo_graph, graph)
        if best_swaps == 0:
            continue
        n_swaps.append(num_swaps / best_swaps)
        if num_swaps / best_swaps > 2:
            graph.to_graphviz().render('test-output/graph1.gv', view=True)
            sorted_graph = Graph(nodes=sorted_nodes, edges=[])
            sorted_graph.to_graphviz().render('test-output/graph1_sorted.gv', view=True)
            quit()
    # plot distribution of n_swaps
    plt.hist(n_swaps, bins=30)
    plt.show()
    return


if __name__ == "__main__":
    main()
