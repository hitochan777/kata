import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  U, V, W = (int(x) for x in input().split())
  U, V = U-1, V-1
  g[U].append((V,W))
  g[V].append((U,W))

colors = [0] * N
def dfs(node, color, parent=-1):
  global colors
  colors[node] = color
  for nb, d in g[node]:
    if parent == nb:
      continue

    new_color = (color + d) % 2
    dfs(nb, new_color, node)

dfs(0, 0)
print(*colors)



