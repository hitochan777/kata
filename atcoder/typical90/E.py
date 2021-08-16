N, B, K = (int(x) for x in input().split())
C = list(int(x) for x in input().split())

MOD = 10**9 + 7
dp = [[0] * B for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
  for b in range(B):
    for k in range(K):
      new_b = (b * 10 + C[k])%B
      dp[i+1][new_b] += dp[i][b]
      dp[i+1][new_b] %= MOD

print(dp[N][0])
