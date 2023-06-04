import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_distance(self, dist, visited):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_value and not visited[v]:
                min_value = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    not visited[v]
                    and self.graph[u][v] > 0
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        print("Vertex\tDistance from Source")
        for v in range(self.V):
            print(f"{v}\t{dist[v]}")


# Example usage:
g = Graph(5)
g.graph = [
    [0, 4, 0, 0, 0],
    [4, 0, 8, 0, 0],
    [0, 8, 0, 7, 6],
    [3, 0, 7, 5, 9],
    [0, 0, 0, 9, 0]
]

g.dijkstra(0)
