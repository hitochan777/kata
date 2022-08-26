from atcoder.dsu import DSU

N, M = (int(x) for x in input().split())
dsu = DSU(N)
P = list(int(x)-1 for x in input().split())
for _ in range(M):
  x, y = (int(x)-1 for x in input().split())
  dsu.merge(x, y)

ans = 0
for group in dsu.groups():
  s = set(group)
  ps = set(P[i] for i in s)
  ans += len(s.intersection(ps))

print(ans)
