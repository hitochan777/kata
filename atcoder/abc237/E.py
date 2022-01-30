class Graph:
  def __init__(self, vertices):
    self.V = vertices # No. of vertices
    self.graph = []

  def addEdge(self, u, v, w):
    self.graph.append([u, v, w])
    
  def BellmanFord(self, src):
    dist = [float("Inf")] * self.V
    dist[src] = 0

    for _ in range(self.V - 1):
      for u, v, w in self.graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

    return dist


N, M = (int(x) for x in input().split())
H = list(int(x) for x in input().split())

g = Graph(N)
for _ in range(M):
  U, V = (int(x) for x in input().split())
  U, V = U-1, V-1
  g.addEdge(U, V, -(H[U] - H[V]))
  g.addEdge(V, U, -2 * (H[V] - H[U]))
  print(-(H[U] - H[V]))
  print(-2 * (H[V] - H[U]))

dist = g.BellmanFord(0)
print(-min(dist))