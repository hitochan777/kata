from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        nodes = [d]
        for i in self.graph[d]:
            if not visited_vertex[i]:
                nodes += self.dfs(i, visited_vertex)

        return nodes

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
    
    def get_scc(self):
        sccs = []
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                scc = gr.dfs(i, visited_vertex)
                sccs.append(scc)

        return sccs


N = int(input())
A = list(int(x)-1 for x in input().split())
MOD = 998244353
g = Graph(N)
incomings = set()

for i in range(N):
  g.add_edge(i, A[i])
  incomings.add(A[i])

sccs = g.get_scc()
# print(sccs)

cnt = 1
for scc in sccs:
  if len(scc) == 1:
    if scc[0] not in incomings:
      continue

  cnt *= 2
  cnt %= MOD

print(cnt-1)
