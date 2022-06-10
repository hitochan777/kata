from collections import defaultdict, deque

g = defaultdict(list)
N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
for _ in range(M):
  a, b = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append(b)

q = deque()
for i in range(N):
  q.append((i, A[i], A[i], -10**18))

while len(q) > 0:
  node, mn, mx, cost = q.pop()
  for nb in g[node]:
    pass