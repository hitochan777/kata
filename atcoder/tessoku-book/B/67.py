from atcoder.dsu import DSU
N, M = (int(x) for x in input().split())
edges = []
for _ in range(M):
  A, B, C = (int(x) for x in input().split())
  edges.append((C, A-1, B-1))


edges.sort(reverse=True)
dsu = DSU(N)
total = 0
for c, a, b in edges:
  if not dsu.same(a, b):
    dsu.merge(a, b)
    total += c

print(total)