import heapq
from collections import defaultdict

def dijkstra(s, edges):
  cost = [float('inf')] * N
  cost[s] = 0
  hq = []
  for node, c in edges[s]:
    hq.append((c, node))
    if cost[node] > c:
      cost[node] = c

  heapq.heapify(hq)
  while len(hq) > 0:
    c, v = heapq.heappop(hq)
    if c > cost[v]:
      continue

    for u, d in edges[v]:
      tmp = d + cost[v]
      if tmp < cost[u]:
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))

  return cost

N, M, T = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
g = defaultdict(list)
ig = defaultdict(list)
for _ in range(M):
  a, b, c = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append((b, c))
  ig[b].append((a, c))

cost = dijkstra(0, g)
icost = dijkstra(0, ig)
# print(cost)
# print(icost)
ans = 0
for c, ic, a in zip(cost, icost, A):
  if c == float('inf') or ic == float('inf'):
    continue

  rem = max(0, T-c-ic)
  ans = max(ans, rem * a)

print(ans)