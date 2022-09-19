N, M = (int(x) for x in input().split())
MOD = 998244353

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

if N > 60:
  print(0)
  exit()

ans = 0
l = len(bin(M))-2
res = (M & ((1 << (l-1)) - 1)) + 1
dp = make_array(N+1, l+1)
dp[0][0] = 1
for i in range(N):
  for j in range(1, l+1):
    tmp = 0
    for k in range(j):
      tmp += dp[i][k]
      tmp %= MOD

    mul = res if j == l else 1<<(j-1)
    dp[i+1][j] = (tmp * mul) % MOD

# print(dp)
print(sum(dp[N]) % MOD)