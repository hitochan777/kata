def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

MOD = 10**9+7

def solve():
  K = int(input())
  if K % 9 != 0:
    return 0

  dp = [0] * (K+1)
  dp[0] = 1
  for i in range(K+1):
    for j in range(1,min(i+1,10)):
      dp[i] += dp[i-j]
      dp[i] %= MOD

  return dp[K]

print(solve())