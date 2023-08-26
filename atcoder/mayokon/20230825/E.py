import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(set)
for _ in range(N-1):
  u, v = (int(x)-1 for x in input().split())
  g[u].add(v)
  g[v].add(u)


sub = defaultdict(int)
dist_sum = defaultdict(int)

def dfs(node, parent=-1):
  total_num_children = 1
  total_dist_sum = 0
  for nb in g[node]:
    if nb == parent:
      continue

    dfs(nb, node)
    total_dist_sum += dist_sum[nb] + sub[nb] 
    total_num_children += sub[nb]

  dist_sum[node] = total_dist_sum
  sub[node] = total_num_children

dfs(0)
ans = [0] * N
ans[0] = dist_sum[0]
q = [(0, -1)]
while q:
  node, parent = q.pop()
  for nb in g[node]:
    if nb == parent:
      continue

    ans[nb] = ans[node] + N - 2 * sub[nb]
    q.append((nb, node))

for i in range(N):
  print(ans[i])
