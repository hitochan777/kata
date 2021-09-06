N = int(input())
A = list(int(x) for x in input().split())

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]

dp = make_array(2 * N, 2 * N, default=lambda: 1<<30)
for i in range(2 * N - 1):
  dp[i][i+1] = abs(A[i] - A[i+1])

for w in range(3, 2*N+1, 2):
  for i in range(2*N-w):
    l, r = i, i+w
    for j in range(r):
      dp[l][r] = min(dp[l][r], dp[l][j] + dp[j+1][r])
    
    dp[l][r] = min(dp[l][r], dp[l+1][r-1] + abs(A[l] - A[r]))

print(dp[0][2*N-1])
