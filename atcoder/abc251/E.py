N = int(input())
A = list(int(x) for x in input().split())
def make_array(*args, default=int):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N, 2)

dp[0][0] = 0
dp[0][1] = 10**18

for i in range(1,N):
  dp[i][0] = dp[i-1][1]
  dp[i][1] = min(dp[i-1][1], dp[i-1][0]) + A[i]

ans = dp[N-1][1]

dp = make_array(N, 2)

dp[0][0] = 10**18
dp[0][1] = A[0]

for i in range(1,N):
  dp[i][0] = dp[i-1][1]
  dp[i][1] = min(dp[i-1][1], dp[i-1][0]) + A[i]

ans = min(ans, dp[N-1][0], dp[N-1][1])
print(ans)