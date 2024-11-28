import heapq

class Vertex:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.neighbors = []

    def __lt__(self, other):
        return self.key < other.key

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def MST_PRIM(self, root):
        V = len(self.vertices)
        key = [float('inf')] * V
        key[root] = 0
        parent = [None] * V
        Q = []
        for v in range(V):
            Q.append(Vertex(key[v]))

        heapq.heapify(Q)

        while Q:
            u = heapq.heappop(Q)
            for v in range(V):
                if self.graph[u.key][v] > 0 and v in Q and self.graph[u.key][v] < Q[v].key:
                    Q[v].key = self.graph[u.key][v]
                    Q[v].parent = u.key
                    heapq.heapify(Q)

        print("Edge \tWeight")
        for v in range(1, V):
            print(f"{parent[v]} - {v} \t{self.graph[parent[v]][v]}")

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)

g.MST_PRIM(0)