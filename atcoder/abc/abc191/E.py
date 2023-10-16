import heapq

def dijkstra(s):
    cost = [float('inf')] * N
    hq = []
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

N, M = map(int,input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int,input().split())
    a, b = a - 1, b - 1
    edges[a].append((b, c))

for i in range(N):
    ans = float('inf')
    cost = dijkstra(i)
    dist = cost[i]
    print(-1 if dist == float('inf') else dist)