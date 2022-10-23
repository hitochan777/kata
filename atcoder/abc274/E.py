def dist(p1, p2):
  return (((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)) ** 0.5

pos = [(0,0)]
N, M = (int(x) for x in input().split())
for _ in range(N+M):
  X, Y = (int(x) for x in input().split())
  pos.append((X, Y))

N += 1

INF = 10**20

speeds = [1]*(1<<M)
for s in range(1<<M):
  speed = 1
  for i in range(M):
    if (s >> i) & 1 == 1:
      speed *= 2
  
  speeds[s] = speed

dp = [[INF]*(1<<(N+M)) for _ in range(N+M)]
dp[0][1] = 0
for s in range(1<<(N+M)):
  speed = speeds[s>>N]
  for i in range(N+M):
    if dp[i][s] == INF:
      continue

    if not (s >> i) & 1:
      continue

    for j in range(N+M):
      if j != 0 and (s >> j) & 1:
        continue

      dp[j][s|(1<<j)] = min(dp[j][s|1<<j], dp[i][s] + dist(pos[i], pos[j]) / speed)

ans = INF 
for i in range(1<<M):
  ans = min(ans, dp[0][(i<<N)+(1<<N)-1])

print(ans)