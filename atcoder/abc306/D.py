def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

N = int(input())
dishes = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  dishes.append((X, Y))

dp = make_array(N+1, 3)
for i in range(N):
  dp[i+1][0] = dp[i][0]
  dp[i+1][1] = dp[i][1]
  X, Y = dishes[i]
  if X == 0:
    dp[i+1][0] = max(dp[i+1][0], dp[i][0] + Y, dp[i][1] + Y)
  else:
    dp[i+1][1] = max(dp[i+1][1], dp[i][0] + Y)

print(max(dp[N]))
