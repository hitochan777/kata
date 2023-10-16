from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(input())
g = defaultdict(set)
cnt = defaultdict(int)
for _ in range(N-1):
  u, v = (int(x)-1 for x in input().split())
  g[u].add(v)
  g[v].add(u)
  cnt[u] += 1
  cnt[v] += 1

ans = []
def dfs(node, parent=-1):
  children = 0
  for nb in g[node]:
    if nb == parent:
      continue

    children += dfs(nb, node)

  if cnt[parent] == 2 and cnt[node] == 2 and children >= 2:
    ans.append(children)
    cnt[parent] -= 1
    return 0

  return children + 1

dfs(0)
ans.append(N - (len(ans) + sum(ans)) - 1)
ans.sort()
print(*ans)