N, K = (int(x) for x in input().split())
H = list(int(x) for x in input().split())
dp = [10**18] * N 
dp[0] = 0
for i in range(N):
  for j in range(i+1,min(i+K+1,N)):
    dp[j] = min(dp[i] + abs(H[i]-H[j]), dp[j])

print(dp[N-1])