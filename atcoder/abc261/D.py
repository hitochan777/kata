from collections import defaultdict


N, M = (int(x) for x in input().split())
X = list(int(x) for x in input().split())
B = defaultdict(int)
for _ in range(M):
  C, Y = (int(x) for x in input().split())
  B[C] = Y

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, N+1)

for i in range(N):
  dp[i+1][0] = max(dp[i])
  for c in range(1,min(i+2, N+1)):
    dp[i+1][c] = dp[i][c-1] + B[c] + X[i]

print(max(dp[N]))