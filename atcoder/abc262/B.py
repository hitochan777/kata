from collections import defaultdict

N, M = (int(x) for x in input().split())
g = defaultdict(set)
for _ in range(M):
  u, v = (int(x) for x in input().split())
  g[v].add(u)
  g[u].add(v)

cnt = 0
for a in range(1, N+1):
  for b in range(a+1, N+1):
    for c in range(b+1, N+1):
      if b in g[a] and c in g[b] and a in g[c]:
        cnt += 1

print(cnt)