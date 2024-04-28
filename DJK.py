import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}

    # Priority queue to keep track of vertices and their distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Check if this path is shorter than the currently known one
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Example graph representation (replace it with your own network graph)
network_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances, predecessors = dijkstra(network_graph, start_vertex)

# Example: Find the shortest path to 'D'
end_vertex = 'D'
path = []
while end_vertex is not None:
    path.insert(0, end_vertex)
    end_vertex = predecessors[end_vertex]

print(f"Shortest path from {start_vertex} to {path[-1]}: {path}")
print(f"Total distance: {distances[path[-1]]}")
