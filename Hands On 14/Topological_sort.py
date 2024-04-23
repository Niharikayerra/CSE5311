class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)
        if end not in self.graph:
            self.graph[end] = []

    def dfs_util(self, v, visited, stack):
        visited[v] = True

        if v in self.graph:
            for i in self.graph[v]:
                if not visited[i]:
                    self.dfs_util(i, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = {}
        stack = []

        for v in self.graph.keys():
            visited[v] = False

        for v in self.graph.keys():
            if not visited[v]:
                self.dfs_util(v, visited, stack)

        return stack[::-1]

#Example from figure 22.7
g = Graph()
g.add_edge('undershorts', 'pants')
g.add_edge('undershorts', 'socks')
g.add_edge('pants', 'shoes')
g.add_edge('pants', 'belt')
g.add_edge('socks', 'shoes')
g.add_edge('shirt', 'belt')
g.add_edge('shirt', 'tie')
g.add_edge('tie', 'jacket')
g.add_edge('belt', 'jacket')

print("Topological Ordering:")
print(g.topological_sort())


'''Output:
Topological Ordering:
['shirt', 'tie', 'undershorts', 'socks', 'pants', 'belt', 'jacket', 'shoes'] '''