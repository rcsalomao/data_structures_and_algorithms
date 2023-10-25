from copy import deepcopy
from pprint import pp

from ds_graph import Graph, Vertex
from ds_priority_queue import PriorityQueue
from ds_queue import Queue


def dijkstra_search(graph: Graph, start_vertex: Vertex):
    pq = PriorityQueue()
    start_vertex.set_distance(0)
    pq.build_heap([(vertex.get_distance(), vertex) for vertex in graph])
    while not pq.is_empty():
        current_vertex: Vertex = pq.pop_min()
        neighbour: Vertex
        for neighbour in current_vertex.get_connections():
            new_distance = current_vertex.get_distance() + current_vertex.get_weight(
                neighbour
            )
            if new_distance < neighbour.get_distance():
                neighbour.set_distance(new_distance)
                neighbour.set_predecessor(current_vertex)
                pq.decrease_key(new_distance, neighbour)


def traverse_node_to_source(node: Vertex):
    x: Vertex = deepcopy(node)
    q = Queue()
    while x.get_predecessor():
        q.enqueue(x.get_id())
        x = x.get_predecessor()
    q.enqueue(x.get_id())
    return q.to_list()


def shortest_path_djikstra(graph: Graph, start_vertex_key: int, end_vertex_key: int):
    dijkstra_search(graph, graph.get_vertex(start_vertex_key))
    vertex_key_route = traverse_node_to_source(graph.get_vertex(end_vertex_key))
    if start_vertex_key == vertex_key_route[0]:
        return {
            "path": vertex_key_route,
            "distance": graph.get_vertex(end_vertex_key).get_distance(),
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
    dijkstra_search(g, g.get_vertex(0))
    pp([(v.get_id(), v.get_distance()) for v in g])
    # pp(traverse_node_to_source(g.get_vertex(5)))
    # pp(shortest_path_djikstra(g, 0, 5))
