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
    edges.sort(key=lambda x: x[2]) 

    for u, v, w in edges:
        if ds.find_parent(u) != ds.find_parent(v):
            mst.append((u, v, w))
            ds.union(u, v)

    return mst