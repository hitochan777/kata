import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
N, M = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  A, B = (int(x)-1 for x in input().split())
  g[A].append(B)
  g[B].append(A)

if any(len(v) > 2 for v in g.values()):
  print("No")
  exit()


def _has_loop(node, visited, parent=-1):
  visited.add(node)
  for nb in g[node]:
    if nb not in visited:
      if _has_loop(nb, visited, node):
        return True

    elif nb != parent:
      return True
    
  return False

def has_loop(N):
  visited = set()
  for i in range(N):
    if i not in visited:
      if _has_loop(i, visited):
        return True

  return False

if has_loop(N):
  print("No")
else:
  print("Yes")

