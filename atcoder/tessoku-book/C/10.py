W = int(input())
dp = [0] * (W+1)
dp[1] = 12
MOD = 1000000007

for i in range(1,W):
  dp[i+1] = (dp[i] * 7) % MOD

print(dp[W])