from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(10**5 + 10)

class Graph:
    def __init__(self, n):
      self.n = n
      self.g = defaultdict(list)

    def add_edge(self, u, v):
      self.g[u].append(v)

    def topological_sort(self):
      in_degree = [0] * self.n
      for u in range(self.n):
        for nb in self.g[u]:
          in_degree[nb] += 1

      s = []
      for i in range(self.n):
        if in_degree[i] == 0:
          heapq.heappush(s, i)

      cnt = 0
      top_order = []
      appended = set()
      while len(s) > 0:
        u = heapq.heappop(s)
        if u not in appended:
          top_order.append(str(u+1))
          appended.add(u)

        for nb in self.g[u]:
          in_degree[nb] -= 1
          if in_degree[nb] == 0:
            heapq.heappush(s, nb)

        cnt += 1

      if (cnt != self.n):
        print(-1)
        return

      sys.stdout.write(" ".join(top_order))

N, M = (int(x) for x in sys.stdin.readline().split())
graph = Graph(N)
for _ in range(M):
  A, B = (int(x) for x in sys.stdin.readline().split())
  A, B = A-1, B-1
  graph.add_edge(A, B)

graph.topological_sort()
