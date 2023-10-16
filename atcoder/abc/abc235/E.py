from atcoder.dsu import DSU

N, M, Q = (int(x) for x in input().split())
edges = []
for i in range(M+Q):
  a, b, c = (int(x) for x in input().split()) 
  a, b = a-1, b-1
  edges.append((c, a, b, i))

dsu = DSU(N)
edges = sorted(edges)
result = [""] * Q
for w, u, v, l in edges:
  if l >= M:
    result[l-M] = not dsu.same(u, v)
  else: 
    dsu.merge(u, v)

for ok in result:
  if ok:
    print("Yes")
  else:
    print("No")