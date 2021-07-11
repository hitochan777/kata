N, Q = map(int,input().split())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    a, b = a - 1, b - 1
    edges[b].append(a)
    edges[a].append(b)

q = [(0, False)]
colors = [False] * N
visited = set()
while len(q) > 0:
  node = q.pop(0)
  colors[node[0]] = node[1]
  visited.add(node[0])
  for ne in edges[node[0]]:
    if ne in visited:
      continue

    q.append((ne, not node[1]))

for _ in range(Q):
  c, d = map(int,input().split())
  c, d = c - 1, d - 1
  print("Town" if colors[c] == colors[d] else "Road")