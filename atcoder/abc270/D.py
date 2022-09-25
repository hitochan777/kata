N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(2, N+1)

for i in range(2):
  for j in range(N+1):
    for k in range(K):
      if N - j >= A[k]:
        dp[i][j] = max(dp[i][j], dp[(i+1)%2][j-A[k]] + A[k])

print(dp[0])
print(dp[1])
print(dp[1][N])
