from copy import deepcopy
from ds_graph import Graph, Vertex
from ds_queue import Queue


def dfs_visit(from_vertex: Vertex, persistent_vars):
    from_vertex.set_color("gray")
    persistent_vars["current_step"] += 1
    from_vertex.set_discovery_step(persistent_vars["current_step"])
    to_vertex: Vertex
    for to_vertex in from_vertex.get_connections():
        if to_vertex.get_color() == "white":
            to_vertex.set_predecessor(from_vertex)
            dfs_visit(to_vertex, persistent_vars)
    from_vertex.set_color("black")
    persistent_vars["current_step"] += 1
    from_vertex.set_finish_step(persistent_vars["current_step"])


def depth_first_search(graph: Graph):
    persistent_vars = {"current_step": 0}
    for vertex in graph:
        vertex.set_color("white")
    for vertex in graph:
        if vertex.get_color() == "white":
            dfs_visit(vertex, persistent_vars)


def traverse_node_to_source(node: Vertex):
    x: Vertex = deepcopy(node)
    q = Queue()
    while x.get_predecessor():
        q.enqueue(x.get_id())
        x = x.get_predecessor()
    q.enqueue(x.get_id())
    return q.to_list()


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(2, 1)
    g.add_edge(3, 1)
    g.add_edge(1, 4)
    g.add_edge(5, 4)
    g.add_edge(4, 6)
    depth_first_search(g)
    print(traverse_node_to_source(g.get_vertex(6)))
