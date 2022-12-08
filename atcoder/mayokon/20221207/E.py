from itertools import permutations

N, M, R = (int(x) for x in input().split())
INF = 10**18
cost = [[INF] * N for _ in range(N)]
r = [int(x)-1 for x in input().split()]
for _ in range(M):
  A, B, C = (int(x) for x in input().split())
  A, B = A-1,B-1
  cost[A][B] = C
  cost[B][A] = C

for k in range(N):
  for i in range(N):
    for j in range(N):
      if cost[i][k]!=INF and cost[k][j]!=INF:
        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

ans = INF
for p in permutations(range(R)):
  total = 0
  for i in range(R-1):
    total += cost[r[p[i]]][r[p[i+1]]]

  ans = min(ans, total)

print(ans)


    
  