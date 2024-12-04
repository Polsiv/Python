class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find_parent(x)
        y_root = self.find_parent(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def kruskal_mst(edges, num_vertices):
    mst = []
    ds = DisjointSet(num_vertices)
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for u, v, w in edges:
        if ds.find_parent(u) != ds.find_parent(v):
            mst.append((u, v, w))
            ds.union(u, v)

    return mst


# edge list with vertices converted to indices
edges = [
    (0, 2, 2),  # a -> c
    (1, 3, 2),  # b -> d
    (7, 9, 2),  # h -> j
    (2, 6, 3),  # c -> g
    (5, 9, 3),  # f -> j
    (0, 1, 4),  # a -> b
    (6, 9, 4),  # g -> j
    (6, 9, 4),  # d -> g
    (3, 7, 6),  # d -> h
    (0, 6, 7),  # a -> g
    (2, 5, 8),  # c -> f 
]

edges2 = [
    (0, 1, 5), # a -> b
    (1, 2, 3), # b -> c
    (2, 0, 1), # c -> a
]


# Peculiar problem, we "need" 2 edges more since we skipped i and e.

#https://www.youtube.com/watch?v=5iBeLKst5bo
print(f"First Problem {'=' * 20}")

num_vertices = 10
result = kruskal_mst(edges, num_vertices)
print("number of nodes:", len(result))
print(result)
print("cost:", sum(x[2] for x in result))


num_vertices2 = 3

print(f"Second Problem {'=' * 20}")

result2 = kruskal_mst(edges2, num_vertices2)
print("number of nodes", len(result2))
print(result2)
print("cost:", sum(x[2] for x in result2))
