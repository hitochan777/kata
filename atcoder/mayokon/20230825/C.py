import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

N, X, Y = (int(x) for x in input().split())
X -= 1
Y -= 1
g = defaultdict(set)
for _ in range(N-1):
  a, b = (int(x)-1 for x in input().split())
  g[a].add(b)
  g[b].add(a)

def dfs(n, goal, parent=-1, path=[]):
  path.append(n+1)
  if n == goal:
    print(*path)
    exit()

  for nb in g[n]:
    if nb == parent:
      continue

    dfs(nb, goal, n, path)

  path.pop()

dfs(X, Y)