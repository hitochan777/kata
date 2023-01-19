from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)

g = defaultdict(list)
visited = set()
ans = 0
limit = 10**6
def dfs(c):
  global ans
  global limit
  if ans == limit:
    return

  visited.add(c) 
  ans += 1
  
  for d in g[c]:
    if d not in visited:
      dfs(d)

  visited.remove(c)

N, M = (int(x) for x in input().split())
for _ in range(M):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)

dfs(0)
print(ans)