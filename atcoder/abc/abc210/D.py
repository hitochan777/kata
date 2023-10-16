H, W, C = list(int(x) for x in input().split())

INF = 10**18
A = []
for _ in range(H):
  A.append(list(int(x) for x in input().split()))

min_val = INF
for _ in range(2):
  dp = [[INF] * (W+1) for _ in range(H+1)]
  for i in range(1, H+1):
    for j in range(1, W+1):
      dp[i][j] = min(dp[i-1][j] + C, dp[i][j-1] + C, A[i-1][j-1])
      min_val = min(min_val, min(dp[i-1][j] + C + A[i-1][j-1], dp[i][j-1] + C + A[i-1][j-1]))
  
  A = list(reversed(A))

print(min_val)