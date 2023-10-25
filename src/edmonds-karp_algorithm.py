from collections import deque

from smol_graph import Graph


def max_flow(capacity_graph: Graph, source, sink):
    flux_map = {}
    for u in capacity_graph:
        for v in capacity_graph.get_vertex_edges(u):
            flux_map[(u, v)] = 0
            flux_map[(v, u)] = 0
    path = bfs(capacity_graph, flux_map, source, sink)
    while path is not None:
        flow = min(capacity_graph.get_weight(u, v) - flux_map[(u, v)] for u, v in path)
        for u, v in path:
            flux_map[(u, v)] += flow
            flux_map[(v, u)] -= flow
        path = bfs(capacity_graph, flux_map, source, sink)
    max = 0
    for e, value in flux_map.items():
        u, v = e
        if v is sink:
            max += value
    return {"max_flow": max, "flux_map": flux_map}


def bfs(capacity_graph: Graph, flux_map, source, sink):
    queue = deque()
    queue.appendleft(source)
    paths = {source: []}
    if source is sink:
        return []
    while queue:
        u = queue.pop()
        for v in capacity_graph.get_vertex_edges(u):
            if (
                capacity_graph.get_weight(u, v) - flux_map[(u, v)] > 0
            ) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v is sink:
                    return paths[v]
                queue.appendleft(v)
    return None


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 8)
    graph.add_edge(1, 3, 9)
    graph.add_edge(2, 3, 5)
    source = 0
    sink = 3
    res = max_flow(graph, source, sink)
    print(res["max_flow"])
    print(res["flux_map"])
