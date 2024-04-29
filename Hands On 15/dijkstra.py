import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    prev = {node: None for node in graph}

    while pq:
        cur_distance, cur_node = heapq.heappop(pq)

        if cur_distance > distances[cur_node]:
            continue

        for neighbor, weight in graph[cur_node].items():
            distance = cur_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = cur_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, prev

# Example 24.6 from Page 659:
graph = {
    'S': {'T': 10, 'Y': 5, 'Z': 7},
    'T': {'X': 1, 'Y': 2},
    'X': {'Z': 4},
    'Y': {'Z': 2, 'T': 3, 'X': 9},
    'Z': {'S': 7, 'X': 6}
}

start_node = 'S'
distances, previous = dijkstra(graph, start_node)

print("Distances from", start_node + ":")
for node, distance in distances.items():
    print(node + ":", distance)

print("\nPrevious nodes:")
for node, prev_node in previous.items():
    print(node + ":", prev_node)


''' Output:
Distances from S:
S: 0
T: 8
X: 9
Y: 5
Z: 7

Previous nodes:
S: None
T: Y
X: T
Y: S
Z: S  '''