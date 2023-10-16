def make_array(*args, default=int):
  if len(args) == 0:
    return 10**6

  return [make_array(*args[1:]) for _ in range(args[0])]

N = int(input())
MAX_NUM = 302
X, Y = (int(x) for x in input().split())
dp = make_array(N+1,MAX_NUM,MAX_NUM)
dp[0][0][0] = 0

li = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  li.append((A, B))

for i in range(N):
  for x in range(MAX_NUM):
    for y in range(MAX_NUM):
      dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])
      xd, yd = li[i]
      xt, yt = min(MAX_NUM-1, x + xd), min(MAX_NUM-1, y + yd)
      dp[i+1][xt][yt] = min(dp[i+1][xt][yt], dp[i][xt][yt], dp[i][x][y] + 1)

# for i in range(N+1):
#   print(dp[i])

min_val = 10**6
for x in range(X, MAX_NUM):
  for y in range(Y, MAX_NUM):
    min_val = min(min_val, dp[N][x][y])

print(-1 if min_val == 10**6 else min_val)

