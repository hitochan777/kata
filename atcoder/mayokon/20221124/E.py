INF = 10**18
H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  S = input()
  g.append(S)

def f(c):
  if c == "+":
    return 1
  else:
    return -1

dp = [[0] * W for _ in range(H)]
for i in range(H-1, -1, -1):
  for j in range(W-1, -1, -1):
    if i == H-1 and j == W-1:
      continue

    cmp = max if (i + j) % 2 == 0 else min
    sign = 1 if (i+j) % 2 == 0 else -1
    # print(dp[i+1][j], sign, f(g[i+1][j]), dp[i][j+1], sign, f(g[i][j+1]))
    dp[i][j] = -INF if (i+j) % 2 == 0 else INF
    if i+1 < H:
      dp[i][j] = cmp(dp[i][j], dp[i+1][j] + sign*f(g[i+1][j]))
    if j+1 < W:
      dp[i][j] = cmp(dp[i][j], dp[i][j+1] + sign*f(g[i][j+1]))

# print(dp)

if dp[0][0] > 0:
  print("Takahashi")
elif dp[0][0] < 0:
  print("Aoki")
else:
  print("Draw")
