class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

def initialize_single_source(vertices, start):
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    predecessors = {v: None for v in vertices}
    return distances, predecessors

def bellman_ford_algorithm(vertices, edges, start):
    distances, predecessors = initialize_single_source(vertices, start)
    for _ in range(len(vertices) - 1):
        for edge in edges:
            relax(edge.start, edge.end, edge.weight, distances, predecessors)
    for edge in edges:
        if distances[edge.end] > distances[edge.start] + edge.weight:
            return False
    return distances, predecessors

def relax(u, v, weight, distances, predecessors):
    if distances[v] > distances[u] + weight:
        distances[v] = distances[u] + weight
        predecessors[v] = u


# Example usage (Figure 24.4 from Page 652):
vertices = ['s', 't', 'x', 'y', 'z']
edges = [
    Edge('s', 't', 6),
    Edge('s', 'y', 7),
    Edge('t', 'x', 5),
    Edge('t', 'y', 8),
    Edge('t', 'z', -4),
    Edge('x', 't', -2),
    Edge('y', 'x', -3),
    Edge('y', 'z', 9),
    Edge('z', 'x', 7),
    Edge('z', 's', 2)
]
start = 's'

result = bellman_ford_algorithm(vertices, edges, start)
if result:
    distances, predecessors = result
    print("Shortest distances from", start)
    for vertex in vertices:
        print("Vertex:", vertex, "Distance:", distances[vertex], "Predecessor:", predecessors[vertex])
else:
    print("Negative cycle detected")


''' Output:
Shortest distances from s
Vertex: s Distance: 0 Predecessor: None
Vertex: t Distance: 2 Predecessor: x
Vertex: x Distance: 4 Predecessor: y
Vertex: y Distance: 7 Predecessor: s
Vertex: z Distance: -2 Predecessor: t '''