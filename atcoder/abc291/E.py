import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
 

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def neighbor_gen(self, v):
        for k in self.graph[v]:
            yield k

    def topologicalSortUtil(self, v, visited, stack):
        working_stack = [(v, self.neighbor_gen(v))]
        while working_stack:
            v, gen = working_stack.pop()
            visited[v] = True
            for next_neighbor in gen:
                if not visited[next_neighbor]:  # not seen before?
                    working_stack.append((v, gen))
                    working_stack.append(
                        (next_neighbor, self.neighbor_gen(next_neighbor)))
                    break
            else:
                stack.append(v)
 
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
 
        for i in range(self.V):
            if not(visited[i]):
                self.topologicalSortUtil(i, visited, stack)
        stack.reverse()
        return stack
 
N, M = (int(x) for x in input().split())
g = Graph(N)
for _ in range(M):
    X, Y = (int(x)-1 for x in input().split())
    g.addEdge(X, Y)
 
 
seq = g.topologicalSort()
idx = {val: i for i, val in enumerate(seq)}

if not all(seq[i+1] in g.graph[seq[i]] for i in range(N-1)):
    print("No")
else:
    print("Yes")
    ans = [0] * N
    for i, val in enumerate(seq):
        ans[val] = i+1

    print(*ans)