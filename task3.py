import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],
    'E': [('C', 10), ('D', 2), ('Z', 3)],
    'Z': [('D', 6), ('E', 3)]
}

def dijkstra_heap(graph, start):
    """
    Алгоритм Дейкстри з приоритетною чергою (heap)
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]  # (distance, vertex)

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

if __name__ == "__main__":
    start_node = 'A'
    result = dijkstra_heap(graph, start_node)

    print(f"=== Найкоротші шляхи від сторини '{start_node}':")
    for vertex, dist in result.items():
        print(f"  До {vertex}: {dist}")
