import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Якщо граф неорієнтований

    def dijkstra(self, start):
        heap = [(0, start)]
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Приклад використання:
# g = Graph()
# g.add_edge(0, 1, 1)
# g.add_edge(0, 4, 2)
# g.add_edge(4, 5, 3)
# g.add_edge(4, 10, 2)
# g.add_edge(1, 3, 4)
# print(g.dijkstra(0))