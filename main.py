from random import uniform, randint
from typing import List

import matplotlib.pyplot as plt

from all_topo import graph_to_topo_graph, get_best_swaps
from graph import Graph
from graph_generator import get_random_dag
from node import Node
from reorder import rank_sort


def get_num_protocol_swaps(nodes: List[Node]) -> int:
    swaps = 0
    for i in range(len(nodes) - 1):
        if nodes[i].protocol != nodes[i + 1].protocol:
            swaps += 1
    return swaps


def main():
    n_swaps = []
    for i in range(100):
        p = uniform(0.1, 0.5)
        n = randint(5, 9)
        graph = get_random_dag(n=n, p=p)
        graph.prune()

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
