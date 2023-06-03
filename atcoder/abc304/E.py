from atcoder.dsu import DSU

N, M = (int(x) for x in input().split())
dsu = DSU(N)
for _ in range(M):
  u, v = (int(x)-1 for x in input().split())
  dsu.merge(u, v)

K = int(input())
ngs = set()
for _ in range(K):
  x, y = (int(x)-1 for x in input().split())
  x = dsu.leader(x)
  y = dsu.leader(y)
  ngs.add((min(x,y), max(x,y)))

Q = int(input())
for _ in range(Q):
  u, v = (int(x)-1 for x in input().split())
  u = dsu.leader(u)
  v = dsu.leader(v)
  if not dsu.same(u, v) and (min(u, v), max(u, v)) in ngs:
    print("No")
  else:
    print("Yes")


