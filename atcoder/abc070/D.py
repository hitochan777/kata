from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  a, b, c = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append((b, c))
  g[b].append((a, c))


Q, K = (int(x) for x in input().split())
K -= 1
dist = [10**18] * N
dist[K] = 0


def dfs(node, total_cost = 0, parent = -1):
  dist[node] = total_cost
  for nb, c in g[node]:
    if nb == parent:
      continue

    dfs(nb, total_cost+c, node)

dfs(K)

for _ in range(Q):
  x, y = (int(x) for x in input().split())
  x, y = x-1, y-1
  print(dist[x] + dist[y])