import numpy as np

INF = 10**18
N, M = (int(x) for x in input().split())
C = []
P = []
S = []
for _ in range(N):
  c, p, *s = (int(x) for x in input().split())
  C.append(c)
  P.append(P)
  S.append(S)

dp = np.full((N + 1, M + 1), INF)
dp[0][0] = 0

for i in range(N):
  Pi, Si = roulette[i - 1]
  for j in range(M):
        for k in range(Pi + 1):
            if j - k >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + k * C[i - 1])
                for s in Si:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + s)

result = np.min(dp[N][M:])
print(result)