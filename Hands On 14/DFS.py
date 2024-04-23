class Vertex:
    def __init__(self, label):
        self.label = label
        self.state = 0
        self.start_time = 0
        self.finish_time = 0
        self.previous = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {}
        self.time = 0

    def add_edge(self, start, end):
        if start not in self.adj:
            self.adj[start] = [end]
        else:
            self.adj[start].append(end)

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def depth_first_search(self):
        for v in self.adj.keys():
            v.state = 0
            v.previous = None
        self.time = 0
        for v in self.adj.keys():
            if v.state == 0:
                self.depth_first_search_visit(v)

    def depth_first_search_visit(self, vertex):
        self.time += 1
        vertex.start_time = self.time
        vertex.state = 1
        for v in self.adj[vertex]:
            if v.state == 0:
                v.previous = vertex
                self.depth_first_search_visit(v)
        vertex.state = 2
        self.time += 1
        vertex.finish_time = self.time

    def __str__(self):
        print("\n ---Adjacency List ---")
        for v in self.adj.keys():
            print(v.label, end=": ")
            for j in self.adj[v]:
                print(j.label, end=" ")
            print("\b")
        return "---End of Adjacency List ---\n"

# Testing the algorithm with an example
if __name__ == "__main__":
    graph = Graph(6)
    u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')
    graph.add_edge(u, v)
    graph.add_edge(u, x)
    graph.add_edge(x, v)
    graph.add_edge(v, y)
    graph.add_edge(y, x)
    graph.add_edge(w, y)
    graph.add_edge(w, z)
    graph.add_edge(z, z)

    graph.depth_first_search()
    print("DFS Ordering:")
    for i in graph.adj.keys():
        print(f"{i.label} ({i.start_time}/{i.finish_time}),", end=" ")


'''Output:
DFS Ordering: 
u (1/8), x (4/5), v (2/7), y (3/6), w (9/12), z (10/11), '''