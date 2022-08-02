N = int(input())
dp = [[0]*3 for _ in range(N+1)]
for i in range(N):
  score = [int(x) for x in input().split()]
  for j in range(3):
    dp[i+1][j] = max(dp[i][(j+1)%3], dp[i][(j+2)%3]) + score[j]

print(max(dp[N]))