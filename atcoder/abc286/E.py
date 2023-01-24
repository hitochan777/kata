N = int(input())
A = list(int(x) for x in input().split())
INF = 10**18
cost = [[(INF, 0)]*N for _ in range(N)]

for i in range(N):
  S = input()
  for j, c in enumerate(S):
    if c == "Y":
      cost[i][j] = (1, -A[j])
      
def wf(cost):
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if cost[i][k][0] != INF and cost[k][j][0] != INF:
          cost[i][j] = min(cost[i][j], (cost[i][k][0] + cost[k][j][0], cost[i][k][1] + cost[k][j][1]))

wf(cost)
Q = int(input())
for _ in range(Q):
  U, V = (int(x)-1 for x in input().split())
  dist, price = cost[U][V]
  if dist == INF:
    print("Impossible")
  else:
    print(dist, A[U] - price)