import math


N = int(input())

def dist(p1, p2):
  return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

pos = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  pos.append((X, Y))

dp = [[10**18] * N for _ in range(1<<N)]
dp[1][0] = 0
for s in range(1<<N):
  for i in range(N):
    if (s >> i) & 1 == 0:
      continue

    for j in range(N):
      dp[s|(1<<j)][j] = min(dp[s|1<<j][j], dp[s][i] + dist(pos[i], pos[j]))

print(dp[(1<<N)-1][0])