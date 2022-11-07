from collections import defaultdict

N, M = (int(x) for x in input().split())
g = defaultdict(set)
for _ in range(M):
  U, V = (int(x)-1 for x in input().split())
  g[U].add(V)
  g[V].add(U)

cnt = 0
for a in range(N):
  for b in range(a+1,N):
    for c in range(b+1,N):
      if b in g[a] and c in g[b] and a in g[c]:
        cnt += 1

print(cnt)