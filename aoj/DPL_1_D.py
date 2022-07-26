N = int(input())
dp = [1] * (N+1)
A = []
for _ in range(N):
  a = int(input())
  A.append(a)

for i in range(1,N):
  dp[i+1] = max(dp[j+1] + 1 if A[j] < A[i] else 1 for j in range(i))

print(max(dp))
