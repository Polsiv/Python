import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
 
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def MST_PRIM(self, root):
        V = self.V
        key = [float('inf')] * V
        parent = [None] * V
        key[root] = 0


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