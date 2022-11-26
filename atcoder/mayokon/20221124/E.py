H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  S = input()
  g.append(S+"*")

g.append("*" * (W+1))

def f(c):
  if c == "+":
    return 1
  elif c == "-":
    return -1
  else:
    return 0

dp = [[0] * (W+1) for _ in range(H+1)]
for i in range(H-1, -1, -1):
  for j in range(W-1, -1, -1):
    cmp = max if (i + j) % 2 == 0 else min
    sign = 1 if (i+j) % 2 == 0 else -1
    dp[i][j] = cmp(dp[i+1][j] + sign*f(g[i+1][j]), dp[i][j+1] + sign*f(g[i][j+1]))

if dp[0][0] > 0:
  print("Takahashi")
elif dp[0][0] < 0:
  print("Aoki")
else:
  print("Draw")
