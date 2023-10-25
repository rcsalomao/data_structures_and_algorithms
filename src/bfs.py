from smol_graph import Graph
from collections import deque


def bfs(graph: Graph, initial_vertex):
    visited = set()
    path = deque()
    queue = deque()
    queue.appendleft(initial_vertex)
    while queue:
        u = queue.pop()
        if u in visited:
            continue
        visited.add(u)
        path.append(u)
        for v in graph.get_vertex_edges(u):
            # path.append((u, v))
            queue.appendleft(v)
    return list(path)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(0, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    print(bfs(g, 0))
