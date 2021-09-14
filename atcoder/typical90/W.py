def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]

def only_one_bit(n):
  return n and (n & (n-1) == 0)


MOD = 10**9 + 7
H, W = (int(x) for x in input().split())
lines = []
for _ in range(H):
  lines.append(input())

dp = make_array(H+1, 1 << W)
dp[0][0] = 1

for i in range(H):
  for j in range(1<<W):
    if dp[i][j] == 0:
      continue

    for k in range(1<<W):
      if k == j or ((k - j) & j == 0 and only_one_bit(k - j)):
        dp[i+1][k] += dp[i][j]
        dp[i+1][k] %= MOD

print(dp)
print(sum(dp[H]))