import sys
S = input()
N = len(S)
MOD = 10**9 + 7

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, 2)
dp[0][0] = 1
for i in range(N):
  a = dp[i][1]
  dp[i+1][1] = a * (1 if S[i] == "0" else 3)

  a = dp[i][0]
  dp[i+1][1] = a * (1 if S[i] == "1" else 0)
  dp[i+1][0] = a * (2 if S[i] == "1" else 1)

  dp[i+1][0] %= MOD
  dp[i+1][1] %= MOD

print(sum(dp[N]) % MOD)