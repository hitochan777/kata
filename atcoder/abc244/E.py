MOD = 998244353
N, M, K, S, T, X = (int(x) for x in input().split())
S -= 1
T -= 1
X -= 1
edges = []
for _ in range(M):
  U, V = (int(x) for x in input().split())
  U, V = U-1, V-1
  edges.append((U,V))

def make_array(*args):
  if len(args) == 0:
    return 0 

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(2,K+1,N)
dp[0][0][S] = 1

for i in range(K):
  for u, v in edges:
    for x in range(2):
      dp[x][i+1][v] += dp[x ^ (v == X)][i][u]
      dp[x][i+1][v] %= MOD
      dp[x][i+1][u] += dp[x ^ (u == X)][i][v]
      dp[x][i+1][u] %= MOD

print(dp[0][K][T])