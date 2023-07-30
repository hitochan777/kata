S = input()
def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

MOD = 998244353
N = len(S)
dp = make_array(N+1, N+1)
dp[0][0] = 1
for i in range(N):
  for j in range(N):
    if S[i] == "?":
      if dp[i][j] > 0 and j > 0:
        dp[i+1][j-1] += dp[i][j]
        dp[i+1][j-1] %= MOD

      dp[i+1][j+1] += dp[i][j]
      dp[i+1][j+1] %= MOD
    elif S[i] == "(":
      dp[i+1][j+1] += dp[i][j]
      dp[i+1][j+1] %= MOD
    else:
      if j > 0:
        dp[i+1][j-1] += dp[i][j]
        dp[i+1][j-1] %= MOD
# print(dp)
print(dp[N][0])