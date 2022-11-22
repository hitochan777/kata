from collections import defaultdict, deque

N, X, Y = (int(x) for x in input().split())
X, Y = X-1, Y-1
g = defaultdict(list)
for i in range(N-1):
  g[i].append(i+1)
  g[i+1].append(i)

g[X].append(Y)
g[Y].append(X)

dist = defaultdict(lambda: set())
for i in range(N):
  q = deque()
  visited = set()
  q.append((i,0))
  visited.add(i)
  while len(q) > 0:
    n, d = q.popleft()
    if d > 0:
      dist[d].add((min(i, n), max(i, n)))

    for nb in g[n]:
      if nb in visited:
        continue

      visited.add(nb)
      q.append((nb, d+1))

for k in range(1,N):
  print(len(dist[k]))



