N = int(input())
A = list(int(x) for x in input().split())
cost = [[INF]*N for _ in range(N)]

for _ in range(N):
  S = input()

INF = 10**18
def wf(cost):
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if cost[i][k] != INF and cost[k][j] != INF:
          cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


