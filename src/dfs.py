from smol_graph import Graph
from collections import deque


def dfs_helper(graph: Graph, visited: set, path: deque, u):
    if u in visited:
        return
    visited.add(u)
    path.append(u)
    for v in graph.get_vertex_edges(u):
        # path.append((u, v))
        dfs_helper(graph, visited, path, v)


def dfs(graph: Graph, start_vertex):
    visited = set()
    path = deque()
    dfs_helper(graph, visited, path, start_vertex)
    return list(path)


# # Non recursive version 1
# def dfs(graph: Graph, start_vertex):
#     visited = set()
#     path = deque()
#     stack = deque()
#     stack.append(start_vertex)
#     while stack:
#         u = stack.pop()
#         if u in visited:
#             continue
#         visited.add(u)
#         path.append(u)
#         for v in graph.get_vertex_edges(u):
#             stack.append(v)
#     return list(path)


# # Non recursive version 2
# def dfs(graph: Graph, start_vertex):
#     visited = set()
#     path = deque()
#     stack = deque()
#     visited.add(start_vertex)
#     path.append(start_vertex)
#     stack.append(deque(g.get_vertex_edges(start_vertex).keys()))
#     while stack:
#         if stack[-1]:
#             u = stack[-1].popleft()
#             if u in visited:
#                 continue
#             visited.add(u)
#             path.append(u)
#             stack.append(deque(g.get_vertex_edges(u).keys()))
#         else:
#             stack.pop()
#     return list(path)


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
    print(dfs(g, 0))
