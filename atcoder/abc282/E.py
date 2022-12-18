from atcoder.dsu import DSU

N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
scores = []
edges = []
for i in range(N):
  a = A[i]
  for j in range(i+1,N):
    b = A[j]
    score = (pow(a,b,M)+pow(b,a,M)) % M
    edges.append((score, i, j))

edges.sort(reverse=True)
dsu = DSU(N)
ans = 0
for score, i, j in edges:
  if dsu.same(i,j):
    continue

  dsu.merge(i,j)
  ans += score

print(ans)
