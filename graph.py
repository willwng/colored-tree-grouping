import copy
from typing import List, Tuple

from node import Node
import graphviz


class Graph:
    nodes: List[Node]

    def __init__(self, nodes: List[Node], edges: List[Tuple[Node, Node]]):
        self.nodes = nodes
        if edges is not None:
            for edge in edges:
                edge[0].add_successor(edge[1])
                edge[1].add_predecessor(edge[0])

    def __str__(self):
        return "\n".join([str(node) for node in self.nodes])

    def get_nodes(self):
        return copy.deepcopy(self.nodes)

    def to_graphviz(self):
        dot = graphviz.Digraph()
        for node in self.nodes:
            dot.node(node.data, node.data, color=node.protocol.to_color())
        for node in self.nodes:
            for successor in node.next:
                dot.edge(node.data, successor.data)
        return dot

    def get_joins(self):
        joins = []
        for node in self.nodes:
            if len(node.prev) > 1:
                joins.append(node)
        return joins
