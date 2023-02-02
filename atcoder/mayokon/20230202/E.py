N, M, Q = (int(x) for x in input().split())
g = [[0]*N for _ in range(N)]
for _ in range(M):
  L, R = (int(x)-1 for x in input().split())
  g[L][R] += 1

for i in range(N):
  for j in range(1,N):
    g[i][j] += g[i][j-1]

for i in range(1,N):
  for j in range(N):
    g[i][j] += g[i-1][j]

for _ in range(Q):
  p, q = (int(x)-1 for x in input().split())
  if p == 0:
    print(g[-1][q])
  else:
    print(g[-1][q] - g[p-1][q])
