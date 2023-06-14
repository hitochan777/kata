N, K, D = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
def make_array(*args):
  if len(args) == 0:
    return -10**18

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, K+1, D)
dp[0][0][0] = 0

for i in range(N):
  for k in range(K+1):
    for m in range(D):
      dp[i+1][k][m] = max(dp[i+1][k][m], dp[i][k][m])
      if k + 1 <= K:
        dp[i+1][k+1][(m+A[i]) % D] = max(dp[i+1][k+1][(m+A[i]) % D], dp[i][k][m] + A[i])

print(dp[N][K][0] if dp[N][K][0] >= 0 else -1)