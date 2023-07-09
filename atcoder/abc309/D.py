import heapq
from collections import defaultdict

INF = 10**18
def dijkstra(s, edges, N):
    cost = [INF] * N
    hq = []
    cost[s] = 0
    for node, c in edges[s]:
        hq.append((c, node))
        cost[node] = min(cost[node], c)

    heapq.heapify(hq)
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:
            continue

        for u, d in edges[v]:
            # print((v, u, d, cost[v]))
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))

    return cost

N1, N2, M = (int(x) for x in input().split())
edges = defaultdict(set)
for _ in range(M):
  a, b = (int(x)-1 for x in input().split())
  edges[a].add((b,1))
  edges[b].add((a,1))

c1 = dijkstra(0, edges, N1+N2)
# print(c1)
c2 = dijkstra(N1+N2-1, edges, N1+N2)
# print(c2)
d1 = max(v for v in c1 if v < INF)
d2 = max(v for v in c2 if v < INF)
# print(d1, d2)
print(d1+d2+1)


