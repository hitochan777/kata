from collections import defaultdict, deque

N, M = (int(x) for x in input().split())
g = defaultdict(set)
dist = defaultdict(lambda: defaultdict(int))
for _ in range(M):
    u, v = (int(x)-1 for x in input().split())
    g[u].add(v)
    g[v].add(u)

K = int(input())
constraints = []
for _ in range(K):
    p, d = (int(x) for x in input().split())
    p -= 1
    constraints.append((p, d))

for i in range(N):
    visited = set()
    q = deque()
    q.appendleft((i, 0))
    visited.add(i)
    dist[i][i] = 0
    while len(q) > 0:
      n, d = q.pop()
      dist[i][n] = d
      for nb in g[n]:
        if nb in visited:
           continue

        q.appendleft((nb, d+1))
        visited.add(nb)

for i in range(1<<N):
  whites = set()
  for j in range(N):
    if (i >> j) & 1 == 1:
      whites.add(j)

  for p, d in constraints:
    min_dist = 10**18

    for j in range(N):
      if j not in whites:

        min_dist = min(dist[p][j], min_dist)
        if i == 5:
          print(p, j, min_dist)

    if min_dist != d:
      break
  else:
    print("Yes")
    print("".join(["0" if i in whites else "1" for i in range(N)]))
    exit()

print("No")
