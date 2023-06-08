N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
MOD = 998244353
def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, B[-1]+1)
dp[0][0] = 1

for n in range(N):
  total = 0
  for k in range(A[n]):
    total += dp[n][k]
    total %= MOD

  for k in range(A[n], B[n]+1):
    total += dp[n][k]
    total %= MOD
    dp[n+1][k] = total

print(sum(dp[N]) % MOD)