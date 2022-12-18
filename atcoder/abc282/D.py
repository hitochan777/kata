import sys
from collections import defaultdict, Counter
sys.setrecursionlimit(10**6)
N, M = (int(x) for x in input().split())

g = defaultdict(list)
def dfs(graph, v, visited, color, base):
  for u in graph[v]:
    if u not in visited:
      visited.add(u)
      color[u] = (not (color[v] - base)) + base
      if not dfs(graph, u, visited, color, base):
        return False
 
    elif color[v] == color[u]:
      return False
 
  return True
 
 
def isBipartite(graph):
  visited = set()
  color = [0] * N
  base = 0
  for i in range(N):
    if i in visited:
      continue

    color[i] = base
    ok = dfs(graph, i, visited, color, base)
    if not ok:
      return False, None

    base += 2

  # print(color)
  return True, Counter(color)

for _ in range(M):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)

ok, cnt = isBipartite(g)
if not ok:
  print(0)
  exit()

# print(cnt)
nums = [val for val in cnt.values()]
# print(nums)
acc = [0]
for a in nums:
  acc.append(acc[-1]+a)

ans = 0
for i, a in enumerate(nums):
  ans += a * (acc[-1] - acc[i+1])

ans -= M
print(ans)

