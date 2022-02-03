from email.policy import default
from heapq import heapify, heappop, heappush
from collections import defaultdict
N, M = (int(x) for x in input().split())
H = list(int(x) for x in input().split())

g = defaultdict(lambda: defaultdict(int))
d = defaultdict(lambda: 10**18)
c = defaultdict(int)
d[0] = 0
q = [(0, 0)]
for _ in range(M):
  U, V = (int(x) for x in input().split())
  U, V = U-1, V-1
  diff = abs(H[U] - H[V])
  g[U][V] = diff
  g[V][U] = diff

while len(q) > 0:
  c, u = heappop(q)
  for v in g[u].keys():
    if c + g[u][v] < d[v]:
      d[v] = c + g[u][v]
      heappush(q, (d[v], v))

ans = max((3 * (H[0] - H[v]) - c ) >> 1 for v, c in d.items())
print(ans)