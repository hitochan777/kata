from collections import defaultdict
def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

N, M, K, S, T, X = (int(x) for x in input().split())
S, T, X = S-1, T-1, X-1
MOD = 998244353 
g = defaultdict(list)
for _ in range(M):
  U, V = (int(x)-1 for x in input().split())
  g[U].append(V)
  g[V].append(U)

dp = make_array(K+1, N, 2)
dp[0][S][0] = 1
for k in range(K):
  for n in range(N):
    for d in range(2):
      idx = (d+1)%2 if n == X else d
      for nb in g[n]:
        dp[k+1][n][d] += dp[k][nb][idx]

      dp[k+1][n][d] %= MOD

print(dp[K][T][0])