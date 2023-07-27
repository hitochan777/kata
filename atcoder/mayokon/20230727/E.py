from collections import defaultdict
import heapq

INF = 10**18
def dijkstra(s, edges):
  cost = [INF] * N
  hq = []
  for u, c in edges[s]:
    hq.append((c, u))
    if cost[u] > c:
      cost[u] = c

  heapq.heapify(hq)
  while hq:
    c, v = heapq.heappop(hq)
    if c > cost[v]:
      continue

    for u, d in edges[v]:
      tmp = d + cost[v]
      if tmp < cost[u]:
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))

  return cost

N, M = (int(x) for x in input().split())
edges = defaultdict(set)
for _ in range(M):
  A, B, C = (int(x) for x in input().split())
  A, B = A-1, B-1
  edges[A].add((B, C))

for i in range(N):
  costs = dijkstra(i, edges)
  if costs[i] == INF:
    print(-1)
  else:
    print(costs[i])
