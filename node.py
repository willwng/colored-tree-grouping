from __future__ import annotations

from typing import List

from protocol import Protocol


class Node:
    """
    A node class
    """
    data: str
    protocol: Protocol
    next: List[Node]
    prev: List[Node]

    def __init__(self, data: str, protocol: Protocol):
        self.data = data
        self.protocol = protocol
        self.next = []
        self.prev = []

    def get_protocol(self) -> Protocol:
        return self.protocol

    def set_successors(self, successors: List[Node]):
        self.next = successors

    def add_successor(self, successor: Node):
        self.next.append(successor)

    def set_predecessors(self, predecessors: List[Node]):
        self.prev = predecessors

    def remove_predecessor(self, predecessor: Node):
        self.prev.remove(predecessor)

    def remove_successor(self, successor: Node):
        self.next.remove(successor)

    def add_predecessor(self, predecessor: Node):
        self.prev.append(predecessor)

    def all_predecessors(self) -> List[Node]:
        predecessors = []
        for predecessor in self.prev:
            predecessors.append(predecessor)
            predecessors.extend(predecessor.all_predecessors())
        return predecessors

    def __str__(self):
        return f"{self.data}, {self.protocol}; next: {[node.data for node in self.next]}; prev: {[node.data for node in self.prev]}"

    def simple_str(self):
        return f"({self.data}, {self.protocol})"