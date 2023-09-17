from collections import defaultdict, deque

N, M = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  A, B, X, Y = (int(x) for x in input().split())
  A -= 1
  B -= 1
  g[A].append((B, X, Y))
  g[B].append((A, -X, -Y))

X = [None] * N
Y = [None] * N
X[0] = 0
Y[0] = 0
q = deque()
q.appendleft(0)
visited = set()
while q:
  n = q.pop()
  for nb, x, y in g[n]:
    if nb in visited:
      continue

    q.appendleft(nb)
    visited.add(nb)
    X[nb] = X[n] + x
    Y[nb] = Y[n] + y

for i in range(N):
  if X[i] is None:
    print("undecidable")
  else:
    print(X[i], Y[i])

  

