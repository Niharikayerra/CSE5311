def floyd_warshall_algorithm(graph):
    distance = {u: {v: float('inf') if u != v else 0 for v in graph} for u in graph}
    
    # Fill distance matrix with initial values
    for u in graph:
        for v in graph[u]:
            distance[u][v] = graph[u][v]

    # Compute shortest paths
    for k in graph:
        for i in graph:
            for j in graph:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# Example graph (Figure 25.1 from Page 690)
graph = {
    '1': {'2': 3, '3': 8, '5': -4},
    '2': {'5': 7, '4': 1},
    '3': {'2': 4},
    '4': {'3': -5, '1': 2},
    '5': {'4': 6}
}

all_pairs_shortest_paths = floyd_warshall_algorithm(graph)
for u in graph:
    for v in graph:
        print(f"Shortest path from {u} to {v}: {all_pairs_shortest_paths[u][v]}")
    print()

'''output:
Shortest path from 1 to 1: 0
Shortest path from 1 to 2: 1
Shortest path from 1 to 3: -3
Shortest path from 1 to 4: 2
Shortest path from 1 to 5: -4

Shortest path from 2 to 1: 3
Shortest path from 2 to 2: 0
Shortest path from 2 to 3: -4
Shortest path from 2 to 4: 1
Shortest path from 2 to 5: -1

Shortest path from 3 to 1: 7
Shortest path from 3 to 2: 4
Shortest path from 3 to 3: 0
Shortest path from 3 to 4: 5
Shortest path from 3 to 5: 3

Shortest path from 4 to 1: 2
Shortest path from 4 to 2: -1
Shortest path from 4 to 3: -5
Shortest path from 4 to 4: 0
Shortest path from 4 to 5: -2

Shortest path from 5 to 1: 8
Shortest path from 5 to 2: 5
Shortest path from 5 to 3: 1
Shortest path from 5 to 4: 6
Shortest path from 5 to 5: 0  '''