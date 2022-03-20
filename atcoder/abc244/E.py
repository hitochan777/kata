from collections import defaultdict
MOD = 998244353
N, M, K, S, T, X = (int(x) for x in input().split())
S -= 1
T -= 1
X -= 1
g = defaultdict(list)
for _ in range(M):
  U, V = (int(x) for x in input().split())
  U, V = U-1, V-1
  g[U].append(V)
  g[V].append(U)

  def make_array(*args):
    if len(args) == 0:
      return 0 
  
    return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(K+1,N,2)
dp[0][S][0] = 1

for i in range(K):
  for j in range(N):
    for x in range(2):
      if j == X:
        dp[i+1][X][1-x] += sum(dp[i][k][x] for k in g[X])
        dp[i+1][X][1-x] %= MOD
      else:
        dp[i+1][j][x] += sum(dp[i][k][x] for k in g[j])
        dp[i+1][j][x] %= MOD

print(dp[K][T][0])