import networkx as nx
import random
from node import Node
from graph import Graph
from protocol import get_random_protocol


def get_random_dag(n: int, p: float):
    g = nx.gnp_random_graph(n, p, directed=True)
    dag = nx.DiGraph([(u, v, {'weight': random.randint(-n, n)}) for (u, v) in g.edges() if u < v])
    nodes = [Node(data=str(i), protocol=get_random_protocol()) for i in range(n)]
    edges = [(nodes[edge[0]], nodes[edge[1]]) for edge in dag.edges()]
    graph = Graph(nodes=nodes, edges=edges)
    return graph
