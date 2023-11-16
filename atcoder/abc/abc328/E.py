from atcoder.dsu import DSU
from collections import defaultdict
from itertools import combinations

N, M, K = (int(x) for x in input().split())

edges = []
for _ in range(M):
  u, v, w = (int(x) for x in input().split())
  u, v = u-1, v-1
  edges.append((u,v,w))

ans = 10**18
for comb in combinations(range(M), N-1):
  dsu = DSU(N)
  for ei in comb:
    a, b, _ = edges[ei]
    if dsu.same(a, b):
      break

    dsu.merge(a, b)
  else:
    if len(dsu.groups()) == 1:
      s = sum(edges[ei][2] for ei in comb) % K
      ans = min(s, ans)

print(ans)

