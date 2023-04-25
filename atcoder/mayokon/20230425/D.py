import math
import heapq

INF = 10**18
def dijkstra(s):
  cost = [INF] * N
  hq = []
  for node, t, _ in edges[s]:
      hq.append((t, node))
      cost[node] = min(cost[node], t)

  heapq.heapify(hq)
  while hq:
      c, v = heapq.heappop(hq)
      if c > cost[v]:
          continue

      for u, t, k in edges[v]:
          # print((v, u, d, cost[v]))
          tmp = k * math.ceil(c / k) - c + t + cost[v]
          if tmp < cost[u]:
              cost[u] = tmp
              heapq.heappush(hq, (tmp, u))

  return cost

N, M, X, Y = map(int,input().split())
X -= 1
Y -= 1
edges = [set() for _ in range(N)]
for _ in range(M):
    a, b, t, k = map(int,input().split())
    a, b = a - 1, b - 1
    edges[a].add((b, t, k))
    edges[b].add((a, t, k))

ans = INF
cost = dijkstra(X)
dist = cost[Y]
print(-1 if dist == INF else dist)