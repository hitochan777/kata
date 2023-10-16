N, M, K = (int(x) for x in input().split())
dp = [0] * (N+1)
dp[0] = 1
MOD = 998244353
mmod = pow(M, MOD-2, MOD)

ans = 0
for k in range(K):
  dp2 = [0] * (N+1)
  for i in range(N+1):
    for m in range(1, M+1):
      pos = i + m
      if pos > N:
        pos = N - (pos - N)

      dp2[pos] += dp[i] * mmod
      dp2[pos] %= MOD

  # print(dp2)
  dp = dp2
  ans = (ans + dp[N]) % MOD
  dp[N] = 0

print(ans)