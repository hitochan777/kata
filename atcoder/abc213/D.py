import sys
from collections import defaultdict
sys.setrecursionlimit(210000)

graph = defaultdict(list)
visited = set()

def dfs(node) -> bool:
  if node in visited:
    return False

  visited.add(node)
  print(node+1, end=" ")
  for nb in graph[node]:
    ok = dfs(nb)
    if ok:
      print(node+1, end=" ")

  return True

N = int(input())
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  graph[A].append(B)
  graph[B].append(A)

for key in graph.keys():
  graph[key].sort()

dfs(0)