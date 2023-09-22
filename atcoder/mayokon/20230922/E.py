def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

N = input()
K = int(input())
if len(N) < K:
  print(0)
  exit()

dp = make_array(len(N)+1, 2, K+1)
dp[0][0][0] = 1
for i in range(len(N)):
  for k in range(K+1):
    dp[i+1][1][k] += dp[i][1][k]
    if k < K:
      dp[i+1][1][k+1] += dp[i][1][k] * 9

    if N[i] == "0":
      dp[i+1][0][k] += dp[i][0][k]
    else:
      if k < K:
        dp[i+1][0][k+1] += dp[i][0][k]

    if k < K:
      dp[i+1][1][k+1] += dp[i][0][k] * max(0, int(N[i])-1)

    if int(N[i]) > 0:
      dp[i+1][1][k] += dp[i][0][k]

print(dp[len(N)][0][K] + dp[len(N)][1][K])
