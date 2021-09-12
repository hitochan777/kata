from atcoder.dsu import DSU
N, M = (int(x) for x in input().split())
edges = []
cost = 0
for _ in range(M):
  A, B, C = (int(x) for x in input().split())
  edges.append((C, A-1, B-1))
  if C > 0:
    cost += C

edges.sort()

dsu = DSU(N)

for c, a, b in edges:
  if not dsu.same(a, b):
    dsu.merge(a, b)
    if c > 0:
      cost -= c

print(cost)