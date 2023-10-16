N = int(input())
A = list(int(x) for x in input().split())

B = [0]
for i in range(1,N+1):
  B.append(A[(i+1)//2-1] + B[-1])

dp = [0] * (N+1)
for i in range(1,N+1):
  for j in range(i):
    dp[i] = max(dp[i], dp[j] + B[i-j-1])

print(dp[N])