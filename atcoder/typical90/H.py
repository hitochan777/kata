N = int(input())
S = input()
pattern = "atcoder"
M = len(pattern)

MOD = 10**9 + 7
dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(N+1):
  dp[i][0] = 1

for i in range(1,N+1):
  for j in range(1,M+1):
    dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if S[i-1] == pattern[j-1] else 0)
    dp[i][j] %= MOD

print(dp[N][M])
