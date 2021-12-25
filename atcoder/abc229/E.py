from collections import defaultdict
from atcoder.dsu import DSU

N, M = (int(x) for x in input().split())
g = defaultdict(set)
dsu = DSU(N)
cnt = 0
for _ in range(M):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  g[A].add(B)

ans = [0]
for i in range(N-1, -1, -1):
  cnt += 1
  for nb in g[i]:
    if not dsu.same(i, nb):
      dsu.merge(nb, i)
      cnt -= 1

  ans.append(cnt)

for val in ans[::-1][1:]:
  print(val)