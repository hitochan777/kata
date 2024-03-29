N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

def make_array(*args):
  if len(args) == 0:
    return -10**20

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, M+1)
max_val = A[0] 
for i in range(N):
  max_val = max(max_val, A[i])
  dp[i+1][1] = max_val

for i in range(N):
  for j in range(2, M+1):
    dp[i+1][j] = max(dp[i][j], dp[i][j-1] + j * A[i])

print(max(dp[i][M] for i in range(N+1)))