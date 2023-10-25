from collections import deque
from pprint import pp

from ds_depth_first_search import depth_first_search
from ds_graph import Graph


def topological_sort(graph: Graph):
    depth_first_search(graph)
    q = deque()
    for vertex in graph:
        q.append(vertex)
    sorted_queue = sorted(q, key=lambda vertex: vertex.get_finish_step(), reverse=True)
    return [{"id": x.get_id(), "vertex": x} for x in sorted_queue]


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(2, 1)
    g.add_edge(3, 1)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(4, 6)
    g.add_edge(6, 7)
    g.add_edge(5, 7)
    sorted_vertices = topological_sort(g)
    pp(sorted_vertices)
    pp(
        [
            (i["id"], i["vertex"].get_discovery_step(), i["vertex"].get_finish_step())
            for i in sorted_vertices
        ]
    )
