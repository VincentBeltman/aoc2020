class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([(x.id, value) for x, value in self.adjacent.items()])

    def add_neighbor(self, neighbor, weight=0, is_upstream=True):
        self.adjacent[neighbor] = {"weight": weight, "is_upstream": is_upstream}

    def get_connections(self):
        return self.adjacent.keys()

    def get_downstream_connections(self):
        return [key for key, value in self.adjacent.items() if not value["is_upstream"]]

    def get_upstream_connections(self):
        return [key for key, value in self.adjacent.items() if value["is_upstream"]]

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]["weight"]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def print(self):
        for node in self:
            for neighbour in node.get_connections():
                node_id = node.get_id()
                neighbour_id = neighbour.get_id()
                print('(%s, %s, %3d)' % (node_id, neighbour_id, node.get_weight(neighbour)))

        for node in self:
            print('g.vert_dict[%s]=%s' % (node.get_id(), self.vert_dict[node.get_id()]))

    def add_vertex(self, node):
        if node not in self.vert_dict:
            self.num_vertices = self.num_vertices + 1
            new_vertex = Vertex(node)
            self.vert_dict[node] = new_vertex
        return self.vert_dict[node]

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost, False)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost, True)

    def get_vertices(self):
        return self.vert_dict.keys()
