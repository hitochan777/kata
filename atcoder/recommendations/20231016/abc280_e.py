N, P = (int(x) for x in input().split())
mod = 998244353

def divmod(a, b):
  # return a / b
  return (a * pow(b, mod-2,mod)) % mod

INF = 10**18
dp = [0] * (N+1)
dp[0] = 0

for i in range(1, N+1):
  dp[i] = (dp[i-1]+1)*(1-divmod(P, 100)+mod) + (dp[max(0, i-2)]+1)*(divmod(P, 100))
  dp[i] %= mod 

# print(dp)
print(dp[N])
