import heapq

def dijkstra(s):
  path = {}
  cost = [float('inf')] * N
  hq = []
  for node, c, n in edges[s]:
    hq.append((c, node))
    if cost[node] > c:
      path[node] = n
      cost[node] = c

  heapq.heapify(hq)
  while hq:
    c, v = heapq.heappop(hq)
    if c > cost[v]:
      continue

    for u, d, n in edges[v]:
      tmp = d + cost[v]
      if tmp < cost[u]:
        path[u] = n
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))

  return path

N, M = map(int,input().split())
edges = [[] for _ in range(N)]
for i in range(M):
  a, b, c = map(int,input().split())
  a, b = a - 1, b - 1
  edges[a].append((b, c, i))
  edges[b].append((a, c, i))

used = set() 
for i in range(N):
  path = dijkstra(i)
  for n in path.values():
    used.add(n)

edges = [(u,c,n)for u, c, n in edges if n in used]

print(M - len(used))