N = int(input())
dp = [[0] * 2 for _ in range(N)]
nums = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  nums.append([A,B])

dp[0] = [1, 1]
MOD = 998244353
for i in range(N-1):
  for j in range(2):
    if nums[i+1][j] != nums[i][0]:
      dp[i+1][j] += dp[i][0]

    if nums[i+1][j] != nums[i][1]:
      dp[i+1][j] += dp[i][1]

    dp[i+1][j] %= MOD

print(sum(dp[N-1]) % MOD)