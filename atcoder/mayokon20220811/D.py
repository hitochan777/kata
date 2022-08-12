H, N = (int(x) for x in input().split())
A = []
B = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  A.append(a)
  B.append(b)

dp = [[10**18]*(H+1) for _ in range(N+1)]
dp[0][H] = 0
for i in range(N):
  for j in range(H, -1, -1):
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    dp[i+1][max(j-A[i], 0)] = min(dp[i+1][max(j-A[i], 0)], dp[i+1][j] + B[i])

print(dp[N][0])