from collections import defaultdict

N, M, K = (int(x) for x in input().split())
graph = defaultdict(list)
for _ in range(M):
  U, V = (int(x) for x in input().split())
  graph[U-1].append(V-1)
  graph[V-1].append(U-1)

dp = [[0] * N for _ in range(K+1)]
dp[0][0] = 1

for day in range(K):
  s = sum(dp[day])
  for nxt in range(N):
    dp[day+1][nxt] = (s - dp[day][nxt] - sum(dp[day][node] for node in graph[nxt])) % 998244353


print(dp[K][0])