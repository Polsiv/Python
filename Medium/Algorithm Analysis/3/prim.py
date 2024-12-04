import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        
        # adjacency matrix
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def MST_PRIM(self, root):
        V = self.V
        key = [float('inf')] * V
        parent = [None] * V
        key[root] = 0

        # priority queue of (key, vertex)
        Q = [(0, root)]
        in_queue = {i: True for i in range(V)}

        while Q:
            _, u = heapq.heappop(Q)
            in_queue[u] = False

            for v in range(V):
                weight = self.graph[u][v]
                if weight > 0 and in_queue[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
                    heapq.heappush(Q, (key[v], v))

        print("Edge \tWeight")
        for v in range(1, V):
            if parent[v] is not None:
                print(f"{parent[v]} - {v} \t{self.graph[parent[v]][v]}")

# graph (u, v, w)
edges = [
    (2, 5, 8),  # c -> f
    (0, 2, 2),  # a -> c
    (0, 6, 7),  # a -> g
    (1, 3, 2),  # b -> d
    (7, 9, 2),  # h -> j
    (2, 6, 3),  # c -> g
    (5, 9, 3),  # f -> j
    (0, 1, 4),  # a -> b
    (3, 7, 6),  # d -> h
    (6, 9, 5),  # g -> j
    (6, 3, 4),  # g -> d
]

# vertices (highest vertex index + 1)
num_vertices = max(max(u, v) for u, v, _ in edges) + 1

# create the graph, then add edges
g = Graph(num_vertices)
for u, v, w in edges:
    g.add_edge(u, v, w)

g.MST_PRIM(0)
