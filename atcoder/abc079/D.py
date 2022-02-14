def floydWarshall(graph, N):
  dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  return dist


H, W = (int(x) for x in input().split())
graph = []
for i in range(10):
  cs = list(int(x) for x in input().split())
  graph.append(cs)

dist = floydWarshall(graph, 10)

total = 0
for i in range(H):
  A = list(int(x) for x in input().split())
  for a in A:
    if a == -1:
      continue

    total += dist[a][1]

print(total)
  