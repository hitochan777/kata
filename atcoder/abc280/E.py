MOD = 998244353
def divmod(a, b, mod):
  return (a * pow(b, mod-2,mod)) % mod

N, P = (int(x) for x in input().split())
dp = [0] * (N+2)

normal = divmod(100-P,100,MOD)
critical = divmod(P,100,MOD)
for i in range(1,N+2):
  dp[i] = (dp[max(i-1,0)]*normal + dp[max(i-2,0)]*critical)+1 
  dp[i] %= MOD

  
print(dp[N])
