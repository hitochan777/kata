from itertools import permutations
from collections import defaultdict

g = defaultdict(lambda: defaultdict(lambda: -10**18))
N, M = (int(x) for x in input().split())
for _ in range(M):
  A, B, C = (int(x) for x in input().split())
  g[A][B] = max(g[A][B], C)
  g[B][A] = max(g[B][A], C)

ans = 0
for p in permutations(range(1, N+1)):
  n = p[0]
  dist = 0
  for nb in p[1:]:
    if nb not in g[n]:
      continue

    dist += g[n][nb]
    ans = max(ans, dist)
    n = nb

print(ans)

