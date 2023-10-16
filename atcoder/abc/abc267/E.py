from collections import defaultdict
import heapq


N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
g = defaultdict(list)
costs = defaultdict(int)
for _ in range(M):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)
  costs[u] += A[v]
  costs[v] += A[u]

h = []
for node, cost in costs.items():
  heapq.heappush(h, (cost, node))

ans = 0
visited = set()
while len(h) > 0:
  cost, node = heapq.heappop(h)
  if node in visited:
    continue

  visited.add(node)
  ans = max(ans, cost) 
  for x in g[node]:
    if x not in visited:
      costs[x] -= A[node]
      heapq.heappush(h, (costs[x], x))

print(ans)

