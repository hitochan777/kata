from collections import defaultdict, Counter
from atcoder.dsu import DSU

incoming = defaultdict(int)
N, M = (int(x) for x in input().split())
dsu = DSU(N)
if M != N-1:
  print("No")
  exit()

for _ in range(M):
  u, v = (int(x)-1 for x in input().split())
  incoming[u] += 1
  incoming[v] += 1
  dsu.merge(u, v)

cnt = Counter(incoming.values())
if cnt[2] == N-2 and cnt[1] == 2 and len(dsu.groups()) == 1:
  print("Yes")
else:
  print("No")