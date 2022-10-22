def dist(p1, p2):
  return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

pos = [(0,0)]
N, M = (int(x) for x in input().split())
for _ in range(N+M):
  X, Y = (int(x) for x in input().split())
  pos.append((X, Y))

N += 1

dp = [[10**18]*(1<<(N+M)) for _ in range(N+M)]
dp[0][1] = 0
for s in range(1<<(N+M)):
  speed = 1
  for i in range(N, N+M):
    if (s >> i) & 1 == 1:
      speed *= 2

  for i in range(N+M):
    if (s >> i) & 1 == 0:
      continue

    for j in range(N+M):
      dp[j][s|(1<<j)] = min(dp[j][s|1<<j], dp[i][s] + dist(pos[i], pos[j]) / speed)

ans = 10**18
for i in range(1<<M):
  ans = min(ans, dp[0][(i<<N)+(1<<N)-1])

print(ans)