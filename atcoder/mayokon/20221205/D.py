import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

g = defaultdict(list)
N, Q = (int(x) for x in input().split())
X = list(int(x) for x in input().split())
for _ in range(N-1):
  A, B = (int(x)-1 for x in input().split())
  g[A].append(B)
  g[B].append(A)

mins = defaultdict(list)
def dfs(node, parent=-1):
  li = [X[node]]
  for nb in g[node]:
    if parent == nb:
      continue

    li.extend(dfs(nb, node))

  mins[node] = sorted(li, reverse=True)[:20]
  return mins[node]

dfs(0)

for _ in range(Q):
  V, K = (int(x) for x in input().split())
  V -= 1
  print(mins[V][K-1])