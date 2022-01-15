from bisect import insort

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def fixGraph(self):
      self.graph = sorted(self.graph)

    def KruskalMST(self, a, b, c):
        i = 0
        e = 0
        graph = self.graph[:] 
        insort(graph, (c, a, b))
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        while e < self.V - 1:
            w, u, v = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                e = e + 1
                if w == c:
                  print("Yes")
                  return

                self.union(parent, rank, x, y)

        print("No")

N, M, Q = (int(x) for x in input().split())
g = Graph(N)
for _ in range(M):
  a, b, c = (int(x) for x in input().split()) 
  a, b = a-1, b-1
  g.addEdge(a, b, c)

g.fixGraph()

for _ in range(Q):
  u, v, w = (int(x) for x in input().split())
  u, v = u-1, v-1
  g.KruskalMST(u, v, w)