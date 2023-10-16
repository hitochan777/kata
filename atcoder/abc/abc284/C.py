from atcoder.dsu import DSU
N, M = (int(x) for x in input().split())
dsu = DSU(N)
for _ in range(M):
  u, v = (int(x)-1 for x in input().split())
  dsu.merge(u,v)

print(len(dsu.groups()))
