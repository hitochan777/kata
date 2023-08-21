from itertools import combinations

MOD = 10**9 + 7
N = int(input())
dp = [[0] * (1<<2) for _ in range(2)]
dp[0][0] = 1

for i in range(N):
  dp[(i+1)%2] = [0] * (1<<2)
  dp[(i+1)%2][0] += dp[i%2][0] * 8
  dp[(i+1)%2][1] += dp[i%2][0] * 1
  dp[(i+1)%2][2] += dp[i%2][0] * 1

  dp[(i+1)%2][1] += dp[i%2][1] * 9
  dp[(i+1)%2][3] += dp[i%2][1] * 1

  dp[(i+1)%2][2] += dp[i%2][2] * 9
  dp[(i+1)%2][3] += dp[i%2][2] * 1

  dp[(i+1)%2][3] += dp[i%2][3] * 10
  for j in range(1<<2):
    dp[(i+1)%2][j] %= MOD

print(dp[N%2][3])