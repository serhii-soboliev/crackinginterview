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
