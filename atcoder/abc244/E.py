from collections import defaultdict
MOD = 998244353
N, M, K, S, T, X = (int(x) for x in input().split())
g = defaultdict(list)
for _ in range(M):
  U, V = (int(x) for x in input().split())
  U, V = U-1, V-1
  g[U].append(V)
  g[V].append(U)

prev = defaultdict(int)
for i in range(K):
  d = defaultdict(int)
  for i in range(N):
    for nb in g[i]:
      d[i] += prev[i]
      d[i] %= MOD

  prev = d
