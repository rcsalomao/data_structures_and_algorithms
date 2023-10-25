from copy import deepcopy

from ds_graph import Graph, Vertex
from ds_queue import Queue


def breadth_first_search(graph: Graph, source_vertex: Vertex):
    source_vertex.set_distance(0)
    source_vertex.set_predecessor(None)
    vertex_queue = Queue()
    vertex_queue.enqueue(source_vertex)
    while not vertex_queue.is_empty():
        current_vertex: Vertex = vertex_queue.dequeue()
        neighbour: Vertex
        for neighbour in current_vertex.get_connections():
            if neighbour.get_color() == "white":
                neighbour.set_color("gray")
                neighbour.set_distance(current_vertex.get_distance() + 1)
                neighbour.set_predecessor(current_vertex)
                vertex_queue.enqueue(neighbour)
        current_vertex.set_color("black")


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
    g.add_edge(0, 2)
    g.add_edge(3, 1)
    g.add_edge(2, 4)
    breadth_first_search(g, g.get_vertex(0))
    print(traverse_node_to_source(g.get_vertex(4)))
