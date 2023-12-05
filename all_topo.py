# class to represent a graph object
from graph import Graph


class TopoGraph:

    # Constructor
    def __init__(self, edges, N):
        self.best_score = 999999
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # stores in-degree of a vertex
        # initialize in-degree of each vertex by 0
        self.indegree = [0] * N

        # add edges to the undirected graph
        for (src, dest) in edges:
            # add an edge from source to destination
            self.adjList[src].append(dest)

            # increment in-degree of destination vertex by 1
            self.indegree[dest] = self.indegree[dest] + 1


def graph_to_topo_graph(graph):
    edges = []
    for node in graph.nodes:
        for successor in node.next:
            edges.append((int(node.data), int(successor.data)))
    return TopoGraph(edges, len(graph.nodes))


def get_num_protocol_swaps(path, nodes) -> int:
    swaps = 0
    for i in range(len(path) - 1):
        if nodes[path[i]].protocol != nodes[path[i + 1]].protocol:
            swaps += 1
    return swaps


# Recursive function to find
# all topological orderings of a given DAG
def findAllTopologicalOrders(graph, path, discovered, N, real_graph):
    # do for every vertex
    for v in range(N):

        # proceed only if in-degree of current node is 0 and
        # current node is not processed yet
        if graph.indegree[v] == 0 and not discovered[v]:

            # for every adjacent vertex u of v,
            # reduce in-degree of u by 1
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] - 1

            # include current node in the path
            # and mark it as discovered
            path.append(v)
            discovered[v] = True

            # recur
            findAllTopologicalOrders(graph, path, discovered, N, real_graph)

            # backtrack: reset in-degree
            # information for the current node
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] + 1

            # backtrack: remove current node from the path and
            # mark it as undiscovered
            path.pop()
            discovered[v] = False

    # print the topological order if
    # all vertices are included in the path
    if len(path) == N:
        graph.best_score = min(graph.best_score, get_num_protocol_swaps(path, real_graph.nodes))


# Print all topological orderings of a given DAG
def get_best_swaps(topo_graph, real_graph):
    # get number of nodes in the graph
    N = len(topo_graph.adjList)

    # create an auxiliary space to keep track of whether vertex is discovered
    discovered = [False] * N

    # list to store the topological order
    path = []

    # find all topological ordering and print them
    findAllTopologicalOrders(topo_graph, path, discovered, N, real_graph)
    return topo_graph.best_score


if __name__ == '__main__':
    # List of graph edges as per above diagram
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

    print("All Topological sorts")

    # Number of nodes in the graph
    N = 6

    # create a graph from edges
    graph = TopoGraph(edges, N)

    # print all topological ordering of the graph
    get_best_swaps(graph)
