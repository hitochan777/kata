from collections import defaultdict
import heapq

def dijkstra(s, edges):
  path = {}
  cost = [float('inf')] * N
  hq = []
  for node, c, n, i in edges[s]:
    hq.append((c, node))
    if cost[node] > c:
      path[node] = (n, i)
      cost[node] = c

  heapq.heapify(hq)
  while hq:
    c, v = heapq.heappop(hq)
    if c > cost[v]:
      continue

    for u, d, n, i in edges[v]:
      tmp = d + cost[v]
      if tmp < cost[u]:
        path[u] = (n, i)
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))

  return path

N, M = (int(x) for x in input().split())
g = defaultdict(list)
for i in range(M):
  A, B, C = (int(x) for x in input().split())
  A, B, = A-1, B-1
  g[A].append((B, C, A, i))
  g[B].append((A, C, B, i))

path = dijkstra(0, g)
edge_nums = set(i+1 for _, i in path.values())
print(*list(edge_nums))