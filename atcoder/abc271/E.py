from bisect import bisect_left
from collections import defaultdict
import heapq

def dijkstra(s, edges, t, indices):
  cost = [float('inf')] * N
  hq = []
  for idx, node, c in edges[s]:
    i = bisect_left(indices[idx], 0)
    if i >= len(indices[idx]):
      continue

    hq.append((c, node, indices[idx][i]+1))
    if cost[node] > c:
      cost[node] = c

  heapq.heapify(hq)
  while hq:
    c, v, i = heapq.heappop(hq)
    if c > cost[v]:
      continue

    for idx, u, d in edges[v]:
      j = bisect_left(indices[idx], i)
      if j >= len(indices[idx]):
        continue

      tmp = d + cost[v]
      if tmp < cost[u]:
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u, indices[idx][j]+1))

  return cost[t]

N, M, K = (int(x) for x in input().split())
g = defaultdict(list)
for i in range(M):
  A, B, C = (int(x) for x in input().split())
  A -= 1
  B -= 1
  g[A].append((i, B, C))
  g[B].append((i, A, C))

E = list(int(x)-1 for x in input().split())
indices = defaultdict(list)
for i, k in enumerate(E):
  indices[k].append(i)

cost = dijkstra(0, g, N-1, indices)
if cost == float('inf'):
  print(-1)
else:
  print(cost)