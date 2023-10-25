from collections import deque
from pprint import pp

import numpy as np

from smol_graph import Graph


def get_path(backward_vertices_idx_map, prev_matrix, idx_u, idx_v):
    path = deque()
    if prev_matrix[idx_u, idx_v] is None:
        return []
    else:
        path.appendleft(backward_vertices_idx_map[idx_v])
        while idx_u != idx_v:
            idx_v = prev_matrix[idx_u, idx_v]
            path.appendleft(backward_vertices_idx_map[idx_v])
        return list(path)


def floyd_warshall_algorithm(graph: Graph):
    n_vertices = graph.num_verts
    dists = np.full((n_vertices, n_vertices), np.inf)
    prev = np.full((n_vertices, n_vertices), None)
    vertices_idx_map = {u: i for i, u in enumerate(graph)}
    backward_vertices_idx_map = {i: u for u, i in vertices_idx_map.items()}
    for u in graph:
        idx_u = vertices_idx_map[u]
        for v in graph.get_vertex_edges(u):
            idx_v = vertices_idx_map[v]
            dists[idx_u, idx_v] = graph.get_weight(u, v)
            prev[idx_u, idx_v] = idx_u
    for u in graph:
        idx_u = vertices_idx_map[u]
        dists[idx_u, idx_u] = 0
        prev[idx_u, idx_u] = idx_u
    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                val = dists[i, k] + dists[k, j]
                if dists[i, j] > val:
                    dists[i, j] = val
                    prev[i, j] = prev[k, j]
    res = []
    for u in graph:
        idx_u = vertices_idx_map[u]
        res.append(
            {
                "vertex": u,
                "dists": [
                    {
                        "vertex": v,
                        "dist": dists[idx_u, vertices_idx_map[v]],
                        "path": get_path(
                            backward_vertices_idx_map,
                            prev,
                            idx_u,
                            vertices_idx_map[v],
                        ),
                    }
                    for v in graph
                ],
            }
        )
    return res


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 3, -2)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 2)
    g.add_edge(4, 2, -1)
    a = floyd_warshall_algorithm(g)
    pp(a)
