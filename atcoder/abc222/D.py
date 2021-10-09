def make_array(*args, default=int):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
MAX = max(max(A), max(B))

MOD = 998244353
dp = make_array(N+1, MAX+1)
dp[0][0] = 1

for i in range(N):
  total = 0
  for j in range(MAX+1):
    total = (total + dp[i][j]) % MOD
    # print(i, j, A[i], B[i])
    if j < A[i] or j > B[i]:
      dp[i+1][j] = 0
      continue

    dp[i+1][j] = total

# print(dp)
print(sum(dp[N]) % MOD)
  