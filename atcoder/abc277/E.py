from collections import deque, defaultdict

N, M, K = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  u, v, a = (int(x) for x in input().split())
  g[u].append((v, a))
  g[v].append((u, a))

S = set(int(x) for x in input().split())

q = deque()
visited = set()
q.append((1, 0, 0))
visited.add((1, 0))
dist = [10**18] * (N+1)
while len(q) > 0:
  n, d, flipped = q.popleft()
  if n == N:
    dist[n] = d
    break

  for nb, a in g[n]:
    a ^= flipped
    if a == 0 and n not in S:
      continue

    f = flipped if a == 1 else not flipped
    if (nb, f) not in visited:
      q.append((nb,d+1,f))
      visited.add((n, f))


print(dist[N] if dist[N] < 10**18 else -1)
