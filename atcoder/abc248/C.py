N, M, K = (int(x) for x in input().split())

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

MOD = 998244353

dp = make_array(N+1, N*M+1)
dp[0][0] = 1
for i in range(1,N+1):
  for j in range(N*M+1):
    for k in range(1,M+1):
      if j + k > K:
        break

      dp[i][j+k] += dp[i-1][j]
      dp[i][j+k] %= MOD

print(sum(dp[N]) % MOD)