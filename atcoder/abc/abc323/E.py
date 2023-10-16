from functools import lru_cache
MOD = 998244353

@lru_cache(10000)
def divmod(a, b, mod):
  return (a * pow(b, mod-2,mod)) % mod

N, X = (int(x) for x in input().split())
# N, X = 1000, 10000
T = list(int(x) for x in input().split())
# T = [1] * N

dp = [0]*(X+1)
dp[0] = 1
for i in range(X+1):
  for t in T:
    if i-t>=0:
      dp[i] += divmod(dp[i-t], N, MOD)
      dp[i] %= MOD

# print("yeaj")

ans = 0
for i in range(min(X+1, T[0])):
  # print(dp[X-i])
  ans += divmod(dp[X-i], N, MOD)
  ans %= MOD

print(ans)
