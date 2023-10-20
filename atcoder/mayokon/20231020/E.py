H, W, K = (int(x) for x in input().split())
x1, y1, x2, y2 = (int(x) for x in input().split())

dp = [0, 0, 0, 0] # other, same row, same col, same
idx = 0
if x1 == x2:
  idx += 1 << 0
if y1 == y2:
  idx += 1 << 1

dp[idx] = 1

MOD = 998244353
for i in range(K):
  a = [0] * 4
  a[0] += dp[0] * (H-2 + W-2)
  a[1] += dp[0]
  a[2] += dp[0]

  a[0] += dp[1] * (H-1)
  a[1] += dp[1] * (W-2)
  a[3] += dp[1]

  a[0] += dp[2] * (W-1)
  a[2] += dp[2] * (H-2)
  a[3] += dp[2]

  a[1] += dp[3] * (W-1)
  a[2] += dp[3] * (H-1)

  for i in range(4):
    a[i] %= MOD

  dp = a

print(dp[3])