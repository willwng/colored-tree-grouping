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
        clone = copy.deepcopy(self.nodes)
        return clone

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

    def prune(self):
        for node in self.nodes:
            protocols = [predecessor.protocol for predecessor in node.prev]
            if node.protocol not in protocols:
                continue
            other_protocols = [p for p in protocols if p != node.protocol]
            if len(other_protocols) == 1:
                for p in node.prev:
                    if p.protocol == other_protocols[0]:
                        node.remove_predecessor(p)
                        p.remove_successor(node)
