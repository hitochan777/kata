from atcoder.dsu import DSU
N, M = (int(x) for x in input().split())

edges = []
for _ in range(M):
  A, B = (int(x) for x in input().split())
  edges.append((A-1,B-1))


cnt = 0
for i in range(M):
  dsu = DSU(N)
  for j in range(M):
    if i == j:
      continue
    
    dsu.merge(edges[j][0],edges[j][1])

  if (len(dsu.groups()) > 1):
    cnt += 1

print(cnt)