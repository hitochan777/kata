from atcoder.dsu import DSU
from collections import defaultdict

N, M = (int(x) for x in input().split())
dsu = DSU(N)
g = defaultdict(int)
for i in range(M):
    u, v = (int(x)-1 for x in input().split())
    g[u] += 1
    g[v] += 1
    dsu.merge(u, v)

for group in dsu.groups():
  node_num = len(group)
  cnt = 0
  for node in group:
    cnt += g[node]

  cnt //= 2
  if cnt != node_num:
    print("No")
    exit()

print("Yes")
     
