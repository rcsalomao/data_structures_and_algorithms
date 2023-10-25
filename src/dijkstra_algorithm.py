import math
from collections import deque
from ds_priority_queue import PriorityQueue
from smol_graph import Graph


def dijkstra_search(graph: Graph, start_vertex):
    distance = {}
    predecessor = {}
    pq = PriorityQueue()
    for v in graph:
        distance[v] = math.inf
        predecessor[v] = None
    distance[start_vertex] = 0
    pq.build_heap([(distance[u], u) for u in graph])
    while not pq.is_empty():
        u = pq.pop_min()
        for v in graph.get_vertex_edges(u):
            new_dist = distance[u] + graph.get_weight(u, v)
            if new_dist < distance[v]:
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


def shortest_path_djikstra(graph: Graph, start_vertex, end_vertex):
    dij_res = dijkstra_search(graph, start_vertex)
    vertex_route = traverse_vertex_to_source(dij_res["predecessors"], end_vertex)
    if start_vertex == vertex_route[0]:
        return {
            "path": vertex_route,
            "distance": dij_res["distances"][end_vertex],
        }
    else:
        return None


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
    res = dijkstra_search(g, 0)
    # print(traverse_vertex_to_source(res["predecessors"], 6))
    print(shortest_path_djikstra(g, 0, 6))
