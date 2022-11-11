N = int(input())

dp = [[0] * 4 for _ in range(N+1)]
dp[0][0] = 1
MOD = 10**9+7

for i in range(N):
  dp[i+1][0] += dp[i][0] * 8
  dp[i+1][0] %= MOD
  dp[i+1][1] += dp[i][0] + dp[i][1] * 9
  dp[i+1][1] %= MOD
  dp[i+1][2] += dp[i][0] + dp[i][2] * 9
  dp[i+1][2] %= MOD
  dp[i+1][3] += dp[i][1] + dp[i][2] + dp[i][3] * 10
  dp[i+1][3] %= MOD

print(dp[N][3])