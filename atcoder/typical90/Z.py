from collections import defaultdict
import sys

sys.setrecursionlimit(10**5+1)

graph = defaultdict(list)
N = int(input())
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  graph[A-1].append(B-1)
  graph[B-1].append(A-1)

def dfs(node, color):
  if node in visited:
    return

  visited.add(node)
  colored[color].append(str(node+1))
  for nb in graph[node]:
    dfs(nb, not color)

visited = set()
colored = defaultdict(list)
dfs(0, True)
bigger = colored[True] if len(colored[True]) > len(colored[False]) else colored[False]
print(" ".join(bigger[:N//2]))
