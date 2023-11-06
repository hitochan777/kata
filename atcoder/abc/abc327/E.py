N = int(input())

INF = 10**18
P = list(int(x) for x in input().split())
dp = [[-INF] * (N+1) for _ in range(N+1)]
for i in range(N+1):
  dp[i][0] = 0

for i in range(1, N+1):
  for j in range(1, i+1):
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] * 0.9 + P[i-1])

# print(dp)
ans = -INF
for k in range(1, N+1):
  R = dp[N][k] / sum(0.9 ** (k-i) for i in range(1, k+1)) - 1200 / (k**0.5)
  ans = max(ans, R)

print(ans)
