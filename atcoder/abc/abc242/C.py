N = int(input())
MOD = 998244353
def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, 11)

for i in range(1,10):
  dp[1][i] = 1

for i in range(1,N):
  for j in range(1,10):
    dp[i+1][j] += dp[i][j]
    dp[i+1][j] %=  MOD
    dp[i+1][j] += dp[i][j-1] 
    dp[i+1][j] %=  MOD
    dp[i+1][j] += dp[i][j+1]
    dp[i+1][j] %=  MOD

total = sum(dp[N][i] for i in range(1,10))
total %= MOD
print(total)