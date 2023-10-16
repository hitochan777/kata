N, M, K = (int(x) for x in input().split())
MOD = 998244353

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

if K == 0:
  total = M
  for i in range(N-1):
    total *= M
    total %= MOD

  print(total)
  exit()

dp = make_array(N+1, M+1)
for m in range(1,M+1):
  dp[1][m] = 1

for n in range(2,N+1):
  acc = [dp[n-1][0]]
  for i in range(1,M+1):
    acc.append(acc[-1] + dp[n-1][i])


  for m in range(1, M+1):
    dp[n][m] += acc[M] - acc[max(min(M, m+K-1), 1)]
    # print(n, m, dp[n][m])
    dp[n][m] += acc[max(m-K, 0)] - acc[0]
    # print(n, m, dp[n][m])
    dp[n][m] %= MOD

total = 0
for val in dp[N]:
  total += val
  total %= MOD

print(total)