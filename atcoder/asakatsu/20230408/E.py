from atcoder.dsu import DSU
N, Q = (int(x) for x in input().split())
dsu = DSU(N+1)
for _ in range(Q):
    l, r = (int(x) for x in input().split())
    dsu.merge(l-1, r)

if dsu.same(0, N):
    print("Yes")
else:
    print("No")
