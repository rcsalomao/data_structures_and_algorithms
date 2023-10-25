import math
from collections import deque
from pprint import pp

from ds_priority_queue import PriorityQueue
from smol_graph import Graph


def prim_search(graph: Graph, start_vertex):
    pq = PriorityQueue()
    distance = {}
    predecessor = {}
    for v in graph:
        distance[v] = math.inf
        predecessor[v] = None
    distance[start_vertex] = 0
    pq.build_heap([(distance[u], u) for u in graph])
    while not pq.is_empty():
        u = pq.pop_min()
        for v in graph.get_vertex_edges(u):
            new_dist = graph.get_weight(u, v)
            if v in pq and new_dist < distance[v]:
                distance[v] = new_dist
                predecessor[v] = u
                pq.decrease_key(new_dist, v)
    return {"distances": distance, "predecessors": predecessor}


def traverse_vertex_to_source(predecessors: dict, vertex):
    q = deque()
    while predecessors[vertex] is not None:
        q.appendleft(vertex)
        vertex = predecessors[vertex]
    q.appendleft(vertex)
    return list(q)


def calc_prim_MST(graph: Graph, start_vertex):
    prim_res = prim_search(graph, start_vertex)
    g = Graph()
    for v, u in prim_res["predecessors"].items():
        if u is not None:
            g.add_edge(u, v, graph.get_weight(u, v))
    return g


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 1)
    g.add_edge(2, 1, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(3, 1, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(1, 4, 1)
    g.add_edge(5, 4, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 6, 1)
    prim_res = prim_search(g, 0)
    pp(prim_res)
    print(traverse_vertex_to_source(prim_res["predecessors"], 6))
    mst = calc_prim_MST(g, 0)
    pp(g.adj_list)
    pp(mst.adj_list)
