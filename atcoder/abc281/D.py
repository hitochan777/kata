N, K, D = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

def make_array(*args):
  if len(args) == 0:
    return -1

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, K+1, D)
for i in range(N+1):
  dp[i][0][0] = 0

for i in range(N):
  for k in range(1,K+1):
    for d in range(D):
      if dp[i][k][d] >= 0:
        dp[i+1][k][d] = dp[i][k][d]

      if dp[i][k-1][(d-A[i]+D)%D] >= 0:
        dp[i+1][k][d] = max(dp[i+1][k][d],dp[i][k-1][(d-A[i]+D)%D]+A[i])

# for row in dp:
#   print(row)

print(dp[N][K][0])
