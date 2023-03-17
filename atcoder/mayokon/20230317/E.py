from collections import defaultdict
import heapq

INF = 10**18
def dijkstra(s, edges):
  cost = [INF] * N
  hq = []
  for node, c in edges[s]:
    hq.append((c, node))
    if cost[node] > c:
      cost[node] = c

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
g = defaultdict(list)
for i in range(M):
  A, B, C = (int(x) for x in input().split())
  A, B, = A-1, B-1
  g[A].append((B, C))

for i in range(N):
  cost = dijkstra(i, g)
  print(cost[i] if cost[i] < INF else -1)