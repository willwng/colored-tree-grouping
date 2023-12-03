from typing import List

from block import Block
from graph import Graph
from node import Node
from protocol import Protocol
from reorder import create_blocks, topo_sort


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


def main():
    graph = build_graph1()
    print(graph)
    # blocks = create_basic_blocks(graph=graph)
    # print(blocks)
    graph.to_graphviz().render('test-output/graph1.gv', view=True)
    # print(", ".join([node.simple_str() for node in sorted_nodes]))
    # joins = graph.get_joins()
    sorted_nodes = topo_sort(graph)
    sorted_graph = Graph(nodes=sorted_nodes, edges=[])
    sorted_graph.to_graphviz().render('test-output/graph1_sorted.gv', view=True)
    return


if __name__ == "__main__":
    main()
