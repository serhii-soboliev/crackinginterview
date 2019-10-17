class Graph:
    v = []
    e = {}

    def __init__(self, v, e):
        self.v = v
        self.e = e

    def __str__(self) -> str:
        s1 = "Vertices: " + "\n" + "   " + str(self.v) + "\n"
        s2 = "Edges:  " + "\n" + "\n".join(list(map(lambda ve: "   %s -> %s" % (ve[0], ve[1]), self.e)))
        return s1 + s2

    def find_longest_acyclic_path_recursive(self, v_from, v_to):
        assert v_from in self.v
        assert v_to in self.v
        if v_from == v_to:
            return 0
        else:
            in_v = self.find_in_vertices(v_to)
            return 1 + max(map(lambda x: self.find_longest_acyclic_path_recursive(v_from, x), in_v))

    def find_longest_acyclic_path_optimal(self, v_from, v_to):
        assert v_from in self.v
        assert v_to in self.v
        paths = self.build_paths()
        return paths[v_from][v_to]

    def find_in_vertices(self, v):
        return list(map(lambda x: x[0],  filter(lambda y: y[1] == v, self.e)))

    def build_paths(self):
        pass
