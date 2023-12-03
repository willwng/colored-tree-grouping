from typing import List

from node import Node


class Block:
    nodes = List[Node]

    def __init__(self, nodes: List[Node]):
        self.nodes = nodes
        # Assert that all protocols are the same
        assert len(set([node.protocol for node in nodes])) == 1

    def __str__(self):
        return f"Block: {[node.data for node in self.nodes]}"
