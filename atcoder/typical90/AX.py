def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]

MOD = 10**9 + 7
N, L = (int(x) for x in input().split())
dp = make_array(N+1)
dp[0] = 1

for i in range(N):
  dp[i+1] += dp[i]
  if i+1 >= L:
    dp[i+1] += dp[i+1-L]

  dp[i+1] %= MOD

# print(dp)

print(dp[N])

  