N = int(input())

def make_array(*args):
  if len(args) == 0:
    return 10**18

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1)
dp[0] = 0

for i in range(N):
  if i + 1 <= N:
    dp[i+1] = min(dp[i] + 1, dp[i+1])

  j = 6
  while i + j <= N:
    dp[i+j] = min(dp[i+j], dp[i] + 1)
    j *= 6

  j = 9
  while i + j <= N:
    dp[i+j] = min(dp[i+j], dp[i] + 1)
    j *= 9

print(dp[N])