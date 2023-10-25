import math
from pprint import pp


def create_knight_graph(n):
    def check_square_border(x, y, n):
        if x < 0 or y < 0 or x >= n or y >= n:
            return False
        else:
            return True

    move_offsets = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]
    graph = {}
    for i in range(n):
        for j in range(n):
            possible_movements = [(i + x, j + y) for x, y in move_offsets]
            graph[(i, j)] = {}
            for mov in possible_movements:
                if check_square_border(mov[0], mov[1], n):
                    graph[(i, j)][mov] = 1
    return graph


def calc_shortest_path(graph, source_node, destination_node):
    unvisited_graph = graph
    shortest_distances = {}
    route = []
    path_nodes = {}
    # initialize shortest distances
    for nodes in unvisited_graph:
        shortest_distances[nodes] = math.inf
    shortest_distances[source_node] = 0
    # djikstra algorithm
    while unvisited_graph:
        min_node = None
        for current_node in unvisited_graph:
            if min_node is None:
                min_node = current_node
            elif shortest_distances[min_node] > shortest_distances[current_node]:
                min_node = current_node
        for node, value in unvisited_graph[min_node].items():
            if value + shortest_distances[min_node] < shortest_distances[node]:
                shortest_distances[node] = value + shortest_distances[min_node]
                path_nodes[node] = min_node
        unvisited_graph.pop(min_node)
    node = destination_node
    # check if destination node is reachable
    while node != source_node:
        try:
            route.insert(0, node)
            node = path_nodes[node]
        except Exception:
            print("Destination node not reachable")
            break
    route.insert(0, source_node)
    return {"path": route, "distance": shortest_distances[destination_node]}


if __name__ == "__main__":
    size = 8
    graph = create_knight_graph(size)
    # pp(graph)
    shortest_path = calc_shortest_path(graph, (0, 0), (0, 1))
    pp(shortest_path)
