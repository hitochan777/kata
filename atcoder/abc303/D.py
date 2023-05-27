X, Y, Z = (int(x) for x in input().split())
S = input()
def make_array(*args, default=int):
  if len(args) == 0:
    return 10**18

  return [make_array(*args[1:]) for _ in range(args[0])]

N = len(S)
dp = make_array(N+1, 2)
dp[0][0] = 0
for i in range(N):
  if S[i] == "a":
    dp[i+1][0] = min(dp[i][0]+X, dp[i][1]+X+Z, dp[i][1]+Y+Z)
    dp[i+1][1] = min(dp[i][0]+X+Z,dp[i][0]+Y+Z,dp[i][1]+Y)
  else:
    dp[i+1][0] = min(dp[i][0]+Y, dp[i][1]+X+Z, dp[i][1]+Y+Z)
    dp[i+1][1] = min(dp[i][0]+X+Z, dp[i][0]+Y+Z, dp[i][1] + X)

print(min(dp[N]))