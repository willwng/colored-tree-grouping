from typing import List, Optional, Dict

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


def fetch_next(protocol: Optional[Protocol], nodes: List[Node], protocol_rank: Dict[Protocol, int]) -> Node:
    sorted_protocols = sorted(protocol_rank.keys(), key=lambda x: protocol_rank[x], reverse=False)
    sorted_protocols = [protocol] + sorted_protocols
    for protocol in sorted_protocols:
        same_protocol_nodes = [n for n in nodes if n.protocol == protocol]
        if len(same_protocol_nodes) == 0:
            continue
        ret = same_protocol_nodes.pop()
        nodes.remove(ret)
        return ret


def rank_protocols(graph: Graph) -> Dict[Protocol, int]:
    all_protocols = get_all_protocols()
    protocol_ranks = {protocol: 0 for protocol in all_protocols}
    for join in graph.get_joins():
        protocol_ranks[join.protocol] += len(join.prev)
    return protocol_ranks


def topo_sort(graph: Graph) -> List[Node]:
    protocol_rank = rank_protocols(graph=graph)
    # Topological sort of nodes
    nodes = graph.get_nodes()
    work_list = [node for node in nodes if len(node.prev) == 0]
    sorted_nodes = []
    protocol: Optional[Protocol] = None
    while work_list:
        node = fetch_next(protocol=protocol, nodes=work_list, protocol_rank=protocol_rank)
        protocol = node.protocol
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
