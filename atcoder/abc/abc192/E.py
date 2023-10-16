import heapq
import math

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)
    cost = [float('inf')] * N
    cost[s] = 0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:
            continue

        for d, u, k in edges[v]:
            extra = max(0, math.ceil(cost[v] / k) * k - cost[v])
            tmp = d + extra + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))

    return cost

N, M, X, Y = map(int,input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, k = map(int,input().split())
    a, b = a - 1, b - 1
    edges[a].append((t, b, k))
    edges[b].append((t, a, k))

ans = float('inf')
cost = dijkstra(X-1)
dist = cost[Y-1]
print(-1 if dist == float('inf') else dist)