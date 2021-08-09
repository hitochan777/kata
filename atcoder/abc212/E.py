from collections import defaultdict

N, M , K = (int(x) for x in input().split())
graph = defaultdict(list)
for _ in range(M):
  U, V = (int(x) for x in input().split())
  graph[U].append(V)
  graph[V].append(U)

dp = [[0] * N for _ in range(K+1)]
dp[0][0] = 1

for day in range(K):
  s = sum(dp[day])
  for nxt in range(N):
    dp[day+1][nxt] = s - dp[day][nxt]
    dp[day+1][nxt] = s - sum(dp[day][node] for node in graph[nxt])

print(dp[K][0])