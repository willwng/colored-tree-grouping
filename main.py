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
    n_dags = 1000
    for i in range(n_dags):
        p = uniform(0.1, 0.9)
        n = randint(3, 10)
        n_protocols = min(randint(2, 5), n)
        graph = get_random_dag(n=n, p=p, n_protocol=n_protocols)

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
    plt.title(f"{n_dags} Random DAGs, size 3-10, p=0.1-0.9, 2-5 protocols")
    plt.hist(n_swaps, bins=10, weights=[1 / len(n_swaps)] * len(n_swaps))
    plt.xlabel(r"$\alpha$" + "= # swaps / # best swaps")
    plt.ylabel("Frequency")
    plt.show()
    return


if __name__ == "__main__":
    main()
