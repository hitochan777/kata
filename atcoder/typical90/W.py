def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]


MOD = 10**9 + 7
H, W = (int(x) for x in input().split())
lines = []
for _ in range(H):
  lines.append(input())

dp = make_array(H+1, 1 << W)
dp[0][0] = 1

def is_ith_one(n, i):
  ith = (n >> i) & 1
  # print(i,ith)
  return ith == 1

for i in range(H):
  for j in range(1<<W):
    if dp[i][j] == 0:
      continue

    for k in range(1<<W):
      valid = True
      for l in range(W):
        if (is_ith_one(j, l) and is_ith_one(k, l)):
          valid = False
          break

        if (is_ith_one(j, l+1) and is_ith_one(k, l)):
          valid = False
          break

        if (is_ith_one(j, l) and is_ith_one(k, l+1)):
          valid = False
          break

        if is_ith_one(k, l) and is_ith_one(k, l+1):
          valid = False
          break

        if is_ith_one(k, l) and lines[i][l] == "#":
          valid = False
          break

      if valid:
          dp[i+1][k] += dp[i][j]
          dp[i+1][k] %= MOD

# print(dp)
print(sum(dp[H]))