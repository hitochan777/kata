MOD = 998244353
def divmod(a, b):
  # return a/b
  return (a * pow(b, MOD-2,MOD)) % MOD

N = int(input())
A = list(int(x) for x in input().split())
dp = [0] * (N+1)

acc = [0]
for a in A:
  acc.append(acc[-1]+a)

sub_dp_sum = 0
for x in range(N-1, -1, -1):
  dp[x] = (divmod(1, N) * ((acc[-1] - acc[x]) + sub_dp_sum)) % MOD
  # dp[x] = (divmod(1, N) * ((acc[-1] - acc[x]) + sub_dp_sum))
  sub_dp_sum += dp[x]
  sub_dp_sum %= MOD

print(dp[0])
