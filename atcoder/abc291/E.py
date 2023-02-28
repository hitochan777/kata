from collections import defaultdict
 
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(set) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    def addEdge(self,u,v):
        self.graph[u].add(v)
 
    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        stack.insert(0,v)

    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        return stack
 
N, M = (int(x) for x in input().split())
g = Graph(N)
for _ in range(M):
    X, Y = (int(x)-1 for x in input().split())
    g.addEdge(X, Y)


seq = g.topologicalSort()
if all(seq[i+1] in g.graph[seq[i]] for i in range(N-1)):
    print("Yes")
else:
    print("No")
    
