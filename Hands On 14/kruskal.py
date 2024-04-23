class MyGraph:
    def __init__(self, num_vertices):
        self.vertices = num_vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def find_root(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_root(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_root(parent, x)
        y_root = self.find_root(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_algorithm(self):
        result = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        index = 0
        edge_index = 0

        while edge_index < self.vertices - 1:
            u, v, weight = self.graph[index]
            index += 1
            x = self.find_root(parent, u)
            y = self.find_root(parent, v)

            if x != y:
                edge_index += 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)

        return result


my_graph = MyGraph(9)
node_positions = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
my_graph.add_edge(node_positions['a'], node_positions['b'], 4)  # A-B
my_graph.add_edge(node_positions['a'], node_positions['h'], 8)  # A-H
my_graph.add_edge(node_positions['b'], node_positions['h'], 11) # B-H
my_graph.add_edge(node_positions['b'], node_positions['c'], 8)  # B-C
my_graph.add_edge(node_positions['h'], node_positions['i'], 7)  # H-I
my_graph.add_edge(node_positions['g'], node_positions['h'], 1)  # G-H
my_graph.add_edge(node_positions['g'], node_positions['i'], 6)  # G-I
my_graph.add_edge(node_positions['c'], node_positions['i'], 2)  # C-I
my_graph.add_edge(node_positions['c'], node_positions['f'], 4)  # C-F
my_graph.add_edge(node_positions['c'], node_positions['d'], 7)  # C-D
my_graph.add_edge(node_positions['f'], node_positions['d'], 14) # F-D
my_graph.add_edge(node_positions['f'], node_positions['e'], 10) # F-E
my_graph.add_edge(node_positions['d'], node_positions['e'], 9)  # D-E

minimum_spanning_tree = my_graph.kruskal_algorithm()
print(" Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"{chr(97 + u)} - {chr(97 + v)} = {weight}") 

'''Output:
g - h = 1
c - i = 2
a - b = 4
c - f = 4
g - i = 6
c - d = 7
a - h = 8
d - e = 9 '''