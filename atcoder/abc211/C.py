MOD = 10**9 + 7
S = input()
p = "chokudai"
dp = [[0] * (len(p) + 1) for _ in range(len(S)+1)]

for i in range(len(S)+1):
  dp[i][0] = 1

for i in range(1, len(S)+1):
  for j in range(1, len(p)+1):
    dp[i][j] = (dp[i-1][j] + (dp[i-1][j-1] if p[j-1] == S[i-1] else 0)) % MOD

print(dp[len(S)][len(p)])

