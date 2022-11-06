from collections import defaultdict, deque
N, T = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  g[A].append(B)
  g[B].append(A)

q = deque()
q.append((T, 0))
visited = set()
dist = defaultdict(int)
while len(q) > 0:
  n, d = q.popleft()
  visited.add(n)
  dist[n] = d
  for nb in g[n]:
    if nb in visited:
      continue

    q.append((nb, d+1))
    visited.add(nb)

rank = [0] * (N+1)
for _, n in sorted([(v, k) for k, v in dist.items()], reverse=True):
  max_val = 0
  for child in g[n]:
    max_val = max(max_val, rank[child])

  rank[n] = max_val + 1
  
print(*[r-1 for r in rank[1:]])
