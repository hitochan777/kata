N = int(input())
H = list(int(x) for x in input().split())
def make_array(*args):
  if len(args) == 0:
    return 10**18

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N)
dp[0] = 0

for i in range(N-1):
  dp[i+1] = min(dp[i+1], dp[i] + abs(H[i+1] - H[i]))
  if i > 0:
    dp[i+1] = min(dp[i+1], dp[i-1] + abs(H[i+1] - H[i-1]))

print(dp[N-1])