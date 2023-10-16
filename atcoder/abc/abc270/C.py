from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N, X, Y = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(N-1):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)

prev = [-1] * N
def dfs(node, dest, path=[], parent=-1):
  prev[node] = parent
  if node == dest:
    return

  for nb in g[node]:
    if nb == parent:
      continue

    dfs(nb, dest, path, node)

dfs(X-1, Y-1, [])
ans = [Y]
cur = Y-1
while cur != X-1:
  cur = prev[cur]
  ans.append(cur+1)

print(*ans[::-1])
   