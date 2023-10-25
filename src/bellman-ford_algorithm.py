from pprint import pp
import math
from smol_graph import Graph
from collections import deque


def bellman_ford_algorithm(graph: Graph, source_vertex):
    max_iter = graph.num_verts - 1
    distance = {}
    predecessor = {}
    for u in graph:
        distance[u] = math.inf
        predecessor[u] = None
    distance[source_vertex] = 0
    for _ in range(max_iter):
        for u in graph:
            for v in graph.get_vertex_edges(u):
                old_dist = distance[v]
                distance[v] = min(
                    old_dist,
                    distance[u] + graph.get_weight(u, v),
                )
                if old_dist != distance[v]:
                    predecessor[v] = u
    return {"distances": distance, "predecessors": predecessor}


def traverse_vertex_to_source(predecessors: dict, vertex):
    q = deque()
    while predecessors[vertex] is not None:
        q.appendleft(vertex)
        vertex = predecessors[vertex]
    q.appendleft(vertex)
    return list(q)


if __name__ == "__main__":
    g = Graph()
    g.add_edge("S", "A", 10)
    g.add_edge("S", "E", 8)
    g.add_edge("E", "D", 1)
    g.add_edge("D", "C", -1)
    g.add_edge("D", "A", -4)
    g.add_edge("A", "C", 2)
    g.add_edge("C", "B", -2)
    g.add_edge("B", "A", 1)
    bell_res = bellman_ford_algorithm(g, "S")
    pp({v: bell_res["distances"][v] for v in g})
    print(traverse_vertex_to_source(bell_res["predecessors"], "B"))
