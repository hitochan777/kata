from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

class Graph:
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list)
  
    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self,v,visited,parent):
        visited[v]= True
        for i in self.graph[v]:
            if  visited[i]==False : 
                if(self.isCyclicUtil(i,visited,v)):
                    return True

            elif  parent!=i:
                return True
          
        return False
           
   
    def isCyclic(self):
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i] ==False: 
                if(self.isCyclicUtil
                       (i,visited,-1)) == True:
                    return True
          
        return False

nb = defaultdict(lambda: set())
edges = set()
N, M = (int(x) for x in input().split())
for _ in range(M):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  nb[A].add(B)
  nb[B].add(A)
  edges.add((A,B))

g = Graph(N)
for A, B in edges:
  g.addEdge(A, B)

ok = all(len(s) <= 2 for s in nb.values()) and not g.isCyclic()
if ok:
  print("Yes")
else:
  print("No")
