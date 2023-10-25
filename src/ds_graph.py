import math


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = "white"
        self.distance = math.inf
        self.predecessor = None
        self.discovery_step = 0
        self.finish_step = 0

    def add_neighbour(self, neighbour, weight=0):
        self.connected_to[neighbour] = weight

    def __str__(self):
        return "{0} connected to: {1}".format(
            str(self.id), str([i.id for i in self.connected_to])
        )

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.connected_to[neighbour]

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_predecessor(self):
        return self.predecessor

    def set_discovery_step(self, discovery_step):
        self.discovery_step = discovery_step

    def get_discovery_step(self):
        return self.discovery_step

    def set_finish_step(self, finish_step):
        self.finish_step = finish_step

    def get_finish_step(self):
        return self.finish_step


class Graph(object):
    def __init__(self):
        self.verts = {}
        self.num_verts = 0

    def add_vertex(self, key):
        self.num_verts += 1
        self.verts[key] = Vertex(key)

    def get_vertex(self, key):
        if key in self.verts:
            return self.verts[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.verts

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verts:
            self.add_vertex(from_key)
        if to_key not in self.verts:
            self.add_vertex(to_key)
        self.verts[from_key].add_neighbour(self.verts[to_key], weight)

    def get_vertices(self):
        return self.verts.keys()

    def __iter__(self):
        return iter(self.verts.values())


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.num_verts)
    print(g.verts)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connections():
            print("( %s, %s, %s )" % (v.get_id(), w.get_id(), v.get_weight(w)))
