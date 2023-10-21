from collections import defaultdict
import heapq

def dijkstra(s, edges, N):
  path = {}
  cost = [float('inf')] * N
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


g = defaultdict(list)
N, A, B, C = (int(x) for x in input().split())
for i in range(N):
  D = list(int(x) for x in input().split())
  for j, d in enumerate(D):
    g[i].append((j, d * A))
    g[i+N].append((j+N, d * B + C))
    g[i].append((i+N, 0))

cost = dijkstra(0, g, 2*N)
print(min(cost[N-1], cost[2*N-1]))



