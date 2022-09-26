N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

dp = [0] * (N+1)
dp[1] = 1

for i in range(N):
  dp[i+1] = max(a + i + 1 - a - dp[i+1-a] for a in A if a <= i+1)

print(dp[N])
