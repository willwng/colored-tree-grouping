from typing import List, Optional, Dict, Set

from block import Block
from graph import Graph
from node import Node
from protocol import Protocol, get_all_protocols


def create_blocks(graph: Graph) -> List[Block]:
    """
    Create blocks from a graph
    :param graph: the graph
    :return: a list of blocks
    """
    blocks = []
    all_nodes = graph.get_nodes()
    while len(all_nodes) > 0:
        node = all_nodes.pop()
        # Filter all the nodes that have the same protocol as the current node
        same_protocol_nodes = [n for n in all_nodes if n.protocol == node.protocol]

        # Find nodes in the same basic block
        block = Block(nodes=same_protocol_nodes + [node])
        blocks.append(block)

    return blocks


def fetch_next_protocol(protocol: Optional[Protocol], nodes: List[Node]) -> Node:
    same_protocol_nodes = [n for n in nodes if n.protocol == protocol]
    if len(same_protocol_nodes) != 0:
        ret = same_protocol_nodes[0]
    else:
        ret = nodes[0]
    return ret


def fetch_next(protocol: Optional[Protocol], work_list: List[Node], done: Set[Node]) -> Node:
    sorted_protocols = rank_protocols(work_list=work_list, done=done)
    # Always prefer the protocol that is currently being processed
    sorted_protocols = [protocol] + sorted_protocols
    for protocol in sorted_protocols:
        same_protocol_nodes = [n for n in work_list if n.protocol == protocol]
        if len(same_protocol_nodes) == 0:
            continue
        ret = same_protocol_nodes.pop()
        return ret


def rank_protocols(work_list: List[Node], done: Set[Node]) -> List[Protocol]:
    protocol_ranks = {protocol: 0 for protocol in get_all_protocols()}
    protocol_reachable = {protocol: set() for protocol in get_all_protocols()}
    for work_node in work_list:
        # find all reachable nodes from [work_node]
        reachable_nodes = set()
        dfs_list = [work_node]
        while dfs_list:
            node = dfs_list.pop()
            reachable_nodes.add(node)
            for successor in node.next:
                if successor not in reachable_nodes:
                    dfs_list.append(successor)
        # add reachable nodes to the set of reachable nodes for the protocol
        protocol_reachable[work_node.protocol] = protocol_reachable[work_node.protocol].union(reachable_nodes)

    # Get the protocols for the reachable nodes (excluding the processed nodes)
    protocol_protocol = {protocol: set() for protocol in get_all_protocols()}
    for protocol in get_all_protocols():
        reachable_nodes = protocol_reachable[protocol]
        protocols = set([n.protocol for n in reachable_nodes if n.protocol != protocol and n not in done])
        protocol_protocol[protocol] = protocols
        protocol_ranks[protocol] += len(protocols)

    # Sort the protocols by rank
    sorted_protocols = sorted(protocol_ranks, key=lambda x: protocol_ranks[x], reverse=True)
    # print(sorted_protocols)
    # print(protocol_ranks)

    # Define an ordering: if protocol i is reachable from protocol j, and not the other way around, then protocol j
    #  should be more important than protocol i
    for i in range(len(sorted_protocols)):
        for j in range(i + 1, len(sorted_protocols)):
            # Protocol j should be more important than protocol i
            if sorted_protocols[i] in protocol_protocol[sorted_protocols[j]] and sorted_protocols[j] not in \
                    protocol_protocol[sorted_protocols[i]]:
                sorted_protocols[i], sorted_protocols[j] = sorted_protocols[j], sorted_protocols[i]

    # # Sort the protocols by the ordering
    # more_important = []
    # for i in range(len(sorted_protocols)):
    #     for j in range(i + 1, len(sorted_protocols)):
    #         if (sorted_protocols[i], sorted_protocols[j]) in ordering_pairs:
    #             more_important.append(sorted_protocols[j])
    #         elif (sorted_protocols[j], sorted_protocols[i]) in ordering_pairs:
    #             more_important.append(sorted_protocols[i])
    #
    # more_important = list(more_important)
    # # fill in the rest by size:
    # for protocol in sorted_protocols:
    #     if protocol not in more_important:

    return sorted_protocols


def topo_sort(graph: Graph) -> List[Node]:
    # Topological sort of nodes
    nodes = graph.get_nodes()
    work_list = [node for node in nodes if len(node.prev) == 0]
    sorted_nodes = []
    while work_list:
        node = work_list.pop()
        sorted_nodes.append(node)
        for successor in node.next:
            successor.remove_predecessor(node)
            if len(successor.prev) == 0:
                work_list.append(successor)
        nodes.remove(node)

    # Set successors
    for i in range(len(sorted_nodes) - 1):
        sorted_nodes[i].set_successors([sorted_nodes[i + 1]])
    return sorted_nodes


def protocol_sort(graph: Graph) -> List[Node]:
    # Topological sort of nodes
    nodes = graph.get_nodes()
    work_list = [node for node in nodes if len(node.prev) == 0]
    sorted_nodes = []
    protocol: Optional[Protocol] = None
    while work_list:
        node = fetch_next_protocol(protocol=protocol, nodes=work_list)
        protocol = node.protocol
        sorted_nodes.append(node)
        work_list.remove(node)
        for successor in node.next:
            successor.remove_predecessor(node)
            if len(successor.prev) == 0:
                work_list.append(successor)

    # Set successors
    for i in range(len(sorted_nodes) - 1):
        sorted_nodes[i].set_successors([sorted_nodes[i + 1]])
    return sorted_nodes


def rank_sort(graph: Graph) -> List[Node]:
    # Topological sort of nodes
    nodes = graph.get_nodes()
    work_list = [node for node in nodes if len(node.prev) == 0]
    sorted_nodes = []
    protocol: Optional[Protocol] = None
    while work_list:
        node = fetch_next(protocol=protocol, work_list=work_list, done=set(sorted_nodes))
        protocol = node.protocol
        sorted_nodes.append(node)
        for successor in node.next:
            successor.remove_predecessor(node)
            if len(successor.prev) == 0:
                work_list.append(successor)
        work_list.remove(node)

    # Set successors
    for i in range(len(sorted_nodes) - 1):
        sorted_nodes[i].set_successors([sorted_nodes[i + 1]])
    return sorted_nodes
