N = int(input())
A = list(int(x) for x in input().split())

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

MOD = 998244353

dp = make_array(N-1, 10)
dp[0][(A[0] + A[1]) % 10] += 1
dp[0][(A[0] * A[1]) % 10] += 1

for i in range(N-2):
  for d in range(10):
    plus = (d * A[i+2]) % 10
    mult = (d + A[i+2]) % 10
    dp[i+1][mult] += dp[i][d]
    dp[i+1][mult] %= MOD
    dp[i+1][plus] += dp[i][d]
    dp[i+1][plus] %= MOD

for d in range(10):
  print(dp[N-2][d] % MOD)