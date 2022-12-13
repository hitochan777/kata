N = int(input())

dp = [10**18] * (N+1)
dp[0] = 0
for i in range(1,N+1):
  dp[i] = dp[i-1] + 1
  k = 1
  while True:
    j = i-6**k
    if j < 0:
      break

    dp[i] = min(dp[i], dp[j]+1)
    k += 1

  k = 1
  while True:
    j = i-9**k
    if j < 0:
      break

    dp[i] = min(dp[i], dp[j]+1)
    k += 1


print(dp[N])
