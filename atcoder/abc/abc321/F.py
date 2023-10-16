Q, K = (int(x) for x in input().split())
dp = [0] * (K+1)
dp[0] = 1
MOD = 998244353 
for q in range(Q):
  sign, n = input().split()
  x = int(n)
  if sign == "+":
    for i in range(K,x-1,-1):
      dp[i] += dp[i-x]
      dp[i] %= MOD
  else:
    for i in range(x, K+1):
      dp[i] -= dp[i-x]
      dp[i] %= MOD

  print(dp[K])
