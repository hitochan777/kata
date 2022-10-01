N = int(input())
A = list(int(x) for x in input().split())

dp = [0] * (N+1)

for i in range(N):
  if i == 0:
    dp[i+1] = A[i]
  if i == 1:
    dp[i+1] = dp[i-1] + A[i]
  else:
    dp[i+1] = max(dp[i-1], dp[i-2]) + A[i]

# print(dp)
print(max(dp[N],dp[N-1]))
