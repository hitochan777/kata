from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  a,b,c = (int(x) for x in input().split())
  g[a].append((b,c))
  g[b].append((a,c))

dist = [0] * (N+1)
def dfs(node, parent, acc_dist):
  global dist
  dist[node] = acc_dist

  for nb, d in g[node]:
    if nb == parent:
      continue

    dfs(nb, node, acc_dist+d)


Q, K = (int(x) for x in input().split())
dfs(K, 0, 0)
for _ in range(Q):
  x, y = (int(x) for x in input().split())
  print(dist[x] + dist[y])